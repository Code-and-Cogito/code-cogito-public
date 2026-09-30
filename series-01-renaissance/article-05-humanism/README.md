# Article 05 — Humanism Network Analysis

**Humanism — The Birth of Human Dignity**

Three illustrative charts for the article: six Renaissance humanists plotted by hand-set influence scores, a Medieval vs Humanist "God-centered" radar with author-assigned scores, and a timeline of key text rediscoveries and events.

## Quick Start

```bash
pip install numpy matplotlib
python humanism_analysis.py
```

## What You'll Get

**Terminal output** (this is exactly what the script prints; values are read from the hand-set dictionary in the script):

```text
=== Humanism Analysis Summary (illustrative inputs) ===
Most connected thinker: Erasmus (9 connections, hand-set)
Highest influence score: Petrarch (95, author-assigned)
No network metric is computed here; the NetworkX snippet is in the article.
Timeline marker: 1453 (Fall of Constantinople); Greek learning was already
reaching Italy earlier, e.g. Chrysoloras teaching in Florence from 1397.
Deep Dive Pack adds NetworkX centrality analysis, a Monte Carlo network-
resilience simulation, and a notebook + 20-thinker CSV.
```

**Charts:**
- `humanist_network.png` — scatter plot of six humanists: approximate "year active" marker vs an illustrative influence score (bubble size = hand-set number of connections). It is a scatter plot, not a network graph.
- `paradigm_shift_radar.png` — radar chart of illustrative, author-assigned God-centeredness scores (0-100) for a Medieval and a Humanist profile on five dimensions
- `text_discovery_timeline.png` — timeline of key text rediscoveries and events that fueled humanism (1345 Cicero's letters found by Petrarch in Verona, 1416 Quintilian, 1417 Lucretius, 1453 Fall of Constantinople, 1462 Cosimo begins backing Ficino, 1486 Pico's 900 Theses)

## Notes on the Numbers

**All input numbers in this script are illustrative.** They are typed in by hand, not measured from texts, archives or a citation database.

| Input | What it is |
|-------|-----------|
| `influence` (0-100) | Subjective score assigned by the author |
| `connections` | Hand-set count that only sets the bubble size and the "most connected" line above |
| `era` | Rough "year active" marker, not a birth year or an exact event date. The article's chain diagram uses slightly different illustrative dates (e.g. Boccaccio 1360, Ficino 1470, Erasmus 1510) |
| Radar scores | God-centeredness on a 0-100 scale: Medieval 85-95, Humanist 15-35 (lower = more human-centered). They draw the traditional God-centered to human-centered narrative, which the article presents as the traditional account and the author's reading, not as a result of this analysis |
| Timeline years | Dates typed in by hand from standard accounts, used only to place labels |

**Timeline notes (matching the corrected article):**
- 1345: Petrarch found Cicero's letters (to Atticus and others) in the Chapter Library of Verona, not in Avignon. He was 40.
- 1453: Greek scholars and manuscripts were already reaching Italy earlier (Manuel Chrysoloras taught Greek in Florence from 1397; Giovanni Aurispa brought 238 Greek manuscripts to Venice in 1423), so 1453 is a marker, not a starting point.
- 1462: the year Cosimo de' Medici began supporting Ficino, not the year the Plato translation was finished. The Careggi property was formally given in 1463 and the Corpus Hermeticum came first; Ficino's Latin Plato was complete in draft c. 1468-69 and printed in 1484.

**No network metric is computed in this script.** The NetworkX snippet in the article (12 nodes, directed graph, edges assigned by the author from the historical narrative) is in the article only. Re-running that snippet gives these betweenness centralities:

| Thinker | Betweenness (article snippet) |
|---------|-------------------------------|
| Pico | 0.145 |
| Ficino | 0.118 |
| Erasmus | 0.091 |
| Petrarch | 0.055 |

Petrarch is not the top node in that graph. With Petrarch removed, the other ten nodes stay connected and only Seneca is left isolated.

## Files

| File | Description |
|------|-------------|
| `humanism_analysis.py` | Main script (illustrative influence scatter + paradigm radar + text/event timeline) |
| `humanist_network.png` | Humanist influence scatter plot (illustrative scores) |
| `paradigm_shift_radar.png` | Medieval vs Humanist radar (illustrative scores) |
| `text_discovery_timeline.png` | Key text rediscoveries and events timeline |

## Read the Full Article

- [English](https://code-cogito.com/en/humanism-the-birth-of-human-dignity-en/)
- [Chinese](https://code-cogito.com/humanism-birth-renaissance/)
- [Japanese](https://code-cogito.com/ja/humanism-birth-renaissance-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-05?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-05) includes:
- NetworkX influence graph with degree, betweenness and eigenvector centrality
- Medieval vs Humanist paradigm radar (5 dimensions)
- Geographic-spread, key-works timeline and domain-clustering charts
- Monte Carlo network-resilience simulation (what if key nodes were removed?)
- Jupyter Notebook + CSV of 20 thinkers (scores are author-assigned, not measured)

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-05) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
