"""
佛羅倫斯網絡分析（基礎版）
分析15世紀義大利8個主要城市的貿易網絡

文章：佛羅倫斯為何成為文藝復興搖籃？
作者：Wina
系列：文藝復興的數位重生 #1/12
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("佛羅倫斯網絡分析：15世紀義大利城市網絡")
print("=" * 60)

# ===== 城市數據 =====

# 8個主要城市（人口為1400年左右估計值）
cities = {
    'Florence': {'population': 60000, 'lat': 43.77, 'lon': 11.25},
    'Venice': {'population': 100000, 'lat': 45.44, 'lon': 12.32},
    'Milan': {'population': 80000, 'lat': 45.46, 'lon': 9.19},
    'Rome': {'population': 50000, 'lat': 41.90, 'lon': 12.49},
    'Genoa': {'population': 60000, 'lat': 44.41, 'lon': 8.93},
    'Naples': {'population': 40000, 'lat': 40.84, 'lon': 14.25},
    'Bologna': {'population': 30000, 'lat': 44.49, 'lon': 11.34},
    'Siena': {'population': 20000, 'lat': 43.32, 'lon': 11.33}
}

# 主要貿易路線（權重=相對貿易量，1-10分）
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

# ===== 建立網絡 =====

G = nx.Graph()

# 添加節點
for city, attrs in cities.items():
    G.add_node(city, **attrs)

# 添加邊
G.add_weighted_edges_from(trade_routes)

# ===== 網絡分析 =====

print("\n[網絡基本資訊]")
print(f"節點數（城市）: {G.number_of_nodes()}")
print(f"邊數（貿易路線）: {G.number_of_edges()}")
print(f"網絡密度: {nx.density(G):.3f}")

# 計算中介中心性（Betweenness Centrality）
betweenness_centrality = nx.betweenness_centrality(G)

print("\n[中介中心性 (Betweenness Centrality)]")
print("衡量：一個城市在多少條最短路徑上（樞紐地位）\n")
print(f"{'城市':<12} {'中介中心性':<15}")
print("-" * 30)

for city in sorted(betweenness_centrality, 
                   key=betweenness_centrality.get, 
                   reverse=True):
    print(f"{city:<12} {betweenness_centrality[city]:<15.3f}")

# 比較主要城市
print("\n[佛羅倫斯 vs 主要競爭對手]")
print("-" * 50)
comparison = ['Florence', 'Venice', 'Milan', 'Rome']
print(f"{'城市':<12} {'中介中心性':<15} {'人口':<10}")
print("-" * 50)

for city in comparison:
    print(f"{city:<12} {betweenness_centrality[city]:<15.3f} {cities[city]['population']:<10,}")

# 計算優勢倍數
florence_bc = betweenness_centrality['Florence']
venice_bc = betweenness_centrality['Venice']
milan_bc = betweenness_centrality['Milan']
rome_bc = betweenness_centrality['Rome']

print(f"\n【關鍵發現】")
print(f"佛羅倫斯的中介中心性:")
print(f"  • 是威尼斯的 {florence_bc/venice_bc:.2f} 倍")
print(f"  • 是米蘭的 {florence_bc/milan_bc:.2f} 倍")
print(f"  • 是羅馬的 {florence_bc/rome_bc:.2f} 倍")
print(f"\n→ 更多資訊、資金、人才流經佛羅倫斯")
print(f"→ 佛羅倫斯是15世紀義大利的網絡中心")

# ===== 視覺化 =====

plt.figure(figsize=(12, 9))

# 使用spring layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# 節點大小根據人口
node_sizes = [cities[city]['population']/80 for city in G.nodes()]

# 節點顏色根據中介中心性
node_colors = [betweenness_centrality[city] for city in G.nodes()]

# 繪製網絡
nx.draw_networkx_nodes(G, pos,
                       node_size=node_sizes,
                       node_color=node_colors,
                       cmap='YlOrRd',
                       alpha=0.9,
                       edgecolors='black',
                       linewidths=2)

# 繪製邊
edge_widths = [G[u][v]['weight']/2 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos,
                       width=edge_widths,
                       alpha=0.5,
                       edge_color='gray')

# 標籤
nx.draw_networkx_labels(G, pos,
                        font_size=11,
                        font_weight='bold')

plt.title('15世紀義大利城市貿易網絡（簡化版）\n節點大小=人口，顏色=中介中心性', 
         fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# 儲存圖片
plt.savefig('florence_network_basic.png', dpi=300, bbox_inches='tight')
print("\n✓ 視覺化完成：florence_network_basic.png")
print("✓ 佛羅倫斯是15世紀義大利的網絡中心")

plt.show()

print("\n" + "=" * 60)
print("分析完成！")
print("=" * 60)
