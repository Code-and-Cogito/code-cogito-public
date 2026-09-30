# Article 03 — The Mathematics of Labor Alienation: From Marx to Algorithms

**From factory floors to feed algorithms: is Marx's alienation theory more relevant than ever?**

Using Python to compute an illustrative alienation index for three worker profiles (artisan, factory worker, gig worker), to plot that index across eras, and to compare the four-dimension autonomy of a gig worker and a factory worker.

> **About the data.** Every input in the script (the 0–1 worker profiles behind the alienation index and the autonomy-dimension scores) is an **illustrative setting chosen by the author** to show how the model works. They are not measured, survey or historical data. The settings were chosen so that the formulas reproduce the values in the article's illustrative table (alienation index: artisan 0.19, factory worker 0.75, gig worker 0.69; autonomy index: gig worker 0.30 vs factory worker 0.11). What the script prints is what those settings produce inside the model, so read it as "in this model", not as a historical fact.

## Quick Start

```bash
pip install numpy matplotlib
python alienation_analysis.py
```

## What You'll Get

**Terminal output** (this is what the script prints today):

```text
[Plot 1] Alienation Index Era Comparison (illustrative profiles)
- Artisan (1800): 0.19 (pre-industrial baseline)
- Factory worker (1900): 0.75 (industrial-era factory work)
- Gig worker (2024): 0.69 (approaches the factory level, 0.06 below it)

[Plot 2] Alienation Trend Across Eras (representative worker types)
- 1800 Artisan: 0.19 (computed here)
- 1900 Factory worker: 0.75 (computed here)
- 1960 Office worker: 0.58 (article table value)
- 2000 Knowledge worker: 0.45 (article table value)
- 2024 Gig worker: 0.69 (computed here)
- Highest of the five: Factory worker (1900) at 0.75; the gig worker (0.69) is 0.06 below it

[Plot 3] Gig vs Factory Autonomy (illustrative scores)
Autonomy index (0.40*decision + 0.25*time + 0.20*method + 0.15*transparency):
- Gig worker: 0.30 | Factory worker: 0.11 (the gig worker looks freer on paper)
- Widest gap in the gig worker's favor: Time control (0.70 vs 0.10)
- The gig worker scores lower than the factory worker on information transparency (0.10 vs 0.30): the rules stay hidden
```

Three things to keep in mind when you read these numbers:

- **The worker profiles are hand-set.** The article publishes the alienation-index formula (weights 0.30 / 0.25 / 0.25 / 0.20) and the resulting table, but not the inputs behind that table. The profiles in the script are this script's own illustrative settings, chosen so the formula gives 0.19, 0.75 and 0.69. Change them and the index moves accordingly.
- **Two points in the trend chart are not computed here.** The 1960 office worker (0.58) and the 2000 knowledge worker (0.45) are the article's table values, drawn as hollow markers. Their input profiles are not part of this script, and nothing between the five points is interpolated.
- **The autonomy weights and the factory scores are this script's choice.** The article gives the gig worker's four scores (time control 0.70, decision authority 0.20, method choice 0.15, information transparency 0.10) and the two composites (0.30 vs 0.11), but not its weights. The weights (0.40 / 0.25 / 0.20 / 0.15) and the factory worker's four scores are illustrative settings chosen to reproduce those two composites.

**Charts** (written to the current directory each time you run the script; the copies shipped here were produced by the script):
- `alienation_comparison.png` — alienation index of the three illustrative profiles, with the hand-set inputs in a table
- `alienation_trend.png` — alienation index across eras, 1800–2024 (three computed points, two article-table values)
- `autonomy_gap.png` — four-dimension autonomy of a gig worker vs a factory worker (industrial vs digital era)

## Files

| File | Description |
|------|-------------|
| `alienation_analysis.py` | Main script (alienation index model + trend + autonomy comparison) |
| `alienation_comparison.png` | Alienation index comparison |
| `alienation_trend.png` | Alienation trend chart |
| `autonomy_gap.png` | Gig vs factory autonomy chart |

## Read the Full Article

- [English](https://code-cogito.com/en/labor-alienation-marx-to-algorithms-en/)
- [Chinese](https://code-cogito.com/labor-alienation-marx-to-algorithms/)
- [Japanese](https://code-cogito.com/ja/labor-alienation-marx-to-algorithms-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/industrial-data-03?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=industrial-data-03) includes the full 14 sub-plot version of this analysis (alienation index calculator with heatmap and trend, sentiment-analysis demos on simulated data, labor-autonomy radar chart, algorithm-alienation deep dive), a Jupyter Notebook, and the data file.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=industrial-data-03) takes one real dataset (Maddison Project GDP per capita, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
