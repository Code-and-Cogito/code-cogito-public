# Code & Cogito: 量子計算 vs 禪宗——超越二元邏輯
# Article: https://code-cogito.com/quantum-computing-zen-beyond-binary/
# All the code blocks of the article, in order. Program output is kept as comments.

# | H = (1/√2) × [1   1]
# |               [1  -1]

# | X = [0  1]
# |     [1  0]

# | Z = [1   0]
# |     [0  -1]

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumBitSimulator:
    """
    量子比特模擬器
    展示：量子比特的疊加態與Bloch球
    """

    def __init__(self):
        pass

    def bloch_sphere(self, ax, state_vector, label):
        """
        繪製Bloch球和量子態
        """
        # Bloch球面
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, alpha=0.2, color='cyan')

        # 座標軸
        ax.plot([0, 1.3], [0, 0], [0, 0], 'k-', linewidth=1, alpha=0.5)
        ax.plot([0, 0], [0, 1.3], [0, 0], 'k-', linewidth=1, alpha=0.5)
        ax.plot([0, 0], [0, 0], [0, 1.3], 'k-', linewidth=1, alpha=0.5)

        ax.text(1.4, 0, 0, 'X', fontsize=10)
        ax.text(0, 1.4, 0, 'Y', fontsize=10)
        ax.text(0, 0, 1.4, 'Z', fontsize=10)

        # |0⟩ 和 |1⟩
        ax.text(0, 0, 1.2, '|0⟩', fontsize=12, color='blue', fontweight='bold')
        ax.text(0, 0, -1.2, '|1⟩', fontsize=12, color='red', fontweight='bold')

        # 量子態向量：從振幅計算 Bloch 球座標
        alpha, beta = state_vector
        theta = 2 * np.arccos(np.abs(alpha))
        phi = np.angle(beta) - np.angle(alpha)

        sx = np.sin(theta) * np.cos(phi)
        sy = np.sin(theta) * np.sin(phi)
        sz = np.cos(theta)

        ax.quiver(0, 0, 0, sx, sy, sz, color='purple',
                 arrow_length_ratio=0.15, linewidth=3)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(label, fontsize=13, fontweight='bold')

    def visualize_quantum_states(self):
        """
        視覺化不同的量子態
        """
        fig = plt.figure(figsize=(18, 12))

        # === |0⟩ 態 ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')
        self.bloch_sphere(ax1, [1, 0], '|0⟩ 態\n（北極）')

        # === |1⟩ 態 ===
        ax2 = fig.add_subplot(2, 3, 2, projection='3d')
        self.bloch_sphere(ax2, [0, 1], '|1⟩ 態\n（南極）')

        # === |+⟩ 態（疊加態）===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')
        self.bloch_sphere(ax3, [1/np.sqrt(2), 1/np.sqrt(2)],
                         '|+⟩ = (|0⟩+|1⟩)/√2\n（赤道）')

        # === |-⟩ 態（疊加態）===
        ax4 = fig.add_subplot(2, 3, 4, projection='3d')
        self.bloch_sphere(ax4, [1/np.sqrt(2), -1/np.sqrt(2)],
                         '|−⟩ = (|0⟩−|1⟩)/√2\n（赤道）')

        # === 任意疊加態 ===
        ax5 = fig.add_subplot(2, 3, 5, projection='3d')
        alpha = np.cos(np.pi/6)
        beta = np.sin(np.pi/6) * np.exp(1j * np.pi/4)
        self.bloch_sphere(ax5, [alpha, beta],
                         '任意疊加態\n球面上任意點')

        # === 對比說明 ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text = '''
        【量子比特 vs 經典比特】

        經典比特：
        • 只有兩個狀態：0 或 1
        • 非黑即白
        • 二元邏輯

        量子比特：
        • 疊加態：α|0⟩ + β|1⟩
        • |α|² + |β|² = 1
        • 既0又1
        • 超越二元

        Bloch球：
        • 球面上每個點 = 一個量子態
        • 北極 = |0⟩
        • 南極 = |1⟩
        • 赤道 = 疊加態
        • 球內沒有量子態（純態）

        禪宗類比：
        • 經典：有 or 無
        • 量子：既有又無（疊加）
        • 禪：超越有無（不二）

        Hadamard門：
        H|0⟩ = (|0⟩+|1⟩)/√2
        → 從北極到赤道
        → 創造疊加態
        → 打破二元對立
        '''

        ax6.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('quantum_bit_bloch_sphere.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子比特：超越0與1】")
        print("="*70)

        print("\n經典比特：")
        print("  • 只有兩個狀態：0 或 1")
        print("  • 布爾邏輯：AND, OR, NOT")
        print("  • 非此即彼")

        print("\n量子比特：")
        print("  • 疊加態：|ψ⟩ = α|0⟩ + β|1⟩")
        print("  • α, β 是複數")
        print("  • |α|² + |β|² = 1")
        print("  • |α|² = 測量到|0⟩的機率")
        print("  • |β|² = 測量到|1⟩的機率")

        print("\n關鍵區別：")
        print("  經典：0 或 1（二選一）")
        print("  量子：既0又1（疊加）")

        print("\nBloch球：")
        print("  • 球面上每個點代表一個量子態")
        print("  • |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩")
        print("  • θ ∈ [0,π], φ ∈ [0,2π]")

        print("\n常見量子態：")
        print("  • |0⟩：北極")
        print("  • |1⟩：南極")
        print("  • |+⟩ = (|0⟩+|1⟩)/√2：赤道（X軸）")
        print("  • |−⟩ = (|0⟩−|1⟩)/√2：赤道（−X軸）")
        print("  • |i⟩ = (|0⟩+i|1⟩)/√2：赤道（Y軸）")

        print("\n禪宗類比：")
        print("  經典比特 ≈ 二元對立（有/無）")
        print("  量子比特 ≈ 不二法門（超越有無）")
        print("  疊加態 ≈ 「非有非無」")

        print("\nHadamard門的哲學意義：")
        print("  H|0⟩ = (|0⟩+|1⟩)/√2")
        print("  → 把「確定」變成「疊加」")
        print("  → 打破二元對立")
        print("  → 進入「既A又非A」的狀態")
        print("="*70)

# 執行
simulator = QuantumBitSimulator()
simulator.visualize_quantum_states()

class HadamardGateSimulator:
    """
    Hadamard門模擬器
    展示：如何創造疊加態，打破二元對立
    """

    def __init__(self):
        self.H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

    def apply_hadamard(self, state):
        """應用Hadamard門"""
        return self.H @ state

    def visualize_hadamard_transformation(self):
        """
        視覺化Hadamard門的轉換過程
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        # === 初態：|0⟩（確定）===
        ax = axes[0, 0]
        ax.bar(['|0⟩', '|1⟩'], [1, 0], color=['blue', 'red'], alpha=0.7,
              edgecolor='black', linewidth=2)
        ax.set_ylabel('振幅', fontsize=12)
        ax.set_title('初態：|0⟩\n完全確定', fontsize=13, fontweight='bold')
        ax.set_ylim(-0.8, 1.2)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        # === Hadamard門作用 ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        rect = plt.Rectangle((0.35, 0.4), 0.3, 0.2,
                            facecolor='yellow', alpha=0.7,
                            edgecolor='black', linewidth=3)
        ax.add_patch(rect)
        ax.text(0.5, 0.5, 'H', ha='center', va='center',
               fontsize=24, fontweight='bold')

        ax.annotate('', xy=(0.5, 0.35), xytext=(0.5, 0.8),
                   arrowprops=dict(arrowstyle='->', lw=4, color='purple'))
        ax.text(0.6, 0.6, '轉換', ha='left', fontsize=12,
               color='purple', fontweight='bold')

        ax.set_title('Hadamard門\n創造疊加態', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, 'H|0⟩ = (|0⟩+|1⟩)/√2', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === 結果：|+⟩（疊加）===
        ax = axes[0, 2]
        amplitudes = [1/np.sqrt(2), 1/np.sqrt(2)]
        ax.bar(['|0⟩', '|1⟩'], amplitudes, color=['blue', 'red'], alpha=0.7,
              edgecolor='black', linewidth=2)
        ax.set_ylabel('振幅', fontsize=12)
        ax.set_title('結果：|+⟩ = (|0⟩+|1⟩)/√2\n疊加態',
                    fontsize=13, fontweight='bold')
        ax.set_ylim(-0.8, 1.2)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        for i, (label, amp) in enumerate(zip(['|0⟩', '|1⟩'], amplitudes)):
            ax.text(i, amp + 0.1, f'{amp:.3f}', ha='center', fontsize=10,
                   fontweight='bold')

        # === 禪宗類比：執著 ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle = plt.Circle((0.5, 0.6), 0.15, color='blue', alpha=0.6,
                           edgecolor='black', linewidth=3)
        ax.add_patch(circle)
        ax.text(0.5, 0.6, '執著\n「有」', ha='center', va='center',
               fontsize=12, fontweight='bold', color='white')

        ax.text(0.5, 0.3, '二元對立：有 or 無', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue'))

        ax.set_title('初始：執著於「有」\n二元思維', fontsize=13, fontweight='bold')

        # === 禪宗類比：破執 ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ax.text(0.5, 0.5, '喝！', ha='center', va='center',
               fontsize=36, fontweight='bold', color='red')

        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            x = 0.5 + 0.3 * np.cos(angle)
            y = 0.5 + 0.3 * np.sin(angle)
            ax.plot([0.5, x], [0.5, y], 'yellow', linewidth=3, alpha=0.7)

        ax.set_title('棒喝/公案\n打破執著', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, '破除二元對立', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === 禪宗類比：不二 ===
        ax = axes[1, 2]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle1 = plt.Circle((0.45, 0.5), 0.15, color='blue', alpha=0.3,
                            edgecolor='blue', linewidth=2)
        circle2 = plt.Circle((0.55, 0.5), 0.15, color='red', alpha=0.3,
                            edgecolor='red', linewidth=2)
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        ax.text(0.5, 0.5, '不二', ha='center', va='center',
               fontsize=14, fontweight='bold', color='purple')

        ax.text(0.5, 0.3, '超越有無\n非有非無', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen'))

        ax.set_title('結果：不二法門\n超越二元', fontsize=13, fontweight='bold')

        fig.text(0.5, 0.98, 'Hadamard門 vs 禪宗「破執」',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        plt.savefig('hadamard_gate_zen.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【Hadamard門：創造疊加態，打破二元】")
        print("="*70)

        print("\nHadamard門的數學：")
        print("  H = (1/√2) × [1   1]")
        print("                [1  -1]")

        print("\n作用：")
        print("  H|0⟩ = (|0⟩ + |1⟩) / √2 = |+⟩")
        print("  H|1⟩ = (|0⟩ − |1⟩) / √2 = |−⟩")

        print("\n意義：")
        print("  • 從確定態 → 疊加態")
        print("  • 從「0或1」→「既0又1」")
        print("  • 打破二元對立")

        print("\n量子計算中的作用：")
        print("  • 創造疊加態（量子並行性的基礎）")
        print("  • 量子算法的第一步")
        print("  • 例：Grover算法、Shor算法")

        print("\n禪宗類比：")
        print("  初始：執著於「有」或「無」")
        print("  → 二元對立思維")

        print("\n  棒喝/公案：打破執著")
        print("  → 像Hadamard門打破確定性")

        print("\n  結果：不二法門")
        print("  → 超越「有無」的二元對立")
        print("  → 像疊加態超越「0/1」")

        print("\n深刻類比：")
        print("  Hadamard門 ≈ 禪宗「破執」")
        print("  疊加態 ≈ 不二法門")
        print("  測量坍縮 ≈ 起念執著")

        print("\n六祖慧能：")
        print("  「不思善，不思惡，")
        print("   正與麼時，哪個是明上座本來面目？」")
        print("  → 超越善惡二元，直指本心")
        print("  → 像疊加態超越0/1二元")
        print("="*70)

# 執行
hadamard_sim = HadamardGateSimulator()
hadamard_sim.visualize_hadamard_transformation()

class QuantumParallelismSimulator:
    """
    量子並行性模擬器
    展示：如何同時計算所有可能
    """

    def __init__(self):
        pass

    def visualize_quantum_parallelism(self):
        """
        視覺化量子並行性
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === 左圖：經典並行計算 ===
        n_bits = 3
        n_states = 2 ** n_bits

        # 經典：需要逐個計算
        for i in range(n_states):
            binary = format(i, f'0{n_bits}b')
            y = n_states - i - 1

            # 輸入
            rect_input = plt.Rectangle((0.1, y*0.12), 0.15, 0.1,
                                      facecolor='lightblue', alpha=0.7,
                                      edgecolor='blue', linewidth=1.5)
            ax1.add_patch(rect_input)
            ax1.text(0.175, y*0.12 + 0.05, binary, ha='center', va='center',
                    fontsize=9)

            # 函數f
            rect_f = plt.Rectangle((0.4, y*0.12), 0.15, 0.1,
                                  facecolor='yellow', alpha=0.7,
                                  edgecolor='orange', linewidth=1.5)
            ax1.add_patch(rect_f)
            ax1.text(0.475, y*0.12 + 0.05, 'f(x)', ha='center', va='center',
                    fontsize=9, fontweight='bold')

            # 箭頭
            ax1.annotate('', xy=(0.4, y*0.12 + 0.05), xytext=(0.25, y*0.12 + 0.05),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
            ax1.annotate('', xy=(0.7, y*0.12 + 0.05), xytext=(0.55, y*0.12 + 0.05),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

            # 輸出
            output_value = (i * 2) % n_states  # 示例函數
            rect_output = plt.Rectangle((0.7, y*0.12), 0.15, 0.1,
                                       facecolor='lightgreen', alpha=0.7,
                                       edgecolor='green', linewidth=1.5)
            ax1.add_patch(rect_output)
            ax1.text(0.775, y*0.12 + 0.05, f'{output_value}', ha='center', va='center',
                    fontsize=9)

        ax1.set_xlim(0, 1)
        ax1.set_ylim(-0.1, 1.1)
        ax1.axis('off')
        ax1.set_title(f'經典計算：逐個處理\n{n_states}次運算',
                     fontsize=14, fontweight='bold')

        ax1.text(0.5, -0.05, f'時間複雜度：O({n_states})',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === 右圖：量子並行計算 ===

        # 初態
        rect_init = plt.Rectangle((0.1, 0.4), 0.15, 0.2,
                                 facecolor='lightblue', alpha=0.7,
                                 edgecolor='blue', linewidth=2)
        ax2.add_patch(rect_init)
        ax2.text(0.175, 0.5, '|0...0⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # Hadamard門
        rect_h = plt.Rectangle((0.35, 0.4), 0.15, 0.2,
                              facecolor='yellow', alpha=0.7,
                              edgecolor='orange', linewidth=2)
        ax2.add_patch(rect_h)
        ax2.text(0.425, 0.5, 'H⊗n', ha='center', va='center',
                fontsize=11, fontweight='bold')

        ax2.annotate('', xy=(0.35, 0.5), xytext=(0.25, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=3, color='purple'))

        # 疊加態
        superposition_text = '|ψ⟩ = Σ|x⟩'
        rect_super = plt.Rectangle((0.6, 0.35), 0.15, 0.3,
                                  facecolor='purple', alpha=0.3,
                                  edgecolor='purple', linewidth=2)
        ax2.add_patch(rect_super)

        for i in range(min(n_states, 8)):
            binary = format(i, f'0{n_bits}b')
            y_offset = 0.65 - i * 0.035
            ax2.text(0.675, y_offset, f'|{binary}⟩', ha='center',
                    fontsize=7, alpha=0.8)

        ax2.text(0.675, 0.4, superposition_text, ha='center', va='center',
                fontsize=10, fontweight='bold', color='purple')

        ax2.annotate('', xy=(0.6, 0.5), xytext=(0.5, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=3, color='purple'))

        # 函數U_f
        rect_uf = plt.Rectangle((0.35, 0.1), 0.15, 0.15,
                               facecolor='yellow', alpha=0.7,
                               edgecolor='orange', linewidth=2)
        ax2.add_patch(rect_uf)
        ax2.text(0.425, 0.175, 'U_f', ha='center', va='center',
                fontsize=11, fontweight='bold')

        ax2.plot([0.675, 0.675, 0.425, 0.425], [0.35, 0.25, 0.25, 0.25],
                'purple', linewidth=2, alpha=0.6)
        ax2.annotate('', xy=(0.425, 0.25), xytext=(0.425, 0.28),
                    arrowprops=dict(arrowstyle='->', lw=2, color='purple'))

        result_text = 'Σ|x⟩|f(x)⟩'
        ax2.text(0.425, 0.05, result_text, ha='center', va='center',
                fontsize=10, fontweight='bold', color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 0.8)
        ax2.axis('off')
        ax2.set_title(f'量子計算：並行處理\n1次運算！',
                     fontsize=14, fontweight='bold')

        ax2.text(0.5, -0.05, '時間複雜度：O(1)',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
                transform=ax2.transAxes)

        fig.text(0.5, 0.98, f'量子並行性：{n_states}個狀態同時計算',
                ha='center', fontsize=16, fontweight='bold')

        explanation = '''
        經典計算：逐個計算 f(x)，需要 2^n 次
        量子計算：創造疊加態 Σ|x⟩，一次計算所有 f(x)

        禪宗類比：
        經典：一念生一法（逐個）
        量子：一念生萬法（同時）
        禪：「一心萬法」，一念頓現萬法
        '''

        fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        plt.tight_layout()
        plt.subplots_adjust(top=0.9, bottom=0.15)
        plt.savefig('quantum_parallelism.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子並行性：一次計算所有可能】")
        print("="*70)

        print(f"\n問題：計算函數 f(x) 對所有 x ∈ {{0,1}}^{n_bits} 的值")
        print(f"共有 {n_states} 個可能的x")

        print("\n經典計算：")
        print(f"  • 逐個計算 f(0), f(1), ..., f({n_states-1})")
        print(f"  • 需要 {n_states} 次運算")
        print(f"  • 時間複雜度：O(2^n)")

        print("\n量子計算：")
        print("  1. 創造疊加態：H⊗n|0⟩^n = Σ|x⟩")
        print("  2. 應用函數：U_f Σ|x⟩ = Σ|x⟩|f(x)⟩")
        print("  3. 一次運算得到所有結果！")
        print("  • 時間複雜度：O(1)")

        print("\n關鍵技術：")
        print("  • 疊加態：同時表示所有可能")
        print("  • 量子門：一次作用在所有狀態")
        print("  • 量子干涉：增強正確答案")

        print("\n陷阱：")
        print("  • 測量會坍縮，只得到一個結果")
        print("  • 需要量子干涉來「提取」資訊")

        print("\n禪宗類比：")
        print("  經典思維：")
        print("    一念生一法（串行）")
        print("    逐個思考，逐個解決")

        print("\n  量子/禪：")
        print("    一念生萬法（並行）")
        print("    一念頓現，萬法俱足")

        print("\n華嚴宗「一心萬法」：")
        print("  • 一個心念包含萬法")
        print("  • 不是逐個生起")
        print("  • 而是同時具足")

        print("\n量子並行性 ≈ 一心萬法：")
        print("  • 一個疊加態包含所有可能")
        print("  • 一次運算作用在所有可能")
        print("  • 超越線性時間")

        print("\n深刻洞見：")
        print("  線性思維：A → B → C（串行）")
        print("  量子/禪：A+B+C 同時（並行）")
        print("  → 超越時間的順序性")
        print("="*70)

# 執行
parallelism_sim = QuantumParallelismSimulator()
parallelism_sim.visualize_quantum_parallelism()

def visualize_measurement_念():
    """
    視覺化測量坍縮與禪宗「起念」的對應
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === 量子：測量前（疊加態）===
    ax = axes[0, 0]

    states = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    amplitudes = [0.5, 0.5, 0.5, 0.5]

    ax.bar(states, amplitudes, color='purple', alpha=0.6,
          edgecolor='black', linewidth=2)
    ax.set_ylabel('振幅', fontsize=12)
    ax.set_title('量子：測量前（疊加態）\n所有可能同時存在',
                fontsize=13, fontweight='bold')
    ax.set_ylim(0, 0.8)
    ax.grid(True, alpha=0.3, axis='y')

    ax.text(0.5, 0.7, '|ψ⟩ = Σ|x⟩', transform=ax.transAxes,
           ha='center', fontsize=11, fontweight='bold', color='purple')

    # === 量子：測量（坍縮）===
    ax = axes[0, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, '測量\n坍縮', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, '|10⟩', ha='center', fontsize=16,
           fontweight='bold', color='green',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('測量：坍縮\n疊加態→確定態', fontsize=13, fontweight='bold')

    # === 禪：無念（不二）===
    ax = axes[1, 0]

    thoughts = ['喜', '怒', '哀', '樂', '愛', '恨', '欲']
    np.random.seed(42)
    for thought in thoughts:
        x, y = np.random.random(2)
        ax.text(x, y, thought, fontsize=14, alpha=0.3,
               color=np.random.choice(['blue', 'red', 'green', 'purple']))

    circle = plt.Circle((0.5, 0.5), 0.15, color='gold', alpha=0.5,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '無念\n不二', ha='center', va='center',
           fontsize=12, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('禪：無念（不二）\n超越二元對立', fontsize=13, fontweight='bold')

    # === 禪：起念（執著）===
    ax = axes[1, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, '起念\n執著', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, '愛', ha='center', fontsize=20,
           fontweight='bold', color='red',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('起念：執著\n無念→有念', fontsize=13, fontweight='bold')

    fig.text(0.5, 0.98, '測量坍縮 vs 起念執著',
            ha='center', fontsize=16, fontweight='bold')

    comparison = '''
    量子測量：                    禪宗起念：
    • 測量前：疊加態              • 無念：不二，超越對立
    • 所有可能同時存在            • 心不住於任何念
    • 測量：坍縮                  • 起念：執著
    • 選擇一個結果                • 執著一個念頭
    • 失去疊加性                  • 落入二元對立

    共同點：
    觀察/起念 → 從「超越二元」到「落入二元」
    疊加態/無念 → 確定態/有念
    '''

    fig.text(0.5, 0.02, comparison, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.18)
    plt.savefig('measurement_collapse_念.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【測量坍縮 vs 禪宗「起念」】")
    print("="*70)

    print("\n量子測量：")
    print("  測量前：|ψ⟩ = Σα_i|i⟩（疊加態）")
    print("  → 所有可能同時存在")
    print("  → 超越「0或1」的二元")

    print("\n  測量時：波函數坍縮")
    print("  → 隨機選擇一個結果|i⟩")
    print("  → 機率 = |α_i|²")

    print("\n  測量後：確定態|i⟩")
    print("  → 失去疊加性")
    print("  → 回到「0或1」的二元")

    print("\n禪宗「起念」：")
    print("  無念：心不住於任何念")
    print("  → 超越喜怒哀樂的對立")
    print("  → 超越「有無」的二元")
    print("  → 不二法門")

    print("\n  起念：執著一個念頭")
    print("  → 例如：執著於「愛」")
    print("  → 就產生了「愛/恨」的對立")

    print("\n  有念：落入二元對立")
    print("  → 喜/怒，好/壞，對/錯")
    print("  → 失去「不二」")

    print("\n對應：")
    print("  疊加態 ≈ 無念")
    print("  測量 ≈ 起念")
    print("  坍縮 ≈ 執著")
    print("  確定態 ≈ 有念")

    print("\n六祖慧能：")
    print("  「何期自性，本自清淨。」")
    print("  → 本來面目是「無念」（清淨）")

    print("\n  「念念不住」")
    print("  → 不執著於任何念頭")
    print("  → 保持「無念」狀態")
    print("  → 像保持疊加態不坍縮")

    print("\n深刻類比：")
    print("  • 測量破壞疊加性")
    print("    → 起念破壞無念")
    print("  • 疊加態是「潛在的」")
    print("    → 無念是「超越的」")
    print("  • 坍縮是「選擇」")
    print("    → 執著是「固化」")

    print("\n問題：")
    print("  • 如何保持疊加態不坍縮？")
    print("    → 量子糾錯，退相干時間")
    print("  • 如何保持無念不起念？")
    print("    → 禪修，覺照")

    print("\n最終洞見：")
    print("  量子計算的威力來自「保持疊加態」")
    print("  禪的智慧來自「保持無念」")
    print("  兩者都是超越二元對立")
    print("="*70)

# 執行
visualize_measurement_念()
