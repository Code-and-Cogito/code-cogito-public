# Article 09 — Romanticism Analysis

**Romanticism: When Poets Rebel Against Philosophers**

Three short charts built with Python and matplotlib: an Enlightenment-vs-Romanticism value comparison, a timeline of six landmark Romantic works, and a chart of Romantic themes. The scores behind the first and third charts are illustrative numbers set by the author in the script, not measured data (see the note below).

## Quick Start

```bash
pip install numpy matplotlib
python romanticism_analysis.py
```

## What You'll Get

**Terminal output:**
- Highest-scoring theme among the illustrative theme scores (Nature Sublime, 92%)
- Span of the six featured works (66 years, 1774-1840)
- Number of art-form categories shown (4: Literature, Poetry, Music, Painting)
- A reminder that the value and theme scores are illustrative inputs

**Charts:**
- `enlightenment_vs_romanticism.png` — Value comparison: reason vs emotion across five dimensions (illustrative scores)
- `romantic_works_timeline.png` — Six landmark Romantic works across literature, poetry, music, and painting
- `romantic_themes.png` — Five Romantic themes (illustrative scores)

## What the Charts Show

> **Data note:** the numbers in the value-comparison chart and the theme chart are hand-set illustrative scores. They are not measured, counted, or surveyed data. Only the works and dates in the timeline are historical facts: their commonly cited publication, completion, painting, or exhibition years.

- In those illustrative scores, "Nature Sublime" ranks highest (92%), ahead of "Individual Genius" (85%) and "Revolution & Liberty" (78%).
- The six featured works are dated 1774-1840, a 66-year window across literature, poetry, music, and painting. That is the span of the works chosen for the chart, not a definition of when the movement began or ended.

## Files

| File | Description |
|------|-------------|
| `romanticism_analysis.py` | Main script (values comparison + works timeline + theme chart) |
| `enlightenment_vs_romanticism.png` | Enlightenment vs Romanticism values (illustrative scores) |
| `romantic_works_timeline.png` | Landmark works timeline |
| `romantic_themes.png` | Theme chart (illustrative scores) |

## Read the Full Article

- [English](https://code-cogito.com/en/romanticism-poets-vs-philosophers-en/)
- [Chinese](https://code-cogito.com/romanticism-poets-vs-philosophers/)
- [Japanese](https://code-cogito.com/ja/romanticism-poets-vs-philosophers-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-09?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-09) includes:
- A dataset of 15 Romantic-era works (1774-1862) across five art forms (novel, poetry, music, painting, drama), each hand-scored 0-100 on emotion, nature, individualism, the sublime, and nostalgia (CSV)
- A cross-art-form heatmap comparing the five art forms across the five dimensions
- Interactive Jupyter Notebook: rerun the analysis and adjust it yourself
- 409 lines of commented Python and 9 charts (300 dpi PNG)

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-09) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
