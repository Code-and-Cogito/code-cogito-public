# Article 12 — Legacy Analysis

**The Ultimate Legacy of the Renaissance: What Did We Inherit After 500 Years?**

Three charts for the series finale: a hand-rated influence matrix across the 11 previous articles plus the synthesis article (12 themes), five "legacy pillars" scored by the author, and an illustrative index of innovation, individual freedom and knowledge access from the 14th to the 19th century. All the numbers are the author's own ratings, not measured data.

## Quick Start

```bash
pip install numpy matplotlib
python legacy_analysis.py
```

## What You'll Get

**Terminal output** (this is exactly what the script prints):

```text
=== Legacy Analysis Summary ===
All scores are hand-set by the author (illustrative ratings, not measured data).
Highest total outgoing influence rating: Legacy (Synthesis) (score: 68 of a possible 110)
  Next highest: Enlightenment (Reason) (score: 61)
Highest single link rating: 9/10, shared by 5 links:
  Medici (Finance) -> Da Vinci (Anatomy)
  Da Vinci (Anatomy) -> Perspective (Math)
  Humanism (Philosophy) -> Enlightenment (Reason)
  Printing (Technology) -> Reformation (Authority)
  Enlightenment (Reason) -> Romanticism (Emotion)
Innovation index (illustrative) 14th->19th century: 20 -> 95
  (not a straight climb: 80 -> 70 in the 17th century)
Full analysis: the Deep Dive Pack adds an influence network graph, PageRank and
betweenness centrality, theme clustering, a give-vs-receive influence flow and a
map from each theme to a present-day parallel.
```

**Charts:**
- `influence_matrix.png` — 12 x 12 heatmap of hand-set 0-10 ratings: how strongly the author rates each theme's influence on every other theme (row influences column)
- `legacy_pillars.png` — five pillars (scientific method, individual rights, democratic governance, free markets, secular ethics), each with a hand-set 0-100 score for "Renaissance contribution" and for "modern relevance"
- `500_year_arc.png` — hand-set 0-100 indexes of innovation, individual freedom and knowledge access, 14th to 19th century

## Notes on the Numbers

**Everything in this script is illustrative.** The values are typed in by hand to sketch an argument. They are subjective judgements, not read from a dataset, and no historical statistics are computed here. (Sourced figures such as the death tolls of the religious wars appear in the article, with their references in its References section.)

| Input | Status |
|-------|--------|
| Influence matrix (12 x 12) | Hand-set 0-10 ratings by the author. Row = influencing theme, column = influenced theme; the diagonal is 0. Another author would fill it differently |
| "Most influential" ranking | The row sum of those ratings, so it only reflects the ratings above. The synthesis article (Legacy) is rated as touching every theme and therefore comes first; Enlightenment is next |
| Legacy pillars | Hand-set 0-100 scores (Renaissance contribution and modern relevance). Not measured |
| Century arc (innovation, freedom, knowledge access) | Hand-set 0-100 indexes for six centuries. Not measured, and not a fitted curve |

## What the Charts Show

- Five links tie for the top rating (9/10): Medici → Da Vinci, Da Vinci → Perspective, Humanism → Enlightenment, Printing → Reformation and Enlightenment → Romanticism. No single link stands alone at the top.
- Summed over its row, Legacy scores 68 of a possible 110 and Enlightenment 61; every other theme is lower. The ranking follows directly from the hand-set ratings.
- In the hand-set arc, the innovation index rises from 20 (14th century) to 95 (19th century) with a dip in the 17th century (80 to 70). Individual freedom rises from 10 to 75 and knowledge access from 15 to 95. This is an illustration of the article's narrative, not a measurement, and the innovation line is not exponential.

## Files

| File | Description |
|------|-------------|
| `legacy_analysis.py` | Main script (hand-rated influence matrix + legacy pillars + 500-year arc) |
| `influence_matrix.png` | Influence heatmap (illustrative ratings) |
| `legacy_pillars.png` | Legacy pillars chart (illustrative scores) |
| `500_year_arc.png` | 500-year arc chart (illustrative index) |

## Read the Full Article

- [English](https://code-cogito.com/en/renaissance-legacy-500-years-en/)
- [Chinese](https://code-cogito.com/renaissance-legacy-500-years-2/)
- [Japanese](https://code-cogito.com/ja/renaissance-legacy-500-years-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-12?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-12) includes:
- An influence network graph of the 12 articles (NetworkX), with PageRank and betweenness centrality
- Theme clustering of the articles by their innovation, freedom and knowledge scores, and a give-vs-receive influence chart
- A map from each article's theme to a present-day parallel (for example AI disruption, or AI ethics and climate)
- Jupyter Notebook + CSV data file (12 rows, one per article): author-rated scores, not measured data

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-12) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes (notebooks in English, Traditional Chinese and Japanese).

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
