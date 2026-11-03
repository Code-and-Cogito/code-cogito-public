# Code & Cogito: Humanism — The Birth of Human Dignity
# Article: https://code-cogito.com/en/humanism-the-birth-of-human-dignity-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import networkx as nx

# Build the humanist influence network
G = nx.DiGraph()

ancient_philosophers = ['Plato', 'Aristotle', 'Cicero', 'Seneca']
byzantine_scholars = ['Chrysoloras', 'Bessarion', 'Gemistus']
italian_humanists = ['Petrarch', 'Ficino', 'Pico', 'Erasmus', 'More']

G.add_nodes_from(ancient_philosophers, group='ancient')
G.add_nodes_from(byzantine_scholars, group='byzantine')
G.add_nodes_from(italian_humanists, group='humanist')

influences = [
    ('Plato', 'Chrysoloras'), ('Plato', 'Gemistus'),
    ('Aristotle', 'Bessarion'),
    ('Chrysoloras', 'Ficino'), ('Gemistus', 'Ficino'),
    ('Bessarion', 'Ficino'), ('Bessarion', 'Pico'),
    ('Plato', 'Ficino'), ('Plato', 'Pico'),
    ('Cicero', 'Petrarch'), ('Cicero', 'Erasmus'),
    ('Seneca', 'Petrarch'), ('Aristotle', 'Pico'),
    ('Petrarch', 'Ficino'), ('Ficino', 'Pico'),
    ('Pico', 'Erasmus'), ('Erasmus', 'More'),
]

G.add_edges_from(influences)
centrality = nx.betweenness_centrality(G)

# Draw the network
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

color_map = []
for node in G.nodes():
    if node in ancient_philosophers:
        color_map.append('#FFD700')
    elif node in byzantine_scholars:
        color_map.append('#9370DB')
    else:
        color_map.append('#4169E1')

node_sizes = [3000 * centrality[node] + 300 for node in G.nodes()]

# | Petrarch (1340)
# |     |
# | Boccaccio (1360)
# |     |
# | Salutati (1390)
# |     |
# | Bruni (1420)
# |     |
# | Ficino (1470) ———— Pico (1486)
# |     |
# | Erasmus (1510)
# |     |
# | More (1516)
