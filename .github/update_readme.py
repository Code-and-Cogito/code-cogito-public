"""
Auto-update README.md with published article links (v2: sitemap-driven).

v1 relied on registry's `slug` field as ground truth and HEAD-requested it.
If the registry slug was wrong (a frequent reality — slugs are decided at
publish time, not at draft time), the HEAD always 404'd and no link was
ever added. S1 articles 05-12 silently failed this way for weeks.

v2 reads Yoast's public sitemap_index.xml as the single source of truth:
1. Walk sitemap_index → collect every published ZH article URL.
2. For each registry article:
   a. If registry slug appears in sitemap → use it.
   b. Else fuzzy-match title keywords against all sitemap slugs.
      If 2+ keywords overlap, use the best match and warn about drift.
   c. Else mark as not-yet-published.
3. Update README table rows.

No WordPress credentials needed — sitemap is public.

Usage:
    python update_readme.py           # Dry run
    python update_readme.py --apply   # Actually update README.md
"""

import json
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
REGISTRY_PATH = Path(__file__).parent / "article_registry.json"
README_PATH = Path(__file__).parent.parent / "README.md"
SITEMAP_INDEX = "https://code-cogito.com/sitemap_index.xml"
BASE_URL = "https://code-cogito.com"
TIMEOUT = 20
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Words that don't carry semantic load — skipped when matching title to slug.
STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "at", "and", "or", "to", "for",
    "vs", "with", "from", "into", "by", "as", "is", "are", "was", "were",
    "what", "when", "where", "why", "how", "did", "do", "does",
    "we", "our", "their", "his", "her", "its",
    "became", "becomes", "become", "rebel", "rebels", "new",
}


# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------
# Hostinger's LiteSpeed WAF returns Errno 101 (Network unreachable) when
# requests come from datacenter IPs with bot-flavored user agents. Pretend
# to be a real browser. Also force IPv4 because Azure-hosted GitHub runners
# sometimes resolve AAAA for Hostinger but the IPv6 path is dead-ended.
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/xml,text/xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Force IPv4 for getaddrinfo. Safe on GitHub-hosted Linux runners; on
# machines where the patch isn't desired (no AAAA in DNS) this is a no-op.
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
                return resp.read().decode("utf-8")
        except (URLError, HTTPError, socket.timeout) as e:
            last_err = e
            if attempt < retries:
                wait = 2 ** attempt  # 2s, 4s
                print(f"  retry {attempt}/{retries} after {wait}s ({e})")
                time.sleep(wait)
    raise URLError(f"giving up after {retries} attempts: {last_err}")


def fetch_all_zh_slugs() -> set:
    """Walk sitemap_index → all post-sitemaps → return set of ZH article slugs.

    ZH = root-level (no `/en/` or `/ja/` prefix).
    """
    slugs = set()
    try:
        idx_xml = fetch_url(SITEMAP_INDEX)
        idx_root = ET.fromstring(idx_xml)
    except (URLError, HTTPError, ET.ParseError) as e:
        print(f"  ERROR: Could not fetch sitemap index: {e}")
        return slugs

    for sm in idx_root.findall("sm:sitemap/sm:loc", NS):
        sub_url = sm.text
        if not sub_url or "post-sitemap" not in sub_url:
            # only post sitemaps (skip page/category/tag/author/mailpoet)
            continue
        try:
            sub_xml = fetch_url(sub_url)
            sub_root = ET.fromstring(sub_xml)
        except (URLError, HTTPError, ET.ParseError) as e:
            print(f"  WARN: skip {sub_url}: {e}")
            continue

        for loc in sub_root.findall("sm:url/sm:loc", NS):
            url = loc.text
            if not url:
                continue
            if "/en/" in url or "/ja/" in url:
                continue
            m = re.match(r"https://code-cogito\.com/([^/]+)/?$", url)
            if m:
                slugs.add(m.group(1))
    return slugs


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------
def title_keywords(title: str) -> set:
    """Lowercased keyword set from title, stopwords removed, length > 2."""
    words = re.findall(r"[a-zA-Z]+", title.lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 2}


def score_slug(keywords: set, slug: str) -> int:
    """Count title keywords appearing as substrings of the slug."""
    s = slug.lower()
    return sum(1 for w in keywords if w in s)


# Minimum title-keyword overlap to trust a fuzzy match. 2 was too loose
# (e.g. "Data Archaeology of the Industrial Revolution" wrongly matched
# S1's "industrial-revolution-machines-changed-everything" on just
# "industrial" + "revolution"). 3 forces a more topic-specific hit.
MIN_FUZZY_OVERLAP = 3


def resolve_slug(article: dict, candidate_slugs: set):
    """Return the actual published slug, or None if article isn't live."""
    registry_slug = article["slug"]
    if registry_slug in candidate_slugs:
        return registry_slug

    # Fall back to keyword fuzzy match (registry slug drifted from reality).
    kw = title_keywords(article["title"])
    if not kw:
        return None
    best_score = 0
    best_slug = None
    for slug in candidate_slugs:
        s = score_slug(kw, slug)
        if s > best_score:
            best_score = s
            best_slug = slug
    if best_score >= MIN_FUZZY_OVERLAP:
        if best_slug != registry_slug:
            print(
                f"  [DRIFT] registry slug '{registry_slug}' not in sitemap; "
                f"matched '{best_slug}' ({best_score} kw overlap) — "
                f"please update article_registry.json"
            )
        return best_slug
    return None


# ---------------------------------------------------------------------------
# README rewriting
# ---------------------------------------------------------------------------
def build_table_row(num: str, article: dict, published_slug):
    title = article["title"]
    code = article["code"]
    code_path = article["code_path"]
    if published_slug:
        url = f"{BASE_URL}/{published_slug}/"
        title_cell = f"[{title}]({url})"
    else:
        title_cell = title
    return f"| {num} | {title_cell} | [{code}]({code_path}) |"


def update_readme(registry: dict, all_zh_slugs: set, dry_run: bool = True) -> int:
    readme = README_PATH.read_text(encoding="utf-8")
    changes = 0

    # Mutable working set: once a slug is claimed by article N, remove it so
    # later articles can't fuzzy-match the same slug.
    candidates = set(all_zh_slugs)
    # Pre-claim any slugs already present in linked rows of the README, so a
    # later unlinked article doesn't steal them via fuzzy match.
    for series_data in registry["series"].values():
        for article in series_data["articles"].values():
            if article["slug"] in readme:
                candidates.discard(article["slug"])

    for series_key, series_data in registry["series"].items():
        for num, article in series_data["articles"].items():
            title = article["title"]
            code = article["code"]
            code_path = article["code_path"]

            # Already linked? skip.
            if f"| {num} | [{title}]" in readme:
                continue

            unlinked = (
                f"| {num} | {title} | [{code}]({code_path}) |"
            )
            if unlinked not in readme:
                continue  # row not present in README

            print(f"Checking: {series_key} #{num} '{title}'")
            slug = resolve_slug(article, candidates)
            if not slug:
                print("  [NOT YET] not published")
                continue

            new_row = build_table_row(num, article, slug)
            readme = readme.replace(unlinked, new_row, 1)
            candidates.discard(slug)  # don't let later articles steal it
            changes += 1
            print(f"  [PUBLISHED] -> {BASE_URL}/{slug}/")

    if changes > 0 and not dry_run:
        README_PATH.write_text(readme, encoding="utf-8")
        print(f"\n{'=' * 60}\nUPDATED: {changes} row(s) in README.md")
    elif changes > 0:
        print(
            f"\n{'=' * 60}\n"
            f"DRY RUN: {changes} row(s) would change. Use --apply to write."
        )
    else:
        print("\nNo changes needed.")
    return changes


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> int:
    apply = "--apply" in sys.argv
    print("Code & Cogito - README Link Updater (v2: sitemap-driven)")
    print("=" * 60)
    print(f"Mode: {'APPLY' if apply else 'DRY RUN'}")
    print(f"Sitemap: {SITEMAP_INDEX}\n")

    print("Fetching all published ZH slugs from sitemap...")
    all_zh = fetch_all_zh_slugs()
    print(f"  found {len(all_zh)} ZH article slug(s)\n")

    if not all_zh:
        # Graceful exit: sitemap unreachable today is annoying but not a
        # repository-state bug. Returning 0 means the workflow stays green
        # and just tries again on tomorrow's cron.
        print(
            "WARN: Could not load sitemap (network/firewall issue). "
            "Skipping this run; will retry tomorrow."
        )
        return 0

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    total = sum(len(s["articles"]) for s in registry["series"].values())
    print(f"Registry: {len(registry['series'])} series, {total} article(s)\n")

    update_readme(registry, all_zh, dry_run=not apply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
