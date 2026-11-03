# Article 04 — Data Archaeology of the Industrial Revolution

**What do 200-year-old GDP records tell us about today's economy?**

Using Python to visualise the shape of Britain's industrialisation: a GDP growth trend, city population growth and a shift in economic structure. The inputs are small, hand-typed illustrative numbers (see "About the data" below), not archival records.

## Quick Start

```bash
pip install numpy pandas matplotlib
python data_archaeology_analysis.py
```

## What You'll Get

**Charts** (the script saves these three files next to itself):
- `gdp_analysis.png` — Illustrative GDP index (1760 = 100) with separate trend lines before and after an assumed split at 1800
- `urbanization.png` — Population of four British cities, 1750 vs 1850, with the growth multiple (rounded illustrative figures)
- `economic_structure.png` — Stylised economic structure, 1760 vs 1850 (pie charts)

**Printed output** (what the script prints when you run it):

```text
Index rises 3.3x from 1760 to 1850
Average growth 1760-1800: 0.93%/yr
Average growth 1800-1850: 1.66%/yr

Manchester  :     18,000 →    300,000  (16.7x)
Birmingham  :     70,000 →    230,000  (3.3x)
Leeds       :     16,000 →    172,000  (10.8x)
London      :    740,000 →  2,360,000  (3.2x)

1760: Agriculture 70%, Industry 20%, Services 10%
1850: Agriculture 22%, Industry 45%, Services 33%
```

## About the data

Every input in the script (the GDP index, the city populations and the sector shares) is typed in by hand, rounded, and loosely modelled on the general shape of published long-run estimates. None of it is extracted from the Maddison Project or from any other archive, so please do not cite these numbers as historical statistics.

- The tables in the article are computed from a different simplified series, and the Deep Dive Pack uses yet another one. The numbers differ between the three by design.
- The city figures are rounded approximations, and city populations depend on where the boundary is drawn. For example, the article quotes Manchester at 18,000 (1750) and 316,000 (1851), which is 17.6x, while the rounded 1850 value in this script gives 16.7x.
- The sector shares are stylised to show the direction of change. They are not employment or output statistics and do not match the milestones quoted in the article, so treat the percentages as illustration only.
- For real figures, see the sources in the article's reference section (Maddison 2007, Mitchell 1988, Crafts 1985, Broadberry et al. 2015).

## Files

| File | Description |
|------|-------------|
| `data_archaeology_analysis.py` | Main script (illustrative GDP index + city populations + economic structure) |
| `gdp_analysis.png` | GDP index chart |
| `urbanization.png` | City population chart |
| `economic_structure.png` | Economic structure chart |

## Read the Full Article

- [English](https://code-cogito.com/en/data-archaeology-python-industrial-revolution-en/)
- [Chinese](https://code-cogito.com/data-archaeology-python-industrial-revolution/)
- [Japanese](https://code-cogito.com/ja/data-archaeology-python-industrial-revolution-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/industrial-data-04?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=industrial-data-04) includes extended analysis (11 sub-plots, also on a simplified illustrative dataset), a Jupyter Notebook, and the data file.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=industrial-data-04) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
