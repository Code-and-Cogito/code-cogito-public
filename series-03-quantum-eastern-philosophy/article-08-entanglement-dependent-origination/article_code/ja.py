# Code & Cogito: 量子もつれ vs 仏教「縁起」——万物は互いの因縁によって在る
# Article: https://code-cogito.com/ja/quantum-entanglement-dependent-origination-ja/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class DependentOriginationNetwork:
    """
    Dependent Origination Network Simulator
    Demonstrates how all things arise through mutual causation
    """

    def __init__(self):
        self.G = nx.DiGraph()

# |     def create_twelve_links(self):
# |         """
# |         Create the Twelve Links of Dependent Origination network
# |         """
# |         # Twelve links (in Japanese Buddhist terminology)
# |         links = [
# |             ('無明', '行'),
# |             ('行', '識'),
# |             ('識', '名色'),
# |             ('名色', '六処'),
# |             ('六処', '触'),
# |             ('触', '受'),
# |             ('受', '愛'),
# |             ('愛', '取'),
# |             ('取', '有'),
# |             ('有', '生'),
# |             ('生', '老死'),
# |             ('老死', '無明'),  # cycle
# |         ]
# | 
# |         self.G.add_edges_from(links)

    def visualize_twelve_links(self):
        """
        Visualize the Twelve Links of Dependent Origination
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

        # === Left: Twelve Links Ring ===
        self.create_twelve_links()

        # Circular layout
        pos = nx.circular_layout(self.G)

        # Node colors by category
        node_colors = {
            '無明': 'gray',
            '行': 'orange',
            '識': 'yellow',
            '名色': 'lightblue',
            '六処': 'lightgreen',
            '触': 'cyan',
            '受': 'pink',
            '愛': 'red',
            '取': 'darkred',
            '有': 'purple',
            '生': 'green',
            '老死': 'black',
        }

        colors = [node_colors[node] for node in self.G.nodes()]

        # Draw network
        nx.draw_networkx_nodes(self.G, pos, node_color=colors,
                              node_size=1500, alpha=0.8,
                              edgecolors='black', linewidths=2, ax=ax1)

        nx.draw_networkx_labels(self.G, pos, font_size=12,
                               font_weight='bold', ax=ax1)

        nx.draw_networkx_edges(self.G, pos, edge_color='gray',
                              arrows=True, arrowsize=20, arrowstyle='->',
                              width=2, connectionstyle='arc3,rad=0.1', ax=ax1)

        ax1.set_title('十二因縁：輪廻の機構\n「此れ有るが故に彼れ有り、此れ生ずるが故に彼れ生ず」',
                     fontsize=14, fontweight='bold')
        ax1.axis('off')

        # Explanation text
        explanation = '''
        十二因縁：

        1. 無明 → 2. 行 → 3. 識
        → 4. 名色 → 5. 六処 → 6. 触
        → 7. 受 → 8. 愛 → 9. 取
        → 10. 有 → 11. 生 → 12. 老死
        → 1. 無明（循環）

        任意の一支を断てば → 全鎖が崩壊する
        '''

        ax1.text(0.5, -1.3, explanation, ha='center', fontsize=10,
                transform=ax1.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === Right: Mutual Dependence Network ===

        # Create a more complex interdependence network
        elements = ['水', '火', '木', '土', '金', '人', '動物', '植物']
        G2 = nx.DiGraph()

        # Interdependence relations
        relations = [
            ('水', '植物'), ('水', '動物'), ('水', '人'),
            ('火', '人'), ('火', '土'),
            ('木', '火'), ('木', '人'),
            ('土', '植物'), ('土', '木'),
            ('金', '人'), ('金', '水'),
            ('人', '火'), ('人', '木'), ('人', '金'),
            ('動物', '人'), ('動物', '土'),
            ('植物', '動物'), ('植物', '人'), ('植物', '土'),
            ('植物', '水'),  # cycle
            ('動物', '水'),  # cycle
        ]

        G2.add_edges_from(relations)

        # Force-directed layout
        pos2 = nx.spring_layout(G2, k=2, iterations=50, seed=42)

        # Draw
        nx.draw_networkx_nodes(G2, pos2, node_color='lightblue',
                              node_size=2000, alpha=0.8,
                              edgecolors='darkblue', linewidths=2, ax=ax2)

        nx.draw_networkx_labels(G2, pos2, font_size=12,
                               font_weight='bold', ax=ax2)

        nx.draw_networkx_edges(G2, pos2, edge_color='gray', alpha=0.5,
                              arrows=True, arrowsize=15, arrowstyle='->',
                              width=1.5, connectionstyle='arc3,rad=0.2', ax=ax2)

        ax2.set_title('万物の相互依存\n「一切の法は互いに因縁」',
                     fontsize=14, fontweight='bold')
        ax2.axis('off')

        ax2.text(0.5, -0.1, '独立自存するものは何もない\nすべての要素は他の要素に依存する',
                ha='center', fontsize=11, transform=ax2.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        plt.tight_layout()
        plt.savefig('dependent_origination_network.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【縁起：此れ有るが故に彼れ有り】")
        print("="*70)

        print("\n釈尊の教え：")
        print("  「此れ有るが故に彼れ有り、此れ生ずるが故に彼れ生ず。」")
        print("  「此れ無きが故に彼れ無く、此れ滅するが故に彼れ滅す。」")

        print("\nその意味：")
        print("  - これが存在するから、あれが存在する")
        print("  - これが存在しないから、あれも存在しない")
        print("  - 一切の法は互いに因縁である")
        print("  - 独立自存するものは何もない")

        print("\n十二因縁：")
        print("  1. 無明（根本的無知）")
        print("  2. 行（意志的形成作用）")
        print("  3. 識（意識）")
        print("  4. 名色（精神と物質）")
        print("  5. 六処（六根）")
        print("  6. 触（接触）")
        print("  7. 受（感受）")
        print("  8. 愛（渇愛）")
        print("  9. 取（取着）")
        print("  10. 有（存在）")
        print("  11. 生（誕生）")
        print("  12. 老死（老いと死）")

        print("\n鍵となる洞察：")
        print("  - 各支は前の支に依存する")
        print("  - 任意の一支を断てば → 全鎖が崩壊する")
        print("  - 無明滅すれば → 行滅す → ... → 老死滅す")
        print("  - これが涅槃である")

        print("\n現代の例：")
        print("  - 水は水素と酸素に依存する")
        print("  - 植物は水・日光・土壌に依存する")
        print("  - 動物は植物に依存する")
        print("  - 人は動物・植物・水…に依存する")
        print("  - 一切は互いに依存し合っている")

        print("\n哲学的意義：")
        print("  - 「存在する」とは絶対的なものではない")
        print("  - 「存在する」とは相対的で依存的なものである")
        print("  - 独立した「自性」はない")
        print("="*70)

# Execute
network = DependentOriginationNetwork()
network.visualize_twelve_links()

class QuantumEntanglementOntology:
    """
    Quantum Entanglement and Relational Ontology
    Demonstrates how parts cannot exist independently from the whole
    """

    def __init__(self):
        pass

    def visualize_entanglement_ontology(self):
        """
        Visualize the ontological implications of entanglement
        """
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Classical Substance Ontology ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')

        ax1.text(0.5, 0.95, '古典的実体存在論', ha='center',
                fontsize=14, fontweight='bold', transform=ax1.transAxes)

        # Two independent particles
        circle_A = plt.Circle((0.3, 0.5), 0.12, color='red', alpha=0.6,
                             edgecolor='black', linewidth=3)
        circle_B = plt.Circle((0.7, 0.5), 0.12, color='blue', alpha=0.6,
                             edgecolor='black', linewidth=3)
        ax1.add_patch(circle_A)
        ax1.add_patch(circle_B)

        ax1.text(0.3, 0.5, '粒子A\n自性あり', ha='center', va='center',
                fontsize=11, fontweight='bold')
        ax1.text(0.7, 0.5, '粒子B\n自性あり', ha='center', va='center',
                fontsize=11, fontweight='bold')

        ax1.text(0.5, 0.2, '粒子は独立に存在\n固定した属性を持つ', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
                transform=ax1.transAxes)

        # === Panel 2: Quantum Relational Ontology ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')

        ax2.text(0.5, 0.95, '量子的関係存在論', ha='center',
                fontsize=14, fontweight='bold', transform=ax2.transAxes)

        # Entangled state: the whole
        ellipse = plt.matplotlib.patches.Ellipse((0.5, 0.5), 0.7, 0.4,
                                                 color='purple', alpha=0.3,
                                                 edgecolor='purple', linewidth=3)
        ax2.add_patch(ellipse)

        circle_A2 = plt.Circle((0.35, 0.5), 0.08, color='red', alpha=0.5,
                              edgecolor='red', linewidth=2)
        circle_B2 = plt.Circle((0.65, 0.5), 0.08, color='blue', alpha=0.5,
                              edgecolor='blue', linewidth=2)
        ax2.add_patch(circle_A2)
        ax2.add_patch(circle_B2)

        ax2.text(0.35, 0.5, 'A', ha='center', va='center',
                fontsize=12, fontweight='bold')
        ax2.text(0.65, 0.5, 'B', ha='center', va='center',
                fontsize=12, fontweight='bold')

        ax2.annotate('', xy=(0.62, 0.5), xytext=(0.38, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))

        ax2.text(0.5, 0.7, 'もつれ状態\n|ψ⟩_AB', ha='center', va='center',
                fontsize=12, fontweight='bold', color='purple')

        ax2.text(0.5, 0.2, 'AとBは分離不可能\n部分を独立に定義できない', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7),
                transform=ax2.transAxes)

        # === Panel 3: Buddhist Dependent Origination Ontology ===
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')

        ax3.text(0.5, 0.95, '仏教の縁起存在論', ha='center',
                fontsize=14, fontweight='bold', transform=ax3.transAxes)

        rect = plt.Rectangle((0.15, 0.3), 0.7, 0.4,
                            facecolor='gold', alpha=0.2,
                            edgecolor='gold', linewidth=3)
        ax3.add_patch(rect)

        elements = [
            (0.25, 0.55, '法1'),
            (0.4, 0.45, '法2'),
            (0.55, 0.6, '法3'),
            (0.7, 0.5, '法4'),
        ]

        for x, y, label in elements:
            circle = plt.Circle((x, y), 0.05, color='orange', alpha=0.6,
                               edgecolor='darkorange', linewidth=1.5)
            ax3.add_patch(circle)
            ax3.text(x, y, label, ha='center', va='center', fontsize=9)

        for i, (x1, y1, _) in enumerate(elements):
            for x2, y2, _ in elements[i+1:]:
                ax3.plot([x1, x2], [y1, y2], 'orange', alpha=0.3, linewidth=1.5)

        ax3.text(0.5, 0.7, '法界', ha='center', va='center',
                fontsize=12, fontweight='bold', color='gold')

        ax3.text(0.5, 0.2, '諸法無自性\n一切は互いに因縁', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
                transform=ax3.transAxes)

# |         # === Panel 4: Density Matrix (Mathematics) ===
# |         ax4 = fig.add_subplot(2, 3, 4)
# |         ax4.axis('off')
# | 
# |         text = '''
# |         もつれ状態の数学：
# | 
# |         ベル状態：
# |         |ψ⟩ = (|↑↓⟩ − |↓↑⟩)/√2
# | 
# |         粒子Aの縮約密度行列：
# |         ρ_A = Tr_B(|ψ⟩⟨ψ|)
# |              = (|↑⟩⟨↑| + |↓⟩⟨↓|)/2
# | 
# |         これは混合状態であり、純粋状態ではない！
# | 
# |         意味：
# |         - 粒子Aには確定した状態がない
# |         - Aの状態は系全体ABに依存する
# |         - 部分は全体から切り離せない
# | 
# |         鍵となる洞察：
# |         関係が実体に先立つ
# |         '''
# | 
# |         ax4.text(0.1, 0.5, text, fontsize=10, va='center',
# |                 family='monospace',
# |                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
# |                          edgecolor='black', linewidth=2))
# | 
# |         # === Panel 5: Formal Structure of Dependent Origination ===
# |         ax5 = fig.add_subplot(2, 3, 5)
# |         ax5.axis('off')
# | 
# |         text2 = '''
# |         縁起の形式構造：
# | 
# |         Aが存在する → Bが存在する
# |         Bが存在する → Cが存在する
# |         Cが存在する → Aが存在する
# | 
# |         A ↔ B ↔ C ↔ A（循環）
# | 
# |         独立した起点は存在しない
# |         絶対的な「第一因」はない
# | 
# |         意味：
# |         - いかなるものにも「自性」はない
# |         - 「存在」は相対的である
# |         - 一切は条件によって有る
# | 
# |         鍵となる洞察：
# |         縁起すなわち空性
# |         '''
# | 
# |         ax5.text(0.1, 0.5, text2, fontsize=10, va='center',
# |                 family='monospace',
# |                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
# |                          edgecolor='black', linewidth=2))
# | 
# |         # === Panel 6: Summary Comparison ===
# |         ax6 = fig.add_subplot(2, 3, 6)
# |         ax6.axis('off')
# | 
# |         comparison = '''
# |         【量子もつれ vs 縁起】
# | 
# |         量子もつれ状態：
# |         - 分解不可能
# |         - 部分を独立に定義できない
# |         - 関係が実体に先立つ
# |         - 全体は部分の和を超える
# | 
# |         仏教の縁起：
# |         - 互いに因縁
# |         - 諸法無自性
# |         - 縁起が存在に先立つ
# |         - 法界は分割不可能な一体
# | 
# |         共通構造：
# |         * 実体存在論に反対
# |         * 関係存在論を主張
# |         * 「存在」は相対的
# |         * 部分は全体に依存する
# | 
# |         深い洞察：
# |         宇宙は「実体の集合」ではなく
# |         「関係のネットワーク」である
# |         '''
# | 
# |         ax6.text(0.1, 0.5, comparison, fontsize=10, va='center',
# |                 bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9,
# |                          edgecolor='black', linewidth=2))
# | 
# |         plt.tight_layout()
# |         plt.savefig('entanglement_ontology.png', dpi=300, bbox_inches='tight')
# |         plt.show()

        print("\n" + "="*70)
        print("【関係存在論：量子と縁起の共通洞察】")
        print("="*70)

        print("\n古典的存在論（実体論）：")
        print("  - 宇宙は「実体」から成る")
        print("  - 実体は「属性」を持つ")
        print("  - 関係は二次的である")
        print("  - 部分は独立に定義できる")

        print("\n量子的存在論（関係論）：")
        print("  - 宇宙は「関係のネットワーク」である")
        print("  - 独立した「実体」は存在しない")
        print("  - 関係が実体に先立つ")
        print("  - 部分は全体に依存する")

        print("\nもつれ状態の数学的証明：")
        print("  - |ψ⟩_AB は |ψ⟩_A ⊗ |ψ⟩_B に分解できない")
        print("  - 粒子Aの状態は混合状態であり、純粋状態ではない")
        print("  - ρ_A = Tr_B(|ψ⟩⟨ψ|)")
        print("  → 部分を独立に定義することはできない")

        print("\n縁起の形式構造：")
        print("  - 此れ有るが故に彼れ有り")
        print("  - A → B → C → A（循環）")
        print("  - 独立した起点は存在しない")
        print("  → 諸法無自性")

        print("\n共通の洞察：")
        print("  - 「固定した本質」は幻覚である")
        print("  - 「独立した実体」は存在しない")
        print("  - 宇宙は分割不可能な全体である")
        print("  - 関係が実在を構成する")
        print("="*70)

# Execute
ontology = QuantumEntanglementOntology()
ontology.visualize_entanglement_ontology()

def visualize_emptiness_superposition():
    """
    Visualize the correspondence between Emptiness and Superposition
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Panel 1: Eternalism (Being) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '常見（有）', ha='center',
           fontsize=14, fontweight='bold')

    # Fixed entity
    rect = plt.Rectangle((0.3, 0.4), 0.4, 0.3,
                        facecolor='blue', alpha=0.7,
                        edgecolor='black', linewidth=3)
    ax.add_patch(rect)
    ax.text(0.5, 0.55, '実体\n自性あり', ha='center', va='center',
           fontsize=12, fontweight='bold', color='white')

    ax.text(0.5, 0.2, '誤り：事物に固定した本質があると考える',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 2: Nihilism (Non-being) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '断見（無）', ha='center',
           fontsize=14, fontweight='bold')

    # Void
    ax.text(0.5, 0.55, '空無\n何も存在しない', ha='center', va='center',
           fontsize=14, fontweight='bold', color='gray')

    ax.text(0.5, 0.2, '誤り：一切は存在しないと考える',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Panel 3: Middle Way (Emptiness = Dependent Origination) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '中道：空＝縁起', ha='center',
           fontsize=14, fontweight='bold')

    # Interdependent network
    nodes = [
        (0.3, 0.6), (0.5, 0.7), (0.7, 0.6),
        (0.3, 0.4), (0.5, 0.5), (0.7, 0.4),
    ]

    for x, y in nodes:
        circle = plt.Circle((x, y), 0.05, color='green', alpha=0.7,
                           edgecolor='darkgreen', linewidth=2)
        ax.add_patch(circle)

    # Connections
    for i, (x1, y1) in enumerate(nodes):
        for x2, y2 in nodes[i+1:]:
            distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
            if distance < 0.3:
                ax.plot([x1, x2], [y1, y2], 'green', alpha=0.4, linewidth=2)

    ax.text(0.5, 0.25, '正解：事物は因縁によって有る\n非有非無',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === Panel 4: Quantum Superposition ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '量子重ね合わせ状態', ha='center',
           fontsize=14, fontweight='bold')

    # Superposition diagram
    circle_0 = plt.Circle((0.35, 0.55), 0.1, color='red', alpha=0.5,
                         edgecolor='red', linewidth=2)
    circle_1 = plt.Circle((0.65, 0.55), 0.1, color='blue', alpha=0.5,
                         edgecolor='blue', linewidth=2)
    ax.add_patch(circle_0)
    ax.add_patch(circle_1)

    ax.text(0.35, 0.55, '|0⟩', ha='center', va='center',
           fontsize=14, fontweight='bold')
    ax.text(0.65, 0.55, '|1⟩', ha='center', va='center',
           fontsize=14, fontweight='bold')

    # Double arrow
    ax.annotate('', xy=(0.62, 0.55), xytext=(0.38, 0.55),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.6, '+', ha='center', fontsize=16, fontweight='bold')

    ax.text(0.5, 0.4, '|ψ⟩ = α|0⟩ + β|1⟩', ha='center',
           fontsize=11, fontweight='bold', color='purple')

    ax.text(0.5, 0.25, '|0⟩でも|1⟩でもない\nしかし「何でもない」わけでもない',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7))

    # Main title
    fig.text(0.5, 0.98, '龍樹の「空」と量子重ね合わせ状態の対応',
            ha='center', fontsize=16, fontweight='bold')

    # Bottom explanation
    explanation = '''
    龍樹の中観：非有非無、二元対立を超越する
    量子重ね合わせ状態：|0⟩でも|1⟩でもない、古典論理を超越する
    共通点：「固定した本質」という思考を超越する
    '''

    fig.text(0.5, 0.02, explanation, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.1)
    plt.savefig('emptiness_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【龍樹の「空」と量子重ね合わせ状態】")
    print("="*70)

    print("\n龍樹は両辺を破斥する：")
    print("  1. 常見（有）：事物に固定した本質があると考える")
    print("     → 誤り！なぜなら一切は変化しているから")
    print("  2. 断見（無）：一切は存在しないと考える")
    print("     → 誤り！なぜなら私たちは明らかに世界を経験しているから")

    print("\n龍樹の結論：中道")
    print("  - 事物は「有ではない」（固定した本質はない）")
    print("  - 事物は「無ではない」（完全に存在しないわけでもない）")
    print("  - 事物は「縁起である」（因縁によって有る）")

    print("\n量子重ね合わせ状態：")
    print("  - |ψ⟩ = α|0⟩ + β|1⟩")
    print("  - 「|0⟩ではない」（|0⟩に確定しているのではない）")
    print("  - 「|1⟩ではない」（|1⟩に確定しているのではない）")
    print("  - 「何でもないのでもない」（重ね合わせ状態は実在する）")

    print("\n対応：")
    print("  常見（有） ≈ 古典状態（|0⟩または|1⟩）")
    print("  断見（無） ≈ 虚無（状態がない）")
    print("  中道（空＝縁起） ≈ 重ね合わせ状態（α|0⟩+β|1⟩）")

    print("\n共通構造：")
    print("  - いずれも二元対立を超越する")
    print("  - いずれも「固定した本質」を否定する")
    print("  - いずれも「依存性」を主張する")

    print("\n龍樹の四句否定：")
    print("  任意の命題Pに対して：")
    print("  1. Pは真か？ → 否")
    print("  2. Pは偽か？ → 否")
    print("  3. Pは真かつ偽か？ → 否")
    print("  4. Pは真でも偽でもないか？ → 否")
    print("  → 概念を超越し、実相を直指する")

    print("\n深い洞察：")
    print("  古典論理：有か無か、二者択一")
    print("  量子論理：重ね合わせ、二元を超越する")
    print("  龍樹の論理：中道、有無を超越する")
    print("="*70)

# Execute
visualize_emptiness_superposition()

def visualize_indra_net_holographic():
    """
    Holographic nature of Indra's Net and quantum entanglement
    """

    fig = plt.figure(figsize=(18, 10))

    # === Left: Indra's Net (3D) ===
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')

    # Create 3D grid
    n = 4
    positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                positions.append((i, j, k))

    positions = np.array(positions)

    # Draw jewels
    ax1.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='gold', s=200, edgecolors='black', linewidth=1.5,
               alpha=0.8)

    # Highlight one jewel
    highlight = np.array([1, 1, 1])
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3,
               zorder=10)

    # Connect to neighbors
    for pos in positions:
        distance = np.linalg.norm(pos - highlight)
        if 0 < distance <= 1.5:
            ax1.plot([highlight[0], pos[0]],
                    [highlight[1], pos[1]],
                    [highlight[2], pos[2]],
                    'r-', alpha=0.5, linewidth=2)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('因陀羅網：各珠が一切を映し出す\n一珠を変えれば全網が動く',
                 fontsize=14, fontweight='bold')

    # === Right: Entanglement Network and Holography ===
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.axis('off')

    # Create entanglement network
    G = nx.complete_graph(8)
    pos = nx.circular_layout(G)

    # Draw all connections (entanglement)
    nx.draw_networkx_edges(G, pos, edge_color='lightblue', alpha=0.3,
                          width=2, ax=ax2)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=800,
                          edgecolors='darkblue', linewidths=2,
                          alpha=0.8, ax=ax2)

    # Labels
    labels = {i: f'粒子{i+1}' for i in range(8)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10,
                           font_weight='bold', ax=ax2)

    # Highlight one node
    nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color='red',
                          node_size=1000, edgecolors='black',
                          linewidths=3, ax=ax2)

    # Bold edges from this node
    edges_from_0 = [(0, i) for i in range(1, 8)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_from_0,
                          edge_color='red', alpha=0.7, width=3, ax=ax2)

    ax2.set_title('量子もつれネットワーク：全息構造\n各粒子が系全体の情報を含む',
                 fontsize=14, fontweight='bold')

# |     # Bottom explanation
# |     explanation = '''
# |     因陀羅網（華厳宗）：
# |     - 各珠がすべての珠を映し出す
# |     - 一珠を変えれば、全網が変わる
# |     - 部分が全体を含む
# |     - 重重無尽
# | 
# |     量子もつれネットワーク：
# |     - 各粒子がすべての粒子ともつれる
# |     - 一粒子を測定すれば、すべての粒子に影響する
# |     - 部分が全体の情報を含む（全息性）
# |     - 非局所的相関
# | 
# |     共通の洞察：
# |     * 宇宙は分割不可能な全体である
# |     * 部分と全体は不可分である
# |     * 一即一切、一切即一
# |     * 関係が実在を構成する
# |     '''
# | 
# |     fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
# |             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
# | 
# |     plt.tight_layout()
# |     plt.subplots_adjust(bottom=0.25)
# |     plt.savefig('indra_net_holographic.png', dpi=300, bbox_inches='tight')
# |     plt.show()

    print("\n" + "="*70)
    print("【因陀羅網と量子全息性】")
    print("="*70)

    print("\n華厳宗の因陀羅網：")
    print("  - 帝釈天の宮殿に張られた宝網")
    print("  - 各交点に一つの宝珠がある")
    print("  - 各珠が他のすべての珠を映し出す")
    print("  - 各映像がさらにすべての珠を映す")
    print("  - 無限に再帰する——重重無尽")

    print("\n量子もつれの全息性：")
    print("  - もつれ状態：|ψ⟩_AB は分解できない")
    print("  - 粒子Aを測定 → 瞬時に粒子Bに影響")
    print("  - 各粒子が系全体の情報を含む")
    print("  - 部分は全体から切り離せない")

    print("\nホログラフィック原理（Holographic Principle）：")
    print("  - 物理学の重要概念")
    print("  - ある領域の情報はその境界上に符号化できる")
    print("  - 体積の情報 ＝ 表面の情報")
    print("  - 3次元宇宙は2次元ホログラムかもしれない")

    print("\n縁起の全息性：")
    print("  - 此れ有るが故に彼れ有り")
    print("  - 一切は互いに因縁である")
    print("  - 一法を変えれば、一切の法が変わる")
    print("  - 法界は分割不可能な全体である")

    print("\n究極の洞察：")
    print("  宇宙は「部分の集合」ではなく")
    print("  「分割不可能な全体」である")
    print("  「分離」は幻覚にすぎない")
    print("  「一」こそが真相である")
    print("="*70)

# Execute
visualize_indra_net_holographic()
