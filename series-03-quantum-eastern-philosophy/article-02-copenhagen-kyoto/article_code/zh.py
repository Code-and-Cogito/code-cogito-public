# Code & Cogito: 哥本哈根詮釋 vs 京都學派——兩種智慧的對話
# Article: https://code-cogito.com/copenhagen-interpretation-vs-kyoto-school/
# All the code blocks of the article, in order. Program output is kept as comments.

# | |ψ⟩ = Σ cᵢ|φᵢ⟩

# | Δx · Δp ≥ ℏ/2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class DoubleSlit:
    """
    雙縫實驗模擬
    展示：觀察vs不觀察的巨大差異
    """

    def __init__(self):
        self.observed = False
        self.screen_resolution = 500

    def simulate_unobserved(self):
        """不觀察：光子表現為波，產生干涉條紋"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # 雙縫波源
        slit1_pos = -1.0
        slit2_pos = 1.0
        wavelength = 0.5

        # 來自兩個縫的波
        wave1 = np.sin(2 * np.pi * (y - slit1_pos) / wavelength)
        wave2 = np.sin(2 * np.pi * (y - slit2_pos) / wavelength)

        # 疊加（干涉）
        total_wave = wave1 + wave2
        intensity = np.abs(total_wave)**2
        intensity = intensity / np.max(intensity)

        return y, intensity

    def simulate_observed(self):
        """觀察：測量每個光子走哪條縫，破壞干涉"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # 觀察後，每個光子只走一條縫
        slit1_pattern = np.exp(-(y - (-1.0))**2 / 0.5)
        slit2_pattern = np.exp(-(y - (1.0))**2 / 0.5)

        # 簡單相加（沒有干涉）
        intensity = slit1_pattern + slit2_pattern
        intensity = intensity / np.max(intensity)

        return y, intensity

    def visualize_comparison(self):
        """並排比較：觀察 vs 不觀察"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # 左圖：不觀察（波動性）
        y_unobs, intensity_unobs = self.simulate_unobserved()
        ax1.fill_between(y_unobs, 0, intensity_unobs, alpha=0.7, color='blue')
        ax1.plot(y_unobs, intensity_unobs, 'b-', linewidth=2)
        ax1.set_xlabel('屏幕位置', fontsize=13)
        ax1.set_ylabel('光子擊中數量', fontsize=13)
        ax1.set_title('不觀察：出現干涉條紋 → 波動性',
                     fontsize=14, fontweight='bold', color='blue')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.2)
        ax1.text(0, 1.1, '多個峰值 = 干涉條紋\n光子像「波」',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # 右圖：觀察（粒子性）
        y_obs, intensity_obs = self.simulate_observed()
        ax2.fill_between(y_obs, 0, intensity_obs, alpha=0.7, color='red')
        ax2.plot(y_obs, intensity_obs, 'r-', linewidth=2)
        ax2.set_xlabel('屏幕位置', fontsize=13)
        ax2.set_ylabel('光子擊中數量', fontsize=13)
        ax2.set_title('觀察：干涉條紋消失 → 粒子性',
                     fontsize=14, fontweight='bold', color='red')
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 1.2)
        ax2.text(0, 1.1, '兩個峰值 = 無干涉\n光子像「粒子」',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        fig.text(0.5, 0.02,
                '關鍵洞見：觀察改變了實驗結果！這不是測量誤差，是量子世界的本質。\n'
                '禪宗觀點：「主客不分」——觀察者與被觀察物本來就是一體的。',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.12)
        plt.savefig('double_slit_observer_effect.png', dpi=300, bbox_inches='tight')
        plt.show()

# 執行
experiment = DoubleSlit()
experiment.visualize_comparison()

print("\n" + "="*70)
print("【雙縫實驗：觀察者效應】")
print("="*70)
print("量子力學：觀察改變現實")
print("禪宗：    主客本來不分")

def taiji_and_complementarity():
    """太極圖與互補原理"""
    fig = plt.figure(figsize=(16, 6))

    # 左圖：經典太極圖
    ax1 = fig.add_subplot(131)
    theta = np.linspace(0, 2*np.pi, 1000)

    # S曲線分界
    r_yin = 1 + 0.5 * np.sin(theta)
    r_yang = 1 - 0.5 * np.sin(theta)

    # 繪製陰陽
    ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
            color='black', alpha=0.8)
    ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
            color='white', edgecolor='black', linewidth=2)

    # 陰中有陽（白點）
    circle_yang = plt.Circle((0, 0.5), 0.15, color='white', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yang)

    # 陽中有陰（黑點）
    circle_yin = plt.Circle((0, -0.5), 0.15, color='black', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yin)

    # 外圓
    circle_outer = plt.Circle((0, 0), 1.5, fill=False, edgecolor='black', linewidth=3)
    ax1.add_patch(circle_outer)

    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('太極圖（明代定型）\n對立統一，陰陽互補',
                 fontsize=13, fontweight='bold')

    ax1.text(0, -2.3, '• 陰中有陽，陽中有陰\n• 對立面相互依存',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 中圖：波粒二象性
    ax2 = fig.add_subplot(132, projection='polar')

    theta_wave = np.linspace(0, np.pi, 100)
    r_wave = np.ones_like(theta_wave)
    ax2.fill_between(theta_wave, 0, r_wave, alpha=0.7, color='blue', label='波動性')

    theta_particle = np.linspace(np.pi, 2*np.pi, 100)
    r_particle = np.ones_like(theta_particle)
    ax2.fill_between(theta_particle, 0, r_particle, alpha=0.7, color='red', label='粒子性')

    ax2.set_ylim(0, 1.2)
    ax2.set_title('波粒二象性（波耳，1927）\n互補原理',
                 fontsize=13, fontweight='bold', pad=20)
    ax2.legend(loc='upper right')

    # 右圖：Bloch球
    ax3 = fig.add_subplot(133, projection='3d')

    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax3.plot_surface(x, y, z, alpha=0.2, color='gray')

    # 標記特殊態
    ax3.scatter([0], [0], [1], c='blue', s=200, label='|0⟩')
    ax3.scatter([0], [0], [-1], c='red', s=200, label='|1⟩')
    ax3.scatter([1], [0], [0], c='purple', s=200, label='疊加態')

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('Bloch球：量子態空間', fontsize=13, fontweight='bold')
    ax3.legend()

    plt.tight_layout()
    plt.savefig('taiji_complementarity.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【太極與互補原理的數學對應】")
    print("="*70)
    print("陰陽        ↔ |0⟩ 和 |1⟩")
    print("對立統一    ↔ 疊加態 α|0⟩+β|1⟩")
    print("互補        ↔ 非對易觀測量 [x,p]=iℏ")
    print("="*70)

# 執行
taiji_and_complementarity()

def wave_function_collapse_zen():
    """波函數坍縮 vs 禪宗見性"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    times = ['測量前', '測量中', '測量後']
    x = np.linspace(-5, 5, 1000)

    # 上排：量子力學
    for i, (ax, time_label) in enumerate(zip(axes[0], times)):
        if i < 2:
            # 測量前：波包
            psi_real = np.exp(-x**2/2) * np.cos(3*x)
            prob = np.exp(-x**2)

            ax.plot(x, psi_real, 'b-', label='ψ 實部', linewidth=1.5)
            ax.fill_between(x, 0, prob, alpha=0.3, color='purple', label='機率密度')
            ax.set_title(f'{time_label}\n無限可能性', fontsize=12, fontweight='bold')
            ax.text(0, 1.3, '粒子「既在這裡又在那裡」',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
        else:
            # 測量後：坍縮
            measured_pos = 1.5
            collapsed = np.zeros_like(x)
            collapsed[np.abs(x - measured_pos) < 0.1] = 10

            ax.bar(x[np.abs(x - measured_pos) < 0.1],
                  collapsed[np.abs(x - measured_pos) < 0.1],
                  width=0.1, color='red', alpha=0.8)
            ax.set_title(f'{time_label}\n確定位置', fontsize=12, fontweight='bold', color='red')
            ax.text(0, 11, f'粒子確定在 x={measured_pos}',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        ax.set_xlabel('位置 x')
        ax.set_ylabel('波函數')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-1.5, 12)

    # 下排：禪宗
    zen_states = [
        ('迷', 'blue', '分別心未生'),
        ('悟中', 'purple', '覺察升起'),
        ('悟', 'red', '見性成佛')
    ]

    for i, (ax, (state, color, desc)) in enumerate(zip(axes[1], zen_states)):
        if i < 2:
            # 悟前：心識混亂
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
            # 悟後：一心清明
            circle = plt.Circle((0, 0), 2, color=color, alpha=0.5)
            ax.add_patch(circle)
            ax.plot(0, 0, 'o', markersize=30, color='gold',
                   markeredgecolor='red', markeredgewidth=3)
            ax.set_title(f'{state}\n{desc}', fontsize=12, fontweight='bold', color=color)
            ax.text(0, 4, '頓悟！「本來無一物」',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

    fig.text(0.5, 0.98,
            '波函數坍縮 vs 禪宗頓悟：觀察的瞬間',
            ha='center', fontsize=16, fontweight='bold')

    fig.text(0.5, 0.02,
            '量子：測量的瞬間，可能性→現實\n禪宗：覺察的瞬間，妄念→本性',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.subplots_adjust(top=0.95, bottom=0.12)
    plt.savefig('collapse_vs_enlightenment.png', dpi=300, bbox_inches='tight')
    plt.show()

# 執行
wave_function_collapse_zen()
