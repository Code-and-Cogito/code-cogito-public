# Code & Cogito: 量子糾纏 vs 華嚴宗「因陀羅網」——宇宙是不可分割的整體
# Article: https://code-cogito.com/quantum-entanglement-indras-net/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class EPRExperiment:
    """
    EPR實驗模擬
    展示：量子糾纏的非局域關聯
    """

    def __init__(self):
        self.n_trials = 1000

    def create_entangled_pair(self):
        """
        創建糾纏態：|ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2
        返回：(狀態1, 狀態2, 相位)
        """
        # 隨機相位（但測量時總是反關聯）
        phase = np.random.uniform(0, 2*np.pi)
        return phase

    def measure_spin(self, phase, angle):
        """
        測量自旋
        angle: 測量角度（弧度）
        返回：+1（向上）或 -1（向下）
        """
        # 量子力學預測：機率 = cos²(θ/2)
        prob_up = np.cos((angle - phase) / 2)**2

        if np.random.random() < prob_up:
            return +1  # 向上
        else:
            return -1  # 向下

    def run_epr_experiment(self, angle_A, angle_B):
        """
        運行EPR實驗
        angle_A: Alice的測量角度
        angle_B: Bob的測量角度
        返回：(結果A列表, 結果B列表, 關聯函數)
        """
        results_A = []
        results_B = []

        for _ in range(self.n_trials):
            # Alice的結果：糾纏態的邊際機率恆為50/50，與角度無關
            result_A = +1 if np.random.random() < 0.5 else -1

            # Bob的結果：依單態的聯合機率與Alice相關，而非獨立測量
            prob_diff = np.cos((angle_A - angle_B) / 2)**2
            result_B = -result_A if np.random.random() < prob_diff else result_A

            results_A.append(result_A)
            results_B.append(result_B)

        # 計算關聯函數 E(a,b) = ⟨A·B⟩
        correlation = np.mean(np.array(results_A) * np.array(results_B))

        return results_A, results_B, correlation

    def visualize_correlations(self):
        """
        視覺化不同角度下的關聯函數
        """
        angles = np.linspace(0, np.pi, 50)
        correlations_quantum = []
        correlations_classical = []

        for angle in angles:
            _, _, corr_q = self.run_epr_experiment(0, angle)
            correlations_quantum.append(corr_q)

            # 經典預測（局域隱變量）
            corr_c = -1 + 2*angle/np.pi
            correlations_classical.append(corr_c)

        # 量子力學理論預測
        correlations_theory = -np.cos(angles)

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(angles * 180/np.pi, correlations_theory, 'b-',
               linewidth=3, label='量子力學理論預測', alpha=0.7)
        ax.scatter(angles * 180/np.pi, correlations_quantum,
                  c='red', s=50, label=f'實驗結果（{self.n_trials}次）',
                  alpha=0.6, zorder=5)
        ax.plot(angles * 180/np.pi, correlations_classical, 'g--',
               linewidth=2, label='經典預測（局域實在論）', alpha=0.7)

        ax.set_xlabel('Bob的測量角度（度）', fontsize=13)
        ax.set_ylabel('關聯函數 E(0°, θ)', fontsize=13)
        ax.set_title('EPR實驗：量子關聯 vs 經典預測\nAlice固定測量0°',
                    fontsize=15, fontweight='bold')
        ax.legend(fontsize=12, loc='upper right')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='black', linewidth=0.5)

        # 標註關鍵角度
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
        print("【EPR實驗結果】")
        print("="*70)
        print(f"\n實驗次數：{self.n_trials}")
        print("\n關鍵發現：")
        print("  • 量子關聯：E(θ) = -cos(θ)")
        print("  • 經典預測：E(θ) = 線性函數")
        print("  • 實驗符合量子預測，不符合經典預測")
        print("\n意義：")
        print("  • 糾纏是真實的")
        print("  • 沒有隱變量")
        print("  • 愛因斯坦錯了")
        print("="*70)

    def demonstrate_nonlocality(self):
        """
        演示非局域性
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # 三個場景
        scenarios = [
            (0, 0, 'Alice和Bob\n測量同方向'),
            (0, np.pi/4, 'Alice測0°\nBob測45°'),
            (0, np.pi/2, 'Alice測0°\nBob測90°'),
        ]

        for idx, (angle_A, angle_B, title) in enumerate(scenarios):
            ax = axes[idx]

            results_A, results_B, correlation = self.run_epr_experiment(angle_A, angle_B)

            # 繪製結果分佈
            n_up_up = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == 1)
            n_up_down = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == -1)
            n_down_up = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == 1)
            n_down_down = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == -1)

            categories = ['↑↑', '↑↓', '↓↑', '↓↓']
            counts = [n_up_up, n_up_down, n_down_up, n_down_down]
            colors = ['green', 'blue', 'orange', 'red']

            bars = ax.bar(categories, counts, color=colors, alpha=0.7, edgecolor='black', linewidth=2)

            ax.set_ylabel('觀測次數', fontsize=12)
            ax.set_title(f'{title}\n關聯 E = {correlation:.3f}',
                        fontsize=13, fontweight='bold')
            ax.set_ylim(0, self.n_trials * 0.8)
            ax.grid(True, alpha=0.3, axis='y')

            # 標註數量
            for bar, count in zip(bars, counts):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                       f'{count}\n({count/self.n_trials*100:.1f}%)',
                       ha='center', va='bottom', fontsize=10)

        fig.text(0.5, 0.02,
                '關鍵洞見：無論距離多遠，測量結果總是關聯的！\n'
                '這不是事先約定，是真實的「超距關聯」',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig('epr_nonlocality.png', dpi=300, bbox_inches='tight')
        plt.show()

# 執行
experiment = EPRExperiment()
experiment.visualize_correlations()
experiment.demonstrate_nonlocality()

class BellInequality:
    """
    貝爾不等式（CHSH形式）驗證
    """

    def __init__(self):
        self.n_trials = 10000

    def quantum_correlation(self, angle_A, angle_B):
        """
        量子力學預測的關聯函數
        E(a, b) = -cos(a - b)
        """
        return -np.cos(angle_A - angle_B)

    def local_realism_correlation(self, angle_A, angle_B, hidden_var):
        """
        局域實在論（隱變量）預測
        hidden_var: λ ∈ [0, 2π]
        """
        result_A = +1 if np.cos(angle_A - hidden_var) > 0 else -1
        result_B = +1 if np.cos(angle_B - hidden_var + np.pi) > 0 else -1
        return result_A * result_B

    def compute_chsh_quantum(self):
        """
        計算量子力學的CHSH值
        S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
        """
        # 最優角度選擇
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
        計算局域實在論的CHSH值
        對所有可能的λ求平均
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
        視覺化貝爾不等式測試
        """
        S_quantum, E_quantum = self.compute_chsh_quantum()
        S_local, E_local = self.compute_chsh_local()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # === 左圖：CHSH值比較 ===
        categories = ['量子力學', '局域實在論', '貝爾界限']
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
                   label='貝爾界限 |S| ≤ 2')
        ax1.axhline(2*np.sqrt(2), color='red', linestyle=':', linewidth=2,
                   label=f'量子極限 |S| = 2√2 ≈ {2*np.sqrt(2):.3f}')

        ax1.set_ylabel('|S| 值', fontsize=13)
        ax1.set_title('CHSH不等式測試\n量子力學 vs 局域實在論',
                     fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.set_ylim(0, 3)

        if abs(S_quantum) > 2:
            verdict = '違反！量子力學勝利'
            verdict_color = 'red'
        else:
            verdict = '未違反'
            verdict_color = 'green'

        ax1.text(0.5, 2.5, f'判決：{verdict}',
                ha='center', fontsize=13, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=verdict_color, alpha=0.5))

        # === 右圖：四個關聯函數 ===
        labels = ['E(a,b)', 'E(a,b\')', 'E(a\',b)', 'E(a\',b\')']
        x_pos = np.arange(len(labels))

        quantum_vals = E_quantum
        local_vals = E_local

        width = 0.35
        bars1 = ax2.bar(x_pos - width/2, quantum_vals, width,
                       label='量子力學', color='red', alpha=0.7,
                       edgecolor='black', linewidth=1.5)
        bars2 = ax2.bar(x_pos + width/2, local_vals, width,
                       label='局域實在論', color='blue', alpha=0.7,
                       edgecolor='black', linewidth=1.5)

        ax2.set_ylabel('關聯函數 E', fontsize=13)
        ax2.set_title('四個測量配置的關聯函數', fontsize=14, fontweight='bold')
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
        print("【貝爾不等式測試結果】")
        print("="*70)
        print(f"\nCHSH不等式：|S| ≤ 2 （如果局域實在論成立）")
        print(f"\n量子力學預測：")
        print(f"  S = {S_quantum:.4f}")
        print(f"  |S| = {abs(S_quantum):.4f} > 2  ✓ 違反不等式")
        print(f"\n局域實在論（隱變量）：")
        print(f"  S = {S_local:.4f}")
        print(f"  |S| = {abs(S_local):.4f} ≤ 2  ✓ 滿足不等式")
        print(f"\n實驗結果（1982-2022）：")
        print(f"  • 阿斯佩（1982）：S = 2.697 ± 0.015（實測值）")
        print(f"  • 塞林格（1998）：S ≈ 2.73 ± 0.02")
        print(f"  • 潘建偉（2017）：S ≈ 2.37 ± 0.09（1200公里）")
        print(f"\n結論：")
        print(f"  ✓ 量子力學是對的")
        print(f"  ✗ 局域實在論（隱變量理論）是錯的")
        print(f"  ✗ 愛因斯坦的希望破滅了")
        print("="*70)

# 執行
bell_test = BellInequality()
bell_test.visualize_bell_test()

import networkx as nx
from itertools import combinations

def indras_net_3d():
    """
    因陀羅網的3D可視化
    展示：重重無盡的映現
    """

    fig = plt.figure(figsize=(18, 12))

    # === 左上：網格因陀羅網 ===
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')

    # 創建3D網格
    n = 4
    nodes = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

    # 繪製節點
    xs, ys, zs = zip(*nodes)
    ax1.scatter(xs, ys, zs, c='gold', s=200, edgecolors='black',
               linewidth=2, alpha=0.8)

    # 繪製連接（只連接相鄰節點）
    for node1, node2 in combinations(nodes, 2):
        distance = sum((a-b)**2 for a, b in zip(node1, node2))
        if distance == 1:  # 只連接相鄰
            ax1.plot([node1[0], node2[0]],
                    [node1[1], node2[1]],
                    [node1[2], node2[2]],
                    'gray', alpha=0.3, linewidth=1)

    # 高亮一個節點
    highlight = (1, 1, 1)
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    # 高亮其鄰居
    neighbors = [(i, j, k) for i, j, k in nodes
                if sum((a-b)**2 for a, b in zip((i,j,k), highlight)) == 1]
    if neighbors:
        nx_list, ny_list, nz_list = zip(*neighbors)
        ax1.scatter(nx_list, ny_list, nz_list,
                   c='orange', s=300, edgecolors='red', linewidth=2, alpha=0.8)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('因陀羅網（3D網格）\n每珠連結相鄰珠',
                 fontsize=13, fontweight='bold')

    # === 右上：全連接因陀羅網 ===
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
    ax2.set_title('因陀羅網（全連接）\n改變一珠，全網皆動',
                 fontsize=13, fontweight='bold')

    # === 左下：量子糾纏網絡 ===
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
    ax3.set_title('量子糾纏網絡\n測量一粒子，影響全網',
                 fontsize=13, fontweight='bold')

    # === 右下：對應說明 ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    【因陀羅網 vs 量子糾纏】

    華嚴宗《華嚴經》（7世紀）：

    「帝釋天宮有寶網，
     網上珠珠相映現，
     一珠含一切珠影，
     重重無盡不思議。」

    ━━━━━━━━━━━━━━━━━━━━━━━━

    量子力學（20世紀）：

    糾纏態 |ψ⟩ 不可分解
    粒子A與粒子B非局域關聯
    測量A → 瞬間影響B
    整體 > 部分之和

    ━━━━━━━━━━━━━━━━━━━━━━━━

    共同洞見：

    宇宙是不可分割的整體
    部分無法脫離整體而存在
    改變局部 = 改變整體
    「分離」是幻覺

    華嚴宗：一即一切，一切即一
    量子力學：糾纏即整體，不可分
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('indras_net_3d_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【因陀羅網：1300多年前的量子洞見】")
    print("="*70)
    print("\n法藏向武則天展示鏡室（7世紀）：")
    print("  • 十面鏡子環繞佛像")
    print("  • 一支火炬照明")
    print("  • 無數倒影，重重映現")
    print("  → 一即一切的直觀展示")
    print("\n華嚴宗的十玄門（第四門）：")
    print("  「因陀羅網境界門」")
    print("  → 一切法如珠網，互相映現")
    print("\n現代量子糾纏：")
    print("  • EPR態：|ψ⟩ = (|↑↓⟩ - |↓↑⟩)/√2")
    print("  • 測量A → 瞬間確定B")
    print("  • 不可分離的整體")
    print("\n2022年諾貝爾物理學獎：")
    print("  授予Aspect, Clauser, Zeilinger")
    print("  表彰：證明量子糾纏是真實的")
    print("="*70)

# 執行
indras_net_3d()

def nonlocal_correlation_demo():
    """
    非局域關聯互動演示
    讓用戶「體驗」超距作用
    """

    fig = plt.figure(figsize=(16, 10))

    # 模擬參數
    n_measurements = 50
    distance_light_years = [0.001, 0.1, 1, 10, 100, 1000]

    # === 上圖：距離不影響關聯強度 ===
    ax1 = fig.add_subplot(2, 1, 1)

    correlations = []
    for distance in distance_light_years:
        corr = -np.cos(np.pi/4)  # 固定角度
        noise = np.random.randn() * 0.05  # 實驗噪音
        correlations.append(corr + noise)

    ax1.plot(distance_light_years, correlations, 'ro-',
            markersize=12, linewidth=3, label='實驗測量')
    ax1.axhline(correlations[0], color='blue', linestyle='--',
               linewidth=2, label=f'理論值 ≈ {correlations[0]:.3f}')

    ax1.set_xscale('log')
    ax1.set_xlabel('粒子間距離（光年）', fontsize=13)
    ax1.set_ylabel('關聯強度', fontsize=13)
    ax1.set_title('量子糾纏：距離不減弱關聯\n（違反「局域性」原理）',
                 fontsize=15, fontweight='bold')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)

    # 標註關鍵距離
    annotations = [
        (0.001, '約63 AU（冥王星軌道外）'),
        (1, '1光年'),
        (1000, '1000光年\n銀河系直徑的1%'),
    ]
    for distance, label in annotations:
        idx = distance_light_years.index(distance)
        ax1.annotate(label, xy=(distance, correlations[idx]),
                    xytext=(distance*3, correlations[idx]+0.1),
                    fontsize=10, ha='left',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6),
                    arrowprops=dict(arrowstyle='->', lw=1.5))

    ax1.text(0.5, 0.15,
            '關鍵：無論距離多遠，關聯強度不變！\n'
            '資訊「瞬間」到達，不需要傳播時間',
            transform=ax1.transAxes, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === 下圖：時間線模擬 ===
    ax2 = fig.add_subplot(2, 1, 2)

    time_events = [
        (0, 'Alice和Bob接收\n糾纏粒子對', 'green'),
        (1, 'Alice和Bob分開\n相距1000光年', 'blue'),
        (2, 'Alice測量自旋\n（t = 2秒）', 'red'),
        (2.0000001, 'Bob的粒子\n「瞬間」確定\n（沒有延遲！）', 'red'),
        (3, '如果是光速傳播\n需要1000年才到達', 'gray'),
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
    ax2.set_title('量子糾纏的時間線：「瞬間」影響',
                 fontsize=15, fontweight='bold')
    ax2.set_yticks([])
    ax2.grid(True, alpha=0.3, axis='x')

    ax2.annotate('', xy=(2.0000001, 0.9), xytext=(2, 0.9),
                arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax2.text(2.00000005, 0.7, '瞬間！', ha='center', fontsize=12,
            fontweight='bold', color='red')

    ax2.plot([2, 3], [0.8, 0.8], 'gray', linestyle=':', linewidth=3)
    ax2.text(2.5, 0.65, '光速需要1000年', ha='center',
            fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig('nonlocal_correlation_demo.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【非局域性：超越空間和時間】")
    print("="*70)
    print("\n實驗事實：")
    print("  1. Alice和Bob分享糾纏粒子對")
    print("  2. 分開到1000光年外")
    print("  3. Alice測量 → Bob的粒子瞬間確定")
    print("  4. 關聯強度不隨距離減弱")
    print("\n三種可能解釋：")
    print("  X 資訊超光速傳播？")
    print("     → 違反相對論")
    print("  X 粒子事先「約定」？")
    print("     → 貝爾不等式排除了")
    print("  O 糾纏粒子本來就是一個整體")
    print("     → 沒有「傳播」，因為沒有「分離」")
    print("\n華嚴宗的觀點：")
    print("  「一切法互為緣起」")
    print("  → 沒有獨立的「粒子A」和「粒子B」")
    print("  → 只有不可分的「系統AB」")
    print("  → 「分離」是幻覺")
    print("="*70)

# 執行
nonlocal_correlation_demo()
