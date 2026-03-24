#!/usr/bin/env python3
"""Free highlight code from Code & Cogito Renaissance Series.
Article 02: Medici Bank Network - Hub-and-spoke financial empire analysis.
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# === Medici Bank Branch Data (1397-1494) ===

branches = {
    'Florence': {'pos': (11.25, 43.77), 'opened': 1397, 'closed': 1494, 'revenue': 100000, 'type': 'headquarters'},
    'Rome':     {'pos': (12.49, 41.90), 'opened': 1397, 'closed': 1478, 'revenue': 80000, 'type': 'branch'},
    'Venice':   {'pos': (12.32, 45.44), 'opened': 1402, 'closed': 1469, 'revenue': 50000, 'type': 'branch'},
    'Geneva':   {'pos': (6.14, 46.20),  'opened': 1424, 'closed': 1478, 'revenue': 45000, 'type': 'branch'},
    'Bruges':   {'pos': (3.22, 51.21),  'opened': 1439, 'closed': 1480, 'revenue': 40000, 'type': 'branch'},
    'London':   {'pos': (-0.13, 51.51), 'opened': 1446, 'closed': 1478, 'revenue': 35000, 'type': 'branch'},
    'Avignon':  {'pos': (4.81, 43.95),  'opened': 1446, 'closed': 1478, 'revenue': 30000, 'type': 'branch'},
    'Milan':    {'pos': (9.19, 45.46),  'opened': 1452, 'closed': 1478, 'revenue': 25000, 'type': 'branch'}
}

# === Build Hub-and-Spoke Network ===

G = nx.Graph()
for city, data in branches.items():
    G.add_node(city, **data)

for city in branches:
    if city != 'Florence':
        G.add_edge('Florence', city, weight=branches[city]['revenue'] / 10000)

# === Revenue Ranking ===

print("=" * 60)
print("Medici Bank Network Analysis: 1397-1494")
print("=" * 60)

print(f"\n{'Branch':<15} {'Revenue (florins)':<20} {'Opened':<12} {'Closed':<12}")
print("-" * 65)

for city, data in sorted(branches.items(), key=lambda x: x[1]['revenue'], reverse=True):
    print(f"{city:<15} {data['revenue']:<20,} {data['opened']:<12} {data['closed']:<12}")

total_revenue = sum(b['revenue'] for b in branches.values())
print(f"\nTotal branches: {len(branches)}")
print(f"Operating period: 1397-1494 (97 years)")
print(f"Peak (1450-1470): 8 branches simultaneously")
print(f"Total annual revenue: {total_revenue:,} florins")

# === Visualization ===

fig, ax = plt.subplots(1, 1, figsize=(14, 10))

pos = {city: data['pos'] for city, data in branches.items()}
node_sizes = [branches[city]['revenue'] / 80 for city in G.nodes()]
node_colors = ['#C41E3A' if branches[city]['type'] == 'headquarters' else '#FFD700'
               for city in G.nodes()]

edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw_networkx_edges(G, pos, ax=ax, width=[w/2 for w in weights],
                       alpha=0.4, edge_color='gray')
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes,
                       node_color=node_colors, alpha=0.9,
                       edgecolors='black', linewidths=2)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold')

ax.set_title('Medici Bank European Branch Network (1397-1494)\nNode size = revenue',
             fontsize=14, fontweight='bold', pad=15)
ax.axis('off')

legend_elements = [
    plt.scatter([], [], s=200, c='#C41E3A', edgecolors='black', linewidths=2, label='Headquarters'),
    plt.scatter([], [], s=200, c='#FFD700', edgecolors='black', linewidths=2, label='Branch')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

plt.tight_layout()
plt.savefig('medici_bank_network_basic.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved: medici_bank_network_basic.png")
