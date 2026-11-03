# Code & Cogito: コペンハーゲン解釈 vs 京都学派——二つの叡智の対話
# Article: https://code-cogito.com/ja/copenhagen-interpretation-vs-kyoto-school-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

# | |ψ⟩ = Σ cᵢ|φᵢ⟩

# | Δx · Δp ≥ ℏ/2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class DoubleSlit:
    """
    Double-slit experiment simulation
    Demonstrates the dramatic difference between observed and unobserved cases
    """

    def __init__(self):
        self.observed = False
        self.screen_resolution = 500

    def simulate_unobserved(self):
        """Unobserved: photon behaves as wave, producing interference pattern"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # Double-slit wave sources
        slit1_pos = -1.0
        slit2_pos = 1.0
        wavelength = 0.5

        # Waves from two slits
        wave1 = np.sin(2 * np.pi * (y - slit1_pos) / wavelength)
        wave2 = np.sin(2 * np.pi * (y - slit2_pos) / wavelength)

        # Superposition (interference)
        total_wave = wave1 + wave2
        intensity = np.abs(total_wave)**2
        intensity = intensity / np.max(intensity)

        return y, intensity

    def simulate_observed(self):
        """Observed: measuring which slit each photon passes through destroys interference"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # After observation, each photon passes through only one slit
        slit1_pattern = np.exp(-(y - (-1.0))**2 / 0.5)
        slit2_pattern = np.exp(-(y - (1.0))**2 / 0.5)

        # Simple addition (no interference)
        intensity = slit1_pattern + slit2_pattern
        intensity = intensity / np.max(intensity)

        return y, intensity

    def visualize_comparison(self):
        """Side-by-side comparison: observed vs unobserved"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Left: unobserved (wave behavior)
        y_unobs, intensity_unobs = self.simulate_unobserved()
        ax1.fill_between(y_unobs, 0, intensity_unobs, alpha=0.7, color='blue')
        ax1.plot(y_unobs, intensity_unobs, 'b-', linewidth=2)
        ax1.set_xlabel('スクリーン位置', fontsize=13)
        ax1.set_ylabel('光子到達数', fontsize=13)
        ax1.set_title('観測なし：干渉縞が出現 → 波動性',
                     fontsize=14, fontweight='bold', color='blue')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.2)
        ax1.text(0, 1.1, '複数のピーク＝干渉縞\n光子は「波」のように振る舞う',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # Right: observed (particle behavior)
        y_obs, intensity_obs = self.simulate_observed()
        ax2.fill_between(y_obs, 0, intensity_obs, alpha=0.7, color='red')
        ax2.plot(y_obs, intensity_obs, 'r-', linewidth=2)
        ax2.set_xlabel('スクリーン位置', fontsize=13)
        ax2.set_ylabel('光子到達数', fontsize=13)
        ax2.set_title('観測あり：干渉縞が消失 → 粒子性',
                     fontsize=14, fontweight='bold', color='red')
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 1.2)
        ax2.text(0, 1.1, '2つのピーク＝干渉なし\n光子は「粒子」のように振る舞う',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        fig.text(0.5, 0.02,
                '核心的洞察：観測が実験結果を変えた！これは測定誤差ではなく、量子世界の本質です。\n'
                '禅の視点：「主客不分」——観察者と被観察物はもとより一体である。',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.12)
        plt.savefig('double_slit_observer_effect.png', dpi=300, bbox_inches='tight')
        plt.show()

# Execute
experiment = DoubleSlit()
experiment.visualize_comparison()

print("\n" + "="*70)
print("【二重スリット実験：観測者効果】")
print("="*70)
print("量子力学：観測が現実を変える")
print("禅　　：主客はもとより不分")

def taiji_and_complementarity():
    """Taiji diagram and complementarity principle"""
    fig = plt.figure(figsize=(16, 6))

    # Left: classical Taiji diagram
    ax1 = fig.add_subplot(131)
    theta = np.linspace(0, 2*np.pi, 1000)

    # S-curve boundary
    r_yin = 1 + 0.5 * np.sin(theta)
    r_yang = 1 - 0.5 * np.sin(theta)

    # Draw yin-yang
    ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
            color='black', alpha=0.8)
    ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
            color='white', edgecolor='black', linewidth=2)

    # Yang within Yin (white dot)
    circle_yang = plt.Circle((0, 0.5), 0.15, color='white', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yang)

    # Yin within Yang (black dot)
    circle_yin = plt.Circle((0, -0.5), 0.15, color='black', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yin)

    # Outer circle
    circle_outer = plt.Circle((0, 0), 1.5, fill=False, edgecolor='black', linewidth=3)
    ax1.add_patch(circle_outer)

    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('太極図（明代に定着した形）\n対立統一、陰陽相補',
                 fontsize=13, fontweight='bold')

    ax1.text(0, -2.3, '• 陰の中に陽あり、陽の中に陰あり\n• 対立面は互いに依存する',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Center: wave-particle duality
    ax2 = fig.add_subplot(132, projection='polar')

    theta_wave = np.linspace(0, np.pi, 100)
    r_wave = np.ones_like(theta_wave)
    ax2.fill_between(theta_wave, 0, r_wave, alpha=0.7, color='blue', label='波動性')

    theta_particle = np.linspace(np.pi, 2*np.pi, 100)
    r_particle = np.ones_like(theta_particle)
    ax2.fill_between(theta_particle, 0, r_particle, alpha=0.7, color='red', label='粒子性')

    ax2.set_ylim(0, 1.2)
    ax2.set_title('波粒二重性（ボーア、1927）\n相補性原理',
                 fontsize=13, fontweight='bold', pad=20)
    ax2.legend(loc='upper right')

    # Right: Bloch sphere
    ax3 = fig.add_subplot(133, projection='3d')

    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax3.plot_surface(x, y, z, alpha=0.2, color='gray')

    # Mark special states
    ax3.scatter([0], [0], [1], c='blue', s=200, label='|0⟩')
    ax3.scatter([0], [0], [-1], c='red', s=200, label='|1⟩')
    ax3.scatter([1], [0], [0], c='purple', s=200, label='重ね合わせ状態')

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('ブロッホ球：量子状態空間', fontsize=13, fontweight='bold')
    ax3.legend()

    plt.tight_layout()
    plt.savefig('taiji_complementarity.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【太極図と相補性原理の数学的対応】")
    print("="*70)
    print("陰陽        ↔ |0⟩ と |1⟩")
    print("対立統一    ↔ 重ね合わせ状態 α|0⟩+β|1⟩")
    print("相補        ↔ 非可換観測量 [x,p]=iℏ")
    print("="*70)

# Execute
taiji_and_complementarity()

def wave_function_collapse_zen():
    """Wave function collapse vs Zen satori"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    times = ['測定前', '測定中', '測定後']
    x = np.linspace(-5, 5, 1000)

    # Upper row: quantum mechanics
    for i, (ax, time_label) in enumerate(zip(axes[0], times)):
        if i < 2:
            # Before measurement: wave packet
            psi_real = np.exp(-x**2/2) * np.cos(3*x)
            prob = np.exp(-x**2)

            ax.plot(x, psi_real, 'b-', label='ψ 実部', linewidth=1.5)
            ax.fill_between(x, 0, prob, alpha=0.3, color='purple', label='確率密度')
            ax.set_title(f'{time_label}\n無限の可能性', fontsize=12, fontweight='bold')
            ax.text(0, 1.3, '粒子は「ここにもあそこにも同時に」',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
        else:
            # After measurement: collapse
            measured_pos = 1.5
            collapsed = np.zeros_like(x)
            collapsed[np.abs(x - measured_pos) < 0.1] = 10

            ax.bar(x[np.abs(x - measured_pos) < 0.1],
                  collapsed[np.abs(x - measured_pos) < 0.1],
                  width=0.1, color='red', alpha=0.8)
            ax.set_title(f'{time_label}\n位置が確定', fontsize=12, fontweight='bold', color='red')
            ax.text(0, 11, f'粒子の位置が x={measured_pos} に確定',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        ax.set_xlabel('位置 x')
        ax.set_ylabel('波動関数')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-1.5, 12)

    # Lower row: Zen
    zen_states = [
        ('迷', 'blue', '分別心がまだ生じていない'),
        ('悟りの途上', 'purple', '覚察が立ち上がる'),
        ('悟', 'red', '見性成仏')
    ]

    for i, (ax, (state, color, desc)) in enumerate(zip(axes[1], zen_states)):
        if i < 2:
            # Before satori: scattered mind
            np.random.seed(42 + i)
            n_thoughts = 50
            thoughts_x = np.random.randn(n_thoughts) * 2
            thoughts_y = np.random.randn(n_thoughts) * 2

            ax.scatter(thoughts_x, thoughts_y, s=100, alpha=0.6, c=color)
            ax.set_title(f'{state}\n{desc}', fontsize=12, fontweight='bold', color=color)
            ax.text(0, 5, '妄念紛飛',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
        else:
            # After satori: clear mind
            circle = plt.Circle((0, 0), 2, color=color, alpha=0.5)
            ax.add_patch(circle)
            ax.plot(0, 0, 'o', markersize=30, color='gold',
                   markeredgecolor='red', markeredgewidth=3)
            ax.set_title(f'{state}\n{desc}', fontsize=12, fontweight='bold', color=color)
            ax.text(0, 4, '頓悟！「本来無一物」',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

    fig.text(0.5, 0.98,
            '波動関数の収縮 vs 禅の頓悟：観察の瞬間',
            ha='center', fontsize=16, fontweight='bold')

    fig.text(0.5, 0.02,
            '量子力学：測定の瞬間、可能性→現実\n禅：覚察の瞬間、妄念→本性',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.subplots_adjust(top=0.95, bottom=0.12)
    plt.savefig('collapse_vs_enlightenment.png', dpi=300, bbox_inches='tight')
    plt.show()

# Execute
wave_function_collapse_zen()
