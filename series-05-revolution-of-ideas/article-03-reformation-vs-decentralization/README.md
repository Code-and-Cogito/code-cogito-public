# Article 03 — Reformation vs Decentralization Movement

**Martin Luther (1517) vs Satoshi Nakamoto (2008): when authority crumbles, who fills the void?**

Using Python to sketch an authority hierarchy collapse, run an SIR model of how an idea spreads, draw church-branch and blockchain-lineage networks, compare indulgences to ICOs, tabulate Nakamoto coefficients, and plot a qualitative phase-transition curve.

## Quick Start

```bash
pip install numpy matplotlib networkx
python reformation_vs_decentralization_analysis.py
```

The script prints its results and writes the six PNGs below into the current directory (overwriting existing files).

## Data note

Nothing in this script is loaded from a dataset or computed from raw data. Every number is typed in by hand:

- Hierarchy headcounts, SIR rates, bubble curves and phase-transition "temperatures" are the author's **illustrative assumptions**, not measurements.
- The Nakamoto coefficients for the Catholic Church (1), Protestant churches (~50) and traditional banking (~5) are the author's estimates.
- The crypto coefficients are **hand-entered approximations** from dated sources, cited in the code comments: Bitcoin 2 (mining-pool block shares over 24 hours around 4 July 2024), Ethereum 3 (3–5 depending on whether Dune's unidentified 16.9% staking category counts as one entity, April 2024), Solana 19 (a one-third-of-stake threshold, not 51%, so not directly comparable).
- The ICO scam share (~78%, by project count) is Satis Group's 2018 figure. There is no comparable figure for indulgences.

What the script prints with the current settings: in the SIR model half the population is reached at model day 44 (Luther's rates) vs day 19 (Bitcoin white paper rates), a 2.3x gap that comes entirely from the hand-picked rates (both runs saturate by construction); the branching comparison gives 8 entries in 221 years vs 6 in 9 years, roughly 18x on those small counts.

Sources and the fact-check notes are in the article's References and "About the data" sections.

## Charts

- `01_authority_hierarchy_collapse.png` — Hierarchy layers (headcounts are illustrative assumptions)
- `02_theses_propagation.png` — SIR model of idea spread with hand-set rates (model days, not historical time)
- `03_church_division_network.png` — Protestant branches vs blockchain lineages (simplified sketches, not exact lineages)
- `04_indulgences_vs_ico.png` — Indulgences vs ICOs (illustrative price curves; ICO scam share from Satis Group 2018)
- `05_nakamoto_coefficient.png` — Nakamoto coefficients (hand-entered; estimates and sources labelled)
- `06_phase_transition.png` — Reform-to-revolution phase transition (hand-set qualitative curves)

## Read the Full Article

- [English](https://code-cogito.com/en/thought-revolution-03-en/)
- [Chinese](https://code-cogito.com/thought-revolution-03/)
- [Japanese](https://code-cogito.com/ja/thought-revolution-03-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/revolution-of-ideas-03?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=revolution-of-ideas-03) for this article includes five extended Python models, a Jupyter Notebook, a CSV dataset, PDF cheatsheets (EN/JA/ZH), Notion templates and setup guides.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=revolution-of-ideas-03) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
