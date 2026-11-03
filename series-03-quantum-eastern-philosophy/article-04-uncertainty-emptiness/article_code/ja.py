# Code & Cogito: 不確定性原理 vs 仏教の「空性」——万物に自性なし
# Article: https://code-cogito.com/ja/uncertainty-principle-buddhist-emptiness-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class UncertaintyPrinciple:
    """
    Uncertainty principle interactive experiment.
    Demonstrates the trade-off between position and momentum uncertainty.
    """

    def __init__(self):
        self.hbar = 1.0  # reduced Planck constant (arbitrary units)

    def gaussian_wavepacket(self, x, x0, sigma_x, k0):
        """
        Gaussian wave packet.
        x0: center position
        sigma_x: position standard deviation (uncertainty)
        k0: central wavenumber (corresponding momentum p0 = hbar * k0)
        """
        return (1 / (2 * np.pi * sigma_x**2)**0.25) * \
               np.exp(-((x - x0)**2) / (4 * sigma_x**2)) * \
               np.exp(1j * k0 * x)

    def momentum_distribution(self, psi_x, dx):
        """
        Compute momentum-space wavefunction from position-space wavefunction
        via Fourier transform.
        """
        psi_k = fft(psi_x) * dx
        return psi_k

    def visualize_uncertainty(self, sigma_x_values=[0.5, 1.0, 2.0, 4.0]):
        """
        Visualize wave packets for different position uncertainties.
        """
        x = np.linspace(-20, 20, 2000)
        dx = x[1] - x[0]

        fig, axes = plt.subplots(2, len(sigma_x_values), figsize=(18, 10))

        for i, sigma_x in enumerate(sigma_x_values):
            # Generate wave packet
            psi_x = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

            # Position-space probability density
            prob_x = np.abs(psi_x)**2

            # Momentum space
            psi_k = self.momentum_distribution(psi_x, dx)
            k = fftfreq(len(x), dx) * 2 * np.pi
            prob_k = np.abs(psi_k)**2

            # Re-sort (fft output needs reordering)
            k_sorted_idx = np.argsort(k)
            k_sorted = k[k_sorted_idx]
            prob_k_sorted = prob_k[k_sorted_idx]

            # Compute uncertainties
            delta_x = sigma_x
            delta_k = 1 / (2 * sigma_x)
            delta_p = self.hbar * delta_k
            uncertainty_product = delta_x * delta_p

            # === Upper plot: position space ===
            ax = axes[0, i]
            ax.plot(x, prob_x, 'b-', linewidth=2)
            ax.fill_between(x, 0, prob_x, alpha=0.3, color='blue')
            ax.set_xlabel('位置 x', fontsize=11)
            ax.set_ylabel('|ψ(x)|²', fontsize=11)
            ax.set_title(f'位置の不確定性\nΔx = {delta_x:.2f}',
                        fontsize=12, fontweight='bold', color='blue')
            ax.grid(True, alpha=0.3)
            ax.set_xlim(-15, 15)
            ax.axvspan(-delta_x, delta_x, alpha=0.2, color='cyan',
                      label=f'Δx = {delta_x:.2f}')
            ax.legend(fontsize=9)

            # === Lower plot: momentum space ===
            ax = axes[1, i]
            center_idx = len(k_sorted) // 2
            plot_range = 500
            k_plot = k_sorted[center_idx-plot_range:center_idx+plot_range]
            prob_k_plot = prob_k_sorted[center_idx-plot_range:center_idx+plot_range]

            if np.max(prob_k_plot) > 0:
                prob_k_plot = prob_k_plot / np.max(prob_k_plot)

            ax.plot(k_plot, prob_k_plot, 'r-', linewidth=2)
            ax.fill_between(k_plot, 0, prob_k_plot, alpha=0.3, color='red')
            ax.set_xlabel('波数 k（運動量 p=ℏk）', fontsize=11)
            ax.set_ylabel('|ψ(k)|²', fontsize=11)
            ax.set_title(f'運動量の不確定性\nΔp = {delta_p:.2f}',
                        fontsize=12, fontweight='bold', color='red')
            ax.grid(True, alpha=0.3)

            color = 'green' if uncertainty_product >= self.hbar/2 else 'red'
            ax.text(0.5, 0.9,
                   f'Δx·Δp = {uncertainty_product:.3f}\n(ℏ/2 = {self.hbar/2:.3f})',
                   transform=ax.transAxes, ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor=color, alpha=0.5))

        fig.text(0.5, 0.98, '不確定性原理：Δx が小さいほど → Δp は大きくなる',
                ha='center', fontsize=16, fontweight='bold')
        fig.text(0.5, 0.02,
                '核心的洞察：これは測定誤差ではなく、波動の数学的性質である！\n'
                '波束を「狭く（位置確定）」しながら「純粋（運動量確定）」にすることは不可能',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(top=0.93, bottom=0.1)
        plt.savefig('uncertainty_principle_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()

    def interactive_measurement(self):
        """
        Interactive measurement: observe the effect of measurement order.
        """
        print("\n" + "="*70)
        print("【不確定性原理インタラクティブ実験】")
        print("="*70)

        x = np.linspace(-10, 10, 1000)
        sigma_x = 1.0
        psi = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

        print("\n初期状態：")
        print(f"  位置の不確定性 Δx ≈ {sigma_x:.2f}")
        print(f"  運動量の不確定性 Δp ≈ {self.hbar/(2*sigma_x):.2f}")
        print(f"  不確定性の積 Δx·Δp ≈ {sigma_x * self.hbar/(2*sigma_x):.3f}")
        print(f"  ハイゼンベルクの下限 ℏ/2 = {self.hbar/2:.3f}")

        print("\n実験1：位置を先に測定し、次に運動量を測定")
        print("  → 位置測定後、波動関数は特定の位置に収縮する")
        print("  → このとき Δx → 0、したがって Δp → ∞")
        print("  → 運動量は完全に不確定！")

        print("\n実験2：運動量を先に測定し、次に位置を測定")
        print("  → 運動量測定後、波動関数は平面波になる")
        print("  → このとき Δp → 0、したがって Δx → ∞")
        print("  → 位置は完全に不確定！")

        print("\n結論：")
        print("  • 測定の順序が結果を変える（x̂ と p̂ は非可換）")
        print("  • ある量を測定すると、別の量が撹乱される")
        print("  • これは機器の問題ではなく、自然法則である")

        print("\n仏教的視点：")
        print("  • 万物に固定した「自性」はない")
        print("  • 属性は観察の仕方に依存する")
        print("  • 見る角度が変われば、見える相も変わる")
        print("  → 道元：「仏道を習ふといふは、自己を習ふなり」")
        print("="*70)

# Execute
experiment = UncertaintyPrinciple()
experiment.visualize_uncertainty(sigma_x_values=[0.5, 1.0, 2.0, 4.0])
experiment.interactive_measurement()

def visualize_emptiness():
    """
    Visualization of sunyata (emptiness).
    Demonstrates how properties of things depend on observation conditions.
    """

    fig = plt.figure(figsize=(16, 12))

    # === Example: the "emptiness" of a teacup ===

    # Subplot 1: different angles reveal different shapes
    ax1 = fig.add_subplot(2, 3, 1)
    circle = plt.Circle((0.5, 0.5), 0.3, fill=False, edgecolor='blue', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.1, '上から見ると：円形', ha='center', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Subplot 2: side view: rectangle
    ax2 = fig.add_subplot(2, 3, 2)
    rect = plt.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='red', linewidth=3)
    ax2.add_patch(rect)
    ax2.text(0.5, 0.1, '横から見ると：長方形', ha='center', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # Subplot 3: the question
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.text(0.5, 0.5, '問：茶碗の\n「真の形」は？\n\n答：「固定した形」は\n存在しない！\n\n形は観察角度に\n依存する',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')

    # === Quantum analogy: particle "position" ===

    # Subplot 4: position measurement
    ax4 = fig.add_subplot(2, 3, 4)
    x = np.linspace(-5, 5, 1000)
    psi_position = np.exp(-x**2)
    ax4.plot(x, psi_position, 'b-', linewidth=3)
    ax4.fill_between(x, 0, psi_position, alpha=0.3, color='blue')
    ax4.set_xlabel('位置', fontsize=11)
    ax4.set_ylabel('確率', fontsize=11)
    ax4.set_title('「位置」を測定\n→ 位置が確定', fontsize=12, fontweight='bold', color='blue')
    ax4.grid(True, alpha=0.3)

    # Subplot 5: momentum measurement
    ax5 = fig.add_subplot(2, 3, 5)
    k = np.linspace(-5, 5, 1000)
    psi_momentum = np.exp(-(k-2)**2/4)
    ax5.plot(k, psi_momentum, 'r-', linewidth=3)
    ax5.fill_between(k, 0, psi_momentum, alpha=0.3, color='red')
    ax5.set_xlabel('運動量', fontsize=11)
    ax5.set_ylabel('確率', fontsize=11)
    ax5.set_title('「運動量」を測定\n→ 運動量が確定', fontsize=12, fontweight='bold', color='red')
    ax5.grid(True, alpha=0.3)

    # Subplot 6: conclusion
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.text(0.5, 0.5, '問：粒子の\n「真の状態」は？\n\n答：「固定した属性」は\n存在しない！\n\n属性は測定方法に\n依存する',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')

    # Overall title and correspondence notes
    fig.text(0.5, 0.98, '「空性」と「不確定性」の構造的対応',
            ha='center', fontsize=16, fontweight='bold')
    fig.text(0.5, 0.02,
            '仏教：事物に「自性」（固定した本質）はなく、属性は条件に応じて顕れる\n'
            '量子力学：粒子に「確定した属性」はなく、属性は測定によって決まる\n'
            '共通点：「固定性」は実在の本質ではない',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.12)
    plt.savefig('emptiness_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Text output
    print("\n" + "="*70)
    print("【空性の三つの意味】")
    print("="*70)

    print("\n1. 空は「無」ではない")
    print("   『般若心経』：「色即是空、空即是色」")
    print("   → 事物は存在するが、固定した本質を持たない")

    print("\n2. 空は「縁起」")
    print("   龍樹：「因縁所生の法、我これを空と説く」")
    print("   → 一切は条件に依存して存在する")

    print("\n3. 空は「執着」を破る")
    print("   → 固定した「我」はない")
    print("   → 固定した「物」はない")
    print("   → 空性を悟り、執着を手放す（放下著）")

    print("\n不確定性原理との対応：")
    print("   • 粒子に固定した「位置」や「運動量」はない")
    print("   • 属性は測定方法によって決まる")
    print("   • 観察から独立した「客観的属性」は存在しない")

    print("\n共通の洞察：")
    print("   世界は「固定した属性を持つ物体」からなるのではなく")
    print("   「条件に応じて顕れる関係」からなる")
    print("="*70)

# Execute
visualize_emptiness()

import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

def indras_net_quantum():
    """
    Indra's Net and quantum entanglement.
    Demonstrates: everything is interconnected; changing one affects all.
    """

    fig = plt.figure(figsize=(18, 12))

    # === Left: Indra's Net (2D network) ===
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

    ax1.set_title('インドラの網：各珠が一切を映す\n一つを変えれば、全てが変わる',
                 fontsize=13, fontweight='bold')
    ax1.axis('off')
    ax1.text(2, -0.5, '華厳宗：一即一切、一切即一',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === Right: quantum entanglement network (3D) ===
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

    ax2.set_title('量子もつれ：粒子間の非局所的相関\n一つを測定すれば、全てに影響',
                 fontsize=13, fontweight='bold')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    # === Lower left: entangled state mathematics ===
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.axis('off')

    text = '''
    もつれ状態（ベル状態）：

    |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2

    特性：
    • 粒子AとBは分離不可能
    • Aを測定 → 即座にBが判明
    • Aの状態は単独で定義できない
    • 全体 ≠ 部分の和

    ベルの不等式（1964年）：
    粒子が「局所実在性」を持つなら
    → ある不等式を満たすはず

    実験結果（1982-2022年）：
    不等式は破れた！
    → 局所実在性はない
    → もつれは実在する
    '''

    ax3.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Lower right: Indra's Net vs entanglement ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    comparison = '''
    【インドラの網 vs 量子もつれ】

    インドラの網：
    • 各珠は網全体を含む
    • 一珠を変えれば、全網が動く
    • 部分が全体である
    • 一即一切

    量子もつれ：
    • 各粒子はシステム全体の情報を含む
    • 一粒子を測定すれば、全もつれ粒子に影響
    • 粒子の状態は単独で定義不可能
    • 全体は分割不可能

    共通点：
    → 「独立した」部分は存在しない
    → 一切は相互に依存する
    → 局部を変える＝全体を変える
    '''

    ax4.text(0.1, 0.5, comparison, fontsize=11, va='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.savefig('indras_net_entanglement.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Data explanation
    print("\n" + "="*70)
    print("【インドラの網と量子もつれ】")
    print("="*70)

    print("\n『華厳経』のインドラの網（帝網）：")
    print("  • 無限に広がる珠の網")
    print("  • 各珠がすべての珠を映す")
    print("  • 無限に再帰し、互いに映し合う")
    print("  → 一即一切、一切即一")

    print("\n量子もつれ（Entanglement）：")
    print("  • 二つ以上の粒子がもつれ状態にある")
    print("  • |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2")
    print("  • 一つの粒子を測定すると、瞬時に他の粒子に影響")
    print("  • たとえ光年の距離を隔てても、相関は保たれる")

    print("\n実験的証拠：")
    print("  • 1982年：アスペの実験がもつれを実証")
    print("  • 2015年：「抜け穴のない」ベル実験")
    print("  • 2022年：ノーベル物理学賞")

    print("\n哲学的含意：")
    print("  • 「独立した」粒子は存在しない")
    print("  • 宇宙は分割不可能な全体である")
    print("  • 「分離」は幻想にすぎない")

    print("\n仏教の「縁起」：")
    print("  • 此有るが故に彼有り、此生ずるが故に彼生ず")
    print("  • 一切の法は互いに因縁となる")
    print("  • 独立自存の「我」も「物」もない")

    print("\n共通の洞察：")
    print("  世界は「独立した個体の集合」ではなく")
    print("  「相互依存の関係の網」である")
    print("="*70)

# Execute
indras_net_quantum()

def self_as_entanglement():
    """
    Emptiness of the "self".
    Demonstrates how the "self" is a dependent arising with no intrinsic nature.
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # === Left: classical concept of "self" ===
    circle_self = plt.Circle((0.5, 0.5), 0.15, color='red', alpha=0.7,
                            edgecolor='black', linewidth=3)
    ax1.add_patch(circle_self)
    ax1.text(0.5, 0.5, '我', ha='center', va='center', fontsize=20,
            fontweight='bold', color='white')

    external_things = [
        (0.2, 0.8, '家族'),
        (0.8, 0.8, '友人'),
        (0.1, 0.5, '仕事'),
        (0.9, 0.5, '身体'),
        (0.2, 0.2, '記憶'),
        (0.8, 0.2, '思考'),
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
    ax1.set_title('古典的概念：独立した「我」\n「我」が身体・記憶・思考を所有する…',
                 fontsize=14, fontweight='bold')
    ax1.text(0.5, 0.05, '仮定：独立した「自我」の核心が存在する',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === Right: Buddhist "non-self" (anātman) ===
    elements = [
        (0.3, 0.7, '色'),
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
    ax2.set_title('仏教の概念：「五蘊」は無我\n独立した「我」はなく、因縁和合のみ',
                 fontsize=14, fontweight='bold')
    ax2.text(0.5, 0.05, '真実：「我」は五蘊（色・受・想・行・識）の一時的な和合',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('self_emptiness.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Quantum analogy
    print("\n" + "="*70)
    print("【「我」の空性：自己はもつれ状態】")
    print("="*70)

    print("\n仏教の「五蘊」（pañcaskandha）理論：")
    print("  1. 色蘊（rūpa）：身体、物質")
    print("  2. 受蘊（vedanā）：感受、感覚")
    print("  3. 想蘊（saṃjñā）：表象、概念")
    print("  4. 行蘊（saṃskāra）：意志、心の働き")
    print("  5. 識蘊（vijñāna）：認識、意識")

    print("\n仏教の主張：")
    print("  • 独立した「我」（ātman）は存在しない")
    print("  • 「我」は五蘊の一時的な和合にすぎない")
    print("  • 五蘊が因縁によって和合 → 「我」という幻が生じる")
    print("  • 五蘊が散ずれば → 「我」は消える")

    print("\n量子力学との類比：")
    print("  • 粒子には独立した「状態」がない")
    print("  • 「状態」は測定基底への射影である")
    print("  • 系は異なる基底で展開できる：")
    print("    |ψ⟩ = Σ cᵢ|φᵢ⟩ （位置基底）")
    print("    |ψ⟩ = Σ dⱼ|χⱼ⟩ （運動量基底）")
    print("  • 「本質的な」状態はなく、基底に相対的な表現があるのみ")

    print("\n「我」がもつれ状態である理由：")
    print("  |我⟩ = α|身体⟩|記憶⟩|環境⟩... （簡略化した表現）")
    print("  ")
    print("  • 「我」は身体ともつれている（身体が変われば「我」が変わる）")
    print("  • 「我」は記憶ともつれている（記憶を失えば「我」が変わる）")
    print("  • 「我」は環境ともつれている（環境が変われば「我」も変わる）")
    print("  • これらから独立した「我の核心」は存在しない")

    print("\n実践的意義：")
    print("  • 「我」への執着が苦（duḥkha）の根源である")
    print("  • 「無我」を悟れば、執着から解放される")
    print("  • 「我が存在しない」のではなく「我に自性がない」のだ")
    print("  • 「我」は因縁に依って有り、因縁が変われば「我」も変わる")

    print("\n深い問い：")
    print("  もし「我」に自性がないなら、「誰が」この文章を読んでいるのか？")
    print("  答え：読むという営みが起きているが、独立した「読者」はいない。")
    print("  波動関数の収縮が起きるが、独立した「粒子」がいないのと同じだ。")
    print("  道元：「自己をならふといふは、自己をわするるなり。」")
    print("="*70)

# Execute
self_as_entanglement()
