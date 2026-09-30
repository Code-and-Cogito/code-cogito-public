# Article 02 — Factory Discipline vs Platform Algorithms

**From Taylor's stopwatch to Uber's algorithm: how worker control evolved.**

Using Python to compare a simulated Taylorist factory with simulated gig-economy earnings, and to visualize how discipline mechanisms shifted from physical to algorithmic.

> **Toy models, not data.** Every input in this script is a hand-set, illustrative assumption. The charts and printed numbers are outputs of those assumptions. They are not measurements of a real factory, and they are not Uber statistics or real driver earnings. See [About the numbers](#about-the-numbers).

## Quick Start

```bash
pip install numpy pandas matplotlib
python factory_vs_platform_analysis.py
```

Run it from this folder: the three charts are written to the current directory and overwrite the PNGs stored here. Each chart opens in its own window, so close it to continue, or run headless with `MPLBACKEND=Agg python factory_vs_platform_analysis.py`. The chart labels are in Traditional Chinese, so matplotlib needs a CJK font (the script asks for Arial Unicode MS, Microsoft JhengHei or SimHei); without one the labels show as empty boxes. The whole run takes a few seconds.

## What You'll Get

**Charts:**
- `taylor_output.png` — Taylorist factory output distribution (simulated, arbitrary units)
- `uber_earnings.png` — Gig-driver daily net earnings distribution (simulated)
- `discipline_comparison.png` — Factory vs platform discipline comparison (hand-set 0–1 scores)

**Console output** (seed 42, so it is the same on every run):

```text
[Visualization 1] Taylor Factory Worker Output
  Mean output: 103.1 units/worker/day
  Std: 14.8 units
[Visualization 2] Uber Driver Earnings
  Mean daily net: $210.39
  Median daily net: $209.74
  Gini of daily net income: 0.08
[Visualization 3] Taylor vs Uber Basic Comparison
    Surveillance visibility: Taylor 0.9 vs Uber 0.2
    Worker time autonomy: Taylor 0.1 vs Uber 0.7
    Rule transparency: Taylor 0.8 vs Uber 0.2
    Income stability: Taylor 0.9 vs Uber 0.3
    Management cost: Taylor 0.7 vs Uber 0.3
[Income Volatility Check] Fixed wage vs gig income
  Traditional worker: fixed $100/day (zero variance)
  Gig worker mean daily income: $106.30
  Coefficient of variation: 32.4%
  Days under $50: 1.5% (about 5.4 days per worker per year)
```

## About the numbers

- **Factory output** (mean 103.1 units): arbitrary units from hand-set task times, a fatigue curve and an efficiency spread. It is not calibrated to Taylor's Bethlehem data.
- **Driver earnings** (mean about $210 a day net, Gini 0.08): hand-set rating spread, fare, trips per hour and a round 22% commission. The 22% is not an official Uber figure and the dollar amounts are not calibrated to real driver earnings. The article rounds the Gini of its UberAlgorithm model to "about 0.1" and draws the point that the gap between drivers is modest in this model, while the dispatch rules that produce it are invisible to the drivers.
- **Comparison scores** (0–1): set by hand to encode the mechanisms discussed in the article. They are illustrative, not measured.
- **Income volatility check**: the GigEconomyModel shown in the article (100 workers × 365 days, a fixed $100 wage against a gig income built from four random factors). The article quotes its output as roughly $106 a day, a coefficient of variation of about 32% and about 1.5% of days under $50. This is model output under hand-set assumptions, not measured Uber data.
- **Real-world reference points** used in the article but *not* modelled in this script: Taylor's 1899 pig-iron experiment at Bethlehem Steel Works (Bethlehem, Pennsylvania), with pigs of about 92 lb and loading per handler rising from about 12.5 to 47.5 long tons a day. Source: F. W. Taylor, *The Principles of Scientific Management* (1911), [Project Gutenberg](https://www.gutenberg.org/ebooks/6435). The article's references list the other sources.

## Files

| File | Description |
|------|-------------|
| `factory_vs_platform_analysis.py` | Main script (Taylor output + Uber earnings + comparison + income volatility check) |
| `taylor_output.png` | Factory output distribution (written by the script) |
| `uber_earnings.png` | Gig economy earnings (written by the script) |
| `discipline_comparison.png` | Discipline mechanism comparison (written by the script) |

## Read the Full Article

- [English](https://code-cogito.com/en/factory-discipline-vs-platform-algorithms-en/)
- [Chinese](https://code-cogito.com/factory-discipline-vs-platform-algorithms/)
- [Japanese](https://code-cogito.com/ja/factory-discipline-vs-platform-algorithms-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/industrial-data-02?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=industrial-data-02) includes complete version with 14 sub-plots, extended analysis, Jupyter Notebook, and the data file.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=industrial-data-02) (English, Traditional Chinese and Japanese editions) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
