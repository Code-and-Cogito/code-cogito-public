"""
Auto-update README.md with published article links.

Makes HEAD requests to check which blog articles are live, then updates
the README table rows to include clickable links for published articles.

Usage:
    python update_readme.py           # Dry run - show what would change
    python update_readme.py --apply   # Actually update README.md

Designed to run in GitHub Actions on a daily schedule.
No WordPress credentials needed - just checks if the URL returns 200.
"""

import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REGISTRY_PATH = Path(__file__).parent / "article_registry.json"
README_PATH = Path(__file__).parent / "README.md"
TIMEOUT = 15  # seconds per request


def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def check_article_published(slug: str) -> str | None:
    """
    Check if a blog post is live by making a HEAD request to its URL.
    Returns the URL if it responds 200, None otherwise.

    Uses the Chinese (default language) blog URL.
    """
    article_url = f"https://code-cogito.com/{slug}/"
    try:
        req = Request(
            article_url,
            method="HEAD",
            headers={"User-Agent": "CodeCogito-ReadmeUpdater/1.0"},
        )
        with urlopen(req, timeout=TIMEOUT) as resp:
            if resp.status == 200:
                return article_url
    except HTTPError as e:
        if e.code == 404:
            return None  # Not published yet, expected
        print(f"  Warning: HTTP {e.code} for '{slug}'")
    except URLError as e:
        print(f"  Warning: Could not reach '{slug}': {e}")
    return None


def build_table_row(num: str, article: dict, published_url: str | None) -> str:
    """Build a markdown table row for an article."""
    title = article["title"]
    code = article["code"]
    code_path = article["code_path"]

    if published_url:
        title_cell = f"[{title}]({published_url})"
    else:
        title_cell = title

    return f"| {num} | {title_cell} | [{code}]({code_path}) |"


def update_readme(registry: dict, dry_run: bool = True) -> int:
    """
    Read README.md, find article table rows, update links for published articles.
    Returns the number of changes made.
    """
    readme_text = README_PATH.read_text(encoding="utf-8")
    changes = 0

    for series_key, series_data in registry["series"].items():
        articles = series_data["articles"]

        for num, article in articles.items():
            title = article["title"]
            code = article["code"]
            slug = article["slug"]

            # Check if this article already has a link in README
            linked_marker = f"| {num} | [{title}]"
            if linked_marker in readme_text:
                continue  # Already linked

            # Check if this article exists in README but without a link
            unlinked_pattern = f"| {num} | {title} |"
            if unlinked_pattern not in readme_text:
                continue  # Row not in README

            # This article is in README but not linked - check if published
            print(f"Checking: {series_key} #{num} (slug: {slug})...")
            published_url = check_article_published(slug)

            if published_url:
                print(f"  [PUBLISHED] {published_url}")
                new_row = build_table_row(num, article, published_url)

                old_row = (
                    f"| {num} | {title} | "
                    f"[{code}]({article['code_path']}) |"
                )
                if old_row in readme_text:
                    readme_text = readme_text.replace(old_row, new_row, 1)
                    changes += 1
                else:
                    print(f"  Warning: Could not find exact row for #{num}")
            else:
                print(f"  [NOT YET] Not published")

    if changes > 0:
        if dry_run:
            print(f"\n{'='*60}")
            print(f"DRY RUN: {changes} article(s) would be updated.")
            print(f"Run with --apply to actually update README.md")
        else:
            README_PATH.write_text(readme_text, encoding="utf-8")
            print(f"\n{'='*60}")
            print(f"UPDATED: {changes} article(s) linked in README.md")
    else:
        print(f"\nNo changes needed - all published articles already linked.")

    return changes


def main():
    apply = "--apply" in sys.argv

    print("Code & Cogito - README Link Updater")
    print("=" * 60)
    print(f"Mode: {'APPLY' if apply else 'DRY RUN'}")
    print()

    registry = load_registry()
    total_articles = sum(
        len(s["articles"]) for s in registry["series"].values()
    )
    print(f"Registry: {len(registry['series'])} series, {total_articles} articles")
    print()

    changes = update_readme(registry, dry_run=not apply)
    return 0 if changes >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
