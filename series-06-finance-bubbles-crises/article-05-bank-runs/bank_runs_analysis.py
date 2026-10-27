"""
Finance, Bubbles & Crises #05: Bank Runs -- From Northern Rock to SVB
Free Version -- 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install numpy matplotlib networkx

ABOUT THE DATA (read this first)
  Nothing is loaded from files or APIs: every input below is typed in by hand.
  - Figures that mirror a real event carry a "Source:" comment (FDIC, Federal
    Reserve, SEC filings, UK Treasury Committee, ...). They are rounded the same
    way as in the article.
  - Everything else is ILLUSTRATIVE: the bank-run model inputs (1,000 depositors,
    $10,000 each, 10% reserve, 30% fire-sale discount), the information-speed
    index, the risk / impact / severity / trade-off scores and the network edge
    weights. They are chosen to show a mechanism, not measured, and the chart
    titles say so.
  - Model 3 prints a payout table. Its 27% loss at 100% withdrawal follows
    entirely from the assumed 30% fire-sale discount; it is an input, not a
    finding.
"""

from datetime import date

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Maturity Mismatch -- The Structural Vulnerability
# ============================================================
print("=" * 65)
print("MODEL 1: Maturity Mismatch -- Banking's Fatal Flaw")
print("=" * 65)

categories = ['Deposits\n(Liabilities)', 'Loans\n(Assets)', 'Reserve\nRatio',
              'Mismatch\nGap (years)']
typical_bank = [100, 90, 10, 15]  # deposits%, loans%, reserve%, avg maturity gap

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("Maturity Mismatch: Banking's Structural Vulnerability\n"
             "Deposits: withdrawable anytime | Loans: 5-30 year terms | "
             "Reserves: a small fraction of deposits (US requirement was 3-10% until March 2020)",
             fontsize=14, fontweight='bold')

# Panel 1: Balance sheet visualization
ax = axes[0]
# Liabilities side
ax.barh([2], [100], color='#3498DB', alpha=0.8, label='Deposits (short-term)',
        edgecolor='black', linewidth=1.5, height=0.6)
ax.barh([2], [10], color='#2C3E50', alpha=0.8, label='Equity', left=100,
        edgecolor='black', linewidth=1.5, height=0.6)
# Assets side
ax.barh([1], [10], color='#27AE60', alpha=0.8, label='Cash Reserves',
        edgecolor='black', linewidth=1.5, height=0.6)
ax.barh([1], [100], color='#E74C3C', alpha=0.8, label='Long-term Loans', left=10,
        edgecolor='black', linewidth=1.5, height=0.6)
ax.set_yticks([1, 2])
ax.set_yticklabels(['Assets', 'Liabilities'], fontsize=12, fontweight='bold')
ax.set_xlabel('Amount (%)', fontsize=11)
ax.set_title('Bank Balance Sheet (stylised)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper right')
ax.grid(axis='x', alpha=0.3)

# Panel 2: Time horizon mismatch
ax = axes[1]
items = ['Checking\nDeposits', 'Savings\nAccounts', 'CDs\n(1 year)', 'Mortgage\nLoans',
         'Business\nLoans', 'Government\nBonds']
durations = [0.01, 0.1, 1, 25, 5, 10]  # in years; typical orders of magnitude, illustrative
colors_d = ['#3498DB', '#3498DB', '#2980B9', '#E74C3C', '#E67E22', '#F39C12']
bars = ax.barh(range(len(items)), durations, color=colors_d, edgecolor='black', linewidth=1)
ax.axvline(x=1, color='red', linestyle='--', linewidth=2, alpha=0.7, label='1 year mark')
ax.set_yticks(range(len(items)))
ax.set_yticklabels(items, fontsize=9)
ax.set_xlabel('Duration (years, log scale; typical values, illustrative)', fontsize=11)
ax.set_xscale('log')
ax.set_title('Liability vs Asset Duration', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3)
ax.text(0.02, -0.8, 'LIABILITIES (short)', fontsize=10, color='#3498DB', fontweight='bold')
ax.text(5, -0.8, 'ASSETS (long)', fontsize=10, color='#E74C3C', fontweight='bold')

# Panel 3: The movie theater analogy
ax = axes[2]
theta = np.linspace(0, 2*np.pi, 100)
# Theater with people
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# Draw "seats" as dots (100 dots stand for the 1,000 seats: one dot = 10 seats)
np.random.seed(42)
n_seats = 100
seat_x = np.random.uniform(-1.5, 1.5, n_seats)
seat_y = np.random.uniform(-1.2, 1.2, n_seats)
ax.scatter(seat_x, seat_y, s=30, color='#3498DB', alpha=0.6,
           label=f'{n_seats} dots = 1000 depositors (1 dot = 10)')
# Draw exits (only 2!)
ax.scatter([1.8, -1.8], [0, 0], s=300, color='#E74C3C', marker='s', zorder=5,
          edgecolors='black', linewidths=2)
ax.text(1.8, -0.3, 'EXIT 1\n(10%)', ha='center', fontsize=8, fontweight='bold', color='#E74C3C')
ax.text(-1.8, -0.3, 'EXIT 2\n(reserves)', ha='center', fontsize=8, fontweight='bold', color='#E74C3C')
ax.set_title('The Movie Theater Analogy\n1000 seats, 2 exits', fontsize=12, fontweight='bold')
ax.text(0, -1.8, 'Normal: slow orderly exit\nPanic: stampede -> everyone trapped',
        ha='center', fontsize=9, fontweight='bold', style='italic')
ax.axis('off')

fig.text(0.5, 0.0, 'Stylised illustration with illustrative numbers, not data from any real bank.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('01_maturity_mismatch.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_maturity_mismatch.png")


# ============================================================
# MODEL 2: Bank Run Speed -- 1866 to 2023
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Bank Run Speed Evolution (1866-2023)")
print("=" * 65)

events = ['Overend\nGurney\n1866', 'Great\nDepression\n1930-33', 'Continental\nIllinois\n1984',
          'Northern\nRock\n2007', 'SVB\n2023']

# Run duration in hours -- approximate, reconstructed from the historical
# literature (sources differ slightly), and not the same measurement for every
# event (time to failure vs time to official intervention).
#   Overend Gurney 1866: acute phase ~1 week.
#     Source: Yale New Bagehot, "Bank of England Lending during the Panic of 1866".
#   Great Depression 1930-33: runs came in waves over months. 720 h is a
#     PLACEHOLDER, not the length of a single run: the bar is hatched and the
#     event is left out of the speed line in panel 3.
#   Continental Illinois 1984: ~10 days.
#     Source: Federal Reserve History; St. Louis Fed (Rose, 2023).
#   Northern Rock 2007: ~3 days, 14-17 Sep, to the government guarantee.
#     Source: UK Treasury Committee, "The run on the Rock".
#   SVB 2023: ~43 h, from SVB's announcement on the evening of 8 Mar to closure
#     on 10 Mar. Source: SVB 8-K (8 Mar 2023); FDIC testimony, 27 Mar 2023.
duration_hours = [168, 720, 240, 72, 43]
duration_labels = ['~1 week', 'months (waves)', '~10 days', '~3 days', '~43 hours']
comparable = [True, False, True, True, True]  # single-run durations only

# Share of deposits (Continental Illinois: of funding) that left, as reported.
# The windows differ, so read it as "how much, how fast", not one like-for-like metric.
#   Northern Rock: ~GBP 1bn on 14 Sep (~5% of deposits), ~GBP 2bn (~8%) by 17 Sep.
#     Source: UK Treasury Committee; Yale case study "Northern Rock Emergency Liquidity Program".
#   SVB: USD 42bn on 9 Mar (~25% of deposits; FDIC testimony, St. Louis Fed). With
#     ~USD 100bn queued for 10 Mar, nearly nine-tenths (25% + 62% = 87%, St. Louis Fed)
#     of deposits were on their way out within two days.
#   Continental Illinois: ~30% of funding (>USD 10bn) in ~10 days.
#     Source: Federal Reserve History; St. Louis Fed (Rose, 2023).
#   np.nan = no comparable figure found.
worst_day_pct = [np.nan, np.nan, np.nan, 5, 25]
whole_run_pct = [np.nan, np.nan, 30, 8, 87]

info_channel = ['Newspaper', 'Newspaper\n+ Telegraph', 'Phone\n+ Wire', 'TV +\nInternet',
                'Social\nMedia +\nMobile']
# ILLUSTRATIVE index of how fast news travels (not measured, no source).
info_speed = [1, 5, 50, 500, 10000]

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Bank Run Speed, 1866-2023\n'
             '1866: ~1 week | 2023: under 2 days | SVB ~5-10x faster than Northern Rock, '
             'relative to deposits',
             fontsize=14, fontweight='bold')

# Panel 1: Duration bars
ax = axes[0]
colors_dur = plt.cm.RdYlGn_r(np.linspace(0.2, 0.9, len(events)))
bars = ax.barh(range(len(events)), duration_hours, color=colors_dur,
               edgecolor='black', linewidth=1)
bars[1].set_hatch('//')  # waves over months, not a single run
ax.set_yticks(range(len(events)))
ax.set_yticklabels(events, fontsize=9)
ax.set_xlabel('Duration (hours, approximate)', fontsize=11)
ax.set_xlim(0, 950)
ax.set_title('Approximate Length of the Run', fontsize=12, fontweight='bold')
for bar, label in zip(bars, duration_labels):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            label, va='center', fontweight='bold', fontsize=10)
ax.grid(axis='x', alpha=0.3)

# Panel 2: Share of deposits that left (replaces the old hand-set "$ per hour" series)
ax = axes[1]
x = np.arange(len(events))
w = 0.38
for offset, vals, color, lab in [(-w/2, worst_day_pct, '#F39C12', 'Worst single day'),
                                 (w/2, whole_run_pct, '#E74C3C',
                                  'Whole run, as reported (windows differ)')]:
    valid = [i for i, v in enumerate(vals) if not np.isnan(v)]
    ax.bar(x[valid] + offset, [vals[i] for i in valid], w, color=color,
           edgecolor='black', linewidth=1, label=lab)
    for i, v in enumerate(vals):
        if not np.isnan(v):
            ax.text(x[i] + offset, v + 1.5, f'~{v:.0f}%', ha='center', fontweight='bold',
                    fontsize=10)
for i in range(len(events)):  # mark the gaps: no comparable figure found
    no_worst, no_whole = np.isnan(worst_day_pct[i]), np.isnan(whole_run_pct[i])
    if no_worst and no_whole:
        ax.text(x[i], 3, 'n/a', ha='center', fontsize=9, color='gray')
    elif no_worst:
        ax.text(x[i] - w/2, 3, 'n/a', ha='center', fontsize=7, color='gray', rotation=90)
    elif no_whole:
        ax.text(x[i] + w/2, 3, 'n/a', ha='center', fontsize=7, color='gray', rotation=90)
ax.set_xticks(x)
ax.set_xticklabels(['Overend\nGurney', 'Great\nDepression', 'Continental\nIllinois',
                    'Northern\nRock', 'SVB'], fontsize=9)
ax.set_ylabel('% of deposits (Continental Illinois: % of funding)', fontsize=11)
ax.set_ylim(0, 105)
ax.set_title('Share of Deposits That Left', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Information channel evolution
ax = axes[2]
ax.plot(range(len(events)), info_speed, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=10, label='Info speed (illustrative index)')
speed_idx = [i for i, ok in enumerate(comparable) if ok]
run_speed = [duration_hours[0] / duration_hours[i] for i in speed_idx]  # 1 / duration, 1866 = 1
ax.plot(speed_idx, run_speed, 's-', color='#3498DB', linewidth=2.5, markersize=8,
        label='Run speed = 1 / duration (1866 = 1)')
ax.set_xticks(range(len(events)))
ax.set_xticklabels(info_channel, fontsize=7)
ax.set_ylabel('Relative Speed (log)', fontsize=11)
ax.set_yscale('log')
ax.set_title('Information Speed vs Run Speed\n(illustrative index; Great Depression run speed not plotted)',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

fig.text(0.5, 0.0,
         'Durations are approximate reconstructions that measure different things (time to failure vs time to '
         'official intervention). SVB whole run = 25% withdrawn on 9 Mar + ~62% queued for 10 Mar '
         '(St. Louis Fed). Info-speed index is illustrative.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('02_bank_run_speed.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Approximate duration:", ", ".join(
    f"{e.replace(chr(10), ' ')} {lab}" for e, lab in zip(events, duration_labels)))
print("  Worst single day (share of deposits): Northern Rock ~5%, SVB ~25% -> about 5x")
print("  Whole run (as reported): Northern Rock ~8% after 3-4 days, "
      "SVB ~87% (withdrawn + queued) within 2 days -> close to 10x")
print("=> Saved: 02_bank_run_speed.png")


# ============================================================
# MODEL 3: Coordination Game -- The Self-Fulfilling Prophecy
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Coordination Game -- Self-Fulfilling Bank Run")
print("=" * 65)


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

    All inputs are ILLUSTRATIVE assumptions, not data from any real bank.
    Returns one dict per panic level (used for the charts below).
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

    results = []
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

        results.append({'panic': panic, 'loss': loss, 'recovery': recovery, 'status': status})
        print(f"{panic:>11.0%} {withdrawers:>8} ${demand:>13,.0f} "
              f"${available:>13,.0f} ${recovery:>9,.0f} "
              f"{loss:>7.1%} {status:>16}")

    print(f"\n--- Coordination Game Analysis ---")
    print(f"If you believe others won't withdraw -> you don't withdraw -> bank is safe (best outcome)")
    print(f"If you believe others will withdraw  -> you must withdraw  -> bank fails (worst outcome)")
    print(f"Conclusion: Individually rational choices -> collectively catastrophic result")
    return results


# ILLUSTRATIVE inputs (same values as the function defaults above)
panic_levels = [0.05, 0.10, 0.15, 0.25, 0.50, 0.75, 1.00]
n_depositors = 1000
deposit_each = 10000
reserve_ratio = 0.10
fire_sale_penalty = 0.30

results_nash = bank_run_simulation(n_depositors, deposit_each, reserve_ratio,
                                   fire_sale_penalty, panic_levels)

# Depositors only start to lose money once the bank has sold ALL its loans:
# cash reserve + loans after the fire-sale discount = 10% + 90% x 70% = 73% of deposits.
loss_threshold = reserve_ratio + (1 - reserve_ratio) * (1 - fire_sale_penalty)
bad_recovery = [r for r in results_nash if r['panic'] == 1.0][0]['recovery']

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Coordination Game: The Self-Fulfilling Prophecy of Bank Runs\n'
             'Good equilibrium: no one panics -> bank safe | Bad equilibrium: everyone panics -> bank fails',
             fontsize=14, fontweight='bold')

# Panel 1: Loss rate vs panic level
ax = axes[0]
panics = [r['panic']*100 for r in results_nash]
losses = [r['loss']*100 for r in results_nash]
ax.plot(panics, losses, 'o-', color='#E74C3C', linewidth=2.5, markersize=8)
ax.fill_between(panics, losses, alpha=0.2, color='#E74C3C')
ax.axvline(x=reserve_ratio*100, color='green', linestyle='--', linewidth=2,
           label='Reserve ratio (10%): fire sales start')
ax.axvline(x=loss_threshold*100, color='purple', linestyle=':', linewidth=2,
           label=f'~{loss_threshold:.0%}: depositors start to lose money')
ax.set_xlabel('% of Depositors Withdrawing', fontsize=11)
ax.set_ylabel('Loss per Depositor (%)', fontsize=11)
ax.set_title('Loss vs Panic Level', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: Coordination game payoff sketch
ax = axes[1]
labels_m = [['Everyone holds\nBank safe\n$10,000 each',
             f'You hold, >{loss_threshold:.0%} run\nBank fails\nYou get $0'],
            ['You run, others hold\nBank safe\nYou get $10,000',
             f'Everyone runs\nBank fails\n${bad_recovery:,.0f} each']]
cell_colors = [['#27AE60', '#E74C3C'], ['#F39C12', '#E74C3C']]
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
for i in range(2):
    for j in range(2):
        rect = plt.Rectangle((j, 1-i), 1, 1, facecolor=cell_colors[i][j],
                             alpha=0.3, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(j+0.5, 1.5-i, labels_m[i][j], ha='center', va='center',
               fontsize=8, fontweight='bold')
ax.set_xticks([0.5, 1.5])
ax.set_xticklabels(['Others: HOLD', 'Others: RUN'], fontsize=10, fontweight='bold')
ax.set_yticks([0.5, 1.5])
ax.set_yticklabels(['You: RUN', 'You: HOLD'], fontsize=10, fontweight='bold')
ax.set_title("Coordination Game Payoffs\n(not a prisoner's dilemma: two equilibria)",
             fontsize=12, fontweight='bold')

# Panel 3: Two equilibria
ax = axes[2]
eq_labels = ['Good Equilibrium\n(Trust)', 'Bad Equilibrium\n(Panic)']
eq_values = [100, round(bad_recovery / deposit_each * 100)]  # % of deposits recovered: 100 and 73
eq_colors = ['#27AE60', '#E74C3C']
bars = ax.bar(eq_labels, eq_values, color=eq_colors, edgecolor='black', linewidth=2, width=0.5)
ax.set_ylabel('% of Deposits Recovered', fontsize=11)
ax.set_title('Two Possible Outcomes\n(Both Self-Fulfilling)', fontsize=12, fontweight='bold')
for bar, v in zip(bars, eq_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f'{v}%', ha='center', fontweight='bold', fontsize=14)
ax.set_ylim(0, 120)
ax.grid(axis='y', alpha=0.3)

fig.text(0.5, 0.0,
         'Illustrative inputs: 1,000 depositors x $10,000, 10% reserve, 30% fire-sale discount. '
         'The 27% loss at 100% withdrawal comes entirely from the assumed 30% discount.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('03_nash_equilibrium.png', dpi=300, bbox_inches='tight')  # file name kept: articles link to it
plt.close()
print("=> Saved: 03_nash_equilibrium.png")


# ============================================================
# MODEL 4: Deposit Insurance Effectiveness
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Deposit Insurance -- Breaking the Run Equilibrium")
print("=" * 65)

periods = ['1930-33\n(no FDIC)\n4 years', '1934-2000\n(FDIC era)\n67 years',
           '2008-10\n(crisis)\n3 years', 'Mar 2023\n(SVB, Signature)\n1 month']
# Period TOTALS, not per-year rates, so the bars cover different spans of time.
# Source: FDIC "Bank Failures in Brief" and BankFind failures data (FDIC API).
#   1930-33: about 9,000 US banks suspended operations (FDIC figures).
#   1934-2000: 3,530 failure/assistance records, concentrated in 1980-94 (1,600+ closed
#     or assisted); 1941-79 and 1995-2000 were mostly single digits a year.
#   2008-10: 322 failures.
#   Mar 2023: 2 (SVB, Signature). First Republic failed on 1 May 2023: 3 in all.
bank_failures = [9000, 3530, 322, 2]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Deposit Insurance: It Defuses Runs by Small Depositors\n'
             'After 1934, runs by insured depositors became rare | But it has a blind spot: uninsured deposits',
             fontsize=14, fontweight='bold')

ax = axes[0]
colors_f = ['#E74C3C', '#27AE60', '#F39C12', '#E74C3C']
bars = ax.bar(range(len(periods)), bank_failures, color=colors_f,
              edgecolor='black', linewidth=1)
ax.set_xticks(range(len(periods)))
ax.set_xticklabels(periods, fontsize=9)
ax.set_ylabel('Bank failures (period total, log scale)', fontsize=11)
ax.set_yscale('log')
ax.set_title('Bank Failures by Era (totals over different spans)', fontsize=12, fontweight='bold')
for bar, v in zip(bars, bank_failures):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.2,
            f'{v:,}', ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Insurance coverage gap
# Source: Barr, "Review of the Federal Reserve's Supervision and Regulation of SVB"
# (Apr 2023): about 94% of SVB's deposits were uninsured at end-2022 (S&P: 93.9%).
# The old "average US bank" bar (35% uninsured) had no source and was removed.
ax = axes[1]
banks_data = ['SVB\n(end-2022)']
insured_pct = [6]
uninsured_pct = [94]
x = np.arange(len(banks_data))
ax.bar(x, insured_pct, 0.5, color='#27AE60', alpha=0.8, label='Insured',
       edgecolor='black', linewidth=1)
ax.bar(x, uninsured_pct, 0.5, bottom=insured_pct, color='#E74C3C', alpha=0.8,
       label='Uninsured', edgecolor='black', linewidth=1)
ax.set_xlim(-1, 1)
ax.set_xticks(x)
ax.set_xticklabels(banks_data, fontsize=10)
ax.set_xlabel('FDIC limit: $250,000 per depositor, per insured bank, per ownership category',
              fontsize=9)
ax.set_ylabel('% of Deposits', fontsize=11)
ax.set_title('Insurance Coverage Gap', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
for i, (ins, unins) in enumerate(zip(insured_pct, uninsured_pct)):
    ax.text(i, ins/2 + 1, f'~{ins}%', ha='center', fontweight='bold', fontsize=11, color='black')
    ax.text(i, ins + unins/2, f'~{unins}%', ha='center', fontweight='bold', fontsize=11, color='white')

# Panel 3: Moral hazard trade-off (qualitative scores chosen by the author, not data)
ax = axes[2]
tradeoff = ['Panic\nReduction', 'Market\nDiscipline', 'Moral\nHazard Risk',
            'System\nStability']
with_fdic = [95, 30, 65, 85]
without_fdic = [10, 90, 15, 25]
x2 = np.arange(len(tradeoff))
ax.bar(x2 - 0.18, without_fdic, 0.35, color='#E74C3C', alpha=0.8, label='No Insurance',
       edgecolor='black', linewidth=1)
ax.bar(x2 + 0.18, with_fdic, 0.35, color='#27AE60', alpha=0.8, label='With FDIC',
       edgecolor='black', linewidth=1)
ax.set_xticks(x2)
ax.set_xticklabels(tradeoff, fontsize=9)
ax.set_ylabel('Score (0-100, qualitative)', fontsize=11)
ax.set_title('Trade-offs of Deposit Insurance\n(illustrative scores, not data)',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

fig.text(0.5, 0.0,
         'Sources: FDIC (failure counts); Fed Barr review (SVB uninsured share). '
         'Trade-off scores are illustrative judgements.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('04_deposit_insurance.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_deposit_insurance.png")


# ============================================================
# MODEL 5: SVB Collapse -- A Case Study
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: SVB Collapse -- Digital Age Bank Run")
print("=" * 65)

svb_timeline = ['End-2019', 'End-2020', 'End-2021\n(Peak)', 'End-2022\n(Rate hikes)',
                'Mar 8\n2023', 'Mar 9', 'Mar 10\n(Closed)']
# Deposits, USD billions.
# Source: SVB Financial Group SEC filings (year-end figures): 2019 61.7, 2020 102,
#   2021 189.2, 2022 173.
# The three March points are NOT reported figures:
#   Mar 8  = the end-2022 level, used as a proxy (last reported number);
#   Mar 9  = that level minus the $42bn withdrawn on 9 Mar (FDIC testimony; St. Louis Fed);
#   Mar 10 = 0 is schematic: California regulators closed the bank and the FDIC took
#            over, which does not mean the deposits vanished.
svb_deposits = [61.7, 102, 189.2, 173, 173, 173 - 42, 0]  # billions

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('SVB Collapse: Anatomy of a Digital Bank Run\n'
             '$42 billion withdrawn on 9 March | ~94% uninsured deposits (end-2022) | '
             'Closed in under 48 hours',
             fontsize=14, fontweight='bold')

# Panel 1: Deposit trajectory
ax = axes[0]
ax.plot(range(len(svb_timeline)), svb_deposits, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=8)
ax.fill_between(range(len(svb_timeline)), svb_deposits, alpha=0.2, color='#E74C3C')
ax.set_xticks(range(len(svb_timeline)))
ax.set_xticklabels(svb_timeline, fontsize=8)
ax.set_ylabel('Deposits ($B)', fontsize=11)
ax.set_title('SVB Deposit Trajectory\n(year-ends reported; March points derived, see note)',
             fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)
ax.annotate('$42B withdrawn\non 9 March', xy=(5, svb_deposits[5]), xytext=(3, 80),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, fontweight='bold', color='red')

# Panel 2: The interest rate trap
ax = axes[1]
# Upper bound of the federal funds target range at each date (FOMC):
# 1.50-1.75, 0-0.25, 0-0.25, 4.25-4.50, 4.50-4.75 (8 Mar 2023).
fed_rate = [1.75, 0.25, 0.25, 4.50, 4.75, 4.75, 4.75]
# ILLUSTRATIVE index: 100 = value before the rate hikes. The 17.5-point drop mirrors the
# ~$17.5bn unrealised loss quoted in the article; it is not scaled to the portfolio size.
bond_value = [100, 100, 100, 82.5, 82, 82, 82]
ax2 = ax.twinx()
ax.plot(range(len(svb_timeline)), fed_rate, 's-', color='#3498DB', linewidth=2.5,
        markersize=6, label='Fed Rate, upper bound of target range (%)')
ax2.plot(range(len(svb_timeline)), bond_value, 'o-', color='#E74C3C', linewidth=2.5,
         markersize=6, label='Bond Portfolio Value (illustrative index)')
ax.set_xticks(range(len(svb_timeline)))
ax.set_xticklabels(svb_timeline, fontsize=8)
ax.set_ylabel('Fed Rate (%)', fontsize=11, color='#3498DB')
ax2.set_ylabel('Bond Value (illustrative index)', fontsize=11, color='#E74C3C')
ax.set_title('The Interest Rate Trap', fontsize=12, fontweight='bold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, fontsize=8, loc='center right')
ax.grid(alpha=0.3)

# Panel 3: SVB risk factors (scores are the author's illustrative judgement, not measured)
ax = axes[2]
risk_factors = ['Client\nConcentration\n(Tech / VC)', 'Uninsured\nDeposits\n(~94%)',
                'Duration\nMismatch', 'Rate\nSensitivity', 'Social Media\nContagion']
risk_scores = [90, 95, 85, 88, 92]
colors_risk = plt.cm.Reds(np.linspace(0.3, 0.9, len(risk_factors)))
bars = ax.barh(range(len(risk_factors)), risk_scores, color=colors_risk,
               edgecolor='black', linewidth=1)
ax.set_yticks(range(len(risk_factors)))
ax.set_yticklabels(risk_factors, fontsize=8)
ax.set_xlabel('Risk Score (0-100, illustrative)', fontsize=11)
ax.set_title('SVB Risk Factor Analysis\n(illustrative scores, not data)',
             fontsize=12, fontweight='bold')
for bar, v in zip(bars, risk_scores):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 105)
ax.grid(axis='x', alpha=0.3)

fig.text(0.5, 0.0,
         'Sources: SVB SEC filings (year-end deposits), FDIC testimony and St. Louis Fed ($42B on 9 Mar), '
         'Fed Barr review (~94% uninsured). Mar 8 / Mar 9 / Mar 10 deposit points are derived or schematic.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('05_svb_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 05_svb_analysis.png")


# ============================================================
# MODEL 6: Contagion -- How One Bank's Failure Spreads
# ============================================================
print("\n" + "=" * 65)
print("MODEL 6: Contagion Network -- Bank Failure Spreads")
print("=" * 65)

import networkx as nx
from matplotlib.lines import Line2D

G = nx.Graph()
banks = ['SVB', 'Signature\nBank', 'First\nRepublic', 'Credit\nSuisse',
         'Regional\nBanks', 'Crypto\nLenders', 'Tech\nStartups', 'VC\nFunds']
G.add_nodes_from(banks)

# ILLUSTRATIVE network: the node set and the edge weights (1-10) are hand-set.
# Solid edges: plausible exposure or shared-depositor channels.
# Dashed edges: "confidence channel" only. No obvious direct financial linkage between
# SVB, Signature and Credit Suisse has been shown: SVB's collapse seems to have shaken
# confidence in banks generally, and Credit Suisse already had problems of its own.
exposure_edges = [
    ('SVB', 'Signature\nBank', 9), ('SVB', 'First\nRepublic', 8),
    ('SVB', 'Tech\nStartups', 10), ('SVB', 'VC\nFunds', 9),
    ('SVB', 'Regional\nBanks', 6), ('Signature\nBank', 'Crypto\nLenders', 8),
    ('First\nRepublic', 'Regional\nBanks', 7),
    ('VC\nFunds', 'Tech\nStartups', 8),
    ('Crypto\nLenders', 'Tech\nStartups', 5),
]
confidence_edges = [
    ('SVB', 'Credit\nSuisse', 4), ('Credit\nSuisse', 'Regional\nBanks', 5),
]
G.add_weighted_edges_from(exposure_edges + confidence_edges)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle("Bank Run Contagion: An Illustrative Network of Channels\n"
             "Fear travels through social networks, interbank lending, shared depositor bases "
             "and general loss of confidence",
             fontsize=14, fontweight='bold')

# Panel 1: Contagion network
ax = axes[0]
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
failed = ['SVB', 'Signature\nBank', 'First\nRepublic']  # SVB, Signature (Mar 2023), First Republic (1 May 2023)
node_colors = ['#E74C3C' if n in failed else '#F39C12' if n == 'Credit\nSuisse' else '#3498DB'
               for n in G.nodes()]
node_sizes = [1200 if n == 'SVB' else 800 for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors,
                       alpha=0.9, edgecolors='black', linewidths=2)
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u, v) for u, v, _ in exposure_edges],
                       width=[G[u][v]['weight'] * 0.3 for u, v, _ in exposure_edges],
                       alpha=0.4, edge_color='gray')
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u, v) for u, v, _ in confidence_edges],
                       width=[G[u][v]['weight'] * 0.3 for u, v, _ in confidence_edges],
                       alpha=0.8, edge_color='#F39C12', style='dashed')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=7, font_weight='bold')
ax.legend(handles=[Line2D([0], [0], color='gray', lw=2, label='Exposure / shared depositors'),
                   Line2D([0], [0], color='#F39C12', lw=2, ls='--',
                          label='Confidence channel (no direct link shown)')],
          fontsize=8, loc='lower left')
ax.set_title('Contagion Network (illustrative weights)', fontsize=12, fontweight='bold')
ax.axis('off')

# Panel 2: Contagion timeline. Days are counted from the trigger: the evening of 8 Mar 2023,
# when SVB announced its securities sale and capital raise (SVB 8-K, 8 Mar 2023).
# Dates: SVB closed 10 Mar, Signature closed 12 Mar, UBS agreed to buy Credit Suisse 19 Mar
# (CHF 3bn, Swiss Federal Department of Finance), First Republic failed 1 May.
# The "severity" values are hand-set and ILLUSTRATIVE.
ax = axes[1]
trigger = date(2023, 3, 8)
timeline = [
    ('SVB\nannounces\nloss', date(2023, 3, 8), 40),
    ('SVB run\nbegins', date(2023, 3, 9), 70),
    ('SVB\nclosed', date(2023, 3, 10), 100),
    ('Signature\nBank closed', date(2023, 3, 12), 85),
    ('First\nRepublic\nunder pressure', date(2023, 3, 13), 75),
    ('UBS agrees\nto buy\nCredit Suisse', date(2023, 3, 19), 90),
]
contagion_events = [t[0] for t in timeline]
days = [(t[1] - trigger).days for t in timeline]
severity = [t[2] for t in timeline]
first_republic_fails_day = (date(2023, 5, 1) - trigger).days
ax.plot(days, severity, 'o-', color='#E74C3C', linewidth=2.5, markersize=10)
for i, (d, s, e) in enumerate(zip(days, severity, contagion_events)):
    y_off = 8 if i % 2 == 0 else -12
    ax.annotate(e, (d, s), textcoords="offset points", xytext=(0, y_off),
                ha='center', fontsize=7, fontweight='bold')
ax.set_xlim(-0.8, 12.5)
ax.set_ylim(30, 112)
ax.text(0.98, 0.04, f'First Republic fails 1 May (day {first_republic_fails_day}, off the scale)',
        transform=ax.transAxes, ha='right', fontsize=8, style='italic')
ax.set_xlabel('Days After Initial Trigger (8 Mar 2023)', fontsize=11)
ax.set_ylabel('Severity Score (illustrative)', fontsize=11)
ax.set_title('Contagion Timeline', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

# Panel 3: Contagion channels (impact scores are illustrative judgements, not measured)
ax = axes[2]
channels = ['Social Media\nPanic', 'Interbank\nLending', 'Shared\nDepositors',
            'Investor\nFlight', 'Regulatory\nUncertainty']
channel_impact = [95, 70, 80, 85, 60]
colors_ch = ['#E74C3C', '#E67E22', '#F39C12', '#8E44AD', '#3498DB']
bars = ax.barh(channels, channel_impact, color=colors_ch, edgecolor='black', linewidth=1)
ax.set_xlabel('Impact Score (0-100, illustrative)', fontsize=11)
ax.set_title('Contagion Channels (illustrative scores)', fontsize=12, fontweight='bold')
for bar, v in zip(bars, channel_impact):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 110)
ax.grid(axis='x', alpha=0.3)

fig.text(0.5, 0.0,
         'Network weights, severity and impact scores are illustrative. Contagion mechanisms are an '
         'interpretation, not an established finding.',
         ha='center', va='bottom', fontsize=9, style='italic', color='#444444')
plt.tight_layout(rect=[0, 0.04, 1, 0.92], w_pad=3)
plt.savefig('06_contagion.png', dpi=300, bbox_inches='tight')
plt.close()
for d, e in zip(days, contagion_events):
    print(f"  day {d:>2}: {e.replace(chr(10), ' ')}")
print(f"  day {first_republic_fails_day:>2}: First Republic fails (1 May)")
print("=> Saved: 06_contagion.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
