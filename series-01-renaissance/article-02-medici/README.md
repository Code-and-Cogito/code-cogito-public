# Article 02 — Medici Bank Network Analysis

**The Medici Family: A Financial Empire's Cultural Investment**

Using Python and NetworkX to build a simplified model of the Medici Bank's European branch network (1397-1494) and visualize its hub-and-spoke shape around Florence. The branch revenues are hand-set illustrative inputs, not historical accounts (see [About the Data](#about-the-data)).

## Quick Start

```bash
pip install networkx matplotlib numpy
python medici_bank_analysis.py
```

## What You'll Get

**Terminal output:**
- A branch table ranked by revenue (illustrative values) with opening and closing years
- Summary lines: number of branches, operating period, peak window, sum of the branch revenues

**Chart:**
- `medici_bank_network_basic.png` — Bank network visualization with geographic positioning; node size = illustrative revenue (not historical accounts)

## Key Findings

What the model contains (a simplified model, not archival data):
- 8 entries in the branch table: Florence headquarters plus 7 branches (Rome, Venice, Geneva, Bruges, London, Avignon, Milan)
- 97 years of operation (1397-1494)
- A hub-and-spoke shape centered on Florence — built into the model: every link joins Florence to a branch. (Real branches also traded bills directly with one another.)
- All 8 entries overlap only in 1452-1469 (Milan opens in 1452, Venice closes in 1469), which is what the script prints: `Peak (1452-1469): 8 branches simultaneously`
- Sum of the illustrative branch revenues: 405,000 florins (hand-set, not historical), printed as `Total annual revenue (illustrative inputs): 405,000 florins`

## About the Data

- **Illustrative inputs:** the branch revenues (100,000 florins for Florence down to 25,000 for Milan) are hand-set to size the network chart. They are not taken from Medici accounts.
- **Simplified dates:** the opening and closing years are a rough reconstruction. The table closes Rome, Geneva, London, Avignon and Milan in 1478, whereas historically the London branch was wound up in 1478 together with Bruges (the table says 1480), Geneva's business moved to Lyon in 1466, and Rome and the Lyon office were still open in 1492.
- **Not computed here:** the script models the branch network only. It computes no bill-of-exchange returns.

## Historical Context

- A bill of exchange was written in one currency and paid in another weeks or months later. The quoted rate built in a return for that time — interest, in effect, folded into a currency exchange.
- For a sense of real margins: in 1441 the Medici's Venice branch bought a bill on Bruges at 54½ groats per ducat, then used the proceeds to buy a bill back to Venice at 51½ groats per ducat — about 5.8% ahead after roughly four months. Sources: Raymond de Roover, *The Rise and Decline of the Medici Bank, 1397–1494* (Harvard University Press, 1963); Wikipedia, "[Medici Bank](https://en.wikipedia.org/wiki/Medici_Bank)".

## Files

| File | Description |
|------|-------------|
| `medici_bank_analysis.py` | Main analysis (network model + branch table + chart) |
| `medici_bank_network.png` | Pre-rendered chart (the script itself writes `medici_bank_network_basic.png`) |

## Read the Full Article

- [English](https://code-cogito.com/en/medici-family-cultural-investment-en/)
- [Chinese](https://code-cogito.com/medici-family-cultural-investment/)
- [Japanese](https://code-cogito.com/ja/medici-family-cultural-investment-ja/)

The article's "About the data" note explains which numbers are historical and which are illustrative.

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-02?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-02) includes:
- Time series of branch revenue and active branches (21 time points, 1397-1494; author-built estimates, not archival records)
- Bill of exchange profit model (margin, transit time and annualized return, plus 100 simulated transactions)
- Monte Carlo simulation (exchange rate fluctuation)
- Cascade failure simulation (1478 London default)
- Jupyter Notebook + data file

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-02) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
