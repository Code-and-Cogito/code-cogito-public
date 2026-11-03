# Code & Cogito: なぜフィレンツェはルネサンスの揺籃となったのか？
# Article: https://code-cogito.com/ja/florence-renaissance-cradle-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import networkx as nx

# Illustrative model: cities, links and weights are author-chosen

print("=" * 60)
print("Florence Network Analysis: 15th Century Italian City Network")
print("=" * 60)

# ===== Basic Network: 8 Major Cities =====

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

print(f"\nNodes (cities): {G.number_of_nodes()}")
print(f"Edges (trade routes): {G.number_of_edges()}")
print(f"Network density: {nx.density(G):.3f}")

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("\n[Betweenness Centrality Ranking]")
print("Measures: how many shortest paths pass through a city (hub status)\n")

for city in sorted(betweenness_centrality,
                   key=betweenness_centrality.get,
                   reverse=True):
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

# | ============================================================
# | Florence Network Analysis: 15th Century Italian City Network
# | ============================================================
# | 
# | Nodes (cities): 8
# | Edges (trade routes): 10
# | Network density: 0.357
# | 
# | [Betweenness Centrality Ranking]
# | Measures: how many shortest paths pass through a city (hub status)
# | 
# | Florence    : 0.762
# | Rome        : 0.286
# | Venice      : 0.024
# | Milan       : 0.024
# | Genoa       : 0.000
# | Naples      : 0.000
# | Bologna     : 0.000
# | Siena       : 0.000
# | 
# | [Key Finding]
# | Florence betweenness centrality:
# |   - 32.00x Venice
# |   - 32.00x Milan
# |   - 2.67x Rome
# | 
# | => More information, capital, and talent flowed through Florence

node_sizes = [cities[city]['population']/80 for city in G.nodes()]
node_colors = [betweenness_centrality[city] for city in G.nodes()]
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
