#!/usr/bin/env python3
"""Free highlight code from Code & Cogito Renaissance Series.
Article 01: Florence Network Analysis - Why Florence became the cradle of the Renaissance.
"""

import networkx as nx
import matplotlib.pyplot as plt

# === 8-City Italian Trade Network (15th Century) ===

cities = {
    'Florence': {'population': 60000},
    'Venice': {'population': 100000},
    'Milan': {'population': 80000},
    'Rome': {'population': 50000},
    'Genoa': {'population': 60000},
    'Naples': {'population': 40000},
    'Bologna': {'population': 30000},
    'Siena': {'population': 20000}
}

trade_routes = [
    ('Florence', 'Venice', 8),
    ('Florence', 'Milan', 7),
    ('Florence', 'Rome', 9),
    ('Florence', 'Genoa', 6),
    ('Florence', 'Bologna', 5),
    ('Florence', 'Siena', 7),
    ('Venice', 'Milan', 6),
    ('Venice', 'Bologna', 5),
    ('Milan', 'Genoa', 8),
    ('Rome', 'Naples', 7),
    ('Genoa', 'Milan', 5),
    ('Bologna', 'Venice', 4)
]

G = nx.Graph()
for city, attrs in cities.items():
    G.add_node(city, **attrs)
G.add_weighted_edges_from(trade_routes)

# === Centrality Analysis ===

print("=" * 60)
print("Florence Network Analysis: 15th Century Italian City Network")
print("=" * 60)

print(f"\nNodes (cities): {G.number_of_nodes()}")
print(f"Edges (trade routes): {G.number_of_edges()}")
print(f"Network density: {nx.density(G):.3f}")

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("\n[Betweenness Centrality Ranking]")
print("Measures: how many shortest paths pass through a city\n")

for city in sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True):
    print(f"{city:<12}: {betweenness_centrality[city]:.3f}")

florence_bc = betweenness_centrality['Florence']
venice_bc = betweenness_centrality['Venice']
milan_bc = betweenness_centrality['Milan']

print(f"\n[Key Finding]")
print(f"Florence betweenness centrality:")
print(f"  - {florence_bc/venice_bc:.2f}x Venice")
print(f"  - {florence_bc/milan_bc:.2f}x Milan")
print(f"  - {florence_bc/betweenness_centrality['Rome']:.2f}x Rome")
print(f"\n=> More information, capital, and talent flowed through Florence")

# === Visualization ===

plt.figure(figsize=(12, 9))

node_sizes = [cities[city]['population'] / 80 for city in G.nodes()]
node_colors = [betweenness_centrality[city] for city in G.nodes()]
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors,
                       cmap=plt.cm.YlOrRd, alpha=0.9, edgecolors='black', linewidths=2)

edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=[w/3 for w in edge_weights],
                       alpha=0.5, edge_color='gray')

nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

plt.title('15th Century Italian Trade Network\nNode color = betweenness centrality, size = population',
          fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.savefig('florence_network_basic.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved: florence_network_basic.png")
