# Article 06 — Printing Press Analysis

**When Ideas Became Copyable: How the Printing Press Ignited the First Information Revolution**

Using Python to simulate the spread of Gutenberg's printing press across Europe, visualize the book production explosion, and trace the 98% cost collapse that democratized knowledge.

## Quick Start

```bash
pip install numpy matplotlib
python printing_press_analysis.py
```

## What You'll Get

**Terminal output:**
- Years from Mainz to London (26 years)
- Book cost reduction by 1500 (98%)
- Estimated printed books by the 1490s

**Charts:**
- `print_spread_map.png` — Geographic spread of printing press across Europe (1450-1480)
- `book_production.png` — Manuscripts vs printed books by decade (log scale)
- `book_cost_decline.png` — 98% cost collapse in 50 years

## Key Findings

| Metric | 1450 | 1500 | Change |
|--------|------|------|--------|
| Total books | 30,000 | 12,000,000 | **400x** |
| Annual production | 500/year | 1,000,000/year | **2,000x** |
| Books per capita | 1 per 2,333 | 1 per 5.8 | **400x** |
| Relative cost | 100 | 2 | **98% drop** |

Luther's 95 Theses (1517) went from one church door to all of Europe in two months — the first viral information event in history.

## Files

| File | Description |
|------|-------------|
| `printing_press_analysis.py` | Main script (spread map + production chart + cost decline) |
| `print_spread_map.png` | Geographic spread visualization |
| `book_production.png` | Manuscript vs printed book production |
| `book_cost_decline.png` | Book cost collapse chart |

## Read the Full Article

- [English](https://code-cogito.com/en/printing-press-knowledge-revolution-en/)
- [Chinese](https://code-cogito.com/printing-press-knowledge-revolution/)
- [Japanese](https://code-cogito.com/ja/printing-press-knowledge-revolution-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-06?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-06) includes:
- Luther's 95 Theses viral diffusion simulation
- SIR model for information spread
- Literacy rate impact analysis
- Complete propaganda network model
- Jupyter Notebook + data file

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-06) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
