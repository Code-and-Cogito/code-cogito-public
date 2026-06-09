# Code & Cogito — SEO Toolkit (Taiwan · Japan · Europe/US)

This folder is a **ready-to-apply SEO playbook** for the Code & Cogito blog
([code-cogito.com](https://code-cogito.com)), targeting three Google markets:

| Market | Language | Locale | URL prefix | Primary Google property |
|--------|----------|--------|------------|--------------------------|
| 🇹🇼 Taiwan | Traditional Chinese | `zh-TW` | `/` (root, default) | google.com.tw |
| 🇯🇵 Japan | Japanese | `ja-JP` | `/ja/…-ja/` | google.co.jp |
| 🇪🇺🇺🇸 Europe/US | English | `en` (`en-US`) | `/en/…-en/` | google.com |

> ℹ️ **Why this lives in the code repo, not the site.** The blog is a
> **WordPress** site (Yoast SEO + a multilingual plugin, hosted on
> Hostinger/LiteSpeed). The site source is not in this repository, so these
> files are *instructions and copy-paste assets* you apply inside WordPress —
> not code that auto-deploys. Each file says exactly where to paste it.

## How to use this toolkit (priority order)

Work top-down. The first three items move the needle fastest for a
multilingual site.

1. **[`hreflang-multilingual.md`](./hreflang-multilingual.md)** — make sure
   Google knows your zh-TW / en / ja pages are translations of each other.
   This is the #1 fix for a 3-market site; without it the versions compete
   and dilute each other.
2. **[`meta-tags.md`](./meta-tags.md)** — paste optimized SEO titles & meta
   descriptions (all three languages) for every published article + the home,
   products and series pages.
3. **[`technical-seo.md`](./technical-seo.md)** — sitemaps, `robots.txt`,
   Search Console setup per market, Core Web Vitals on LiteSpeed, image SEO.
4. **[`structured-data.md`](./structured-data.md)** — JSON-LD schema
   (Organization, WebSite + Sitelinks Search Box, Article, Breadcrumb, FAQ).
5. **[`keyword-strategy.md`](./keyword-strategy.md)** — the search terms each
   market actually types, mapped to your articles, plus content-gap ideas.
6. **[`onpage-checklist.md`](./onpage-checklist.md)** — a per-article QA
   checklist to run before hitting *Publish* in any language.

## The 10 highest-impact actions (TL;DR)

1. ✅ Add reciprocal **`hreflang`** tags linking zh-TW ⇄ en ⇄ ja for every
   translated page, plus `x-default` → the zh-TW (canonical) version.
2. ✅ Give every page a **self-referencing canonical** in its own language
   (Yoast does this — verify it isn't pointing cross-language).
3. ✅ Rewrite **SEO titles** to lead with the keyword + a benefit, ≤ ~60 Latin
   chars / ~30 CJK chars (see `meta-tags.md`).
4. ✅ Write a **unique meta description** per language (don't auto-translate
   one into all three — search intent differs by market).
5. ✅ Register **all three language trees** in Google Search Console and set
   **International Targeting** where relevant; submit `sitemap_index.xml`.
6. ✅ Add **Article + BreadcrumbList JSON-LD** with the correct `inLanguage`
   per version.
7. ✅ Add a visible, crawlable **language switcher** (real `<a href>` links,
   not JS-only) on every article.
8. ✅ Fix **image SEO**: descriptive filenames + localized `alt` text on every
   chart (`.png`) — your posts are chart-heavy, this wins Google Images.
9. ✅ Build **internal links** within each series and language (silo by
   series; never link zh→en mid-article — keep readers in-language).
10. ✅ Improve **Core Web Vitals**: enable LiteSpeed Cache, lazy-load images,
    preload fonts, serve WebP. Mobile-first matters most in TW & JP.

## Measuring success

- **Search Console** (per market): impressions, average position, and CTR by
  query — track separately for `/`, `/en/`, `/ja/`.
- **CTR** is the fastest signal that a new title/description works — watch it
  per page for 2–4 weeks after each change.
- **Indexed pages**: confirm all three language versions are indexed (URL
  Inspection). A common multilingual bug is only the default language getting
  indexed.

---

**Code & Cogito** — Decoding history through code. Understanding philosophy
through data.
