# Structured Data (JSON-LD)

> **Apply in:** Yoast already outputs a baseline `@graph` (WebSite, WebPage,
> Organization, Article, Breadcrumb). **First check what you already have** with
> the [Rich Results Test](https://search.google.com/test/rich-results) before
> adding anything — don't duplicate types. Add the extras below only where
> Yoast doesn't cover them, via a code block / SEO plugin's schema feature.

Correct schema makes your results eligible for rich features: article rich
results, breadcrumbs, the sitelinks search box, and FAQ accordions. For a
multilingual site the critical field is **`inLanguage`** — set it per version.

## 1. Organization (site-wide — once, on the homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Code & Cogito",
  "url": "https://code-cogito.com/",
  "logo": "https://code-cogito.com/path-to-logo.png",
  "description": "Decoding history through code. Understanding philosophy through data.",
  "founder": { "@type": "Person", "name": "Wina" },
  "sameAs": [
    "https://github.com/Code-and-Cogito/code-cogito-public"
  ]
}
```
> Add your real logo URL and any social profiles (X, YouTube, Threads, etc.)
> to `sameAs` — it strengthens entity recognition across all three markets.

## 2. WebSite + Sitelinks Search Box (homepage)

Lets Google show a search box for your brand query.

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Code & Cogito",
  "url": "https://code-cogito.com/",
  "inLanguage": "zh-Hant",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://code-cogito.com/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

## 3. Article (every post — set `inLanguage` per version)

Example for the zh-TW Florence article. For the `/en/…` and `/ja/…` versions,
change `inLanguage`, `headline`, `url`, and `description` accordingly.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "為什麼是佛羅倫斯？用 Python 解析文藝復興的起點",
  "description": "用 Python 與網絡分析重建 15 世紀義大利貿易網，揭開佛羅倫斯成為文藝復興搖籃的數據真相。",
  "inLanguage": "zh-Hant",
  "url": "https://code-cogito.com/florence-renaissance-cradle/",
  "image": "https://code-cogito.com/path-to/florence_network_basic.png",
  "datePublished": "2025-01-01",
  "dateModified": "2026-06-09",
  "author": { "@type": "Person", "name": "Wina", "url": "https://code-cogito.com/about/" },
  "publisher": {
    "@type": "Organization",
    "name": "Code & Cogito",
    "logo": { "@type": "ImageObject", "url": "https://code-cogito.com/path-to-logo.png" }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://code-cogito.com/florence-renaissance-cradle/" }
}
```
- `inLanguage` values: `zh-Hant` (TW), `en`, `ja`.
- Always set a real `image` (your chart `.png` works well — it's the topic).
- Keep `dateModified` current when you re-edit; it can refresh ranking.

## 4. BreadcrumbList (every post)

Helps Google show `Home › Series › Article` breadcrumbs in results.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://code-cogito.com/" },
    { "@type": "ListItem", "position": 2, "name": "Renaissance", "item": "https://code-cogito.com/series/renaissance/" },
    { "@type": "ListItem", "position": 3, "name": "Why Florence Became the Cradle of the Renaissance" }
  ]
}
```

## 5. FAQPage (optional, high-value)

If an article answers a few concrete questions, add an FAQ block on the page
*and* mark it up — it can earn an expandable rich result and capture
voice/AI-overview queries. Use real Q&A that appears on the page.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did the Renaissance start in Florence and not Venice or Rome?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Network analysis shows Florence's betweenness centrality was 2.2× Venice and 9.9× Rome — more information, capital and talent flowed through it than any rival city."
      }
    }
  ]
}
```
> Localize the questions/answers per language version. Only mark up content
> that is actually visible on the page.

## Validation

- [ ] [Rich Results Test](https://search.google.com/test/rich-results) on one
      page per language → no errors, expected types detected.
- [ ] [Schema Markup Validator](https://validator.schema.org/) for full graph.
- [ ] Search Console → *Enhancements* → check Breadcrumbs / FAQ reports for
      coverage and errors after a couple of weeks.
