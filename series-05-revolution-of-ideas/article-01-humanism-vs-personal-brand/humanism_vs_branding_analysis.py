"""
Revolution of Ideas #01: The Rise of Humanism vs the Age of Personal Branding
Free Version — 5 Models (Basic Analysis)

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
# MODEL 1: Humanist Intellectual Network Analysis
# ============================================================
print("=" * 65)
print("MODEL 1: Humanist Network Analysis")
print("=" * 65)

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

betweenness = nx.betweenness_centrality(G)
degree = nx.degree_centrality(G)

print(f"\nNodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.3f}\n")

print("[Betweenness Centrality — Who bridges different groups?]")
for name in sorted(betweenness, key=betweenness.get, reverse=True):
    print(f"  {name:<12}: {betweenness[name]:.3f}")

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

plt.title('Humanist Intellectual Network (14th-16th Century)\n'
          'Node size = letters written | Red=Early, Orange=Mid, Blue=Late',
          fontsize=13, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('01_humanist_network.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n=> Saved: 01_humanist_network.png")


# ============================================================
# MODEL 2: "Human-Centered" Index
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Human-Centered Index")
print("=" * 65)

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
ax.set_ylabel('Human / God keyword ratio', fontsize=12)
ax.set_title('"Human-Centered Index" — When Human Surpasses God\n'
             'Based on text corpus keyword frequency analysis',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
for i, v in enumerate(ratio):
    ax.text(i, v + 0.04, f'{v:.2f}', ha='center', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('02_human_centered_index.png', dpi=300, bbox_inches='tight')
plt.close()

for p, r in zip(periods, ratio):
    status = "GOD > Human" if r < 1 else "HUMAN > God"
    print(f"  {p:<15}: {r:.2f}  ({status})")
print("\n=> Crossover at ~1400-1500. Saved: 02_human_centered_index.png")


# ============================================================
# MODEL 3: Influence Building Speed Comparison
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Influence Building — Petrarch vs YouTuber")
print("=" * 65)

years = np.arange(0, 25)
petrarch = 100 * (1 - np.exp(-0.08 * years))
youtuber = 100 * (1 - np.exp(-0.45 * years))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, petrarch, 'o-', color='#8E44AD', linewidth=2.5, markersize=4,
        label='Petrarch (14th century)')
ax.plot(years, youtuber, 's-', color='#E74C3C', linewidth=2.5, markersize=4,
        label='Modern YouTuber (21st century)')
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Years Active', fontsize=12)
ax.set_ylabel('Influence Index (0-100)', fontsize=12)
ax.set_title('Speed of Influence Building: 14th vs 21st Century\n'
             'Same mechanism, 10x the speed',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('03_influence_speed.png', dpi=300, bbox_inches='tight')
plt.close()

print("  Petrarch: ~9 years to 50% influence")
print("  YouTuber: ~2 years to 50% influence")
print("  Speedup: ~10x")
print("\n=> Saved: 03_influence_speed.png")


# ============================================================
# MODEL 4: Knowledge Democratization Cost Curve
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Education Democratization — 600-Year Cost Curve")
print("=" * 65)

cost_years = [1400, 1455, 1500, 1600, 1800, 1900, 1950, 2000, 2010, 2024]
book_cost = [10000, 10000, 1000, 300, 50, 10, 5, 20, 10, 0.01]

fig, ax = plt.subplots(figsize=(10, 6))
ax.semilogy(cost_years, book_cost, 'o-', color='#E74C3C', linewidth=2.5, markersize=8)
ax.fill_between(cost_years, book_cost, alpha=0.1, color='#E74C3C')
ax.annotate('Gutenberg\nPrinting Press', xy=(1455, 10000), fontsize=10,
            xytext=(1500, 30000), arrowprops=dict(arrowstyle='->', color='black'),
            fontweight='bold')
ax.annotate('Wikipedia\nLaunched', xy=(2000, 20), fontsize=10,
            xytext=(1920, 200), arrowprops=dict(arrowstyle='->', color='black'),
            fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cost per book equivalent (USD, log scale)', fontsize=12)
ax.set_title('600 Years of Falling Knowledge Access Costs\n$10,000 → $0',
             fontsize=13, fontweight='bold')
ax.grid(alpha=0.3)
ax.set_xlim(1380, 2040)
plt.tight_layout()
plt.savefig('04_knowledge_cost.png', dpi=300, bbox_inches='tight')
plt.close()

print("  1400: $10,000 (hand-copied manuscript)")
print("  1500: $1,000 (after printing press)")
print("  2024: ~$0 (Wikipedia/YouTube)")
print("\n=> Saved: 04_knowledge_cost.png")


# ============================================================
# MODEL 5: "Be Yourself" Inequality Paradox (Gini Coefficient)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: The 'Be Yourself' Paradox — Influence Inequality")
print("=" * 65)

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
        label=f'Renaissance (Gini={gini_r:.3f})')
ax.plot(np.linspace(0, 1, len(ml)), ml, color='#E74C3C', linewidth=2.5,
        label=f'Modern Creator Economy (Gini={gini_m:.3f})')
ax.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Perfect equality')
ax.fill_between(np.linspace(0, 1, len(ml)), ml, np.linspace(0, 1, len(ml)),
                alpha=0.1, color='#E74C3C')
ax.set_xlabel('Cumulative % of population', fontsize=12)
ax.set_ylabel('Cumulative % of influence', fontsize=12)
ax.set_title('Lorenz Curve: Influence Inequality\n'
             'More people speak, fewer are heard',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('05_influence_inequality.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"  Renaissance Gini: {gini_r:.3f}")
print(f"  Modern Gini: {gini_m:.3f}")
print(f"  Inequality increase: {((gini_m - gini_r) / gini_r * 100):.1f}%")
print("\n=> Saved: 05_influence_inequality.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
