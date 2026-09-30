# Article 07 — Reformation Analysis

**Reformation — When Authority Crumbles**

Using Python to map the timeline of the Reformation, sketch an illustrative before/after picture of Church authority, and put rough numbers on what the religious wars cost.

## Quick Start

```bash
pip install numpy matplotlib
python reformation_analysis.py
```

## What You'll Get

**Terminal output:**
- Span of the timeline (131 years, 1517–1648)
- Combined rough death estimate for the three conflicts shown (about 7.6–11.1 million)
- Largest conflict (Thirty Years' War, 4.5–8 million)

**Charts:**
- `reformation_timeline.png` — Key events from Luther's 95 Theses (1517) to Peace of Westphalia (1648)
- `authority_radar.png` — Illustrative before/after scores for five dimensions of authority (set by the author, not measured data)
- `religious_wars_deaths.png` — Rough death-toll estimates for three major conflicts; the Thirty Years' War is drawn as a range

## Key Findings

- The timeline runs 131 years, from the 95 Theses (1517) to the Peace of Westphalia (1648)
- Modern estimates for the Thirty Years' War run from about 4.5 to 8 million deaths (battle, famine and disease); 8 million is the upper end, not a settled count
- In the illustrative radar, religious authority and political centralization fall, while individual conscience, Bible access and intellectual freedom rise. These scores are the author's judgement, not data

## Data Notes

| Chart | Data status |
|-------|-------------|
| Timeline | Historical event dates |
| Authority radar | **Illustrative** — the 0–100 scores are hand-set by the author to demonstrate the chart |
| War deaths | Rough estimates; sources differ widely. Peasants' War: about 100,000. French Wars of Religion: about 3 million (rough round figure). Thirty Years' War: 4.5–8 million (see Wikipedia, "Thirty Years' War") |

The pamphlet-diffusion and cascade-failure code shown in the English article is printed in the article itself and is not part of this folder. To run it, add `import matplotlib.pyplot as plt` at the top; with its default parameters it does not produce a full cascade, so treat it as a sketch of the idea rather than a result.

## Files

| File | Description |
|------|-------------|
| `reformation_analysis.py` | Main script (timeline + authority radar + war deaths) |
| `reformation_timeline.png` | Reformation event timeline |
| `authority_radar.png` | Illustrative authority radar (before vs. after) |
| `religious_wars_deaths.png` | Religious war casualties chart |

## Read the Full Article

- [English](https://code-cogito.com/en/reformation-authority-challenged-en/)
- [Chinese](https://code-cogito.com/reformation-authority-challenged/)
- [Japanese](https://code-cogito.com/ja/reformation-authority-challenged-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-07?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-07) includes:
- City cascade network: a stochastic simulation of how ideas spread from Wittenberg across 14 European cities
- Print production analysis: pamphlet output over time, with an exponential-growth fit and its correlation with the Protestant share of territory
- Territorial change chart: Protestant vs. Catholic share of territory over time
- War-death charts: bar and cumulative-line charts of named conflicts
- Jupyter Notebook + a CSV of 20 key events (1517–1685)

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-07) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
