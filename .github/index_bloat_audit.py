"""
Index-bloat audit for code-cogito.com (Yoast sitemap).

WordPress + Yoast hands Google a set of XML sitemaps. The *post* sitemaps list
the articles you actually wrote. The *tag / category / author* sitemaps list
auto-generated archive pages — many of them empty shells or near-duplicates of
each other. When those archive pages outnumber (or drown) your real posts in
Google's view, that's "index bloat", and it dilutes the crawl budget and the
topical clarity of the site.

This tool reads the public sitemap index and reports the breakdown:

    posts        <- your real articles (good)
    tags         <- archive pages (bloat candidate)
    categories   <- archive pages (usually keep a few)
    authors      <- archive pages (bloat candidate)

Run it BEFORE the Yoast fix to see how many tag pages are being served, and
AGAIN a few days after flipping "Show Tags in search results" to Off — the tag
sitemap should vanish from the index (or empty out). That's your proof the
cleanup landed.

No WordPress credentials needed — sitemaps are public.

Usage:
    python index_bloat_audit.py                 # summary breakdown
    python index_bloat_audit.py --list          # also list every archive URL
    python index_bloat_audit.py --check-empty    # fetch each tag/category page
                                                  # and flag the empty ones
                                                  # (slower; best-effort)
    python index_bloat_audit.py --report         # for CI: write a baseline
                                                  # (index_bloat_state.json) and a
                                                  # GitHub step summary; used by the
                                                  # daily workflow to alert on change
"""

import json
import os
import re
import socket
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from xml.etree import ElementTree as ET

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SITEMAP_INDEX = "https://code-cogito.com/sitemap_index.xml"
TIMEOUT = 20
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Baseline written by --report so the daily workflow can detect changes.
STATE_PATH = Path(__file__).parent / "index_bloat_state.json"
TRACKED_KINDS = ("posts", "pages", "categories", "tags", "authors")

# Phrases Yoast / common themes render on an archive page that has no posts.
# Multilingual because the site publishes ZH / EN / JA.
EMPTY_MARKERS = (
    "it seems we can't find",
    "it seems we cant find",
    "nothing found",
    "no posts found",
    "找不到",
    "沒有找到",
    "見つかりませんでした",
    "見つかりません",
)


# ---------------------------------------------------------------------------
# Network (mirrors update_readme.py: browser UA + forced IPv4 + retry, because
# Hostinger's LiteSpeed WAF blocks bot-flavored datacenter requests)
# ---------------------------------------------------------------------------
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/xml,text/xml,text/html,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

_orig_getaddrinfo = socket.getaddrinfo


def _ipv4_only_getaddrinfo(*args, **kwargs):
    res = _orig_getaddrinfo(*args, **kwargs)
    return [r for r in res if r[0] == socket.AF_INET] or res


socket.getaddrinfo = _ipv4_only_getaddrinfo


def fetch_url(url: str, retries: int = 3) -> str:
    """GET with browser headers and exponential-backoff retry on network errors."""
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(url, headers=BROWSER_HEADERS)
            with urlopen(req, timeout=TIMEOUT) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except (URLError, HTTPError, socket.timeout) as e:
            last_err = e
            if attempt < retries:
                wait = 2 ** attempt  # 2s, 4s
                print(f"  retry {attempt}/{retries} after {wait}s ({e})")
                time.sleep(wait)
    raise URLError(f"giving up after {retries} attempts: {last_err}")


# ---------------------------------------------------------------------------
# Parsing (pure functions — no network, so they're unit-testable)
# ---------------------------------------------------------------------------
def parse_sitemap_index(xml: str) -> list:
    """Return the list of sub-sitemap URLs from a <sitemapindex> document."""
    root = ET.fromstring(xml)
    locs = []
    for loc in root.findall("sm:sitemap/sm:loc", NS):
        if loc.text:
            locs.append(loc.text.strip())
    return locs


def parse_urlset(xml: str) -> list:
    """Return the list of page URLs from a <urlset> document."""
    root = ET.fromstring(xml)
    urls = []
    for loc in root.findall("sm:url/sm:loc", NS):
        if loc.text:
            urls.append(loc.text.strip())
    return urls


def classify_sitemap(loc: str) -> str:
    """Map a sub-sitemap URL to a kind label based on its Yoast filename.

    Yoast names sitemaps `<thing>-sitemap.xml` (post, page, category,
    post_tag, author, ...), paginating large ones as `<thing>-sitemap1.xml`.
    """
    name = loc.rsplit("/", 1)[-1]
    name = name.split("?", 1)[0]
    prefix = re.split(r"-sitemap", name, maxsplit=1)[0]
    prefix = prefix.rstrip("0123456789").lower()
    if prefix in ("post",):
        return "posts"
    if prefix in ("page",):
        return "pages"
    if prefix in ("category", "product_cat"):
        return "categories"
    if prefix in ("post_tag", "tag", "product_tag"):
        return "tags"
    if prefix in ("author", "author_user"):
        return "authors"
    return f"other:{prefix}" if prefix else "other"


# Which kinds are auto-generated archive pages (the bloat suspects).
ARCHIVE_KINDS = ("tags", "categories", "authors")


def looks_empty(html: str) -> bool:
    # WordPress's wptexturize turns straight apostrophes into curly ones in
    # rendered text, so normalize before matching the EMPTY_MARKERS.
    low = html.lower().replace("’", "'").replace("‘", "'")
    return any(marker in low for marker in EMPTY_MARKERS)


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------
def audit(list_urls: bool, check_empty: bool):
    """Run the audit. Returns (counts dict, reachable bool)."""
    print("Code & Cogito — Index Bloat Audit")
    print("=" * 60)
    print(f"Sitemap index: {SITEMAP_INDEX}\n")

    try:
        idx_xml = fetch_url(SITEMAP_INDEX)
        sub_sitemaps = parse_sitemap_index(idx_xml)
    except (URLError, HTTPError, ET.ParseError) as e:
        print(f"ERROR: could not read sitemap index: {e}")
        print("(If you're on a network that blocks the site, run this from a"
              " machine that can reach code-cogito.com.)")
        return {}, False

    if not sub_sitemaps:
        print("No sub-sitemaps found in the index.")
        return {}, True

    print(f"Found {len(sub_sitemaps)} sub-sitemap(s):\n")

    counts = {}
    archive_urls = {}  # kind -> list of page URLs

    for sub in sub_sitemaps:
        kind = classify_sitemap(sub)
        try:
            urls = parse_urlset(fetch_url(sub))
        except (URLError, HTTPError, ET.ParseError) as e:
            print(f"  WARN: skip {sub}: {e}")
            continue
        counts[kind] = counts.get(kind, 0) + len(urls)
        print(f"  [{kind:>12}] {len(urls):>4} url(s)  <-  {sub}")
        if kind in ARCHIVE_KINDS:
            archive_urls.setdefault(kind, []).extend(urls)

    # ---- summary -----------------------------------------------------------
    posts = counts.get("posts", 0)
    archive_total = sum(counts.get(k, 0) for k in ARCHIVE_KINDS)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("-" * 60)
    print(f"  Real article pages (posts):     {posts}")
    for k in ARCHIVE_KINDS:
        if k in counts:
            print(f"  Archive pages ({k}):{' ' * (15 - len(k))}{counts[k]}")
    print(f"  Archive pages handed to Google: {archive_total}")

    if posts:
        ratio = archive_total / posts
        print(f"  Archive-to-article ratio:       {ratio:.1f}x")
        if ratio >= 1:
            print("  -> Google is being handed at least as many auto-generated"
                  " archive pages as real articles. That's index bloat.")

    if counts.get("tags"):
        print("\n  ACTION: tag archives are still in the sitemap. After you set"
              "\n  Yoast > Settings > Categories & tags > Tags > 'Show Tags in"
              "\n  search results' to Off, re-run this — 'tags' should drop to 0.")
    else:
        print("\n  OK: no tag archives in the sitemap (Yoast tag noindex is"
              " working).")

    # ---- optional listings -------------------------------------------------
    if list_urls and archive_urls:
        print("\n" + "=" * 60)
        print("ARCHIVE PAGE URLS")
        for kind, urls in archive_urls.items():
            print(f"\n[{kind}] {len(urls)}")
            for u in sorted(urls):
                print(f"  {u}")

    if check_empty and archive_urls:
        print("\n" + "=" * 60)
        print("EMPTY-PAGE CHECK (best-effort; fetches each archive page)")
        empties = []
        for kind, urls in archive_urls.items():
            for u in sorted(urls):
                try:
                    html = fetch_url(u, retries=2)
                except (URLError, HTTPError, socket.timeout) as e:
                    print(f"  WARN: skip {u}: {e}")
                    continue
                if looks_empty(html):
                    empties.append(u)
                    print(f"  EMPTY  {u}")
        print(f"\n  {len(empties)} archive page(s) look empty and are safe to"
              " delete in WordPress (Posts > Tags, count = 0).")

    return counts, True


def _write_step_summary(lines: list) -> None:
    """Append a Markdown block to the GitHub Actions run summary, if running in CI."""
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def do_report(counts: dict, reachable: bool) -> None:
    """CI mode: persist a baseline and emit a run summary / change alert.

    The daily workflow commits index_bloat_state.json only when it changes, so
    a new commit (and the ::warning:: below) is the signal that the archive
    counts moved — e.g. tag pages dropping to 0 after the Yoast noindex fix.
    """
    if not reachable:
        print("\n[report] sitemap unreachable — baseline left unchanged, no alert.")
        _write_step_summary([
            "### Index bloat audit",
            "",
            "Sitemap was unreachable this run; baseline left unchanged, will retry.",
        ])
        return

    current = {k: counts.get(k, 0) for k in TRACKED_KINDS}

    prev = None
    if STATE_PATH.exists():
        try:
            prev = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            prev = None

    STATE_PATH.write_text(
        json.dumps(current, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    tags_now = current["tags"]
    tags_prev = prev.get("tags") if isinstance(prev, dict) else None

    summary = [
        "### Index bloat audit",
        "",
        f"- Real article pages (posts): **{current['posts']}**",
        f"- Tag archive pages: **{tags_now}**",
        f"- Category archive pages: **{current['categories']}**",
        f"- Author archive pages: **{current['authors']}**",
    ]
    if tags_prev is not None and tags_prev != tags_now:
        delta = tags_now - tags_prev
        direction = "up" if delta > 0 else "down"
        msg = (f"Tag archive pages changed: {tags_prev} -> {tags_now} "
               f"({direction} {abs(delta)})")
        summary += ["", f"**CHANGE — {msg}**"]
        print(f"::warning::{msg}")
    elif tags_now == 0:
        summary += ["", "Tag archives are out of the sitemap (Yoast noindex working)."]

    _write_step_summary(summary)
    print(f"\n[report] baseline written to {STATE_PATH.name} (tags={tags_now}).")


def main() -> int:
    list_urls = "--list" in sys.argv
    check_empty = "--check-empty" in sys.argv
    report = "--report" in sys.argv
    counts, reachable = audit(list_urls=list_urls, check_empty=check_empty)
    if report:
        do_report(counts, reachable)
    return 0


if __name__ == "__main__":
    sys.exit(main())
