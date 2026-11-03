# Article 01 — Rise of Humanism vs Age of Personal Branding

**Pico della Mirandola (1486) vs YouTuber (2024): the quest for individual identity, 500 years apart.**

Five small, illustrative Python models that compare the Renaissance with today's creator economy: a hand-set humanist network, a keyword-frequency index, influence-building curves, a book-cost curve and a simulated influence-inequality comparison. They are built to show how each method works, not to report historical measurements (see [Data Notes](#data-notes)).

## Quick Start

```bash
pip install numpy matplotlib networkx
python humanism_vs_branding_analysis.py
```

The script prints the model outputs and writes the five PNG charts below into the current folder (re-running it overwrites the files in this repository).

## Charts

- `01_humanist_network.png` — Illustrative humanist network (hand-set nodes and edges)
- `02_human_centered_index.png` — Illustrative human-centered index: 1200 to 1600 (hand-set frequencies)
- `03_influence_speed.png` — Illustrative influence-building curves: Petrarch vs a YouTuber
- `04_knowledge_cost.png` — Knowledge access cost over time (illustrative values)
- `05_influence_inequality.png` — Influence inequality, simulated: then vs now

## What the Script Prints

Key outputs, exactly as the script prints them:

| Model | Output |
|-------|--------|
| 1. Network | 8 nodes, 13 edges; highest betweenness centrality: Salutati 0.476 (next: Bruni and Ficino, 0.214). Without Salutati, Petrarch and Boccaccio are cut off from the other five. |
| 2. Index | Human / God ratio 0.14, 0.35, 1.08, 2.29 for 1200-1300 to 1500-1600 |
| 3. Influence curves | ~8.7 years vs ~1.5 years to 50% influence, ~5.6x (computed as ln 2 / k from the assumed k = 0.08 and k = 0.45) |
| 4. Cost curve | 1400: $10,000, 1500: $1,000, 2024: ~$0 (hard-coded illustrative values) |
| 5. Inequality | Gini 0.840 (68 simulated participants) vs 0.985 (7,555 simulated participants) |

## Data Notes

Every input in this script is illustrative (hand-set or synthetic). Nothing here is historical data.

- **Model 1:** the 8-person network, its 13 edges, tie strengths and "letters" counts are hand-set rough numbers. Some edges join people who never lived at the same time (for example Ficino and Salutati, or Erasmus and Bruni). The betweenness values are properties of this toy graph, not of the historical network. For scale, the standard edition of Erasmus's correspondence counts 3,141 letters, sent and received; the script's rough value of 1,800 is only used for node size.
- **Model 2:** the God/Human keyword frequencies are hand-typed numbers. No text corpus is analysed.
- **Model 3:** the curves use assumed rate constants (k = 0.08 and k = 0.45). The printed half-times and the ~5.6x ratio follow directly from those constants.
- **Model 4:** the cost series is hard-coded and illustrative, not a record of historical prices (the last value is 0.01 instead of 0 only so the log axis can show it).
- **Model 5:** the two distributions are random samples drawn with a fixed seed (42) from distributions we chose. The Gini values describe this simulation, not measured influence.

The Deep Dive Pack builds on the same illustrative approach: a 20-scholar, 36-edge network (betweenness and PageRank), a logistic S-curve fit, a five-scholar radar chart and a simulated Erasmus letter-volume series, with static matplotlib charts (no interactive charts, no exercises).

## Read the Full Article

- [English](https://code-cogito.com/en/thought-revolution-01-en/)
- [Chinese](https://code-cogito.com/thought-revolution-01/)
- [Japanese](https://code-cogito.com/ja/thought-revolution-01-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/revolution-of-ideas-01?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=revolution-of-ideas-01) for this article includes the complete code, the data file (an illustrative dataset), Jupyter Notebook, and a PDF cheatsheet.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=revolution-of-ideas-01) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes, in English, Traditional Chinese and Japanese.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
