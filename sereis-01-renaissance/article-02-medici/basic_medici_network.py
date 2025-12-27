"""
美第奇銀行網絡分析（基礎版）
分析1397-1494年美第奇銀行的歐洲分行網絡

文章：美第奇家族的金融帝國
作者：Wina
系列：文藝復興的數位重生 #2/12
"""

import networkx as nx
import matplotlib.pyplot as plt

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("美第奇銀行網絡分析：1397-1494")
print("=" * 60)

# ===== 美第奇銀行分行資料 =====

branches = {
    'Florence': {
        'pos': (11.25, 43.77),
        'opened': 1397,
        'closed': 1494,
        'revenue': 100000,  # 佛羅林/年
        'type': 'headquarters'
    },
    'Rome': {
        'pos': (12.49, 41.90),
        'opened': 1397,
        'closed': 1478,
        'revenue': 80000,  # 教宗銀行，第二高
        'type': 'branch'
    },
    'Venice': {
        'pos': (12.32, 45.44),
        'opened': 1402,
        'closed': 1469,
        'revenue': 50000,
        'type': 'branch'
    },
    'Geneva': {
        'pos': (6.14, 46.20),
        'opened': 1424,
        'closed': 1478,
        'revenue': 45000,
        'type': 'branch'
    },
    'Bruges': {
        'pos': (3.22, 51.21),
        'opened': 1439,
        'closed': 1480,
        'revenue': 40000,
        'type': 'branch'
    },
    'London': {
        'pos': (-0.13, 51.51),
        'opened': 1446,
        'closed': 1478,
        'revenue': 35000,
        'type': 'branch'
    },
    'Avignon': {
        'pos': (4.81, 43.95),
        'opened': 1446,
        'closed': 1478,
        'revenue': 30000,
        'type': 'branch'
    },
    'Milan': {
        'pos': (9.19, 45.46),
        'opened': 1452,
        'closed': 1478,
        'revenue': 25000,
        'type': 'branch'
    }
}

# ===== 建立網絡 =====

G = nx.Graph()

# 添加節點
for city, data in branches.items():
    G.add_node(city, **data)

# 添加邊（總行連接所有分行 - 輪軸式結構）
headquarters = 'Florence'
for city in branches.keys():
    if city != headquarters:
        G.add_edge(headquarters, city, 
                  weight=branches[city]['revenue']/10000)

# ===== 網絡分析 =====

print("\n[美第奇銀行分行營業額排名]")
print(f"{'分行':<15} {'營業額(佛羅林)':<20} {'開設年份':<12} {'關閉年份':<12}")
print("-" * 65)

for city, data in sorted(branches.items(), 
                        key=lambda x: x[1]['revenue'], 
                        reverse=True):
    print(f"{city:<15} {data['revenue']:<20,} {data['opened']:<12} {data['closed']:<12}")

print(f"\n【網絡統計】")
print(f"總分行數: {len(branches)}個")
print(f"營運時間: 1397-1494年（97年）")
print(f"巔峰期（1450-1470）: 8個分行同時營運")
print(f"衰退期（1470-1494）: 分行陸續關閉")

print(f"\n【關鍵發現】")
print(f"• 佛羅倫斯總行營業額: 100,000佛羅林/年")
print(f"• 羅馬分行（教宗銀行）: 80,000佛羅林/年")
total_revenue = sum(b['revenue'] for b in branches.values())
print(f"• 所有分行總營業額: {total_revenue:,}佛羅林/年")
print(f"\n→ 美第奇銀行控制了歐洲金融的關鍵節點")
print(f"→ 輪軸式（hub-and-spoke）網絡結構")

# ===== 視覺化 =====

fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# 使用地理座標
pos = {city: data['pos'] for city, data in branches.items()}

# 節點大小根據營業額
node_sizes = [branches[city]['revenue']/80 for city in G.nodes()]

# 節點顏色：總行vs分行
node_colors = ['#C41E3A' if branches[city]['type'] == 'headquarters' 
               else '#FFD700' for city in G.nodes()]

# 繪製邊
edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw_networkx_edges(G, pos, ax=ax,
                       width=[w/2 for w in weights],
                       alpha=0.4,
                       edge_color='gray')

# 繪製節點
nx.draw_networkx_nodes(G, pos, ax=ax,
                       node_size=node_sizes,
                       node_color=node_colors,
                       alpha=0.9,
                       edgecolors='black',
                       linewidths=2)

# 標籤
nx.draw_networkx_labels(G, pos, ax=ax,
                       font_size=10,
                       font_weight='bold')

ax.set_title('美第奇銀行歐洲分行網絡（1397-1494）\n節點大小=營業額', 
            fontsize=14, fontweight='bold', pad=15)
ax.axis('off')

# 圖例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#C41E3A',
           markersize=12, markeredgecolor='black', markeredgewidth=2,
           label='總行（佛羅倫斯）'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700',
           markersize=12, markeredgecolor='black', markeredgewidth=2,
           label='分行')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

plt.tight_layout()

# 儲存圖片
plt.savefig('medici_bank_network.png', dpi=300, bbox_inches='tight')
print("\n✓ 視覺化完成：medici_bank_network.png")
print("✓ 美第奇銀行的輪軸式網絡清楚可見")

plt.show()

print("\n" + "=" * 60)
print("分析完成！")
print("=" * 60)
