# Code & Cogito: 一通の手紙が、いかにして世界を変えたのか？人文主義の誕生とデータ分析
# Article: https://code-cogito.com/ja/humanism-birth-renaissance-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
from collections import Counter

# デモ用の中世キーワード集計（著者が手動設定した数値で、テキスト統計ではない）
medieval_text_keywords = {
    'God': 450, 'sin': 280, 'salvation': 220, 'soul': 310,
    'grace': 190, 'faith': 240, 'heaven': 180, 'hell': 160,
    'church': 200, 'divine': 170, 'eternal': 150, 'prayer': 140,
    'devil': 120, 'holy': 190, 'scripture': 130
}

# デモ用のルネサンスキーワード集計（著者が手動設定した数値で、テキスト統計ではない）
renaissance_text_keywords = {
    'human': 380, 'nature': 290, 'reason': 310, 'virtue': 270,
    'knowledge': 250, 'wisdom': 230, 'individual': 200, 'dignity': 180,
    'freedom': 220, 'beauty': 190, 'truth': 210, 'experience': 180,
    'mind': 240, 'education': 160, 'achievement': 140
}

# 以下は辞書をlistに変換しているだけで、フォント設定やグラフ描画のコードは含まれていない

medieval_words = list(medieval_text_keywords.keys())
medieval_counts = list(medieval_text_keywords.values())

renaissance_words = list(renaissance_text_keywords.keys())
renaissance_counts = list(renaissance_text_keywords.values())

import networkx as nx

# 建立思想影響網絡
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

# 繪製網絡圖
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

# | ペトラルカ（1340）
# |     |
# | ボッカッチョ（1360）
# |     |
# | サルターティ（1390）
# |     |
# | ブルーニ（1420）
# |     |
# | フィチーノ（1470）———— ピコ（1486）
# |     |
# | エラスムス（1510）
# |     |
# | トマス・モア（1516）

# | 概念の強度（0-100）
# | 
# | 神の権威：90 > 85 > 75 > 60 > 45 > 30 > 20
# | 個人の価値：10 > 15 > 30 > 50 > 70 > 85 > 90
# | 理性的思考：15 > 20 > 35 > 55 > 75 > 88 > 92
# | 
# | 年：     1300 1350 1400 1450 1500 1550 1600
