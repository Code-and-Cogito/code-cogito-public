# Code & Cogito: 宗教改革 vs 去中心化運動
# Article: https://code-cogito.com/thought-revolution-03/
# All the code blocks of the article, in order. Program output is kept as comments.

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# === 定義四個體系的階層結構 ===
systems = {
    "天主教會": {
        "layers": ["教宗", "樞機主教", "主教", "神父", "平信徒"],
        "population": [1, 70, 500, 250000, 70000000],
        "color": "#8B0000"
    },
    "新教教會": {
        "layers": ["牧師", "會眾"],
        "population": [50000, 20000000],
        "color": "#2E8B57"
    },
    "傳統金融": {
        "layers": ["中央銀行", "商業銀行", "用戶"],
        "population": [1, 5000, 50000000],
        "color": "#4169E1"
    },
    "加密貨幣": {
        "layers": ["節點/用戶"],
        "population": [100000000],
        "color": "#FF8C00"
    }
}

fig, axes = plt.subplots(1, 4, figsize=(18, 8))
fig.suptitle("Hierarchy Collapse: Centralization → Decentralization",
             fontsize=16, fontweight='bold', y=0.98)

for idx, (name, data) in enumerate(systems.items()):
    ax = axes[idx]
    n = len(data["layers"])

    # 繪製金字塔：每層的寬度代表人數（對數比例）
    max_log = np.log10(max(data["population"]))

    for i, (layer, pop) in enumerate(zip(data["layers"], data["population"])):
        width = (np.log10(pop) + 1) / (max_log + 1)
        y_pos = n - i - 1
        rect = mpatches.FancyBboxPatch(
            (0.5 - width/2, y_pos * 0.8), width, 0.6,
            boxstyle="round,pad=0.05",
            facecolor=data["color"], alpha=0.3 + 0.5*(i/(max(n-1,1))),
            edgecolor=data["color"], linewidth=2
        )
        ax.add_patch(rect)
        label = f"{layer}\n({pop:,})"
        ax.text(0.5, y_pos * 0.8 + 0.3, label,
                ha='center', va='center', fontsize=8, fontweight='bold')

    # 計算去中心化指數 (1/層數)
    decentralization = 1.0 / n
    ax.set_title(f"{name}\n層數={n} | 去中心化={decentralization:.0%}",
                 fontsize=11, fontweight='bold')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.3, n * 0.8 + 0.2)
    ax.axis('off')

plt.tight_layout()
plt.savefig("model1_hierarchy_collapse.png", dpi=150, bbox_inches='tight')
plt.show()

# === 輸出統計摘要 ===
print("\n=== 去中心化程度比較 ===")
print(f"{'系統':<12} {'階層數':<8} {'去中心化指數':<12} {'頂底比例'}")
print("-" * 55)
for name, data in systems.items():
    n = len(data["layers"])
    ratio = data["population"][-1] / data["population"][0]
    print(f"{name:<12} {n:<8} {1/n:<12.0%} 1:{ratio:,.0f}")

# | === 去中心化程度比較 ===
# | 系統          階層數    去中心化指數    頂底比例
# | -------------------------------------------------------
# | 天主教會      5        20%          1:70,000,000
# | 新教教會      2        50%          1:400
# | 傳統金融      3        33%          1:50,000,000
# | 加密貨幣      1        100%         1:1

# | 天主教 → 路德宗 → 加爾文宗 → 長老宗 → 浸信會 → ...
# | 比特幣 → 萊特幣 ／ 比特幣現金 → BSV　｜　以太坊 → ETC　｜　…（多條分支，不是單一路徑）
