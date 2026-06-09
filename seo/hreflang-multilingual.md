# Hreflang & Multilingual SEO

> **Apply in:** WordPress `<head>` of every translated page. If you use
> **Polylang** or **WPML**, hreflang is emitted automatically once
> translations are linked — your job is to *verify* it (see QA below). If
> tags are missing, add them via your multilingual plugin or with a small
> `wp_head` snippet / Yoast filter.

This is the single most important fix for a three-market site. Without correct
`hreflang`, Google may treat your zh-TW, English and Japanese pages as
duplicate/competing content, index only one, or show the wrong language to the
wrong country.

## The rules

1. **Reciprocal & complete.** Every page in a translation set must list **all**
   versions, *including itself* (self-referential). zh ↔ en ↔ ja — all three,
   on all three.
2. **One `x-default`.** Point it at the page you want shown to users whose
   language/region you don't explicitly target. Use the **zh-TW** (root) URL,
   since that's your canonical default.
3. **Use the right codes.** `zh-Hant` (or `zh-TW`) for Traditional Chinese,
   `ja` for Japanese, `en` for English. Don't use `zh` alone (that's ambiguous
   with Simplified) and don't use `zh-CN`.
4. **Absolute URLs, with trailing slash**, matching exactly how the page
   resolves (your site uses trailing slashes).
5. **Canonical stays in-language.** Each page's `rel="canonical"` points to
   **itself**, never to another language. (hreflang handles the relationship;
   canonical handles duplicates *within* one language.)

## The tag block

Put this identical block in the `<head>` of **all three** versions of an
article. Example for *Why Florence Became the Cradle of the Renaissance*:

```html
<link rel="alternate" hreflang="zh-Hant" href="https://code-cogito.com/florence-renaissance-cradle/" />
<link rel="alternate" hreflang="en"      href="https://code-cogito.com/en/florence-renaissance-cradle-en/" />
<link rel="alternate" hreflang="ja"      href="https://code-cogito.com/ja/florence-renaissance-cradle-ja/" />
<link rel="alternate" hreflang="x-default" href="https://code-cogito.com/florence-renaissance-cradle/" />
```

Also add the homepage set:

```html
<link rel="alternate" hreflang="zh-Hant" href="https://code-cogito.com/" />
<link rel="alternate" hreflang="en"      href="https://code-cogito.com/en/home-en/" />
<link rel="alternate" hreflang="ja"      href="https://code-cogito.com/ja/home-ja/" />
<link rel="alternate" hreflang="x-default" href="https://code-cogito.com/" />
```

## Full alternate-URL map (published articles)

These are the live translation sets. **Series 1** URLs are verified against the
repo's article READMEs. For **Series 2 & 3** the zh-TW URL is verified; fill the
`en`/`ja` columns from your **Yoast sitemap** (`/en/post-sitemap.xml`,
`/ja/post-sitemap.xml`) — published English slugs are *not* always
`{zh-slug}-en` (e.g. "humanism" → `humanism-the-birth-of-human-dignity-en`), so
copy the exact slug rather than guessing.

### Series 1 — Renaissance (verified)

| # | zh-Hant (x-default) | en | ja |
|---|---------------------|----|----|
| 01 | `/florence-renaissance-cradle/` | `/en/florence-renaissance-cradle-en/` | `/ja/florence-renaissance-cradle-ja/` |
| 02 | `/medici-family-cultural-investment/` | `/en/medici-family-cultural-investment-en/` | `/ja/medici-family-cultural-investment-ja/` |
| 03 | `/da-vinci-anatomy-revolution/` | `/en/da-vinci-anatomy-revolution-en/` | `/ja/da-vinci-anatomy-revolution-ja/` |
| 04 | `/perspective-math-changed-art/` | `/en/perspective-math-changed-art-en/` | `/ja/perspective-math-changed-art-ja/` |
| 05 | `/humanism-birth-renaissance/` | `/en/humanism-the-birth-of-human-dignity-en/` | `/ja/humanism-birth-renaissance-ja/` |
| 06 | `/printing-press-knowledge-revolution/` | `/en/printing-press-knowledge-revolution-en/` | `/ja/printing-press-knowledge-revolution-ja/` |
| 07 | `/reformation-authority-challenged/` | `/en/reformation-authority-challenged-en/` | `/ja/reformation-authority-challenged-ja/` |
| 08 | `/enlightenment-age-of-reason/` | `/en/enlightenment-age-of-reason-en/` | `/ja/enlightenment-age-of-reason-ja/` |
| 09 | `/romanticism-poets-vs-philosophers/` | `/en/romanticism-poets-vs-philosophers-en/` | `/ja/romanticism-poets-vs-philosophers-ja/` |
| 10 | `/industrial-revolution-machines-changed-everything/` | `/en/the-industrial-revolution-when-machines-changed-everything-en/` | `/ja/industrial-revolution-machines-changed-everything-ja/` |
| 11 | `/darwin-evolution-philosophical-shock/` | `/en/darwin-evolution-philosophical-shock-en/` | `/ja/darwin-evolution-philosophical-shock-ja/` |
| 12 | `/renaissance-legacy-500-years-2/` | `/en/renaissance-legacy-500-years-en/` | `/ja/renaissance-legacy-500-years-ja/` |

### Series 2 — Industrial & Data Revolution (zh-TW verified; fill en/ja from sitemap)

| # | zh-Hant (x-default) | en | ja |
|---|---------------------|----|----|
| 01 | `/steam-engine-vs-cloud-computing/` | `/en/…-en/` | `/ja/…-ja/` |
| 02 | `/factory-discipline-vs-platform-algorithms-2/` | `/en/…-en/` | `/ja/…-ja/` |
| 03 | `/labor-alienation-marx-to-algorithms-2/` | `/en/…-en/` | `/ja/…-ja/` |
| 04 | `/data-archaeology-python-industrial-revolution-2/` | `/en/…-en/` | `/ja/…-ja/` |
| 05 | `/child-labor-vs-algorithmic-bias/` | `/en/…-en/` | `/ja/…-ja/` |

### Series 3 — Quantum × Eastern Philosophy (zh-TW verified; fill en/ja from sitemap)

| # | zh-Hant (x-default) | en | ja |
|---|---------------------|----|----|
| 01 | `/quantum-revolution-newton-universe-collapse/` | `/en/…-en/` | `/ja/…-ja/` |
| 02 | `/copenhagen-interpretation-vs-kyoto-school/` | `/en/…-en/` | `/ja/…-ja/` |

> Series 3 articles 03–12, Series 5, and Series 6 are scheduled for
> 2026 — add their rows here as each goes live.

## Language switcher (crawlable)

Each article needs a **real anchor-tag** switcher so Google can discover the
other languages even if it ignores hreflang:

```html
<nav class="lang-switcher" aria-label="Language">
  <a href="https://code-cogito.com/florence-renaissance-cradle/" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a>
  <a href="https://code-cogito.com/en/florence-renaissance-cradle-en/" hreflang="en" lang="en">English</a>
  <a href="https://code-cogito.com/ja/florence-renaissance-cradle-ja/" hreflang="ja" lang="ja">日本語</a>
</nav>
```

Avoid auto-redirecting visitors by IP/`Accept-Language` — it blocks
Googlebot (which crawls from the US) from seeing your zh-TW & ja pages. Offer a
*suggestion banner* instead, and always let the chosen URL render.

## `<html lang>` per version

Make sure each version declares the matching root language so screen readers
and Google read it correctly:

- zh-TW page → `<html lang="zh-Hant-TW">`
- en page → `<html lang="en">`
- ja page → `<html lang="ja">`

## QA checklist

- [ ] View source on one article in each language → confirm **3 + x-default**
      hreflang tags, all absolute, all reciprocal.
- [ ] Run the set through a hreflang validator (e.g. Search Console
      *International Targeting* report, or a crawler like Screaming Frog).
- [ ] Confirm `rel="canonical"` on each page points to **itself**, not another
      language.
- [ ] Confirm no IP-based forced redirect blocks Googlebot.
- [ ] In Search Console, watch for "Alternate page with proper canonical tag"
      vs. unexpected "Duplicate" classifications.
