# Article 02 — South Sea Bubble vs Dot-Com Bubble

**1720 vs 2000: when narratives replace fundamentals, everything becomes a "sure thing."**

Five illustrative models in Python: a P/E deviation index on hand-set P/E values, sourced IPO counts and first-day returns, a promise-versus-reality sketch, Newton's South Sea trades, and peak-to-bottom decline paths.

## Quick Start

```bash
pip install numpy matplotlib
python south_sea_vs_dotcom_analysis.py
```

## Charts

- `01_pe_deviation.png` — P/E deviation from an assumed historical average (hand-set illustrative P/E values)
- `02_ipo_mania.png` — Nearly 200 share projects in 1720 London vs 856 US IPOs in 1999–2000, Ritter's yearly IPO counts and first-day returns, and an illustrative "who profits" panel
- `03_promise_vs_reality.png` — Promise vs reality gap (illustrative index values, not dollars)
- `04_rationality_collapse.png` — Newton's South Sea timeline, the published estimates of his gain and loss, and illustrative bias scores
- `05_collapse_chain.png` — Peak-to-bottom decline paths, South Sea vs NASDAQ Composite (the file name is kept; the chart plots price paths and is not a contagion model)

## What the script prints

- **Model 1:** peak deviation 11.4x (South Sea, 1720Q3) vs 7.5x (NASDAQ, 2000Q2); correlation of the two deviation curves **0.37**. That number depends on how the curves are lined up: starting the NASDAQ window one quarter earlier gives 0.89, two quarters earlier 0.83. The 3x line is first crossed in 1720Q2 (South Sea) and 1999Q3 (NASDAQ); the deviation takes 2 and 5 quarters to revert. These are properties of two hand-set curves, not evidence of a reliable warning signal.
- **Model 2:** US IPOs per year 474 / 283 / 476 / 380 (1997–2000, 1,613 in total; 856 in 1999–2000) with average first-day returns of 14.0% / 21.9% / 71.2% / 56.3% (about 64.6% for 1999–2000, weighted by number of deals).
- **Model 3:** Pets.com's filed figures for the first nine months of 2000 — sales about $25.8M, cost of goods about $32.7M ($1.27 of cost per $1 of goods sold), operating loss about $86.7M (3.4x sales). The chart itself uses illustrative index values.
- **Model 4:** approximate South Sea price milestones and Newton's figures as published by Odlyzko.
- **Model 5:** South Sea about -85% by the end of September and about -90% by year-end 1720 (-87.5% if the year-end price is taken as 125 rather than 100); NASDAQ Composite -78% over about 31 months.

## Data

- **Hand-set illustrative inputs (not measured data):** the P/E paths and "historical average" P/E in Model 1; the "who profits" returns in Model 2; every value in Model 3 (arbitrary index units, plus approximate hand-typed survival months); the bias scores in Model 4; and the intermediate points of the NASDAQ path in Model 5. Search the script for `ILLUSTRATIVE` to find them all.
- **Sourced values:**
  - 1720 share projects ("nearly 200") — William R. Scott's tally, as cited in Andrew Odlyzko, "An undertaking of great advantage, but nobody to know what it is: Bubbles and gullibility", *Financial History*, 2020. These were announced projects, not all were formed, and they are not IPOs in the modern sense, so the two counts in `02_ipo_mania.png` are not like-for-like.
  - US IPO counts and first-day returns — Jay R. Ritter, "Initial Public Offerings: Updated Statistics", Table 1 (University of Florida).
  - South Sea price milestones (about 128 in January 1720, 330 in March–April, about 550 at the end of May, 890 in early June, about 1,000 in early August, about 150 at the end of September, about 100–125 at year-end; price series differ slightly) and Newton's figures (spring-1720 sale profit about 20,000 pounds, older accounts 7,000; bought back around mid-June at about twice the price; total loss at least 10,000, family lore 20,000) — Odlyzko, "Newton's financial misadventures in the South Sea Bubble", *Notes and Records of the Royal Society* 73(1), 2019.
  - Pets.com — Form 10-Q for the quarter ended 30 September 2000, SEC EDGAR.
  - NASDAQ Composite — close of 5,048.62 on 10 March 2000 and a low of about 1,114 in October 2002.
- Newton's quote is reported as "could not calculate the madness of the people" (earliest record: notes of 1756, published 1820); the comparison with heavenly bodies is a later addition. His motives are undocumented, so the bias scores in Model 4 are a later reading, not a finding.

## Read the Full Article

- [English](https://code-cogito.com/en/finance-02-en/)
- [Chinese](https://code-cogito.com/finance-02/)
- [Japanese](https://code-cogito.com/ja/finance-02-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-02?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-02) for this article adds five more illustrative models (an IPO company network, a P/E-versus-growth regression and insider-versus-outsider returns on randomly generated data, a regulatory timeline, narrative scores) as a Python script and Jupyter Notebook, a CSV of 59 companies and scores, cheat-sheet PDFs in English, Japanese and Chinese, Notion templates and a getting-started guide.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-02) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
