# Code & Cogito: Bank Runs: From Northern Rock to Silicon Valley Bank
# Article: https://code-cogito.com/en/finance-05-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

def bank_run_simulation(
    n_depositors=1000,
    deposit_each=10000,
    reserve_ratio=0.10,
    fire_sale_penalty=0.30,
    panic_levels=[0.05, 0.10, 0.15, 0.25, 0.50, 0.75, 1.00]
):
    """
    Bank Run Self-Fulfilling Prophecy Model (a coordination-game sketch: it tabulates payouts, it does not solve for equilibria)

    Core insight: Each depositor's "rational" withdrawal decision,
    when aggregated, creates the very bank failure everyone is trying to avoid.
    """
    total_deposits = n_depositors * deposit_each
    cash_reserve = total_deposits * reserve_ratio
    loans = total_deposits * (1 - reserve_ratio)

    print(f"=== Bank Run: The Self-Fulfilling Prophecy ===\n")
    print(f"Number of depositors: {n_depositors}")
    print(f"Deposit per person: ${deposit_each:,.0f}")
    print(f"Total deposits: ${total_deposits:,.0f}")
    print(f"Cash reserves ({reserve_ratio:.0%}): ${cash_reserve:,.0f}")
    print(f"Loans outstanding: ${loans:,.0f}\n")

    print(f"{'Withdrawal%':>12} {'# People':>8} {'Demand':>14} "
          f"{'Available':>14} {'Per Person':>10} {'Loss%':>8} {'Outcome':>16}")
    print("-" * 90)

    for panic in panic_levels:
        withdrawers = int(n_depositors * panic)
        demand = withdrawers * deposit_each

        if demand <= cash_reserve:
            available = demand
            recovery = deposit_each
            loss = 0.0
            status = "Bank survives"
        else:
            shortfall = demand - cash_reserve
            liquidated = min(shortfall / (1 - fire_sale_penalty), loans)
            recovered = liquidated * (1 - fire_sale_penalty)
            available = cash_reserve + recovered
            recovery = available / withdrawers if withdrawers > 0 else 0
            loss = 1 - (recovery / deposit_each)
            remaining_assets = loans - liquidated
            status = "Fire sale" if remaining_assets > 0 else "Bank fails"

        print(f"{panic:>11.0%} {withdrawers:>8} ${demand:>13,.0f} "
              f"${available:>13,.0f} ${recovery:>9,.0f} "
              f"{loss:>7.1%} {status:>16}")

    print(f"\n--- Coordination Game Analysis ---")
    print(f"If you believe others won't withdraw -> you don't withdraw -> bank is safe (best outcome)")
    print(f"If you believe others will withdraw  -> you must withdraw  -> bank fails (worst outcome)")
    print(f"Conclusion: Individually rational choices -> collectively catastrophic result")

bank_run_simulation()

# | === Bank Run: The Self-Fulfilling Prophecy ===
# | 
# | Number of depositors: 1000
# | Deposit per person: $10,000
# | Total deposits: $10,000,000
# | Cash reserves (10%): $1,000,000
# | Loans outstanding: $9,000,000
# | 
# |  Withdrawal% # People         Demand      Available Per Person    Loss%          Outcome
# | ------------------------------------------------------------------------------------------
# |          5%       50 $      500,000 $      500,000 $   10,000    0.0%    Bank survives
# |         10%      100 $    1,000,000 $    1,000,000 $   10,000    0.0%    Bank survives
# |         15%      150 $    1,500,000 $    1,500,000 $   10,000    0.0%        Fire sale
# |         25%      250 $    2,500,000 $    2,500,000 $   10,000    0.0%        Fire sale
# |         50%      500 $    5,000,000 $    5,000,000 $   10,000    0.0%        Fire sale
# |         75%      750 $    7,500,000 $    7,300,000 $    9,733    2.7%       Bank fails
# |        100%     1000 $   10,000,000 $    7,300,000 $    7,300   27.0%       Bank fails
# | 
# | --- Coordination Game Analysis ---
# | If you believe others won't withdraw -> you don't withdraw -> bank is safe (best outcome)
# | If you believe others will withdraw  -> you must withdraw  -> bank fails (worst outcome)
# | Conclusion: Individually rational choices -> collectively catastrophic result
