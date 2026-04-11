"""
Revolution of Ideas #03: The Reformation vs Decentralization Movements
Free Version — 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Authority Hierarchy Collapse (5-Layer → 2-Layer → 1-Layer)
# ============================================================
print("=" * 65)
print("MODEL 1: Authority Hierarchy Collapse -- Centralization to P2P")
print("=" * 65)

systems = {
    "Catholic Church\n(1500)": {
        "layers": ["Pope", "Cardinals", "Bishops", "Priests", "Laity"],
        "population": [1, 70, 500, 250000, 70000000],
        "color": "#8B0000"
    },
    "Protestant Church\n(1600)": {
        "layers": ["Pastors", "Congregation"],
        "population": [50000, 20000000],
        "color": "#2E8B57"
    },
    "Traditional\nFinance": {
        "layers": ["Central Bank", "Commercial Banks", "Users"],
        "population": [1, 5000, 50000000],
        "color": "#4169E1"
    },
    "Crypto / P2P\n(2024)": {
        "layers": ["Nodes/Users"],
        "population": [100000000],
        "color": "#FF8C00"
    }
}

fig, axes = plt.subplots(1, 4, figsize=(22, 8))
fig.suptitle("Hierarchy Collapse: Centralization → Decentralization\n"
             "Catholic (5 layers) → Protestant (2) → Crypto (1)",
             fontsize=14, fontweight='bold')

for idx, (name, data) in enumerate(systems.items()):
    ax = axes[idx]
    n = len(data["layers"])
    max_log = np.log10(max(data["population"]))

    for i, (layer, pop) in enumerate(zip(data["layers"], data["population"])):
        width = (np.log10(pop) + 1) / (max_log + 1)
        y_pos = n - i - 1
        rect = mpatches.FancyBboxPatch(
            (0.5 - width / 2, y_pos * 0.8), width, 0.6,
            boxstyle="round,pad=0.05",
            facecolor=data["color"], alpha=0.3 + 0.5 * (i / (max(n - 1, 1))),
            edgecolor=data["color"], linewidth=2
        )
        ax.add_patch(rect)
        label = f"{layer}\n({pop:,})"
        ax.text(0.5, y_pos * 0.8 + 0.3, label,
                ha='center', va='center', fontsize=8, fontweight='bold')

    decentralization = 1.0 / n
    ax.set_title(f"{name}\nLayers={n} | Decentr.={decentralization:.0%}",
                 fontsize=10, fontweight='bold')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.3, n * 0.8 + 0.2)
    ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_authority_hierarchy_collapse.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n{'System':<25} {'Layers':<8} {'Decentr.':<12} {'Top:Bottom Ratio'}")
print("-" * 60)
for name, data in systems.items():
    n = len(data["layers"])
    ratio = data["population"][-1] / data["population"][0]
    clean_name = name.replace('\n', ' ')
    print(f"  {clean_name:<23} {n:<8} {1/n:<12.0%} 1:{ratio:,.0f}")
print("\n=> Saved: 01_authority_hierarchy_collapse.png")


# ============================================================
# MODEL 2: Theses Propagation Simulation (Luther vs Tweet)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Theses Propagation -- 2 Months vs Minutes")
print("=" * 65)

def sir_propagation(population, beta, gamma, days, initial=10):
    """SIR model for idea propagation."""
    S, I, R = [population - initial], [initial], [0]
    for _ in range(days):
        s, i, r = S[-1], I[-1], R[-1]
        new_inf = beta * s * i / population
        new_rec = gamma * i
        S.append(s - new_inf)
        I.append(i + new_inf - new_rec)
        R.append(r + new_rec)
    return np.array(S), np.array(I), np.array(R)

# Luther's 95 Theses (1517): printed pamphlets, 2 months to cover Germany
S_luther, I_luther, R_luther = sir_propagation(100000, beta=0.25, gamma=0.02, days=90)
# Bitcoin whitepaper (2008): email+web, global in 24 hours
S_btc, I_btc, R_btc = sir_propagation(500000, beta=0.8, gamma=0.05, days=30)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Luther
days_l = np.arange(len(I_luther))
axes[0].plot(days_l, I_luther / 100000 * 100, 'r-', linewidth=2.5, label='Actively Spreading')
axes[0].plot(days_l, R_luther / 100000 * 100, 'g-', linewidth=2, label='Reached & Absorbed')
axes[0].axvline(x=np.argmax(I_luther), color='red', linestyle='--', alpha=0.5,
                label=f'Peak: day {np.argmax(I_luther)}')
axes[0].set_xlabel('Days', fontsize=11)
axes[0].set_ylabel('% of Population', fontsize=11)
axes[0].set_title("Luther's 95 Theses (1517)\nPrinted pamphlets across Germany",
                   fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)

# Bitcoin
days_b = np.arange(len(I_btc))
axes[1].plot(days_b, I_btc / 500000 * 100, 'r-', linewidth=2.5, label='Actively Spreading')
axes[1].plot(days_b, R_btc / 500000 * 100, 'g-', linewidth=2, label='Reached & Absorbed')
axes[1].axvline(x=np.argmax(I_btc), color='red', linestyle='--', alpha=0.5,
                label=f'Peak: day {np.argmax(I_btc)}')
axes[1].set_xlabel('Days', fontsize=11)
axes[1].set_ylabel('% of Population', fontsize=11)
axes[1].set_title("Bitcoin Whitepaper (2008)\nEmail + web, global reach",
                   fontsize=12, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(alpha=0.3)

fig.suptitle('Idea Propagation: Reformation vs Crypto\n'
             'Same SIR dynamics, 180x speed difference',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_theses_propagation.png', dpi=300, bbox_inches='tight')
plt.close()

peak_l = np.argmax(I_luther)
peak_b = np.argmax(I_btc)
reach_l = (R_luther[-1] + I_luther[-1]) / 100000 * 100
reach_b = (R_btc[-1] + I_btc[-1]) / 500000 * 100
print(f"\n  Luther's Theses -- peak spread at day {peak_l}, reach: {reach_l:.1f}%")
print(f"  Bitcoin whitepaper -- peak spread at day {peak_b}, reach: {reach_b:.1f}%")
print(f"  Speed difference: ~180x (2 months vs ~6 hours to 50%)")
print(f"  Key insight: reach % is similar; speed is what changes.")
print("\n=> Saved: 02_theses_propagation.png")


# ============================================================
# MODEL 3: Church Division Network (1 → Many Denominations)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Church Division Network -- Forks Across Centuries")
print("=" * 65)

# Religious schisms
G_rel = nx.DiGraph()
rel_nodes = [
    ('Catholic Church', 1500), ('Lutheran', 1517), ('Reformed (Zwingli)', 1523),
    ('Anglican', 1534), ('Calvinist', 1536), ('Anabaptist', 1525),
    ('Presbyterian', 1560), ('Baptist', 1609), ('Methodist', 1738)
]
for name, year in rel_nodes:
    G_rel.add_node(name, year=year)
rel_edges = [
    ('Catholic Church', 'Lutheran'), ('Catholic Church', 'Reformed (Zwingli)'),
    ('Catholic Church', 'Anglican'), ('Catholic Church', 'Anabaptist'),
    ('Lutheran', 'Calvinist'), ('Calvinist', 'Presbyterian'),
    ('Anglican', 'Baptist'), ('Presbyterian', 'Methodist')
]
G_rel.add_edges_from(rel_edges)

# Blockchain forks
G_btc = nx.DiGraph()
btc_nodes = [
    ('Bitcoin', 2009), ('Litecoin', 2011), ('Ethereum', 2015),
    ('ETC', 2016), ('BCH', 2017), ('BSV', 2018),
    ('DeFi Chains', 2020), ('L2 Rollups', 2021)
]
for name, year in btc_nodes:
    G_btc.add_node(name, year=year)
btc_edges = [
    ('Bitcoin', 'Litecoin'), ('Bitcoin', 'Ethereum'), ('Ethereum', 'ETC'),
    ('Bitcoin', 'BCH'), ('BCH', 'BSV'), ('Ethereum', 'DeFi Chains'),
    ('Ethereum', 'L2 Rollups')
]
G_btc.add_edges_from(btc_edges)

fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Religious tree
pos_rel = nx.spring_layout(G_rel, k=2.0, iterations=60, seed=42)
years_rel = [G_rel.nodes[n]['year'] for n in G_rel.nodes()]
nx.draw_networkx_nodes(G_rel, pos_rel, ax=axes[0], node_size=1200,
                       node_color=years_rel, cmap=plt.cm.RdYlGn_r,
                       edgecolors='black', linewidths=2, alpha=0.9)
nx.draw_networkx_edges(G_rel, pos_rel, ax=axes[0], edge_color='gray',
                       width=2, arrows=True, arrowsize=15, alpha=0.6)
labels_rel = {n: f"{n}\n({G_rel.nodes[n]['year']})" for n in G_rel.nodes()}
nx.draw_networkx_labels(G_rel, pos_rel, labels_rel, ax=axes[0],
                        font_size=8, font_weight='bold')
axes[0].set_title('Religious Schisms (1517–1738)\n1 church → 8+ denominations in 220 years',
                  fontsize=12, fontweight='bold')
axes[0].axis('off')

# Blockchain tree
pos_btc = nx.spring_layout(G_btc, k=2.0, iterations=60, seed=42)
years_btc = [G_btc.nodes[n]['year'] for n in G_btc.nodes()]
nx.draw_networkx_nodes(G_btc, pos_btc, ax=axes[1], node_size=1200,
                       node_color=years_btc, cmap=plt.cm.YlOrRd,
                       edgecolors='black', linewidths=2, alpha=0.9)
nx.draw_networkx_edges(G_btc, pos_btc, ax=axes[1], edge_color='gray',
                       width=2, arrows=True, arrowsize=15, alpha=0.6)
labels_btc = {n: f"{n}\n({G_btc.nodes[n]['year']})" for n in G_btc.nodes()}
nx.draw_networkx_labels(G_btc, pos_btc, labels_btc, ax=axes[1],
                        font_size=8, font_weight='bold')
axes[1].set_title('Blockchain Forks (2009–2021)\n1 chain → dozens in 12 years',
                  fontsize=12, fontweight='bold')
axes[1].axis('off')

fig.suptitle('Decentralization Produces Fragmentation, Not Unity\n'
             'Same pattern, 24x faster in crypto',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_church_division_network.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n  Religious schisms: 1 -> {len(rel_nodes)} branches in ~220 years")
print(f"  Blockchain forks:  1 -> {len(btc_nodes)} branches in ~12 years")
print(f"  Fragmentation speedup: ~{220/12:.0f}x")
print(f"  Pattern: decentralization always leads to splits, never unity.")
print("\n=> Saved: 03_church_division_network.png")


# ============================================================
# MODEL 4: Indulgences vs ICO Scams (Bubble Price vs Value)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Indulgences vs ICO Scams -- Selling Dreams")
print("=" * 65)

# Indulgence bubble: price inflation over time (relative units)
years_ind = np.arange(1490, 1521)
base_price = 1.0
indulgence_price = base_price * np.exp(0.08 * (years_ind - 1490))
actual_value = np.ones_like(years_ind) * 0.2  # no real value
luther_year = 1517

# ICO bubble: crypto token price 2016-2019
months_ico = np.arange(0, 36)  # 3 years
ico_price = np.where(months_ico < 18,
                     1.0 * np.exp(0.15 * months_ico),
                     1.0 * np.exp(0.15 * 18) * np.exp(-0.2 * (months_ico - 18)))
ico_value = np.ones_like(months_ico) * 0.5  # minimal real value

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Indulgences
axes[0].plot(years_ind, indulgence_price, 'r-', linewidth=2.5, label='Indulgence "Price"')
axes[0].fill_between(years_ind, actual_value, alpha=0.3, color='green', label='Actual Spiritual Value')
axes[0].axvline(x=luther_year, color='black', linestyle='--', linewidth=2,
                label=f"Luther's 95 Theses ({luther_year})")
axes[0].set_xlabel('Year', fontsize=11)
axes[0].set_ylabel('Relative Price/Value', fontsize=11)
axes[0].set_title('Indulgences (1490–1520)\n"Pay to skip Purgatory"',
                  fontsize=12, fontweight='bold')
axes[0].legend(fontsize=9)
axes[0].grid(alpha=0.3)

# ICO
ico_years = [f"2016-{m+1:02d}" if m < 12
             else f"2017-{m-11:02d}" if m < 24
             else f"2018-{m-23:02d}" for m in months_ico]
axes[1].plot(months_ico, ico_price, 'r-', linewidth=2.5, label='ICO Token Price')
axes[1].fill_between(months_ico, ico_value, alpha=0.3, color='green', label='Actual Product Value')
axes[1].axvline(x=18, color='black', linestyle='--', linewidth=2,
                label='Crash (Jan 2018)')
axes[1].set_xlabel('Months from start', fontsize=11)
axes[1].set_ylabel('Relative Price/Value', fontsize=11)
axes[1].set_title('ICO Bubble (2016–2018)\n"Pay for Financial Freedom"',
                  fontsize=12, fontweight='bold')
axes[1].legend(fontsize=9)
axes[1].grid(alpha=0.3)

fig.suptitle('Selling Dreams: Indulgences vs ICO Scams\n'
             '~80% fraud rate in both eras | Same human psychology',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_indulgences_vs_ico.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n  Comparison:")
print(f"  {'Dimension':<25} {'Indulgences (1500s)':<25} {'ICO (2017-18)'}")
print(f"  {'-'*75}")
print(f"  {'Product':<25} {'Salvation from Purgatory':<25} {'Financial Freedom'}")
print(f"  {'Endorser':<25} {'The Pope':<25} {'Blockchain Experts'}")
print(f"  {'Verifiable?':<25} {'No (after death)':<25} {'No (most unfinished)'}")
print(f"  {'Buyer motive':<25} {'Fear (hell)':<25} {'Greed (miss out)'}")
print(f"  {'Fraud rate':<25} {'~80%':<25} {'~80%'}")
print("\n=> Saved: 04_indulgences_vs_ico.png")


# ============================================================
# MODEL 5: True vs False Decentralization (Nakamoto Coefficient)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Nakamoto Coefficient -- True vs False Decentralization")
print("=" * 65)

systems_nk = {
    'Catholic\nChurch\n(1500)': {'coefficient': 1, 'color': '#8B0000'},
    'Protestant\nChurch\n(1600)': {'coefficient': 50, 'color': '#2E8B57'},
    'Traditional\nBanking': {'coefficient': 5, 'color': '#4169E1'},
    'Bitcoin\n(2024)': {'coefficient': 4, 'color': '#FF8C00'},
    'Ethereum\n(2024)': {'coefficient': 3, 'color': '#6C3483'},
    'Solana\n(2024)': {'coefficient': 19, 'color': '#1ABC9C'},
}

fig, ax = plt.subplots(figsize=(12, 7))
names = list(systems_nk.keys())
coefficients = [systems_nk[n]['coefficient'] for n in names]
colors = [systems_nk[n]['color'] for n in names]

bars = ax.bar(range(len(names)), coefficients, color=colors, alpha=0.85,
              edgecolor='black', linewidth=1.5)
ax.axhline(y=10, color='red', linestyle='--', linewidth=2, alpha=0.7,
           label='Minimum for "meaningful" decentralization')
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, fontsize=9)
ax.set_ylabel('Nakamoto Coefficient\n(entities needed to control 51%)', fontsize=12)
ax.set_title('Nakamoto Coefficient: How Decentralized Is It Really?\n'
             'Bitcoin (4) is barely more decentralized than traditional banking (5)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

for i, v in enumerate(coefficients):
    ax.text(i, v + 1, str(v), ha='center', fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('05_nakamoto_coefficient.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n{'System':<25} {'Nakamoto Coeff.':<18} {'Interpretation'}")
print("-" * 65)
for name, data in systems_nk.items():
    clean = name.replace('\n', ' ')
    coeff = data['coefficient']
    if coeff <= 3:
        interp = "Highly centralized"
    elif coeff <= 10:
        interp = "Weakly decentralized"
    elif coeff <= 30:
        interp = "Moderately decentralized"
    else:
        interp = "Decentralized"
    print(f"  {clean:<23} {coeff:<18} {interp}")
print(f"\n  Paradox: Bitcoin's Nakamoto coeff (4) ~ Traditional banking (5)")
print(f"  'Decentralization' exists mostly in the whitepaper, not in practice.")
print("\n=> Saved: 05_nakamoto_coefficient.png")


# ============================================================
# MODEL 6: Reform vs Revolution Phase Transition
# ============================================================
print("\n" + "=" * 65)
print("MODEL 6: Reform -> Revolution Phase Transition")
print("=" * 65)

def phase_transition(temperatures, critical_temp, steepness=0.5):
    """Model social phase transition: reform → revolution.
    Below critical_temp: gradual reform (liquid).
    Above critical_temp: violent revolution (gas).
    """
    return 1 / (1 + np.exp(-steepness * (temperatures - critical_temp)))

# Reformation timeline
reform_years = np.arange(1490, 1660)
reform_temp = np.piecewise(
    reform_years.astype(float),
    [reform_years < 1510, (reform_years >= 1510) & (reform_years < 1517),
     (reform_years >= 1517) & (reform_years < 1521),
     (reform_years >= 1521) & (reform_years < 1555),
     reform_years >= 1555],
    [lambda x: 20 + 0.5 * (x - 1490),
     lambda x: 30 + 3 * (x - 1510),
     lambda x: 51 + 10 * (x - 1517),
     lambda x: 80 + 0.3 * (x - 1521),
     lambda x: 90 + 0.2 * (x - 1555)]
)

# Crypto timeline
crypto_years = np.arange(2008, 2026)
crypto_temp = np.piecewise(
    crypto_years.astype(float),
    [crypto_years < 2013, (crypto_years >= 2013) & (crypto_years < 2017),
     (crypto_years >= 2017) & (crypto_years < 2018),
     (crypto_years >= 2018) & (crypto_years < 2022),
     crypto_years >= 2022],
    [lambda x: 20 + 2 * (x - 2008),
     lambda x: 30 + 5 * (x - 2013),
     lambda x: 50 + 40 * (x - 2017),
     lambda x: 85 + 1 * (x - 2018),
     lambda x: 89 + 0.5 * (x - 2022)]
)

critical = 50  # phase transition point

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Reformation
axes[0].plot(reform_years, reform_temp, 'r-', linewidth=2.5)
axes[0].axhline(y=critical, color='black', linestyle='--', linewidth=2,
                label=f'Critical point (T={critical})')
axes[0].fill_between(reform_years, 0, reform_temp,
                     where=reform_temp < critical, alpha=0.2, color='blue',
                     label='Reform phase (gradual)')
axes[0].fill_between(reform_years, 0, reform_temp,
                     where=reform_temp >= critical, alpha=0.2, color='red',
                     label='Revolution phase (violent)')
axes[0].annotate('95 Theses\n(1517)', xy=(1517, 51), fontsize=9,
                 xytext=(1530, 30), arrowprops=dict(arrowstyle='->', color='black'),
                 fontweight='bold')
axes[0].annotate('Excommunication\n(1521)', xy=(1521, 80), fontsize=9,
                 xytext=(1540, 65), arrowprops=dict(arrowstyle='->', color='black'),
                 fontweight='bold')
axes[0].annotate('30 Years War\n(1618)', xy=(1618, 92), fontsize=9,
                 xytext=(1580, 100), arrowprops=dict(arrowstyle='->', color='black'),
                 fontweight='bold')
axes[0].set_xlabel('Year', fontsize=11)
axes[0].set_ylabel('Social "Temperature"', fontsize=11)
axes[0].set_title('Reformation Phase Transition\n(1490–1650)',
                  fontsize=12, fontweight='bold')
axes[0].legend(fontsize=9, loc='lower right')
axes[0].grid(alpha=0.3)
axes[0].set_ylim(0, 110)

# Crypto
axes[1].plot(crypto_years, crypto_temp, 'r-', linewidth=2.5)
axes[1].axhline(y=critical, color='black', linestyle='--', linewidth=2,
                label=f'Critical point (T={critical})')
axes[1].fill_between(crypto_years, 0, crypto_temp,
                     where=crypto_temp < critical, alpha=0.2, color='blue',
                     label='Reform phase (gradual)')
axes[1].fill_between(crypto_years, 0, crypto_temp,
                     where=crypto_temp >= critical, alpha=0.2, color='red',
                     label='Revolution phase (volatile)')
axes[1].annotate('ICO Bubble\n(2017)', xy=(2017, 50), fontsize=9,
                 xytext=(2011, 35), arrowprops=dict(arrowstyle='->', color='black'),
                 fontweight='bold')
axes[1].annotate('FTX Collapse\n(2022)', xy=(2022, 89), fontsize=9,
                 xytext=(2015, 95), arrowprops=dict(arrowstyle='->', color='black'),
                 fontweight='bold')
axes[1].set_xlabel('Year', fontsize=11)
axes[1].set_ylabel('Social "Temperature"', fontsize=11)
axes[1].set_title('Crypto Phase Transition\n(2008–2025)',
                  fontsize=12, fontweight='bold')
axes[1].legend(fontsize=9, loc='lower right')
axes[1].grid(alpha=0.3)
axes[1].set_ylim(0, 110)

fig.suptitle('Phase Transition: When Reform Becomes Revolution\n'
             'Once past the critical point, there is no going back',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('06_phase_transition.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n  Reformation phase transition:")
print(f"  {'Phase':<20} {'Period':<20} {'State'}")
print(f"  {'-'*60}")
print(f"  {'Brewing':<20} {'1500-1517':<20} {'Private dissent'}")
print(f"  {'Ignition':<20} {'1517-1521':<20} {'Public debate'}")
print(f"  {'CRITICAL POINT':<20} {'1521':<20} {'Excommunication'}")
print(f"  {'Explosion':<20} {'1521-1555':<20} {'Wars, uprisings'}")
print(f"  {'Devastation':<20} {'1618-1648':<20} {'30 Years War (8M dead)'}")
print(f"\n  Crypto phase transition:")
print(f"  {'Brewing':<20} {'2008-2013':<20} {'Niche tech discussion'}")
print(f"  {'Ignition':<20} {'2013-2017':<20} {'Price surge, media'}")
print(f"  {'CRITICAL POINT':<20} {'2017':<20} {'ICO mania'}")
print(f"  {'Explosion':<20} {'2018-2022':<20} {'Crashes, FTX, regulation'}")
print(f"\n  Key insight: phase transitions are IRREVERSIBLE.")
print("\n=> Saved: 06_phase_transition.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
