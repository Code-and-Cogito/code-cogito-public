# Code & Cogito: 測不準原理 vs 佛教的「空性」——萬物無自性
# Article: https://code-cogito.com/uncertainty-principle-buddhist-emptiness/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class UncertaintyPrinciple:
    """
    不確定性原理互動實驗
    展示：位置不確定性 vs 動量不確定性的trade-off
    """

    def __init__(self):
        self.hbar = 1.0  # 約化普朗克常數（任意單位）

    def gaussian_wavepacket(self, x, x0, sigma_x, k0):
        """
        高斯波包
        x0: 中心位置
        sigma_x: 位置標準差（不確定性）
        k0: 中心波數（對應動量 p0 = ℏk0）
        """
        return (1 / (2 * np.pi * sigma_x**2)**0.25) * \
               np.exp(-((x - x0)**2) / (4 * sigma_x**2)) * \
               np.exp(1j * k0 * x)

    def momentum_distribution(self, psi_x, dx):
        """
        從位置空間波函數計算動量空間波函數
        使用傅立葉變換
        """
        psi_k = fft(psi_x) * dx
        return psi_k

    def visualize_uncertainty(self, sigma_x_values=[0.5, 1.0, 2.0, 4.0]):
        """
        視覺化不同位置不確定性下的波包
        """
        x = np.linspace(-20, 20, 2000)
        dx = x[1] - x[0]

        fig, axes = plt.subplots(2, len(sigma_x_values), figsize=(18, 10))

        for i, sigma_x in enumerate(sigma_x_values):
            # 生成波包
            psi_x = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

            # 位置空間機率密度
            prob_x = np.abs(psi_x)**2

            # 動量空間
            psi_k = self.momentum_distribution(psi_x, dx)
            k = fftfreq(len(x), dx) * 2 * np.pi
            prob_k = np.abs(psi_k)**2

            # 重新排序（fft的輸出需要重新排列）
            k_sorted_idx = np.argsort(k)
            k_sorted = k[k_sorted_idx]
            prob_k_sorted = prob_k[k_sorted_idx]

            # 計算不確定性
            delta_x = sigma_x
            delta_k = 1 / (2 * sigma_x)
            delta_p = self.hbar * delta_k
            uncertainty_product = delta_x * delta_p

            # === 上圖：位置空間 ===
            ax = axes[0, i]
            ax.plot(x, prob_x, 'b-', linewidth=2)
            ax.fill_between(x, 0, prob_x, alpha=0.3, color='blue')
            ax.set_xlabel('位置 x', fontsize=11)
            ax.set_ylabel('|ψ(x)|²', fontsize=11)
            ax.set_title(f'位置不確定性\nΔx = {delta_x:.2f}',
                        fontsize=12, fontweight='bold', color='blue')
            ax.grid(True, alpha=0.3)
            ax.set_xlim(-15, 15)
            ax.axvspan(-delta_x, delta_x, alpha=0.2, color='cyan',
                      label=f'Δx = {delta_x:.2f}')
            ax.legend(fontsize=9)

            # === 下圖：動量空間 ===
            ax = axes[1, i]
            center_idx = len(k_sorted) // 2
            plot_range = 500
            k_plot = k_sorted[center_idx-plot_range:center_idx+plot_range]
            prob_k_plot = prob_k_sorted[center_idx-plot_range:center_idx+plot_range]

            if np.max(prob_k_plot) > 0:
                prob_k_plot = prob_k_plot / np.max(prob_k_plot)

            ax.plot(k_plot, prob_k_plot, 'r-', linewidth=2)
            ax.fill_between(k_plot, 0, prob_k_plot, alpha=0.3, color='red')
            ax.set_xlabel('波數 k (動量 p=ℏk)', fontsize=11)
            ax.set_ylabel('|ψ(k)|²', fontsize=11)
            ax.set_title(f'動量不確定性\nΔp = {delta_p:.2f}',
                        fontsize=12, fontweight='bold', color='red')
            ax.grid(True, alpha=0.3)

            color = 'green' if uncertainty_product >= self.hbar/2 else 'red'
            ax.text(0.5, 0.9,
                   f'Δx·Δp = {uncertainty_product:.3f}\n(ℏ/2 = {self.hbar/2:.3f})',
                   transform=ax.transAxes, ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor=color, alpha=0.5))

        fig.text(0.5, 0.98, '不確定性原理：Δx 越小 → Δp 越大',
                ha='center', fontsize=16, fontweight='bold')
        fig.text(0.5, 0.02,
                '關鍵洞見：這不是測量誤差，是波動的數學性質！\n'
                '你不能同時讓波包既窄（位置確定）又純（動量確定）',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(top=0.93, bottom=0.1)
        plt.savefig('uncertainty_principle_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()

    def interactive_measurement(self):
        """
        互動式測量：觀察測量順序的影響
        """
        print("\n" + "="*70)
        print("【不確定性原理互動實驗】")
        print("="*70)

        x = np.linspace(-10, 10, 1000)
        sigma_x = 1.0
        psi = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

        print("\n初始狀態：")
        print(f"  位置不確定性 Δx ≈ {sigma_x:.2f}")
        print(f"  動量不確定性 Δp ≈ {self.hbar/(2*sigma_x):.2f}")
        print(f"  不確定性乘積 Δx·Δp ≈ {sigma_x * self.hbar/(2*sigma_x):.3f}")
        print(f"  海森堡下限 ℏ/2 = {self.hbar/2:.3f}")

        print("\n實驗1：先測位置，再測動量")
        print("  → 測位置後，波函數坍縮到某個位置")
        print("  → 此時 Δx → 0，因此 Δp → ∞")
        print("  → 動量完全不確定！")

        print("\n實驗2：先測動量，再測位置")
        print("  → 測動量後，波函數變成平面波")
        print("  → 此時 Δp → 0，因此 Δx → ∞")
        print("  → 位置完全不確定！")

        print("\n結論：")
        print("  • 測量順序很重要（x̂ 和 p̂ 不對易）")
        print("  • 測量一個量會擾動另一個量")
        print("  • 不是儀器問題，是自然法則")

        print("\n佛教類比：")
        print("  • 萬物沒有固定的「自性」")
        print("  • 屬性依賴觀察方式")
        print("  • 從不同角度看，看到不同面向")
        print("="*70)

# 執行
experiment = UncertaintyPrinciple()
experiment.visualize_uncertainty(sigma_x_values=[0.5, 1.0, 2.0, 4.0])
experiment.interactive_measurement()

def visualize_emptiness():
    """
    「空性」的視覺化
    展示：事物的屬性如何依賴觀察條件
    """

    fig = plt.figure(figsize=(16, 12))

    # === 示例：「杯子」的空性 ===

    # 子圖1：不同角度看到不同形狀
    ax1 = fig.add_subplot(2, 3, 1)
    circle = plt.Circle((0.5, 0.5), 0.3, fill=False, edgecolor='blue', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.1, '從上面看：圓形', ha='center', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 子圖2：從側面看：矩形
    ax2 = fig.add_subplot(2, 3, 2)
    rect = plt.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='red', linewidth=3)
    ax2.add_patch(rect)
    ax2.text(0.5, 0.1, '從側面看：矩形', ha='center', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # 子圖3：問題
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.text(0.5, 0.5, '問：杯子的\n「真實形狀」是？\n\n答：沒有\n「固定形狀」！\n\n形狀依賴\n觀察角度',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')

    # === 量子類比：粒子的「位置」===

    # 子圖4：位置測量
    ax4 = fig.add_subplot(2, 3, 4)
    x = np.linspace(-5, 5, 1000)
    psi_position = np.exp(-x**2)
    ax4.plot(x, psi_position, 'b-', linewidth=3)
    ax4.fill_between(x, 0, psi_position, alpha=0.3, color='blue')
    ax4.set_xlabel('位置', fontsize=11)
    ax4.set_ylabel('機率', fontsize=11)
    ax4.set_title('測量「位置」\n→ 位置確定', fontsize=12, fontweight='bold', color='blue')
    ax4.grid(True, alpha=0.3)

    # 子圖5：動量測量
    ax5 = fig.add_subplot(2, 3, 5)
    k = np.linspace(-5, 5, 1000)
    psi_momentum = np.exp(-(k-2)**2/4)
    ax5.plot(k, psi_momentum, 'r-', linewidth=3)
    ax5.fill_between(k, 0, psi_momentum, alpha=0.3, color='red')
    ax5.set_xlabel('動量', fontsize=11)
    ax5.set_ylabel('機率', fontsize=11)
    ax5.set_title('測量「動量」\n→ 動量確定', fontsize=12, fontweight='bold', color='red')
    ax5.grid(True, alpha=0.3)

    # 子圖6：結論
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.text(0.5, 0.5, '問：粒子的\n「真實狀態」是？\n\n答：沒有\n「固定屬性」！\n\n屬性依賴\n測量方式',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')

    # 總標題與對應說明
    fig.text(0.5, 0.98, '「空性」與「測不準」的結構對應',
            ha='center', fontsize=16, fontweight='bold')
    fig.text(0.5, 0.02,
            '佛教：事物沒有「自性」（固定本質），屬性依條件而顯\n'
            '量子力學：粒子沒有「確定屬性」，屬性依測量而定\n'
            '共同點：「固定性」不是實在的本質',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.12)
    plt.savefig('emptiness_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 文字說明
    print("\n" + "="*70)
    print("【空性的三層意義】")
    print("="*70)

    print("\n1. 空不是「無」")
    print("   《心經》：「色即是空，空即是色」")
    print("   → 事物存在，但沒有固定本質")

    print("\n2. 空是「緣起」")
    print("   龍樹：「因緣所生法，我說即是空」")
    print("   → 一切依條件而存在")

    print("\n3. 空破「執著」")
    print("   → 沒有固定的「我」")
    print("   → 沒有固定的「物」")
    print("   → 了悟空性，放下執著")

    print("\n與測不準原理的對應：")
    print("   • 粒子沒有固定的「位置」或「動量」")
    print("   • 屬性依測量方式而定")
    print("   • 沒有獨立於觀察的「客觀屬性」")

    print("\n共同洞見：")
    print("   世界不是由「固定屬性的物體」組成")
    print("   而是由「依條件而顯的關係」組成")
    print("="*70)

# 執行
visualize_emptiness()

import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

def indras_net_quantum():
    """
    因陀羅網與量子糾纏
    展示：一切互相連結，改變一個影響全體
    """

    fig = plt.figure(figsize=(18, 12))

    # === 左圖：因陀羅網（2D網絡）===
    ax1 = fig.add_subplot(2, 2, 1)

    n = 5
    G = nx.grid_2d_graph(n, n)
    pos = {(i, j): (i, j) for i, j in G.nodes()}

    nx.draw_networkx_nodes(G, pos, node_color='gold', node_size=800,
                          edgecolors='black', linewidths=2, ax=ax1)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, ax=ax1)

    highlight_node = (2, 2)
    nx.draw_networkx_nodes(G, pos, nodelist=[highlight_node],
                          node_color='red', node_size=1000,
                          edgecolors='black', linewidths=3, ax=ax1)

    ax1.set_title('因陀羅網：每顆珠子映現一切\n改變一顆，影響全部',
                 fontsize=13, fontweight='bold')
    ax1.axis('off')
    ax1.text(2, -0.5, '華嚴宗：一即一切，一切即一',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === 右圖：量子糾纏網絡（3D）===
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')

    n_particles = 8
    positions = np.random.randn(n_particles, 3)

    ax2.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='cyan', s=300, edgecolors='black', linewidth=2, alpha=0.8)

    for i in range(n_particles):
        for j in range(i+1, n_particles):
            ax2.plot([positions[i, 0], positions[j, 0]],
                    [positions[i, 1], positions[j, 1]],
                    [positions[i, 2], positions[j, 2]],
                    'b-', alpha=0.2, linewidth=1)

    ax2.scatter([positions[0, 0]], [positions[0, 1]], [positions[0, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    ax2.set_title('量子糾纏：粒子間非局域關聯\n測量一個，影響全部',
                 fontsize=13, fontweight='bold')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

# |     # === 下左：糾纏態數學 ===
# |     ax3 = fig.add_subplot(2, 2, 3)
# |     ax3.axis('off')
# | 
# |     text = '''
# |     糾纏態（Bell態）：
# | 
# |     |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2
# | 
# |     特性：
# |     • 粒子A和B不可分離
# |     • 測量A → 立刻知道B
# |     • A的狀態無法單獨定義
# |     • 整體 ≠ 部分之和
# | 
# |     貝爾不等式（1964）：
# |     如果粒子有「定域實在性」
# |     → 應滿足某個不等式
# | 
# |     實驗結果（1982-2022）：
# |     不等式被違反！
# |     → 沒有定域實在性
# |     → 糾纏是真實的
# |     '''
# | 
# |     ax3.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
# |             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
# | 
# |     # === 下右：因陀羅網與糾纏的對應 ===
# |     ax4 = fig.add_subplot(2, 2, 4)
# |     ax4.axis('off')
# | 
# |     comparison = '''
# |     【因陀羅網 vs 量子糾纏】
# | 
# |     因陀羅網：
# |     • 每顆珠子包含整張網
# |     • 改變一珠，全網皆動
# |     • 部分即整體
# |     • 一即一切
# | 
# |     量子糾纏：
# |     • 每個粒子包含整個系統信息
# |     • 測量一粒子，影響所有糾纏粒子
# |     • 粒子態不可單獨定義
# |     • 整體不可分解
# | 
# |     共同點：
# |     → 沒有「獨立」的部分
# |     → 一切互相依存
# |     → 改變局部 = 改變整體
# |     '''
# | 
# |     ax4.text(0.1, 0.5, comparison, fontsize=11, va='center',
# |             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
# | 
# |     plt.tight_layout()
# |     plt.savefig('indras_net_entanglement.png', dpi=300, bbox_inches='tight')
# |     plt.show()

    # 數據說明
    print("\n" + "="*70)
    print("【因陀羅網與量子糾纏】")
    print("="*70)

    print("\n《華嚴經》的因陀羅網：")
    print("  • 無限大的珠網")
    print("  • 每顆珠子反射所有珠子")
    print("  • 無限遞迴，互相映照")
    print("  → 一即一切，一切即一")

    print("\n量子糾纏（Entanglement）：")
    print("  • 兩個或多個粒子處於糾纏態")
    print("  • |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2")
    print("  • 測量一個粒子，瞬間影響其他粒子")
    print("  • 即使相距光年，仍然關聯")

    print("\n實驗證據：")
    print("  • 1982年：阿斯佩實驗證實糾纏")
    print("  • 2015年：「無漏洞」貝爾實驗")
    print("  • 2022年：諾貝爾物理學獎")

    print("\n哲學意義：")
    print("  • 沒有「獨立」的粒子")
    print("  • 宇宙是一個不可分割的整體")
    print("  • 「分離」是幻覺")

    print("\n佛教「緣起」：")
    print("  • 此有故彼有，此生故彼生")
    print("  • 一切法互為因緣")
    print("  • 沒有獨立自存的「我」或「物」")

    print("\n共同洞見：")
    print("  世界不是「獨立個體的集合」")
    print("  而是「相互依存的關係網」")
    print("="*70)

# 執行
indras_net_quantum()

def self_as_entanglement():
    """
    「我」的空性
    展示：「自我」如何是因緣和合，沒有獨立自性
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # === 左圖：經典的「自我」觀念 ===
    circle_self = plt.Circle((0.5, 0.5), 0.15, color='red', alpha=0.7,
                            edgecolor='black', linewidth=3)
    ax1.add_patch(circle_self)
    ax1.text(0.5, 0.5, '我', ha='center', va='center', fontsize=20,
            fontweight='bold', color='white')

    external_things = [
        (0.2, 0.8, '家人'),
        (0.8, 0.8, '朋友'),
        (0.1, 0.5, '工作'),
        (0.9, 0.5, '身體'),
        (0.2, 0.2, '記憶'),
        (0.8, 0.2, '想法'),
    ]

    for x, y, label in external_things:
        circle = plt.Circle((x, y), 0.08, color='lightblue', alpha=0.5,
                           edgecolor='gray', linewidth=1.5)
        ax1.add_patch(circle)
        ax1.text(x, y, label, ha='center', va='center', fontsize=10)
        ax1.annotate('', xy=(x, y), xytext=(0.5, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black', alpha=0.5))

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('經典觀念：獨立的「我」\n「我」擁有身體、記憶、想法...',
                 fontsize=14, fontweight='bold')
    ax1.text(0.5, 0.05, '假設：有一個獨立的「自我」核心',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === 右圖：佛教的「無我」===
    elements = [
        (0.3, 0.7, '身'),
        (0.7, 0.7, '受'),
        (0.5, 0.5, '想'),
        (0.3, 0.3, '行'),
        (0.7, 0.3, '識'),
    ]

    for x, y, label in elements:
        circle = plt.Circle((x, y), 0.1, color='lightgreen', alpha=0.6,
                           edgecolor='green', linewidth=2)
        ax2.add_patch(circle)
        ax2.text(x, y, label, ha='center', va='center', fontsize=12,
                fontweight='bold')

    for i, (x1, y1, _) in enumerate(elements):
        for x2, y2, _ in elements[i+1:]:
            ax2.plot([x1, x2], [y1, y2], 'g-', alpha=0.3, linewidth=2)

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('佛教觀念：「五蘊」無我\n沒有獨立的「我」，只有因緣和合',
                 fontsize=14, fontweight='bold')
    ax2.text(0.5, 0.05, '真相：「我」是五蘊（身、受、想、行、識）的暫時組合',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('self_emptiness.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 量子類比
    print("\n" + "="*70)
    print("【「我」的空性：自我是糾纏態】")
    print("="*70)

    print("\n佛教的「五蘊」理論：")
    print("  1. 色蘊（rūpa）：身體、物質")
    print("  2. 受蘊（vedanā）：感受")
    print("  3. 想蘊（saṃjñā）：概念、認知")
    print("  4. 行蘊（saṃskāra）：意志、行為傾向")
    print("  5. 識蘊（vijñāna）：意識")

    print("\n佛教主張：")
    print("  • 沒有獨立的「我」")
    print("  • 「我」只是五蘊的暫時組合")
    print("  • 五蘊因緣和合 → 「我」的幻覺產生")
    print("  • 五蘊分散 → 「我」消失")

    print("\n量子類比：")
    print("  • 粒子沒有獨立的「狀態」")
    print("  • 「狀態」是測量基底的投影")
    print("  • 系統可以分解為不同基底：")
    print("    |ψ⟩ = Σ cᵢ|φᵢ⟩ （位置基底）")
    print("    |ψ⟩ = Σ dⱼ|χⱼ⟩ （動量基底）")
    print("  • 沒有「本質」狀態，只有相對於基底的表達")

    print("\n「我」如何是糾纏態：")
    print("  |我⟩ = α|身體⟩|記憶⟩|環境⟩... （簡化表達）")
    print("  ")
    print("  • 「我」與身體糾纏（改變身體 → 改變「我」）")
    print("  • 「我」與記憶糾纏（失憶 → 「我」改變）")
    print("  • 「我」與環境糾纏（環境變 → 「我」變）")
    print("  • 沒有獨立於這些的「我核心」")

    print("\n實踐意義：")
    print("  • 執著「我」是痛苦根源")
    print("  • 了悟「無我」能解脫")
    print("  • 不是「我不存在」，而是「我無自性」")
    print("  • 「我」依因緣而有，因緣變則「我」變")

    print("\n深刻問題：")
    print("  如果「我」沒有自性，那「誰」在讀這段文字？")
    print("  答：讀的過程在發生，但沒有獨立的「讀者」。")
    print("  就像波函數坍縮在發生，但沒有獨立的「粒子」。")
    print("="*70)

# 執行
self_as_entanglement()
