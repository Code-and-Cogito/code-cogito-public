# Code & Cogito: 總結——走向統一的實在觀
# Article: https://code-cogito.com/unified-view-reality-conclusion/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'PingFang TC', 'Noto Sans CJK TC', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class RelationalOntologyVisualizer:
    """
    關係性本體論視覺化
    展示：關係先於實體
    """

    def __init__(self):
        pass

    def visualize_ontologies(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === 左上：西方實體本體論 ===
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
            ax.text(pos[0], pos[1]-0.18, f'屬性_{entity}', ha='center',
                   fontsize=9, style='italic', color='gray')

        ax.plot([0.2, 0.8], [0.7, 0.7], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)
        ax.plot([0.2, 0.8], [0.3, 0.3], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)

        ax.text(0.5, 0.95, '西方實體本體論', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, '實體是第一性的\n關係是次要的',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === 右上：東方/量子關係本體論 ===
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

        ax.text(0.5, 0.95, '東方/量子關係本體論', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, '關係是第一性的\n實體從關係中湧現',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === 左下：量子糾纏的例子 ===
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

        ax.text(0.5, 0.62, '糾纏', ha='center', fontsize=11,
               fontweight='bold', color='purple')
        ax.text(0.5, 0.8, '量子糾纏：不可分離', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.15, '|psi> = (|01> + |10>) / sqrt(2)\n不能寫成|psi_1> x |psi_2>\n粒子沒有獨立狀態',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === 右下：緣起的例子 ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        causes = ['無明', '行', '識', '名色', '六入', '觸',
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

        ax.text(0.5, 0.95, '佛教緣起：相依相存', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.08, '此有故彼有，此生故彼生\n無一法獨立存在',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, '模式1：實在的關係性本質',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('relational_ontology.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【模式1：實在的關係性本質】")
        print("="*70)

        print("\n西方傳統本體論（自亞里士多德以來的主流傳統）：")
        print("  - 實體（substance）是第一性的")
        print("  - 屬性（attributes）依附於實體")
        print("  - 關係（relations）是次要的")
        print("  - 例：「蘇格拉底是人」")
        print("    -> 蘇格拉底（實體）有「人性」（屬性）")

        print("\n量子力學的挑戰：")
        print("  - 糾纏中的粒子沒有各自獨立的狀態")
        print("  - 量子糾纏：|psi> != |psi_1> x |psi_2>")
        print("  - 糾纏中的粒子不能各自獨立描述")
        print("  - 關係先於實體")

        print("\n東方哲學的洞見：")
        print("  - 佛教空性：萬物無自性")
        print("  - 緣起：此有故彼有，此生故彼生")
        print("  - 華嚴：一即一切，一切即一")
        print("  - 沒有獨立存在的「實體」")

        print("\n共同結論：")
        print("  實在不是由「獨立的實體」組成")
        print("  而是由「關係」組成")
        print("  關係是第一性的，實體從關係中「湧現」")

        print("\n哲學意義：")
        print("  - 這挑戰了西方形而上學的一條主流傳統")
        print("  - 需要「關係本體論」（relational ontology）")
        print("  - 東方哲學裡有相近的關係式思路（這是作者的類比）")
        print("  - 量子力學的某些詮釋與它相呼應，但物理學並未「證實」哲學主張")

        print("\n實踐意義：")
        print("  - 我們與世界是一體的")
        print("  - 沒有獨立的「自我」")
        print("  - 傷害他人就是傷害自己")
        print("  - 環境倫理學的基礎")
        print("="*70)

# 執行
visualizer = RelationalOntologyVisualizer()
visualizer.visualize_ontologies()

class ParticipationVisualizer:
    """
    參與性實在觀視覺化
    展示：觀察者不是外在的
    """

    def __init__(self):
        pass

    def visualize_observer_roles(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === 左上：經典物理的客觀實在觀 ===
        ax = axes[0, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        world_rect = FancyBboxPatch((0.3, 0.4), 0.4, 0.3,
                                   boxstyle="round,pad=0.02",
                                   facecolor='lightblue', alpha=0.7,
                                   edgecolor='blue', linewidth=3)
        ax.add_patch(world_rect)
        ax.text(0.5, 0.55, '世界\n（客觀存在）', ha='center', va='center',
               fontsize=12, fontweight='bold')

        observer_circle = Circle((0.5, 0.15), 0.08, facecolor='yellow',
                                edgecolor='orange', linewidth=3, alpha=0.8)
        ax.add_patch(observer_circle)
        ax.text(0.5, 0.15, '觀察者', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow = FancyArrowPatch((0.5, 0.4), (0.5, 0.23),
                               arrowstyle='->', mutation_scale=30,
                               linewidth=3, color='green')
        ax.add_patch(arrow)
        ax.text(0.55, 0.32, '信息', ha='left', fontsize=10, color='green')

        ax.text(0.5, 0.9, '經典物理：客觀實在觀', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.02, '世界獨立於觀察者\n「客觀」描述可能',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === 右上：量子力學的參與性實在觀 ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_circle = Circle((0.5, 0.5), 0.4, facecolor='lightgreen',
                           alpha=0.2, edgecolor='green', linewidth=3)
        ax.add_patch(big_circle)
        ax.text(0.5, 0.88, '整體系統', ha='center', fontsize=11,
               fontweight='bold', color='green')

        system_circle = Circle((0.4, 0.55), 0.15, facecolor='lightblue',
                              edgecolor='blue', linewidth=3, alpha=0.7)
        ax.add_patch(system_circle)
        ax.text(0.4, 0.55, '量子\n系統', ha='center', va='center',
               fontsize=10, fontweight='bold')

        observer_circle2 = Circle((0.6, 0.45), 0.15, facecolor='yellow',
                                 edgecolor='orange', linewidth=3, alpha=0.7)
        ax.add_patch(observer_circle2)
        ax.text(0.6, 0.45, '觀察者', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow1 = FancyArrowPatch((0.4, 0.55), (0.6, 0.45),
                                arrowstyle='<->', mutation_scale=20,
                                linewidth=3, color='purple')
        ax.add_patch(arrow1)
        ax.text(0.5, 0.52, '互動', ha='center', fontsize=9,
               color='purple', fontweight='bold')

        ax.text(0.5, 0.9, '量子力學：參與性實在觀', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.08, '儀器與系統不可分\n結果依實驗安排而定',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === 左下：唯心論（錯誤的理解）===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_brain = Circle((0.5, 0.6), 0.25, facecolor='pink',
                          edgecolor='red', linewidth=3, alpha=0.6)
        ax.add_patch(big_brain)
        ax.text(0.5, 0.6, '心靈', ha='center', va='center',
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

        ax.text(0.5, 0.9, '唯心論（錯誤理解）', ha='center',
               fontsize=14, fontweight='bold', color='red')
        ax.text(0.5, 0.08, '世界是心靈創造的\n這不是量子力學的意思！',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === 右下：正確的理解 ===
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

        ax.text(0.5, 0.9, '正確理解：心物不二', ha='center',
               fontsize=14, fontweight='bold', color='purple')
        ax.text(0.5, 0.12, '心與物互相依存\n無法分離\n這是量子力學與東方哲學的共同洞見',
               ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, '模式2：觀察者的參與性角色',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('participatory_reality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【模式2：觀察者的參與性角色】")
        print("="*70)

        print("\n經典物理學的假設：")
        print("  - 世界獨立於觀察者存在")
        print("  - 觀察者可以「客觀」地描述世界")
        print("  - 觀察不改變被觀察對象")
        print("  - 「心」與「物」完全分離")

        print("\n量子力學的發現：")
        print("  - 測量改變系統")
        print("  - 測量儀器與系統不可分離（不需要有意識的觀察者）")
        print("  - 無法獨立於觀察來談論屬性")
        print("  - 玻爾的立場：量子現象只能連同整個實驗安排一起被明確描述")

        print("\n東方哲學的洞見：")
        print("  - 王陽明：「心外無物」")
        print("  - 京都學派：「主客不二」")
        print("  - 禪宗：「能觀所觀不二」")
        print("  - 華嚴：「理事無礙」")

        print("\n重要澄清：")
        print("  這不是說「世界是心靈創造的」（唯心論）")
        print("  而是說「心與物不可分離」")
        print("  就像量子力學不是說「意識創造實在」")
        print("  而是說「能談論什麼，取決於整個實驗安排」")

        print("\n約翰・惠勒（John Wheeler）：")
        print("  「參與者宇宙」（Participatory Universe）")
        print("  - 觀察者是宇宙的參與者")
        print("  - 不是外在的旁觀者")
        print("  - 依惠勒的構想，我們的提問與觀測結果共同塑造實在（推測性詮釋，未成共識）")
        print("="*70)

# 執行
participation_viz = ParticipationVisualizer()
participation_viz.visualize_observer_roles()

class BeyondDualityVisualizer:
    """
    超越二元對立視覺化
    展示：「非此即彼」之外的描述方式
    """

    def __init__(self):
        pass

    def visualize_beyond_duality(self):
        fig = plt.figure(figsize=(18, 12))

        # === 圖1：經典二元邏輯 ===
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

        ax1.text(0.5, 0.85, '經典邏輯\n排中律', ha='center',
                fontsize=12, fontweight='bold')
        ax1.text(0.5, 0.12, 'A 或 非A\n不能既A又非A',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

        # === 圖2：量子疊加 ===
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

        ax2.text(0.35, 0.5, '|0>', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.65, 0.5, '|1>', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.5, 0.5, '疊加', ha='center', va='center',
                fontsize=11, fontweight='bold', color='purple')

        ax2.text(0.5, 0.85, '量子疊加\n超越排中律', ha='center',
                fontsize=12, fontweight='bold')
        ax2.text(0.5, 0.12, '|psi> = alpha|0> + beta|1>\n0與1的疊加',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

        # === 圖3：禪宗不二 ===
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

        ax3.text(0.5, 0.85, '禪宗不二\n超越對立', ha='center',
                fontsize=12, fontweight='bold')
        ax3.text(0.5, 0.12, '非有非無\n即有即無',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === 圖4：波粒二象性 ===
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

        ax4.text(0.5, 0.85, '波粒二象性', ha='center',
                fontsize=12, fontweight='bold')
        ax4.text(0.5, 0.12, '波或粒子行為\n互補性',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === 圖5：色即是空 ===
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
        ax5.text(0.5, 0.12, '現象即本質\n本質即現象',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === 圖6：總結 ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        summary_text = (
            "【超越二元對立】\n\n"
            "經典邏輯（亞里士多德）：\n"
            "  排中律：A 或 非A\n"
            "  矛盾律：不能既A又非A\n\n"
            "量子力學 & 東方哲學：\n\n"
            "  量子：疊加態、波粒二象性\n"
            "  禪宗：非有非無\n"
            "  佛教：色即是空\n"
            "  道家：有無相生\n\n"
            "共同洞見：\n"
            "  實在超越二元邏輯\n"
            "  疊加不讓矛盾成真，但「非黑即白」不夠用\n"
            "  這不是矛盾，而是超越"
        )

        ax6.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=9,
                bbox=dict(boxstyle='round', facecolor='white',
                         alpha=0.9, edgecolor='black', linewidth=2))

        fig.text(0.5, 0.98, '模式3：超越二元對立',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('beyond_duality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【模式3：超越二元對立】")
        print("="*70)

        print("\n經典邏輯（亞里士多德以來）：")
        print("  1. 排中律（Law of Excluded Middle）：")
        print("     A 或 非A（必居其一）")
        print("  2. 矛盾律（Law of Non-Contradiction）：")
        print("     不能既A又非A")

        print("\n量子力學的挑戰：")
        print("  - 波粒二象性：光在不同實驗安排下呈現波動或粒子行為")
        print("  - 疊加態：|psi> = alpha|0> + beta|1>（0與1的疊加）")
        print("  - 互補原理：波與粒子互補")
        print("  - 薛丁格的貓（1935年的思想實驗）：測量前處於「死」與「活」的疊加態")

        print("\n東方哲學的洞見：")
        print("  - 禪宗：非有非無，即有即無")
        print("  - 佛教：色即是空，空即是色")
        print("  - 道家：有無相生，難易相成")
        print("  - 華嚴：理事無礙，事事無礙")

        print("\n龍樹的中觀：")
        print("  「不生亦不滅，不常亦不斷，")
        print("   不一亦不異，不來亦不出。」")
        print("  -> 超越所有二元對立")
        print("="*70)

# 執行
duality_viz = BeyondDualityVisualizer()
duality_viz.visualize_beyond_duality()

def visualize_convergence():
    """
    視覺化科學與哲學路徑的匯合
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

    # === 左圖：兩條路徑 ===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    science_x = [0.2] * 10
    science_y = np.linspace(0.1, 0.7, 10)

    milestones_science = [
        (0.15, '黑體輻射\n1900'),
        (0.25, '物質波\n1924'),
        (0.35, '不確定性\n1927'),
        (0.45, '糾纏\n1935'),
        (0.55, '貝爾不等式\n1964'),
        (0.65, '量子計算\n1980s'),
    ]

    for y, label in milestones_science:
        ax1.plot(0.2, y, 'o', markersize=12, color='blue')
        ax1.text(0.05, y, label, ha='right', fontsize=8)

    ax1.plot(science_x, science_y, 'b-', linewidth=3, alpha=0.5)
    ax1.text(0.2, 0.08, '科學路徑', ha='center', fontsize=12,
            fontweight='bold', color='blue')

    phil_x = [0.8] * 10
    phil_y = np.linspace(0.1, 0.7, 10)

    milestones_phil = [
        (0.15, '佛陀\n前5世紀'),
        (0.25, '龍樹\n200'),
        (0.35, '華嚴\n7-8世紀'),
        (0.45, '禪宗\n700'),
        (0.55, '陽明\n1508'),
        (0.65, '京都學派\n1900s'),
    ]

    for y, label in milestones_phil:
        ax1.plot(0.8, y, 'o', markersize=12, color='orange')
        ax1.text(0.95, y, label, ha='left', fontsize=8)

    ax1.plot(phil_x, phil_y, color='orange', linewidth=3, alpha=0.5)
    ax1.text(0.8, 0.08, '哲學/修行路徑', ha='center', fontsize=12,
            fontweight='bold', color='orange')

# |     # 匯合點
# |     convergence_y = 0.85
# |     ax1.plot([0.2, 0.5], [0.7, convergence_y], 'b-', linewidth=3)
# |     ax1.plot([0.8, 0.5], [0.7, convergence_y], color='orange', linewidth=3)
# | 
# |     ax1.scatter(0.5, convergence_y, s=500, marker='*',
# |                color='gold', edgecolors='black', linewidths=2, zorder=5)
# |     ax1.text(0.5, convergence_y, '匯合', ha='center', va='center',
# |             fontsize=12, fontweight='bold')
# | 
# |     ax1.text(0.5, 0.95, '統一的實在觀', ha='center',
# |             fontsize=14, fontweight='bold', color='purple')
# | 
# |     ax1.set_title('兩條認識路徑的驚人匯合', fontsize=14, fontweight='bold')
# | 
# |     # === 右圖：共同洞見 ===
# |     ax2.axis('off')
# | 
# |     insights_text = (
# |         "【三大共同洞見】\n\n"
# |         "1. 實在的關係性本質\n"
# |         "   科學：量子糾纏、非局域性\n"
# |         "   哲學：緣起、因陀羅網\n"
# |         "   -> 關係先於實體\n\n"
# |         "2. 觀察者的參與性角色\n"
# |         "   科學：測量問題、波函數坍縮\n"
# |         "   哲學：心外無物、主客不二\n"
# |         "   -> 心物不可分\n\n"
# |         "3. 超越二元對立\n"
# |         "   科學：波粒二象性、互補原理\n"
# |         "   哲學：不二法門、中觀\n"
# |         "   -> 需要新邏輯\n\n"
# |         "---\n\n"
# |         "兩條完全不同的路徑：\n"
# |         "  科學：外向觀察，數學建模\n"
# |         "  哲學：內向體驗，概念思辨\n\n"
# |         "在這三點上指向相近的結論！\n\n"
# |         "這暗示：\n"
# |         "它們可能觸及了\n"
# |         "實在的同一個深層真理\n\n"
# |         "---\n\n"
# |         "但要注意：\n"
# |         "  這不意味它們完全等同\n"
# |         "  科學有可驗證性\n"
# |         "  哲學有直接體驗\n"
# |         "  兩者互補，不可替代"
# |     )
# | 
# |     ax2.text(0.5, 0.5, insights_text, ha='center', va='center',
# |             fontsize=9.5,
# |             bbox=dict(boxstyle='round', facecolor='lightyellow',
# |                      alpha=0.9, edgecolor='purple', linewidth=3))
# | 
# |     ax2.set_title('共同指向的真理', fontsize=14, fontweight='bold')
# | 
# |     plt.tight_layout()
# |     plt.savefig('paths_convergence.png', dpi=300, bbox_inches='tight')
# |     plt.show()

    print("\n" + "="*70)
    print("【兩條認識路徑的驚人匯合】")
    print("="*70)

    print("\n科學路徑：")
    print("  方法：觀察實驗、數學建模、可重複驗證")
    print("  里程碑：")
    print("    1900：普朗克（黑體輻射）")
    print("    1924：德布羅意（物質波，把二象性延伸到物質）")
    print("    1927：海森堡（不確定性）")
    print("    1935：EPR悖論（糾纏）")
    print("    1964：貝爾不等式")
    print("    1980s：量子計算")

    print("\n哲學/修行路徑：")
    print("  方法：內省冥想、哲學思辨、直接體驗")
    print("  里程碑：")
    print("    前5世紀：佛陀（緣起；空性由龍樹系統化）")
    print("    200：龍樹（中觀）")
    print("    7-8世紀：華嚴宗（因陀羅網）")
    print("    700：禪宗（不二）")
    print("    1508：王陽明（龍場悟道，心即理）")
    print("    1900s：京都學派（西田幾多郎）")

    print("\n驚人的匯合：")
    print("  兩條完全不同的路徑")
    print("  在這三點上指向相近的結論！")
    print("="*70)

# 執行
visualize_convergence()
