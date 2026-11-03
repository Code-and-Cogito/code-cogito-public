"""
Finance, Bubbles & Crises #06: FTX Collapse & The Bankruptcy of Trust (Finale)
Free Version -- 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy

ABOUT THE NUMBERS
-----------------
Only a few inputs below are documented real-world figures; each has a source
note next to it. Most bar heights, scores and indices are HAND-SET
illustrations chosen to show a mechanism -- they are not measured data, not a
ledger, and not Alameda's or FTX's actual books. The chart titles say so.
"""

from datetime import date

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Fund Flow (illustrative) -- Where Did the Money Go?
# ============================================================
print("=" * 65)
print("MODEL 1: FTX Fund Flow (illustrative) -- Where Did the Money Go?")
print("=" * 65)

# Rows are rough, OVERLAPPING estimates on DIFFERENT bases (press reports and
# prosecutors' allegations). They are not a ledger and do not add up to $8B.
# (label, amount in $B, basis)
fund_rows = [
    ('High-risk Crypto\nTrading', 3.0,
     'hand-set placeholder (no reliable single figure)'),
    ('Bahamas\nReal Estate', 0.256,
     'about $250-300M; $256M in a Dec 2022 report, estimates vary'),
    ('Political\nDonations', 0.1,
     'over $100M alleged by prosecutors to be customer-funded; about $40M publicly disclosed'),
    ('VC\nInvestments', 2.0,
     "about $2B of equity stakes on Alameda's June 2022 balance sheet"),
    ('Loans to insiders\nand their entities', 4.1,
     '$4.1B related-party loans per the Ray declaration (about $1.6B to three individuals, '
     'about $2.3B to SBF-linked entities)'),
]
categories = [r[0] for r in fund_rows]
amounts = [r[1] for r in fund_rows]  # in billions; overlapping, mixed bases

print("  Prosecutors said more than $8 billion of customer money was taken")
print("  (that is NOT the sum of the rows below).")
print("  Illustrative amounts (overlapping, different bases -- not a ledger):")
for c, a, basis in fund_rows:
    print(f"    {c.replace(chr(10), ' ')}: ${a:.3f}B  [{basis}]")
print(f"  The rows add up to ${sum(amounts):.3f}B, more than $8B, because the categories "
      f"overlap and the bases differ.")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('FTX Fund Flow (illustrative): Where Did the Money Go?\n'
             'Prosecutors said more than $8B of customer money was taken -- the bars are rough, '
             'overlapping estimates on different bases, not a ledger',
             fontsize=14, fontweight='bold')

# Panel 1: Flow diagram (Sankey-style using bars)
ax = axes[0]
colors_flow = ['#E74C3C', '#E67E22', '#8E44AD', '#3498DB', '#2C3E50']
bars = ax.barh(range(len(categories)), amounts, color=colors_flow,
               edgecolor='black', linewidth=1.5)
bars[0].set_hatch('//')  # hatched = hand-set placeholder
ax.set_yticks(range(len(categories)))
ax.set_yticklabels(categories, fontsize=9)
ax.invert_yaxis()
ax.set_xlabel('Amount ($B, rough estimate)', fontsize=11)
ax.set_title('Illustrative Fund Destinations\n(overlapping; hatched bar = placeholder)',
             fontsize=12, fontweight='bold')
for bar, v in zip(bars, amounts):
    ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
            f'${v:.2f}B', va='center', fontweight='bold', fontsize=10)
ax.set_xlim(0, max(amounts) * 1.2)
ax.grid(axis='x', alpha=0.3)

# Panel 2: Governance failures (hand-set scores)
ax = axes[1]
governance_items = ['Independent\nBoard', 'Risk\nManagement', 'Audit\nQuality',
                    'Proper\nAccounting', 'Client Fund\nSeparation', 'Outside\nOversight']
traditional = [95, 90, 99, 95, 99, 85]   # hand-set, typical regulated exchange
ftx_scores = [0, 0, 0, 5, 0, 10]         # hand-set; FTX had two non-Big-Four auditors (quality later questioned)
x = np.arange(len(governance_items))
w = 0.35
ax.bar(x - w/2, traditional, w, color='#27AE60', alpha=0.8, label='Traditional exchange (typical)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, ftx_scores, w, color='#E74C3C', alpha=0.8, label='FTX',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(governance_items, fontsize=8)
ax.set_ylabel('Illustrative score (0-100, hand-set)', fontsize=11)
ax.set_title('Governance: Exchange vs FTX\n(hand-set scores, not measured data)',
             fontsize=12, fontweight='bold')
ax.set_ylim(0, 125)
ax.legend(fontsize=10, loc='upper right')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Timeline from the Fortune cover story to prison
# Dates: Fortune cover story 1 Aug 2022 (August/September issue); CoinDesk report 2 Nov 2022;
# CZ's FTT tweet / start of the run 6 Nov (withdrawals halted 8 Nov); Chapter 11 filing 11 Nov;
# arrest in Nassau 12 Dec 2022; 25-year sentence 28 Mar 2024 (US DOJ). The $32B valuation was
# a January 2022 funding round (month precision only). Severity values are hand-set.
ax = axes[2]
cover_date = date(2022, 8, 1)
timeline = [
    # (label, date, hand-set severity, label offset in points, text alignment)
    ('$32B\nvaluation', date(2022, 1, 15), 5, (0, 9), 'center'),
    ('Fortune\ncover story', cover_date, 10, (0, 9), 'center'),
    ('CoinDesk\nReport', date(2022, 11, 2), 50, (-12, -4), 'right'),
    ('Run\nBegins', date(2022, 11, 6), 80, (-12, -4), 'right'),
    ('Chapter 11\nfiling', date(2022, 11, 11), 100, (-12, -4), 'right'),
    ('Arrested', date(2022, 12, 12), 95, (12, -10), 'left'),
    ('Sentenced\n25 years', date(2024, 3, 28), 90, (0, -30), 'center'),
]
events = [t[0] for t in timeline]
months = [(t[1] - cover_date).days / 30.44 for t in timeline]  # months from the cover story
severity = [t[2] for t in timeline]
colors_ev = ['#3498DB', '#27AE60', '#F39C12', '#E67E22', '#E74C3C', '#8B0000', '#2C3E50']
ax.scatter(months, severity, c=colors_ev, s=200, zorder=5, edgecolors='black', linewidths=1.5)
ax.plot(months, severity, '-', color='gray', linewidth=1.5, alpha=0.5)
for (label, _, s, off, ha), m, c in zip(timeline, months, colors_ev):
    ax.annotate(label, (m, s), textcoords="offset points", xytext=off,
                ha=ha, fontsize=8, fontweight='bold', color=c)
ax.set_xlabel('Months from the Fortune cover story (1 Aug 2022)', fontsize=11)
ax.set_ylabel('Crisis severity (hand-set index)', fontsize=11)
ax.set_ylim(-5, 115)
ax.set_title(f'From Cover to Prison: about {round(months[-1])} Months',
             fontsize=12, fontweight='bold')
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

# ILLUSTRATIVE ASSUMPTIONS -- NOT Alameda's actual books.
# For scale: the Alameda balance sheet CoinDesk reported (dated 30 June 2022) showed
# about $5.8B of FTT (some 40% of roughly $14.6B in assets), versus $3.5B in this model.
ftt_initial_price = 25.0                 # FTT traded at about $24 on 6 Nov 2022 (Yahoo Finance daily data)
total_ftt = 350_000_000                  # FTT supply was roughly 352M; 350M is a round number
alameda_ftt = total_ftt * 0.40           # assumption: Alameda holds 40% of the supply
collateral_ratio = 0.80                  # assumption: borrowed = 80% of the initial collateral value
liquidation_line = 0.50                  # assumption: coverage below 50% = forced liquidation
initial_value = alameda_ftt * ftt_initial_price
borrowed = initial_value * collateral_ratio

print(f"  Initial collateral value: ${initial_value/1e9:.2f}B   Borrowed funds: ${borrowed/1e9:.2f}B")
print(f"  Coverage below 100% = margin call; below {liquidation_line:.0%} = forced liquidation")
print("  (hypothetical scenario: Alameda holds 40% of FTT, 80% collateral ratio, 50% liquidation line)")

price_drops = [0.0, -0.10, -0.20, -0.30, -0.40, -0.50, -0.70, -0.90]
tower_data = []
for drop in price_drops:
    price = ftt_initial_price * (1 + drop)
    collateral = alameda_ftt * price
    coverage = collateral / borrowed if borrowed > 0 else 0
    gap = collateral - borrowed
    if coverage >= 1.0:
        status = 'Safe'
    elif coverage >= liquidation_line:
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
fig.suptitle("FTX-Alameda Leverage Tower (illustrative model, not Alameda's books)\n"
             "FTX creates FTT -> Alameda holds FTT -> borrows against it -> "
             "FTT is worth only as much as FTX's own credit",
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
colors_cov = ['#27AE60' if c >= 100 else '#F39C12' if c >= liquidation_line*100 else '#E74C3C'
              for c in coverages]
bars = ax.bar(range(len(price_drops)), coverages, color=colors_cov,
              edgecolor='black', linewidth=1)
ax.axhline(y=100, color='green', linestyle='--', linewidth=2,
           label='100%: below = margin call')
ax.axhline(y=liquidation_line*100, color='red', linestyle='--', linewidth=1.5, alpha=0.7,
           label=f'{liquidation_line:.0%}: below = forced liquidation')
ax.set_xticks(range(len(price_drops)))
ax.set_xticklabels([f'{d:.0%}' for d in price_drops], fontsize=9)
ax.set_xlabel('FTT Price Change', fontsize=11)
ax.set_ylabel('Coverage Ratio (%)', fontsize=11)
ax.set_title('Coverage Ratio Collapse', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Death spiral diagram (stylised; model assumption: FTT is the only asset Alameda can sell,
# whereas in reality it held other assets too)
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
    ax.scatter(x_sp[i], y_sp[i], s=3000, color=colors_sp[i], zorder=5,
              edgecolors='black', linewidths=1.5)
    ax.text(x_sp[i], y_sp[i], spiral_steps[i], ha='center', va='center',
           fontsize=6.5, fontweight='bold', zorder=6,
           color='white' if i >= 4 else 'black')
    if i < len(spiral_steps) - 1:
        ax.annotate('', xy=(x_sp[i+1], y_sp[i+1]), xytext=(x_sp[i], y_sp[i]),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
ax.set_title('Death Spiral Mechanism (stylised)', fontsize=12, fontweight='bold')
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
    'Regulators': {'role': 'Thin Oversight', 'color': '#8E44AD'},
    'Customers': {'role': 'Victims', 'color': '#3498DB'},
}

for name, attrs in actors.items():
    G.add_node(name, **attrs)

# The third item of each tuple is documentation only (edge labels are not drawn).
trust_flows = [
    ('Customers', 'SBF/FTX', 'Deposits (prosecutors: more than $8B of customer money taken)'),
    ('SBF/FTX', 'Alameda', 'Transferred funds'),
    ('VCs\n(Sequoia etc)', 'SBF/FTX', 'Equity investments (e.g. Sequoia about $214M)'),
    ('Auditors', 'SBF/FTX', 'Audited by two non-Big-Four firms (quality later questioned)'),
    ('Celebrities', 'Customers', 'Endorsed'),
    ('Politicians', 'SBF/FTX', 'Legitimized'),
    ('Media', 'Customers', 'Hyped'),
    ('Regulators', 'SBF/FTX', 'Thin, fragmented oversight'),
    ('SBF/FTX', 'Politicians', 'Donations (about $40M publicly disclosed; $100M+ alleged by prosecutors)'),
]
G.add_edges_from([(u, v) for u, v, _ in trust_flows])

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Trust Network: Every Gatekeeper Failed (stylised sketch; the scores are hand-set judgements)\n'
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

# Panel 2: Gatekeeper failure scores (hand-set judgements)
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
ax.set_ylabel('Due Diligence Score (0-100, hand-set)', fontsize=11)
ax.set_title('Gatekeeper Performance\n(hand-set judgement, not measured data)',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Why no one looked (hand-set judgements)
ax = axes[2]
reasons = ['Story too\ngood', 'Everyone\ninvested', 'Regulatory\narbitrage',
           'Herd\nmentality', 'Perverse\nincentives']
reason_scores = [92, 85, 88, 80, 90]
colors_r = plt.cm.Oranges(np.linspace(0.3, 0.9, len(reasons)))
bars = ax.barh(reasons, reason_scores, color=colors_r, edgecolor='black', linewidth=1)
ax.set_xlabel('Contribution Score (0-100, hand-set)', fontsize=11)
ax.set_title('Why Nobody Looked Closely\n(hand-set judgement, not measured data)',
             fontsize=12, fontweight='bold')
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
# MODEL 4: Regulatory Arbitrage -- Offshore vs US
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Regulatory Arbitrage -- Offshore (Antigua/Bahamas) vs US")
print("=" * 65)

# Scores are HAND-SET illustrations of the critics' reading (thin, fragmented offshore oversight);
# they are not measured regulatory data. FTX itself argued that the Bahamian rules were clearer
# than the US ones (FTX Digital Markets held a licence under the 2020 DARE Act).
regs = ['Client Fund\nSeparation', 'Independent\nAudit', 'Capital\nRequirements',
        'Risk\nReporting', 'Conflict-of-\nInterest Rules', 'Regulator\nEnforcement']
us_scores = [95, 98, 90, 85, 80, 88]
offshore_scores = [10, 15, 20, 10, 5, 15]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("Regulatory Arbitrage (the critics' view): Why FTX Went Offshore\n"
             "Hand-set illustrative scores, not measured data -- FTX itself argued the Bahamian rules were "
             "clearer than the US ones",
             fontsize=14, fontweight='bold')

# Panel 1: US vs offshore comparison
ax = axes[0]
x = np.arange(len(regs))
w = 0.35
ax.bar(x - w/2, us_scores, w, color='#27AE60', alpha=0.8, label='US (SEC/CFTC)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, offshore_scores, w, color='#E74C3C', alpha=0.8, label='Offshore (Antigua/Bahamas)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(regs, fontsize=8)
ax.set_ylabel('Illustrative score (0-100, hand-set)', fontsize=11)
ax.set_title('Regulatory Environment\n(hand-set, critics\' reading)', fontsize=12, fontweight='bold')
ax.set_ylim(0, 125)
ax.legend(fontsize=10, loc='upper right')
ax.grid(axis='y', alpha=0.3)

# Panel 2: Reported scale of the damage (different measures, not additive, log scale)
# 8     : prosecutors said more than $8B of customer money was taken
# 0.214 : Sequoia invested about $214M across two funds and marked it down to zero (TechCrunch, 9 Nov 2022)
# 32    : FTX's valuation in its January 2022 funding round (a valuation, not a loss)
# 2000  : total crypto market cap fell from about $2.9-3T to about $830B between Nov 2021 and end of 2022
#         (CoinGecko), i.e. more than $2T
ax = axes[1]
cost_items = ['Customer money\ntaken (prosecutors)', 'Sequoia stake\nmarked to zero',
              'FTX valuation\n(Jan 2022 round)', 'Crypto market cap\nlost, Nov 2021-\nend 2022']
cost_values = [8, 0.214, 32, 2000]  # in $B
cost_labels = ['>$8B', '~$0.21B', '$32B', '>$2,000B']
colors_cost = ['#E74C3C', '#E67E22', '#8E44AD', '#2C3E50']
bars = ax.bar(cost_items, cost_values, color=colors_cost, edgecolor='black', linewidth=1)
ax.set_ylabel('Amount ($B, log scale)', fontsize=11)
ax.set_yscale('log')
ax.set_ylim(0.05, 10000)
ax.set_title('Scale of the Damage\n(reported figures, different measures, not additive)',
             fontsize=12, fontweight='bold')
for bar, lab in zip(bars, cost_labels):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.3,
            lab, ha='center', fontweight='bold', fontsize=10)
ax.tick_params(axis='x', labelsize=8)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Crypto's trust paradox (hand-set scores)
ax = axes[2]
paradox_labels = ['Crypto\nPromise', 'Crypto\nReality']
trust_needed = [0, 100]  # promise: no trust needed; reality: maximum trust
transparency = [100, 5]
oversight = [0, 15]      # reality: thin, fragmented outside oversight (not zero)
x2 = np.arange(len(paradox_labels))
ax.bar(x2 - 0.25, trust_needed, 0.24, color='#E74C3C', alpha=0.8, label='Trust Required',
       edgecolor='black', linewidth=1)
ax.bar(x2, transparency, 0.24, color='#3498DB', alpha=0.8, label='Actual Transparency',
       edgecolor='black', linewidth=1)
ax.bar(x2 + 0.25, oversight, 0.24, color='#27AE60', alpha=0.8, label='Outside Oversight',
       edgecolor='black', linewidth=1)
ax.set_xticks(x2)
ax.set_xticklabels(paradox_labels, fontsize=11, fontweight='bold')
ax.set_ylabel('Illustrative score (0-100, hand-set)', fontsize=11)
ax.set_title("Crypto's Trust Paradox (hand-set)", fontsize=12, fontweight='bold')
ax.set_ylim(0, 140)
ax.legend(fontsize=9, loc='upper center', ncol=3)
ax.grid(axis='y', alpha=0.3)
ax.text(0, 108, '"Don\'t trust,\nverify"', ha='center', fontsize=10, fontweight='bold',
        color='#27AE60')
ax.text(1, 108, '"Just trust\nSBF"', ha='center', fontsize=10, fontweight='bold',
        color='#E74C3C')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_regulatory_arbitrage.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_regulatory_arbitrage.png")


# ============================================================
# MODEL 5: Crypto Contagion Chain (2022)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Crypto Contagion Chain -- 2022 Domino Effect (approximate scale)")
print("=" * 65)

dominoes = ['Terra/Luna\nMay 2022', 'Three Arrows\nCapital\nJun 2022',
            'Celsius\nJun 2022', 'Voyager\nJul 2022', 'FTX\nNov 2022']
# Approximate scale per event, in $B. The measure DIFFERS per event, so the values must not be
# added up or read as "value destroyed":
#   Terra/Luna    : roughly $40B or more wiped out (9-12 May 2022)
#   Three Arrows  : reportedly managed up to about $10B at its peak
#   Celsius       : owed users about $4.7B (per its July filing)
#   Voyager       : peak platform assets about $5.9B (about $1.3B of customer crypto at filing)
#   FTX           : $32B January 2022 valuation (a valuation, not a loss)
approx_scale = [40, 10, 4.7, 5.9, 32]
measures = ['value wiped out', 'reported peak AUM', 'owed to users per July filing',
            'peak platform assets', 'Jan 2022 valuation']
days_between = [0, 30, 7, 30, 120]  # hand-set approximate gaps between the events, in days
cumulative_days = np.cumsum(days_between)

fig, axes = plt.subplots(1, 3, figsize=(22, 7.4))
fig.suptitle('2022 Crypto Contagion: Approximate Scale of Each Domino (illustrative, not additive)\n'
             'Terra -> Three Arrows -> Celsius -> Voyager -> FTX | Each failure eroded trust in the next; '
             'the causal links are the usual reading, not all proven',
             fontsize=14, fontweight='bold')

# Panel 1: Approximate scale per event
ax = axes[0]
colors_dom = plt.cm.Reds(np.linspace(0.3, 0.9, len(dominoes)))
bars = ax.bar(range(len(dominoes)), approx_scale, color=colors_dom,
              edgecolor='black', linewidth=1.5)
ax.set_xticks(range(len(dominoes)))
ax.set_xticklabels(dominoes, fontsize=8)
ax.set_ylabel('Approximate scale ($B, different measures)', fontsize=11)
ax.set_title('Approximate Scale Per Event', fontsize=12, fontweight='bold')
for bar, v in zip(bars, approx_scale):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'~${v:g}B', ha='center', fontweight='bold', fontsize=10)
ax.set_ylim(0, max(approx_scale) * 1.15)
ax.grid(axis='y', alpha=0.3)

# Panel 2: The dominoes on a timeline (hand-set gaps; the scales are NOT summed)
ax = axes[1]
ax.vlines(cumulative_days, 0, approx_scale, color='#E74C3C', linewidth=2, alpha=0.6)
ax.scatter(cumulative_days, approx_scale, s=120, color='#E74C3C', zorder=5,
           edgecolors='black', linewidths=1.2)
for d, v, name in zip(cumulative_days, approx_scale, [n.split('\n')[0] for n in dominoes]):
    ax.annotate(f'{name}\n~${v:g}B', (d, v), textcoords="offset points",
                xytext=(8, 6), fontsize=8, fontweight='bold')
ax.set_xlabel('Days from first collapse (hand-set approximate gaps)', fontsize=11)
ax.set_ylabel('Approximate scale ($B, different measures)', fontsize=11)
ax.set_title('Timeline of the Dominoes', fontsize=12, fontweight='bold')
ax.set_xlim(-10, max(cumulative_days) * 1.15)
ax.set_ylim(0, max(approx_scale) * 1.3)
ax.grid(alpha=0.3)

# Panel 3: Causal chain (the usual reading; the evidence is stronger for some links than others)
ax = axes[2]
causes = [
    'Terra/Luna\ncollapses',
    '3AC: huge losses\n(reported Luna\nposition, high\nleverage)',
    'Lenders hit:\nVoyager (3AC claim\nover $650M);\nCelsius hurt by\nmarket fall, runs',
    'Celsius and\nVoyager halt\nwithdrawals,\nfile for bankruptcy',
    "Alameda's losses\nand funding gap\ncan't stay hidden"
]
y_pos = np.linspace(0.9, 0.1, len(causes))
for i, (cause, y) in enumerate(zip(causes, y_pos)):
    color = colors_dom[i]
    ax.scatter(0.12, y, s=800, color=color, zorder=5, edgecolors='black', linewidths=1.5)
    ax.text(0.12, y, str(i + 1), ha='center', va='center', fontsize=10, fontweight='bold',
            color='white' if i >= 2 else 'black', zorder=6)
    ax.text(0.22, y, cause, ha='left', va='center', fontsize=9, fontweight='bold')
    if i < len(causes) - 1:
        ax.annotate('', xy=(0.12, y_pos[i+1] + 0.05), xytext=(0.12, y - 0.05),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('Causal Chain (usual reading, uneven evidence)', fontsize=12, fontweight='bold')
ax.axis('off')

fig.text(0.5, 0.005,
         'Measures differ: Terra = value wiped out; Three Arrows = reported peak AUM; Celsius = owed to users '
         '(July filing); Voyager = peak platform assets; FTX = Jan 2022 valuation.',
         ha='center', fontsize=9, style='italic')
plt.tight_layout(rect=[0, 0.03, 1, 0.92], w_pad=3)
plt.savefig('05_crypto_contagion.png', dpi=300, bbox_inches='tight')
plt.close()

print("  Approximate scale per event (different measures -- do not add them up):")
for name, v, m in zip([n.replace(chr(10), ' ') for n in dominoes], approx_scale, measures):
    print(f"    {name}: ~${v:g}B ({m})")
print(f"  Timeline: about {sum(days_between)} days between the first and last domino "
      f"(hand-set gaps, roughly May-Nov 2022)")
print("=> Saved: 05_crypto_contagion.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
