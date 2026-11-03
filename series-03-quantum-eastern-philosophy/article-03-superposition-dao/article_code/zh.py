# Code & Cogito: 量子疊加態 vs 老莊的「道」——在存在與不存在之間
# Article: https://code-cogito.com/quantum-superposition-taoism-dao/
# All the code blocks of the article, in order. Program output is kept as comments.

# | P(總) = P(可能性1) + P(可能性2)

# | P(總) = |α₁ + α₂|²

# | P(總) = |α₁|² + |α₂|² + 2Re(α₁*α₂*)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class SchrodingerCat:
    """
    薛丁格的貓完整模擬
    包含：原子狀態、貓狀態、時間演化、測量
    """

    def __init__(self, half_life=1.0):
        self.half_life = half_life
        self.lambda_decay = np.log(2) / half_life  # 衰變常數

    def atom_state(self, t):
        """原子在時間t的量子態：|ψ⟩ = α|未衰變⟩ + β|已衰變⟩"""
        alpha = np.sqrt(np.exp(-self.lambda_decay * t))
        beta = np.sqrt(1 - np.exp(-self.lambda_decay * t))
        return alpha, beta

    def cat_state(self, t):
        """貓的狀態隨時間演化：|貓⟩ = α|活⟩ + β|死⟩"""
        alpha, beta = self.atom_state(t)
        prob_alive = np.abs(alpha)**2
        prob_dead = np.abs(beta)**2
        return prob_alive, prob_dead

    def measure(self, t):
        """打開盒子，測量貓的狀態——波函數坍縮"""
        prob_alive, prob_dead = self.cat_state(t)
        outcome = np.random.choice(['alive', 'dead'],
                                  p=[prob_alive, prob_dead])
        return outcome

    def visualize_evolution(self, max_time=3.0):
        """視覺化貓的量子態隨時間演化"""
        times = np.linspace(0, max_time, 100)
        probs_alive = []
        probs_dead = []

        for t in times:
            p_alive, p_dead = self.cat_state(t)
            probs_alive.append(p_alive)
            probs_dead.append(p_dead)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # === 上圖：機率演化 ===
        ax1.fill_between(times, 0, probs_alive, alpha=0.6, color='green', label='P(貓活)')
        ax1.fill_between(times, 0, probs_dead, alpha=0.6, color='red', label='P(貓死)')
        ax1.plot(times, probs_alive, 'g-', linewidth=2)
        ax1.plot(times, probs_dead, 'r-', linewidth=2)

        ax1.set_xlabel('時間（小時）', fontsize=13)
        ax1.set_ylabel('機率', fontsize=13)
        ax1.set_title('薛丁格的貓：疊加態隨時間演化\n（打開盒子前）',
                     fontsize=15, fontweight='bold')
        ax1.legend(fontsize=12, loc='center right')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.1)

        # 標註半衰期
        ax1.axvline(self.half_life, color='black', linestyle='--', linewidth=2,
                   label=f'半衰期 = {self.half_life}小時')
        ax1.text(self.half_life + 0.1, 0.9,
                f'半衰期\n此時P(活)=P(死)=50%',
                fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

        ax1.text(max_time * 0.5, 0.3,
                '重要：這不是「貓要麼死要麼活」！\n'
                '而是「貓同時既死又活」！\n'
                '量子態 |貓⟩ = α|活⟩ + β|死⟩',
                fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # === 下圖：Bloch球表示 ===
        ax2 = fig.add_subplot(212, projection='3d')

        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='gray')

        for i, t in enumerate(times[::5]):
            alpha, beta = self.atom_state(t)
            theta = 2 * np.arctan2(np.abs(beta), np.abs(alpha))
            phi = 0
            x = np.sin(theta) * np.cos(phi)
            y = np.sin(theta) * np.sin(phi)
            z = np.cos(theta)
            color = plt.cm.RdYlGn(1 - t/max_time)
            ax2.scatter([x], [y], [z], c=[color], s=50, alpha=0.8)

        ax2.scatter([0], [0], [1], c='green', s=300, marker='o',
                   edgecolors='black', linewidth=2, label='t=0: |活⟩')
        ax2.scatter([0], [0], [-1], c='red', s=300, marker='o',
                   edgecolors='black', linewidth=2, label=f't={max_time}: 接近|死⟩')

        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('Bloch球：貓的量子態軌跡', fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)

        plt.tight_layout()
        plt.savefig('schrodinger_cat_evolution.png', dpi=300, bbox_inches='tight')
        plt.show()

    def run_experiments(self, t, n_trials=100):
        """運行多次實驗，統計結果"""
        print("\n" + "="*70)
        print(f"【薛丁格的貓實驗】時間 t = {t} 小時")
        print("="*70)

        prob_alive, prob_dead = self.cat_state(t)
        print(f"\n理論預測：")
        print(f"  P(貓活) = {prob_alive:.2%}")
        print(f"  P(貓死) = {prob_dead:.2%}")

        results = [self.measure(t) for _ in range(n_trials)]
        count_alive = results.count('alive')
        count_dead = results.count('dead')

        print(f"\n實驗結果（{n_trials}次測量）：")
        print(f"  觀察到貓活：{count_alive}次 ({count_alive/n_trials:.2%})")
        print(f"  觀察到貓死：{count_dead}次 ({count_dead/n_trials:.2%})")

        print(f"\n關鍵洞見：")
        print(f"  • 每次打開盒子之前，貓都處於疊加態")
        print(f"  • 打開盒子（測量）導致波函數坍縮")
        print(f"  • 不同次實驗給出不同結果，但統計上符合理論")
        print("="*70)

# 創建貓
cat = SchrodingerCat(half_life=1.0)

# 視覺化演化
cat.visualize_evolution(max_time=3.0)

# 運行實驗
cat.run_experiments(t=0.5, n_trials=100)
cat.run_experiments(t=1.0, n_trials=100)
cat.run_experiments(t=2.0, n_trials=100)

def dao_you_wu_animation():
    """
    「有無相生」的動態視覺化
    展示：有和無如何互相產生、互相依存
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    theta = np.linspace(0, 2*np.pi, 1000)
    n_frames = 60

    def update(frame):
        ax1.clear()
        ax2.clear()
        rotation = 2 * np.pi * frame / n_frames

        # 太極圖（旋轉）
        r_yin = 1 + 0.5 * np.sin(theta + rotation)
        r_yang = 1 - 0.5 * np.sin(theta + rotation)

        ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
                color='black', alpha=0.8, label='無')
        ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
                color='white', edgecolor='black', linewidth=2, label='有')

        # 魚眼
        eye_x_yang = 0.5 * np.cos(rotation)
        eye_y_yang = 0.5 * np.sin(rotation)
        eye_x_yin = -0.5 * np.cos(rotation)
        eye_y_yin = -0.5 * np.sin(rotation)

        ax1.add_patch(plt.Circle((eye_x_yang, eye_y_yang), 0.15,
                                color='white', ec='black', linewidth=1.5))
        ax1.add_patch(plt.Circle((eye_x_yin, eye_y_yin), 0.15,
                               color='black', ec='black', linewidth=1.5))
        ax1.add_patch(plt.Circle((0, 0), 1.5, fill=False,
                                 edgecolor='black', linewidth=3))

        ax1.set_xlim(-2, 2)
        ax1.set_ylim(-2, 2)
        ax1.set_aspect('equal')
        ax1.axis('off')
        ax1.set_title('太極圖：有無相生\n「有」中生「無」，「無」中生「有」',
                     fontsize=14, fontweight='bold')

        # === 右圖：量子疊加態（同步旋轉）===
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 30)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='gray')

        theta_q = np.pi/3
        phi_q = rotation
        x_state = np.sin(theta_q) * np.cos(phi_q)
        y_state = np.sin(theta_q) * np.sin(phi_q)
        z_state = np.cos(theta_q)

        ax2.quiver(0, 0, 0, x_state, y_state, z_state,
                  arrow_length_ratio=0.3, color='red', linewidth=3)
        ax2.scatter([0], [0], [1], c='blue', s=200, label='|0⟩ (有)')
        ax2.scatter([0], [0], [-1], c='green', s=200, label='|1⟩ (無)')
        ax2.plot([0, x_state], [0, y_state], [0, 0], 'r--', alpha=0.5, linewidth=1)

        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('量子疊加態：|ψ⟩ = α|有⟩ + β|無⟩\n隨時間演化',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1.5, 1.5])
        ax2.set_zlim([-1.5, 1.5])

    anim = FuncAnimation(fig, update, frames=n_frames,
                        interval=100, repeat=True)
    plt.tight_layout()
    plt.show()

    # 靜態版本（用於文章）
    fig_static, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    theta = np.linspace(0, 2*np.pi, 1000)
    r_yin = 1 + 0.5 * np.sin(theta)
    r_yang = 1 - 0.5 * np.sin(theta)

    ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta), color='black', alpha=0.8)
    ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
            color='white', edgecolor='black', linewidth=2)
    ax1.add_patch(plt.Circle((0, 0.5), 0.15, color='white', ec='black', lw=1.5))
    ax1.add_patch(plt.Circle((0, -0.5), 0.15, color='black', ec='black', lw=1.5))
    ax1.add_patch(plt.Circle((0, 0), 1.5, fill=False, ec='black', lw=3))

    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('老子：有無相生\n「無」中有「有」，「有」中有「無」',
                 fontsize=14, fontweight='bold')
    ax1.text(0, -2.5, '對立面不是矛盾，而是同一整體的兩個側面',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax2 = fig_static.add_subplot(122, projection='3d')
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax2.plot_surface(x, y, z, alpha=0.1, color='gray')

    states = [
        (0, 0, 1, 'blue', '|0⟩ (純有)'),
        (0, 0, -1, 'green', '|1⟩ (純無)'),
        (1, 0, 0, 'red', '(|0⟩+|1⟩)/√2'),
        (0, 1, 0, 'purple', '(|0⟩+i|1⟩)/√2'),
    ]

    for x, y, z, color, label in states:
        ax2.scatter([x], [y], [z], c=color, s=200, label=label)
        if x != 0 or y != 0 or z != 1:
            ax2.quiver(0, 0, 0, x, y, z, arrow_length_ratio=0.2,
                      color=color, alpha=0.5, linewidth=2)

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('量子力學：疊加態\n|ψ⟩ = α|有⟩ + β|無⟩',
                 fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('dao_you_wu_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【有無相生 vs 量子疊加】")
    print("="*70)
    print("\n老子《道德經》：")
    print("  「有無相生，難易相成。」")
    print("  → 有和無互相依存，不可分割")
    print("\n量子力學：")
    print("  |ψ⟩ = α|0⟩ + β|1⟩")
    print("  → |0⟩ 和 |1⟩ 同時存在於疊加態中")
    print("\n共同點：")
    print("  • 對立面不是二選一，而是同時共存")
    print("  • 整體大於部分之和")
    print("  • 分別是觀察/命名的產物，不是本質")
    print("="*70)

# 執行
dao_you_wu_animation()

def zhuangzi_butterfly_dream():
    """
    莊周夢蝶的量子力學詮釋
    展示：觀察者與被觀察物的糾纏
    """

    fig = plt.figure(figsize=(16, 10))

    # === 左上：疊加態機率柱狀圖 ===
    ax1 = fig.add_subplot(221)

    scenarios = {
        '夢前\n(疊加態)': [0.5, 0.5],
        '夢中\n(仍是疊加)': [0.5, 0.5],
        '醒後測量1\n(坍縮到莊周)': [1.0, 0.0],
        '醒後測量2\n(坍縮到蝴蝶)': [0.0, 1.0],
    }

    x = np.arange(len(scenarios))
    width = 0.35
    values_state1 = [v[0] for v in scenarios.values()]
    values_state2 = [v[1] for v in scenarios.values()]

    ax1.bar(x - width/2, values_state1, width, label='|莊周⟩', color='blue', alpha=0.7)
    ax1.bar(x + width/2, values_state2, width, label='|蝴蝶⟩', color='orange', alpha=0.7)

    ax1.set_ylabel('機率', fontsize=13)
    ax1.set_title('莊周夢蝶：量子疊加態詮釋', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios.keys(), fontsize=10)
    ax1.legend(fontsize=12)
    ax1.set_ylim(0, 1.2)
    ax1.grid(True, alpha=0.3, axis='y')

    ax1.text(1.5, 0.8, '關鍵：測量前，\n莊周和蝴蝶\n「同樣真實」！',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # === 左下：莊周的視角 ===
    ax2 = fig.add_subplot(223)
    ax2.text(0.5, 0.7, '如果莊周測量...', ha='center', fontsize=14,
            fontweight='bold', transform=ax2.transAxes)
    ax2.text(0.5, 0.5,
            '波函數坍縮：\n|ψ⟩ → |莊周⟩\n\n'
            '結論：\n「我是莊周，\n剛才夢見蝴蝶。」',
            ha='center', va='center', fontsize=12,
            transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.axis('off')

    # === 右下：蝴蝶的視角 ===
    ax3 = fig.add_subplot(224)
    ax3.text(0.5, 0.7, '如果蝴蝶測量...', ha='center', fontsize=14,
            fontweight='bold', transform=ax3.transAxes)
    ax3.text(0.5, 0.5,
            '波函數坍縮：\n|ψ⟩ → |蝴蝶⟩\n\n'
            '結論：\n「我是蝴蝶，\n剛才夢見莊周。」',
            ha='center', va='center', fontsize=12,
            transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax3.axis('off')

    # === 右上：3D量子態空間 ===
    ax4 = fig.add_subplot(222, projection='3d')

    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax4.plot_surface(x, y, z, alpha=0.1, color='gray')

    ax4.scatter([0], [0], [1], c='blue', s=300, label='|莊周⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([0], [0], [-1], c='orange', s=300, label='|蝴蝶⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([1], [0], [0], c='purple', s=300,
               label='疊加態\n(|莊周⟩+|蝴蝶⟩)/√2',
               edgecolors='black', linewidth=2)
    ax4.quiver(0, 0, 0, 1, 0, 0, arrow_length_ratio=0.3,
              color='purple', linewidth=3, alpha=0.7)

    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    ax4.set_title('量子態空間\n測量前：疊加態', fontsize=13, fontweight='bold')
    ax4.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('zhuangzi_butterfly_quantum.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 文字說明
    print("\n" + "="*70)
    print("【莊周夢蝶的量子詮釋】")
    print("="*70)
    print("\n經典問題（莊子）：")
    print("  「不知周之夢為蝴蝶與？蝴蝶之夢為周與？」")
    print("\n量子答案：")
    print("  測量前，系統處於疊加態：")
    print("    |ψ⟩ = (|莊周⟩ + |蝴蝶⟩) / √2")
    print("  沒有「絕對真實」的答案！")
    print("\n深層意義：")
    print("  • 沒有獨立於觀察者的「客觀實在」")
    print("  • 「真」和「假」是相對的，不是絕對的")
    print("  • 觀察者與被觀察物不可分離")
    print("="*70)

# 執行
zhuangzi_butterfly_dream()

def decoherence_simulation():
    """
    退相干模擬
    解釋：為什麼宏觀物體（如貓）不顯示量子疊加態
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    times = np.linspace(0, 10, 1000)

    # === (0,0) 微觀粒子：長相干時間 ===
    ax = axes[0, 0]
    tau_coherence_micro = 10.0
    coherence_micro = np.exp(-times / tau_coherence_micro)

    ax.plot(times, coherence_micro, 'b-', linewidth=3, label='相干性')
    ax.fill_between(times, 0, coherence_micro, alpha=0.3, color='blue')
    ax.axhline(0.5, color='red', linestyle='--', label='50%相干')
    ax.set_xlabel('時間（任意單位）', fontsize=12)
    ax.set_ylabel('相干性', fontsize=12)
    ax.set_title('微觀粒子（如電子）\n相干時間長 → 可以保持疊加態',
                fontsize=13, fontweight='bold', color='blue')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'相干時間 τ = {tau_coherence_micro}\n可觀察到量子效應',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === (0,1) 宏觀物體：極短相干時間 ===
    ax = axes[0, 1]
    tau_coherence_macro = 0.001
    coherence_macro = np.exp(-times / tau_coherence_macro)

    ax.plot(times, coherence_macro, 'r-', linewidth=3, label='相干性')
    ax.fill_between(times, 0, coherence_macro, alpha=0.3, color='red')
    ax.set_xlabel('時間（任意單位）', fontsize=12)
    ax.set_ylabel('相干性', fontsize=12)
    ax.set_title('宏觀物體（如貓）\n相干時間極短 → 瞬間坍縮',
                fontsize=13, fontweight='bold', color='red')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'相干時間 τ ≈ {tau_coherence_macro}\n幾乎瞬間退相干',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === (1,0) 環境粒子數 vs 退相干速率 ===
    ax = axes[1, 0]

    n_particles = np.logspace(0, 10, 100)
    decoherence_rate = n_particles / 1e9

    ax.loglog(n_particles, decoherence_rate, 'g-', linewidth=3)
    ax.fill_between(n_particles, 1e-10, decoherence_rate, alpha=0.3, color='green')

    ax.scatter([1], [1e-9], s=200, c='blue', label='單個原子', zorder=5)
    ax.scatter([1e6], [1e-3], s=200, c='purple', label='病毒', zorder=5)
    ax.scatter([1e18], [1e9], s=200, c='red', label='貓', zorder=5)

    ax.set_xlabel('環境粒子數（對數尺度）', fontsize=12)
    ax.set_ylabel('退相干速率（對數尺度）', fontsize=12)
    ax.set_title('退相干速率 ∝ 環境粒子數\n物體越大，退相干越快',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, which='both')

    # === (1,1) 疊加態保持時間 ===
    ax = axes[1, 1]

    objects = ['電子', '分子', '病毒', '灰塵', '細菌', '貓']
    coherence_times = [1e10, 1e5, 1e-3, 1e-10, 1e-15, 1e-40]
    colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red']

    y_pos = np.arange(len(objects))
    ax.barh(y_pos, np.log10(coherence_times), color=colors, alpha=0.7)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(objects, fontsize=12)
    ax.set_xlabel('相干時間（log₁₀秒）', fontsize=12)
    ax.set_title('不同尺度物體的相干時間\n為什麼我們看不到「既死又活」的貓？',
                fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')

    ax.text(-20, 5.5,
           f'貓的相干時間 ≈ 10⁻⁴⁰秒\n(比宇宙年齡短10⁵⁷倍！)\n→ 根本無法觀察到疊加態',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.text(8, 0.5,
           f'電子的相干時間 ≈ 10¹⁰秒\n(約300年)\n→ 容易觀察到量子效應',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('decoherence_explanation.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【退相干：薛丁格的貓為什麼不現實？】")
    print("="*70)
    print("\n問題：")
    print("  如果量子疊加是真的，為什麼我們從沒見過「既死又活」的貓？")
    print("\n答案：退相干（Decoherence）")
    print("  • 宏觀物體與環境有無數次相互作用")
    print("  • 每次相互作用都是一次「測量」")
    print("  • 疊加態極快地坍縮")
    print("\n數學：")
    print("  相干時間 τ ∝ 1 / (環境粒子數)")
    print("  電子：   τ ≈ 10¹⁰ 秒 (可觀察)")
    print("  病毒：   τ ≈ 10⁻³ 秒")
    print("  灰塵：   τ ≈ 10⁻¹⁰ 秒")
    print("  貓：     τ ≈ 10⁻⁴⁰ 秒 (根本無法觀察)")
    print("\n關鍵洞見：")
    print("  1. 量子疊加是真的")
    print("  2. 但宏觀物體退相干太快，我們看不到")
    print("  3. 不是「量子力學不適用於宏觀」")
    print("     而是「宏觀物體太難隔離」")
    print("\n老子的觀點：")
    print("  「道可道，非常道。」")
    print("  → 一旦觀察/命名，「道」就變成「非常道」")
    print("  → 退相干是自然界的「觀察」")
    print("="*70)

# 執行
decoherence_simulation()
