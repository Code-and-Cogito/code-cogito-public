# Article 01 — Steam Engine vs Cloud Computing

**Two technologies, 200 years apart, compared with the same toolkit: a Bass diffusion S-curve, a cost-decline comparison and a market-concentration check.**

Using Python and the Bass diffusion model on an illustrative series of UK steam-engine counts (1760–1850), plus a normalized cost comparison of steam engines and cloud computing and a look at 2024 cloud market concentration.

> **About the data.** Every input series in the script (steam-engine counts, the steam and cloud cost series, the 2024 market shares) is an **illustrative figure set by the author** for teaching. They are not verified historical statistics or vendor records; the one real anchor is the 2006 EC2 launch price of $0.10 per hour. What the script prints is what those figures produce inside a model, so read it as "in this model", not as a historical fact.

## Quick Start

```bash
pip install numpy pandas matplotlib scipy
python steam_vs_cloud_analysis.py
```

## What You'll Get

**Terminal output** (this is what the script prints today):

```text
Innovation coefficient (p): 0.0010
Imitation coefficient (q): 0.0500
q/p ratio: 50.0 (imitation dominates)
Peak adoption growth in this model: around 1837
Lag after 1776 (first commercial Watt engines): 61 years

Steam cost reduction: 75.0% over 90 years (illustrative series)
Cloud cost reduction: 86.5% over 18 years (illustrative series)

HHI Index (named providers only, 'Others' left out): 1690
Market classification: Moderately concentrated
```

Two things to keep in mind when you read these numbers:

- **The Bass fit sits on its bounds.** With the fit bounds used in the script, both `p` and `q` end up on their lower bound (0.001 and 0.05), so the q/p ratio of 50 and the 1837 peak mostly reflect those bounds rather than being estimated from the data. The script prints a note saying so. Try changing `lower_bounds` / `upper_bounds` and watch how the numbers move.
- **The HHI is a lower bound.** The "Others" slice (30%) is a long tail of many small providers, so it is left out of the sum; counting it as one firm would add 900 points and overstate concentration. The HHI values in the article's table are a separate rough estimate by the author and are not computed by this script.

**Charts** (written to the current directory each time you run the script; the copies shipped here were produced by the script):
- `technology_adoption_bass.png` — Bass diffusion S-curve fitted to the illustrative UK steam-engine counts
- `cost_comparison.png` — normalized cost decline: steam engine (90 years) vs cloud (18 years), illustrative series
- `market_growth.png` — 2024 cloud market share pie chart (author's rough estimate)

## Files

| File | Description |
|------|-------------|
| `steam_vs_cloud_analysis.py` | Main script (Bass model + cost comparison + market share and HHI) |
| `technology_adoption_bass.png` | Bass diffusion S-curve |
| `cost_comparison.png` | Cost comparison chart |
| `market_growth.png` | Cloud market share chart |

## Read the Full Article

- [English](https://code-cogito.com/en/steam-engine-vs-cloud-computing-en/)
- [Chinese](https://code-cogito.com/steam-engine-vs-cloud-computing/)
- [Japanese](https://code-cogito.com/ja/steam-engine-vs-cloud-computing-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/industrial-data-01?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=industrial-data-01) includes complete version with 11 sub-plots, extended analysis, Jupyter Notebook, and the data file.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=industrial-data-01) takes one real dataset (Maddison Project GDP per capita, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
