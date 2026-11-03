# Code & Cogito: 理性が新たな神となるとき：啓蒙運動はいかにして恐怖政治に至ったか
# Article: https://code-cogito.com/ja/enlightenment-age-of-reason-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import networkx as nx
import pandas as pd
import numpy as np

# NetworkX: 思想家の影響力ネットワークを構築
G = nx.DiGraph()

# PageRank: 最も影響力のある思想家を特定
pagerank = nx.pagerank(G)

# 指数成長モデル: 科学出版の爆発
def exponential_growth(t, initial, rate):
    return initial * np.exp(rate * t)

import networkx as nx
import pandas as pd

# 思想家の影響ネットワークを構築
G = nx.DiGraph()

thinkers = {
    'Locke': 1689, 'Voltaire': 1734, 'Montesquieu': 1748,
    'Rousseau': 1762, 'Hume': 1739, 'Kant': 1781,
    'Smith': 1776, 'Diderot': 1751, 'Descartes': 1637,
    'Spinoza': 1677, 'Leibniz': 1710, 'D_Alembert': 1751
}

for thinker, year in thinkers.items():
    G.add_node(thinker, year=year)

# 影響関係を追加
influences = [
    ('Descartes', 'Spinoza'), ('Descartes', 'Locke'),
    ('Locke', 'Voltaire'), ('Locke', 'Montesquieu'),
    ('Locke', 'Rousseau'), ('Voltaire', 'Diderot'),
    ('Voltaire', 'Rousseau'), ('Hume', 'Kant'),
    ('Hume', 'Smith'), ('Rousseau', 'Kant'),
]

G.add_edges_from(influences)

# PageRankを計算
pagerank = nx.pagerank(G, alpha=0.85)
betweenness = nx.betweenness_centrality(G)

# ソートして出力
sorted_thinkers = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
for thinker, score in sorted_thinkers[:5]:
    print(f"{thinker}: PageRank={score:.3f}, Betweenness={betweenness[thinker]:.2f}")

# | Kant: PageRank=0.176, Betweenness=0.00
# | Rousseau: PageRank=0.112, Betweenness=0.03
# | Diderot: PageRank=0.090, Betweenness=0.00
# | Locke: PageRank=0.080, Betweenness=0.05
# | Smith: PageRank=0.080, Betweenness=0.00

import pandas as pd
import numpy as np

cities = pd.DataFrame({
    'city': ['London', 'Paris', 'Edinburgh', 'Berlin', 'Geneva', 'Philadelphia'],
    'year': [1689, 1734, 1739, 1740, 1750, 1776],
    'key_figure': ['Locke', 'Voltaire', 'Hume', 'Frederick', 'Rousseau', 'Franklin']
})

cities['time_gap'] = cities['year'].diff()

print("City-to-city propagation intervals:")
for _, row in cities.iterrows():
    if pd.notna(row['time_gap']):
        print(f"  {row['city']:15} gap from previous: {int(row['time_gap'])} years")

avg_gap = cities['time_gap'].mean()
print(f"\nAverage: {avg_gap:.1f} years per new center")

import numpy as np
from scipy.optimize import curve_fit

years = np.array([1650, 1700, 1750, 1800])
publications = np.array([200, 450, 1200, 10000])

# 指数成長モデル
def exp_model(t, a, r):
    return a * np.exp(r * t)

t = (years - years[0]) / 50
params, _ = curve_fit(exp_model, t, publications)
a_fit, r_fit = params

growth_factor = publications[-1] / publications[0]
annual_rate = (growth_factor ** (1/150) - 1) * 100

print(f"Growth factor (1650-1800): {growth_factor:.0f}x")
print(f"Annual compound growth rate: {annual_rate:.1f}%")
print(f"Doubling time: {np.log(2)/r_fit*50:.1f} years")

# | 出版の増加 → 読者の増加 → 著者の増加 → 出版の増加

import pandas as pd

terror = pd.DataFrame({
    'Month': ['1793/6', '1793/7', '1793/8', '1793/9', '1793/10',
              '1793/11', '1793/12', '1794/1', '1794/2', '1794/3',
              '1794/4', '1794/5', '1794/7'],
    'Executions': [45, 89, 156, 234, 542, 896, 1245,
                   1456, 1823, 2156, 2589, 1363, 200]
})

terror['Cumulative'] = terror['Executions'].cumsum()

print(f"Total executions: {terror['Executions'].sum():,}")
print(f"Peak month: {terror.loc[terror['Executions'].idxmax(), 'Month']}")
print(f"Peak executions: {terror['Executions'].max():,}")

import numpy as np

categories = ['信仰の権威', '理性の権威', '社会的凝集',
              '意味の確実性', '個人の自由', '進歩への信念']

medieval = [90, 20, 80, 85, 15, 10]
enlightenment = [30, 85, 40, 45, 70, 90]
modern = [20, 90, 30, 25, 85, 60]

angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
medieval += medieval[:1]
enlightenment += enlightenment[:1]
modern += modern[:1]
angles += angles[:1]
