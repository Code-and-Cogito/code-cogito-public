"""
Revolution of Ideas #01: The Rise of Humanism vs the Age of Personal Branding
Free Version — 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

DATA NOTE: All inputs in this script are illustrative (hand-set or synthetic);
nothing here is historical data. The network, the keyword-frequency index, the
influence-curve constants, the book-cost series and the random samples are
numbers chosen to demonstrate each method, not measurements. Read every output
as "what this toy model would show", not as a finding about history.

Requirements: pip install networkx matplotlib numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Humanist Intellectual Network Analysis (illustrative network)
# ============================================================
print("=" * 65)
print("MODEL 1: Humanist Network Analysis (illustrative network)")
print("=" * 65)

# NOTE: This is an illustrative toy network, not a historical record.
# The nodes, edges, edge weights and "letters" counts below are hand-set rough
# numbers. Some edges join people who never lived at the same time (for
# example Ficino and Salutati, or Erasmus and Bruni), so the results say
# "if the network looked like this ...", not what history was.
# For scale: the standard edition of Erasmus's correspondence counts
# 3,141 letters, sent and received (see the article's reference list:
# Collected Works of Erasmus, vol. 21, University of Toronto Press).
humanists = {
    'Erasmus': {'era': 'late', 'letters': 1800, 'country': 'Netherlands'},
    'Petrarch': {'era': 'early', 'letters': 500, 'country': 'Italy'},
    'Boccaccio': {'era': 'early', 'letters': 150, 'country': 'Italy'},
    'Salutati': {'era': 'mid', 'letters': 300, 'country': 'Italy'},
    'Bruni': {'era': 'mid', 'letters': 200, 'country': 'Italy'},
    'Pico': {'era': 'mid', 'letters': 100, 'country': 'Italy'},
    'Ficino': {'era': 'mid', 'letters': 400, 'country': 'Italy'},
    'More': {'era': 'late', 'letters': 280, 'country': 'England'},
}

# (person A, person B, hand-set tie strength 1-10)
connections = [
    ('Erasmus', 'More', 9), ('Erasmus', 'Ficino', 5),
    ('Erasmus', 'Pico', 3), ('Erasmus', 'Bruni', 4),
    ('Petrarch', 'Boccaccio', 10), ('Petrarch', 'Salutati', 7),
    ('Salutati', 'Bruni', 9), ('Boccaccio', 'Salutati', 8),
    ('Bruni', 'Ficino', 7), ('Ficino', 'Pico', 10),
    ('Ficino', 'Salutati', 4), ('More', 'Pico', 3),
    ('Pico', 'Bruni', 5),
]

G = nx.Graph()
for name, attrs in humanists.items():
    G.add_node(name, **attrs)
G.add_weighted_edges_from(connections)

# nx.betweenness_centrality is unweighted by default (edge weights are ignored)
betweenness = nx.betweenness_centrality(G)
degree = nx.degree_centrality(G)

print(f"\nNodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.3f}\n")

print("[Betweenness Centrality — Who bridges different groups in this toy graph?]")
for name in sorted(betweenness, key=betweenness.get, reverse=True):
    print(f"  {name:<12}: {betweenness[name]:.3f}")

# Toy-graph check: what happens if the top bridge node is removed?
bridge = max(betweenness, key=betweenness.get)
H = G.copy()
H.remove_node(bridge)
parts = sorted((sorted(c) for c in nx.connected_components(H)), key=len)
print(f"\n[Toy-graph check — remove {bridge}]")
print(f"  Connected groups left: {parts}")

# Visualization
plt.figure(figsize=(12, 9))
era_colors = {'early': '#E74C3C', 'mid': '#F39C12', 'late': '#3498DB'}
node_colors = [era_colors[humanists[n]['era']] for n in G.nodes()]
node_sizes = [humanists[n]['letters'] * 2.5 + 200 for n in G.nodes()]
pos = nx.spring_layout(G, k=2.5, iterations=80, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors,
                       alpha=0.9, edgecolors='black', linewidths=2)
edge_weights = [G[u][v]['weight'] * 0.4 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_weights, alpha=0.4, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

plt.title('Illustrative Humanist Network (14th-16th Century)\n'
          'Hand-set nodes, edges and letter counts (not a historical record)\n'
          'Node size = hand-set letter count | Red=Early, Orange=Mid, Blue=Late',
          fontsize=13, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('01_humanist_network.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n=> Saved: 01_humanist_network.png")


# ============================================================
# MODEL 2: "Human-Centered" Index (illustrative index)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Human-Centered Index (illustrative index)")
print("=" * 65)

# NOTE: These keyword frequencies are hand-typed illustrative numbers.
# No text corpus was analysed; the ratios are plain arithmetic on these inputs.
periods = ['1200-1300', '1300-1400', '1400-1500', '1500-1600']
god_freq = [85, 72, 48, 31]
human_freq = [12, 25, 52, 71]
ratio = [h / g for h, g in zip(human_freq, god_freq)]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(periods))
colors = ['#8E44AD', '#C0392B', '#E67E22', '#2ECC71']
bars = ax.bar(x, ratio, 0.55, color=colors, alpha=0.85, edgecolor='black', linewidth=1)
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Parity (Human = God)')
ax.set_xticks(x)
ax.set_xticklabels(periods, fontsize=11)
ax.set_ylabel('Human / God keyword ratio (illustrative)', fontsize=12)
ax.set_title('"Human-Centered Index" — When Human Surpasses God\n'
             'Illustrative index (hand-set frequencies, no corpus)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
for i, v in enumerate(ratio):
    ax.text(i, v + 0.04, f'{v:.2f}', ha='center', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('02_human_centered_index.png', dpi=300, bbox_inches='tight')
plt.close()

print("  (hand-set keyword frequencies, no corpus was analysed)")
for p, r in zip(periods, ratio):
    status = "GOD > Human" if r < 1 else "HUMAN > God"
    print(f"  {p:<15}: {r:.2f}  ({status})")
print("\n=> Crossover at ~1400-1500 in these illustrative numbers. "
      "Saved: 02_human_centered_index.png")


# ============================================================
# MODEL 3: Influence Building Speed Comparison (illustrative curves)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Influence Building — Petrarch vs YouTuber (illustrative)")
print("=" * 65)

# influence(t) = 100 * (1 - exp(-k * t)); the rate constants k are assumed by us,
# not estimated from data. The time to reach 50% influence is ln(2) / k.
k_petrarch = 0.08
k_youtuber = 0.45

years = np.arange(0, 25)
petrarch = 100 * (1 - np.exp(-k_petrarch * years))
youtuber = 100 * (1 - np.exp(-k_youtuber * years))

half_petrarch = np.log(2) / k_petrarch   # about 8.7 years
half_youtuber = np.log(2) / k_youtuber   # about 1.5 years
speedup = half_petrarch / half_youtuber  # = k_youtuber / k_petrarch, about 5.6x

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, petrarch, 'o-', color='#8E44AD', linewidth=2.5, markersize=4,
        label=f'Petrarch (14th century), k = {k_petrarch}')
ax.plot(years, youtuber, 's-', color='#E74C3C', linewidth=2.5, markersize=4,
        label=f'Modern YouTuber (21st century), k = {k_youtuber}')
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Years Active', fontsize=12)
ax.set_ylabel('Influence Index (0-100)', fontsize=12)
ax.set_title('Speed of Influence Building: 14th vs 21st Century\n'
             f'Same mechanism, ~{speedup:.1f}x the speed (illustrative k)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('03_influence_speed.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"  Petrarch: ~{half_petrarch:.1f} years to 50% influence (ln2/k, k = {k_petrarch})")
print(f"  YouTuber: ~{half_youtuber:.1f} years to 50% influence (ln2/k, k = {k_youtuber})")
print(f"  Speedup: ~{speedup:.1f}x (follows from the assumed k values)")
print("\n=> Saved: 03_influence_speed.png")


# ============================================================
# MODEL 4: Knowledge Democratization Cost Curve (illustrative values)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Education Democratization — 600-Year Cost Curve (illustrative)")
print("=" * 65)

# NOTE: book_cost holds hand-set illustrative values (USD per book equivalent),
# NOT historical prices. For empirical work on how book prices fell after
# printing arrived, see Dittmar (2011), "Information Technology and Economic
# Change: The Impact of the Printing Press", Quarterly Journal of Economics
# 126(3), listed in the article's references.
# The press is dated c. 1450 (the Gutenberg Bible was finished c. 1454-55).
# The last value is 0.01 rather than 0 only so the log axis can draw it.
cost_years = [1400, 1450, 1500, 1600, 1800, 1900, 1950, 2001, 2010, 2024]
book_cost = [10000, 10000, 1000, 300, 50, 10, 5, 20, 10, 0.01]

fig, ax = plt.subplots(figsize=(10, 6))
ax.semilogy(cost_years, book_cost, 'o-', color='#E74C3C', linewidth=2.5, markersize=8)
ax.fill_between(cost_years, book_cost, alpha=0.1, color='#E74C3C')
ax.annotate('Gutenberg\nPrinting Press\n(c. 1450)', xy=(1450, 10000), fontsize=10,
            xytext=(1530, 1800), arrowprops=dict(arrowstyle='->', color='black'),
            fontweight='bold')
ax.annotate('Wikipedia\nLaunched (2001)', xy=(2001, 20), fontsize=10,
            xytext=(1920, 200), arrowprops=dict(arrowstyle='->', color='black'),
            fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Illustrative cost per book equivalent (USD, log scale)', fontsize=12)
# escape the dollar signs so matplotlib does not treat them as math mode
ax.set_title('600 Years of Falling Knowledge Access Costs (illustrative values)\n'
             r'\$10,000 → close to \$0',
             fontsize=13, fontweight='bold')
ax.grid(alpha=0.3)
ax.set_xlim(1380, 2040)
plt.tight_layout()
plt.savefig('04_knowledge_cost.png', dpi=300, bbox_inches='tight')
plt.close()

print("  (hand-set illustrative values, not historical prices)")
print(f"  1400: ${book_cost[0]:,.0f} (hand-copied manuscript, illustrative)")
print(f"  1500: ${book_cost[2]:,.0f} (after printing press, illustrative)")
print(f"  2024: ~$0 (hard-coded as ${book_cost[-1]} for the log axis; Wikipedia/YouTube)")
print("\n=> Saved: 04_knowledge_cost.png")


# ============================================================
# MODEL 5: "Be Yourself" Inequality Paradox (Gini Coefficient, simulated)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: The 'Be Yourself' Paradox — Influence Inequality (simulated)")
print("=" * 65)

# NOTE: Simulated distributions. The samples are random draws (fixed seed 42)
# from exponential mixtures whose scales we chose; they are not measured
# influence data, so the Gini values describe the simulation only.
np.random.seed(42)

renaissance = np.concatenate([
    np.random.exponential(1, 50),
    np.random.exponential(10, 15),
    np.random.exponential(100, 3)
])

modern = np.concatenate([
    np.random.exponential(0.1, 5000),
    np.random.exponential(1, 2000),
    np.random.exponential(10, 500),
    np.random.exponential(100, 50),
    np.random.exponential(10000, 5)
])

def gini(arr):
    arr = np.sort(arr)
    n = len(arr)
    idx = np.arange(1, n + 1)
    return (2 * np.sum(idx * arr) / (n * np.sum(arr))) - (n + 1) / n

def lorenz(arr):
    arr = np.sort(arr)
    cumsum = np.cumsum(arr)
    return np.insert(cumsum / cumsum[-1], 0, 0)

gini_r = gini(renaissance)
gini_m = gini(modern)

fig, ax = plt.subplots(figsize=(10, 7))
rl = lorenz(renaissance)
ml = lorenz(modern)
ax.plot(np.linspace(0, 1, len(rl)), rl, color='#8E44AD', linewidth=2.5,
        label=f'Simulated "Renaissance" (n={len(renaissance)}, Gini={gini_r:.3f})')
ax.plot(np.linspace(0, 1, len(ml)), ml, color='#E74C3C', linewidth=2.5,
        label=f'Simulated "modern creator economy" (n={len(modern):,}, Gini={gini_m:.3f})')
ax.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Perfect equality')
ax.fill_between(np.linspace(0, 1, len(ml)), ml, np.linspace(0, 1, len(ml)),
                alpha=0.1, color='#E74C3C')
ax.set_xlabel('Cumulative % of population', fontsize=12)
ax.set_ylabel('Cumulative % of influence', fontsize=12)
ax.set_title('Lorenz Curve: Influence Inequality (simulated distributions)\n'
             'More people speak, fewer are heard',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('05_influence_inequality.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"  Simulated Renaissance: {len(renaissance)} participants")
print(f"  Simulated modern creators: {len(modern):,} participants")
print(f"  Renaissance Gini: {gini_r:.3f}")
print(f"  Modern Gini: {gini_m:.3f}")
print(f"  Inequality increase: {((gini_m - gini_r) / gini_r * 100):.1f}%")
print("\n=> Saved: 05_influence_inequality.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE (all inputs illustrative or simulated)")
print("Output files: 01-05_*.png")
print("=" * 65)
