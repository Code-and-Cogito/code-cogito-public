# Code & Cogito: 多世界解釈 vs 華厳宗「重重無尽」——無限の並行宇宙
# Article: https://code-cogito.com/ja/many-worlds-interpretation-huayan-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class MultiverseSimulator:
    """
    Many-worlds universe splitting simulator.
    Demonstrates how each measurement causes the universe to branch.
    """

    def __init__(self):
        self.worlds = []

    def initialize(self):
        """Initialize with a single world"""
        self.worlds = [{'id': 0, 'history': [], 'amplitude': 1.0}]

    def quantum_measurement(self, n_outcomes=2):
        """
        Quantum measurement.
        n_outcomes: number of possible outcomes (usually 2)
        """
        new_worlds = []

        for world in self.worlds:
            # Each world splits into n_outcomes new worlds
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
        Visualize universe branching tree
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

        # === Left panel: Tree diagram ===
        self.initialize()

        # Record world count at each step
        steps = [0]
        world_counts = [1]

        # Compute positions
        max_level = n_measurements
        level_positions = {}  # {level: [world_ids]}

        for level in range(max_level + 1):
            level_positions[level] = []

        # Initial world
        level_positions[0] = [0]

        # Draw initial world
        ax1.scatter([0], [0], s=300, c='green', zorder=5,
                   edgecolors='black', linewidth=2)
        ax1.text(0, -0.3, '初期\n宇宙', ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # Step-by-step measurements
        for measurement in range(1, n_measurements + 1):
            n_worlds = self.quantum_measurement(n_outcomes=2)
            steps.append(measurement)
            world_counts.append(n_worlds)

            # Compute positions at this level
            n_worlds_this_level = 2 ** measurement
            y_positions = np.linspace(-n_worlds_this_level/4,
                                     n_worlds_this_level/4,
                                     n_worlds_this_level)

            # Draw connections and nodes
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

        ax1.set_xlabel('測定回数', fontsize=13)
        ax1.set_ylabel('世界の分岐', fontsize=13)
        ax1.set_title(f'多世界・宇宙分裂樹\n{n_measurements}回の測定 → {2**n_measurements}個の世界',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.2)
        ax1.set_xlim(-0.5, n_measurements + 0.5)

        red_patch = mpatches.Patch(color='red', label='結果0（例：猫が死亡）', alpha=0.6)
        blue_patch = mpatches.Patch(color='blue', label='結果1（例：猫が生存）', alpha=0.6)
        ax1.legend(handles=[red_patch, blue_patch], fontsize=10)

        # === Right panel: World count growth ===
        ax2.plot(steps, world_counts, 'ro-', linewidth=3, markersize=10, label='実際の世界数')
        ax2.fill_between(steps, 0, world_counts, alpha=0.3, color='red')

        theory_counts = [2**i for i in steps]
        ax2.plot(steps, theory_counts, 'b--', linewidth=2, label='理論値：2^n', alpha=0.7)

        ax2.set_xlabel('測定回数 n', fontsize=13)
        ax2.set_ylabel('世界の数', fontsize=13)
        ax2.set_title('世界数の指数的増大\n多世界の存在論的爆発',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.set_yscale('log')

        for step, count in zip(steps[::2], world_counts[::2]):
            ax2.text(step, count * 1.5, f'{count}個の世界',
                    ha='center', fontsize=9,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.savefig('multiverse_branching.png', dpi=300, bbox_inches='tight')
        plt.show()

        # Data output
        print("\n" + "="*70)
        print("【多世界・宇宙の分裂】")
        print("="*70)
        print(f"\n初期：1つの宇宙")
        print(f"測定1回：{2**1}個の世界（宇宙が2つに分裂）")
        print(f"測定2回：{2**2}個の世界")
        print(f"測定3回：{2**3}個の世界")
        print(f"測定4回：{2**4}個の世界")
        print(f"測定5回：{2**5}個の世界")
        print(f"\n測定n回：2^n 個の世界")
        print(f"\n例：")
        print(f"  * 測定10回 = {2**10:,}個の世界")
        print(f"  * 測定20回 = {2**20:,}個の世界")
        print(f"  * 測定30回 = {2**30:,}個の世界")
        print(f"  * 測定100回 = {2**100:.2e}個の世界")
        print(f"\n宇宙では毎秒約10^50回の量子イベントが起きている...")
        print(f"世界の数：想像を絶する膨大さ！")
        print("="*70)

    def compare_interpretations(self):
        """
        Compare different interpretations of measurement
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # === Copenhagen interpretation ===
        ax = axes[0, 0]
        ax.text(0.5, 0.7, 'コペンハーゲン解釈', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, '重ね合わせ\n|ψ⟩', ha='center', va='center', fontsize=11)

        ax.annotate('', xy=(0.7, 0.6), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red'))
        ax.text(0.6, 0.65, '測定\n収縮', ha='center', fontsize=10, color='red')

        circle2 = plt.Circle((0.7, 0.6), 0.1, color='red', alpha=0.7)
        ax.add_patch(circle2)
        ax.text(0.7, 0.6, '|0⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.text(0.7, 0.3, 'または', ha='center', fontsize=12, fontweight='bold')

        circle3 = plt.Circle((0.7, 0.2), 0.1, color='blue', alpha=0.7)
        ax.add_patch(circle3)
        ax.text(0.7, 0.2, '|1⟩', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.text(0.5, 0.05, '波動関数が収縮\n結果は一つだけ', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Many-worlds interpretation ===
        ax = axes[0, 1]
        ax.text(0.5, 0.7, '多世界解釈', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, '重ね合わせ\n|ψ⟩', ha='center', va='center', fontsize=11)

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

        ax.text(0.5, 0.05, '波動関数は収縮しない\n全ての結果が起こる', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Huayan Buddhism ===
        ax = axes[1, 0]
        ax.text(0.5, 0.9, '華厳宗：重重無尽', ha='center', fontsize=16,
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
            ax.text(x, y, f'刹{i+1}', ha='center', va='center', fontsize=7)
            ax.plot([0.5, x], [0.5, y], 'gray', alpha=0.3, linewidth=1)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.text(0.5, 0.05, '一塵に塵数の刹を含む\n刹刹相含', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Comparison summary ===
        ax = axes[1, 1]
        ax.axis('off')

        comparison_text = '''
        【コペンハーゲン vs 多世界 vs 華厳】

        コペンハーゲン解釈：
        * 波動関数が収縮
        * 結果は一つだけ
        * 確率：本質的に不確定

        多世界解釈：
        * 波動関数は収縮しない
        * 全結果が起こる（異なる世界で）
        * 確率：測定後「私」がどの世界にいるか

        華厳宗：
        * 一切法が同時に存在
        * 重重無尽の法界
        * 「我」の見るもの：業力に依る

        共通点：
        - 多種の「実在」が並存
        - 観測者の相対性
        - 無限の可能性
        '''

        ax.text(0.1, 0.5, comparison_text, fontsize=11, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                        edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('interpretations_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()

# Execute
simulator = MultiverseSimulator()
simulator.visualize_branching(n_measurements=5)
simulator.compare_interpretations()

class QuantumBiography:
    """
    Quantum biography: how many worlds does "I" exist in?
    """

    def __init__(self):
        self.decisions = []

    def add_decision(self, description, n_choices=2):
        """
        Add a life decision.
        description: description of the decision
        n_choices: number of choices
        """
        self.decisions.append({
            'description': description,
            'n_choices': n_choices
        })

    def calculate_parallel_lives(self):
        """
        Calculate the number of parallel lives
        """
        total_worlds = 1
        for decision in self.decisions:
            total_worlds *= decision['n_choices']
        return total_worlds

    def visualize_life_tree(self):
        """
        Visualize life decision tree
        """
        # Example decisions
        self.decisions = [
            {'description': '今日の朝食は何にする？', 'n_choices': 3},
            {'description': '大学で何を専攻する？', 'n_choices': 5},
            {'description': 'この仕事を受けるか？', 'n_choices': 2},
            {'description': 'あの人に告白するか？', 'n_choices': 2},
            {'description': '新しい街に引っ越すか？', 'n_choices': 2},
        ]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left panel: Decision tree ===
        cumulative_worlds = [1]
        for i, decision in enumerate(self.decisions):
            cumulative_worlds.append(cumulative_worlds[-1] * decision['n_choices'])

        for level, n_worlds in enumerate(cumulative_worlds):
            if level < 4:  # Only draw first few levels to avoid clutter
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

        ax1.set_xlabel('人生の決断ポイント', fontsize=13)
        ax1.set_ylabel('並行生命の分岐', fontsize=13)
        ax1.set_title('あなたの並行生命樹\n各決断が新しい「あなた」を生む',
                     fontsize=14, fontweight='bold')
        ax1.set_xticks(range(len(self.decisions) + 1))
        ax1.set_xticklabels(['誕生'] + [d['description'][:8]+'...'
                                       for d in self.decisions],
                           rotation=45, ha='right', fontsize=9)
        ax1.grid(True, alpha=0.2)

        # === Right panel: Parallel life count ===
        decision_labels = ['誕生'] + [f"決断{i+1}" for i in range(len(self.decisions))]

        ax2.bar(range(len(cumulative_worlds)), cumulative_worlds,
               color='purple', alpha=0.7, edgecolor='black', linewidth=1.5)

        ax2.set_xlabel('人生の段階', fontsize=13)
        ax2.set_ylabel('並行生命の数', fontsize=13)
        ax2.set_title('あなたはいくつの世界に存在するか？', fontsize=14, fontweight='bold')
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

        # Statistics
        total = self.calculate_parallel_lives()

        print("\n" + "="*70)
        print("【あなたの並行生命】")
        print("="*70)
        print("\n決断の例：")
        for i, decision in enumerate(self.decisions, 1):
            print(f"  {i}. {decision['description']} ({decision['n_choices']}つの選択肢)")

        print(f"\n結果：")
        print(f"  * これらの決断が {total:,} 人の並行する「あなた」を生んだ")
        print(f"  * 各「あなた」は異なる人生の軌跡を歩んでいる")
        print(f"  * 各「あなた」は自分が「唯一」だと感じている")

        print(f"\n現実には：")
        print(f"  * 人は1日に約 35,000 の決断をする")
        print(f"  * 各決断には平均 2〜3 の選択肢がある")
        print(f"  * 1日で：約 2^35000 個の世界")
        print(f"  * 一生では：計算不能な天文学的数字！")

        print(f"\n哲学的問い：")
        print(f"  * どの「あなた」が「本当のあなた」なのか？")
        print(f"  * 他の世界の「あなた」も同じことを考えているのか？")
        print(f"  * 「私」の唯一性はどこにあるのか？")

        print(f"\n華厳宗の答え：")
        print(f"  * 全ての「あなた」が真実である")
        print(f"  * 「私」とはもともと単一のものではない")
        print(f"  * 「一即一切」：各々の私が一切の私を含む")
        print("="*70)

# Execute
biography = QuantumBiography()
biography.visualize_life_tree()

def visualize_huayan_fractals():
    """
    Huayan "one dust contains ten directions" fractal visualization.
    Demonstrates the infinitely recursive structure.
    """

    fig = plt.figure(figsize=(18, 12))

    # === Panel 1: Mandelbrot set (classic fractal example) ===
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
    ax1.set_title('マンデルブロ集合：無限の細部\nどの領域を拡大しても類似構造が現れる',
                 fontsize=13, fontweight='bold')
    ax1.set_xlabel('実部')
    ax1.set_ylabel('虚部')
    plt.colorbar(im1, ax=ax1, label='反復回数')

    # === Panel 2: Sierpinski triangle (recursive structure) ===
    ax2 = fig.add_subplot(2, 2, 2)

    def sierpinski(ax, order, points):
        """Draw Sierpinski triangle"""
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
    ax2.set_title('シェルピンスキーの三角形：自己相似\n各小三角形が全体の構造を含む',
                 fontsize=13, fontweight='bold')

    # === Panel 3: Huayan structural diagram ===
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
        ax3.text(x, y, '刹', ha='center', va='center', fontsize=10)
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
    ax3.set_title('華厳宗：一塵に塵数の刹を含む\n刹刹相含、重重無尽',
                 fontsize=13, fontweight='bold')

    ax3.text(0.5, 0.05, '「一塵の中に塵数の刹あり、一一の刹に難思の仏あり」\n無限の再帰',
            ha='center', fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === Panel 4: Correspondence summary ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    【フラクタル vs 華厳「重重無尽」】

    数学的フラクタル：
    * 自己相似性
    * 無限の細部
    * 部分が全体を含む
    * 拡大すると同じ構造が現れる

    華厳宗「重重無尽」：
    * 一塵に十方を含む
    * 刹刹相含
    * 微細相容
    * 無限の再帰

    共通構造：
    - 無限の入れ子
    - 部分＝全体
    - 各層が完全
    - 窮まりなし

    多世界解釈：
    * 宇宙が絶えず分裂する
    * 各世界がさらに分裂する
    * 分岐樹が無限に成長する
    * 指数的爆発

    三者の共通洞察：
    「無限」とは「非常に大きい」ではなく
    構造そのものの性質である
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center',
            family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                     edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('huayan_fractals.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【華厳宗のフラクタル構造】")
    print("="*70)
    print("\n数学的アナロジー：")
    print("  * フラクタル：自己相似、無限の細部")
    print("  * マンデルブロ集合：どの領域を拡大しても類似構造が見える")
    print("  * シェルピンスキーの三角形：各小三角形＝全体")
    print("\n深い洞察：")
    print("  「無限」とは数量の概念ではなく")
    print("  構造そのものの性質である")
    print("  部分即全体、全体即部分")
    print("="*70)

# Execute
visualize_huayan_fractals()

def visualize_time_multiverse():
    """
    Temporal multiverse.
    Demonstrates how past, present, and future contain each other.
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

    # === Left panel: Quantum mechanical temporal branching ===
    times = np.array([0, 1, 2, 3, 4])

    ax1.scatter([0], [0], s=500, c='green', zorder=5,
               edgecolors='black', linewidth=3)
    ax1.text(0, -0.5, 't=0\n初期', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # t=1: split into 2
    y1 = [-1, 1]
    for y in y1:
        ax1.scatter([1], [y], s=300, c='blue', zorder=5,
                   edgecolors='black', linewidth=2, alpha=0.7)
        ax1.plot([0, 1], [0, y], 'b-', alpha=0.5, linewidth=2)

    # t=2: each splits into 2 more
    y2 = [-1.5, -0.5, 0.5, 1.5]
    for i, y in enumerate(y2):
        parent_y = y1[i//2]
        ax1.scatter([2], [y], s=200, c='red', zorder=5,
                   edgecolors='black', linewidth=1.5, alpha=0.6)
        ax1.plot([1, 2], [parent_y, y], 'r-', alpha=0.4, linewidth=1.5)

    # t=3: continue splitting
    y3 = np.linspace(-2, 2, 8)
    for i, y in enumerate(y3):
        parent_y = y2[i//2]
        ax1.scatter([3], [y], s=100, c='purple', zorder=5,
                   edgecolors='black', linewidth=1, alpha=0.5)
        ax1.plot([2, 3], [parent_y, y], 'purple', alpha=0.3, linewidth=1)

    # t=4: more splitting
    y4 = np.linspace(-2.5, 2.5, 16)
    for i, y in enumerate(y4):
        parent_y = y3[i//2]
        ax1.scatter([4], [y], s=50, c='orange', zorder=5,
                   edgecolors='black', linewidth=0.5, alpha=0.4)
        ax1.plot([3, 4], [parent_y, y], 'orange', alpha=0.2, linewidth=0.5)

    ax1.set_xlabel('時間', fontsize=13)
    ax1.set_ylabel('世界の分岐', fontsize=13)
    ax1.set_title('量子多世界：時間は未来に向かって分裂する\n過去は唯一、未来は多元',
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.2)
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-3, 3)

    ax1.text(2, 2.5, f't=2: {4}個の世界', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))
    ax1.text(4, 2.8, f't=4: {16}個の世界', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    # === Right panel: Huayan ten temporal worlds ===
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
    ax2.text(future_center[0], future_center[1], '未来',
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
        (0.1, 0.8, '過去の\n過去'),
        (0.1, 0.5, '過去の\n現在'),
        (0.1, 0.2, '過去の\n未来'),
        (0.5, 0.8, '現在の\n過去'),
        (0.5, 0.2, '現在の\n未来'),
        (0.9, 0.8, '未来の\n過去'),
        (0.9, 0.5, '未来の\n現在'),
        (0.9, 0.2, '未来の\n未来'),
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
    ax2.set_title('華厳宗「十世」：時間が互いに包含する\n過去は未来を含み、未来は過去を含む',
                 fontsize=14, fontweight='bold')

    ax2.text(0.5, 0.05, '「十世隔法異成門」\n一念に三世を含み、三世が互いに摂す',
            ha='center', fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('time_multiverse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【時間の多世界】")
    print("="*70)

    print("\n量子力学の多世界：")
    print("  * 時間は未来に向かって分裂する")
    print("  * 過去：唯一")
    print("  * 未来：多元（指数的増大）")
    print("  * 時間は一方向的")

    print("\n華厳宗「十世」：")
    print("  1. 過去過去世")
    print("  2. 過去現在世")
    print("  3. 過去未来世")
    print("  4. 現在過去世")
    print("  5. 現在現在世")
    print("  6. 現在未来世")
    print("  7. 未来過去世")
    print("  8. 未来現在世")
    print("  9. 未来未来世")
    print("  10. 三世各別総摂為一世")

    print("\n対比：")
    print("  量子：時間は前へ進み、分岐が増える")
    print("  華厳：時間に方向はなく、互いに包含する")
    print("="*70)

# Execute
visualize_time_multiverse()
