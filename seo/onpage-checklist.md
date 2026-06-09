# Per-Article On-Page SEO Checklist

Run this before hitting **Publish** on *each language version* of an article.
Keep it open in a second tab while editing in WordPress.

## Title & metadata
- [ ] **SEO title** set in Yoast, keyword-first, ≤ ~60 Latin / ~30 CJK chars,
      ends `| Code & Cogito` (see `meta-tags.md`).
- [ ] **Meta description** unique to this language, ~140–155 Latin / ~70–80 CJK
      chars, with a click reason (data/finding/code).
- [ ] **URL slug** short, lowercase, keyword-bearing, no stop-words. (en/ja use
      the `-en` / `-ja` convention.)
- [ ] **Yoast focus keyphrase** set; green/orange, not red.

## Content structure
- [ ] Exactly **one `<h1>`** = the on-page headline (not the SEO title verbatim).
- [ ] Logical **H2/H3** hierarchy; primary keyphrase in the first H2.
- [ ] Keyphrase appears in the **first 100 words** naturally.
- [ ] Intro answers "what will I learn / what's the finding" within 2–3 lines
      (above the fold) — critical for JP/TW mobile readers.
- [ ] Scannable: short paragraphs, bullets, a key-findings callout.
- [ ] ≥ ~800–1,000 words of substantive content (your explainers easily clear
      this) — but quality over padding.

## Multilingual
- [ ] This version **linked to its zh/en/ja siblings** in the multilingual
      plugin (Polylang/WPML) so hreflang emits.
- [ ] **hreflang** block present (3 + `x-default`) — view source to confirm.
- [ ] **Canonical** points to this page itself, in this language.
- [ ] **`<html lang>`** correct (`zh-Hant-TW` / `en` / `ja`).
- [ ] Crawlable **language switcher** present (real `<a href>`).

## Images (you ship several charts per post)
- [ ] Descriptive filename (e.g. `florence_network_basic.png`).
- [ ] **Localized `alt`** describing the chart, in this page's language.
- [ ] Compressed / WebP; explicit `width`/`height`; lazy-loaded if below fold.
- [ ] Lead/feature image set (used by Open Graph + Article schema `image`).

## Structured data & social
- [ ] **Article** + **BreadcrumbList** JSON-LD valid, `inLanguage` correct.
- [ ] **Open Graph**: `og:title`, `og:description`, `og:image` (≥1200×630),
      `og:locale` (`zh_TW` / `en_US` / `ja_JP`), `og:locale:alternate` for the
      others.
- [ ] **Twitter card** = `summary_large_image`.
- [ ] Rich Results Test passes for this URL.

## Internal & external links
- [ ] Links to the **series hub** + 2–4 sibling articles **in this language**.
- [ ] Link to **Deep Dive Pack** (`/products/`) where relevant.
- [ ] Link to the **GitHub code** for this article (you already do — keep it;
      it adds credibility/E-E-A-T).
- [ ] Descriptive anchor text (not "here"/"click").

## Pre-publish & post-publish
- [ ] Preview on **mobile** — TW & JP traffic is mobile-first.
- [ ] No broken links (esp. the cross-language and GitHub links).
- [ ] After publish: **URL Inspection** in Search Console → *Request indexing*
      for the new URL (do this per language).
- [ ] Add the new translation set to `hreflang-multilingual.md`'s map.
- [ ] 2–4 weeks later: review CTR & position per country; iterate the title.

## E-E-A-T (trust signals — matters across all markets)
- [ ] Visible **author** (Wina) with a link to an About page describing the
      ocean-physics / cross-disciplinary background.
- [ ] Published & updated dates shown.
- [ ] Sources/references cited where you state historical figures or data.
- [ ] Working, reproducible **code link** — a genuine differentiator that
      signals expertise to both readers and Google.
