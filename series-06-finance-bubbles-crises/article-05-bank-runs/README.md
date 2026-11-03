# Article 05 — Bank Runs: Northern Rock to Silicon Valley Bank

**2007 vs 2023: bank runs got faster, but the game theory never changed.**

Using Python to sketch maturity mismatch, compare bank run speeds from 1866 to 2023, tabulate a coordination game of depositor decisions (the self-fulfilling run), look at what deposit insurance does and does not cover, walk through SVB's collapse, and draw an illustrative contagion network.

## Quick Start

```bash
pip install numpy matplotlib networkx
python bank_runs_analysis.py
```

The script takes a few seconds, saves the six charts below into the current folder and prints the Model 3 payout table shown further down.

## About the data

Nothing is loaded from files or APIs: every input is typed into the script by hand.

- **Real figures** (Northern Rock's outflows, SVB's $42 billion on 9 March and its ~94% uninsured share, FDIC failure counts, SVB's year-end deposits) carry a `Source:` comment in the code: UK Treasury Committee, FDIC, Federal Reserve (Barr review, St. Louis Fed), SVB's SEC filings. Run durations are approximate reconstructions from the historical literature and do not all measure the same thing.
- **Illustrative inputs** show a mechanism and are not measurements: the bank-run model (1,000 depositors, $10,000 each, 10% reserve, 30% fire-sale discount), the information-speed index, the bond-value index, the risk / impact / severity / trade-off scores and the network edge weights. The chart titles say so.
- In chart 05 the March 8, 9 and 10 deposit points are derived or schematic (end-2022 level, minus $42 billion on 9 March, then zero once the bank is closed); only the year-end values are reported figures.

## What Model 3 prints

`bank_run_simulation()` in `bank_runs_analysis.py` prints this (it is the output of the script, not a hand-written table):

```text
=== Bank Run: The Self-Fulfilling Prophecy ===

Number of depositors: 1000
Deposit per person: $10,000
Total deposits: $10,000,000
Cash reserves (10%): $1,000,000
Loans outstanding: $9,000,000

 Withdrawal% # People         Demand      Available Per Person    Loss%          Outcome
------------------------------------------------------------------------------------------
         5%       50 $      500,000 $      500,000 $   10,000    0.0%    Bank survives
        10%      100 $    1,000,000 $    1,000,000 $   10,000    0.0%    Bank survives
        15%      150 $    1,500,000 $    1,500,000 $   10,000    0.0%        Fire sale
        25%      250 $    2,500,000 $    2,500,000 $   10,000    0.0%        Fire sale
        50%      500 $    5,000,000 $    5,000,000 $   10,000    0.0%        Fire sale
        75%      750 $    7,500,000 $    7,300,000 $    9,733    2.7%       Bank fails
       100%     1000 $   10,000,000 $    7,300,000 $    7,300   27.0%       Bank fails

--- Coordination Game Analysis ---
If you believe others won't withdraw -> you don't withdraw -> bank is safe (best outcome)
If you believe others will withdraw  -> you must withdraw  -> bank fails (worst outcome)
Conclusion: Individually rational choices -> collectively catastrophic result
```

Past 10% withdrawal the bank has to sell loans at a discount ("Fire sale"), but depositors are still paid in full until withdrawals pass about 73% of depositors. The 27% loss at 100% withdrawal comes entirely from the assumed 30% fire-sale discount (0.9 x 0.30): it is an input, not an observation. The code tabulates payouts for a coordination game; it does not solve for equilibria.

## Charts

- `01_maturity_mismatch.png` — Maturity mismatch visualization
- `02_bank_run_speed.png` — Bank run speed, 1866-2023 (approximate durations; share of deposits that left)
- `03_nash_equilibrium.png` — Coordination game: to withdraw or not (file name kept so existing article links keep working)
- `04_deposit_insurance.png` — Deposit insurance: failures by era and the uninsured-deposit gap
- `05_svb_analysis.png` — SVB collapse analysis
- `06_contagion.png` — Illustrative contagion network and timeline

## Read the Full Article

📅 Publishing November 24, 2026 on [Code & Cogito](https://code-cogito.com)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-05?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-05) for this article adds what is not in this free folder: a simulated 48-hour SVB timeline (a stylised model, not hour-by-hour data), a speed comparison of seven bank runs (illustrative values), a 22-bank contagion network with a 50-step contagion simulation that includes a social-media factor, commented code, a Jupyter Notebook, an illustrative data file and a PDF cheatsheet.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-05) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
