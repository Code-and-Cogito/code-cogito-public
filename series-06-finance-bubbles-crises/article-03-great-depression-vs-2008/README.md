# Article 03 — Great Depression vs 2008 Financial Crisis

**1929 vs 2008: two crashes, two recoveries — what did we learn (and what did we forget)?**

Six simplified, illustrative Python models that compare the two crises: leverage, an agent-based bank-run toy model, a credit-spiral toy model, unemployment paths, an inequality sketch and recovery times.

> **Data note.** The script reads no data file. The leverage scores (Model 1) and the policy / institution panels are hand-set; Model 3 is a deterministic toy model whose "1929 vs 2008" gap is one hand-set parameter (`policy_response` 0 vs 5); Model 5 is a hand-entered illustrative series, not measured wealth statistics. The Model 4 unemployment rates are annual averages (1929 side: Lebergott's historical estimates, 2008 side: U.S. BLS) and the Model 6 recovery years are simplified (the stock market row uses the nominal Dow price index). The docstring at the top of the script has the details.

## Quick Start

```bash
pip install numpy matplotlib
python depression_vs_2008_analysis.py
```

It needs only numpy and matplotlib, runs in a few seconds, prints a short summary per model and writes the six PNGs below. Model 2 uses `random.seed(42)`, so the bank-run run is reproducible:

```
Step  0:   5 withdrew (  2.5%) | Bank: Operating
Step  5:  15 withdrew (  7.5%) | Bank: Operating
Step  6:  21 withdrew ( 10.5%) | Bank: FAILED
```

(In this toy model the bank holds a 10% cash reserve, i.e. 20 depositors' worth, so it fails as soon as 20 depositors have withdrawn; in this run that happens in step 6, with 21 withdrawn. The script also reruns the model with 200 seeds for each panic threshold and prints the median failure step, which stays between 2 and 5.)

## Charts

- `01_leverage_evolution.png` — Leverage, 1920s vs 2000s (hand-set illustrative scores; leverage about 3x vs about 30x)
- `02_bank_run_agents.png` — Toy agent-based bank run (seed 42) and a threshold check over 200 seeds
- `03_credit_spiral.png` — Credit-spiral toy model: the same reinforcing feedback loop with `policy_response` 0 vs 5
- `04_unemployment_cascade.png` — Unemployment paths (annual averages, 1929 side vs 2008 side)
- `05_wealth_gini.png` — Illustrative inequality series (not measured wealth statistics)
- `06_recovery_time.png` — Recovery times in simplified years (nominal Dow, real GDP, unemployment, banking)

## Read the Full Article

Published on [Code & Cogito](https://code-cogito.com): [English](https://code-cogito.com/en/finance-03-en/) · [繁體中文](https://code-cogito.com/finance-03/) · [日本語](https://code-cogito.com/ja/finance-03-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/finance-bubbles-03?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=finance-bubbles-03) for this article has Python code and a Jupyter notebook for five more advanced illustrative models (leverage network, stress-test cascade, Keynesian multiplier, policy timeline, inequality 1913–2024), an illustrative CSV dataset (not measured data), one-page PDF cheatsheets in three languages, Notion templates and getting-started guides.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=finance-bubbles-03) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
