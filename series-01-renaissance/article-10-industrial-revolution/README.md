# Article 10 — Industrial Revolution Analysis

**The Industrial Revolution: When Machines Changed Everything**

Three charts for the article: a hand-set, illustrative "GDP hockey stick" (Britain vs Europe vs the world), an urbanization chart built from approximate census anchor years (1750, 1801, 1851, 1901), and an illustrative comparison of working conditions in three eras.

## Quick Start

```bash
pip install numpy matplotlib
python industrial_revolution_analysis.py
```

## What You'll Get

**Terminal output** (this is exactly what the script prints):

```text
=== Industrial Revolution Summary ===
UK GDP growth 1750-1900: 462% (Europe 285%, world 100%)
  -> hand-set illustrative series, not Maddison Project data
Urbanization 1750-1901: 17% -> 77% (majority urban by 1851: 54%; approximate)
Child labor at peak: roughly 25% of the workforce (rough estimate; varies with age cutoff and industry)
Life expectancy: 35 years pre-industrial baseline vs 22 years for specific groups in the worst-hit industrial towns
  -> not a national average: England overall rose from about 35 to about 40 (c.1781-c.1851)
Chart 3 values are illustrative (set by the author), not measured statistics.
Full analysis: the Deep Dive Pack adds an industrialization dashboard (GDP, cotton,
coal, steam engines, railways), a three-phase regression of GDP per capita, a
13-indicator correlation heatmap, a Kuznets curve and a 500-run Monte Carlo counterfactual.
```

**Charts:**
- `gdp_hockey_stick.png` — GDP per capita 1000-1900 for Britain, Europe and the world. The values are hand-set and illustrative, not Maddison Project data.
- `urbanization.png` — urban vs rural share of the British population at four census anchor years (1750, 1801, 1851, 1901); the lines between them are interpolation
- `working_conditions.png` — work hours, child labor, life expectancy, literacy and real wages in three eras (1750, 1830, 1900); illustrative bars set by the author, not measured statistics

## Notes on the Numbers

**The GDP lines and the working-conditions bars are illustrative.** They are typed in by hand, not read from a dataset. Only the urbanization anchors and a few reference ranges come from published sources.

| Input | Status |
|-------|--------|
| GDP per capita (Britain / Europe / world) | Hand-set, rounded values that sketch the general shape. **Not** the Maddison Project Database. The UK line rises much more steeply than the published series (Maddison Project Database 2023, constant 2011 int. $: about +181% from 1750 to 1900, versus +462% in this script). For the real series, use the free Starter Notebook |
| Urbanization | Approximate: about 17% (1750), about 30% (1801), 54% (1851), 77% (1901). Sources: Britannica "Urbanization"; Wikipedia "Demographics of the Victorian era". Definitions of "urban" and the area covered differ between sources |
| Work hours (per day) | Rounded bars inside sourced ranges: factory days of 14-16 hours, about 50 hours/week in agriculture around 1750, a 10-hour day for women and children after the 1847 Factories Act |
| Child labor (% of workforce) | Peak value of 25 is a rough estimate for the 1830s; published figures vary widely with the age cutoff and industry. The 1750 and 1900 bars are hand-set |
| Life expectancy | 35 = national baseline (England, about 35 in c.1781). 22 = the average found for specific groups in the worst-hit industrial towns (Chadwick 1842), **not** a national average; England overall rose from about 35 to about 40 by c.1851. 42 (1900) is hand-set |
| Literacy, real wages | Hand-set, no source |

## What the Charts Show

- In the hand-set GDP series, Britain pulls away from Europe and the world after 1750 (+462% vs +285% vs +100% from 1750 to 1900). It is a sketch of the shape of the "hockey stick", not a measurement of it.
- Britain crossed the halfway mark in urban share by the 1851 census (54%), and reached about 77% by 1901.
- The human cost was concentrated in the worst-hit industrial towns and among working-class families: factory days of 14-16 hours, child labor, and average ages at death of about 22 for some groups. National life expectancy did not collapse; it rose slowly from about 35 to about 40.

## Files

| File | Description |
|------|-------------|
| `industrial_revolution_analysis.py` | Main script (illustrative GDP lines + urbanization anchors + illustrative working conditions) |
| `gdp_hockey_stick.png` | GDP per capita chart (illustrative values) |
| `urbanization.png` | Urbanization chart (census anchor years) |
| `working_conditions.png` | Working conditions comparison (illustrative values) |

## Read the Full Article

- [English](https://code-cogito.com/en/the-industrial-revolution-when-machines-changed-everything-en/)
- [Chinese](https://code-cogito.com/industrial-revolution-machines-changed-everything/)
- [Japanese](https://code-cogito.com/ja/industrial-revolution-machines-changed-everything-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-10?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-10) includes:
- 1750-1900 British economic and social indicators: an industrialization dashboard (per-capita GDP, cotton and coal output, steam engines, railway mileage) plus a three-phase piecewise regression of per-capita GDP (1750-1800 / 1800-1860 / 1860-1900)
- Labor conditions statistics: a correlation heatmap across 13 indicators, including working hours, life expectancy, child labor share and the Gini coefficient, plus a regression summary of each social indicator against per-capita GDP (correlation, not causal inference)
- Jupyter Notebook: run the cells in order to reproduce every chart, including a Gini-vs-GDP Kuznets curve and a 500-run Monte Carlo counterfactual in which industrialization starts 50 years earlier or later
- CSV data file (1750-1900, 16 rows): hand-set illustrative values, not archival records

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-10) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes. It is also where to find the real long-run GDP series that the hand-set lines in this script only sketch.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
