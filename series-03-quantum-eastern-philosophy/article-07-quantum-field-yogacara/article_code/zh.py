# Code & Cogito: 量子場論 vs 佛教「唯識」——物質是心的顯現
# Article: https://code-cogito.com/quantum-field-theory-yogacara/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumFieldSimulator:
    """
    量子場模擬器
    展示：場如何激發，產生粒子
    """

    def __init__(self, size=100):
        self.size = size
        self.x = np.linspace(-10, 10, size)
        self.y = np.linspace(-10, 10, size)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def field_vacuum(self):
        """真空態：場的基態，微小的量子漲落"""
        fluctuation = np.random.randn(self.size, self.size) * 0.1
        return fluctuation

    def field_one_particle(self, x0=0, y0=0, k=1):
        """一粒子態：場的激發（高斯波包）"""
        R = np.sqrt((self.X - x0)**2 + (self.Y - y0)**2)
        particle = 2.0 * np.exp(-R**2 / 2) * np.cos(k * R)
        vacuum = self.field_vacuum()
        return particle + vacuum

    def field_two_particles(self, x1=-3, y1=0, x2=3, y2=0):
        """二粒子態：兩個激發"""
        R1 = np.sqrt((self.X - x1)**2 + (self.Y - y1)**2)
        R2 = np.sqrt((self.X - x2)**2 + (self.Y - y2)**2)
        particle1 = 2.0 * np.exp(-R1**2 / 2) * np.cos(2 * R1)
        particle2 = 2.0 * np.exp(-R2**2 / 2) * np.cos(2 * R2)
        vacuum = self.field_vacuum()
        return particle1 + particle2 + vacuum

    def visualize_field_states(self):
        """視覺化不同的場態"""
        fig = plt.figure(figsize=(18, 12))

        # === 真空態 ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')
        vacuum = self.field_vacuum()
        surf1 = ax1.plot_surface(self.X, self.Y, vacuum, cmap='coolwarm',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax1.set_title('真空態 |0⟩\n場的基態（量子漲落）',
                     fontsize=13, fontweight='bold')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('場強度')
        ax1.set_zlim(-3, 3)

        # === 一粒子態 ===
        ax2 = fig.add_subplot(2, 3, 2, projection='3d')
        one_particle = self.field_one_particle(x0=0, y0=0)
        surf2 = ax2.plot_surface(self.X, self.Y, one_particle, cmap='viridis',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax2.set_title('一粒子態 â†|0⟩\n場的局域激發',
                     fontsize=13, fontweight='bold')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('場強度')
        ax2.set_zlim(-3, 3)

        # === 二粒子態 ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')
        two_particles = self.field_two_particles()
        surf3 = ax3.plot_surface(self.X, self.Y, two_particles, cmap='plasma',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax3.set_title('二粒子態 â†â†|0⟩\n兩個局域激發',
                     fontsize=13, fontweight='bold')
        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('場強度')
        ax3.set_zlim(-3, 3)

        # === 真空能量密度（截面）===
        ax4 = fig.add_subplot(2, 3, 4)
        vacuum_slice = vacuum[self.size//2, :]
        ax4.plot(self.x, vacuum_slice, 'b-', linewidth=2)
        ax4.fill_between(self.x, 0, vacuum_slice, alpha=0.3, color='blue')
        ax4.set_xlabel('位置 X', fontsize=11)
        ax4.set_ylabel('場強度', fontsize=11)
        ax4.set_title('真空的量子漲落（X軸截面）', fontsize=12, fontweight='bold')
        ax4.grid(True, alpha=0.3)
        ax4.axhline(0, color='black', linewidth=0.5)

        # === 一粒子能量密度（截面）===
        ax5 = fig.add_subplot(2, 3, 5)
        one_particle_slice = one_particle[self.size//2, :]
        ax5.plot(self.x, one_particle_slice, 'g-', linewidth=2)
        ax5.fill_between(self.x, 0, one_particle_slice, alpha=0.3, color='green')
        ax5.set_xlabel('位置 X', fontsize=11)
        ax5.set_ylabel('場強度', fontsize=11)
        ax5.set_title('粒子 = 場的局域激發（X軸截面）', fontsize=12, fontweight='bold')
        ax5.grid(True, alpha=0.3)
        ax5.axhline(0, color='black', linewidth=0.5)

        # === 對應說明 ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text = '''
        【量子場論 vs 唯識宗】

        量子場論：
        • 場 = 基礎實在
        • 粒子 = 場的激發
        • 真空 ≠ 空無

        唯識宗：
        • 識 = 基礎實在
        • 萬法 = 識的變現
        • 阿賴耶識 ≠ 空

        共同洞見：
        ✓ 「物」不是基礎
        ✓ 「場/識」才是本體
        ✓ 顯現依賴激發/變現
        '''

        ax6.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('quantum_field_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子場與粒子】")
        print("="*70)
        print("\n經典物理：粒子 = 基本實體，有固定位置和速度")
        print("量子場論：場 = 基本實體，粒子 = 場的激發態")
        print("\n唯識類比：")
        print("  阿賴耶識 ≈ 量子場")
        print("  種子 ≈ 場的潛在激發模式")
        print("  現行 ≈ 場的實際激發（粒子）")
        print("\n量子場論：「粒子不是『東西』。粒子只是場的激發。」")
        print("唯識：「萬法不是『實體』。萬法只是識的變現。」")
        print("="*70)

# 執行
simulator = QuantumFieldSimulator(size=100)
simulator.visualize_field_states()

class VirtualParticleSimulator:
    """虛粒子模擬器：展示真空中虛粒子的生滅"""

    def __init__(self):
        pass

    def visualize_vacuum_fluctuations(self):
        """視覺化真空漲落"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === 左圖：虛粒子生滅的時空圖 ===
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
        ax1.set_title('真空中的虛粒子生滅\n海森堡不確定性：ΔE·Δt ≥ ℏ/2',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, 10)
        ax1.set_ylim(-3, 3)

        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='r', linewidth=2, label='粒子'),
            Line2D([0], [0], color='b', linewidth=2, linestyle='--', label='反粒子'),
            Line2D([0], [0], marker='*', color='purple', markersize=12,
                  linestyle='None', label='湮滅'),
        ]
        ax1.legend(handles=legend_elements, fontsize=11)

        # === 右圖：費曼圖示例（電子-電子散射）===
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        ax2.text(0.5, 0.95, '費曼圖：電子-電子散射',
                ha='center', fontsize=14, fontweight='bold',
                transform=ax2.transAxes)

        # 入射與出射電子
        ax2.arrow(0.1, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.25, 'e⁻', fontsize=12, ha='center')
        ax2.arrow(0.1, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.75, 'e⁻', fontsize=12, ha='center')

        # 虛光子交換
        ax2.plot([0.35, 0.35], [0.3, 0.7], 'r', linewidth=3,
                linestyle='dotted', alpha=0.7)
        ax2.text(0.42, 0.5, '虛光子\nγ*', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        ax2.arrow(0.35, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.25, 'e⁻', fontsize=12, ha='center')
        ax2.arrow(0.35, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.75, 'e⁻', fontsize=12, ha='center')

        explanation = '''
        費曼圖規則：
        • 實線 → 真實粒子
        • 虛線 → 虛粒子
        • 頂點 → 相互作用

        虛光子特性：
        • 壽命極短
        • 不能直接觀測
        • 但真實影響相互作用
        '''
        ax2.text(0.5, 0.15, explanation, fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        plt.tight_layout()
        plt.savefig('virtual_particles_feynman.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【虛粒子與真空能量】")
        print("="*70)
        print("\n海森堡不確定性原理：ΔE · Δt ≥ ℏ/2")
        print("→ 真空中不斷有虛粒子對產生和湮滅")
        print("\n卡西米爾效應（1948預言，1997實驗證實）：")
        print("  → 證明：真空不空！")
        print("\n唯識類比：")
        print("  阿賴耶識 = 真空（充滿潛能）")
        print("  種子生現行 = 虛粒子實現")
        print("  現行還滅 = 虛粒子湮滅")
        print("\n深刻洞見：「空」不是「無」，「空」是充滿潛能的「有」")
        print("="*70)

# 執行
virtual_sim = VirtualParticleSimulator()
virtual_sim.visualize_vacuum_fluctuations()

def visualize_eight_consciousnesses():
    """視覺化唯識宗的八識結構"""

    fig = plt.figure(figsize=(18, 12))

    # === 八識層次圖 ===
    ax1 = fig.add_subplot(2, 2, (1, 2))
    ax1.axis('off')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    consciousnesses = [
        (9, '第八識\n阿賴耶識\n(藏識)', 'gold', 2.5, '一切種子識\n根本識'),
        (7.5, '第七識\n末那識', 'orange', 2.0, '恆審思量\n我執根源'),
        (6, '第六識\n意識', 'red', 1.8, '思考判斷\n記憶想像'),
        (4.8, '眼識', 'lightblue', 0.8, '視覺'),
        (4.0, '耳識', 'lightblue', 0.8, '聽覺'),
        (3.2, '鼻識', 'lightblue', 0.8, '嗅覺'),
        (2.4, '舌識', 'lightblue', 0.8, '味覺'),
        (1.6, '身識', 'lightblue', 0.8, '觸覺'),
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

    # 箭頭：前五識 → 第六識
    for y in [4.8, 4.0, 3.2, 2.4, 1.6]:
        ax1.annotate('', xy=(5, 6), xytext=(5.5, y),
                    arrowprops=dict(arrowstyle='->', lw=1.5,
                                  color='blue', alpha=0.5))
    # 第六識 ↔ 第七識 ↔ 第八識
    ax1.annotate('', xy=(5, 7.5), xytext=(5, 6.3),
                arrowprops=dict(arrowstyle='<->', lw=2, color='red', alpha=0.6))
    ax1.annotate('', xy=(5, 9), xytext=(5, 7.8),
                arrowprops=dict(arrowstyle='<->', lw=2, color='purple', alpha=0.6))

    ax1.set_title('唯識宗：八識的層次結構', fontsize=16, fontweight='bold')

    # === 三能變圖 ===
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    circle_center = plt.Circle((0.5, 0.7), 0.15, color='gold', alpha=0.7,
                              edgecolor='black', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.7, '阿賴耶識\n第八識', ha='center', va='center',
            fontsize=11, fontweight='bold')

    # 異熟能變
    ax2.annotate('', xy=(0.2, 0.4), xytext=(0.4, 0.6),
                arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
    ax2.text(0.2, 0.4, '根身\n器界', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.text(0.1, 0.55, '異熟能變\n(變現世界)', ha='center', fontsize=8, color='blue')

    # 思量能變
    circle_manas = plt.Circle((0.8, 0.7), 0.1, color='orange', alpha=0.6,
                             edgecolor='black', linewidth=2)
    ax2.add_patch(circle_manas)
    ax2.text(0.8, 0.7, '末那識\n第七識', ha='center', va='center', fontsize=9)
    ax2.annotate('', xy=(0.8, 0.7), xytext=(0.65, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax2.text(0.725, 0.75, '思量能變\n(執我)', ha='center', fontsize=8, color='red')

    # 了境能變
    ax2.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='green'))
    ax2.text(0.5, 0.3, '前六識\n了境', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.6, 0.42, '了境能變\n(認識境)', ha='center', fontsize=8, color='green')

    ax2.set_title('三能變：識如何變現萬法', fontsize=13, fontweight='bold')

    # === 種子現行圖 ===
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    rect_alaya = plt.Rectangle((0.2, 0.6), 0.6, 0.3,
                               facecolor='gold', edgecolor='black',
                               linewidth=3, alpha=0.6)
    ax3.add_patch(rect_alaya)
    ax3.text(0.5, 0.75, '阿賴耶識（種子庫）', ha='center',
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
        (0.2, 0.3, '色'), (0.35, 0.25, '聲'), (0.5, 0.3, '香'),
        (0.65, 0.25, '味'), (0.8, 0.3, '觸'),
    ]
    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.05, color='lightgreen', alpha=0.8,
                           edgecolor='darkgreen', linewidth=2)
        ax3.add_patch(circle)
        ax3.text(x, y, label, ha='center', va='center', fontsize=10)

    ax3.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.4),
                arrowprops=dict(arrowstyle='->', lw=4, color='red',
                              connectionstyle="arc3,rad=.5"))
    ax3.text(0.3, 0.5, '現行熏種子', ha='right', fontsize=11, color='red',
            fontweight='bold')
    ax3.set_title('種子與現行：循環不息', fontsize=13, fontweight='bold')
    ax3.text(0.5, 0.05, '種子→現行→新種子→現行...',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('eight_consciousnesses.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【唯識宗的八識】")
    print("="*70)
    print("\n前五識：眼、耳、鼻、舌、身（感官識）")
    print("第六識：意識（思考、判斷、記憶）")
    print("第七識：末那識（恆審思量「我」，我執根源）")
    print("第八識：阿賴耶識（藏識，一切法的根源）")
    print("\n三能變：")
    print("  1. 異熟能變（第八識）→ 變現根身、器界")
    print("  2. 思量能變（第七識）→ 執著「我」")
    print("  3. 了境能變（前六識）→ 認識對象")
    print("\n種子與現行循環：種子→現行→新種子→...")
    print("\n量子類比：")
    print("  阿賴耶識 ≈ 量子場 | 種子 ≈ 場的激發模式")
    print("  現行 ≈ 實際粒子 | 熏習 ≈ 場的演化")
    print("="*70)

# 執行
visualize_eight_consciousnesses()

def visualize_mind_matter_debate():
    """視覺化唯心vs唯物的量子詮釋"""

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === 唯物論（經典） ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯物論（經典物理）', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_matter = plt.Circle((0.3, 0.5), 0.15, color='blue', alpha=0.6,
                              edgecolor='black', linewidth=3)
    ax.add_patch(circle_matter)
    ax.text(0.3, 0.5, '物質\n(客觀)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_mind = plt.Circle((0.7, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='black', linewidth=2)
    ax.add_patch(circle_mind)
    ax.text(0.7, 0.5, '心\n(主觀)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, '決定', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, '物質是基礎，心是副產品',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
           transform=ax.transAxes)

    # === 唯心論（古典） ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯心論（古典哲學）', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_mind = plt.Circle((0.3, 0.5), 0.15, color='red', alpha=0.6,
                            edgecolor='black', linewidth=3)
    ax.add_patch(circle_mind)
    ax.text(0.3, 0.5, '心\n(本體)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_matter = plt.Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                              edgecolor='black', linewidth=2)
    ax.add_patch(circle_matter)
    ax.text(0.7, 0.5, '物質\n(顯現)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, '變現', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, '心是基礎，物質是心的顯現',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
           transform=ax.transAxes)

    # === 量子力學的觀點 ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '量子力學', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle1 = plt.Circle((0.45, 0.55), 0.12, color='red', alpha=0.4,
                        edgecolor='red', linewidth=2)
    circle2 = plt.Circle((0.55, 0.45), 0.12, color='blue', alpha=0.4,
                        edgecolor='blue', linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.text(0.45, 0.55, '觀察者', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.text(0.55, 0.45, '系統', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.annotate('', xy=(0.55, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.25, '觀察影響系統\n系統也影響觀察', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(0.5, 0.05, '心與物不可分離',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
           transform=ax.transAxes)

    # === 唯識宗的觀點 ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, '唯識宗', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_consciousness = plt.Circle((0.5, 0.5), 0.18, color='gold', alpha=0.6,
                                     edgecolor='black', linewidth=3)
    ax.add_patch(circle_consciousness)
    ax.text(0.5, 0.5, '識\n(阿賴耶識)', ha='center', va='center',
           fontsize=12, fontweight='bold')

    manifestations = [
        (0.3, 0.75, '色'), (0.7, 0.75, '聲'), (0.25, 0.5, '香'),
        (0.75, 0.5, '味'), (0.3, 0.25, '觸'), (0.7, 0.25, '法'),
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

    ax.text(0.5, 0.05, '萬法唯識\n一切皆是識的變現',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
           transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('mind_matter_debate.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【唯心vs唯物：量子與唯識的觀點】")
    print("="*70)
    print("\n唯物論：物質決定意識，客觀獨立於觀察者")
    print("唯心論：心是唯一實在，物質是心的顯現")
    print("量子力學：觀察者影響系統，心與物無法分離")
    print("唯識宗：三界唯心，萬法唯識——外境的本質是識")
    print("\n量子場論與唯識的共同洞見：")
    print("  場/識是本體，粒子/法是顯現")
    print("  沒有獨立於場的粒子，沒有獨立於識的法")
    print("\n可能的答案：")
    print("  「物質」和「心」都不是最基礎的")
    print("  最基礎的是「場/識」")
    print("  兩者是同一實在的不同面向")
    print("="*70)

# 執行
visualize_mind_matter_debate()
