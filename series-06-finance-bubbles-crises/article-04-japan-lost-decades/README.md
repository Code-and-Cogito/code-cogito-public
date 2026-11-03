# Article 04 — Japan's Lost Decades vs Taiwan's Housing Crisis

**1989 vs 2024: when real estate becomes religion, demographics become destiny.**

Five small Python models that sketch Japan's bubble and its aftermath next to Taiwan's housing and demographic pressure: price-to-income trajectories, housing hoarding and holding costs, demographic headwinds, zombie companies, and the cost to a "lost generation".

> **Read the data notes below first.** Most chart inputs are hand-set *illustrative* values, not official series. Only the figures listed under "Sourced reference figures" are real-world numbers.

## Quick Start

```bash
pip install numpy matplotlib
python japan_lost_decades_analysis.py
```

The script prints a short summary for each model and saves five PNG charts in the current directory (it overwrites files with the same names).

## Charts

- `01_price_to_income.png` — Price-to-income ratios: Japan vs Taiwan (illustrative series)
- `02_housing_hoarding.png` — Vacancy and holding costs (Taiwan figures sourced or marked as author estimates; other bars illustrative)
- `03_demographics.png` — Fertility, births and population outlook (Taiwan population from the NDC medium projection)
- `04_zombie_companies.png` — Zombie companies and bad debt (illustrative inputs)
- `05_lost_generation.png` — Life-milestone gaps for a "lost generation" (illustrative estimates)

## Data Notes

**Sourced reference figures** (printed by the script; the sources are cited in the code comments)

- Taiwan vacant homes: about 1.66 million, 18.5% of the stock (2020 census; includes occasionally used homes and unsold new units). On the Ministry of the Interior's narrower "low-use (electricity)" definition: about 910,000 homes, 9.8% (H2 2024).
- Taiwan: 41,188 people hold 3+ non-owner-occupied homes (Ministry of Finance, 2025), about 6.9% of the roughly 599,000 people who hold non-owner-occupied homes.
- Fertility: Japan 1.54 (1990) to 1.20 (2023), 33 years; Taiwan 1.18 (2015) to 0.87 (2023), 8 years. Against the replacement level of 2.1, a fertility rate of 0.87 means each generation is about 59% smaller than the last (ignoring migration and mortality changes).
- Births: Japan 2023, 727,277 (MHLW); Taiwan 2015, 213,093 and 2023, 133,895 (MOI, by date of birth).
- Taiwan population, National Development Council 2024 projection, medium scenario: about 23.4 million (2024) to about 15.0 million (2070).
- Zombie firms: about 30% of Japan's listed firms in the early 2000s (about 15% by assets), Caballero, Hoshi and Kashyap (2008); Japan FSA major-bank NPL ratio 8.4% (March 2002) to 1.8% (March 2006).
- US average effective property-tax rate: about 0.9% (about 0.3-2% by state).

**Illustrative or author-estimate inputs** (labelled "illustrative" in the charts, hatched where bars mix sourced and unsourced values)

- Price-to-income series for Tokyo and Taipei (hand-set, scaled to published magnitudes; not an official year-by-year series), and the 3-6x "rule of thumb" band (there is no globally accepted standard).
- Taiwan's roughly 0.1% effective holding cost (author estimate), and the US / Japan / UK / Singapore comparison bars other than the US tax rate.
- The vacancy-versus-price path (only the 2020 vacancy value is the census figure) and the Japan population path.
- The zombie and bad-debt tables, and the zombie-impact magnitudes.
- The life-milestone estimates, including the down payment in years of income (price-to-income x 20-30%), and the "cultural resonance" scores. The 1990-2000 cohort is partly projected.

## Read the Full Article

📅 Scheduled for November 10, 2026 on [Code & Cogito](https://code-cogito.com)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-04?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-04) for this article includes the full Python script and Jupyter notebook, the complete CSV dataset, a Taiwan six-municipality price-to-income analysis, PDF cheat sheets and Notion templates in three languages.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-04) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes, with English, Traditional Chinese and Japanese editions.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
