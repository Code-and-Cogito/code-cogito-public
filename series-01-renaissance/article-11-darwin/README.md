# Article 11 — Darwin Analysis

**Darwin's Evolution: The Final Revolution in Human Status**

Using Python to simulate natural selection (the same deer-herd model as in the article), visualize Darwin's impact across disciplines with illustrative scores, and trace the timeline from the Beagle voyage to *The Descent of Man*.

## Quick Start

```bash
pip install numpy matplotlib
python darwin_analysis.py
```

## What You'll Get

**Terminal output:**
- Years from the start of the Beagle voyage (1831) to the publication of the *Origin* (1859): 28
- Mean speed of the simulated deer herd, generation 0 to generation 49: 49.6 -> 228.9 (+362%)
- The Theology score change in the illustrative radar (95 -> 40, -58%), marked as an author-set score, not measured data

**Charts:**
- `natural_selection_sim.png` — Deer-herd toy model: mean speed (±1 std) per generation, and the herd's speed distribution at the start vs. the last recorded generation
- `darwin_impact_radar.png` — Illustrative before/after scores for theology, philosophy, science, society and ethics (set by the author, not measured data)
- `darwin_timeline.png` — Key events from the Beagle voyage (1831) to *The Descent of Man* (1871)

## Key Findings

- The *Origin* came out 28 years after the Beagle set sail (1831) and 23 years after it returned (1836) — why the wait?
- In the toy model (50 generations, the faster half of the herd survives, each offspring adds a small random mutation), mean speed climbs from 49.6 to 228.9 (+362%). The trait has no upper limit here, so the mean keeps rising; a real trait would hit physical limits and trade-offs. It demonstrates the mechanism, not a prediction about real deer
- In the illustrative radar, the Theology score falls from 95 to 40 (-58%) and the Science score rises. These scores are the author's judgement, not data

## Data Notes

| Chart | Data status |
|-------|-------------|
| Natural selection simulation | Toy model, identical to the code block in the article (seed 42, 200 deer, top 50% survive, mutation N(0, 3)). The numbers are outputs of the model, not measurements of real deer |
| Impact radar | **Illustrative** — the 0–100 scores are hand-set by the author to demonstrate the chart |
| Timeline | Historical event years |

## Files

| File | Description |
|------|-------------|
| `darwin_analysis.py` | Main script (selection sim + impact radar + timeline) |
| `natural_selection_sim.png` | Natural selection simulation |
| `darwin_impact_radar.png` | Illustrative impact radar |
| `darwin_timeline.png` | Key events timeline |

## Read the Full Article

- [English](https://code-cogito.com/en/darwin-evolution-philosophical-shock-en/)
- [Chinese](https://code-cogito.com/darwin-evolution-philosophical-shock/)
- [Japanese](https://code-cogito.com/ja/darwin-evolution-philosophical-shock-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-11?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-11) includes:
- Natural selection simulation: 100 generations of beak-depth change for 14 Darwin's finch species, each driven by its own selection-pressure coefficient
- Darwin's finch family tree: a hierarchical-clustering (UPGMA) dendrogram of 14 species built from genetic-distance values
- Jupyter Notebook: a step-by-step walkthrough of the full analysis; change the selection-pressure coefficients or the number of generations and rerun the simulation
- CSV dataset: beak depth and length, body mass, diet, island, genetic distance and conservation status for 14 Darwin's finch species, plus 6 rows on Darwin's other observations
- Publication-quality charts (300 dpi)

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-11) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
