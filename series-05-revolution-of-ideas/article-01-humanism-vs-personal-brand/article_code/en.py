# Code & Cogito: The Rise of Humanism vs the Age of Personal Branding
# Article: https://code-cogito.com/en/thought-revolution-01-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import networkx as nx
import matplotlib.pyplot as plt

# Build an illustrative humanist network (nodes, edges and weights are hand-set, not historical records)
humanists = {
    'Erasmus': {'era': 'late', 'letters': 1800},
    'Petrarch': {'era': 'early', 'letters': 500},
    'Boccaccio': {'era': 'early', 'letters': 150},
    'Salutati': {'era': 'mid', 'letters': 300},
    'Bruni': {'era': 'mid', 'letters': 200},
    'Pico': {'era': 'mid', 'letters': 100},
    'Ficino': {'era': 'mid', 'letters': 400},
    'More': {'era': 'late', 'letters': 280},
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

# Betweenness centrality: who bridges different groups?
betweenness = nx.betweenness_centrality(G)

print("[Betweenness Centrality - Who bridges different groups?]")
for name in sorted(betweenness, key=betweenness.get, reverse=True):
    print(f"  {name:<12}: {betweenness[name]:.3f}")

# | [Betweenness Centrality - Who bridges different groups?]
# |   Salutati    : 0.476
# |   Bruni       : 0.214
# |   Ficino      : 0.214
# |   Erasmus     : 0.119
# |   Pico        : 0.119
# |   Petrarch    : 0.000
# |   Boccaccio   : 0.000
# |   More        : 0.000
