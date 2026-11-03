# Code & Cogito: 量子もつれ vs 華厳宗「因陀羅網」——宇宙は分かちがたき一つの全体
# Article: https://code-cogito.com/ja/quantum-entanglement-indras-net-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class EPRExperiment:
    """
    EPR experiment simulation
    Demonstrates: non-local correlations in quantum entanglement
    """

    def __init__(self):
        self.n_trials = 1000

    def create_entangled_pair(self):
        """
        Create entangled state: |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2
        Returns: phase
        """
        # Random phase (but always anti-correlated upon measurement)
        phase = np.random.uniform(0, 2*np.pi)
        return phase

    def measure_spin(self, phase, angle):
        """
        Measure spin
        angle: measurement angle (radians)
        Returns: +1 (up) or -1 (down)
        """
        # Quantum mechanical prediction: probability = cos²(θ/2)
        prob_up = np.cos((angle - phase) / 2)**2

        if np.random.random() < prob_up:
            return +1  # up
        else:
            return -1  # down

    def run_epr_experiment(self, angle_A, angle_B):
        """
        Run EPR experiment
        angle_A: Alice's measurement angle
        angle_B: Bob's measurement angle
        Returns: (results_A list, results_B list, correlation function)
        """
        results_A = []
        results_B = []

        for _ in range(self.n_trials):
            # Aliceの結果：もつれ状態の周辺確率は角度によらず常に50/50
            result_A = +1 if np.random.random() < 0.5 else -1

            # Bobの結果：独立に測定するのではなく、単態の同時確率でAliceと相関させる
            prob_diff = np.cos((angle_A - angle_B) / 2)**2
            result_B = -result_A if np.random.random() < prob_diff else result_A

            results_A.append(result_A)
            results_B.append(result_B)

        # Compute correlation function E(a,b) = ⟨A·B⟩
        correlation = np.mean(np.array(results_A) * np.array(results_B))

        return results_A, results_B, correlation

    def visualize_correlations(self):
        """
        Visualize correlation function at different angles
        """
        angles = np.linspace(0, np.pi, 50)
        correlations_quantum = []
        correlations_classical = []

        for angle in angles:
            _, _, corr_q = self.run_epr_experiment(0, angle)
            correlations_quantum.append(corr_q)

            # Classical prediction (local hidden variables)
            corr_c = -1 + 2*angle/np.pi
            correlations_classical.append(corr_c)

        # Quantum mechanical theoretical prediction
        correlations_theory = -np.cos(angles)

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(angles * 180/np.pi, correlations_theory, 'b-',
               linewidth=3, label='量子力学理論予測', alpha=0.7)
        ax.scatter(angles * 180/np.pi, correlations_quantum,
                  c='red', s=50, label=f'実験結果（{self.n_trials}回）',
                  alpha=0.6, zorder=5)
        ax.plot(angles * 180/np.pi, correlations_classical, 'g--',
               linewidth=2, label='古典予測（局所実在論）', alpha=0.7)

        ax.set_xlabel('Bobの測定角度（度）', fontsize=13)
        ax.set_ylabel('相関関数 E(0°, θ)', fontsize=13)
        ax.set_title('EPR実験：量子相関 vs 古典予測\nAliceは0°に固定',
                    fontsize=15, fontweight='bold')
        ax.legend(fontsize=12, loc='upper right')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='black', linewidth=0.5)

        # Annotate key angles
        key_angles = [0, 45, 90, 135, 180]
        for angle in key_angles:
            angle_rad = angle * np.pi / 180
            corr_theory = -np.cos(angle_rad)
            ax.axvline(angle, color='gray', linestyle=':', alpha=0.5)
            ax.text(angle, corr_theory - 0.15, f'{angle}°\n{corr_theory:.2f}',
                   ha='center', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        plt.tight_layout()
        plt.savefig('epr_correlations.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【EPR実験結果】")
        print("="*70)
        print(f"\n実験回数：{self.n_trials}")
        print("\n主な発見：")
        print("  ・量子相関：E(θ) = -cos(θ)")
        print("  ・古典予測：E(θ) = 線形関数")
        print("  ・実験は量子予測に一致し、古典予測には一致しない")
        print("\n意義：")
        print("  ・もつれは実在する")
        print("  ・隠れた変数は存在しない")
        print("  ・アインシュタインは間違っていた")
        print("="*70)

    def demonstrate_nonlocality(self):
        """
        Demonstrate non-locality
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Three scenarios
        scenarios = [
            (0, 0, 'AliceとBob\n同方向を測定'),
            (0, np.pi/4, 'Alice 0°\nBob 45°'),
            (0, np.pi/2, 'Alice 0°\nBob 90°'),
        ]

        for idx, (angle_A, angle_B, title) in enumerate(scenarios):
            ax = axes[idx]

            results_A, results_B, correlation = self.run_epr_experiment(angle_A, angle_B)

            # Plot result distribution
            n_up_up = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == 1)
            n_up_down = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == -1)
            n_down_up = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == 1)
            n_down_down = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == -1)

            categories = ['↑↑', '↑↓', '↓↑', '↓↓']
            counts = [n_up_up, n_up_down, n_down_up, n_down_down]
            colors = ['green', 'blue', 'orange', 'red']

            bars = ax.bar(categories, counts, color=colors, alpha=0.7, edgecolor='black', linewidth=2)

            ax.set_ylabel('観測回数', fontsize=12)
            ax.set_title(f'{title}\n相関 E = {correlation:.3f}',
                        fontsize=13, fontweight='bold')
            ax.set_ylim(0, self.n_trials * 0.8)
            ax.grid(True, alpha=0.3, axis='y')

            # Annotate counts
            for bar, count in zip(bars, counts):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                       f'{count}\n({count/self.n_trials*100:.1f}%)',
                       ha='center', va='bottom', fontsize=10)

        fig.text(0.5, 0.02,
                '核心的洞察：どれほど離れていても、測定結果は常に相関する！\n'
                'これは事前の取り決めではなく、真の「遠隔相関」である',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig('epr_nonlocality.png', dpi=300, bbox_inches='tight')
        plt.show()

# Execute
experiment = EPRExperiment()
experiment.visualize_correlations()
experiment.demonstrate_nonlocality()

class BellInequality:
    """
    Bell inequality (CHSH form) verification
    """

    def __init__(self):
        self.n_trials = 10000

    def quantum_correlation(self, angle_A, angle_B):
        """
        Quantum mechanical prediction of correlation function
        E(a, b) = -cos(a - b)
        """
        return -np.cos(angle_A - angle_B)

    def local_realism_correlation(self, angle_A, angle_B, hidden_var):
        """
        Local realism (hidden variable) prediction
        hidden_var: λ ∈ [0, 2π]
        """
        result_A = +1 if np.cos(angle_A - hidden_var) > 0 else -1
        result_B = +1 if np.cos(angle_B - hidden_var + np.pi) > 0 else -1
        return result_A * result_B

    def compute_chsh_quantum(self):
        """
        Compute CHSH value for quantum mechanics
        S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
        """
        # Optimal angle selection
        a = 0
        a_prime = np.pi / 2
        b = np.pi / 4
        b_prime = 3 * np.pi / 4

        E_ab = self.quantum_correlation(a, b)
        E_ab_prime = self.quantum_correlation(a, b_prime)
        E_a_prime_b = self.quantum_correlation(a_prime, b)
        E_a_prime_b_prime = self.quantum_correlation(a_prime, b_prime)

        S_quantum = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime

        return S_quantum, (E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime)

    def compute_chsh_local(self):
        """
        Compute CHSH value for local realism
        Average over all possible λ values
        """
        a = 0
        a_prime = np.pi / 2
        b = np.pi / 4
        b_prime = 3 * np.pi / 4

        lambdas = np.linspace(0, 2*np.pi, self.n_trials)

        E_ab_list = []
        E_ab_prime_list = []
        E_a_prime_b_list = []
        E_a_prime_b_prime_list = []

        for lam in lambdas:
            E_ab_list.append(self.local_realism_correlation(a, b, lam))
            E_ab_prime_list.append(self.local_realism_correlation(a, b_prime, lam))
            E_a_prime_b_list.append(self.local_realism_correlation(a_prime, b, lam))
            E_a_prime_b_prime_list.append(self.local_realism_correlation(a_prime, b_prime, lam))

        E_ab = np.mean(E_ab_list)
        E_ab_prime = np.mean(E_ab_prime_list)
        E_a_prime_b = np.mean(E_a_prime_b_list)
        E_a_prime_b_prime = np.mean(E_a_prime_b_prime_list)

        S_local = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime

        return S_local, (E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime)

    def visualize_bell_test(self):
        """
        Visualize Bell inequality test
        """
        S_quantum, E_quantum = self.compute_chsh_quantum()
        S_local, E_local = self.compute_chsh_local()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # === Left: CHSH value comparison ===
        categories = ['量子力学', '局所実在論', 'ベル限界']
        values = [S_quantum, S_local, 2.0]
        colors = ['red', 'blue', 'green']

        bars = ax1.bar(categories, np.abs(values), color=colors, alpha=0.7,
                      edgecolor='black', linewidth=2)

        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{val:.3f}',
                    ha='center', va='bottom', fontsize=14, fontweight='bold')

        ax1.axhline(2.0, color='green', linestyle='--', linewidth=3,
                   label='ベル限界 |S| ≤ 2')
        ax1.axhline(2*np.sqrt(2), color='red', linestyle=':', linewidth=2,
                   label=f'量子限界 |S| = 2√2 ≈ {2*np.sqrt(2):.3f}')

        ax1.set_ylabel('|S| 値', fontsize=13)
        ax1.set_title('CHSH不等式テスト\n量子力学 vs 局所実在論',
                     fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.set_ylim(0, 3)

        if abs(S_quantum) > 2:
            verdict = '破れた！量子力学の勝利'
            verdict_color = 'red'
        else:
            verdict = '破れていない'
            verdict_color = 'green'

        ax1.text(0.5, 2.5, f'判定：{verdict}',
                ha='center', fontsize=13, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=verdict_color, alpha=0.5))

        # === Right: Four correlation functions ===
        labels = ['E(a,b)', 'E(a,b\')', 'E(a\',b)', 'E(a\',b\')']
        x_pos = np.arange(len(labels))

        quantum_vals = E_quantum
        local_vals = E_local

        width = 0.35
        bars1 = ax2.bar(x_pos - width/2, quantum_vals, width,
                       label='量子力学', color='red', alpha=0.7,
                       edgecolor='black', linewidth=1.5)
        bars2 = ax2.bar(x_pos + width/2, local_vals, width,
                       label='局所実在論', color='blue', alpha=0.7,
                       edgecolor='black', linewidth=1.5)

        ax2.set_ylabel('相関関数 E', fontsize=13)
        ax2.set_title('4つの測定配置の相関関数', fontsize=14, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(labels, fontsize=11)
        ax2.legend(fontsize=11)
        ax2.axhline(0, color='black', linewidth=0.5)
        ax2.grid(True, alpha=0.3, axis='y')

        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + 0.03 if height > 0 else height - 0.08,
                        f'{height:.2f}',
                        ha='center', va='bottom' if height > 0 else 'top', fontsize=9)

        plt.tight_layout()
        plt.savefig('bell_inequality_test.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【ベルの不等式テスト結果】")
        print("="*70)
        print(f"\nCHSH不等式：|S| ≤ 2 （局所実在論が成り立つ場合）")
        print(f"\n量子力学の予測：")
        print(f"  S = {S_quantum:.4f}")
        print(f"  |S| = {abs(S_quantum):.4f} > 2  → 不等式を破る")
        print(f"\n局所実在論（隠れた変数）：")
        print(f"  S = {S_local:.4f}")
        print(f"  |S| = {abs(S_local):.4f} ≤ 2  → 不等式を満たす")
        print(f"\n実験結果（1982-2022）：")
        print(f"  ・アスペ（1982）：S = 2.697 ± 0.015（実測値）")
        print(f"  ・ツァイリンガー（1998）：S ≈ 2.73 ± 0.02")
        print(f"  ・潘建偉（2017）：S ≈ 2.37 ± 0.09（1200km）")
        print(f"\n結論：")
        print(f"  → 量子力学は正しい")
        print(f"  × 局所実在論（隠れた変数理論）は誤り")
        print(f"  × アインシュタインの希望は崩壊した")
        print("="*70)

# Execute
bell_test = BellInequality()
bell_test.visualize_bell_test()

import networkx as nx
from itertools import combinations

def indras_net_3d():
    """
    3D visualization of Indra's Net
    Demonstrates: infinite mutual reflection
    """

    fig = plt.figure(figsize=(18, 12))

    # === Upper left: Grid Indra's Net ===
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')

    # Create 3D grid
    n = 4
    nodes = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

    # Plot nodes
    xs, ys, zs = zip(*nodes)
    ax1.scatter(xs, ys, zs, c='gold', s=200, edgecolors='black',
               linewidth=2, alpha=0.8)

    # Plot connections (only adjacent nodes)
    for node1, node2 in combinations(nodes, 2):
        distance = sum((a-b)**2 for a, b in zip(node1, node2))
        if distance == 1:  # Adjacent only
            ax1.plot([node1[0], node2[0]],
                    [node1[1], node2[1]],
                    [node1[2], node2[2]],
                    'gray', alpha=0.3, linewidth=1)

    # Highlight one node
    highlight = (1, 1, 1)
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    # Highlight neighbors
    neighbors = [(i, j, k) for i, j, k in nodes
                if sum((a-b)**2 for a, b in zip((i,j,k), highlight)) == 1]
    if neighbors:
        nx_list, ny_list, nz_list = zip(*neighbors)
        ax1.scatter(nx_list, ny_list, nz_list,
                   c='orange', s=300, edgecolors='red', linewidth=2, alpha=0.8)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('因陀羅網（3Dグリッド）\n各珠が隣接珠と結ばれる',
                 fontsize=13, fontweight='bold')

    # === Upper right: Fully connected Indra's Net ===
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')

    n_nodes = 8
    np.random.seed(42)
    positions = np.random.randn(n_nodes, 3) * 2

    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            ax2.plot([positions[i, 0], positions[j, 0]],
                    [positions[i, 1], positions[j, 1]],
                    [positions[i, 2], positions[j, 2]],
                    'b-', alpha=0.1, linewidth=0.5)

    ax2.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='cyan', s=300, edgecolors='black', linewidth=2, alpha=0.8)

    highlight_idx = 0
    ax2.scatter([positions[highlight_idx, 0]],
               [positions[highlight_idx, 1]],
               [positions[highlight_idx, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    for j in range(1, n_nodes):
        ax2.plot([positions[highlight_idx, 0], positions[j, 0]],
                [positions[highlight_idx, 1], positions[j, 1]],
                [positions[highlight_idx, 2], positions[j, 2]],
                'r-', alpha=0.5, linewidth=2)

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('因陀羅網（全結合）\n一珠を変えれば全網が動く',
                 fontsize=13, fontweight='bold')

    # === Lower left: Quantum entanglement network ===
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')

    n_particles = 10
    np.random.seed(43)
    particle_pos = np.random.randn(n_particles, 3) * 2

    for i in range(n_particles):
        for j in range(i+1, n_particles):
            strength = np.random.random()
            ax3.plot([particle_pos[i, 0], particle_pos[j, 0]],
                    [particle_pos[i, 1], particle_pos[j, 1]],
                    [particle_pos[i, 2], particle_pos[j, 2]],
                    'g-', alpha=strength*0.3, linewidth=1)

    ax3.scatter(particle_pos[:, 0], particle_pos[:, 1], particle_pos[:, 2],
               c='lightgreen', s=300, edgecolors='darkgreen',
               linewidth=2, alpha=0.8)

    highlight_idx = 3
    ax3.scatter([particle_pos[highlight_idx, 0]],
               [particle_pos[highlight_idx, 1]],
               [particle_pos[highlight_idx, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('量子もつれネットワーク\n一粒子の測定が全体に影響',
                 fontsize=13, fontweight='bold')

    # === Lower right: Correspondence panel ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    【因陀羅網 vs 量子もつれ】

    華厳宗『華厳経』（7世紀）：

    「帝釈天の宮に宝網あり、
     網上の珠珠互いに映現し、
     一珠に一切珠の影を含み、
     重々無尽にして不思議なり。」

    ━━━━━━━━━━━━━━━━━━━━━━━━

    量子力学（20世紀）：

    もつれ状態 |ψ⟩ は分解不能
    粒子Aと粒子Bは非局所的に相関
    Aを測定 → 瞬時にBに影響
    全体 > 部分の総和

    ━━━━━━━━━━━━━━━━━━━━━━━━

    共通の洞察：

    宇宙は分かちがたき一つの全体
    部分は全体から離れて存在しえない
    局所を変える = 全体を変える
    「分離」は幻想

    華厳宗：一即一切、一切即一
    量子力学：もつれ即全体、分離不可
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('indras_net_3d_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【因陀羅網：1300年以上前の量子的洞察】")
    print("="*70)
    print("\n法蔵が則天武后に見せた鏡室（7世紀）：")
    print("  ・仏像を囲む十面の鏡")
    print("  ・一本の松明で照明")
    print("  ・無数の映像、重々映現")
    print("  → 一即一切の直観的デモンストレーション")
    print("\n華厳宗の十玄門（第四門）：")
    print("  「因陀羅網境界門」")
    print("  → 一切法は珠網の如く、互いに映現する")
    print("\n現代の量子もつれ：")
    print("  ・EPR状態：|ψ⟩ = (|↑↓⟩ - |↓↑⟩)/√2")
    print("  ・Aを測定 → 瞬時にBが確定")
    print("  ・分離不可能な全体")
    print("\n2022年ノーベル物理学賞：")
    print("  Aspect、Clauser、Zeilingerに授与")
    print("  表彰理由：量子もつれの実在性の証明")
    print("="*70)

# Execute
indras_net_3d()

def nonlocal_correlation_demo():
    """
    Non-local correlation interactive demonstration
    Let users 'experience' action at a distance
    """

    fig = plt.figure(figsize=(16, 10))

    # Simulation parameters
    n_measurements = 50
    distance_light_years = [0.001, 0.1, 1, 10, 100, 1000]

    # === Upper plot: Distance does not affect correlation strength ===
    ax1 = fig.add_subplot(2, 1, 1)

    correlations = []
    for distance in distance_light_years:
        corr = -np.cos(np.pi/4)  # Fixed angle
        noise = np.random.randn() * 0.05  # Experimental noise
        correlations.append(corr + noise)

    ax1.plot(distance_light_years, correlations, 'ro-',
            markersize=12, linewidth=3, label='シミュレーション値（固定値＋ノイズ）')
    ax1.axhline(correlations[0], color='blue', linestyle='--',
               linewidth=2, label=f'理論値 ≈ {correlations[0]:.3f}')

    ax1.set_xscale('log')
    ax1.set_xlabel('粒子間の距離（光年）', fontsize=13)
    ax1.set_ylabel('相関の強度', fontsize=13)
    ax1.set_title('量子もつれ：距離は相関を弱めない\n（「局所性」原理の破れ）',
                 fontsize=15, fontweight='bold')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Annotate key distances
    annotations = [
        (0.001, '約63 AU（冥王星軌道の外）'),
        (1, '1光年'),
        (1000, '1000光年\n天の川銀河の\n直径の1%'),
    ]
    for distance, label in annotations:
        idx = distance_light_years.index(distance)
        ax1.annotate(label, xy=(distance, correlations[idx]),
                    xytext=(distance*3, correlations[idx]+0.1),
                    fontsize=10, ha='left',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6),
                    arrowprops=dict(arrowstyle='->', lw=1.5))

    ax1.text(0.5, 0.15,
            '要点：距離に関わらず、相関の強度は不変！\n'
            '情報は「瞬時」に到達し、伝播時間を要しない',
            transform=ax1.transAxes, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === Lower plot: Timeline simulation ===
    ax2 = fig.add_subplot(2, 1, 2)

    time_events = [
        (0, 'AliceとBobが\nもつれ粒子対を受け取る', 'green'),
        (1, 'AliceとBobが離れる\n距離：1000光年', 'blue'),
        (2, 'Aliceがスピンを測定\n（t = 2秒）', 'red'),
        (2.0000001, 'Bobの粒子が\n「瞬時に」確定\n（遅延なし！）', 'red'),
        (3, '光速で伝わるなら\n1000年かかるはず', 'gray'),
    ]

    for t, label, color in time_events:
        if t < 2.5:
            ax2.scatter([t], [1], s=500, c=color, zorder=5,
                       edgecolors='black', linewidth=2)
            ax2.text(t, 1.3, label, ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.5))

    ax2.plot([0, 3], [1, 1], 'k-', linewidth=3)
    ax2.set_xlim(-0.5, 3.5)
    ax2.set_ylim(0.5, 2)
    ax2.set_xlabel('時間（秒）', fontsize=13)
    ax2.set_title('量子もつれのタイムライン：「瞬時の」影響',
                 fontsize=15, fontweight='bold')
    ax2.set_yticks([])
    ax2.grid(True, alpha=0.3, axis='x')

    ax2.annotate('', xy=(2.0000001, 0.9), xytext=(2, 0.9),
                arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax2.text(2.00000005, 0.7, '瞬時！', ha='center', fontsize=12,
            fontweight='bold', color='red')

    ax2.plot([2, 3], [0.8, 0.8], 'gray', linestyle=':', linewidth=3)
    ax2.text(2.5, 0.65, '光速では1000年かかる', ha='center',
            fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig('nonlocal_correlation_demo.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【非局所性：空間と時間を超えて】")
    print("="*70)
    print("\n実験的事実：")
    print("  1. AliceとBobがもつれ粒子対を共有")
    print("  2. 1000光年離れる")
    print("  3. Aliceが測定 → Bobの粒子が瞬時に確定")
    print("  4. 相関の強度は距離で減衰しない")
    print("\n三つの可能な説明：")
    print("  × 情報が超光速で伝播する？")
    print("     → 相対性理論に違反")
    print("  × 粒子が事前に「取り決め」ている？")
    print("     → ベルの不等式が排除")
    print("  ○ もつれ粒子はもともと一つの全体")
    print("     → 「伝播」はない。なぜなら「分離」がないから")
    print("\n華厳宗の視点：")
    print("  「一切法は互いに縁起する」")
    print("  → 独立した「粒子A」と「粒子B」は存在しない")
    print("  → あるのは分離不可能な「系AB」のみ")
    print("  → 「分離」は幻想である")
    print("="*70)

# Execute
nonlocal_correlation_demo()
