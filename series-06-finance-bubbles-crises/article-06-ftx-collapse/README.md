# Article 06 — Collapse of FTX: Bankruptcy of Trust

**2022: when an entire industry's trust network collapsed — nine days from CoinDesk's report (2 Nov) to FTX's Chapter 11 filing (11 Nov).**

Five small Python models behind the article's figures: a fund-flow sketch, a simplified FTT leverage tower, a trust network, a regulatory-arbitrage comparison and a 2022 crypto-contagion chart. Most of the amounts, scores and indices are hand-set illustrations, not audited data (see "About the numbers" below). This is not a multi-stage collapse simulation.

## Quick Start

```bash
pip install numpy matplotlib networkx
python ftx_collapse_analysis.py
```

The script prints a short summary for each model and saves five PNG files next to it.

## Charts

- `01_fund_flow.png` — illustrative fund-flow sketch (hand-set, overlapping amounts), hand-set governance scores, and a timeline from the Fortune cover story to the sentence
- `02_leverage_tower.png` — FTT leverage tower: collateral vs debt, coverage ratio and a stylised death spiral (hypothetical parameters)
- `03_trust_network.png` — trust flow network, plus hand-set gatekeeper and "why nobody looked" scores
- `04_regulatory_arbitrage.png` — hand-set regulatory comparison, the reported scale of the damage (different measures), and crypto's trust paradox
- `05_crypto_contagion.png` — the 2022 dominoes (Terra, Three Arrows, Celsius, Voyager, FTX): approximate scale per event, a timeline and the usual causal reading

## About the numbers

- **Documented figures** (sources are in the code comments): prosecutors' allegation of more than $8B of customer money taken, $4.1B of related-party loans (Ray declaration), the January 2022 $32B valuation, the event dates in the timeline, and the 2021–2022 fall in total crypto market capitalisation.
- **Hand-set illustrations**: most bars, scores and indices in the charts, including the fund-flow amounts (rough, overlapping, on different bases — the rows add up to $9.456B, more than $8B, so they are not a ledger), the governance, gatekeeper and regulatory scores, and the gaps between the dominoes. The chart titles say so.
- **Hypothetical model**: the leverage tower assumes Alameda holds 40% of FTT, an 80% collateral ratio and a 50% liquidation line. These are not Alameda's actual books (the balance sheet CoinDesk reported showed about $5.8B of FTT, versus $3.5B in the model). With these assumptions the script prints a coverage of 112% after a 10% FTT drop, 62% after 50% and 12% after 90%.

## Read the Full Article

📅 Publishing December 8, 2026 on [Code & Cogito](https://code-cogito.com)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-06?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-06) for this article includes the extended Python script and Jupyter Notebook, the dataset, PDF cheat sheets and Notion notes (the amounts and indices in its charts are hand-set illustrations too).

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-06) takes one real dataset (Maddison Project GDP per capita, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
