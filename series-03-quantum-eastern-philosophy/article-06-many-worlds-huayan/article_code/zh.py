# Code & Cogito: 多世界詮釋 vs 華嚴宗「重重無盡」——無限的平行宇宙
# Article: https://code-cogito.com/many-worlds-interpretation-huayan/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class MultiverseSimulator:
    """
    多世界宇宙分裂模擬器
    展示：每次測量如何導致宇宙分裂
    """

    def __init__(self):
        self.worlds = []

    def initialize(self):
        """初始化：只有一個世界"""
        self.worlds = [{'id': 0, 'history': [], 'amplitude': 1.0}]

    def quantum_measurement(self, n_outcomes=2):
        """
        量子測量
        n_outcomes: 可能結果的數量（通常是2）
        """
        new_worlds = []

        for world in self.worlds:
            # 每個世界分裂成n_outcomes個新世界
            for outcome in range(n_outcomes):
                new_world = {
                    'id': len(new_worlds),
                    'history': world['history'] + [outcome],
                    'amplitude': world['amplitude'] / np.sqrt(n_outcomes)
                }
                new_worlds.append(new_world)

        self.worlds = new_worlds
        return len(self.worlds)

    def visualize_branching(self, n_measurements=5):
        """
        視覺化宇宙分裂樹
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

        # === 左圖：樹狀圖 ===
        self.initialize()

        # 記錄每一步的世界數
        steps = [0]
        world_counts = [1]

        # 計算位置
        max_level = n_measurements
        level_positions = {}  # {level: [world_ids]}

        for level in range(max_level + 1):
            level_positions[level] = []

        # 初始世界
        level_positions[0] = [0]

        # 繪製初始世界
        ax1.scatter([0], [0], s=300, c='green', zorder=5,
                   edgecolors='black', linewidth=2)
        ax1.text(0, -0.3, '初始\n宇宙', ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # 逐步測量
        for measurement in range(1, n_measurements + 1):
            n_worlds = self.quantum_measurement(n_outcomes=2)
            steps.append(measurement)
            world_counts.append(n_worlds)

            # 計算這一層的位置
            n_worlds_this_level = 2 ** measurement
            y_positions = np.linspace(-n_worlds_this_level/4,
                                     n_worlds_this_level/4,
                                     n_worlds_this_level)

            # 繪製連接線和節點
            prev_level_size = 2 ** (measurement - 1)
            prev_y_positions = np.linspace(-prev_level_size/4,
                                          prev_level_size/4,
                                          prev_level_size)

            for i in range(n_worlds_this_level):
                parent_idx = i // 2
                ax1.plot([measurement-1, measurement],
                        [prev_y_positions[parent_idx], y_positions[i]],
                        'b-', alpha=0.3, linewidth=1)
                color = 'red' if i % 2 == 0 else 'blue'
                ax1.scatter([measurement], [y_positions[i]],
                           s=100, c=color, zorder=5, alpha=0.6,
                           edgecolors='black', linewidth=0.5)

        ax1.set_xlabel('測量次數', fontsize=13)
        ax1.set_ylabel('世界分支', fontsize=13)
        ax1.set_title(f'多世界宇宙分裂樹\n{n_measurements}次測量 → {2**n_measurements}個世界',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.2)
        ax1.set_xlim(-0.5, n_measurements + 0.5)

        red_patch = mpatches.Patch(color='red', label='結果0（例如：貓死）', alpha=0.6)
        blue_patch = mpatches.Patch(color='blue', label='結果1（例如：貓活）', alpha=0.6)
        ax1.legend(handles=[red_patch, blue_patch], fontsize=10)

        # === 右圖：世界數量增長 ===
        ax2.plot(steps, world_counts, 'ro-', linewidth=3, markersize=10, label='實際世界數')
        ax2.fill_between(steps, 0, world_counts, alpha=0.3, color='red')

        theory_counts = [2**i for i in steps]
        ax2.plot(steps, theory_counts, 'b--', linewidth=2, label='理論：2^n', alpha=0.7)

        ax2.set_xlabel('測量次數 n', fontsize=13)
        ax2.set_ylabel('世界數量', fontsize=13)
        ax2.set_title('世界數量指數增長\n多世界本體論爆炸',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.set_yscale('log')

        for step, count in zip(steps[::2], world_counts[::2]):
            ax2.text(step, count * 1.5, f'{count}個世界',
                    ha='center', fontsize=9,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.savefig('multiverse_branching.png', dpi=300, bbox_inches='tight')
        plt.show()

        # 數據輸出
        print("\n" + "="*70)
        print("【多世界宇宙分裂】")
        print("="*70)
        print(f"\n初始：1個宇宙")
        print(f"測量1次：{2**1}個世界（宇宙分裂成2個）")
        print(f"測量2次：{2**2}個世界")
        print(f"測量3次：{2**3}個世界")
        print(f"測量4次：{2**4}個世界")
        print(f"測量5次：{2**5}個世界")
        print(f"\n測量n次：2^n 個世界")
        print(f"\n例子：")
        print(f"  * 測量10次 = {2**10:,}個世界")
        print(f"  * 測量20次 = {2**20:,}個世界")
        print(f"  * 測量30次 = {2**30:,}個世界")
        print(f"  * 測量100次 = {2**100:.2e}個世界")
        print(f"\n宇宙每秒發生約10^50次量子事件...")
        print(f"世界數量：無法想像的龐大！")
        print("="*70)

    def compare_interpretations(self):
        """
        比較不同詮釋對測量的看法
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # === 哥本哈根詮釋 ===
        ax = axes[0, 0]
        ax.text(0.5, 0.7, '哥本哈根詮釋', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, '疊加態\n|ψ⟩', ha='center', va='center', fontsize=11)

        ax.annotate('', xy=(0.7, 0.6), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red'))
        ax.text(0.6, 0.65, '測量\n坍縮', ha='center', fontsize=10, color='red')

        circle2 = plt.Circle((0.7, 0.6), 0.1, color='red', alpha=0.7)
        ax.add_patch(circle2)
        ax.text(0.7, 0.6, '|0⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.text(0.7, 0.3, '或', ha='center', fontsize=12, fontweight='bold')

        circle3 = plt.Circle((0.7, 0.2), 0.1, color='blue', alpha=0.7)
        ax.add_patch(circle3)
        ax.text(0.7, 0.2, '|1⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.text(0.5, 0.05, '波函數坍縮\n只有一個結果', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === 多世界詮釋 ===
        ax = axes[0, 1]
        ax.text(0.5, 0.7, '多世界詮釋', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, '疊加態\n|ψ⟩', ha='center', va='center', fontsize=11)

        ax.annotate('', xy=(0.7, 0.6), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.annotate('', xy=(0.7, 0.2), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.text(0.6, 0.4, '宇宙\n分裂', ha='center', fontsize=10, color='green')

        circle2 = plt.Circle((0.7, 0.6), 0.1, color='red', alpha=0.7)
        ax.add_patch(circle2)
        ax.text(0.7, 0.6, '|0⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')
        ax.text(0.85, 0.6, '世界A', ha='left', fontsize=9)

        circle3 = plt.Circle((0.7, 0.2), 0.1, color='blue', alpha=0.7)
        ax.add_patch(circle3)
        ax.text(0.7, 0.2, '|1⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')
        ax.text(0.85, 0.2, '世界B', ha='left', fontsize=9)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.text(0.5, 0.05, '波函數不坍縮\n所有結果都發生', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === 華嚴宗 ===
        ax = axes[1, 0]
        ax.text(0.5, 0.9, '華嚴宗：重重無盡', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle_center = plt.Circle((0.5, 0.5), 0.08, color='gold', alpha=0.8,
                                  edgecolor='black', linewidth=2)
        ax.add_patch(circle_center)
        ax.text(0.5, 0.5, '一塵', ha='center', va='center', fontsize=10,
               fontweight='bold')

        n_worlds = 12
        angles = np.linspace(0, 2*np.pi, n_worlds, endpoint=False)
        for i, angle in enumerate(angles):
            x = 0.5 + 0.3 * np.cos(angle)
            y = 0.5 + 0.3 * np.sin(angle)
            circle = plt.Circle((x, y), 0.05, color='lightblue', alpha=0.6,
                               edgecolor='blue', linewidth=1)
            ax.add_patch(circle)
            ax.text(x, y, f'剎{i+1}', ha='center', va='center', fontsize=7)
            ax.plot([0.5, x], [0.5, y], 'gray', alpha=0.3, linewidth=1)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.text(0.5, 0.05, '一塵含塵數剎\n剎剎相含', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === 對比總結 ===
        ax = axes[1, 1]
        ax.axis('off')

        comparison_text = '''
        【哥本哈根 vs 多世界 vs 華嚴】

        哥本哈根詮釋：
        * 波函數坍縮
        * 只有一個結果
        * 機率：本質不確定

        多世界詮釋：
        * 波函數不坍縮
        * 所有結果都發生（不同世界）
        * 機率：測量後「我」在哪個世界

        華嚴宗：
        * 一切法同時存在
        * 重重無盡的法界
        * 「我」見：依業力所見

        共同點：
        - 多種「實在」並存
        - 觀察者相對性
        - 無限的可能性
        '''

        ax.text(0.1, 0.5, comparison_text, fontsize=11, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                        edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('interpretations_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()

# 執行
simulator = MultiverseSimulator()
simulator.visualize_branching(n_measurements=5)
simulator.compare_interpretations()

# | class QuantumBiography:
# |     """
# |     量子自傳：「我」在多少個世界裡
# |     """
# | 
# |     def __init__(self):
# |         self.decisions = []
# | 
# |     def add_decision(self, description, n_choices=2):
# |         """
# |         添加一個人生決定
# |         description: 決定的描述
# |         n_choices: 選擇數量
# |         """
# |         self.decisions.append({
# |             'description': description,
# |             'n_choices': n_choices
# |         })
# | 
# |     def calculate_parallel_lives(self):
# |         """
# |         計算平行生命數量
# |         """
# |         total_worlds = 1
# |         for decision in self.decisions:
# |             total_worlds *= decision['n_choices']
# |         return total_worlds

    def visualize_life_tree(self):
        """
        視覺化人生決策樹
        """
        # 示例決策
        self.decisions = [
            {'description': '今天早餐吃什麼？', 'n_choices': 3},
            {'description': '大學選什麼專業？', 'n_choices': 5},
            {'description': '接受這份工作嗎？', 'n_choices': 2},
            {'description': '向TA告白嗎？', 'n_choices': 2},
            {'description': '搬到新城市嗎？', 'n_choices': 2},
        ]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === 左圖：決策樹 ===
        cumulative_worlds = [1]
        for i, decision in enumerate(self.decisions):
            cumulative_worlds.append(cumulative_worlds[-1] * decision['n_choices'])

        for level, n_worlds in enumerate(cumulative_worlds):
            if level < 4:  # 只畫前幾層，避免太密
                y_positions = np.linspace(-n_worlds/10, n_worlds/10,
                                         min(n_worlds, 20))

                for y in y_positions[:min(n_worlds, 20)]:
                    ax1.scatter([level], [y], s=50, c='blue', alpha=0.5,
                              edgecolors='black', linewidth=0.5)

                if level > 0:
                    prev_n_worlds = cumulative_worlds[level-1]
                    prev_y_positions = np.linspace(-prev_n_worlds/10,
                                                   prev_n_worlds/10,
                                                   min(prev_n_worlds, 20))

                    for prev_y in prev_y_positions[:min(prev_n_worlds, 20)]:
                        for y in y_positions[:min(n_worlds, 20)]:
                            if abs(y - prev_y) < n_worlds/5:
                                ax1.plot([level-1, level], [prev_y, y],
                                       'gray', alpha=0.1, linewidth=0.5)

        ax1.set_xlabel('人生決策點', fontsize=13)
        ax1.set_ylabel('平行生命分支', fontsize=13)
        ax1.set_title('你的平行生命樹\n每個決定創造新的你',
                     fontsize=14, fontweight='bold')
        ax1.set_xticks(range(len(self.decisions) + 1))
        ax1.set_xticklabels(['出生'] + [d['description'][:8]+'...'
                                       for d in self.decisions],
                           rotation=45, ha='right', fontsize=9)
        ax1.grid(True, alpha=0.2)

        # === 右圖：平行生命數量 ===
        decision_labels = ['出生'] + [f"決定{i+1}" for i in range(len(self.decisions))]

        ax2.bar(range(len(cumulative_worlds)), cumulative_worlds,
               color='purple', alpha=0.7, edgecolor='black', linewidth=1.5)

        ax2.set_xlabel('人生階段', fontsize=13)
        ax2.set_ylabel('平行生命數量', fontsize=13)
        ax2.set_title('你存在於多少個世界？', fontsize=14, fontweight='bold')
        ax2.set_yscale('log')
        ax2.set_xticks(range(len(cumulative_worlds)))
        ax2.set_xticklabels(decision_labels, rotation=45, ha='right', fontsize=10)
        ax2.grid(True, alpha=0.3, axis='y')

        for i, n_worlds in enumerate(cumulative_worlds):
            ax2.text(i, n_worlds * 1.5, f'{n_worlds:,}',
                    ha='center', fontsize=9,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.savefig('quantum_biography.png', dpi=300, bbox_inches='tight')
        plt.show()

        # 統計
        total = self.calculate_parallel_lives()

        print("\n" + "="*70)
        print("【你的平行生命】")
        print("="*70)
        print("\n示例決策：")
        for i, decision in enumerate(self.decisions, 1):
            print(f"  {i}. {decision['description']} ({decision['n_choices']}個選擇)")

        print(f"\n結果：")
        print(f"  * 這些決策創造了 {total:,} 個平行的「你」")
        print(f"  * 每個「你」有不同的人生軌跡")
        print(f"  * 每個「你」都覺得自己是「唯一」的")

        print(f"\n現實中：")
        print(f"  * 你每天做約 35,000 個決定")
        print(f"  * 每個決定平均有 2-3 個選擇")
        print(f"  * 一天：約 2^35000 個世界")
        print(f"  * 一生：無法計算的天文數字！")

        print(f"\n哲學問題：")
        print(f"  * 哪個「你」是「真正的你」？")
        print(f"  * 其他世界的「你」也這樣想嗎？")
        print(f"  * 「我」的獨特性在哪裡？")

        print(f"\n華嚴宗的答案：")
        print(f"  * 所有的「你」都是真的")
        print(f"  * 「我」本來就不是單一的")
        print(f"  * 「一即一切」：每個我包含一切我")
        print("="*70)

# 執行
biography = QuantumBiography()
biography.visualize_life_tree()

def visualize_huayan_fractals():
    """
    華嚴宗「一塵含十方」的分形視覺化
    展示：無限遞迴的結構
    """

    fig = plt.figure(figsize=(18, 12))

    # === 圖1：Mandelbrot集（分形的經典例子）===
    ax1 = fig.add_subplot(2, 2, 1)

    def mandelbrot(c, max_iter=100):
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter

    width, height = 800, 800
    xmin, xmax = -2.5, 1.0
    ymin, ymax = -1.25, 1.25

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y

    mandelbrot_set = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = mandelbrot(C[i, j], max_iter=50)

    im1 = ax1.imshow(mandelbrot_set, extent=[xmin, xmax, ymin, ymax],
                    cmap='hot', interpolation='bilinear', origin='lower')
    ax1.set_title('Mandelbrot集：無限細節\n放大任何區域，都看到相似結構',
                 fontsize=13, fontweight='bold')
    ax1.set_xlabel('實部')
    ax1.set_ylabel('虛部')
    plt.colorbar(im1, ax=ax1, label='迭代次數')

    # === 圖2：Sierpinski三角形（遞迴結構）===
    ax2 = fig.add_subplot(2, 2, 2)

    def sierpinski(ax, order, points):
        """繪製Sierpinski三角形"""
        if order == 0:
            triangle = plt.Polygon(points, fill=True,
                                  facecolor='blue', edgecolor='black',
                                  linewidth=0.5, alpha=0.6)
            ax.add_patch(triangle)
        else:
            p1, p2, p3 = points
            m12 = (p1 + p2) / 2
            m23 = (p2 + p3) / 2
            m31 = (p3 + p1) / 2
            sierpinski(ax, order-1, np.array([p1, m12, m31]))
            sierpinski(ax, order-1, np.array([m12, p2, m23]))
            sierpinski(ax, order-1, np.array([m31, m23, p3]))

    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3)/2])

    sierpinski(ax2, order=5, points=np.array([p1, p2, p3]))

    ax2.set_xlim(-0.1, 1.1)
    ax2.set_ylim(-0.1, 1.0)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Sierpinski三角形：自相似\n每個小三角形包含整體結構',
                 fontsize=13, fontweight='bold')

    # === 圖3：華嚴宗結構圖 ===
    ax3 = fig.add_subplot(2, 2, 3)

    circle_center = plt.Circle((0.5, 0.5), 0.1, color='gold', alpha=0.9,
                              edgecolor='black', linewidth=3)
    ax3.add_patch(circle_center)
    ax3.text(0.5, 0.5, '一塵', ha='center', va='center', fontsize=14,
            fontweight='bold')

    n_layer1 = 6
    angles1 = np.linspace(0, 2*np.pi, n_layer1, endpoint=False)
    layer1_radius = 0.25

    for angle in angles1:
        x = 0.5 + layer1_radius * np.cos(angle)
        y = 0.5 + layer1_radius * np.sin(angle)

        circle = plt.Circle((x, y), 0.06, color='lightblue', alpha=0.7,
                           edgecolor='blue', linewidth=2)
        ax3.add_patch(circle)
        ax3.text(x, y, '剎', ha='center', va='center', fontsize=10)
        ax3.plot([0.5, x], [0.5, y], 'gray', alpha=0.5, linewidth=2)

        n_layer2 = 4
        angles2 = np.linspace(0, 2*np.pi, n_layer2, endpoint=False)
        layer2_radius = 0.03

        for angle2 in angles2:
            x2 = x + layer2_radius * np.cos(angle2)
            y2 = y + layer2_radius * np.sin(angle2)

            circle2 = plt.Circle((x2, y2), 0.015, color='lightgreen',
                                alpha=0.5, edgecolor='green', linewidth=0.5)
            ax3.add_patch(circle2)
            ax3.plot([x, x2], [y, y2], 'green', alpha=0.3, linewidth=0.5)

    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('華嚴宗：一塵含塵數剎\n剎剎相含，重重無盡',
                 fontsize=13, fontweight='bold')

    ax3.text(0.5, 0.05, '「一塵中有塵數剎，一一剎有難思佛」\n無限遞迴',
            ha='center', fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === 圖4：對應說明 ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    【分形 vs 華嚴「重重無盡」】

    數學分形：
    * 自相似性
    * 無限細節
    * 部分包含整體
    * 放大後看到相同結構

    華嚴宗「重重無盡」：
    * 一塵含十方
    * 剎剎相含
    * 微細相容
    * 無限遞迴

    共同結構：
    - 無限嵌套
    - 部分=整體
    - 每個層次都完整
    - 無窮無盡

    多世界詮釋：
    * 宇宙不斷分裂
    * 每個世界又分裂
    * 分支樹無限增長
    * 指數級爆炸

    三者的共同洞見：
    「無限」不是「很大」
    而是結構本身的性質
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center',
            family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                     edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('huayan_fractals.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【華嚴宗的分形結構】")
    print("="*70)
    print("\n數學類比：")
    print("  * 分形：自相似，無限細節")
    print("  * Mandelbrot集：放大任何區域都看到相似結構")
    print("  * Sierpinski三角形：每個小三角形=整體")
    print("\n深刻洞見：")
    print("  「無限」不是數量概念")
    print("  而是結構本身的性質")
    print("  部分即整體，整體即部分")
    print("="*70)

# 執行
visualize_huayan_fractals()

def visualize_time_multiverse():
    """
    時間的多世界
    展示：過去、現在、未來如何互相包含
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

    # === 左圖：量子力學的時間分支 ===
    times = np.array([0, 1, 2, 3, 4])

    ax1.scatter([0], [0], s=500, c='green', zorder=5,
               edgecolors='black', linewidth=3)
    ax1.text(0, -0.5, 't=0\n初始', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # t=1: 分裂成2個
    y1 = [-1, 1]
    for y in y1:
        ax1.scatter([1], [y], s=300, c='blue', zorder=5,
                   edgecolors='black', linewidth=2, alpha=0.7)
        ax1.plot([0, 1], [0, y], 'b-', alpha=0.5, linewidth=2)

    # t=2: 每個再分裂成2個
    y2 = [-1.5, -0.5, 0.5, 1.5]
    for i, y in enumerate(y2):
        parent_y = y1[i//2]
        ax1.scatter([2], [y], s=200, c='red', zorder=5,
                   edgecolors='black', linewidth=1.5, alpha=0.6)
        ax1.plot([1, 2], [parent_y, y], 'r-', alpha=0.4, linewidth=1.5)

    # t=3: 繼續分裂
    y3 = np.linspace(-2, 2, 8)
    for i, y in enumerate(y3):
        parent_y = y2[i//2]
        ax1.scatter([3], [y], s=100, c='purple', zorder=5,
                   edgecolors='black', linewidth=1, alpha=0.5)
        ax1.plot([2, 3], [parent_y, y], 'purple', alpha=0.3, linewidth=1)

    # t=4: 更多分裂
    y4 = np.linspace(-2.5, 2.5, 16)
    for i, y in enumerate(y4):
        parent_y = y3[i//2]
        ax1.scatter([4], [y], s=50, c='orange', zorder=5,
                   edgecolors='black', linewidth=0.5, alpha=0.4)
        ax1.plot([3, 4], [parent_y, y], 'orange', alpha=0.2, linewidth=0.5)

    ax1.set_xlabel('時間', fontsize=13)
    ax1.set_ylabel('世界分支', fontsize=13)
    ax1.set_title('量子多世界：時間向未來分裂\n過去唯一，未來多元',
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.2)
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-3, 3)

    ax1.text(2, 2.5, f't=2: {4}個世界', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))
    ax1.text(4, 2.8, f't=4: {16}個世界', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    # === 右圖：華嚴宗的十世 ===
    past_center = np.array([0.2, 0.5])
    present_center = np.array([0.5, 0.5])
    future_center = np.array([0.8, 0.5])

    circle_past = plt.Circle(past_center, 0.15, color='blue', alpha=0.3,
                            edgecolor='blue', linewidth=3)
    ax2.add_patch(circle_past)
    ax2.text(past_center[0], past_center[1], '過去',
            ha='center', va='center', fontsize=14, fontweight='bold')

    circle_present = plt.Circle(present_center, 0.15, color='green', alpha=0.3,
                               edgecolor='green', linewidth=3)
    ax2.add_patch(circle_present)
    ax2.text(present_center[0], present_center[1], '現在',
            ha='center', va='center', fontsize=14, fontweight='bold')

    circle_future = plt.Circle(future_center, 0.15, color='red', alpha=0.3,
                              edgecolor='red', linewidth=3)
    ax2.add_patch(circle_future)
    ax2.text(future_center[0], future_center[1], '未來',
            ha='center', va='center', fontsize=14, fontweight='bold')

    connections = [
        (past_center, present_center),
        (present_center, future_center),
        (past_center, future_center),
        (present_center, past_center),
        (future_center, present_center),
        (future_center, past_center),
    ]

    for start, end in connections:
        ax2.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', lw=2, alpha=0.4,
                                  color='gray', connectionstyle="arc3,rad=.3"))

    positions_text = [
        (0.1, 0.8, '過去\n過去'),
        (0.1, 0.5, '過去\n現在'),
        (0.1, 0.2, '過去\n未來'),
        (0.5, 0.8, '現在\n過去'),
        (0.5, 0.2, '現在\n未來'),
        (0.9, 0.8, '未來\n過去'),
        (0.9, 0.5, '未來\n現在'),
        (0.9, 0.2, '未來\n未來'),
    ]

    for x, y, label in positions_text:
        circle_small = plt.Circle((x, y), 0.06, color='yellow', alpha=0.5,
                                 edgecolor='orange', linewidth=1)
        ax2.add_patch(circle_small)
        ax2.text(x, y, label, ha='center', va='center', fontsize=7)

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('華嚴宗「十世」：時間互相包含\n過去含未來，未來含過去',
                 fontsize=14, fontweight='bold')

    ax2.text(0.5, 0.05, '「十世隔法異成門」\n一念含三世，三世互攝',
            ha='center', fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('time_multiverse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【時間的多世界】")
    print("="*70)

    print("\n量子力學多世界：")
    print("  * 時間向未來分裂")
    print("  * 過去：唯一")
    print("  * 未來：多元（指數增長）")
    print("  * 時間是單向的")

    print("\n華嚴宗「十世」：")
    print("  1. 過去過去世")
    print("  2. 過去現在世")
    print("  3. 過去未來世")
    print("  4. 現在過去世")
    print("  5. 現在現在世")
    print("  6. 現在未來世")
    print("  7. 未來過去世")
    print("  8. 未來現在世")
    print("  9. 未來未來世")
    print("  10. 三世各別總攝為一世")

    print("\n對比：")
    print("  量子：時間向前，分支增加")
    print("  華嚴：時間無向，互相包含")
    print("="*70)

# 執行
visualize_time_multiverse()
