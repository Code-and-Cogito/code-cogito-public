# Code & Cogito: 量子コンピューティング vs 禅 ── 二元論理を超えて
# Article: https://code-cogito.com/ja/quantum-computing-zen-beyond-binary-ja/
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

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumBitSimulator:
    """
    Quantum bit simulator
    Demonstrates: qubit superposition states and the Bloch sphere
    """

    def __init__(self):
        pass

    def bloch_sphere(self, ax, state_vector, label):
        """
        Draw the Bloch sphere and a quantum state vector
        """
        # Bloch sphere surface
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, alpha=0.2, color='cyan')

        # Coordinate axes
        ax.plot([0, 1.3], [0, 0], [0, 0], 'k-', linewidth=1, alpha=0.5)
        ax.plot([0, 0], [0, 1.3], [0, 0], 'k-', linewidth=1, alpha=0.5)
        ax.plot([0, 0], [0, 0], [0, 1.3], 'k-', linewidth=1, alpha=0.5)

        ax.text(1.4, 0, 0, 'X', fontsize=10)
        ax.text(0, 1.4, 0, 'Y', fontsize=10)
        ax.text(0, 0, 1.4, 'Z', fontsize=10)

        # |0⟩ and |1⟩ labels
        ax.text(0, 0, 1.2, '|0⟩', fontsize=12, color='blue', fontweight='bold')
        ax.text(0, 0, -1.2, '|1⟩', fontsize=12, color='red', fontweight='bold')

        # Quantum state vector: compute Bloch sphere coordinates from amplitudes
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
        Visualize different quantum states on the Bloch sphere
        """
        fig = plt.figure(figsize=(18, 12))

        # === |0⟩ state ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')
        self.bloch_sphere(ax1, [1, 0], '|0⟩ 状態\n（北極）')

        # === |1⟩ state ===
        ax2 = fig.add_subplot(2, 3, 2, projection='3d')
        self.bloch_sphere(ax2, [0, 1], '|1⟩ 状態\n（南極）')

        # === |+⟩ state (superposition) ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')
        self.bloch_sphere(ax3, [1/np.sqrt(2), 1/np.sqrt(2)],
                         '|+⟩ = (|0⟩+|1⟩)/√2\n（赤道）')

        # === |-⟩ state (superposition) ===
        ax4 = fig.add_subplot(2, 3, 4, projection='3d')
        self.bloch_sphere(ax4, [1/np.sqrt(2), -1/np.sqrt(2)],
                         '|−⟩ = (|0⟩−|1⟩)/√2\n（赤道）')

        # === Arbitrary superposition state ===
        ax5 = fig.add_subplot(2, 3, 5, projection='3d')
        alpha = np.cos(np.pi/6)
        beta = np.sin(np.pi/6) * np.exp(1j * np.pi/4)
        self.bloch_sphere(ax5, [alpha, beta],
                         '任意の重ね合わせ状態\n球面上の任意の点')

        # === Comparison panel ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text = '''
        【量子ビット vs 古典ビット】

        古典ビット：
        ・2つの状態のみ：0 または 1
        ・白か黒か
        ・二元論理

        量子ビット：
        ・重ね合わせ状態：α|0⟩ + β|1⟩
        ・|α|² + |β|² = 1
        ・0でもあり1でもある
        ・二元を超越

        ブロッホ球：
        ・球面上の各点 = 一つの量子状態
        ・北極 = |0⟩
        ・南極 = |1⟩
        ・赤道 = 重ね合わせ状態
        ・球内には量子状態なし（純粋状態）

        禅との対応：
        ・古典：有 or 無
        ・量子：有でもあり無でもある（重ね合わせ）
        ・禅：有無を超える（不二）

        アダマールゲート：
        H|0⟩ = (|0⟩+|1⟩)/√2
        → 北極から赤道へ
        → 重ね合わせ状態を生成
        → 二元対立を打ち破る
        '''

        ax6.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('quantum_bit_bloch_sphere.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子ビット：0と1を超えて】")
        print("="*70)

        print("\n古典ビット：")
        print("  ・2つの状態のみ：0 または 1")
        print("  ・ブール論理：AND, OR, NOT")
        print("  ・二者択一")

        print("\n量子ビット：")
        print("  ・重ね合わせ状態：|ψ⟩ = α|0⟩ + β|1⟩")
        print("  ・α, β は複素数")
        print("  ・|α|² + |β|² = 1")
        print("  ・|α|² = |0⟩が測定される確率")
        print("  ・|β|² = |1⟩が測定される確率")

        print("\n核心的な違い：")
        print("  古典：0 か 1（二者択一）")
        print("  量子：0でもあり1でもある（重ね合わせ）")

        print("\nブロッホ球：")
        print("  ・球面上の各点が一つの量子状態を表す")
        print("  ・|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩")
        print("  ・θ ∈ [0,π], φ ∈ [0,2π]")

        print("\n代表的な量子状態：")
        print("  ・|0⟩：北極")
        print("  ・|1⟩：南極")
        print("  ・|+⟩ = (|0⟩+|1⟩)/√2：赤道（X軸）")
        print("  ・|−⟩ = (|0⟩−|1⟩)/√2：赤道（−X軸）")
        print("  ・|i⟩ = (|0⟩+i|1⟩)/√2：赤道（Y軸）")

        print("\n禅との対応：")
        print("  古典ビット ≈ 二元対立（有/無）")
        print("  量子ビット ≈ 不二法門（有無を超える）")
        print("  重ね合わせ状態 ≈「非有非無」")

        print("\nアダマールゲートの哲学的意義：")
        print("  H|0⟩ = (|0⟩+|1⟩)/√2")
        print("  →「確定」を「重ね合わせ」に変える")
        print("  → 二元対立を打ち破る")
        print("  →「Aでもあり非Aでもある」状態に入る")
        print("="*70)

# Execute
simulator = QuantumBitSimulator()
simulator.visualize_quantum_states()

class HadamardGateSimulator:
    """
    Hadamard gate simulator
    Demonstrates: creating superposition states and breaking binary opposition
    """

    def __init__(self):
        self.H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

    def apply_hadamard(self, state):
        """Apply the Hadamard gate to a state vector"""
        return self.H @ state

    def visualize_hadamard_transformation(self):
        """
        Visualize the Hadamard gate transformation process
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        # === Initial state: |0⟩ (definite) ===
        ax = axes[0, 0]
        ax.bar(['|0⟩', '|1⟩'], [1, 0], color=['blue', 'red'], alpha=0.7,
              edgecolor='black', linewidth=2)
        ax.set_ylabel('振幅', fontsize=12)
        ax.set_title('初期状態：|0⟩\n完全に確定', fontsize=13, fontweight='bold')
        ax.set_ylim(-0.8, 1.2)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        # === Hadamard gate action ===
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
        ax.text(0.6, 0.6, '変換', ha='left', fontsize=12,
               color='purple', fontweight='bold')

        ax.set_title('アダマールゲート\n重ね合わせを生成', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, 'H|0⟩ = (|0⟩+|1⟩)/√2', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === Result: |+⟩ (superposition) ===
        ax = axes[0, 2]
        amplitudes = [1/np.sqrt(2), 1/np.sqrt(2)]
        ax.bar(['|0⟩', '|1⟩'], amplitudes, color=['blue', 'red'], alpha=0.7,
              edgecolor='black', linewidth=2)
        ax.set_ylabel('振幅', fontsize=12)
        ax.set_title('結果：|+⟩ = (|0⟩+|1⟩)/√2\n重ね合わせ状態',
                    fontsize=13, fontweight='bold')
        ax.set_ylim(-0.8, 1.2)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        for i, (label, amp) in enumerate(zip(['|0⟩', '|1⟩'], amplitudes)):
            ax.text(i, amp + 0.1, f'{amp:.3f}', ha='center', fontsize=10,
                   fontweight='bold')

        # === Zen analogy: attachment ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle = plt.Circle((0.5, 0.6), 0.15, color='blue', alpha=0.6,
                           edgecolor='black', linewidth=3)
        ax.add_patch(circle)
        ax.text(0.5, 0.6, '執着\n「有」', ha='center', va='center',
               fontsize=12, fontweight='bold', color='white')

        ax.text(0.5, 0.3, '二元対立：有 or 無', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue'))

        ax.set_title('初期：「有」への執着\n二元的思考', fontsize=13, fontweight='bold')

        # === Zen analogy: breaking attachment ===
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

        ax.set_title('棒喝・公案\n執着を打ち破る', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, '二元対立を超越する', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === Zen analogy: non-duality ===
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

        ax.text(0.5, 0.3, '有無を超えて\n非有非無', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen'))

        ax.set_title('結果：不二法門\n二元を超越', fontsize=13, fontweight='bold')

        fig.text(0.5, 0.98, 'アダマールゲート vs 禅の「破執」',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        plt.savefig('hadamard_gate_zen.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【アダマールゲート：重ね合わせを生成し、二元を打破する】")
        print("="*70)

        print("\nアダマールゲートの数学：")
        print("  H = (1/√2) × [1   1]")
        print("                [1  -1]")

        print("\n作用：")
        print("  H|0⟩ = (|0⟩ + |1⟩) / √2 = |+⟩")
        print("  H|1⟩ = (|0⟩ − |1⟩) / √2 = |−⟩")

        print("\n意義：")
        print("  ・確定状態 → 重ね合わせ状態")
        print("  ・「0か1か」→「0でもあり1でもある」")
        print("  ・二元対立の打破")

        print("\n量子コンピューティングでの役割：")
        print("  ・重ね合わせ状態の生成（量子並列性の基礎）")
        print("  ・量子アルゴリズムの第一歩")
        print("  ・例：グローバーのアルゴリズム、ショアのアルゴリズム")

        print("\n禅との対応：")
        print("  初期：「有」または「無」への執着")
        print("  → 二元対立的思考")

        print("\n  棒喝・公案：執着を破る")
        print("  → アダマールゲートが確定性を破るように")

        print("\n  結果：不二法門")
        print("  →「有無」の二元対立を超越する")
        print("  → 重ね合わせが「0/1」を超えるように")

        print("\n深い対応：")
        print("  アダマールゲート ≈ 禅の「破執」")
        print("  重ね合わせ状態 ≈ 不二法門")
        print("  測定による収縮 ≈ 起念による執着")

        print("\n六祖慧能：")
        print("  「善を思わず、悪を思わず、")
        print("   正にその時、汝の本来の面目は何ぞ」")
        print("  → 善悪の二元を超え、直接に本心を指す")
        print("  → 重ね合わせが0/1の二元を超えるように")
        print("="*70)

# Execute
hadamard_sim = HadamardGateSimulator()
hadamard_sim.visualize_hadamard_transformation()

class QuantumParallelismSimulator:
    """
    Quantum parallelism simulator
    Demonstrates: computing all possibilities simultaneously
    """

    def __init__(self):
        pass

    def visualize_quantum_parallelism(self):
        """
        Visualize quantum parallelism vs classical sequential computation
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left panel: classical sequential computation ===
        n_bits = 3
        n_states = 2 ** n_bits

        # Classical: must compute one by one
        for i in range(n_states):
            binary = format(i, f'0{n_bits}b')
            y = n_states - i - 1

            # Input
            rect_input = plt.Rectangle((0.1, y*0.12), 0.15, 0.1,
                                      facecolor='lightblue', alpha=0.7,
                                      edgecolor='blue', linewidth=1.5)
            ax1.add_patch(rect_input)
            ax1.text(0.175, y*0.12 + 0.05, binary, ha='center', va='center',
                    fontsize=9)

            # Function f
            rect_f = plt.Rectangle((0.4, y*0.12), 0.15, 0.1,
                                  facecolor='yellow', alpha=0.7,
                                  edgecolor='orange', linewidth=1.5)
            ax1.add_patch(rect_f)
            ax1.text(0.475, y*0.12 + 0.05, 'f(x)', ha='center', va='center',
                    fontsize=9, fontweight='bold')

            # Arrows
            ax1.annotate('', xy=(0.4, y*0.12 + 0.05), xytext=(0.25, y*0.12 + 0.05),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
            ax1.annotate('', xy=(0.7, y*0.12 + 0.05), xytext=(0.55, y*0.12 + 0.05),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

            # Output
            output_value = (i * 2) % n_states  # Example function
            rect_output = plt.Rectangle((0.7, y*0.12), 0.15, 0.1,
                                       facecolor='lightgreen', alpha=0.7,
                                       edgecolor='green', linewidth=1.5)
            ax1.add_patch(rect_output)
            ax1.text(0.775, y*0.12 + 0.05, f'{output_value}', ha='center', va='center',
                    fontsize=9)

        ax1.set_xlim(0, 1)
        ax1.set_ylim(-0.1, 1.1)
        ax1.axis('off')
        ax1.set_title(f'古典計算：逐次処理\n{n_states}回の演算',
                     fontsize=14, fontweight='bold')

        ax1.text(0.5, -0.05, f'時間計算量：O({n_states})',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Right panel: quantum parallel computation ===

        # Initial state
        rect_init = plt.Rectangle((0.1, 0.4), 0.15, 0.2,
                                 facecolor='lightblue', alpha=0.7,
                                 edgecolor='blue', linewidth=2)
        ax2.add_patch(rect_init)
        ax2.text(0.175, 0.5, '|0...0⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # Hadamard gate
        rect_h = plt.Rectangle((0.35, 0.4), 0.15, 0.2,
                              facecolor='yellow', alpha=0.7,
                              edgecolor='orange', linewidth=2)
        ax2.add_patch(rect_h)
        ax2.text(0.425, 0.5, 'H⊗n', ha='center', va='center',
                fontsize=11, fontweight='bold')

        ax2.annotate('', xy=(0.35, 0.5), xytext=(0.25, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=3, color='purple'))

        # Superposition state
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

        # Function U_f
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
        ax2.set_title(f'量子計算：並列処理\nたった1回の演算！',
                     fontsize=14, fontweight='bold')

        ax2.text(0.5, -0.05, '時間計算量：O(1)',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
                transform=ax2.transAxes)

        fig.text(0.5, 0.98, f'量子並列性：{n_states}個の状態を同時に計算',
                ha='center', fontsize=16, fontweight='bold')

        explanation = '''
        古典計算：f(x)を一つずつ計算、2^n回必要
        量子計算：重ね合わせ状態Σ|x⟩を作り、一度にすべてのf(x)を計算

        禅との対応：
        古典：一念一法（逐次的）
        量子：一念万法（並列的）
        禅：「一心万法」──一念に万法を頓現する
        '''

        fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        plt.tight_layout()
        plt.subplots_adjust(top=0.9, bottom=0.15)
        plt.savefig('quantum_parallelism.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【量子並列性：すべての可能性を一度に計算する】")
        print("="*70)

        print(f"\n問題：関数 f(x) をすべての x ∈ {{0,1}}^{n_bits} について計算する")
        print(f"合計 {n_states} 個の可能なx")

        print("\n古典計算：")
        print(f"  ・f(0), f(1), ..., f({n_states-1}) を一つずつ計算")
        print(f"  ・{n_states} 回の演算が必要")
        print(f"  ・時間計算量：O(2^n)")

        print("\n量子計算：")
        print("  1. 重ね合わせ状態を生成：H⊗n|0⟩^n = Σ|x⟩")
        print("  2. 関数を適用：U_f Σ|x⟩ = Σ|x⟩|f(x)⟩")
        print("  3. 1回の演算ですべての結果を得る！")
        print("  ・時間計算量：O(1)")

        print("\nコア技術：")
        print("  ・重ね合わせ：すべての可能性を同時に表現")
        print("  ・量子ゲート：すべての状態に一度に作用")
        print("  ・量子干渉：正解を増幅")

        print("\n落とし穴：")
        print("  ・測定すると収縮し、結果は一つだけ")
        print("  ・量子干渉を使って情報を「抽出」する必要がある")

        print("\n禅との対応：")
        print("  古典的思考：")
        print("    一念一法（逐次的）")
        print("    一つずつ考え、一つずつ解決")

        print("\n  量子／禅：")
        print("    一念万法（並列的）")
        print("    一念に頓現し、万法が具足する")

        print("\n華厳宗「一心万法」：")
        print("  ・一つの心念が万法を含む")
        print("  ・一つずつ生じるのではない")
        print("  ・同時に具足している")

        print("\n量子並列性 ≈ 一心万法：")
        print("  ・一つの重ね合わせがすべての可能性を含む")
        print("  ・一回の演算がすべての可能性に作用する")
        print("  ・線形時間を超越する")

        print("\n深い洞察：")
        print("  線形思考：A → B → C（逐次的）")
        print("  量子／禅：A+B+C 同時（並列的）")
        print("  → 時間の順序性を超越する")
        print("="*70)

# Execute
parallelism_sim = QuantumParallelismSimulator()
parallelism_sim.visualize_quantum_parallelism()

def visualize_measurement_thought():
    """
    Visualize the correspondence between measurement collapse
    and the Zen concept of arising thought (kinen)
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Quantum: before measurement (superposition) ===
    ax = axes[0, 0]

    states = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    amplitudes = [0.5, 0.5, 0.5, 0.5]

    ax.bar(states, amplitudes, color='purple', alpha=0.6,
          edgecolor='black', linewidth=2)
    ax.set_ylabel('振幅', fontsize=12)
    ax.set_title('量子：測定前（重ね合わせ状態）\nすべての可能性が共存',
                fontsize=13, fontweight='bold')
    ax.set_ylim(0, 0.8)
    ax.grid(True, alpha=0.3, axis='y')

    ax.text(0.5, 0.7, '|ψ⟩ = Σ|x⟩', transform=ax.transAxes,
           ha='center', fontsize=11, fontweight='bold', color='purple')

    # === Quantum: measurement (collapse) ===
    ax = axes[0, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, '測定\n収縮', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, '|10⟩', ha='center', fontsize=16,
           fontweight='bold', color='green',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('測定：収縮\n重ね合わせ→確定状態', fontsize=13, fontweight='bold')

    # === Zen: no-thought (non-duality) ===
    ax = axes[1, 0]

    thoughts = ['喜', '怒', '哀', '楽', '愛', '憎', '欲']
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
    ax.set_title('禅：無念（不二）\n二元対立を超えて', fontsize=13, fontweight='bold')

    # === Zen: arising thought (attachment) ===
    ax = axes[1, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, '起念\n執着', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, '愛', ha='center', fontsize=20,
           fontweight='bold', color='red',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('起念：執着\n無念→有念', fontsize=13, fontweight='bold')

    fig.text(0.5, 0.98, '測定の収縮 vs 起念と執着',
            ha='center', fontsize=16, fontweight='bold')

    comparison = '''
    量子測定：                      禅の起念：
    ・測定前：重ね合わせ状態        ・無念：不二、対立を超えて
    ・すべての可能性が共存          ・心はいかなる念にも留まらず
    ・測定：収縮                    ・起念：執着
    ・一つの結果を選択              ・一つの念に執着する
    ・重ね合わせを失う              ・二元対立に陥る

    共通点：
    観察／起念 →「二元を超えた状態」から「二元対立」に陥る
    重ね合わせ／無念 → 確定状態／有念
    '''

    fig.text(0.5, 0.02, comparison, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.18)
    plt.savefig('measurement_collapse_thought.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【測定の収縮 vs 禅の「起念」】")
    print("="*70)

    print("\n量子測定：")
    print("  測定前：|ψ⟩ = Σα_i|i⟩（重ね合わせ状態）")
    print("  → すべての可能性が共存")
    print("  →「0か1か」の二元を超えている")

    print("\n  測定時：波動関数の収縮")
    print("  → ランダムに一つの結果|i⟩を選択")
    print("  → 確率 = |α_i|²")

    print("\n  測定後：確定状態|i⟩")
    print("  → 重ね合わせを失う")
    print("  →「0か1か」の二元に戻る")

    print("\n禅の「起念」：")
    print("  無念：心はいかなる念にも留まらない")
    print("  → 喜怒哀楽の対立を超えている")
    print("  →「有無」の二元を超えている")
    print("  → 不二法門")

    print("\n  起念：一つの念への執着")
    print("  → 例えば：「愛」への執着")
    print("  →「愛/憎」の対立が生じる")

    print("\n  有念：二元対立に陥る")
    print("  → 喜/怒、善/悪、正/誤")
    print("  →「不二」を失う")

    print("\n対応：")
    print("  重ね合わせ状態 ≈ 無念")
    print("  測定 ≈ 起念")
    print("  収縮 ≈ 執着")
    print("  確定状態 ≈ 有念")

    print("\n六祖慧能：")
    print("  「何ぞ期せん、自性はもとより清浄なり」")
    print("  → 本来の面目は「無念」（清浄）")

    print("\n  「念念不住」")
    print("  → いかなる念にも留まらない")
    print("  →「無念」の状態を保つ")
    print("  → 重ね合わせが収縮しないよう保つことに通じる")

    print("\n深い対応：")
    print("  ・測定は重ね合わせを破壊する")
    print("    → 起念は無念を破壊する")
    print("  ・重ね合わせは「潜在的」")
    print("    → 無念は「超越的」")
    print("  ・収縮は「選択」")
    print("    → 執着は「固定化」")

    print("\n問い：")
    print("  ・重ね合わせを収縮させずに保つには？")
    print("    → 量子誤り訂正、デコヒーレンス時間")
    print("  ・無念を起念なしに保つには？")
    print("    → 坐禅、只管打坐（しかんたざ）")

    print("\n究極の洞察：")
    print("  量子コンピューティングの威力は「重ね合わせを保つ」ことから来る")
    print("  禅の智慧は「無念を保つ」ことから来る")
    print("  どちらも二元対立の超越である")
    print("="*70)

# Execute
visualize_measurement_thought()
