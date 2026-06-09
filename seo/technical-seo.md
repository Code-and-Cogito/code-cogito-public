# Technical SEO (WordPress · Yoast · Hostinger/LiteSpeed)

Crawling, indexing, speed and the per-market Search Console setup that lets
Taiwan, Japan and Europe/US actually find you.

## 1. Sitemaps

Yoast generates `https://code-cogito.com/sitemap_index.xml`, which links
post/page/category sitemaps. For this multilingual site:

- [ ] Confirm the index includes **all three language trees** (the `/en/` and
      `/ja/` posts must appear — check `post-sitemap.xml` and any
      language-specific sitemaps your multilingual plugin adds).
- [ ] Submit `sitemap_index.xml` in **each** Search Console property (see §4).
- [ ] Reference it in `robots.txt` (below).
- [ ] Don't list `noindex`, redirected, or thin pages (tag/author archives are
      usually best `noindex`-ed in Yoast → *Settings → Content types/Taxonomies*).

## 2. robots.txt

Keep it permissive for content, block only admin/internals, and point to the
sitemap:

```
User-agent: *
Allow: /
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-json/
Disallow: /?s=
Disallow: /*?replytocom=

Sitemap: https://code-cogito.com/sitemap_index.xml
```
> Do **not** `Disallow: /en/` or `/ja/` — a common accident that de-indexes a
> whole market. Don't block CSS/JS (Google needs them to render & judge mobile).

## 3. Canonicals & indexing hygiene

- [ ] Every page self-canonical **in its own language** (Yoast default — verify
      it isn't cross-language; see `hreflang-multilingual.md`).
- [ ] `noindex` thin archives (date archives, author if single-author, tag
      pages with 1 post).
- [ ] Fix duplicate entry points: trailing slash consistent, `www` →
      non-`www` (or vice-versa) 301'd, `http` → `https` 301'd.
- [ ] Avoid orphan pages — every post reachable via series page + internal links.

## 4. Google Search Console — per market

Set up **one property covering the domain** (Domain property:
`code-cogito.com`) so all languages roll up, *and* use the **URL prefix**
properties to analyze each market separately:

- [ ] Domain property: `code-cogito.com` (DNS verification) — submit sitemap here.
- [ ] Optionally add URL-prefix properties: `https://code-cogito.com/en/` and
      `https://code-cogito.com/ja/` to read each market's queries cleanly.
- [ ] **International Targeting** report → check hreflang errors.
- [ ] Use the **Performance** report filtered by *Country* (Taiwan / Japan /
      United States / key EU countries) to see where each language ranks.
- [ ] Also verify in **Bing Webmaster Tools** — meaningful share in EU/US and
      it powers other engines/AI.
- [ ] (Taiwan/Japan) submit the sitemap; Google is dominant in both, so no
      separate engine needed — but make sure geotargeting isn't accidentally
      pinned to one country (a single domain serving 3 markets should stay
      *unset* for country targeting).

## 5. Core Web Vitals & speed (LiteSpeed)

Your posts are chart-heavy `.png` images, so image weight is the main risk.

- [ ] Install **LiteSpeed Cache** (free, native to Hostinger) → enable page
      cache, CSS/JS minify + combine, and **QUIC.cloud image optimization**
      (WebP conversion).
- [ ] **Lazy-load** below-the-fold images; set explicit `width`/`height` on
      every `<img>` to kill layout shift (CLS).
- [ ] Convert chart PNGs to **WebP**; compress losslessly. A network/scatter
      chart rarely needs > 1600px wide.
- [ ] **Preload** the primary web font; use `font-display: swap`. CJK fonts are
      heavy — subset or use the system font stack for zh/ja to cut LCP.
- [ ] Add `loading="lazy"` + `decoding="async"` to inline images.
- [ ] Test each language template in
      [PageSpeed Insights](https://pagespeed.web.dev/) (mobile tab — TW & JP
      traffic is mobile-heavy).

## 6. Image SEO (big opportunity — your content is visual)

Every article ships several analysis charts. Make them work for Google Images:

- [ ] **Descriptive filenames** (you already do this well:
      `florence_network_basic.png`, `01_price_to_income.png`).
- [ ] **Localized `alt` text** per language version — describe what the chart
      shows, e.g.
      - en: `alt="Network graph: Florence's trade centrality vs Venice, Milan, Rome"`
      - zh-TW: `alt="網絡圖：佛羅倫斯與威尼斯、米蘭、羅馬的貿易中心性比較"`
      - ja: `alt="ネットワーク図：フィレンツェとヴェネツィア・ミラノ・ローマの交易中心性比較"`
- [ ] Add a caption where it aids comprehension.
- [ ] Ensure images are in the page sitemap (Yoast includes images by default).

## 7. Internal linking & site architecture

- [ ] **Silo by series and language.** Each article links to its series hub and
      2–4 sibling articles **in the same language** (never link zh → en
      mid-article; it confuses users and signals).
- [ ] Create/maintain a **series landing page** per language as the hub.
- [ ] Link new articles from older high-traffic ones (descriptive anchor text,
      not "click here").
- [ ] Link to the **Deep Dive Pack** (`/products/`) from each related article —
      good for users and for funnelling crawl + conversions.

## 8. Ongoing

- [ ] Keep `dateModified` fresh when you genuinely update a post.
- [ ] Watch Search Console **Pages** report for "Crawled – currently not
      indexed" / "Discovered – not indexed" (thin or duplicate signals).
- [ ] Re-run PageSpeed after any theme/plugin change.
