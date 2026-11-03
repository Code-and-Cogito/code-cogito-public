# Code & Cogito: 人文主義的崛起 vs 個人品牌時代
# Article: https://code-cogito.com/thought-revolution-01/
# All the code blocks of the article, in order. Program output is kept as comments.

# | import networkx as nx
# | import matplotlib.pyplot as plt
# | 
# | # 建立人文主義者示意網絡（節點、連線、權重都是作者設定的示意值，不是史料）
# | humanists = {
# |     'Erasmus': {'era': 'late', 'letters': 1800},
# |     'Petrarch': {'era': 'early', 'letters': 500},
# |     'Boccaccio': {'era': 'early', 'letters': 150},
# |     'Salutati': {'era': 'mid', 'letters': 300},
# |     'Bruni': {'era': 'mid', 'letters': 200},
# |     'Pico': {'era': 'mid', 'letters': 100},
# |     'Ficino': {'era': 'mid', 'letters': 400},
# |     'More': {'era': 'late', 'letters': 280},
# | }
# | 
# | connections = [
# |     ('Erasmus', 'More', 9), ('Erasmus', 'Ficino', 5),
# |     ('Erasmus', 'Pico', 3), ('Erasmus', 'Bruni', 4),
# |     ('Petrarch', 'Boccaccio', 10), ('Petrarch', 'Salutati', 7),
# |     ('Salutati', 'Bruni', 9), ('Boccaccio', 'Salutati', 8),
# |     ('Bruni', 'Ficino', 7), ('Ficino', 'Pico', 10),
# |     ('Ficino', 'Salutati', 4), ('More', 'Pico', 3),
# |     ('Pico', 'Bruni', 5),
# | ]
# | 
# | G = nx.Graph()
# | for name, attrs in humanists.items():
# |     G.add_node(name, **attrs)
# | G.add_weighted_edges_from(connections)
# | 
# | # 中介中心性：誰是不同群體之間的橋樑？
# | betweenness = nx.betweenness_centrality(G)
# | 
# | print("[Betweenness Centrality - Who bridges different groups?]")
# | for name in sorted(betweenness, key=betweenness.get, reverse=True):
# |     print(f"  {name:<12}: {betweenness[name]:.3f}")

# | [Betweenness Centrality - Who bridges different groups?]
# |   Salutati    : 0.476
# |   Bruni       : 0.214
# |   Ficino      : 0.214
# |   Erasmus     : 0.119
# |   Pico        : 0.119
# |   Petrarch    : 0.000
# |   Boccaccio   : 0.000
# |   More        : 0.000
