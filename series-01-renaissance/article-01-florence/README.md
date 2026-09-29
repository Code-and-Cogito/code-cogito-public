# Article 01 — Florence Network Analysis

**Why Florence Became the Cradle of the Renaissance**

Using Python and NetworkX to build an illustrative model of the 15th-century Italian trade network and analyze how Florence became the hub of the Renaissance.

## Quick Start

```bash
pip install networkx matplotlib numpy
python florence_network_analysis.py
```

## What You'll Get

**Terminal output:**
- Network statistics (nodes, edges, density)
- Betweenness centrality ranking
- Florence vs competitors comparison

**Chart:**
- `florence_network_basic.png` — Trade network visualization; node color = betweenness centrality, node size = rough population

## Key Findings

Florence's betweenness centrality was:
- **32.0x** higher than Venice
- **32.0x** higher than Milan
- **2.67x** higher than Rome

More information, capital, and talent flowed through Florence than any other Italian city.

## Files

| File | Description |
|------|-------------|
| `florence_network_analysis.py` | Main analysis script (network construction + visualization) |
| `florence_network_basic.png` | Output chart |

## Read the Full Article

- [English](https://code-cogito.com/en/florence-renaissance-cradle-en/)
- [Chinese](https://code-cogito.com/florence-renaissance-cradle/)
- [Japanese](https://code-cogito.com/ja/florence-renaissance-cradle-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-01?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-01) includes:
- Complete 20-city network analysis
- 150-year time series (1350-1500, illustrative)
- Jupyter Notebook + data file

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-01) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
