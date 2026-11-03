# Code & Cogito: 量子意識 vs 東洋の心の哲学——心は量子過程なのか？
# Article: https://code-cogito.com/ja/quantum-consciousness-eastern-philosophy-ja/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumConsciousnessSimulator:
    """
    Quantum consciousness simulator
    Demonstrates how measurement/observation affects quantum systems
    """

    def __init__(self):
        pass

    def visualize_measurement_consciousness(self):
        """
        Visualize the relationship between measurement and consciousness
        """
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Before measurement (superposition) ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')

        # Bloch sphere representation of superposition state
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax1.plot_surface(x, y, z, alpha=0.3, color='cyan')

        # Superposition state vector
        theta, phi = np.pi/4, np.pi/4
        sx = np.sin(theta) * np.cos(phi)
        sy = np.sin(theta) * np.sin(phi)
        sz = np.cos(theta)

        ax1.quiver(0, 0, 0, sx, sy, sz, color='purple',
                  arrow_length_ratio=0.1, linewidth=3)

        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('測定前：重ね合わせ状態\n|ψ⟩ = α|0⟩ + β|1⟩',
                     fontsize=13, fontweight='bold')

        # === Panel 2: During measurement (observer intervenes) ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # Eye (observer)
        eye = plt.Circle((0.5, 0.7), 0.15, color='blue', alpha=0.6,
                        edgecolor='darkblue', linewidth=3)
        ax2.add_patch(eye)
        ax2.text(0.5, 0.7, '👁', ha='center', va='center', fontsize=40)

        # Arrow pointing down
        ax2.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=5, color='red'))
        ax2.text(0.6, 0.475, '観察\n測定', ha='left', fontsize=12,
                color='red', fontweight='bold')

        # Quantum system
        rect = plt.Rectangle((0.35, 0.25), 0.3, 0.15,
                            facecolor='purple', alpha=0.5,
                            edgecolor='purple', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(0.5, 0.325, '量子系', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        ax2.set_title('測定時：観察者の介入\n波動関数が収縮しようとしている',
                     fontsize=13, fontweight='bold')

        # === Panel 3: After measurement (collapse) ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')

        # Bloch sphere
        ax3.plot_surface(x, y, z, alpha=0.3, color='lightblue')

        # Collapsed to |0⟩ (north pole)
        ax3.quiver(0, 0, 0, 0, 0, 1, color='red',
                  arrow_length_ratio=0.1, linewidth=3)

        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('Z')
        ax3.set_title('測定後：収縮\n|ψ⟩ → |0⟩',
                     fontsize=13, fontweight='bold')

        # === Panel 4: Classical view ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        text_classical = '''
        古典的観点（唯物論）：

        • 物質は観察者から独立
        • 観察は単なる「発見」
        • 意識は副産物
        • 脳は古典的コンピュータ

        問題点：
        → 測定問題を説明できない
        → 意識の統一性を説明できない
        '''

        ax4.text(0.1, 0.5, text_classical, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # === Panel 5: Quantum consciousness view ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')

        text_quantum = '''
        量子意識（Orch OR）：

        • 意識は量子過程
        • 微小管の中で発生
        • 意識が波動関数を収縮させる
        • 各収縮 = 意識の一瞬

        長所：
        → 意識の統一性を説明
        → 意識の非計算性を説明
        → 量子力学と意識を結合
        '''

        ax5.text(0.1, 0.5, text_quantum, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.8))

        # === Panel 6: Eastern philosophy view ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text_eastern = '''
        東洋の心の哲学・禅宗：

        • 心は万法の根源
        • 心を離れて物を語れない
        • 心は脳ではない
        • 心は存在論的根源

        王陽明：
        「心外無物、心外無理」

        禅宗：
        「直指人心、見性成仏」

        西田幾多郎：
        「純粋経験」＝主客未分

        共通点：
        → 心/意識に存在論的地位
        → 観察が実在を創造する
        '''

        ax6.text(0.1, 0.5, text_eastern, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # Main title
        fig.text(0.5, 0.98, '量子測定と意識：三つの観点',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        plt.savefig('quantum_measurement_consciousness.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子測定と意識】")
        print("="*70)

        print("\n測定問題：")
        print("  • 測定前：系は重ね合わせ状態にある")
        print("  • 測定時：波動関数が収縮する")
        print("  • 測定後：系は確定状態にある")
        print("  • 問い：何が収縮を引き起こすのか？")

        print("\n三つの回答：")
        print("\n1. コペンハーゲン解釈（標準的立場）：")
        print("   → 測定装置が収縮を引き起こす")
        print("   → しかし測定装置も量子系")
        print("   → 無限後退の問題")

        print("\n2. 多世界解釈：")
        print("   → 収縮は起こらない、宇宙が分岐する")
        print("   → 意識に特別な地位はない")

        print("\n3. フォン・ノイマン/Orch OR：")
        print("   → 意識が収縮を引き起こす")
        print("   → 意識に特別な地位がある")

        print("\n東洋哲学の関連する見解：")
        print("  王陽明：「心外無物」")
        print("  → 心を離れて物を定義できない")

        print("\n  禅宗：「明心見性」")
        print("  → 心の本質を直接体得する")

        print("\n  西田幾多郎：「純粋経験」")
        print("  → 主客未分の根源的経験")

        print("\n共通点：")
        print("  • 観察者/心が中心的役割を果たす")
        print("  • 「客観的実在」は主体に依存する")
        print("  • 心/意識は副産物ではない")

        print("\n核心的な問い：")
        print("  • 意識は本当に収縮を引き起こすのか？")
        print("  • もしそうなら、そのメカニズムは？")
        print("  • Orch OR理論は正しいのか？")
        print("  • それとも新しい物理学が必要か？")
        print("="*70)

# Execute
simulator = QuantumConsciousnessSimulator()
simulator.visualize_measurement_consciousness()

class OrchORSimulator:
    """
    Orch OR theory simulation
    Demonstrates how microtubules may generate consciousness
    """

    def __init__(self):
        self.hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
        self.c = 299792458  # Speed of light (m/s)

    def calculate_collapse_time(self, delta_mass):
        """
        Calculate objective collapse time
        τ = ℏ / (ΔM · c²)
        """
        delta_energy = delta_mass * self.c**2
        tau = self.hbar / delta_energy
        return tau

    def visualize_orch_or(self):
        """
        Visualize Orch OR theory
        """
        fig = plt.figure(figsize=(18, 10))

        # === Panel 1: Microtubule structure ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.axis('off')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        # Microtubule (cylindrical structure)
        from matplotlib.patches import Rectangle, Circle

        # Simplified microtubule drawing
        for i in range(5):
            y = 0.2 + i * 0.15
            # Tubulin proteins
            circle1 = Circle((0.3, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle2 = Circle((0.5, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle3 = Circle((0.7, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            ax1.add_patch(circle1)
            ax1.add_patch(circle2)
            ax1.add_patch(circle3)

        # Connecting lines
        for i in range(4):
            y = 0.2 + i * 0.15
            ax1.plot([0.3, 0.3], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.5, 0.5], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.7, 0.7], [y+0.04, y+0.11], 'b-', alpha=0.5)

        ax1.set_title('微小管の構造\nチューブリンの配列', fontsize=13, fontweight='bold')

        ax1.text(0.5, 0.05, '直径：約25 nm\n長さ：数マイクロメートル',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))

        # === Panel 2: Quantum superposition ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # Two states of tubulin
        circle_left = Circle((0.3, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='darkred', linewidth=2)
        circle_right = Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                             edgecolor='darkblue', linewidth=2)
        ax2.add_patch(circle_left)
        ax2.add_patch(circle_right)

        ax2.text(0.3, 0.5, '状態|0⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')
        ax2.text(0.7, 0.5, '状態|1⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # Double arrow
        ax2.annotate('', xy=(0.68, 0.5), xytext=(0.32, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
        ax2.text(0.5, 0.55, '+', ha='center', fontsize=16, fontweight='bold')

        ax2.text(0.5, 0.7, '重ね合わせ：α|0⟩ + β|1⟩', ha='center',
                fontsize=11, fontweight='bold', color='purple')

        ax2.set_title('チューブリンの量子重ね合わせ', fontsize=13, fontweight='bold')

        # === Panel 3: Objective collapse ===
        ax3 = fig.add_subplot(2, 3, 3)

        # Time axis
        t = np.linspace(0, 0.03, 100)

        # Superposition "size" (energy/mass difference)
        mass_diff = 1e-8 * (1 - np.exp(-t/0.01))  # kg

        ax3.plot(t * 1000, mass_diff * 1e8, 'b-', linewidth=3)
        ax3.axhline(1e-8 * 1e8, color='red', linestyle='--', linewidth=2,
                   label='収縮の閾値')

        # Mark collapse point
        collapse_idx = np.where(mass_diff >= 1e-8 * 0.99)[0][0]
        ax3.scatter([t[collapse_idx] * 1000], [mass_diff[collapse_idx] * 1e8],
                   c='red', s=200, zorder=5, edgecolors='black', linewidth=2)
        ax3.text(t[collapse_idx] * 1000, mass_diff[collapse_idx] * 1e8 + 0.05,
                '収縮！', ha='center', fontsize=11, fontweight='bold',
                color='red')

        ax3.set_xlabel('時間（ミリ秒）', fontsize=12)
        ax3.set_ylabel('質量差（×10⁻⁸ kg）', fontsize=12)
        ax3.set_title('客観収縮の過程\n重ね合わせが閾値まで蓄積',
                     fontsize=13, fontweight='bold')
        ax3.legend(fontsize=10)
        ax3.grid(True, alpha=0.3)

        # === Panel 4: Collapse time calculation ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        # Calculate collapse time for different mass differences
        masses = np.logspace(-12, -6, 100)  # kg
        times = [self.calculate_collapse_time(m) * 1000 for m in masses]  # ms

        ax4_plot = fig.add_axes([0.1, 0.1, 0.25, 0.35])
        ax4_plot.loglog(masses, times, 'g-', linewidth=3)
        ax4_plot.set_xlabel('質量差（kg）', fontsize=11)
        ax4_plot.set_ylabel('収縮時間（ms）', fontsize=11)
        ax4_plot.set_title('ペンローズの公式：τ = ℏ/(ΔM·c²)',
                          fontsize=12, fontweight='bold')
        ax4_plot.grid(True, alpha=0.3)

        # Mark brain parameters
        brain_mass = 1e-8
        brain_time = self.calculate_collapse_time(brain_mass) * 1000
        ax4_plot.scatter([brain_mass], [brain_time], c='red', s=100,
                        zorder=5, edgecolors='black', linewidth=2)
        ax4_plot.text(brain_mass * 3, brain_time,
                     f'脳\n約{brain_time:.1f} ms',
                     fontsize=9, color='red', fontweight='bold')

        # === Panel 5: Consciousness timeline ===
        ax5 = fig.add_subplot(2, 3, 5)

        # Simulate consciousness "updates"
        n_updates = 10
        update_times = np.linspace(0, 0.25, n_updates)

        for i, t_update in enumerate(update_times):
            ax5.scatter([t_update * 1000], [1], c='purple', s=300,
                       alpha=0.7, edgecolors='black', linewidth=2)
            ax5.text(t_update * 1000, 1.1, f'{i+1}', ha='center',
                    fontsize=9, fontweight='bold')

        ax5.plot([0, 250], [1, 1], 'gray', linestyle='--', alpha=0.3)
        ax5.set_xlabel('時間（ミリ秒）', fontsize=12)
        ax5.set_title('意識の「量子更新」\n各収縮 = 意識の一瞬',
                     fontsize=13, fontweight='bold')
        ax5.set_ylim(0.5, 1.5)
        ax5.set_yticks([])
        ax5.grid(True, alpha=0.3, axis='x')

        # Annotate frequency
        ax5.text(125, 0.7, f'周波数：約40 Hz\n（脳波と一致）',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === Panel 6: Orch OR summary ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text_summary = '''
        Orch OR理論の要約：

        1. チューブリンが量子重ね合わせ状態にある
           |ψ⟩ = α|0⟩ + β|1⟩

        2. 重ね合わせの持続時間：
           τ = ℏ / (ΔM · c²)

        3. ΔMが十分大きくなると：
           時空曲率が顕著に
           → 自発的収縮（客観収縮）

        4. 各収縮 = 意識の一瞬
           収縮頻度 約40 Hz

        5. 脳がこれらの収縮を調和させる
           → 統一的な意識体験

        主要な予測：
        • 麻酔薬が微小管の量子状態に影響
        • 意識は量子コヒーレンスに依存
        • 意識は非アルゴリズム的

        論争：
        • 脳の温度が高すぎる？
        • デコヒーレンスが速すぎる？
        • 客観収縮は存在するか？
        '''

        ax6.text(0.1, 0.5, text_summary, fontsize=9, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('orch_or_simulation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【Orch OR理論：量子意識仮説】")
        print("="*70)

        print("\nペンローズ＝ハメロフ（1996年）：")
        print("  • Orchestrated Objective Reduction")
        print("  • 調和的客観収縮")

        print("\n中核メカニズム：")
        print("  1. チューブリンが量子重ね合わせ状態にある")
        print("  2. 重ね合わせ状態は一定時間持続する")
        print("  3. 質量差ΔMが十分大きくなると")
        print("  4. 時空曲率が顕著になり")
        print("  5. 自発的に収縮する（客観収縮）")
        print("  6. この収縮 = 意識の一瞬")

        print("\nペンローズの公式：")
        print(f"  τ = ℏ / (ΔM · c²)")
        print(f"  ℏ = {self.hbar:.3e} J·s")
        print(f"  c = {self.c:.0f} m/s")

        print("\n脳のパラメータ（推定）：")
        brain_mass = 1e-8  # kg
        brain_tau = self.calculate_collapse_time(brain_mass)
        print(f"  ΔM ≈ {brain_mass:.0e} kg")
        print(f"  τ ≈ {brain_tau * 1000:.1f} ms")
        print(f"  周波数 ≈ {1/brain_tau:.0f} Hz")

        print("\n実験的証拠（2014年）：")
        print("  • 微小管が生理的温度下で量子振動を持つことを発見")
        print("  • ただし、これだけではOrch ORの完全な証明にはならない")

        print("\n論争：")
        print("  支持者：意識の統一性と非計算性を説明できる")
        print("  批判者：脳は高温すぎ、デコヒーレンスが速すぎる")

        print("\nペンローズ（2020年ノーベル賞講演）：")
        print("  「意識が量子的かどうか、私にはわかりません。")
        print("   しかし意識を理解するには、新しい物理学が必要です。」")
        print("="*70)

# Execute
orch_sim = OrchORSimulator()
orch_sim.visualize_orch_or()

def visualize_zen_enlightenment_collapse():
    """
    Visualize the analogy between Zen enlightenment and wavefunction collapse
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Panel 1: Delusion (before measurement) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '迷い（測定前）', ha='center',
           fontsize=14, fontweight='bold')

    # Confused mind (superposition state)
    np.random.seed(42)
    for _ in range(30):
        x, y = np.random.random(2)
        ax.text(x, y, '妄', fontsize=12, alpha=0.6,
               color=np.random.choice(['gray', 'darkgray']))

    # Center: unclear mind
    circle = plt.Circle((0.5, 0.5), 0.15, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n不明', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.15, '妄念紛飛\n重ね合わせ状態のように', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Panel 2: Awakening (during measurement) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '悟り（測定時）', ha='center',
           fontsize=14, fontweight='bold')

    # Flash of light (sudden awakening)
    for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        ax.plot([0.5, x], [0.5, y], 'yellow', linewidth=3, alpha=0.8)

    # Center: illuminated mind
    circle = plt.Circle((0.5, 0.5), 0.15, color='gold', alpha=0.9,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n見性', ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(0.5, 0.15, '瞬間の悟り\n収縮のように', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === Panel 3: After awakening (after measurement) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '悟り後（測定後）', ha='center',
           fontsize=14, fontweight='bold')

    # Clear mind (definite state)
    circle = plt.Circle((0.5, 0.5), 0.2, color='lightblue', alpha=0.7,
                       edgecolor='blue', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '本心\n清明', ha='center', va='center',
           fontsize=12, fontweight='bold', color='darkblue')

    # Surroundings: purity
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax.text(x, y, '浄', fontsize=10, alpha=0.6, color='blue')

    ax.text(0.5, 0.15, '心明らかに性を見る\n確定状態のように', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 4: Correspondence summary ===
    ax = axes[1, 1]
    ax.axis('off')

    comparison = '''
    【禅の悟り vs 波動関数の収縮】

    禅宗：
    • 迷い：妄念紛飛、心が不明
    • 悟り：瞬間の頓悟、明心見性
    • 悟り後：本心清明

    量子力学：
    • 測定前：重ね合わせ、不確定
    • 測定時：波動関数の収縮
    • 測定後：確定状態

    類似点：
    ✓ いずれも非連続的な変化
    ✓ いずれも瞬間的（量子跳躍）
    ✓ いずれも「観察」が関与
    ✓ いずれも不確定→確定

    禅の「頓悟」：
    • 漸進的ではない
    • 突然である
    • 予測不可能
    • 不可逆的

    波動関数の収縮：
    • 連続的ではない
    • 瞬間的
    • 確率的（ランダム）
    • 不可逆的

    深遠な類比：
    「明心見性」= 意識による収縮？
    '''

    ax.text(0.1, 0.5, comparison, fontsize=10, va='center',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                    edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('zen_enlightenment_collapse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【禅の悟りと波動関数の収縮の類比】")
    print("="*70)

    print("\n禅の「明心見性」：")
    print("  • 明心：自らの心を明らかにする")
    print("  • 見性：自らの本性（仏性）を見る")
    print("  • 修行法：坐禅、公案、棒喝")
    print("  • 結果：突然の頓悟")

    print("\n六祖慧能の頓悟：")
    print("  「応無所住而生其心」を聞いて")
    print("  → 瞬間に悟りを開く")

    print("\n  偈：")
    print("  「菩提本無樹、明鏡亦非台。")
    print("   本来無一物、何処惹塵埃。」")

    print("\n禅の「頓悟」の特性：")
    print("  • 非連続：漸進的ではない")
    print("  • 瞬間性：突然に起こる")
    print("  • 予測不可能：いつ起こるかわからない")
    print("  • 不可逆：一度悟れば退転しない")

    print("\n波動関数の収縮の特性：")
    print("  • 非連続：量子跳躍")
    print("  • 瞬間性：遷移過程がない")
    print("  • 確率的：確率しか予測できない")
    print("  • 不可逆：収縮後は元に戻れない")

    print("\n類比の深層：")
    print("  迷い（妄念）≈ 重ね合わせ状態（不確定）")
    print("  悟り（頓悟）≈ 収縮（測定）")
    print("  悟り後（清明）≈ 確定状態（結果）")

    print("\n問い：")
    print("  • 「明心見性」は意識が引き起こす収縮なのか？")
    print("  • 「自らの心を観る」とは一種の「測定」か？")
    print("  • 禅の「心」は量子過程なのか？")

    print("\n考えうる答え：")
    print("  • 禅と量子力学はいずれも、")
    print("    観察/心の役割が中心的だと指し示す")
    print("  • 「頓悟」と「収縮」はいずれも")
    print("    不確定から確定への瞬間的転換")
    print("  • ただし禅の「心」は")
    print("    物理学の「意識」を超えているかもしれない")

    print("\n  道元禅師：「身心脱落」")
    print("  → 身体と心への執着が一瞬で脱落する")
    print("  → 修行と悟りは一つ（修証一等）")
    print("="*70)

# Execute
visualize_zen_enlightenment_collapse()

def visualize_mind_principle_observer():
    """
    Visualize Wang Yangming's "Mind is Principle" and observer effect
    """

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # === Panel 1: Classical view (things outside mind) ===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    ax1.text(0.5, 0.95, '古典的観点：心の外に物がある', ha='center',
            fontsize=14, fontweight='bold', transform=ax1.transAxes)

    # Matter outside
    rect_matter = plt.Rectangle((0.6, 0.4), 0.25, 0.3,
                                facecolor='blue', alpha=0.6,
                                edgecolor='black', linewidth=2)
    ax1.add_patch(rect_matter)
    ax1.text(0.725, 0.55, '物\n（客観）', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Mind inside
    circle_mind = plt.Circle((0.25, 0.55), 0.1, color='red', alpha=0.6,
                            edgecolor='black', linewidth=2)
    ax1.add_patch(circle_mind)
    ax1.text(0.25, 0.55, '心\n（主観）', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Arrow: matter -> mind (passive reception)
    ax1.annotate('', xy=(0.35, 0.55), xytext=(0.6, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax1.text(0.475, 0.6, '知覚', ha='center', fontsize=10)

    ax1.text(0.5, 0.15, '物は心から独立\n心は受動的に受容', ha='center',
            fontsize=10, transform=ax1.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 2: Wang Yangming's "Mind is Principle" ===
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    ax2.text(0.5, 0.95, '王陽明：心即理', ha='center',
            fontsize=14, fontweight='bold', transform=ax2.transAxes)

    # Mind at center
    circle_mind = plt.Circle((0.5, 0.55), 0.15, color='gold', alpha=0.7,
                            edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_mind)
    ax2.text(0.5, 0.55, '心\n（本体）', ha='center', va='center',
            fontsize=12, fontweight='bold')

    # Things manifest from mind
    manifestations = [
        (0.25, 0.75, '物1'),
        (0.75, 0.75, '物2'),
        (0.25, 0.35, '物3'),
        (0.75, 0.35, '物4'),
    ]

    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.07, color='lightblue', alpha=0.6,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, label, ha='center', va='center', fontsize=9)

        # Arrow: mind -> things
        ax2.annotate('', xy=(x, y), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=2, color='orange',
                                  alpha=0.6))

    ax2.text(0.5, 0.15, '心外無物\n物は心に依って顕れる', ha='center',
            fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === Panel 3: Quantum observer effect ===
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    ax3.text(0.5, 0.95, '量子力学：観察者効果', ha='center',
            fontsize=14, fontweight='bold', transform=ax3.transAxes)

    # Observer
    circle_observer = plt.Circle((0.5, 0.75), 0.1, color='purple', alpha=0.7,
                                edgecolor='darkviolet', linewidth=2)
    ax3.add_patch(circle_observer)
    ax3.text(0.5, 0.75, '観察者', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Arrow downward (observation)
    ax3.annotate('', xy=(0.5, 0.45), xytext=(0.5, 0.65),
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax3.text(0.6, 0.55, '観察\n測定', ha='left', fontsize=10,
            color='red', fontweight='bold')

    # Quantum system (superposition -> definite)
    # Superposition state
    circle_left = plt.Circle((0.35, 0.35), 0.06, color='red', alpha=0.3,
                            edgecolor='red', linewidth=1.5)
    circle_right = plt.Circle((0.65, 0.35), 0.06, color='blue', alpha=0.3,
                             edgecolor='blue', linewidth=1.5)
    ax3.add_patch(circle_left)
    ax3.add_patch(circle_right)

    # Line (superposition -> definite)
    ax3.plot([0.35, 0.65], [0.35, 0.35], 'gray', linestyle=':', alpha=0.5)
    ax3.text(0.5, 0.3, '重ね合わせ', ha='center', fontsize=9, color='gray')

    # After collapse
    circle_result = plt.Circle((0.5, 0.15), 0.08, color='green', alpha=0.7,
                              edgecolor='darkgreen', linewidth=2)
    ax3.add_patch(circle_result)
    ax3.text(0.5, 0.15, '確定状態', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    ax3.annotate('', xy=(0.5, 0.23), xytext=(0.5, 0.29),
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))

    ax3.text(0.5, 0.05, '観察が実在を創造する\n属性は測定に依って定まる', ha='center',
            fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Main title
    fig.text(0.5, 0.98, '「心」の役割：三つの観点',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig('mind_principle_observer.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【王陽明「心即理」と観察者効果】")
    print("="*70)

    print("\n王陽明の心学：")
    print("  核心：「心即理」")
    print("  → 心外無物、心外無理")
    print("  → 心を離れて物の存在と意味を論じることはできない")

    print("\n龍場の悟道（1508年）：")
    print("  「聖人の道、吾が性自ら足る、")
    print("   之に向いて理を事物に求むるは誤りなり！」")
    print("  → これまで外に理を求めたのは誤りだった")
    print("  → 理は心の中にある")

    print("\n「知行合一」：")
    print("  • 真の知は必ず真の行をともなう")
    print("  • 知と行は分離できない")
    print("  • 例：火が熱いと知る → 手を出さない")

    print("\n日本における受容：")
    print("  • 中江藤樹：日本陽明学の祖")
    print("  • 大塩平八郎：知行合一の実践")
    print("  • 吉田松陰：松下村塾での教育")
    print("  • 西郷隆盛：明治維新の精神的支柱")

    print("\n量子力学の観察者効果：")
    print("  • 測定前：粒子は重ね合わせ状態にある")
    print("  • 測定時：波動関数が収縮する")
    print("  • 測定後：粒子は確定状態にある")
    print("  → 観察者が実在の創造に参与する")

    print("\n対応関係：")
    print("  王陽明：心外無物")
    print("  量子力学：観察を離れて確定属性はない")

    print("\n  王陽明：物は心に依って顕れる")
    print("  量子力学：属性は測定に依って定まる")

    print("\n相違点：")
    print("  • 王陽明の「心」：")
    print("    個人の意識にとどまらない")
    print("    存在論的・宇宙的な心")
    print("  • 量子力学の「観察者」：")
    print("    測定装置でもよい")
    print("    必ずしも意識を要しない")

    print("\n共通の洞察：")
    print("  • 「客観的実在」は主体に依存する")
    print("  • 主体と客体は分離できない")
    print("  • 「物自体」は不可知")

    print("\n深い問い：")
    print("  • 王陽明の「心」= 量子の「観察者」？")
    print("  • 「心即理」= 「観察が実在を創造する」？")
    print("  • それとも二つは異なる次元の真理を指しているのか？")
    print("="*70)

# Execute
visualize_mind_principle_observer()
