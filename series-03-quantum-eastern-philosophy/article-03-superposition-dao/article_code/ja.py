# Code & Cogito: 量子重ね合わせ vs 老荘の「道」——存在と非存在のあいだで
# Article: https://code-cogito.com/ja/quantum-superposition-taoism-dao-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

# | P(合計) = P(可能性1) + P(可能性2)

# | P(合計) = |α₁ + α₂|²

# | P(合計) = |α₁|² + |α₂|² + 2Re(α₁*α₂*)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure Japanese fonts
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class SchrodingerCat:
    """
    Full simulation of Schrodinger's cat.
    Includes: atom state, cat state, time evolution, measurement.
    """

    def __init__(self, half_life=1.0):
        self.half_life = half_life
        self.lambda_decay = np.log(2) / half_life  # Decay constant

    def atom_state(self, t):
        """Quantum state of atom at time t: |psi> = alpha|undecayed> + beta|decayed>"""
        alpha = np.sqrt(np.exp(-self.lambda_decay * t))
        beta = np.sqrt(1 - np.exp(-self.lambda_decay * t))
        return alpha, beta

    def cat_state(self, t):
        """Cat state evolving with time: |cat> = alpha|alive> + beta|dead>"""
        alpha, beta = self.atom_state(t)
        prob_alive = np.abs(alpha)**2
        prob_dead = np.abs(beta)**2
        return prob_alive, prob_dead

    def measure(self, t):
        """Open the box and measure the cat's state — wave function collapse"""
        prob_alive, prob_dead = self.cat_state(t)
        outcome = np.random.choice(['alive', 'dead'],
                                  p=[prob_alive, prob_dead])
        return outcome

    def visualize_evolution(self, max_time=3.0):
        """Visualize the time evolution of the cat's quantum state"""
        times = np.linspace(0, max_time, 100)
        probs_alive = []
        probs_dead = []

        for t in times:
            p_alive, p_dead = self.cat_state(t)
            probs_alive.append(p_alive)
            probs_dead.append(p_dead)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # === Upper panel: probability evolution ===
        ax1.fill_between(times, 0, probs_alive, alpha=0.6, color='green', label='P(猫が生存)')
        ax1.fill_between(times, 0, probs_dead, alpha=0.6, color='red', label='P(猫が死亡)')
        ax1.plot(times, probs_alive, 'g-', linewidth=2)
        ax1.plot(times, probs_dead, 'r-', linewidth=2)

        ax1.set_xlabel('時間（時間）', fontsize=13)
        ax1.set_ylabel('確率', fontsize=13)
        ax1.set_title('シュレーディンガーの猫：重ね合わせ状態の時間発展\n（箱を開ける前）',
                     fontsize=15, fontweight='bold')
        ax1.legend(fontsize=12, loc='center right')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.1)

        # Mark the half-life
        ax1.axvline(self.half_life, color='black', linestyle='--', linewidth=2,
                   label=f'半減期 = {self.half_life}時間')
        ax1.text(self.half_life + 0.1, 0.9,
                f'半減期\nこの時点でP(生)=P(死)=50%',
                fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

        ax1.text(max_time * 0.5, 0.3,
                '重要：「猫は死か生のどちらか」ではない！\n'
                '「猫は同時に死んでもいて生きてもいる」！\n'
                '量子状態 |猫⟩ = α|生⟩ + β|死⟩',
                fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # === Lower panel: Bloch sphere representation ===
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
                   edgecolors='black', linewidth=2, label='t=0: |生⟩')
        ax2.scatter([0], [0], [-1], c='red', s=300, marker='o',
                   edgecolors='black', linewidth=2, label=f't={max_time}: |死⟩に接近')

        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('ブロッホ球：猫の量子状態の軌跡', fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)

        plt.tight_layout()
        plt.savefig('schrodinger_cat_evolution.png', dpi=300, bbox_inches='tight')
        plt.show()

    def run_experiments(self, t, n_trials=100):
        """Run multiple experiments and collect statistics"""
        print("\n" + "="*70)
        print(f"【シュレーディンガーの猫実験】時刻 t = {t} 時間")
        print("="*70)

        prob_alive, prob_dead = self.cat_state(t)
        print(f"\n理論予測：")
        print(f"  P(猫が生存) = {prob_alive:.2%}")
        print(f"  P(猫が死亡) = {prob_dead:.2%}")

        results = [self.measure(t) for _ in range(n_trials)]
        count_alive = results.count('alive')
        count_dead = results.count('dead')

        print(f"\n実験結果（{n_trials}回の観測）：")
        print(f"  猫が生存と観測：{count_alive}回 ({count_alive/n_trials:.2%})")
        print(f"  猫が死亡と観測：{count_dead}回 ({count_dead/n_trials:.2%})")

        print(f"\n重要な洞察：")
        print(f"  ・箱を開ける前、猫は毎回重ね合わせ状態にある")
        print(f"  ・箱を開ける（観測する）ことで波動関数が収縮する")
        print(f"  ・各実験で異なる結果が出るが、統計的には理論に一致する")
        print("="*70)

# Create a cat
cat = SchrodingerCat(half_life=1.0)

# Visualize evolution
cat.visualize_evolution(max_time=3.0)

# Run experiments
cat.run_experiments(t=0.5, n_trials=100)
cat.run_experiments(t=1.0, n_trials=100)
cat.run_experiments(t=2.0, n_trials=100)

def dao_you_wu_animation():
    """
    Visualization of 'You-Wu Xiang Sheng' (Being and Non-being mutually arise).
    Demonstrates how existence and non-existence generate each other.
    """

    fig = plt.figure(figsize=(16, 7)); ax1 = fig.add_subplot(121); ax2 = fig.add_subplot(122, projection='3d')
    theta = np.linspace(0, 2*np.pi, 1000)
    n_frames = 60

    def update(frame):
        ax1.clear()
        ax2.clear()
        rotation = 2 * np.pi * frame / n_frames

        # Taijitu (rotating)
        r_yin = 1 + 0.5 * np.sin(theta + rotation)
        r_yang = 1 - 0.5 * np.sin(theta + rotation)

        ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
                color='black', alpha=0.8, label='無')
        ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
                color='white', edgecolor='black', linewidth=2, label='有')

        # Fish eyes
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
        ax1.set_title('太極図：有無相生\n「有」の中に「無」が生じ、「無」の中に「有」が生じる',
                     fontsize=14, fontweight='bold')

        # === Right panel: quantum superposition (synchronized rotation) ===
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
        ax2.set_title('量子重ね合わせ：|ψ⟩ = α|有⟩ + β|無⟩\n時間発展',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1.5, 1.5])
        ax2.set_zlim([-1.5, 1.5])

    anim = FuncAnimation(fig, update, frames=n_frames,
                        interval=100, repeat=True)
    plt.tight_layout()
    plt.show()

    # Static version (for article)
    fig_static = plt.figure(figsize=(16, 7)); ax1 = fig_static.add_subplot(121); ax2 = fig_static.add_subplot(122, projection='3d')

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
    ax1.set_title('老子：有無相生\n「無」の中に「有」あり、「有」の中に「無」あり',
                 fontsize=14, fontweight='bold')
    ax1.text(0, -2.5, '対立するものは矛盾ではなく、同一の全体の二つの側面である',
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
        (0, 0, 1, 'blue', '|0⟩ (純粋な有)'),
        (0, 0, -1, 'green', '|1⟩ (純粋な無)'),
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
    ax2.set_title('量子力学：重ね合わせ状態\n|ψ⟩ = α|有⟩ + β|無⟩',
                 fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('dao_you_wu_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【有無相生 vs 量子重ね合わせ】")
    print("="*70)
    print("\n老子『道徳経』：")
    print("  「有無相生、難易相成。」")
    print("  → 有と無は互いに依存し、分割できない")
    print("\n量子力学：")
    print("  |ψ⟩ = α|0⟩ + β|1⟩")
    print("  → |0⟩ と |1⟩ は重ね合わせ状態の中に同時に存在する")
    print("\n共通点：")
    print("  ・対立するものは二者択一ではなく、同時に共存する")
    print("  ・全体は部分の総和を超える")
    print("  ・分別は観察/名づけの産物であり、本質ではない")
    print("="*70)

# Execute
dao_you_wu_animation()

def zhuangzi_butterfly_dream():
    """
    Quantum mechanical interpretation of Zhuangzi's butterfly dream.
    Demonstrates: entanglement between observer and observed.
    """

    fig = plt.figure(figsize=(16, 10))

    # === Upper left: superposition probability bar chart ===
    ax1 = fig.add_subplot(221)

    scenarios = {
        '夢の前\n(重ね合わせ)': [0.5, 0.5],
        '夢の中\n(依然重ね合わせ)': [0.5, 0.5],
        '覚醒後の観測1\n(荘周に収縮)': [1.0, 0.0],
        '覚醒後の観測2\n(蝶に収縮)': [0.0, 1.0],
    }

    x = np.arange(len(scenarios))
    width = 0.35
    values_state1 = [v[0] for v in scenarios.values()]
    values_state2 = [v[1] for v in scenarios.values()]

    ax1.bar(x - width/2, values_state1, width, label='|荘周⟩', color='blue', alpha=0.7)
    ax1.bar(x + width/2, values_state2, width, label='|蝶⟩', color='orange', alpha=0.7)

    ax1.set_ylabel('確率', fontsize=13)
    ax1.set_title('荘周の胡蝶の夢：量子重ね合わせ解釈', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios.keys(), fontsize=10)
    ax1.legend(fontsize=12)
    ax1.set_ylim(0, 1.2)
    ax1.grid(True, alpha=0.3, axis='y')

    ax1.text(1.5, 0.8, '要点：観測前は\n荘周と蝶の両方が\n「等しく実在」！',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # === Lower left: Zhuangzi's perspective ===
    ax2 = fig.add_subplot(223)
    ax2.text(0.5, 0.7, '荘周が観測した場合...', ha='center', fontsize=14,
            fontweight='bold', transform=ax2.transAxes)
    ax2.text(0.5, 0.5,
            '波動関数の収縮：\n|ψ⟩ → |荘周⟩\n\n'
            '結論：\n「私は荘周だ。\nさっき蝶の夢を見た。」',
            ha='center', va='center', fontsize=12,
            transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.axis('off')

    # === Lower right: butterfly's perspective ===
    ax3 = fig.add_subplot(224)
    ax3.text(0.5, 0.7, '蝶が観測した場合...', ha='center', fontsize=14,
            fontweight='bold', transform=ax3.transAxes)
    ax3.text(0.5, 0.5,
            '波動関数の収縮：\n|ψ⟩ → |蝶⟩\n\n'
            '結論：\n「私は蝶だ。\nさっき荘周の夢を見た。」',
            ha='center', va='center', fontsize=12,
            transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax3.axis('off')

    # === Upper right: 3D quantum state space ===
    ax4 = fig.add_subplot(222, projection='3d')

    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax4.plot_surface(x, y, z, alpha=0.1, color='gray')

    ax4.scatter([0], [0], [1], c='blue', s=300, label='|荘周⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([0], [0], [-1], c='orange', s=300, label='|蝶⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([1], [0], [0], c='purple', s=300,
               label='重ね合わせ\n(|荘周⟩+|蝶⟩)/√2',
               edgecolors='black', linewidth=2)
    ax4.quiver(0, 0, 0, 1, 0, 0, arrow_length_ratio=0.3,
              color='purple', linewidth=3, alpha=0.7)

    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    ax4.set_title('量子状態空間\n観測前：重ね合わせ状態', fontsize=13, fontweight='bold')
    ax4.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('zhuangzi_butterfly_quantum.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Text explanation
    print("\n" + "="*70)
    print("【荘周の胡蝶の夢——量子力学的解釈】")
    print("="*70)
    print("\n古典的な問い（荘子）：")
    print("  「周の夢に胡蝶と為れるか、胡蝶の夢に周と為れるかを知らず。」")
    print("\n量子力学的な答え：")
    print("  観測前、系は重ね合わせ状態にある：")
    print("    |ψ⟩ = (|荘周⟩ + |蝶⟩) / √2")
    print("  「絶対的に真実な」答えは存在しない！")
    print("\n深層的意味：")
    print("  ・観測者から独立した「客観的実在」は存在しない")
    print("  ・「真」と「偽」は絶対的ではなく、相対的である")
    print("  ・観測者と被観測対象は分離不可能である")
    print("="*70)

# Execute
zhuangzi_butterfly_dream()

def decoherence_simulation():
    """
    Decoherence simulation.
    Explains why macroscopic objects (like cats) do not exhibit quantum superposition.
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    times = np.linspace(0, 10, 1000)

    # === (0,0) Microscopic particle: long coherence time ===
    ax = axes[0, 0]
    tau_coherence_micro = 10.0
    coherence_micro = np.exp(-times / tau_coherence_micro)

    ax.plot(times, coherence_micro, 'b-', linewidth=3, label='コヒーレンス')
    ax.fill_between(times, 0, coherence_micro, alpha=0.3, color='blue')
    ax.axhline(0.5, color='red', linestyle='--', label='50%コヒーレンス')
    ax.set_xlabel('時間（任意単位）', fontsize=12)
    ax.set_ylabel('コヒーレンス', fontsize=12)
    ax.set_title('ミクロ粒子（例：電子）\nコヒーレンス時間が長い → 重ね合わせ維持可能',
                fontsize=13, fontweight='bold', color='blue')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'コヒーレンス時間 τ = {tau_coherence_micro}\n量子効果を観測可能',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === (0,1) Macroscopic object: extremely short coherence time ===
    ax = axes[0, 1]
    tau_coherence_macro = 0.001
    coherence_macro = np.exp(-times / tau_coherence_macro)

    ax.plot(times, coherence_macro, 'r-', linewidth=3, label='コヒーレンス')
    ax.fill_between(times, 0, coherence_macro, alpha=0.3, color='red')
    ax.set_xlabel('時間（任意単位）', fontsize=12)
    ax.set_ylabel('コヒーレンス', fontsize=12)
    ax.set_title('マクロ物体（例：猫）\nコヒーレンス時間が極短 → 瞬時に収縮',
                fontsize=13, fontweight='bold', color='red')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'コヒーレンス時間 τ ≈ {tau_coherence_macro}\nほぼ瞬時にデコヒーレンス',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === (1,0) Number of environmental particles vs decoherence rate ===
    ax = axes[1, 0]

    n_particles = np.logspace(0, 10, 100)
    decoherence_rate = n_particles / 1e9

    ax.loglog(n_particles, decoherence_rate, 'g-', linewidth=3)
    ax.fill_between(n_particles, 1e-10, decoherence_rate, alpha=0.3, color='green')

    ax.scatter([1], [1e-9], s=200, c='blue', label='単一原子', zorder=5)
    ax.scatter([1e6], [1e-3], s=200, c='purple', label='ウイルス', zorder=5)
    ax.scatter([1e18], [1e9], s=200, c='red', label='猫', zorder=5)

    ax.set_xlabel('環境粒子数（対数スケール）', fontsize=12)
    ax.set_ylabel('デコヒーレンス速度（対数スケール）', fontsize=12)
    ax.set_title('デコヒーレンス速度 ∝ 環境粒子数\n物体が大きいほどデコヒーレンスが速い',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, which='both')

    # === (1,1) Superposition maintenance time ===
    ax = axes[1, 1]

    objects = ['電子', '分子', 'ウイルス', '塵', '細菌', '猫']
    coherence_times = [1e10, 1e5, 1e-3, 1e-10, 1e-15, 1e-40]
    colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red']

    y_pos = np.arange(len(objects))
    ax.barh(y_pos, np.log10(coherence_times), color=colors, alpha=0.7)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(objects, fontsize=12)
    ax.set_xlabel('コヒーレンス時間（log₁₀秒）', fontsize=12)
    ax.set_title('異なるスケールの物体のコヒーレンス時間\nなぜ「死んでもいて生きてもいる猫」を見られないのか？',
                fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')

    ax.text(-20, 5.5,
           f'猫のコヒーレンス時間 ≈ 10⁻⁴⁰秒\n(宇宙の年齢より10⁵⁷倍短い！)\n→ 重ね合わせの観測は不可能',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.text(8, 0.5,
           f'電子のコヒーレンス時間 ≈ 10¹⁰秒\n(約300年)\n→ 量子効果の観測が容易',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('decoherence_explanation.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【デコヒーレンス：シュレーディンガーの猫はなぜ現実的でないのか？】")
    print("="*70)
    print("\n問い：")
    print("  量子重ね合わせが真実なら、なぜ「死んでもいて生きてもいる猫」を見たことがないのか？")
    print("\n答え：デコヒーレンス（量子干渉性の喪失）")
    print("  ・マクロ物体は環境と無数の相互作用を持つ")
    print("  ・各相互作用が一回の「観測」に相当する")
    print("  ・重ね合わせ状態は極めて速く収縮する")
    print("\n数学：")
    print("  コヒーレンス時間 τ ∝ 1 / (環境粒子数)")
    print("  電子：   τ ≈ 10¹⁰ 秒 (観測可能)")
    print("  ウイルス：τ ≈ 10⁻³ 秒")
    print("  塵：     τ ≈ 10⁻¹⁰ 秒")
    print("  猫：     τ ≈ 10⁻⁴⁰ 秒 (観測不可能)")
    print("\n重要な洞察：")
    print("  1. 量子重ね合わせは真実である")
    print("  2. しかしマクロ物体のデコヒーレンスが速すぎて観測できない")
    print("  3. 「量子力学がマクロに適用されない」のではなく")
    print("     「マクロ物体を環境から隔離するのが困難すぎる」のだ")
    print("\n老子の視点：")
    print("  「道可道、非常道。」")
    print("  → 観察・名づけをした瞬間、「道」は「常の道に非ず」となる")
    print("  → デコヒーレンスは自然界による「観察」である")
    print("="*70)

# Execute
decoherence_simulation()
