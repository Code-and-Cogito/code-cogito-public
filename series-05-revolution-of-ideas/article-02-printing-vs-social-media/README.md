# Article 02 — Printing Revolution vs Social Media Explosion

**Gutenberg (1455) vs Zuckerberg (2004): when information breaks free, chaos follows.**

Six small Python models that accompany the article: a relative-speed scale from hand-copying to social media, a book-production curve, an SIR-style simulation of fake-news spread, content-gatekeeping scores, content lengths across media, and an opinion-dynamics simulation of echo chambers.

## Quick Start

```bash
pip install numpy matplotlib
python printing_vs_social_analysis.py
```

Models 1, 2, 4 and 5 use hand-set illustrative values (the author's rough scale for comparison, not measured data or historical statistics). Models 3 and 6 are parameter-driven simulations: their results follow from the parameters you set, and none of them is fitted to data. The script writes the six PNG files listed below into the current folder.

## What the script prints (simulation results)

Model 3 — SIR model, all beta and gamma values are assumed inputs:

| | Luther's Theses (1517) | Modern real news | Modern fake news |
|---|---|---|---|
| Population | 100,000 | 1,000,000 | 1,000,000 |
| Spread rate (beta) | 0.30 | 0.50 | 0.90 |
| Recovery rate (gamma) | 0.01 | 0.10 | 0.02 |
| Peak infected | 86,506 | 188,322 | 925,671 |
| Days to peak | 47 | 30 (window edge, still rising) | 21 |
| Total reached | 100,000 | 242,729 | 1,000,000 |
| Reach rate | 100.0% | 24.3% | 100.0% |

The real-news run is cut off after 30 days, before its peak. The script also prints a 90-day run of the same scenario: it peaks on day 37 with 506,555 infected.

Model 6 — opinion dynamics (200 agents, 80 steps, random seed 42): final opinion standard deviation 0.084 for the geographic chamber (homophily 0.7, no algorithm) and 0.901 for the algorithmic one (homophily 0.5, algorithm boost 1.5), about 10.7 times higher. This is a product of the parameters chosen, so read it as an illustration.

## Charts

- `01_info_speed_comparison.png` — Information speed: manuscript vs print vs digital (illustrative hand-set scale)
- `02_book_production_explosion.png` — Book production 1450–1500 (illustrative hand-set curve ending at 15 million, inside the scholarly estimate of 10–20 million copies printed by 1500)
- `03_fake_news_sir_model.png` — Fake news spread: SIR model (assumed beta and gamma)
- `04_content_filtering_evolution.png` — Content gatekeeping over time (illustrative hand-set scores)
- `05_attention_economy.png` — Content length by medium, from book to short video (illustrative, not measured attention)
- `06_echo_chamber_effect.png` — Echo chamber effect simulation (parameter-driven)

## Sources

The real-world figures quoted in the article (for example Vosoughi, Roy & Aral, "The Spread of True and False News Online", *Science* 359, 2018, and the Reuters Institute *Digital News Report 2024*) are listed with their sources in the References section of each article version. The script only borrows the direction of the MIT finding and does not fit any model to it.

## Read the Full Article

- [English](https://code-cogito.com/en/thought-revolution-02-en/)
- [Chinese](https://code-cogito.com/thought-revolution-02/)
- [Japanese](https://code-cogito.com/ja/thought-revolution-02-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/revolution-of-ideas-02?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=revolution-of-ideas-02) for this article includes complete Python code (.py and Jupyter notebook, with 5 models: a 33-city printing network, book-price changes, SIR on different network structures, attention fragmentation, a polarization index), a CSV dataset (hand-compiled illustrative data, no sources cited), a PDF cheatsheet, a Notion note template and a Getting Started guide (EN/JA/ZH).

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=revolution-of-ideas-02) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes (available in English, Traditional Chinese and Japanese).

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
