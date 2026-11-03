# Article 06 — Printing Press Analysis

**When Ideas Became Copyable: How the Printing Press Ignited the First Information Revolution**

Using Python to sketch the spread of Gutenberg's printing press across Europe, chart an illustrative shift from manuscripts to printed books, and plot a hand-set book-cost index.

> **Data note:** every number in `printing_press_analysis.py` is a hand-set, rounded, illustrative value that shows the shape of the story. None of it is a measured historical series. The article's headline figures are quoted estimates; see [Data Notes](#data-notes) below.

## Quick Start

```bash
pip install numpy matplotlib
python printing_press_analysis.py
```

## What You'll Get

**Terminal output** (the script prints exactly these figures):

```
Years from Mainz to London (approximate first-press dates): 26 years
Illustrative cost index (1400 = 100) by 1500: 2, a 98% drop by construction
Illustrative printed output, 1490s: ~15,000 (hand-set units, not a real count)
Article estimate, total books: 30,000 -> 12,000,000 = 400x (CAGR over 50 years: 12.7%)
Books per person at a rounded 70M population: 1 per 2,333 (1450) -> 1 per 5.8 (1500)
Illustrative annual production: 500 -> 1,000,000 books/year = 2,000x
```

**Charts:**
- `print_spread_map.png` — Spread of printing across Europe, 1450-1480 (8 selected cities, approximate first-press years)
- `book_production.png` — Manuscripts vs printed books by decade (log scale, illustrative units, not real counts)
- `book_cost_decline.png` — Hand-set relative book-cost index, 100 to 2 by 1500 (not measured prices)

## Key Figures (estimates, not measurements)

| Metric | 1450 | 1500 | Change | Status |
|--------|------|------|--------|--------|
| Total books | ~30,000 | ~12,000,000 | **400x** | Quoted estimates; see Data Notes |
| Annual production | 500/year | 1,000,000/year | **2,000x** | Illustrative input, not derived from the totals |
| Books per capita | 1 per 2,333 | 1 per 5.8 | **~400x** | Arithmetic on the totals with a rounded 70 million population |
| Compound annual growth rate | — | — | **~12.7%** | 400^(1/50) − 1 |

The book-cost chart uses a hand-set index (1400 = 100): 100 until 1440, 80 in 1455, 2 in 1500. The "98% drop" is simply 100 → 2 by construction.

The 95 Theses (1517): according to Luther's friend Friedrich Myconius, writing years later, they were known across Germany within two weeks and across almost all of Christendom within four. Historians consider that account probably exaggerated. What is documented is that printed editions appeared in Leipzig, Nuremberg and Basel before the end of 1517, plus a German translation in Nuremberg. The article has the details.

## Data Notes

- **Total books, 1450 (~30,000):** a commonly repeated popular estimate. Scholarly estimates vary enormously; Buringh & van Zanden (2009) put manuscript production in Western Europe at nearly 5 million in the fifteenth century alone.
- **Total books, 1500 (~12,000,000):** in line with Buringh & van Zanden's estimate of more than 12 million books printed between 1454 and 1500.
- **Annual production, per-capita and growth-rate figures:** illustrative numbers and simple arithmetic on rounded estimates. The script prints them (section 4), but they are not verified yearly records.
- **Decade production (`book_production.png`):** arbitrary illustrative units, far smaller than real book counts. Only the shape of the curves is meaningful.
- **City dates (`print_spread_map.png`):** approximate first-press years for 8 selected cities, not verified city by city. The article gives a rounded decade-by-decade overview, so single years can differ from the script's per-city values.
- **Source:** Eltjo Buringh and Jan Luiten van Zanden, ["Charting the 'Rise of the West': Manuscripts and Printed Books in Europe, A Long-Term Perspective from the Sixth through Eighteenth Centuries,"](https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/charting-the-rise-of-the-west-manuscripts-and-printed-books-in-europe-a-longterm-perspective-from-the-sixth-through-eighteenth-centuries/0740F5F9030A706BB7E9FACCD5D975D4) *The Journal of Economic History* 69, no. 2 (2009).

## Files

| File | Description |
|------|-------------|
| `printing_press_analysis.py` | Main script (spread map + production chart + cost index + summary arithmetic) |
| `print_spread_map.png` | Spread of printing, 8 cities, approximate dates |
| `book_production.png` | Manuscript vs printed book production (illustrative units) |
| `book_cost_decline.png` | Hand-set book-cost index chart |

## Read the Full Article

- [English](https://code-cogito.com/en/printing-press-knowledge-revolution-en/)
- [Chinese](https://code-cogito.com/printing-press-knowledge-revolution/)
- [Japanese](https://code-cogito.com/ja/printing-press-knowledge-revolution-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-06?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-06) includes:
- Geographic diffusion map: a scatter-plot map built from data for 20 European cities, showing the order in which printing arrived
- City network analysis: betweenness-centrality scores for cities linked by shared trade-hub, university, and religious-center status
- A generic distance-decay (SIR-style) diffusion simulation between cities. It is a generic model, not a reconstruction of any specific event such as the 95 Theses
- Literacy before/after bar chart for the 20 cities
- Editable-parameter Jupyter Notebook: change the propagation parameters in the code and re-run to explore different scenarios
- CSV dataset: 20 cities with press-founding year, coordinates, book output (1480/1500), literacy rates, and book prices

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-06) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
