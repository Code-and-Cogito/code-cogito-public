# Code & Cogito: 量子場の理論と唯識思想――物質は心の顕れなのか
# Article: https://code-cogito.com/ja/quantum-field-theory-yogacara-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumFieldSimulator:
    """
    Quantum field simulator
    Demonstrates how field excitations produce particles
    """

    def __init__(self, size=100):
        self.size = size
        self.x = np.linspace(-10, 10, size)
        self.y = np.linspace(-10, 10, size)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def field_vacuum(self):
        """Vacuum state: ground state of the field with small quantum fluctuations"""
        fluctuation = np.random.randn(self.size, self.size) * 0.1
        return fluctuation

    def field_one_particle(self, x0=0, y0=0, k=1):
        """One-particle state: field excitation (Gaussian wave packet)"""
        R = np.sqrt((self.X - x0)**2 + (self.Y - y0)**2)
        particle = 2.0 * np.exp(-R**2 / 2) * np.cos(k * R)
        vacuum = self.field_vacuum()
        return particle + vacuum

    def field_two_particles(self, x1=-3, y1=0, x2=3, y2=0):
        """Two-particle state: two excitations"""
        R1 = np.sqrt((self.X - x1)**2 + (self.Y - y1)**2)
        R2 = np.sqrt((self.X - x2)**2 + (self.Y - y2)**2)
        particle1 = 2.0 * np.exp(-R1**2 / 2) * np.cos(2 * R1)
        particle2 = 2.0 * np.exp(-R2**2 / 2) * np.cos(2 * R2)
        vacuum = self.field_vacuum()
        return particle1 + particle2 + vacuum

    def visualize_field_states(self):
        """Visualize different field states"""
        fig = plt.figure(figsize=(18, 12))

        # === Vacuum state ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')
        vacuum = self.field_vacuum()
        surf1 = ax1.plot_surface(self.X, self.Y, vacuum, cmap='coolwarm',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax1.set_title('真空状態 |0⟩\n場の基底状態（量子ゆらぎ）',
                     fontsize=13, fontweight='bold')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('場の強度')
        ax1.set_zlim(-3, 3)

        # === One-particle state ===
        ax2 = fig.add_subplot(2, 3, 2, projection='3d')
        one_particle = self.field_one_particle(x0=0, y0=0)
        surf2 = ax2.plot_surface(self.X, self.Y, one_particle, cmap='viridis',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax2.set_title('一粒子状態 a†|0⟩\n場の局所的励起',
                     fontsize=13, fontweight='bold')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('場の強度')
        ax2.set_zlim(-3, 3)

        # === Two-particle state ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')
        two_particles = self.field_two_particles()
        surf3 = ax3.plot_surface(self.X, self.Y, two_particles, cmap='plasma',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax3.set_title('二粒子状態 a†a†|0⟩\n二つの局所的励起',
                     fontsize=13, fontweight='bold')
        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('場の強度')
        ax3.set_zlim(-3, 3)

        # === Vacuum energy density (cross-section) ===
        ax4 = fig.add_subplot(2, 3, 4)
        vacuum_slice = vacuum[self.size//2, :]
        ax4.plot(self.x, vacuum_slice, 'b-', linewidth=2)
        ax4.fill_between(self.x, 0, vacuum_slice, alpha=0.3, color='blue')
        ax4.set_xlabel('位置 X', fontsize=11)
        ax4.set_ylabel('場の強度', fontsize=11)
        ax4.set_title('真空の量子ゆらぎ（X軸断面）', fontsize=12, fontweight='bold')
        ax4.grid(True, alpha=0.3)
        ax4.axhline(0, color='black', linewidth=0.5)

        # === One-particle energy density (cross-section) ===
        ax5 = fig.add_subplot(2, 3, 5)
        one_particle_slice = one_particle[self.size//2, :]
        ax5.plot(self.x, one_particle_slice, 'g-', linewidth=2)
        ax5.fill_between(self.x, 0, one_particle_slice, alpha=0.3, color='green')
        ax5.set_xlabel('位置 X', fontsize=11)
        ax5.set_ylabel('場の強度', fontsize=11)
        ax5.set_title('粒子 = 場の局所的励起（X軸断面）', fontsize=12, fontweight='bold')
        ax5.grid(True, alpha=0.3)
        ax5.axhline(0, color='black', linewidth=0.5)

        # === Correspondence table ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text = '''
        【量子場の理論 vs 唯識思想】

        量子場の理論：
        ・場 = 基礎的実在
        ・粒子 = 場の励起
        ・真空 ≠ 空無

        唯識思想：
        ・識 = 基礎的実在
        ・万法 = 識の変現
        ・阿頼耶識 ≠ 空

        共通の洞察：
        ○「もの」は基礎ではない
        ○「場/識」こそが本体
        ○ 顕現は励起/変現に依る
        '''

        ax6.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('quantum_field_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子場と粒子】")
        print("="*70)
        print("\n古典物理学：粒子 = 基本的実体、確定した位置と速度を持つ")
        print("量子場の理論：場 = 基本的実体、粒子 = 場の励起状態")
        print("\n唯識との対応：")
        print("  阿頼耶識 ≈ 量子場")
        print("  種子 ≈ 場の潜在的励起モード")
        print("  現行 ≈ 場の実際の励起（粒子）")
        print("\n量子場の理論：「粒子は『もの』ではない。粒子は場の励起にすぎない。」")
        print("唯識：「万法は『実体』ではない。万法は識の変現にすぎない。」")
        print("="*70)

# Execute
simulator = QuantumFieldSimulator(size=100)
simulator.visualize_field_states()

class VirtualParticleSimulator:
    """Virtual particle simulator: demonstrates creation and annihilation in vacuum"""

    def __init__(self):
        pass

    def visualize_vacuum_fluctuations(self):
        """Visualize vacuum fluctuations"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left: Spacetime diagram of virtual particle creation/annihilation ===
        t = np.linspace(0, 10, 1000)
        n_pairs = 15
        np.random.seed(42)

        for i in range(n_pairs):
            t_create = np.random.uniform(0, 10)
            lifetime = np.random.exponential(0.5)
            t_annihilate = t_create + lifetime
            if t_annihilate > 10:
                t_annihilate = 10

            x_particle = np.random.uniform(-2, 2)
            x_antiparticle = -x_particle

            ax1.plot([t_create, t_annihilate], [x_particle, x_particle],
                    'r-', linewidth=2, alpha=0.6)
            ax1.plot([t_create, t_annihilate], [x_antiparticle, x_antiparticle],
                    'b--', linewidth=2, alpha=0.6)

            ax1.scatter([t_create], [x_particle], c='red', s=100,
                       zorder=5, edgecolors='black', linewidth=1)
            ax1.scatter([t_create], [x_antiparticle], c='blue', s=100,
                       zorder=5, edgecolors='black', linewidth=1)
            ax1.scatter([t_annihilate], [x_particle], c='purple', s=150,
                       marker='*', zorder=5, edgecolors='black', linewidth=1)

            ax1.plot([t_create, t_create], [x_particle, x_antiparticle],
                    'gray', linestyle=':', alpha=0.3, linewidth=1)
            ax1.plot([t_annihilate, t_annihilate], [x_particle, x_antiparticle],
                    'purple', linestyle=':', alpha=0.5, linewidth=1.5)

        ax1.set_xlabel('時間', fontsize=13)
        ax1.set_ylabel('空間位置', fontsize=13)
        ax1.set_title('真空中の仮想粒子の生滅\nハイゼンベルクの不確定性：ΔE·Δt ≥ ℏ/2',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, 10)
        ax1.set_ylim(-3, 3)

        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='r', linewidth=2, label='粒子'),
            Line2D([0], [0], color='b', linewidth=2, linestyle='--', label='反粒子'),
            Line2D([0], [0], marker='*', color='purple', markersize=12,
                  linestyle='None', label='対消滅'),
        ]
        ax1.legend(handles=legend_elements, fontsize=11)

        # === Right: Feynman diagram (electron-electron scattering) ===
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        ax2.text(0.5, 0.95, 'ファインマン図：電子-電子散乱',
                ha='center', fontsize=14, fontweight='bold',
                transform=ax2.transAxes)

        # Incoming and outgoing electrons
        ax2.arrow(0.1, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.25, 'e\u207b', fontsize=12, ha='center')
        ax2.arrow(0.1, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.75, 'e\u207b', fontsize=12, ha='center')

        # Virtual photon exchange
        ax2.plot([0.35, 0.35], [0.3, 0.7], 'r', linewidth=3,
                linestyle='dotted', alpha=0.7)
        ax2.text(0.42, 0.5, '仮想光子\n\u03b3*', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        ax2.arrow(0.35, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.25, 'e\u207b', fontsize=12, ha='center')
        ax2.arrow(0.35, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.75, 'e\u207b', fontsize=12, ha='center')

        explanation = '''
        ファインマン図の規則：
        ・実線 → 実粒子
        ・波線 → 仮想粒子
        ・頂点 → 相互作用

        仮想光子の性質：
        ・寿命がきわめて短い
        ・直接観測不可能
        ・しかし相互作用に実際に影響
        '''
        ax2.text(0.5, 0.15, explanation, fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        plt.tight_layout()
        plt.savefig('virtual_particles_feynman.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【仮想粒子と真空エネルギー】")
        print("="*70)
        print("\nハイゼンベルクの不確定性原理：ΔE · Δt ≥ ℏ/2")
        print("→ 真空中では絶えず仮想粒子対が生成と消滅を繰り返す")
        print("\nカシミール効果（1948年予言、1997年実験確認）：")
        print("  → 証明：真空は空ではない！")
        print("\n唯識との対応：")
        print("  阿頼耶識 = 真空（潜在力に満ちている）")
        print("  種子生現行 = 仮想粒子の実現")
        print("  現行還滅 = 仮想粒子の消滅")
        print("\n深い洞察：「空」は「無」ではない。「空」は潜在力に満ちた「有」である")
        print("  ——般若心経：色即是空、空即是色")
        print("="*70)

# Execute
virtual_sim = VirtualParticleSimulator()
virtual_sim.visualize_vacuum_fluctuations()

def visualize_eight_consciousnesses():
    """Visualize the eight-consciousness structure of Yogacara Buddhism"""

    fig = plt.figure(figsize=(18, 12))

    # === Eight-consciousness hierarchy ===
    ax1 = fig.add_subplot(2, 2, (1, 2))
    ax1.axis('off')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    consciousnesses = [
        (9, '第八識\n阿頼耶識\n(蔵識)', 'gold', 2.5, '一切種子識\n根本識'),
        (7.5, '第七識\n末那識', 'orange', 2.0, '恒審思量\n我執の根源'),
        (6, '第六識\n意識', 'red', 1.8, '思考・判断\n記憶・想像'),
        (4.8, '眼識', 'lightblue', 0.8, '視覚'),
        (4.0, '耳識', 'lightblue', 0.8, '聴覚'),
        (3.2, '鼻識', 'lightblue', 0.8, '嗅覚'),
        (2.4, '舌識', 'lightblue', 0.8, '味覚'),
        (1.6, '身識', 'lightblue', 0.8, '触覚'),
    ]

    for y, label, color, width, description in consciousnesses:
        rect = plt.Rectangle((5-width/2, y-0.3), width, 0.6,
                            facecolor=color, edgecolor='black',
                            linewidth=2, alpha=0.7)
        ax1.add_patch(rect)
        ax1.text(5, y, label, ha='center', va='center',
                fontsize=11, fontweight='bold')
        ax1.text(8, y, description, ha='left', va='center',
                fontsize=9,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Arrows: front five consciousnesses -> sixth consciousness
    for y in [4.8, 4.0, 3.2, 2.4, 1.6]:
        ax1.annotate('', xy=(5, 6), xytext=(5.5, y),
                    arrowprops=dict(arrowstyle='->', lw=1.5,
                                  color='blue', alpha=0.5))
    # Sixth <-> seventh <-> eighth consciousness
    ax1.annotate('', xy=(5, 7.5), xytext=(5, 6.3),
                arrowprops=dict(arrowstyle='<->', lw=2, color='red', alpha=0.6))
    ax1.annotate('', xy=(5, 9), xytext=(5, 7.8),
                arrowprops=dict(arrowstyle='<->', lw=2, color='purple', alpha=0.6))

    ax1.set_title('唯識思想：八識の階層構造', fontsize=16, fontweight='bold')

    # === Three transformations diagram ===
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    circle_center = plt.Circle((0.5, 0.7), 0.15, color='gold', alpha=0.7,
                              edgecolor='black', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.7, '阿頼耶識\n第八識', ha='center', va='center',
            fontsize=11, fontweight='bold')

    # Vipaka-parinama (maturation transformation)
    ax2.annotate('', xy=(0.2, 0.4), xytext=(0.4, 0.6),
                arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
    ax2.text(0.2, 0.4, '根身\n器界', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.text(0.1, 0.55, '異熟能変\n(世界の変現)', ha='center', fontsize=8, color='blue')

    # Manana-parinama (cogitation transformation)
    circle_manas = plt.Circle((0.8, 0.7), 0.1, color='orange', alpha=0.6,
                             edgecolor='black', linewidth=2)
    ax2.add_patch(circle_manas)
    ax2.text(0.8, 0.7, '末那識\n第七識', ha='center', va='center', fontsize=9)
    ax2.annotate('', xy=(0.8, 0.7), xytext=(0.65, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax2.text(0.725, 0.75, '思量能変\n(我執)', ha='center', fontsize=8, color='red')

    # Vijnapti-parinama (representation transformation)
    ax2.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='green'))
    ax2.text(0.5, 0.3, '前六識\n了境', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.6, 0.42, '了境能変\n(境の認識)', ha='center', fontsize=8, color='green')

    ax2.set_title('三能変：識はいかに万法を変現するか', fontsize=13, fontweight='bold')

    # === Seed-manifestation cycle diagram ===
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    rect_alaya = plt.Rectangle((0.2, 0.6), 0.6, 0.3,
                               facecolor='gold', edgecolor='black',
                               linewidth=3, alpha=0.6)
    ax3.add_patch(rect_alaya)
    ax3.text(0.5, 0.75, '阿頼耶識（種子庫）', ha='center',
            fontsize=12, fontweight='bold')

    seed_positions = [(0.3, 0.7), (0.4, 0.65), (0.5, 0.7), (0.6, 0.65), (0.7, 0.7)]
    for x, y in seed_positions:
        circle = plt.Circle((x, y), 0.03, color='brown', alpha=0.8)
        ax3.add_patch(circle)
        ax3.text(x, y, '種', ha='center', va='center', fontsize=7, color='white')

    ax3.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.6),
                arrowprops=dict(arrowstyle='->', lw=4, color='blue'))
    ax3.text(0.6, 0.5, '種子生現行', ha='left', fontsize=11, color='blue',
            fontweight='bold')

    manifestations = [
        (0.2, 0.3, '色'), (0.35, 0.25, '声'), (0.5, 0.3, '香'),
        (0.65, 0.25, '味'), (0.8, 0.3, '触'),
    ]
    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.05, color='lightgreen', alpha=0.8,
                           edgecolor='darkgreen', linewidth=2)
        ax3.add_patch(circle)
        ax3.text(x, y, label, ha='center', va='center', fontsize=10)

    ax3.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.4),
                arrowprops=dict(arrowstyle='->', lw=4, color='red',
                              connectionstyle="arc3,rad=.5"))
    ax3.text(0.3, 0.5, '現行薫種子', ha='right', fontsize=11, color='red',
            fontweight='bold')
    ax3.set_title('種子と現行：止まることなき循環', fontsize=13, fontweight='bold')
    ax3.text(0.5, 0.05, '種子→現行→新種子→現行...',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('eight_consciousnesses.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【唯識思想の八識】")
    print("="*70)
    print("\n前五識：眼・耳・鼻・舌・身（感覚識）")
    print("第六識：意識（思考・判断・記憶）")
    print("第七識：末那識（恒審思量、我執の根源）")
    print("第八識：阿頼耶識（蔵識、一切法の根源）")
    print("\n三能変：")
    print("  1. 異熟能変（第八識）→ 根身・器界を変現")
    print("  2. 思量能変（第七識）→ 「我」への執着")
    print("  3. 了境能変（前六識）→ 対象の認識")
    print("\n種子と現行の循環：種子→現行→新種子→...")
    print("\n量子論との対応：")
    print("  阿頼耶識 ≈ 量子場 | 種子 ≈ 場の励起モード")
    print("  現行 ≈ 実際の粒子 | 薫習 ≈ 場の時間発展")
    print("="*70)

# Execute
visualize_eight_consciousnesses()

def visualize_mind_matter_debate():
    """Visualize quantum interpretations of the mind-matter relationship"""

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Materialism (classical) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯物論（古典物理学）', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_matter = plt.Circle((0.3, 0.5), 0.15, color='blue', alpha=0.6,
                              edgecolor='black', linewidth=3)
    ax.add_patch(circle_matter)
    ax.text(0.3, 0.5, '物質\n(客観)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_mind = plt.Circle((0.7, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='black', linewidth=2)
    ax.add_patch(circle_mind)
    ax.text(0.7, 0.5, '心\n(主観)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, '決定', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, '物質が基礎、心は副産物',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
           transform=ax.transAxes)

    # === Idealism (classical) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯心論（古典哲学）', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_mind = plt.Circle((0.3, 0.5), 0.15, color='red', alpha=0.6,
                            edgecolor='black', linewidth=3)
    ax.add_patch(circle_mind)
    ax.text(0.3, 0.5, '心\n(本体)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_matter = plt.Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                              edgecolor='black', linewidth=2)
    ax.add_patch(circle_matter)
    ax.text(0.7, 0.5, '物質\n(顕現)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, '変現', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, '心が基礎、物質は心の顕れ',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
           transform=ax.transAxes)

    # === Quantum mechanics perspective ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '量子力学', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle1 = plt.Circle((0.45, 0.55), 0.12, color='red', alpha=0.4,
                        edgecolor='red', linewidth=2)
    circle2 = plt.Circle((0.55, 0.45), 0.12, color='blue', alpha=0.4,
                        edgecolor='blue', linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.text(0.45, 0.55, '観測者', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.text(0.55, 0.45, '系', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.annotate('', xy=(0.55, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.25, '観測が系に影響し\n系もまた観測に影響する', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(0.5, 0.05, '心と物は分離できない',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
           transform=ax.transAxes)

    # === Yogacara perspective ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯識思想', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_consciousness = plt.Circle((0.5, 0.5), 0.18, color='gold', alpha=0.6,
                                     edgecolor='black', linewidth=3)
    ax.add_patch(circle_consciousness)
    ax.text(0.5, 0.5, '識\n(阿頼耶識)', ha='center', va='center',
           fontsize=12, fontweight='bold')

    manifestations = [
        (0.3, 0.75, '色'), (0.7, 0.75, '声'), (0.25, 0.5, '香'),
        (0.75, 0.5, '味'), (0.3, 0.25, '触'), (0.7, 0.25, '法'),
    ]
    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.06, color='lightblue', alpha=0.7,
                           edgecolor='blue', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)

        dx = x - 0.5
        dy = y - 0.5
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length
        dy_norm = dy / length
        start_x = 0.5 + dx_norm * 0.18
        start_y = 0.5 + dy_norm * 0.18
        end_x = x - dx_norm * 0.06
        end_y = y - dy_norm * 0.06
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='purple', alpha=0.6))

    ax.text(0.5, 0.05, '万法唯識\n一切は識の変現',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
           transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('mind_matter_debate.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【唯心論 vs 唯物論：量子力学と唯識の視点】")
    print("="*70)
    print("\n唯物論：物質が意識を決定する、客観は観測者から独立")
    print("唯心論：心が唯一の実在、物質は心の顕れ")
    print("量子力学：観測者が系に影響する、心と物は分離不可能")
    print("唯識思想：三界唯心、万法唯識——外界の本質は識")
    print("\n量子場の理論と唯識に共通する洞察：")
    print("  場/識が本体であり、粒子/法はその顕現")
    print("  場から独立した粒子はなく、識から独立した法はない")
    print("\n一つの可能な答え：")
    print("  「物質」も「心」も最も根本的なものではない")
    print("  最も根本的なのは「場/識」")
    print("  両者は同一の実在の異なる側面")
    print("="*70)

# Execute
visualize_mind_matter_debate()
