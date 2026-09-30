"""
Revolution of Ideas #03: The Reformation vs Decentralization Movements
Free Version — 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy

DATA NOTE
Nothing here is loaded from a dataset or computed from raw data. Every number is
typed in by hand:
  - hierarchy headcounts, SIR rates, bubble curves and phase-transition
    "temperatures" are the author's illustrative assumptions, not measurements;
  - the Church and banking Nakamoto coefficients are the author's estimates;
  - the crypto Nakamoto coefficients are hand-entered approximations from the
    dated sources cited in the Model 5 comments;
  - the ICO scam share is Satis Group's 2018 figure (by project count).
The article's References and "About the data" section list the sources.
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

# Headcounts are the author's order-of-magnitude assumptions, not historical
# statistics (the College of Cardinals was a few dozen, not 70: 70 is an
# illustrative value). "Decentralization" below is simply 1 / number of layers,
# a crude illustrative index rather than a measured quantity.
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
print("\n  Note: headcounts are the author's order-of-magnitude assumptions;")
print("  Decentr. = 1 / layers is an illustrative index, not a measurement.")
print("\n=> Saved: 01_authority_hierarchy_collapse.png")


# ============================================================
# MODEL 2: Theses Propagation Simulation (Luther vs Bitcoin white paper)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Theses Propagation -- Two Hand-Set Parameter Sets")
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

def day_reaching(I, R, population, share=0.5):
    """First model day on which the cumulative reach (I + R) / population passes `share`."""
    return int(np.argmax((I + R) / population >= share))

# All populations, beta (transmission rate) and gamma (recovery rate) below are
# hand-set illustrative assumptions, NOT estimates from historical or measured data.
# One time step = one model day. Real-world time scales are not modelled
# (Myconius, in a later recollection, says about two weeks across Germany;
# the Bitcoin white paper was posted to a specialist mailing list on 31 Oct 2008).
# Luther's 95 Theses (1517): slower hand-set rates, run for 90 model days
S_luther, I_luther, R_luther = sir_propagation(100000, beta=0.25, gamma=0.02, days=90)
# Bitcoin white paper (2008): faster hand-set rates, run for 30 model days
S_btc, I_btc, R_btc = sir_propagation(500000, beta=0.8, gamma=0.05, days=30)
half_l = day_reaching(I_luther, R_luther, 100000)
half_b = day_reaching(I_btc, R_btc, 500000)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Luther
days_l = np.arange(len(I_luther))
axes[0].plot(days_l, I_luther / 100000 * 100, 'r-', linewidth=2.5, label='Actively Spreading')
axes[0].plot(days_l, R_luther / 100000 * 100, 'g-', linewidth=2, label='Recovered (R)')
axes[0].plot(days_l, (I_luther + R_luther) / 100000 * 100, 'b--', linewidth=2,
             label=f'Cumulative reach (I + R): 50% at day {half_l}')
axes[0].axvline(x=np.argmax(I_luther), color='red', linestyle='--', alpha=0.5,
                label=f'Peak: day {np.argmax(I_luther)}')
axes[0].set_xlabel('Model days', fontsize=11)
axes[0].set_ylabel('% of Population', fontsize=11)
axes[0].set_title("Luther's 95 Theses (1517)\nPrinted pamphlets (hand-set rates)",
                   fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)

# Bitcoin
days_b = np.arange(len(I_btc))
axes[1].plot(days_b, I_btc / 500000 * 100, 'r-', linewidth=2.5, label='Actively Spreading')
axes[1].plot(days_b, R_btc / 500000 * 100, 'g-', linewidth=2, label='Recovered (R)')
axes[1].plot(days_b, (I_btc + R_btc) / 500000 * 100, 'b--', linewidth=2,
             label=f'Cumulative reach (I + R): 50% at day {half_b}')
axes[1].axvline(x=np.argmax(I_btc), color='red', linestyle='--', alpha=0.5,
                label=f'Peak: day {np.argmax(I_btc)}')
axes[1].set_xlabel('Model days', fontsize=11)
axes[1].set_ylabel('% of Population', fontsize=11)
axes[1].set_title("Bitcoin Whitepaper (2008)\nMailing list + web (hand-set rates)",
                   fontsize=12, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(alpha=0.3)

fig.suptitle('Idea Propagation: Reformation vs Crypto\n'
             'Same SIR dynamics, different hand-set transmission rates',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_theses_propagation.png', dpi=300, bbox_inches='tight')
plt.close()

peak_l = np.argmax(I_luther)
peak_b = np.argmax(I_btc)
reach_l = (R_luther[-1] + I_luther[-1]) / 100000 * 100
reach_b = (R_btc[-1] + I_btc[-1]) / 500000 * 100
print(f"\n  Luther's Theses -- 50% reached at model day {half_l}, peak spread at day {peak_l}, "
      f"reach at end of run (day {len(I_luther) - 1}): {reach_l:.1f}%")
print(f"  Bitcoin whitepaper -- 50% reached at model day {half_b}, peak spread at day {peak_b}, "
      f"reach at end of run (day {len(I_btc) - 1}): {reach_b:.1f}%")
print(f"  Speed gap in this model: {half_l / half_b:.1f}x to 50% reach "
      f"(day {half_l} vs day {half_b}), {peak_l / peak_b:.1f}x to the peak")
print("  It comes entirely from the hand-picked beta/gamma, so it says nothing about")
print("  how fast the real internet is.")
print("  Both runs reach (almost) everyone by construction: with beta well above gamma an")
print("  SIR model saturates (final size is close to, not exactly, 100%). Equal reach is")
print("  an assumption of the setup, not a finding; only the speed differs.")
print("\n=> Saved: 02_theses_propagation.png")


# ============================================================
# MODEL 3: Church Division Network (1 → Many Denominations)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Church Division Network -- Branches Across Centuries")
print("=" * 65)

# Both trees are simplified sketches, not exact lineages. The dates are the
# article's "founding" dates, listed in chronological order.
# Religious branches
G_rel = nx.DiGraph()
rel_nodes = [
    ('Catholic Church', 1500), ('Lutheran', 1517), ('Reformed (Zwingli)', 1523),
    ('Anabaptist', 1525), ('Anglican', 1534), ('Calvinist', 1536),
    ('Presbyterian', 1560), ('Baptist', 1609), ('Methodist', 1738)
]
for name, year in rel_nodes:
    G_rel.add_node(name, year=year)
# Calvinist = the Reformed tradition (the article treats them as one lineage);
# 1560 = Scottish Reformation; 1609 = Smyth's Baptist congregation in Amsterdam;
# 1738 = Wesley's Aldersgate revival, i.e. a forerunner of Methodism
# (an independent church only from 1784). Wesley was an Anglican priest.
rel_edges = [
    ('Catholic Church', 'Lutheran'), ('Catholic Church', 'Reformed (Zwingli)'),
    ('Catholic Church', 'Anglican'), ('Catholic Church', 'Anabaptist'),
    ('Reformed (Zwingli)', 'Calvinist'), ('Calvinist', 'Presbyterian'),
    ('Anglican', 'Baptist'), ('Anglican', 'Methodist')
]
G_rel.add_edges_from(rel_edges)

# Blockchain lineages: forks, derivative coins and independent chains are NOT the same thing.
G_btc = nx.DiGraph()
btc_nodes = [
    ('Bitcoin', 2009), ('Litecoin', 2011), ('Ethereum', 2015),
    ('ETC', 2016), ('BCH', 2017), ('BSV', 2018),
    ('DeFi Chains', 2020), ('L2 Rollups', 2021)
]
for name, year in btc_nodes:
    G_btc.add_node(name, year=year)
# Edge kinds (third element):
#   'fork'      = chain split: ETC is the continuation of the pre-DAO-fork Ethereum chain,
#                 BCH split from Bitcoin, BSV split from Bitcoin Cash.
#   'derivative'= Litecoin is a coin derived from Bitcoin's code (a new chain, not a split).
#   'ecosystem' = built on / around Ethereum, NOT a fork (DeFi chains are mostly
#                 independent chains; L2 rollups settle on Ethereum).
# Ethereum itself is an independent chain, so it has no edge from Bitcoin.
btc_edges = [
    ('Bitcoin', 'Litecoin', 'derivative'), ('Ethereum', 'ETC', 'fork'),
    ('Bitcoin', 'BCH', 'fork'), ('BCH', 'BSV', 'fork'),
    ('Ethereum', 'DeFi Chains', 'ecosystem'), ('Ethereum', 'L2 Rollups', 'ecosystem')
]
for u, v, kind in btc_edges:
    G_btc.add_edge(u, v, kind=kind)

fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Religious tree
pos_rel = nx.spring_layout(G_rel, k=2.0, iterations=60, seed=42)
years_rel = [G_rel.nodes[n]['year'] for n in G_rel.nodes()]
nx.draw_networkx_nodes(G_rel, pos_rel, ax=axes[0], node_size=1200,
                       node_color=years_rel, cmap=plt.cm.RdYlGn_r,
                       edgecolors='black', linewidths=2, alpha=0.9)
nx.draw_networkx_edges(G_rel, pos_rel, ax=axes[0], edge_color='gray', node_size=1200,
                       width=2, arrows=True, arrowsize=15, alpha=0.6)
labels_rel = {n: f"{n}\n({G_rel.nodes[n]['year']})" for n in G_rel.nodes()}
nx.draw_networkx_labels(G_rel, pos_rel, labels_rel, ax=axes[0],
                        font_size=8, font_weight='bold')
axes[0].set_title('Protestant Branches (1517–1738)\n8 entries in about 221 years (simplified sketch)',
                  fontsize=12, fontweight='bold')
axes[0].axis('off')

# Blockchain tree
pos_btc = nx.spring_layout(G_btc, k=2.0, iterations=60, seed=42)
years_btc = [G_btc.nodes[n]['year'] for n in G_btc.nodes()]
nx.draw_networkx_nodes(G_btc, pos_btc, ax=axes[1], node_size=1200,
                       node_color=years_btc, cmap=plt.cm.YlOrRd,
                       edgecolors='black', linewidths=2, alpha=0.9)
fork_edges = [(u, v) for u, v, k in G_btc.edges(data='kind') if k == 'fork']
other_edges = [(u, v) for u, v, k in G_btc.edges(data='kind') if k != 'fork']
nx.draw_networkx_edges(G_btc, pos_btc, ax=axes[1], edgelist=fork_edges, edge_color='gray',
                       node_size=1200, width=2, arrows=True, arrowsize=15, alpha=0.6)
nx.draw_networkx_edges(G_btc, pos_btc, ax=axes[1], edgelist=other_edges, edge_color='gray',
                       node_size=1200, width=2, style='dashed', arrows=True, arrowsize=15, alpha=0.6)
labels_btc = {n: f"{n}\n({G_btc.nodes[n]['year']})" for n in G_btc.nodes()}
nx.draw_networkx_labels(G_btc, pos_btc, labels_btc, ax=axes[1],
                        font_size=8, font_weight='bold')
axes[1].set_title('Blockchain Lineages (2009–2021)\nforks, derivative coins and independent chains',
                  fontsize=12, fontweight='bold')
axes[1].axis('off')

fig.suptitle('In These Two Cases, Decentralization Produced Fragmentation, Not Unity\n'
             'Roughly 18x faster branching on the listed counts',
             fontsize=14, fontweight='bold')
fig.text(0.5, 0.02,
         "Simplified sketches, not exact lineages. Left: Calvinist = Reformed tradition; "
         "Methodist = 1738 revival (independent church from 1784).\n"
         "Right: solid = chain fork (ETC continues the pre-DAO-fork Ethereum chain); "
         "dashed = derivative coin (Litecoin) or ecosystem link (not a fork); "
         "Ethereum is an independent chain.",
         ha='center', va='bottom', fontsize=8, style='italic')
plt.tight_layout(rect=[0, 0.05, 1, 0.92], w_pad=3)
plt.savefig('03_church_division_network.png', dpi=300, bbox_inches='tight')
plt.close()

# Counting rule (same as the article's two timelines): entries dated 1517-1738 on the
# religious side (the Catholic Church itself is not counted) and entries dated 2009-2018
# on the blockchain side (Bitcoin itself is counted). DeFi chains / L2 rollups are not counted.
n_rel = sum(1 for _, y in rel_nodes if 1517 <= y <= 1738)
span_rel = 1738 - 1517
n_btc = sum(1 for _, y in btc_nodes if 2009 <= y <= 2018)
span_btc = 2018 - 2009
rate_rel = n_rel / span_rel
rate_btc = n_btc / span_btc
print(f"\n  Protestant branches listed: {n_rel} in {span_rel} years (1517-1738) "
      f"-> {rate_rel:.3f} per year")
print(f"  Blockchain chains listed:   {n_btc} in {span_btc} years (2009-2018) "
      f"-> {rate_btc:.2f} per year")
print(f"  Branching-rate ratio: ~{rate_btc / rate_rel:.0f}x on these counts "
      f"(small counts, simplified trees -- a rough comparison only)")
print("  The blockchain side mixes forks (ETC, BCH, BSV), a derivative coin (Litecoin)")
print("  and an independent chain (Ethereum); not all of these are splits.")
print("  Pattern (my reading of these two cases): decentralization produced fragmentation, not unity.")
print("\n=> Saved: 03_church_division_network.png")


# ============================================================
# MODEL 4: Indulgences vs ICO Scams (Bubble Price vs Value)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Indulgences vs ICO Scams -- Selling Dreams")
print("=" * 65)

# Both curves below are ILLUSTRATIVE shapes in relative units, not price data.
# Indulgence bubble: price inflation over time (relative units)
years_ind = np.arange(1490, 1521)
base_price = 1.0
indulgence_price = base_price * np.exp(0.08 * (years_ind - 1490))
actual_value = np.ones_like(years_ind) * 0.2  # no real value
luther_year = 1517

# ICO bubble: stylised token price path (month 0 ~ mid-2016, so month 18 ~ Jan 2018)
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
axes[0].set_ylabel('Relative Price/Value (illustrative)', fontsize=11)
axes[0].set_title('Indulgences (1490–1520)\nIllustrative price curve',
                  fontsize=12, fontweight='bold')
axes[0].legend(fontsize=9)
axes[0].grid(alpha=0.3)

# ICO
axes[1].plot(months_ico, ico_price, 'r-', linewidth=2.5, label='ICO Token Price')
axes[1].fill_between(months_ico, ico_value, alpha=0.3, color='green', label='Actual Product Value')
axes[1].axvline(x=18, color='black', linestyle='--', linewidth=2,
                label='Crash (Jan 2018)')
axes[1].set_xlabel('Months from start (month 0 ~ mid-2016)', fontsize=11)
axes[1].set_ylabel('Relative Price/Value (illustrative)', fontsize=11)
axes[1].set_title('ICO Bubble (2016–2018)\nIllustrative price curve',
                  fontsize=12, fontweight='bold')
axes[1].legend(fontsize=9)
axes[1].grid(alpha=0.3)

fig.suptitle('Selling Dreams: Indulgences vs ICO Scams\n'
             'ICOs: ~78% scams by project count (Satis Group, 2018) | '
             'no comparable indulgence figure',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_indulgences_vs_ico.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n  Comparison:")
print(f"  {'Dimension':<25} {'Indulgences (1500s)':<25} {'ICO (2017-18)'}")
print(f"  {'-'*75}")
print(f"  {'Product':<25} {'Salvation from Purgatory':<25} {'Financial Freedom'}")
print(f"  {'Endorser':<25} {'The Pope':<25} {'Blockchain Experts'}")
print(f"  {'Verifiable?':<25} {'No (after death)':<25} {'No (most never shipped)'}")
print(f"  {'Buyer motive':<25} {'Fear (hell)':<25} {'Greed (miss out)'}")
print(f"  {'Bad outcomes':<25} {'No reliable estimate':<25} {'~78% scams (by project)'}")
# ICO figure: Satis Group report (2018), reported by CoinDesk, 12 July 2018:
# https://www.coindesk.com/markets/2018/07/12/report-more-than-three-quarters-of-icos-were-scams
# ~78% of ICOs were scams and ~85% were scams, failures or dead projects (by project
# count); by funds raised, scams took ~11%.
# Indulgences: there is no comparable number. The documented use of the proceeds of the
# indulgence authorised in 1515 was about half to Rome and half to repay Albrecht's debt.
print("\n  The two 'bad outcome' measures are different metrics and not comparable: the ICO")
print("  figure is Satis Group's 2018 count of projects (~85% scams, failed or dead; by funds")
print("  raised, scams took ~11%). Indulgences have no comparable estimate; the documented")
print("  use of the 1515 proceeds was about half to Rome, half to repay Albrecht's debt.")
print("  The shared shape is an unverifiable promise sold on fear or greed -- my reading,")
print("  not something these numbers prove.")
print("\n=> Saved: 04_indulgences_vs_ico.png")


# ============================================================
# MODEL 5: True vs False Decentralization (Nakamoto Coefficient)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Nakamoto Coefficient -- True vs False Decentralization")
print("=" * 65)

# The Nakamoto coefficient = minimum number of independent entities needed to control 51%.
# IMPORTANT: every value below is HAND-ENTERED, not computed by this script from raw data.
#   - Catholic Church (1), Protestant Church (~50), Traditional Banking (~5):
#     the author's estimates, with no source or method behind them.
#   - Bitcoin = 2 (counted by mining pool, not by independent entity): over one 24-hour
#     window around 4 July 2024 Foundry USA and AntPool each mined ~30% of blocks (just
#     under 60% together) and ViaBTC ~11%, so two pools already pass 51% (the article
#     says "2-3"). A short snapshot; a pool is not an independent entity (its miners can
#     leave at any time). Source: CryptoSlate, 4 July 2024,
#     https://cryptoslate.com/insights/dual-dominance-foundry-usa-and-antpool-command-60-of-bitcoin-mining-pool-market/
#   - Ethereum = 3, but it is 3-5 depending on the counting. April 2024 Dune staking data
#     (via The Crypto Times, 4 April 2024): Lido ~29.6%, a category Dune could not identify
#     ~16.9%, Coinbase ~14.0%. Count the unidentified category as one entity and three
#     entities pass 51%; leave it out and it takes four or five. (Lido is itself run by many
#     independent node operators.)
#     https://www.cryptotimes.io/2024/04/04/lidos-ethereum-staking-market-share-falls-below-30-mark/
#   - Solana = 19 uses a one-third-of-stake threshold (Helius, 2024), NOT 51%, so it is not
#     directly comparable with the other rows.
#     https://www.helius.dev/blog/solana-decentralization-facts-and-figures
systems_nk = {
    'Catholic\nChurch\n(1500)': {'coefficient': 1, 'label': '1\n(author est.)',
                                 'note': "author's estimate", 'color': '#8B0000'},
    'Protestant\nChurch\n(1600)': {'coefficient': 50, 'label': '~50\n(author est.)',
                                   'note': "author's estimate", 'color': '#2E8B57'},
    'Traditional\nBanking': {'coefficient': 5, 'label': '~5\n(author est.)',
                             'note': "author's estimate", 'color': '#4169E1'},
    'Bitcoin\n(2024)': {'coefficient': 2, 'label': '2',
                        'note': 'by pool, 24 h around 4 Jul 2024 (CryptoSlate)',
                        'color': '#FF8C00'},
    'Ethereum\n(2024)': {'coefficient': 3, 'label': '3\n(3-5 by counting)',
                         'note': '3-5 by counting, Apr 2024 (Dune via Crypto Times)',
                         'color': '#6C3483'},
    'Solana\n(2024)': {'coefficient': 19, 'label': '19\n(1/3-stake threshold)',
                       'note': 'one-third-of-stake threshold (Helius 2024), not 51%',
                       'color': '#1ABC9C'},
}

fig, ax = plt.subplots(figsize=(12, 7))
names = list(systems_nk.keys())
coefficients = [systems_nk[n]['coefficient'] for n in names]
colors = [systems_nk[n]['color'] for n in names]

bars = ax.bar(range(len(names)), coefficients, color=colors, alpha=0.85,
              edgecolor='black', linewidth=1.5)
# The threshold of 10 is the author's illustrative cut-off, not an accepted standard.
ax.axhline(y=10, color='red', linestyle='--', linewidth=2, alpha=0.7,
           label="Author's illustrative cut-off for \"meaningful\" decentralization")
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, fontsize=9)
ax.set_ylabel('Nakamoto Coefficient\n(entities needed to control 51%)', fontsize=12)
ax.set_title('Nakamoto Coefficient: How Decentralized Is It Really?\n'
             'Counted by mining pool, Bitcoin (2) is about as concentrated as banking '
             '(~5, author estimate), or more',
             fontsize=12, fontweight='bold')
ax.set_ylim(0, 62)  # leaves room for the bar labels above the tallest bar (~50)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

for i, n in enumerate(names):
    ax.text(i, coefficients[i] + 0.5, systems_nk[n]['label'], ha='center', va='bottom',
            fontweight='bold', fontsize=10)
fig.text(0.5, 0.005,
         'Hand-entered values, not computed from raw data. Church and banking values are the '
         "author's estimates; crypto values are 2024 approximations from dated sources.",
         ha='center', va='bottom', fontsize=8, style='italic')

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('05_nakamoto_coefficient.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n{'System':<27} {'Nakamoto Coeff.':<18} {'Interpretation':<26} {'Basis'}")
print("-" * 107)
for name, data in systems_nk.items():
    clean = name.replace('\n', ' ')
    coeff = data['coefficient']
    # Bucket boundaries are the author's illustrative choice.
    if coeff <= 3:
        interp = "Highly centralized"
    elif coeff <= 10:
        interp = "Weakly decentralized"
    elif coeff <= 30:
        interp = "Moderately decentralized"
    else:
        interp = "Decentralized"
    print(f"  {clean:<25} {coeff:<18} {interp:<26} {data['note']}")
print("\n  Values are hand-entered, not computed from raw data by this script.")
print("  Solana's 19 uses a one-third threshold, so it is not directly comparable with the 51% rows.")
btc_coeff = systems_nk['Bitcoin\n(2024)']['coefficient']
bank_coeff = systems_nk['Traditional\nBanking']['coefficient']
print(f"\n  Bitcoin counted by mining pool ({btc_coeff}) is about as concentrated as the "
      f"banking estimate ({bank_coeff}), or more.")
print("  A pool is not an independent entity and 24 hours is a short snapshot: a rough guide.")
print("  Ethereum: three entities pass 51% if the unidentified 16.9% counts as one entity,")
print("  four or five if not.")
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

# The "temperature" curves below are hand-set, qualitative illustrations (arbitrary units,
# critical point T=50 chosen by the author), not measurements. They are not calibrated to
# the dates in the printed tables; the tables follow the article's narrative dating.
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
print(f"  {'Devastation':<20} {'1618-1648':<20} {'30 Years War (est. 4.5-8M dead)'}")
print(f"\n  Crypto phase transition:")
print(f"  {'Brewing':<20} {'2008-2013':<20} {'Niche tech discussion'}")
print(f"  {'Ignition':<20} {'2013-2017':<20} {'Price surge, media'}")
print(f"  {'CRITICAL POINT':<20} {'2017':<20} {'ICO mania'}")
print(f"  {'Explosion':<20} {'2018-2022':<20} {'Crashes, FTX, regulation'}")
cross_ref = int(reform_years[np.argmax(reform_temp >= critical)])
cross_crypto = int(crypto_years[np.argmax(crypto_temp >= critical)])
print(f"\n  Note: the 'temperature' curves are hand-set and qualitative. The curves cross T={critical}")
print(f"  in {cross_ref} (Reformation) and {cross_crypto} (crypto); the tables above use the article's")
print("  narrative dating (critical point = 1521 excommunication), not the crossing year.")
print("\n  The metaphor: once past the critical point there is no going back (an analogy, not a law).")
print("\n=> Saved: 06_phase_transition.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
