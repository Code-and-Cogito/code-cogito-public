# Article 01 — Tulip Mania vs Bitcoin Bubble

**1637 vs 2021: the same euphoria, the same crash, 384 years apart.**

Using Python to compare bubble trajectories (DTW alignment), simulate investor type distributions, model the greater fool theory, track fear-greed cycles, and measure wealth inequality.

## Quick Start

```bash
pip install numpy matplotlib
python tulip_vs_bitcoin_analysis.py
```

## Charts

- `01_bubble_trajectory_dtw.png` — Bubble trajectories: tulip vs bitcoin (DTW aligned)
- `02_investor_types.png` — Investor type distribution over bubble phases
- `03_greater_fool.png` — Greater fool theory simulation
- `04_fear_greed.png` — Fear-greed index cycle
- `05_wealth_gini.png` — Wealth Gini coefficient: before and after

## Data

- The 36-point tulip price path (Model 1) is a hand-built illustrative shape, not a historical monthly price record — no month-by-month tulip price series survives from 1636–37.
- The 36-point Bitcoin path (Model 1) is a hand-typed approximation from public price history (mixed monthly closes and intramonth highs/lows, roughly December 2019 to mid-2023), not a dataset of monthly closes.
- Models 2, 4 and 5 (investor types, fear/greed, Gini/wealth transfer) plot values the author assigned for illustration, not measured data.
- The DTW "similarity" score uses a custom 0–100 scale computed on these two hand-typed curves; for reference, random walks score ~71% on the same scale.

## Read the Full Article

- [English](https://code-cogito.com/en/finance-01-en/)
- [Chinese](https://code-cogito.com/finance-01/)
- [Japanese](https://code-cogito.com/ja/finance-01-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-01?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-01) for this article includes the complete code, an illustrative data file, Jupyter Notebook, and a PDF cheatsheet.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-01) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
