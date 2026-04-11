"""
Finance, Bubbles & Crises #06: FTX Collapse & The Bankruptcy of Trust (Finale)
Free Version -- 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Fund Flow -- Where Did $8 Billion Go?
# ============================================================
print("=" * 65)
print("MODEL 1: FTX Fund Flow -- Where Did $8 Billion Go?")
print("=" * 65)

categories = ['High-risk Crypto\nTrading', 'Bahamas\nReal Estate', 'Political\nDonations',
              'VC\nInvestments', 'Executive\nLoans']
amounts = [3.0, 0.256, 0.1, 2.0, 4.2]  # in billions (some overlap)
displayed = [3.0, 0.256, 0.1, 2.0, 2.644]  # adjusted to total ~8B

print(f"  Total client funds misappropriated: ~$8 billion")
for c, a in zip(categories, amounts):
    print(f"    {c.replace(chr(10), ' ')}: ${a:.3f}B")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('FTX Fund Flow: Where Did $8 Billion of Client Money Go?\n'
             'Not lost in trading -- stolen for speculation, real estate, politics, and self-enrichment',
             fontsize=14, fontweight='bold')

# Panel 1: Flow diagram (Sankey-style using bars)
ax = axes[0]
colors_flow = ['#E74C3C', '#E67E22', '#8E44AD', '#3498DB', '#2C3E50']
bars = ax.barh(range(len(categories)), displayed, color=colors_flow,
               edgecolor='black', linewidth=1.5)
ax.set_yticks(range(len(categories)))
ax.set_yticklabels(categories, fontsize=9)
ax.set_xlabel('Amount ($B)', fontsize=11)
ax.set_title('Client Fund Destinations', fontsize=12, fontweight='bold')
for bar, v in zip(bars, displayed):
    ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
            f'${v:.2f}B', va='center', fontweight='bold', fontsize=10)
ax.grid(axis='x', alpha=0.3)

# Panel 2: Governance failures
ax = axes[1]
governance_items = ['Independent\nBoard', 'Risk\nCommittee', 'Big-4\nAudit',
                    'Proper\nAccounting', 'Client Fund\nSeparation', 'Regulatory\nOversight']
traditional = [95, 90, 99, 95, 99, 85]
ftx_scores = [0, 0, 0, 5, 0, 10]
x = np.arange(len(governance_items))
w = 0.35
ax.bar(x - w/2, traditional, w, color='#27AE60', alpha=0.8, label='Traditional Exchange',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, ftx_scores, w, color='#E74C3C', alpha=0.8, label='FTX',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(governance_items, fontsize=8)
ax.set_ylabel('Compliance Score (0-100)', fontsize=11)
ax.set_title('Governance: Exchange vs FTX', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Timeline from Forbes cover to prison
ax = axes[2]
events = ['Forbes\nCover', 'Peak\n$32B', 'CoinDesk\nReport', 'Run\nBegins',
          'Bankrupt', 'Arrested', 'Sentenced\n25 years']
months = [0, 2, 7, 7.5, 7.7, 8.5, 18]
severity = [0, 10, 50, 80, 100, 95, 90]
colors_ev = ['#27AE60', '#3498DB', '#F39C12', '#E67E22', '#E74C3C', '#8B0000', '#2C3E50']
ax.scatter(months, severity, c=colors_ev, s=200, zorder=5, edgecolors='black', linewidths=1.5)
ax.plot(months, severity, '-', color='gray', linewidth=1.5, alpha=0.5)
for m, s, e, c in zip(months, severity, events, colors_ev):
    y_off = 8 if s < 90 else -15
    ax.annotate(e, (m, s), textcoords="offset points", xytext=(0, y_off),
                ha='center', fontsize=8, fontweight='bold', color=c)
ax.set_xlabel('Months from Forbes Cover (Apr 2022)', fontsize=11)
ax.set_ylabel('Crisis Severity', fontsize=11)
ax.set_title('From Cover to Prison: 18 Months', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_fund_flow.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_fund_flow.png")


# ============================================================
# MODEL 2: Leverage Tower -- FTT Circular Dependency
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Leverage Tower -- FTT Circular Dependency Collapse")
print("=" * 65)

ftt_initial_price = 25.0
total_ftt = 350_000_000
alameda_ftt = total_ftt * 0.40
collateral_ratio = 0.80
initial_value = alameda_ftt * ftt_initial_price
borrowed = initial_value * collateral_ratio

price_drops = [0.0, -0.10, -0.20, -0.30, -0.40, -0.50, -0.70, -0.90]
tower_data = []
for drop in price_drops:
    price = ftt_initial_price * (1 + drop)
    collateral = alameda_ftt * price
    coverage = collateral / borrowed if borrowed > 0 else 0
    gap = collateral - borrowed
    if coverage >= 1.0:
        status = 'Safe'
    elif coverage >= 0.5:
        status = 'Margin Call'
    elif coverage > 0:
        status = 'Forced Liquidation'
    else:
        status = 'Total Collapse'
    tower_data.append({'drop': drop, 'price': price, 'collateral': collateral/1e9,
                      'coverage': coverage, 'gap': gap/1e9, 'status': status})
    print(f"  FTT ${price:.2f} ({drop:+.0%}): coverage={coverage:.0%}, "
          f"gap={gap/1e9:+.2f}B, {status}")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('FTX-Alameda Leverage Tower: Circular Dependency Collapse\n'
             'FTX creates FTT -> gives to Alameda -> Alameda borrows against FTT -> money back to FTX',
             fontsize=14, fontweight='bold')

# Panel 1: Collateral vs Debt
ax = axes[0]
drops_pct = [abs(d)*100 for d in price_drops]
collaterals = [t['collateral'] for t in tower_data]
ax.plot(drops_pct, collaterals, 'o-', color='#E74C3C', linewidth=2.5, markersize=8,
        label='Collateral Value')
ax.axhline(y=borrowed/1e9, color='#2C3E50', linestyle='--', linewidth=2,
           label=f'Borrowed: ${borrowed/1e9:.2f}B')
ax.fill_between(drops_pct, collaterals, borrowed/1e9, alpha=0.2,
                where=[c < borrowed/1e9 for c in collaterals], color='#E74C3C')
ax.set_xlabel('FTT Price Drop (%)', fontsize=11)
ax.set_ylabel('Value ($B)', fontsize=11)
ax.set_title('Collateral vs Debt', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

# Panel 2: Coverage ratio
ax = axes[1]
coverages = [t['coverage']*100 for t in tower_data]
colors_cov = ['#27AE60' if c >= 100 else '#F39C12' if c >= 50 else '#E74C3C' for c in coverages]
bars = ax.bar(range(len(price_drops)), coverages, color=colors_cov,
              edgecolor='black', linewidth=1)
ax.axhline(y=100, color='green', linestyle='--', linewidth=2, label='Full coverage')
ax.axhline(y=50, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Margin call')
ax.set_xticks(range(len(price_drops)))
ax.set_xticklabels([f'{d:.0%}' for d in price_drops], fontsize=9)
ax.set_xlabel('FTT Price Change', fontsize=11)
ax.set_ylabel('Coverage Ratio (%)', fontsize=11)
ax.set_title('Coverage Ratio Collapse', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Death spiral diagram
ax = axes[2]
spiral_steps = ['FTT price\ndrops', 'Alameda\ncollateral\ninsufficient',
                'Margin\ncall', 'Forced to\nsell FTT', 'FTT price\ndrops more',
                'Alameda\nbankrupt', 'FTX\nbankrupt']
angles_sp = np.linspace(0, 2*np.pi*1.5, len(spiral_steps))
radii = np.linspace(1.5, 0.3, len(spiral_steps))
x_sp = radii * np.cos(angles_sp)
y_sp = radii * np.sin(angles_sp)
colors_sp = plt.cm.Reds(np.linspace(0.3, 0.95, len(spiral_steps)))
for i in range(len(spiral_steps)):
    ax.scatter(x_sp[i], y_sp[i], s=600, color=colors_sp[i], zorder=5,
              edgecolors='black', linewidths=1.5)
    ax.text(x_sp[i], y_sp[i], spiral_steps[i], ha='center', va='center',
           fontsize=6, fontweight='bold')
    if i < len(spiral_steps) - 1:
        ax.annotate('', xy=(x_sp[i+1], y_sp[i+1]), xytext=(x_sp[i], y_sp[i]),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
ax.set_title('Death Spiral Mechanism', fontsize=12, fontweight='bold')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_leverage_tower.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 02_leverage_tower.png")


# ============================================================
# MODEL 3: Trust Network -- Everyone Failed
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Trust Network -- All Gatekeepers Failed")
print("=" * 65)

G = nx.DiGraph()
actors = {
    'SBF/FTX': {'role': 'Perpetrator', 'color': '#E74C3C'},
    'Alameda': {'role': 'Accomplice', 'color': '#E74C3C'},
    'VCs\n(Sequoia etc)': {'role': 'Failed Oversight', 'color': '#E67E22'},
    'Auditors': {'role': 'Failed Verification', 'color': '#E67E22'},
    'Celebrities': {'role': 'Sold Trust', 'color': '#F39C12'},
    'Politicians': {'role': 'Captured', 'color': '#F39C12'},
    'Media': {'role': 'Amplified Hype', 'color': '#F39C12'},
    'Regulators': {'role': 'Outmaneuvered', 'color': '#8E44AD'},
    'Customers': {'role': 'Victims', 'color': '#3498DB'},
}

for name, attrs in actors.items():
    G.add_node(name, **attrs)

trust_flows = [
    ('Customers', 'SBF/FTX', 'Deposited $8B'),
    ('SBF/FTX', 'Alameda', 'Transferred funds'),
    ('VCs\n(Sequoia etc)', 'SBF/FTX', 'Invested $2B+'),
    ('Auditors', 'SBF/FTX', 'Signed off'),
    ('Celebrities', 'Customers', 'Endorsed'),
    ('Politicians', 'SBF/FTX', 'Legitimized'),
    ('Media', 'Customers', 'Hyped'),
    ('Regulators', 'SBF/FTX', 'Could not reach'),
    ('SBF/FTX', 'Politicians', 'Donated $100M+'),
]
G.add_edges_from([(u, v) for u, v, _ in trust_flows])

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Trust Network: Every Gatekeeper Failed\n'
             'SBF didn\'t fool one person -- he fooled the entire system',
             fontsize=14, fontweight='bold')

# Panel 1: Network graph
ax = axes[0]
pos = nx.spring_layout(G, k=2.5, iterations=80, seed=42)
node_colors = [actors[n]['color'] for n in G.nodes()]
node_sizes = [1500 if n == 'SBF/FTX' else 1000 if n == 'Customers' else 800 for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors,
                       alpha=0.9, edgecolors='black', linewidths=2)
nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.4, edge_color='gray',
                       arrows=True, arrowsize=15, width=1.5)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=7, font_weight='bold')
ax.set_title('Trust Flow Network', fontsize=12, fontweight='bold')
ax.axis('off')

# Panel 2: Gatekeeper failure scores
ax = axes[1]
gatekeepers = ['VCs', 'Auditors', 'Celebrities', 'Politicians', 'Media', 'Regulators']
should_have = [90, 95, 50, 80, 70, 85]
actually_did = [5, 5, 0, 10, 10, 15]
x = np.arange(len(gatekeepers))
w = 0.35
ax.bar(x - w/2, should_have, w, color='#27AE60', alpha=0.6, label='Should have caught',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, actually_did, w, color='#E74C3C', alpha=0.8, label='Actually did',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(gatekeepers, fontsize=10)
ax.set_ylabel('Due Diligence Score (0-100)', fontsize=11)
ax.set_title('Gatekeeper Performance', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Why no one looked
ax = axes[2]
reasons = ['Story too\ngood', 'Everyone\ninvested', 'Regulatory\narbitrage',
           'Herd\nmentality', 'Perverse\nincentives']
reason_scores = [92, 85, 88, 80, 90]
colors_r = plt.cm.Oranges(np.linspace(0.3, 0.9, len(reasons)))
bars = ax.barh(reasons, reason_scores, color=colors_r, edgecolor='black', linewidth=1)
ax.set_xlabel('Contribution Score (0-100)', fontsize=11)
ax.set_title('Why Nobody Looked Closely', fontsize=12, fontweight='bold')
for bar, v in zip(bars, reason_scores):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 105)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_trust_network.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 03_trust_network.png")


# ============================================================
# MODEL 4: Regulatory Arbitrage -- The Bahamas Loophole
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Regulatory Arbitrage -- Bahamas vs US")
print("=" * 65)

regs = ['Client Fund\nSeparation', 'Independent\nAudit', 'Capital\nRequirements',
        'Risk\nReporting', 'Executive\nTrading Limits', 'Regulator\nEnforcement']
us_scores = [95, 98, 90, 85, 80, 88]
bahamas_scores = [10, 15, 20, 10, 5, 15]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Regulatory Arbitrage: Why FTX Chose the Bahamas\n'
             '"Decentralization" was never about freedom -- it was about avoiding rules',
             fontsize=14, fontweight='bold')

# Panel 1: US vs Bahamas comparison
ax = axes[0]
x = np.arange(len(regs))
w = 0.35
ax.bar(x - w/2, us_scores, w, color='#27AE60', alpha=0.8, label='US (SEC/CFTC)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, bahamas_scores, w, color='#E74C3C', alpha=0.8, label='Bahamas',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(regs, fontsize=8)
ax.set_ylabel('Regulatory Score (0-100)', fontsize=11)
ax.set_title('Regulatory Environment', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Cost of no regulation
ax = axes[1]
cost_items = ['Client Funds\nLost', 'Investor\nLosses', 'Market Cap\nDestroyed',
              'Confidence\nDamage']
cost_values = [8, 2.14, 320, 2000]  # in $B
colors_cost = ['#E74C3C', '#E67E22', '#8E44AD', '#2C3E50']
bars = ax.bar(cost_items, cost_values, color=colors_cost, edgecolor='black', linewidth=1)
ax.set_ylabel('Cost ($B)', fontsize=11)
ax.set_yscale('log')
ax.set_title('Cost of Regulatory Failure', fontsize=12, fontweight='bold')
for bar, v in zip(bars, cost_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.3,
            f'${v}B', ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Crypto's regulatory paradox
ax = axes[2]
paradox_labels = ['Crypto\nPromise', 'Crypto\nReality']
trust_needed = [0, 100]  # promise: no trust needed; reality: maximum trust
transparency = [100, 5]
regulation = [0, 0]
x2 = np.arange(len(paradox_labels))
ax.bar(x2 - 0.25, trust_needed, 0.24, color='#E74C3C', alpha=0.8, label='Trust Required',
       edgecolor='black', linewidth=1)
ax.bar(x2, transparency, 0.24, color='#3498DB', alpha=0.8, label='Actual Transparency',
       edgecolor='black', linewidth=1)
ax.bar(x2 + 0.25, regulation, 0.24, color='#27AE60', alpha=0.8, label='Regulation',
       edgecolor='black', linewidth=1)
ax.set_xticks(x2)
ax.set_xticklabels(paradox_labels, fontsize=11, fontweight='bold')
ax.set_ylabel('Score (0-100)', fontsize=11)
ax.set_title("Crypto's Trust Paradox", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)
ax.text(0, 55, '"Don\'t trust,\nverify"', ha='center', fontsize=10, fontweight='bold',
        color='#27AE60')
ax.text(1, 55, '"Just trust\nSBF"', ha='center', fontsize=10, fontweight='bold',
        color='#E74C3C')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_regulatory_arbitrage.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_regulatory_arbitrage.png")


# ============================================================
# MODEL 5: Crypto Contagion Chain (2022)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Crypto Contagion Chain -- 2022 Domino Effect")
print("=" * 65)

dominoes = ['Terra/Luna\nMay 2022', 'Three Arrows\nCapital\nJun 2022',
            'Celsius\nJun 2022', 'Voyager\nJul 2022', 'FTX\nNov 2022']
value_destroyed = [40, 10, 4.7, 5, 32]  # in $B
cumulative = np.cumsum(value_destroyed)
days_between = [0, 30, 7, 30, 120]
cumulative_days = np.cumsum(days_between)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('2022 Crypto Contagion: $91.7 Billion Domino Chain\n'
             'Terra -> Three Arrows -> Celsius -> Voyager -> FTX | Each failure made the next worse',
             fontsize=14, fontweight='bold')

# Panel 1: Value destroyed per event
ax = axes[0]
colors_dom = plt.cm.Reds(np.linspace(0.3, 0.9, len(dominoes)))
bars = ax.bar(range(len(dominoes)), value_destroyed, color=colors_dom,
              edgecolor='black', linewidth=1.5)
ax.set_xticks(range(len(dominoes)))
ax.set_xticklabels(dominoes, fontsize=8)
ax.set_ylabel('Value Destroyed ($B)', fontsize=11)
ax.set_title('Value Destroyed Per Event', fontsize=12, fontweight='bold')
for bar, v in zip(bars, value_destroyed):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'${v}B', ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Cumulative destruction
ax = axes[1]
ax.plot(cumulative_days, cumulative, 'o-', color='#E74C3C', linewidth=2.5, markersize=10)
ax.fill_between(cumulative_days, cumulative, alpha=0.2, color='#E74C3C')
for d, c, name in zip(cumulative_days, cumulative, [n.split('\n')[0] for n in dominoes]):
    ax.annotate(f'{name}\n${c:.0f}B', (d, c), textcoords="offset points",
                xytext=(10, 5), fontsize=8, fontweight='bold')
ax.set_xlabel('Days from First Collapse', fontsize=11)
ax.set_ylabel('Cumulative Destruction ($B)', fontsize=11)
ax.set_title('Cumulative Value Destruction', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

# Panel 3: Causal chain
ax = axes[2]
causes = [
    'Terra/Luna\ncollapses',
    '3AC had huge\nTerra position',
    'Celsius lent\nto 3AC',
    'Voyager lent\nto 3AC',
    'Alameda losses\nescalated'
]
y_pos = np.linspace(0.9, 0.1, len(causes))
for i, (cause, y) in enumerate(zip(causes, y_pos)):
    color = colors_dom[i]
    ax.scatter(0.5, y, s=800, color=color, zorder=5, edgecolors='black', linewidths=1.5)
    ax.text(0.5, y, cause, ha='center', va='center', fontsize=7, fontweight='bold')
    if i < len(causes) - 1:
        ax.annotate('', xy=(0.5, y_pos[i+1] + 0.05), xytext=(0.5, y - 0.05),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('Causal Chain', fontsize=12, fontweight='bold')
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_crypto_contagion.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"  Total value destroyed: ${sum(value_destroyed):.1f}B")
print(f"  Timeline: {sum(days_between)} days (May-Nov 2022)")
print("=> Saved: 05_crypto_contagion.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
