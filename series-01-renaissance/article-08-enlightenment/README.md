# Article 08 — Enlightenment Analysis

**Enlightenment — When Reason Becomes the New God**

Using Python to place eight landmark Enlightenment works on a timeline with hand-set influence scores, sketch an illustrative "reason vs. tradition" shift, and compare how much four ideas mattered to three revolutions (again with hand-set scores).

## Quick Start

```bash
pip install numpy matplotlib
python enlightenment_analysis.py
```

## What You'll Get

**Terminal output:**
- Highest illustrative influence score (Newton, 98)
- Span of the key works in the sample (94 years, 1687-1781)
- Idea with the highest illustrative score for the American Revolution (Natural Rights (Locke), 90)

**Charts:**
- `enlightenment_thinkers.png` — Eight thinkers placed by the publication year of a landmark work, with an illustrative influence score (no connections are drawn)
- `reason_vs_tradition.png` — Illustrative reason vs. tradition curves for six sampled decades (1680s-1780s); the curves cross between the 1720s and 1740s samples
- `ideas_to_revolutions.png` — Illustrative scores for four ideas across the American, French and Industrial revolutions

## Key Findings

- In this sample Newton has the highest illustrative influence score (98), followed by Kant (96) and Locke (95). The scores are the author's judgement, not measured data, and not a scholarly ranking
- Natural Rights (Locke) gets the highest illustrative score for the American Revolution (90) among the four ideas shown
- The eight key works span 94 years, from Newton's *Principia* (1687) to Kant's *Critique of Pure Reason* (1781). That is the spread of this sample, not the length of the Enlightenment itself

## Data Notes

| Chart | Data status |
|-------|-------------|
| Thinkers scatter | Years are publication years of each thinker's landmark work (Principia 1687, Two Treatises 1689, Lettres philosophiques 1734, Treatise of Human Nature 1739, The Spirit of the Laws 1748, The Social Contract 1762, The Wealth of Nations 1776, Critique of Pure Reason 1781). The 0-100 influence scores are **illustrative**, hand-set by the author |
| Reason vs. tradition | **Illustrative** — hand-set 0-100 index values that sketch the idea of a shift; they are not measured shares (the two curves do not sum to 100), and only every second decade is shown |
| Ideas to revolutions | **Illustrative** — hand-set 0-100 scores, not measured data |

The network and revolution-comparison code printed in the articles is not part of this folder. This script is a separate, simpler set of three charts.

## Files

| File | Description |
|------|-------------|
| `enlightenment_analysis.py` | Main script (thinkers scatter + reason vs tradition + ideas-to-revolutions) |
| `enlightenment_thinkers.png` | Thinkers by year of key work and illustrative influence score |
| `reason_vs_tradition.png` | Illustrative reason vs. tradition curves |
| `ideas_to_revolutions.png` | Illustrative idea scores for three revolutions |

## Read the Full Article

- [English](https://code-cogito.com/en/enlightenment-age-of-reason-en/)
- [Chinese](https://code-cogito.com/enlightenment-age-of-reason/)
- [Japanese](https://code-cogito.com/ja/enlightenment-age-of-reason-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-08?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-08) includes:
- Influence network: 20 nodes (15 Enlightenment thinkers plus 5 external predecessors) scored with PageRank, betweenness and eigenvector centrality
- Philosophical spectrum: a static 3D scatter plot placing each thinker by empiricism, rationalism and political-philosophy scores
- Revolution impact: impact scores for the American and French revolutions, with correlations to each thinker's philosophical orientation
- Salon network, key-works timeline, and a static 20-step idea-diffusion model
- 8 charts (300dpi PNG), plus a Jupyter Notebook and a CSV of 15 thinkers

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-08) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
