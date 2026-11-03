# Code & Cogito: 量子糾纏態 vs 佛教「緣起」——萬物互為因緣
# Article: https://code-cogito.com/quantum-entanglement-dependent-origination/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class DependentOriginationNetwork:
    """
    緣起網絡模擬器
    展示：萬物如何互為因緣
    """

    def __init__(self):
        self.G = nx.DiGraph()

    def create_twelve_links(self):
        """
        創建十二因緣網絡
        """
        # 十二支
        links = [
            ('無明', '行'),
            ('行', '識'),
            ('識', '名色'),
            ('名色', '六入'),
            ('六入', '觸'),
            ('觸', '受'),
            ('受', '愛'),
            ('愛', '取'),
            ('取', '有'),
            ('有', '生'),
            ('生', '老死'),
            ('老死', '無明'),  # 循環
        ]

        self.G.add_edges_from(links)

    def visualize_twelve_links(self):
        """
        視覺化十二因緣
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

        # === 左圖：十二因緣環 ===
        self.create_twelve_links()

        # 圓形佈局
        pos = nx.circular_layout(self.G)

        # 節點顏色（根據類別）
        node_colors = {
            '無明': 'gray',
            '行': 'orange',
            '識': 'yellow',
            '名色': 'lightblue',
            '六入': 'lightgreen',
            '觸': 'cyan',
            '受': 'pink',
            '愛': 'red',
            '取': 'darkred',
            '有': 'purple',
            '生': 'green',
            '老死': 'black',
        }

        colors = [node_colors[node] for node in self.G.nodes()]

        # 繪製網絡
        nx.draw_networkx_nodes(self.G, pos, node_color=colors,
                              node_size=1500, alpha=0.8,
                              edgecolors='black', linewidths=2, ax=ax1)

        nx.draw_networkx_labels(self.G, pos, font_size=12,
                               font_weight='bold', ax=ax1)

        nx.draw_networkx_edges(self.G, pos, edge_color='gray',
                              arrows=True, arrowsize=20, arrowstyle='->',
                              width=2, connectionstyle='arc3,rad=0.1', ax=ax1)

        ax1.set_title('十二因緣：輪迴的機制\n「此有故彼有，此生故彼生」',
                     fontsize=14, fontweight='bold')
        ax1.axis('off')

        # 添加說明
        explanation = '''
        十二因緣：

        1. 無明 → 2. 行 → 3. 識
        → 4. 名色 → 5. 六入 → 6. 觸
        → 7. 受 → 8. 愛 → 9. 取
        → 10. 有 → 11. 生 → 12. 老死
        → 1. 無明（循環）

        破除任何一支 → 整個鏈斷裂
        '''

        ax1.text(0.5, -1.3, explanation, ha='center', fontsize=10,
                transform=ax1.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === 右圖：相互依存網絡 ===

        # 創建更複雜的相互依存網絡
        elements = ['水', '火', '木', '土', '金', '人', '動物', '植物']
        G2 = nx.DiGraph()

        # 相互依存關係
        relations = [
            ('水', '植物'), ('水', '動物'), ('水', '人'),
            ('火', '人'), ('火', '土'),
            ('木', '火'), ('木', '人'),
            ('土', '植物'), ('土', '木'),
            ('金', '人'), ('金', '水'),
            ('人', '火'), ('人', '木'), ('人', '金'),
            ('動物', '人'), ('動物', '土'),
            ('植物', '動物'), ('植物', '人'), ('植物', '土'),
            ('植物', '水'),  # 循環
            ('動物', '水'),  # 循環
        ]

        G2.add_edges_from(relations)

        # 春天佈局（force-directed）
        pos2 = nx.spring_layout(G2, k=2, iterations=50, seed=42)

        # 繪製
        nx.draw_networkx_nodes(G2, pos2, node_color='lightblue',
                              node_size=2000, alpha=0.8,
                              edgecolors='darkblue', linewidths=2, ax=ax2)

        nx.draw_networkx_labels(G2, pos2, font_size=12,
                               font_weight='bold', ax=ax2)

        nx.draw_networkx_edges(G2, pos2, edge_color='gray', alpha=0.5,
                              arrows=True, arrowsize=15, arrowstyle='->',
                              width=1.5, connectionstyle='arc3,rad=0.2', ax=ax2)

        ax2.set_title('萬物相互依存\n「一切法互為因緣」',
                     fontsize=14, fontweight='bold')
        ax2.axis('off')

        ax2.text(0.5, -0.1, '沒有獨立自存的事物\n每個元素依賴其他元素',
                ha='center', fontsize=11, transform=ax2.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        plt.tight_layout()
        plt.savefig('dependent_origination_network.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【緣起：此有故彼有】")
        print("="*70)

        print("\n佛陀的教導：")
        print("  「此有故彼有，此生故彼生。」")
        print("  「此無故彼無，此滅故彼滅。」")

        print("\n意思：")
        print("  - 因為這個存在，那個才存在")
        print("  - 因為這個不存在，那個就不存在")
        print("  - 一切法互為因緣")
        print("  - 沒有獨立自存的事物")

        print("\n十二因緣：")
        print("  1. 無明（無知）")
        print("  2. 行（造作）")
        print("  3. 識（意識）")
        print("  4. 名色（精神-物質）")
        print("  5. 六入（六根）")
        print("  6. 觸（接觸）")
        print("  7. 受（感受）")
        print("  8. 愛（渴愛）")
        print("  9. 取（抓取）")
        print("  10. 有（存在）")
        print("  11. 生（出生）")
        print("  12. 老死（衰老死亡）")

        print("\n關鍵洞見：")
        print("  - 每一支依賴前一支")
        print("  - 破除任何一支 → 整個鏈斷裂")
        print("  - 無明滅 → 行滅 → ... → 老死滅")
        print("  - 這就是涅槃")

        print("\n現代例子：")
        print("  - 水依賴氫和氧")
        print("  - 植物依賴水、陽光、土壤")
        print("  - 動物依賴植物")
        print("  - 人依賴動物、植物、水...")
        print("  - 一切互相依存")

        print("\n哲學意義：")
        print("  - 「存在」不是絕對的")
        print("  - 「存在」是相對的、依賴的")
        print("  - 沒有獨立的「自性」")
        print("="*70)

# 執行
network = DependentOriginationNetwork()
network.visualize_twelve_links()

class QuantumEntanglementOntology:
    """
    量子糾纏態與關係本體論
    展示：部分如何無法脫離整體
    """

    def __init__(self):
        pass

    def visualize_entanglement_ontology(self):
        """
        視覺化糾纏態的本體論意義
        """
        fig = plt.figure(figsize=(18, 12))

        # === 圖1：經典實體本體論 ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')

        ax1.text(0.5, 0.95, '經典實體本體論', ha='center',
                fontsize=14, fontweight='bold', transform=ax1.transAxes)

        # 兩個獨立的粒子
        circle_A = plt.Circle((0.3, 0.5), 0.12, color='red', alpha=0.6,
                             edgecolor='black', linewidth=3)
        circle_B = plt.Circle((0.7, 0.5), 0.12, color='blue', alpha=0.6,
                             edgecolor='black', linewidth=3)
        ax1.add_patch(circle_A)
        ax1.add_patch(circle_B)

        ax1.text(0.3, 0.5, '粒子A\n有自性', ha='center', va='center',
                fontsize=11, fontweight='bold')
        ax1.text(0.7, 0.5, '粒子B\n有自性', ha='center', va='center',
                fontsize=11, fontweight='bold')

        ax1.text(0.5, 0.2, '粒子獨立存在\n有固定屬性', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
                transform=ax1.transAxes)

        # === 圖2：量子關係本體論 ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')

        ax2.text(0.5, 0.95, '量子關係本體論', ha='center',
                fontsize=14, fontweight='bold', transform=ax2.transAxes)

        # 糾纏態：整體
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

        ax2.text(0.5, 0.7, '糾纏態\n|psi>_AB', ha='center', va='center',
                fontsize=12, fontweight='bold', color='purple')

        ax2.text(0.5, 0.2, 'A和B不可分離\n部分無法獨立定義', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7),
                transform=ax2.transAxes)

        # === 圖3：緣起本體論 ===
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')

        ax3.text(0.5, 0.95, '佛教緣起本體論', ha='center',
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

        ax3.text(0.5, 0.2, '諸法無自性\n一切互為因緣', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
                transform=ax3.transAxes)

        # === 圖4：密度矩陣（數學）===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        text = '''
        糾纏態的數學：

        貝爾態：
        |psi> = (|up,down> - |down,up>)/sqrt(2)

        粒子A的約化密度矩陣：
        rho_A = Tr_B(|psi><psi|)
             = (|up><up| + |down><down|)/2

        這是混合態，不是純態！

        意義：
        - 粒子A沒有確定的狀態
        - A的狀態依賴整個系統AB
        - 部分無法脫離整體

        關鍵洞見：
        關係先於實體
        '''

        ax4.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        # === 圖5：緣起的數學結構 ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')

        text2 = '''
        緣起的形式結構：

        若A存在 -> B存在
        若B存在 -> C存在
        若C存在 -> A存在

        A <-> B <-> C <-> A（循環）

        沒有獨立的起點
        沒有絕對的「第一因」

        意義：
        - 沒有事物有「自性」
        - 「存在」是相對的
        - 一切依條件而有

        關鍵洞見：
        緣起即空性
        '''

        ax5.text(0.1, 0.5, text2, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        # === 圖6：對應總結 ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        comparison = '''
        【量子糾纏 vs 緣起】

        量子糾纏態：
        - 不可分解
        - 部分無法獨立定義
        - 關係先於實體
        - 整體大於部分之和

        佛教緣起：
        - 互為因緣
        - 諸法無自性
        - 緣起先於存在
        - 法界是不可分割的一體

        共同結構：
        * 反對實體本體論
        * 主張關係本體論
        * 「存在」是相對的
        * 部分依賴整體

        深刻洞見：
        宇宙不是「實體的集合」
        而是「關係的網絡」
        '''

        ax6.text(0.1, 0.5, comparison, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9,
                         edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('entanglement_ontology.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【關係本體論：量子與緣起的共同洞見】")
        print("="*70)

        print("\n經典本體論（實體論）：")
        print("  - 宇宙由「實體」組成")
        print("  - 實體有「屬性」")
        print("  - 關係是次要的")
        print("  - 部分可以獨立定義")

        print("\n量子本體論（關係論）：")
        print("  - 宇宙是「關係的網絡」")
        print("  - 沒有獨立的「實體」")
        print("  - 關係先於實體")
        print("  - 部分依賴整體")

        print("\n糾纏態的數學證明：")
        print("  - |psi>_AB 不能分解為 |psi>_A tensor |psi>_B")
        print("  - 粒子A的狀態是混合態，不是純態")
        print("  - rho_A = Tr_B(|psi><psi|)")
        print("  -> 部分無法獨立定義")

        print("\n緣起的形式結構：")
        print("  - 此有故彼有")
        print("  - A -> B -> C -> A（循環）")
        print("  - 沒有獨立的起點")
        print("  -> 諸法無自性")

        print("\n共同洞見：")
        print("  - 「固定本質」是幻覺")
        print("  - 「獨立實體」不存在")
        print("  - 宇宙是不可分割的整體")
        print("  - 關係構成實在")
        print("="*70)

# 執行
ontology = QuantumEntanglementOntology()
ontology.visualize_entanglement_ontology()

def visualize_emptiness_superposition():
    """
    視覺化「空」與疊加態的對應
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === 圖1：常見（有）===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '常見（有）', ha='center',
           fontsize=14, fontweight='bold')

    # 固定的實體
    rect = plt.Rectangle((0.3, 0.4), 0.4, 0.3,
                        facecolor='blue', alpha=0.7,
                        edgecolor='black', linewidth=3)
    ax.add_patch(rect)
    ax.text(0.5, 0.55, '實體\n有自性', ha='center', va='center',
           fontsize=12, fontweight='bold', color='white')

    ax.text(0.5, 0.2, '錯誤：認為事物有固定本質',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === 圖2：斷見（無）===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '斷見（無）', ha='center',
           fontsize=14, fontweight='bold')

    # 空無
    ax.text(0.5, 0.55, '空無\n什麼都沒有', ha='center', va='center',
           fontsize=14, fontweight='bold', color='gray')

    ax.text(0.5, 0.2, '錯誤：認為一切不存在',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === 圖3：中道（空=緣起）===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '中道：空=緣起', ha='center',
           fontsize=14, fontweight='bold')

    # 相互依存的網絡
    nodes = [
        (0.3, 0.6), (0.5, 0.7), (0.7, 0.6),
        (0.3, 0.4), (0.5, 0.5), (0.7, 0.4),
    ]

    for x, y in nodes:
        circle = plt.Circle((x, y), 0.05, color='green', alpha=0.7,
                           edgecolor='darkgreen', linewidth=2)
        ax.add_patch(circle)

    # 連線
    for i, (x1, y1) in enumerate(nodes):
        for x2, y2 in nodes[i+1:]:
            distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
            if distance < 0.3:
                ax.plot([x1, x2], [y1, y2], 'green', alpha=0.4, linewidth=2)

    ax.text(0.5, 0.25, '正確：事物依因緣而有\n非有非無',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === 圖4：量子疊加態 ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '量子疊加態', ha='center',
           fontsize=14, fontweight='bold')

    # 疊加態圖示
    circle_0 = plt.Circle((0.35, 0.55), 0.1, color='red', alpha=0.5,
                         edgecolor='red', linewidth=2)
    circle_1 = plt.Circle((0.65, 0.55), 0.1, color='blue', alpha=0.5,
                         edgecolor='blue', linewidth=2)
    ax.add_patch(circle_0)
    ax.add_patch(circle_1)

    ax.text(0.35, 0.55, '|0>', ha='center', va='center',
           fontsize=14, fontweight='bold')
    ax.text(0.65, 0.55, '|1>', ha='center', va='center',
           fontsize=14, fontweight='bold')

    # 雙箭頭
    ax.annotate('', xy=(0.62, 0.55), xytext=(0.38, 0.55),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.6, '+', ha='center', fontsize=16, fontweight='bold')

    ax.text(0.5, 0.4, '|psi> = a|0> + b|1>', ha='center',
           fontsize=11, fontweight='bold', color='purple')

    ax.text(0.5, 0.25, '非|0>非|1>\n但也非「什麼都不是」',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7))

    # 總標題
    fig.text(0.5, 0.98, '龍樹的「空」與量子疊加態的對應',
            ha='center', fontsize=16, fontweight='bold')

    # 底部說明
    explanation = '''
    龍樹的中觀：非有非無，超越二元對立
    量子疊加態：非|0>非|1>，超越經典邏輯
    共同點：超越「固定本質」的思維
    '''

    fig.text(0.5, 0.02, explanation, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.1)
    plt.savefig('emptiness_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【龍樹的「空」與量子疊加態】")
    print("="*70)

    print("\n龍樹破斥兩邊：")
    print("  1. 常見（有）：認為事物有固定本質")
    print("     -> 錯！因為一切在變化")
    print("  2. 斷見（無）：認為一切不存在")
    print("     -> 錯！因為我們明顯經驗到世界")

    print("\n龍樹的結論：中道")
    print("  - 事物「非有」（沒有固定本質）")
    print("  - 事物「非無」（不是完全不存在）")
    print("  - 事物「是緣起」（依因緣而有）")

    print("\n量子疊加態：")
    print("  - |psi> = a|0> + b|1>")
    print("  - 「非|0>」（不是確定在|0>）")
    print("  - 「非|1>」（不是確定在|1>）")
    print("  - 「也非什麼都不是」（疊加態是真實的）")

    print("\n對應：")
    print("  常見（有） ~ 經典態（|0>或|1>）")
    print("  斷見（無） ~ 虛無（沒有狀態）")
    print("  中道（空=緣起） ~ 疊加態（a|0>+b|1>）")

    print("\n共同結構：")
    print("  - 都超越二元對立")
    print("  - 都反對「固定本質」")
    print("  - 都主張「依賴性」")

    print("\n龍樹的四句否定：")
    print("  對於命題P：")
    print("  1. P是真的？ -> 不是")
    print("  2. P是假的？ -> 不是")
    print("  3. P既真又假？ -> 不是")
    print("  4. P既非真也非假？ -> 不是")
    print("  -> 超越概念，直指實相")

    print("\n深刻洞見：")
    print("  古典邏輯：有或無，二選一")
    print("  量子邏輯：疊加，超越二元")
    print("  龍樹邏輯：中道，超越有無")
    print("="*70)

# 執行
visualize_emptiness_superposition()

def visualize_indra_net_holographic():
    """
    因陀羅網的全息性與量子糾纏
    """

    fig = plt.figure(figsize=(18, 10))

    # === 左圖：因陀羅網（3D）===
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')

    # 創建3D網格
    n = 4
    positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                positions.append((i, j, k))

    positions = np.array(positions)

    # 繪製珠子
    ax1.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='gold', s=200, edgecolors='black', linewidth=1.5,
               alpha=0.8)

    # 高亮一個珠子
    highlight = np.array([1, 1, 1])
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3,
               zorder=10)

    # 連線到鄰居
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
    ax1.set_title('因陀羅網：每顆珠子映現一切\n改變一珠，全網皆動',
                 fontsize=14, fontweight='bold')

    # === 右圖：糾纏網絡與全息性 ===
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.axis('off')

    # 創建糾纏網絡
    G = nx.complete_graph(8)
    pos = nx.circular_layout(G)

    # 繪製所有連接（糾纏）
    nx.draw_networkx_edges(G, pos, edge_color='lightblue', alpha=0.3,
                          width=2, ax=ax2)

    # 繪製節點
    nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=800,
                          edgecolors='darkblue', linewidths=2,
                          alpha=0.8, ax=ax2)

    # 標籤
    labels = {i: f'粒子{i+1}' for i in range(8)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10,
                           font_weight='bold', ax=ax2)

    # 高亮一個節點
    nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color='red',
                          node_size=1000, edgecolors='black',
                          linewidths=3, ax=ax2)

    # 加粗從此節點出發的連接
    edges_from_0 = [(0, i) for i in range(1, 8)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_from_0,
                          edge_color='red', alpha=0.7, width=3, ax=ax2)

    ax2.set_title('量子糾纏網絡：全息結構\n每個粒子包含整個系統信息',
                 fontsize=14, fontweight='bold')

    # 底部說明
    explanation = '''
    因陀羅網（華嚴宗）：
    - 每顆珠子映現所有珠子
    - 改變一珠，全網改變
    - 部分包含整體
    - 重重無盡

    量子糾纏網絡：
    - 每個粒子與所有粒子糾纏
    - 測量一個粒子，影響所有粒子
    - 部分包含整體信息（全息性）
    - 非局域關聯

    共同洞見：
    * 宇宙是不可分割的整體
    * 部分與整體不可分
    * 一即一切，一切即一
    * 關係構成實在
    '''

    fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)
    plt.savefig('indra_net_holographic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【因陀羅網與量子全息性】")
    print("="*70)

    print("\n華嚴宗的因陀羅網：")
    print("  - 帝釋天宮的寶網")
    print("  - 每個交點有一顆寶珠")
    print("  - 每顆珠子映現所有其他珠子")
    print("  - 每個映像又映現所有珠子")
    print("  - 無限遞迴，重重無盡")

    print("\n量子糾纏的全息性：")
    print("  - 糾纏態：|psi>_AB 不可分解")
    print("  - 測量粒子A -> 瞬間影響粒子B")
    print("  - 每個粒子包含整個系統的信息")
    print("  - 部分不能脫離整體")

    print("\n全息原理（Holographic Principle）：")
    print("  - 物理學的重要概念")
    print("  - 一個區域的信息可以編碼在其邊界上")
    print("  - 體積的信息 = 表面的信息")
    print("  - 3D宇宙可能是2D全息圖")

    print("\n緣起的全息性：")
    print("  - 此有故彼有")
    print("  - 一切互為因緣")
    print("  - 改變一法，一切法變")
    print("  - 法界是不可分割的整體")

    print("\n最終洞見：")
    print("  宇宙不是「部分的集合」")
    print("  而是「不可分割的整體」")
    print("  「分離」是幻覺")
    print("  「一」才是真相")
    print("="*70)

# 執行
visualize_indra_net_holographic()
