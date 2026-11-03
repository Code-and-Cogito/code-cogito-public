# Code & Cogito: The Collapse of FTX and the Bankruptcy of Trust (Season Finale)
# Article: https://code-cogito.com/en/finance-06-en/
# All the code blocks of the article, in order. Program output is kept as comments.

def leverage_tower_collapse(
    initial_ftt_price=25.0,
    total_ftt_supply=350_000_000,
    alameda_ftt_holdings=0.40,
    collateral_ratio=0.80,
    margin_call_threshold=0.50,
    price_drops=[0.0, -0.10, -0.20, -0.30, -0.40, -0.50, -0.70, -0.90]
):
    """
    FTX-Alameda Leverage Tower Model

    Circular dependency with FTT as collateral:
    FTT price drops -> Alameda's collateral falls short -> forced to sell FTT ->
    FTT price drops further -> more collateral shortfalls -> death spiral
    """
    alameda_ftt = total_ftt_supply * alameda_ftt_holdings

    print(f"=== FTX-Alameda Leverage Tower Collapse Model ===\n")
    print(f"FTT initial price: ${initial_ftt_price}")
    print(f"FTT total supply: {total_ftt_supply:,.0f}")
    print(f"Alameda FTT holdings: {alameda_ftt:,.0f} ({alameda_ftt_holdings:.0%})")
    print(f"Collateral ratio: {collateral_ratio:.0%} (borrowed / collateral value)")
    print(f"Coverage below 100% = margin call; below {margin_call_threshold:.0%} = forced liquidation\n")

    initial_value = alameda_ftt * initial_ftt_price
    borrowed = initial_value * collateral_ratio

    print(f"Initial collateral value: ${initial_value / 1e9:.2f}B")
    print(f"Borrowed funds: ${borrowed / 1e9:.2f}B\n")

    print(f"{'FTT Price':>10} {'Drop':>8} {'Collateral':>14} {'Borrowed':>12} "
          f"{'Coverage':>8} {'Gap':>14} {'Status':>16}")
    print("-" * 100)

    for drop in price_drops:
        price = initial_ftt_price * (1 + drop)
        collateral_value = alameda_ftt * price
        coverage = collateral_value / borrowed if borrowed > 0 else 0
        gap = collateral_value - borrowed

        if coverage >= 1.0:
            status = "Safe"
        elif coverage >= margin_call_threshold:
            status = "Margin call"
        elif coverage > 0:
            status = "Forced liquidation"
        else:
            status = "Total collapse"

        if gap < 0:
            gap_str = f"-${abs(gap)/1e9:.2f}B"
        else:
            gap_str = f"+${gap/1e9:.2f}B"

        print(f"${price:>9.2f} {drop:>+7.0%} ${collateral_value/1e9:>10.2f}B "
              f"${borrowed/1e9:>10.2f}B {coverage:>7.0%} {gap_str:>14} {status:>16}")

    print(f"\n--- Death Spiral Mechanism ---")
    print(f"1. FTT price drops -> Alameda's collateral falls short")
    print(f"2. Margin call received -> forced to sell FTT")
    print(f"3. Mass FTT selling -> FTT price drops further")
    print(f"4. More collateral shortfalls -> more forced selling")
    print(f"5. FTT price hits zero -> Alameda bankrupt -> FTX bankrupt")
    print(f"\nKey insight: FTT's value depends on FTX. FTX's solvency depends on")
    print(f"Alameda. Alameda's assets are mostly FTT. A closed loop.")
    print(f"Break any point in the loop, and the entire structure collapses.")

leverage_tower_collapse()

# | === FTX-Alameda Leverage Tower Collapse Model ===
# | 
# | FTT initial price: $25.0
# | FTT total supply: 350,000,000
# | Alameda FTT holdings: 140,000,000 (40%)
# | Collateral ratio: 80% (borrowed / collateral value)
# | Coverage below 100% = margin call; below 50% = forced liquidation
# | 
# | Initial collateral value: $3.50B
# | Borrowed funds: $2.80B
# | 
# |  FTT Price     Drop     Collateral     Borrowed Coverage            Gap           Status
# | ----------------------------------------------------------------------------------------------------
# |     $25.00     +0%      $3.50B      $2.80B   125%       +$0.70B             Safe
# |     $22.50    -10%      $3.15B      $2.80B   112%       +$0.35B             Safe
# |     $20.00    -20%      $2.80B      $2.80B   100%       +$0.00B             Safe
# |     $17.50    -30%      $2.45B      $2.80B    88%       -$0.35B      Margin call
# |     $15.00    -40%      $2.10B      $2.80B    75%       -$0.70B      Margin call
# |     $12.50    -50%      $1.75B      $2.80B    62%       -$1.05B      Margin call
# |      $7.50    -70%      $1.05B      $2.80B    38%       -$1.75B Forced liquidation
# |      $2.50    -90%      $0.35B      $2.80B    12%       -$2.45B Forced liquidation
# | 
# | --- Death Spiral Mechanism ---
# | 1. FTT price drops -> Alameda's collateral falls short
# | 2. Margin call received -> forced to sell FTT
# | 3. Mass FTT selling -> FTT price drops further
# | 4. More collateral shortfalls -> more forced selling
# | 5. FTT price hits zero -> Alameda bankrupt -> FTX bankrupt
# | 
# | Key insight: FTT's value depends on FTX. FTX's solvency depends on
# | Alameda. Alameda's assets are mostly FTT. A closed loop.
# | Break any point in the loop, and the entire structure collapses.
