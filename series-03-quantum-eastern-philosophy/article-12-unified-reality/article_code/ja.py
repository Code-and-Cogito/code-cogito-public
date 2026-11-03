# Code & Cogito: 総括——統一的実在観へ
# Article: https://code-cogito.com/ja/unified-view-reality-conclusion-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class RelationalOntologyVisualizer:
    """
    Relational ontology visualization
    Demonstrates: Relations precede entities
    """

    def __init__(self):
        pass

    def visualize_ontologies(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === Top-left: Western substance ontology ===
        ax = axes[0, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        entities = ['A', 'B', 'C', 'D']
        positions = [(0.2, 0.7), (0.8, 0.7), (0.2, 0.3), (0.8, 0.3)]

        for entity, pos in zip(entities, positions):
            circle = Circle(pos, 0.12, facecolor='lightblue',
                          edgecolor='blue', linewidth=3)
            ax.add_patch(circle)
            ax.text(pos[0], pos[1], entity, ha='center', va='center',
                   fontsize=16, fontweight='bold')
            ax.text(pos[0], pos[1]-0.18, f'属性_{entity}', ha='center',
                   fontsize=9, style='italic', color='gray')

        ax.plot([0.2, 0.8], [0.7, 0.7], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)
        ax.plot([0.2, 0.8], [0.3, 0.3], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)

        ax.text(0.5, 0.95, '西洋の実体存在論', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, '実体が第一義的\n関係は二次的',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Top-right: Eastern/Quantum relational ontology ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        G = nx.complete_graph(6)
        pos_network = nx.spring_layout(G, center=(0.5, 0.5), k=0.3, seed=42)

        for edge in G.edges():
            x_coords = [pos_network[edge[0]][0], pos_network[edge[1]][0]]
            y_coords = [pos_network[edge[0]][1], pos_network[edge[1]][1]]
            ax.plot(x_coords, y_coords, 'purple', linewidth=3, alpha=0.5)

        for node, pos in pos_network.items():
            circle = Circle(pos, 0.05, facecolor='lightgreen',
                          edgecolor='darkgreen', linewidth=2, alpha=0.7)
            ax.add_patch(circle)

        ax.text(0.5, 0.95, '東洋/量子の関係存在論', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, '関係が第一義的\n実体は関係から創発する',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Bottom-left: Quantum entanglement example ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle1 = Circle((0.3, 0.5), 0.1, facecolor='red',
                        edgecolor='darkred', linewidth=3, alpha=0.6)
        circle2 = Circle((0.7, 0.5), 0.1, facecolor='blue',
                        edgecolor='darkblue', linewidth=3, alpha=0.6)
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        ax.text(0.3, 0.5, '粒子1', ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')
        ax.text(0.7, 0.5, '粒子2', ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        x = np.linspace(0.3, 0.7, 100)
        y = 0.5 + 0.05 * np.sin(20 * (x - 0.3))
        ax.plot(x, y, 'purple', linewidth=4, alpha=0.7)

        ax.text(0.5, 0.62, 'もつれ', ha='center', fontsize=11,
               fontweight='bold', color='purple')
        ax.text(0.5, 0.8, '量子もつれ：分離不可能', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.15, '|ψ⟩ = (|01⟩ + |10⟩) / √2\n|ψ₁⟩ ⊗ |ψ₂⟩ と書けない\n粒子に独立した状態はない',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Bottom-right: Dependent origination example ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        causes = ['無明', '行', '識', '名色', '六入', '触',
                  '受', '愛', '取', '有', '生', '老死']
        n = len(causes)
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)

        radius = 0.35
        for i, (cause, angle) in enumerate(zip(causes, angles)):
            x = 0.5 + radius * np.cos(angle)
            y = 0.5 + radius * np.sin(angle)

            circle = Circle((x, y), 0.05, facecolor='orange',
                          edgecolor='darkorange', linewidth=2, alpha=0.7)
            ax.add_patch(circle)
            ax.text(x, y, cause, ha='center', va='center',
                   fontsize=7, fontweight='bold')

            next_angle = angles[(i+1) % n]
            x_next = 0.5 + radius * np.cos(next_angle)
            y_next = 0.5 + radius * np.sin(next_angle)

            arrow = FancyArrowPatch((x, y), (x_next, y_next),
                                   arrowstyle='->', mutation_scale=15,
                                   linewidth=2, color='darkorange', alpha=0.5)
            ax.add_patch(arrow)

        ax.text(0.5, 0.95, '仏教の縁起：相依相存', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.08, '此あれば彼あり、此生ずれば彼生ず\nいかなる法も独立して存在しない',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, 'パターン1：実在の関係的本質',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('relational_ontology.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【パターン1：実在の関係的本質】")
        print("="*70)

        print("\n西洋の伝統的存在論（アリストテレス以来の主流）：")
        print("  - 実体（substance）が第一義的")
        print("  - 属性（attributes）は実体に付随する")
        print("  - 関係（relations）は二次的")
        print("  - 例：「ソクラテスは人間である」")
        print("    -> ソクラテス（実体）が「人間性」（属性）を持つ")

        print("\n量子力学の挑戦：")
        print("  - もつれた粒子には独立した状態がない")
        print("  - 量子もつれ：|ψ⟩ ≠ |ψ₁⟩ ⊗ |ψ₂⟩")
        print("  - もつれた粒子を独立に記述できない")
        print("  - 関係が実体に先行する")

        print("\n東洋哲学の洞察：")
        print("  - 仏教の空性：万物に自性なし")
        print("  - 縁起：此あれば彼あり、此生ずれば彼生ず")
        print("  - 華厳：一即一切、一切即一")
        print("  - 独立して存在する「実体」はない")

        print("\n共通の結論：")
        print("  実在は「独立した実体」から成るのではなく")
        print("  「関係」から成る")
        print("  関係が第一義的であり、実体は関係から「創発」する")

        print("\n哲学的意義：")
        print("  - 西洋形而上学の一つの主流への挑戦")
        print("  - 「関係存在論」（relational ontology）の必要性")
        print("  - 東洋哲学にも近い関係論的な発想がある（筆者の類比）")
        print("  - 量子力学の一部の解釈はこれと響き合うが、哲学的主張を「証明」したわけではない")

        print("\n実践的意義：")
        print("  - 私たちと世界は一体である")
        print("  - 独立した「自己」は存在しない")
        print("  - 他者を傷つけることは自己を傷つけること")
        print("  - 環境倫理学の基盤")
        print("="*70)

# Execute
visualizer = RelationalOntologyVisualizer()
visualizer.visualize_ontologies()

class ParticipationVisualizer:
    """
    Participatory reality visualization
    Demonstrates: The observer is not external
    """

    def __init__(self):
        pass

    def visualize_observer_roles(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === Top-left: Classical physics objective reality ===
        ax = axes[0, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        world_rect = FancyBboxPatch((0.3, 0.4), 0.4, 0.3,
                                   boxstyle="round,pad=0.02",
                                   facecolor='lightblue', alpha=0.7,
                                   edgecolor='blue', linewidth=3)
        ax.add_patch(world_rect)
        ax.text(0.5, 0.55, '世界\n（客観的存在）', ha='center', va='center',
               fontsize=12, fontweight='bold')

        observer_circle = Circle((0.5, 0.15), 0.08, facecolor='yellow',
                                edgecolor='orange', linewidth=3, alpha=0.8)
        ax.add_patch(observer_circle)
        ax.text(0.5, 0.15, '観測者', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow = FancyArrowPatch((0.5, 0.4), (0.5, 0.23),
                               arrowstyle='->', mutation_scale=30,
                               linewidth=3, color='green')
        ax.add_patch(arrow)
        ax.text(0.55, 0.32, '情報', ha='left', fontsize=10, color='green')

        ax.text(0.5, 0.9, '古典物理学：客観的実在観', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.02, '世界は観測者から独立\n「客観的」記述が可能',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Top-right: Quantum mechanics participatory reality ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_circle = Circle((0.5, 0.5), 0.4, facecolor='lightgreen',
                           alpha=0.2, edgecolor='green', linewidth=3)
        ax.add_patch(big_circle)
        ax.text(0.5, 0.88, '全体システム', ha='center', fontsize=11,
               fontweight='bold', color='green')

        system_circle = Circle((0.4, 0.55), 0.15, facecolor='lightblue',
                              edgecolor='blue', linewidth=3, alpha=0.7)
        ax.add_patch(system_circle)
        ax.text(0.4, 0.55, '量子\nシステム', ha='center', va='center',
               fontsize=10, fontweight='bold')

        observer_circle2 = Circle((0.6, 0.45), 0.15, facecolor='yellow',
                                 edgecolor='orange', linewidth=3, alpha=0.7)
        ax.add_patch(observer_circle2)
        ax.text(0.6, 0.45, '観測者', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow1 = FancyArrowPatch((0.4, 0.55), (0.6, 0.45),
                                arrowstyle='<->', mutation_scale=20,
                                linewidth=3, color='purple')
        ax.add_patch(arrow1)
        ax.text(0.5, 0.52, '相互作用', ha='center', fontsize=9,
               color='purple', fontweight='bold')

        ax.text(0.5, 0.9, '量子力学：参与的実在観', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.08, '装置とシステムは不可分\n結果は実験配置に依存する',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Bottom-left: Idealism (incorrect understanding) ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_brain = Circle((0.5, 0.6), 0.25, facecolor='pink',
                          edgecolor='red', linewidth=3, alpha=0.6)
        ax.add_patch(big_brain)
        ax.text(0.5, 0.6, '心', ha='center', va='center',
               fontsize=14, fontweight='bold')

        small_world = Circle((0.5, 0.3), 0.08, facecolor='lightblue',
                           edgecolor='blue', linewidth=2, alpha=0.6)
        ax.add_patch(small_world)
        ax.text(0.5, 0.3, '世界', ha='center', va='center',
               fontsize=8)

        arrow2 = FancyArrowPatch((0.5, 0.5), (0.5, 0.38),
                                arrowstyle='->', mutation_scale=25,
                                linewidth=3, color='red')
        ax.add_patch(arrow2)

        ax.text(0.5, 0.9, '唯心論（誤った理解）', ha='center',
               fontsize=14, fontweight='bold', color='red')
        ax.text(0.5, 0.08, '世界は心が創造したもの\nこれは量子力学の意味ではない！',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Bottom-right: Correct understanding ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        theta = np.linspace(0, 2*np.pi, 100)
        r = 0.3
        x_circle = 0.5 + r * np.cos(theta)
        y_circle = 0.5 + r * np.sin(theta)

        ax.fill_between(x_circle[25:75], y_circle[25:75], 0.5,
                       color='yellow', alpha=0.6)
        ax.fill_between(x_circle[:25], 0.5, y_circle[:25],
                       color='lightblue', alpha=0.6)
        ax.fill_between(x_circle[75:], 0.5, y_circle[75:],
                       color='lightblue', alpha=0.6)

        circle_outline = Circle((0.5, 0.5), 0.3, fill=False,
                               edgecolor='black', linewidth=3)
        ax.add_patch(circle_outline)

        ax.text(0.35, 0.5, '心', ha='center', va='center',
               fontsize=14, fontweight='bold')
        ax.text(0.65, 0.5, '物', ha='center', va='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.5, '不二', ha='center', va='center',
               fontsize=11, fontweight='bold', color='purple')

        ax.text(0.5, 0.9, '正しい理解：心物不二', ha='center',
               fontsize=14, fontweight='bold', color='purple')
        ax.text(0.5, 0.12, '心と物は相互に依存する\n分離できない\nこれが量子力学と東洋哲学の共通の洞察',
               ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, 'パターン2：観測者の参与的役割',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('participatory_reality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【パターン2：観測者の参与的役割】")
        print("="*70)

        print("\n古典物理学の前提：")
        print("  - 世界は観測者から独立して存在する")
        print("  - 観測者は世界を「客観的に」記述できる")
        print("  - 観測は被観測対象を変化させない")
        print("  - 「心」と「物」は完全に分離している")

        print("\n量子力学の発見：")
        print("  - 測定がシステムを変化させる")
        print("  - 測定装置とシステムは分離不可能（意識をもつ観測者は不要）")
        print("  - 観測から独立して属性を語ることはできない")
        print("  - ボーアの立場：量子現象は実験配置全体と合わせてはじめて曖昧さなく記述できる")

        print("\n東洋哲学の洞察：")
        print("  - 王陽明：「心外無物」")
        print("  - 京都学派：「主客不二」")
        print("  - 禅宗：「能観所観不二」")
        print("  - 華厳：「理事無礙」")

        print("\n重要な補足：")
        print("  これは「世界は心が創造したもの」（唯心論）ではない")
        print("  「心と物は分離できない」ということ")
        print("  量子力学も「意識が実在を創造する」とは言っていない")
        print("  「語りうる内容は実験配置全体に依存する」と言っている")

        print("\nジョン・ホイーラー（John Wheeler）：")
        print("  「参与者宇宙」（Participatory Universe）")
        print("  - 観測者は宇宙の参与者である")
        print("  - 外部の傍観者ではない")
        print("  - ホイーラーの構想では、問いと観測結果が実在を形づくる（推測的な解釈で、共通理解ではない）")
        print("="*70)

# Execute
participation_viz = ParticipationVisualizer()
participation_viz.visualize_observer_roles()

class BeyondDualityVisualizer:
    """
    Beyond duality visualization
    Demonstrates: descriptions beyond either/or thinking
    """

    def __init__(self):
        pass

    def visualize_beyond_duality(self):
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Classical binary logic ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.axis('off')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        circle_A = Circle((0.3, 0.5), 0.15, facecolor='blue',
                         edgecolor='darkblue', linewidth=3, alpha=0.7)
        circle_not_A = Circle((0.7, 0.5), 0.15, facecolor='red',
                             edgecolor='darkred', linewidth=3, alpha=0.7)
        ax1.add_patch(circle_A)
        ax1.add_patch(circle_not_A)

        ax1.text(0.3, 0.5, 'A', ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')
        ax1.text(0.7, 0.5, '非A', ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')
        ax1.text(0.5, 0.5, 'or', ha='center', va='center',
                fontsize=12, fontweight='bold')

        ax1.text(0.5, 0.85, '古典論理\n排中律', ha='center',
                fontsize=12, fontweight='bold')
        ax1.text(0.5, 0.12, 'A または 非A\nAかつ非Aは不可能',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

        # === Panel 2: Quantum superposition ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        circle_A2 = Circle((0.4, 0.5), 0.18, facecolor='blue',
                          edgecolor='darkblue', linewidth=3, alpha=0.5)
        circle_not_A2 = Circle((0.6, 0.5), 0.18, facecolor='red',
                              edgecolor='darkred', linewidth=3, alpha=0.5)
        ax2.add_patch(circle_A2)
        ax2.add_patch(circle_not_A2)

        ax2.text(0.35, 0.5, '|0⟩', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.65, 0.5, '|1⟩', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.5, 0.5, '重ね合わせ', ha='center', va='center',
                fontsize=11, fontweight='bold', color='purple')

        ax2.text(0.5, 0.85, '量子重ね合わせ\n排中律を超えて', ha='center',
                fontsize=12, fontweight='bold')
        ax2.text(0.5, 0.12, '|ψ⟩ = α|0⟩ + β|1⟩\n0と1の重ね合わせ',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

        # === Panel 3: Zen non-duality ===
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.axis('off')
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)

        circle_you = Circle((0.4, 0.5), 0.18, facecolor='yellow',
                          edgecolor='orange', linewidth=3, alpha=0.4)
        circle_wu = Circle((0.6, 0.5), 0.18, facecolor='white',
                          edgecolor='gray', linewidth=3, alpha=0.4)
        ax3.add_patch(circle_you)
        ax3.add_patch(circle_wu)

        ax3.text(0.35, 0.5, '有', ha='center', va='center',
                fontsize=16, fontweight='bold')
        ax3.text(0.65, 0.5, '無', ha='center', va='center',
                fontsize=16, fontweight='bold')
        ax3.text(0.5, 0.5, '不二', ha='center', va='center',
                fontsize=12, fontweight='bold', color='gold')

        ax3.text(0.5, 0.85, '禅の不二\n対立を超えて', ha='center',
                fontsize=12, fontweight='bold')
        ax3.text(0.5, 0.12, '非有非無\n即有即無',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Panel 4: Wave-particle duality ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)

        x_wave = np.linspace(0.1, 0.45, 100)
        y_wave = 0.5 + 0.1 * np.sin(20 * x_wave)
        ax4.plot(x_wave, y_wave, 'b-', linewidth=3)
        ax4.text(0.275, 0.35, '波', ha='center', fontsize=12,
                fontweight='bold', color='blue')

        ax4.scatter([0.65, 0.75, 0.85], [0.5, 0.55, 0.45],
                   s=200, c='red', edgecolors='darkred', linewidths=2)
        ax4.text(0.75, 0.35, '粒子', ha='center', fontsize=12,
                fontweight='bold', color='red')

        ax4.text(0.5, 0.5, '=', ha='center', va='center',
                fontsize=20, fontweight='bold')

        ax4.text(0.5, 0.85, '波粒二重性', ha='center',
                fontsize=12, fontweight='bold')
        ax4.text(0.5, 0.12, '光は波であり粒子でもある\n相補性',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Panel 5: Form is emptiness ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')
        ax5.set_xlim(0, 1)
        ax5.set_ylim(0, 1)

        square = plt.Rectangle((0.15, 0.4), 0.2, 0.2,
                               facecolor='orange', alpha=0.7,
                               edgecolor='darkorange', linewidth=3)
        ax5.add_patch(square)
        ax5.text(0.25, 0.5, '色', ha='center', va='center',
                fontsize=16, fontweight='bold')

        circle_empty = Circle((0.75, 0.5), 0.12, facecolor='white',
                             edgecolor='black', linewidth=3, linestyle='--')
        ax5.add_patch(circle_empty)
        ax5.text(0.75, 0.5, '空', ha='center', va='center',
                fontsize=16, fontweight='bold')

        ax5.annotate('', xy=(0.63, 0.5), xytext=(0.35, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
        ax5.text(0.49, 0.55, '即是', ha='center', fontsize=10,
                color='purple', fontweight='bold')

        ax5.text(0.5, 0.85, '色即是空', ha='center',
                fontsize=12, fontweight='bold')
        ax5.text(0.5, 0.12, '現象すなわち本質\n本質すなわち現象',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Panel 6: Summary ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        summary_text = (
            "【二元対立の超越】\n\n"
            "古典論理（アリストテレス）：\n"
            "  排中律：A または 非A\n"
            "  矛盾律：Aかつ非Aは不可能\n\n"
            "量子力学 & 東洋哲学：\n\n"
            "  量子：重ね合わせ、波粒二重性\n"
            "  禅宗：非有非無\n"
            "  仏教：色即是空\n"
            "  道家：有無相生\n\n"
            "共通の洞察：\n"
            "  実在は二元論理を超越する\n"
            "  重ね合わせは矛盾を真にしないが「白か黒か」では足りない\n"
            "  これは矛盾ではなく、超越である"
        )

        ax6.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=9,
                bbox=dict(boxstyle='round', facecolor='white',
                         alpha=0.9, edgecolor='black', linewidth=2))

        fig.text(0.5, 0.98, 'パターン3：二元対立の超越',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('beyond_duality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【パターン3：二元対立の超越】")
        print("="*70)

        print("\n古典論理（アリストテレス以来）：")
        print("  1. 排中律（Law of Excluded Middle）：")
        print("     A または 非A（必ずどちらか一方）")
        print("  2. 矛盾律（Law of Non-Contradiction）：")
        print("     Aかつ非Aは不可能")

        print("\n量子力学の挑戦：")
        print("  - 波粒二重性：光は実験の配置に応じて波または粒子の振る舞いを示す")
        print("  - 重ね合わせ：|ψ⟩ = α|0⟩ + β|1⟩（0と1の重ね合わせ）")
        print("  - 相補性原理：波と粒子は互いに補完的")
        print("  - シュレーディンガーの猫（1935年の思考実験）：測定前は「死」と「生」の重ね合わせ状態")

        print("\n東洋哲学の洞察：")
        print("  - 禅宗：非有非無、即有即無")
        print("  - 仏教：色即是空、空即是色")
        print("  - 道家：有無相生、難易相成")
        print("  - 華厳：理事無礙、事事無礙")

        print("\n龍樹の中観：")
        print("  「不生にして不滅、不常にして不断、")
        print("   不一にして不異、不来にして不出。」")
        print("  -> あらゆる二元対立を超越する")
        print("="*70)

# Execute
duality_viz = BeyondDualityVisualizer()
duality_viz.visualize_beyond_duality()

def visualize_convergence():
    """
    Visualize the convergence of scientific and philosophical paths
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

    # === Left: Two paths ===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    science_x = [0.2] * 10
    science_y = np.linspace(0.1, 0.7, 10)

    milestones_science = [
        (0.15, '黒体放射\n1900'),
        (0.25, '物質波\n1924'),
        (0.35, '不確定性\n1927'),
        (0.45, 'もつれ\n1935'),
        (0.55, 'ベル不等式\n1964'),
        (0.65, '量子計算\n1980s'),
    ]

    for y, label in milestones_science:
        ax1.plot(0.2, y, 'o', markersize=12, color='blue')
        ax1.text(0.05, y, label, ha='right', fontsize=8)

    ax1.plot(science_x, science_y, 'b-', linewidth=3, alpha=0.5)
    ax1.text(0.2, 0.08, '科学の道', ha='center', fontsize=12,
            fontweight='bold', color='blue')

    phil_x = [0.8] * 10
    phil_y = np.linspace(0.1, 0.7, 10)

    milestones_phil = [
        (0.15, '仏陀\n前5世紀'),
        (0.25, '龍樹\n200'),
        (0.35, '華厳\n7-8世紀'),
        (0.45, '禅宗\n700'),
        (0.55, '道元\n1231'),
        (0.65, '京都学派\n1900s'),
    ]

    for y, label in milestones_phil:
        ax1.plot(0.8, y, 'o', markersize=12, color='orange')
        ax1.text(0.95, y, label, ha='left', fontsize=8)

    ax1.plot(phil_x, phil_y, color='orange', linewidth=3, alpha=0.5)
    ax1.text(0.8, 0.08, '哲学/修行の道', ha='center', fontsize=12,
            fontweight='bold', color='orange')

# |     # Convergence point
# |     convergence_y = 0.85
# |     ax1.plot([0.2, 0.5], [0.7, convergence_y], 'b-', linewidth=3)
# |     ax1.plot([0.8, 0.5], [0.7, convergence_y], color='orange', linewidth=3)
# | 
# |     ax1.scatter(0.5, convergence_y, s=500, marker='*',
# |                color='gold', edgecolors='black', linewidths=2, zorder=5)
# |     ax1.text(0.5, convergence_y, '合流', ha='center', va='center',
# |             fontsize=12, fontweight='bold')
# | 
# |     ax1.text(0.5, 0.95, '統一的実在観', ha='center',
# |             fontsize=14, fontweight='bold', color='purple')
# | 
# |     ax1.set_title('2つの認識の道の驚嘆すべき合流', fontsize=14, fontweight='bold')
# | 
# |     # === Right: Common insights ===
# |     ax2.axis('off')
# | 
# |     insights_text = (
# |         "【3つの共通の洞察】\n\n"
# |         "1. 実在の関係的本質\n"
# |         "   科学：量子もつれ、非局所性\n"
# |         "   哲学：縁起、インドラ網\n"
# |         "   -> 関係は実体に先行する\n\n"
# |         "2. 観測者の参与的役割\n"
# |         "   科学：測定問題、波動関数の崩壊\n"
# |         "   哲学：心外無物、主客不二\n"
# |         "   -> 心物不可分\n\n"
# |         "3. 二元対立の超越\n"
# |         "   科学：波粒二重性、相補性原理\n"
# |         "   哲学：不二法門、中観\n"
# |         "   -> 新しい論理が必要\n\n"
# |         "---\n\n"
# |         "根本的に異なる2つの道：\n"
# |         "  科学：外向的観察、数学的モデル化\n"
# |         "  哲学：内向的体験、概念的思弁\n\n"
# |         "にもかかわらずこの3点では近い結論に至った！\n\n"
# |         "これが示唆すること：\n"
# |         "両者はおそらく\n"
# |         "実在の同一の深層真理に触れている\n\n"
# |         "---\n\n"
# |         "ただし注意：\n"
# |         "  両者が完全に等価というわけではない\n"
# |         "  科学には検証可能性がある\n"
# |         "  哲学には直接体験がある\n"
# |         "  両者は互いに補完し合い、代替不可能"
# |     )
# | 
# |     ax2.text(0.5, 0.5, insights_text, ha='center', va='center',
# |             fontsize=9.5,
# |             bbox=dict(boxstyle='round', facecolor='lightyellow',
# |                      alpha=0.9, edgecolor='purple', linewidth=3))
# | 
# |     ax2.set_title('共通に指し示す真理', fontsize=14, fontweight='bold')
# | 
# |     plt.tight_layout()
# |     plt.savefig('paths_convergence.png', dpi=300, bbox_inches='tight')
# |     plt.show()

    print("\n" + "="*70)
    print("【2つの認識の道の驚嘆すべき合流】")
    print("="*70)

    print("\n科学の道：")
    print("  方法：観察と実験、数学的モデル化、再現可能な検証")
    print("  マイルストーン：")
    print("    1900：プランク（黒体放射）")
    print("    1924：ド・ブロイ（物質波：二重性を物質へ拡張）")
    print("    1927：ハイゼンベルク（不確定性）")
    print("    1935：EPRパラドックス（もつれ）")
    print("    1964：ベル不等式")
    print("    1980s：量子コンピューティング")

    print("\n哲学/修行の道：")
    print("  方法：内省と瞑想、哲学的思弁、直接的体験")
    print("  マイルストーン：")
    print("    前5世紀：仏陀（縁起。空性は後に龍樹が体系化）")
    print("    200：龍樹（中観）")
    print("    7-8世紀：華厳宗（インドラ網）")
    print("    700：禅宗（不二）")
    print("    1231年〜：道元（『正法眼蔵』の執筆開始）")
    print("    1900s：京都学派（西田幾多郎）")

    print("\n驚嘆すべき合流：")
    print("  根本的に異なる2つの道が")
    print("  この3点では近い結論に至った！")
    print("="*70)

# Execute
visualize_convergence()
