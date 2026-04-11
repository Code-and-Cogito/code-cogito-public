"""
Finance, Bubbles & Crises #05: Bank Runs -- From Northern Rock to SVB
Free Version -- 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

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
             "Deposits: withdrawable anytime | Loans: 5-30 year terms | Reserve: only 3-10%",
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
ax.barh([1], [90], color='#E74C3C', alpha=0.8, label='Long-term Loans', left=10,
        edgecolor='black', linewidth=1.5, height=0.6)
ax.set_yticks([1, 2])
ax.set_yticklabels(['Assets', 'Liabilities'], fontsize=12, fontweight='bold')
ax.set_xlabel('Amount (%)', fontsize=11)
ax.set_title('Bank Balance Sheet', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper right')
ax.grid(axis='x', alpha=0.3)

# Panel 2: Time horizon mismatch
ax = axes[1]
items = ['Checking\nDeposits', 'Savings\nAccounts', 'CDs\n(1 year)', 'Mortgage\nLoans',
         'Business\nLoans', 'Government\nBonds']
durations = [0.01, 0.1, 1, 25, 5, 10]  # in years
colors_d = ['#3498DB', '#3498DB', '#2980B9', '#E74C3C', '#E67E22', '#F39C12']
bars = ax.barh(range(len(items)), durations, color=colors_d, edgecolor='black', linewidth=1)
ax.axvline(x=1, color='red', linestyle='--', linewidth=2, alpha=0.7, label='1 year mark')
ax.set_yticks(range(len(items)))
ax.set_yticklabels(items, fontsize=9)
ax.set_xlabel('Duration (years, log scale)', fontsize=11)
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
# Draw "seats" as dots
np.random.seed(42)
n_seats = 100
seat_x = np.random.uniform(-1.5, 1.5, n_seats)
seat_y = np.random.uniform(-1.2, 1.2, n_seats)
ax.scatter(seat_x, seat_y, s=30, color='#3498DB', alpha=0.6, label=f'{n_seats} depositors')
# Draw exits (only 2!)
ax.scatter([1.8, -1.8], [0, 0], s=300, color='#E74C3C', marker='s', zorder=5,
          edgecolors='black', linewidths=2)
ax.text(1.8, -0.3, 'EXIT 1\n(10%)', ha='center', fontsize=8, fontweight='bold', color='#E74C3C')
ax.text(-1.8, -0.3, 'EXIT 2\n(reserves)', ha='center', fontsize=8, fontweight='bold', color='#E74C3C')
ax.set_title('The Movie Theater Analogy\n1000 seats, 2 exits', fontsize=12, fontweight='bold')
ax.text(0, -1.8, 'Normal: slow orderly exit\nPanic: stampede -> everyone trapped',
        ha='center', fontsize=9, fontweight='bold', style='italic')
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_maturity_mismatch.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_maturity_mismatch.png")


# ============================================================
# MODEL 2: Bank Run Speed -- 150 Years of Acceleration
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Bank Run Speed Evolution (1866-2023)")
print("=" * 65)

events = ['Overend\nGurney\n1866', 'Great\nDepression\n1930-33', 'Continental\nIllinois\n1984',
          'Northern\nRock\n2007', 'SVB\n2023']
duration_hours = [336, 720, 168, 72, 48]  # approximate hours
withdrawal_rate = [0.5, 0.3, 6, 27.8, 87.5]  # $ per hour (normalized to 2023 $100M units)
info_channel = ['Newspaper', 'Newspaper\n+ Telegraph', 'Phone\n+ Wire', 'TV +\nInternet',
                'Social\nMedia +\nMobile']

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Bank Run Speed: 150 Years of Acceleration\n'
             '1866: 2 weeks | 2023: 48 hours | Speed increased 21x',
             fontsize=14, fontweight='bold')

# Panel 1: Duration bars
ax = axes[0]
colors_dur = plt.cm.RdYlGn_r(np.linspace(0.2, 0.9, len(events)))
bars = ax.barh(range(len(events)), duration_hours, color=colors_dur,
               edgecolor='black', linewidth=1)
ax.set_yticks(range(len(events)))
ax.set_yticklabels(events, fontsize=9)
ax.set_xlabel('Duration (hours)', fontsize=11)
ax.set_title('Time to Bank Failure', fontsize=12, fontweight='bold')
for bar, v in zip(bars, duration_hours):
    days = v / 24
    label = f'{days:.0f} days' if days >= 1 else f'{v:.0f} hrs'
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            label, va='center', fontweight='bold', fontsize=10)
ax.grid(axis='x', alpha=0.3)

# Panel 2: Withdrawal rate per hour
ax = axes[1]
ax.bar(range(len(events)), withdrawal_rate, color=colors_dur,
       edgecolor='black', linewidth=1)
ax.set_xticks(range(len(events)))
ax.set_xticklabels([e.split('\n')[0] for e in events], fontsize=9)
ax.set_ylabel('Withdrawal Rate (relative units/hr)', fontsize=11)
ax.set_title('Withdrawal Speed per Hour', fontsize=12, fontweight='bold')
ax.set_yscale('log')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Information channel evolution
ax = axes[2]
info_speed = [1, 5, 50, 500, 10000]  # relative info propagation speed
ax.plot(range(len(events)), info_speed, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=10, label='Info speed')
ax.plot(range(len(events)), [d/duration_hours[0]*info_speed[0] for d in reversed(duration_hours)],
        's-', color='#3498DB', linewidth=2.5, markersize=8, label='Run speed (inverse duration)')
ax.set_xticks(range(len(events)))
ax.set_xticklabels(info_channel, fontsize=7)
ax.set_ylabel('Relative Speed (log)', fontsize=11)
ax.set_yscale('log')
ax.set_title('Info Speed Drives Run Speed', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_bank_run_speed.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 02_bank_run_speed.png")


# ============================================================
# MODEL 3: Nash Equilibrium -- The Self-Fulfilling Prophecy
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Nash Equilibrium -- Self-Fulfilling Bank Run")
print("=" * 65)

panic_levels = [0.05, 0.10, 0.15, 0.25, 0.50, 0.75, 1.00]
n_depositors = 1000
deposit_each = 10000
reserve_ratio = 0.10
fire_sale_penalty = 0.30

total_deposits = n_depositors * deposit_each
cash_reserve = total_deposits * reserve_ratio
loans = total_deposits * (1 - reserve_ratio)

results_nash = []
for panic in panic_levels:
    withdrawers = int(n_depositors * panic)
    demand = withdrawers * deposit_each
    if demand <= cash_reserve:
        recovery = deposit_each
        loss = 0.0
        status = 'Safe'
    else:
        shortfall = demand - cash_reserve
        liquidated = min(shortfall / (1 - fire_sale_penalty), loans)
        recovered = liquidated * (1 - fire_sale_penalty)
        available = cash_reserve + recovered
        recovery = available / withdrawers if withdrawers > 0 else 0
        loss = 1 - (recovery / deposit_each)
        remaining = loans - liquidated
        status = 'Partial loss' if remaining > 0 else 'BANK FAILED'
    results_nash.append({'panic': panic, 'loss': loss, 'recovery': recovery, 'status': status})
    print(f"  {panic:>6.0%} withdraw: loss={loss:.1%}, recovery=${recovery:,.0f}, {status}")

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Nash Equilibrium: The Self-Fulfilling Prophecy of Bank Runs\n'
             'Good equilibrium: no one panics -> bank safe | Bad equilibrium: everyone panics -> bank dies',
             fontsize=14, fontweight='bold')

# Panel 1: Loss rate vs panic level
ax = axes[0]
panics = [r['panic']*100 for r in results_nash]
losses = [r['loss']*100 for r in results_nash]
ax.plot(panics, losses, 'o-', color='#E74C3C', linewidth=2.5, markersize=8)
ax.fill_between(panics, losses, alpha=0.2, color='#E74C3C')
ax.axvline(x=10, color='green', linestyle='--', linewidth=2, label='Reserve ratio (10%)')
ax.set_xlabel('% of Depositors Withdrawing', fontsize=11)
ax.set_ylabel('Loss per Depositor (%)', fontsize=11)
ax.set_title('Loss vs Panic Level', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

# Panel 2: Game theory payoff matrix
ax = axes[1]
matrix = np.array([[10000, 10000], [10000, 7300], [9963, 7300], [7300, 7300]])
labels_m = [['Everyone holds\nBank safe\n$10,000 each', 'You hold, others run\nBank fails\nYou get $0'],
            ['You run, others hold\nBank safe\nYou get $10,000', 'Everyone runs\nBank fails\n$7,300 each']]
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
ax.set_title("Prisoner's Dilemma Matrix", fontsize=12, fontweight='bold')

# Panel 3: Two equilibria
ax = axes[2]
eq_labels = ['Good Equilibrium\n(Trust)', 'Bad Equilibrium\n(Panic)']
eq_values = [100, 27]
eq_colors = ['#27AE60', '#E74C3C']
bars = ax.bar(eq_labels, eq_values, color=eq_colors, edgecolor='black', linewidth=2, width=0.5)
ax.set_ylabel('% of Deposits Recovered', fontsize=11)
ax.set_title('Two Possible Outcomes\n(Both Self-Fulfilling)', fontsize=12, fontweight='bold')
for bar, v in zip(bars, eq_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f'{v}%', ha='center', fontweight='bold', fontsize=14)
ax.set_ylim(0, 120)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_nash_equilibrium.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 03_nash_equilibrium.png")


# ============================================================
# MODEL 4: Deposit Insurance Effectiveness
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Deposit Insurance -- Breaking the Prisoner's Dilemma")
print("=" * 65)

periods = ['1930-33\n(No FDIC)', '1934-2000\n(FDIC)', '2008-10\n(Crisis)', '2023\n(SVB)']
bank_failures = [9000, 7, 322, 3]  # per year avg for 1934-2000
mass_runs = [True, False, False, True]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Deposit Insurance: The Most Effective Financial Innovation in History\n'
             'FDIC reduced bank failures from 9,000 to ~7/year | But has a blind spot: uninsured deposits',
             fontsize=14, fontweight='bold')

ax = axes[0]
colors_f = ['#E74C3C', '#27AE60', '#F39C12', '#E74C3C']
bars = ax.bar(range(len(periods)), bank_failures, color=colors_f,
              edgecolor='black', linewidth=1)
ax.set_xticks(range(len(periods)))
ax.set_xticklabels(periods, fontsize=9)
ax.set_ylabel('Bank Failures', fontsize=11)
ax.set_yscale('log')
ax.set_title('Bank Failures by Era', fontsize=12, fontweight='bold')
for bar, v in zip(bars, bank_failures):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.2,
            f'{v:,}', ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Insurance coverage gap
ax = axes[1]
banks_data = ['Average\nUS Bank', 'SVB\n(2023)', 'FDIC\nLimit']
insured_pct = [65, 7, 100]
uninsured_pct = [35, 93, 0]
x = np.arange(len(banks_data))
ax.bar(x, insured_pct, 0.5, color='#27AE60', alpha=0.8, label='Insured',
       edgecolor='black', linewidth=1)
ax.bar(x, uninsured_pct, 0.5, bottom=insured_pct, color='#E74C3C', alpha=0.8,
       label='Uninsured', edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(banks_data, fontsize=10)
ax.set_ylabel('% of Deposits', fontsize=11)
ax.set_title('Insurance Coverage Gap', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
for i, (ins, unins) in enumerate(zip(insured_pct, uninsured_pct)):
    if ins < 100:
        ax.text(i, ins/2, f'{ins}%', ha='center', fontweight='bold', fontsize=11, color='white')
    if unins > 0:
        ax.text(i, ins + unins/2, f'{unins}%', ha='center', fontweight='bold', fontsize=11, color='white')

# Panel 3: Moral hazard trade-off
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
ax.set_ylabel('Score (0-100)', fontsize=11)
ax.set_title('Trade-offs of Deposit Insurance', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_deposit_insurance.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_deposit_insurance.png")


# ============================================================
# MODEL 5: SVB Collapse -- A Case Study
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: SVB Collapse -- Digital Age Bank Run")
print("=" * 65)

svb_timeline = ['2019', '2020', '2021\n(Peak)', '2022\n(Rate hike)', 'Mar 8\n2023',
                'Mar 9', 'Mar 10\n(Failed)']
svb_deposits = [61.7, 102, 189.2, 173, 170, 128, 0]  # billions
svb_bond_loss = [0, 0, 0, -17.5, -18, -18, -18]  # unrealized losses

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('SVB Collapse: Anatomy of a Digital Bank Run\n'
             '$42 billion withdrawn in 24 hours | 93% uninsured deposits | Failed in 48 hours',
             fontsize=14, fontweight='bold')

# Panel 1: Deposit trajectory
ax = axes[0]
ax.plot(range(len(svb_timeline)), svb_deposits, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=8)
ax.fill_between(range(len(svb_timeline)), svb_deposits, alpha=0.2, color='#E74C3C')
ax.set_xticks(range(len(svb_timeline)))
ax.set_xticklabels(svb_timeline, fontsize=8)
ax.set_ylabel('Deposits ($B)', fontsize=11)
ax.set_title('SVB Deposit Trajectory', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)
ax.annotate('$42B withdrawn\nin 24 hours', xy=(5, 128), xytext=(3, 80),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, fontweight='bold', color='red')

# Panel 2: The interest rate trap
ax = axes[1]
fed_rate = [1.75, 0.25, 0.25, 4.25, 4.75, 4.75, 4.75]
bond_value = [100, 100, 100, 82.5, 82, 82, 82]
ax2 = ax.twinx()
ax.plot(range(len(svb_timeline)), fed_rate, 's-', color='#3498DB', linewidth=2.5,
        markersize=6, label='Fed Rate (%)')
ax2.plot(range(len(svb_timeline)), bond_value, 'o-', color='#E74C3C', linewidth=2.5,
         markersize=6, label='Bond Portfolio Value')
ax.set_xticks(range(len(svb_timeline)))
ax.set_xticklabels(svb_timeline, fontsize=8)
ax.set_ylabel('Fed Rate (%)', fontsize=11, color='#3498DB')
ax2.set_ylabel('Bond Value (index)', fontsize=11, color='#E74C3C')
ax.set_title('The Interest Rate Trap', fontsize=12, fontweight='bold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, fontsize=9)
ax.grid(alpha=0.3)

# Panel 3: SVB risk factors
ax = axes[2]
risk_factors = ['Client\nConcentration\n(Tech only)', 'Uninsured\nDeposits\n(93%)',
                'Duration\nMismatch', 'Rate\nSensitivity', 'Social Media\nContagion']
risk_scores = [90, 95, 85, 88, 92]
colors_risk = plt.cm.Reds(np.linspace(0.3, 0.9, len(risk_factors)))
bars = ax.barh(range(len(risk_factors)), risk_scores, color=colors_risk,
               edgecolor='black', linewidth=1)
ax.set_yticks(range(len(risk_factors)))
ax.set_yticklabels(risk_factors, fontsize=8)
ax.set_xlabel('Risk Score (0-100)', fontsize=11)
ax.set_title('SVB Risk Factor Analysis', fontsize=12, fontweight='bold')
for bar, v in zip(bars, risk_scores):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 105)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
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

G = nx.Graph()
banks = ['SVB', 'Signature\nBank', 'First\nRepublic', 'Credit\nSuisse',
         'Regional\nBanks', 'Crypto\nLenders', 'Tech\nStartups', 'VC\nFunds']
G.add_nodes_from(banks)

contagion_edges = [
    ('SVB', 'Signature\nBank', 9), ('SVB', 'First\nRepublic', 8),
    ('SVB', 'Tech\nStartups', 10), ('SVB', 'VC\nFunds', 9),
    ('SVB', 'Regional\nBanks', 6), ('Signature\nBank', 'Crypto\nLenders', 8),
    ('First\nRepublic', 'Regional\nBanks', 7),
    ('Credit\nSuisse', 'Regional\nBanks', 5),
    ('SVB', 'Credit\nSuisse', 4), ('VC\nFunds', 'Tech\nStartups', 8),
    ('Crypto\nLenders', 'Tech\nStartups', 5),
]
G.add_weighted_edges_from(contagion_edges)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Bank Run Contagion Network: How SVB\'s Failure Spread\n'
             'Fear travels through social networks, interbank lending, and shared depositor bases',
             fontsize=14, fontweight='bold')

# Panel 1: Contagion network
ax = axes[0]
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
failed = ['SVB', 'Signature\nBank', 'First\nRepublic']
node_colors = ['#E74C3C' if n in failed else '#F39C12' if n == 'Credit\nSuisse' else '#3498DB'
               for n in G.nodes()]
node_sizes = [1200 if n == 'SVB' else 800 for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors,
                       alpha=0.9, edgecolors='black', linewidths=2)
edge_weights = [G[u][v]['weight'] * 0.3 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, ax=ax, width=edge_weights, alpha=0.4, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=7, font_weight='bold')
ax.set_title('Contagion Network', fontsize=12, fontweight='bold')
ax.axis('off')

# Panel 2: Contagion timeline
ax = axes[1]
contagion_events = ['SVB\nannounces\nloss', 'SVB run\nbegins', 'SVB\nfails',
                    'Signature\nBank fails', 'First\nRepublic\nunder pressure',
                    'Credit\nSuisse\nacquired']
days = [0, 1, 2, 2, 5, 17]
severity = [40, 70, 100, 85, 75, 90]
ax.plot(days, severity, 'o-', color='#E74C3C', linewidth=2.5, markersize=10)
for i, (d, s, e) in enumerate(zip(days, severity, contagion_events)):
    y_off = 8 if i % 2 == 0 else -12
    ax.annotate(e, (d, s), textcoords="offset points", xytext=(0, y_off),
                ha='center', fontsize=7, fontweight='bold')
ax.set_xlabel('Days After Initial Trigger', fontsize=11)
ax.set_ylabel('Severity Score', fontsize=11)
ax.set_title('Contagion Timeline', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

# Panel 3: Contagion channels
ax = axes[2]
channels = ['Social Media\nPanic', 'Interbank\nLending', 'Shared\nDepositors',
            'Investor\nFlight', 'Regulatory\nUncertainty']
channel_impact = [95, 70, 80, 85, 60]
colors_ch = ['#E74C3C', '#E67E22', '#F39C12', '#8E44AD', '#3498DB']
bars = ax.barh(channels, channel_impact, color=colors_ch, edgecolor='black', linewidth=1)
ax.set_xlabel('Impact Score (0-100)', fontsize=11)
ax.set_title('Contagion Channels', fontsize=12, fontweight='bold')
for bar, v in zip(bars, channel_impact):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 110)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('06_contagion.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 06_contagion.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
