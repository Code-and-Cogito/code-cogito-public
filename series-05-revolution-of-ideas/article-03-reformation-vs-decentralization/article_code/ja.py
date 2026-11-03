# Code & Cogito: 宗教改革 vs 脱中央集権運動
# Article: https://code-cogito.com/ja/thought-revolution-03-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# === 四つの体制の階層構造を定義 ===
systems = {
    "Catholic Church": {
        "layers": ["Pope", "Cardinals", "Bishops", "Priests", "Laity"],
        "population": [1, 70, 500, 250000, 70000000],
        "color": "#8B0000"
    },
    "Protestant Church": {
        "layers": ["Pastors", "Congregation"],
        "population": [50000, 20000000],
        "color": "#2E8B57"
    },
    "Traditional Finance": {
        "layers": ["Central Bank", "Commercial Banks", "Users"],
        "population": [1, 5000, 50000000],
        "color": "#4169E1"
    },
    "Cryptocurrency": {
        "layers": ["Nodes/Users"],
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

    # ピラミッドを描画：幅は人数を表す（対数スケール）
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

    # 脱中央集権指数を計算（1/層数）
    decentralization = 1.0 / n
    ax.set_title(f"{name}\nLayers={n} | Decentralization={decentralization:.0%}",
                 fontsize=11, fontweight='bold')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.3, n * 0.8 + 0.2)
    ax.axis('off')

plt.tight_layout()
plt.savefig("model1_hierarchy_collapse.png", dpi=150, bbox_inches='tight')
plt.show()

# === 統計サマリーを出力 ===
print("\n=== 脱中央集権度の比較 ===")
print(f"{'System':<22} {'Layers':<8} {'Decentralization':<18} {'Top-to-Bottom Ratio'}")
print("-" * 70)
for name, data in systems.items():
    n = len(data["layers"])
    ratio = data["population"][-1] / data["population"][0]
    print(f"{name:<22} {n:<8} {1/n:<18.0%} 1:{ratio:,.0f}")

# | === 脱中央集権度の比較 ===
# | System                 Layers   Decentralization   Top-to-Bottom Ratio
# | ----------------------------------------------------------------------
# | Catholic Church        5        20%                1:70,000,000
# | Protestant Church      2        50%                1:400
# | Traditional Finance    3        33%                1:50,000,000
# | Cryptocurrency         1        100%               1:1

# | カトリック → ルター派 → カルヴァン派 → 長老派 → バプテスト派 → ...
# | ビットコイン → ライトコイン ／ ビットコイン・キャッシュ → BSV　｜　イーサリアム → ETC　｜　…（単一の系統ではなく複数の枝）
