# Code & Cogito: メディチ家：金融帝国の文化投資
# Article: https://code-cogito.com/ja/medici-family-cultural-investment-ja/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import networkx as nx
import numpy as np

# Set Chinese font

print("=" * 60)
print("Medici Bank Network Analysis: 1397-1494")
print("=" * 60)

# ===== Medici Bank Branch Data =====

branches = {
    'Florence': {
        'pos': (11.25, 43.77), 'opened': 1397, 'closed': 1494,
        'revenue': 100000, 'type': 'headquarters'
    },
    'Rome': {
        'pos': (12.49, 41.90), 'opened': 1397, 'closed': 1478,
        'revenue': 80000, 'type': 'branch'
    },
    'Venice': {
        'pos': (12.32, 45.44), 'opened': 1402, 'closed': 1469,
        'revenue': 50000, 'type': 'branch'
    },
    'Geneva': {
        'pos': (6.14, 46.20), 'opened': 1424, 'closed': 1478,
        'revenue': 45000, 'type': 'branch'
    },
    'Bruges': {
        'pos': (3.22, 51.21), 'opened': 1439, 'closed': 1480,
        'revenue': 40000, 'type': 'branch'
    },
    'London': {
        'pos': (-0.13, 51.51), 'opened': 1446, 'closed': 1478,
        'revenue': 35000, 'type': 'branch'
    },
    'Avignon': {
        'pos': (4.81, 43.95), 'opened': 1446, 'closed': 1478,
        'revenue': 30000, 'type': 'branch'
    },
    'Milan': {
        'pos': (9.19, 45.46), 'opened': 1452, 'closed': 1478,
        'revenue': 25000, 'type': 'branch'
    }
}

G = nx.Graph()
for city, data in branches.items():
    G.add_node(city, **data)

headquarters = 'Florence'
for city in branches.keys():
    if city != headquarters:
        G.add_edge(headquarters, city,
                  weight=branches[city]['revenue']/10000)

print("\n[Branch Revenue Ranking]")
print(f"{'Branch':<15} {'Revenue (florins)':<20} {'Opened':<12} {'Closed':<12}")
print("-" * 65)

for city, data in sorted(branches.items(),
                        key=lambda x: x[1]['revenue'],
                        reverse=True):
    print(f"{city:<15} {data['revenue']:<20,} {data['opened']:<12} {data['closed']:<12}")

total_revenue = sum(b['revenue'] for b in branches.values())
print(f"\n[Key Findings]")
print(f"Total branches: {len(branches)}")
print(f"Operating period: 1397-1494 (97 years)")
print(f"Peak (1452-1469): 8 branches operating simultaneously")
print(f"Total annual revenue: {total_revenue:,} florins")
print(f"\n=> The Medici Bank controlled key nodes of European finance")

pos = {city: data['pos'] for city, data in branches.items()}
node_sizes = [branches[city]['revenue']/80 for city in G.nodes()]
node_colors = ['#C41E3A' if branches[city]['type'] == 'headquarters'
               else '#FFD700' for city in G.nodes()]

edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]

legend_elements = [
    plt.scatter([], [], s=200, c='#C41E3A', edgecolors='black',
               linewidths=2, label='Headquarters (Florence)'),
    plt.scatter([], [], s=200, c='#FFD700', edgecolors='black',
               linewidths=2, label='Branch')
]
