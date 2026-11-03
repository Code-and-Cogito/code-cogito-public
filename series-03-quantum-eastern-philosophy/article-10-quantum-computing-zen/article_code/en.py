# Code & Cogito: Quantum Computing vs Zen — Beyond Binary Logic
# Article: https://code-cogito.com/en/quantum-computing-vs-zen-beyond-binary-logic-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
# | H = (1/√2) × [1   1]
# |               [1  -1]

# | X = [0  1]
# |     [1  0]

# | Z = [1   0]
# |     [0  -1]

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class QuantumBitSimulator:
    """
    Qubit simulator
    Demonstrates: superposition states and the Bloch sphere
    """

    def __init__(self):
        pass

    def bloch_sphere(self, ax, state_vector, label):
        """
        Draw the Bloch sphere and plot a quantum state on it
        """
        # Sphere surface
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

# |     def visualize_quantum_states(self):
# |         """
# |         Visualize different quantum states on the Bloch sphere
# |         """
# |         fig = plt.figure(figsize=(18, 12))
# | 
# |         # === |0⟩ state ===
# |         ax1 = fig.add_subplot(2, 3, 1, projection='3d')
# |         self.bloch_sphere(ax1, [1, 0], '|0⟩ State\n(North Pole)')
# | 
# |         # === |1⟩ state ===
# |         ax2 = fig.add_subplot(2, 3, 2, projection='3d')
# |         self.bloch_sphere(ax2, [0, 1], '|1⟩ State\n(South Pole)')
# | 
# |         # === |+⟩ state (superposition) ===
# |         ax3 = fig.add_subplot(2, 3, 3, projection='3d')
# |         self.bloch_sphere(ax3, [1/np.sqrt(2), 1/np.sqrt(2)],
# |                          '|+⟩ = (|0⟩+|1⟩)/√2\n(Equator)')
# | 
# |         # === |-⟩ state (superposition) ===
# |         ax4 = fig.add_subplot(2, 3, 4, projection='3d')
# |         self.bloch_sphere(ax4, [1/np.sqrt(2), -1/np.sqrt(2)],
# |                          '|−⟩ = (|0⟩−|1⟩)/√2\n(Equator)')
# | 
# |         # === Arbitrary superposition ===
# |         ax5 = fig.add_subplot(2, 3, 5, projection='3d')
# |         alpha = np.cos(np.pi/6)
# |         beta = np.sin(np.pi/6) * np.exp(1j * np.pi/4)
# |         self.bloch_sphere(ax5, [alpha, beta],
# |                          'Arbitrary Superposition\n(Any Point on Sphere)')
# | 
# |         # === Comparison panel ===
# |         ax6 = fig.add_subplot(2, 3, 6)
# |         ax6.axis('off')
# | 
# |         text = '''
# |         [Qubit vs Classical Bit]
# | 
# |         Classical Bit:
# |         • Only two states: 0 or 1
# |         • Black or white
# |         • Binary logic
# | 
# |         Qubit:
# |         • Superposition: α|0⟩ + β|1⟩
# |         • |α|² + |β|² = 1
# |         • Both 0 and 1
# |         • Beyond binary
# | 
# |         Bloch Sphere:
# |         • Each surface point = one quantum state
# |         • North pole = |0⟩
# |         • South pole = |1⟩
# |         • Equator = superposition states
# |         • No pure states inside the sphere
# | 
# |         Zen Analogy:
# |         • Classical: being OR non-being
# |         • Quantum: both (superposition)
# |         • Zen: beyond both (non-duality)
# | 
# |         Hadamard Gate:
# |         H|0⟩ = (|0⟩+|1⟩)/√2
# |         → From north pole to equator
# |         → Creating superposition
# |         → Shattering binary opposition
# |         '''
# | 
# |         ax6.text(0.1, 0.5, text, fontsize=10, va='center',
# |                 family='monospace',
# |                 bbox=dict(boxstyle='round', facecolor='lightyellow',
# |                          alpha=0.9, edgecolor='black', linewidth=2))
# | 
# |         plt.tight_layout()
# |         plt.savefig('quantum_bit_bloch_sphere.png', dpi=300, bbox_inches='tight')
# |         plt.show()

        print("\n" + "="*70)
        print("[QUBITS: BEYOND 0 AND 1]")
        print("="*70)

        print("\nClassical Bit:")
        print("  • Only two states: 0 or 1")
        print("  • Boolean logic: AND, OR, NOT")
        print("  • Either/or — no middle ground")

        print("\nQubit:")
        print("  • Superposition: |ψ⟩ = α|0⟩ + β|1⟩")
        print("  • α, β are complex numbers")
        print("  • |α|² + |β|² = 1")
        print("  • |α|² = probability of measuring |0⟩")
        print("  • |β|² = probability of measuring |1⟩")

        print("\nKey Distinction:")
        print("  Classical: 0 or 1 (pick one)")
        print("  Quantum: both 0 and 1 (superposition)")

        print("\nBloch Sphere:")
        print("  • Every point on the surface = one quantum state")
        print("  • |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩")
        print("  • θ ∈ [0,π], φ ∈ [0,2π]")

        print("\nCommon Quantum States:")
        print("  • |0⟩: north pole")
        print("  • |1⟩: south pole")
        print("  • |+⟩ = (|0⟩+|1⟩)/√2: equator (X axis)")
        print("  • |−⟩ = (|0⟩−|1⟩)/√2: equator (−X axis)")
        print("  • |i⟩ = (|0⟩+i|1⟩)/√2: equator (Y axis)")

        print("\nZen Analogy:")
        print("  Classical bit ≈ binary opposition (being/non-being)")
        print("  Qubit ≈ non-duality (beyond being and non-being)")
        print("  Superposition ≈ 'neither being nor non-being'")

        print("\nPhilosophical Significance of the Hadamard Gate:")
        print("  H|0⟩ = (|0⟩+|1⟩)/√2")
        print("  → Transforms 'certainty' into 'superposition'")
        print("  → Shatters binary opposition")
        print("  → Enters the state of 'both A and not-A'")
        print("="*70)

# Run
simulator = QuantumBitSimulator()
simulator.visualize_quantum_states()

class HadamardGateSimulator:
    """
    Hadamard gate simulator
    Demonstrates: how to create superposition and shatter binary opposition
    """

    def __init__(self):
        self.H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

    def apply_hadamard(self, state):
        """Apply the Hadamard gate"""
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
        ax.set_ylabel('Amplitude', fontsize=12)
        ax.set_title('Initial: |0⟩\nFully Definite', fontsize=13, fontweight='bold')
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
        ax.text(0.6, 0.6, 'Transform', ha='left', fontsize=12,
               color='purple', fontweight='bold')

        ax.set_title('Hadamard Gate\nCreates Superposition', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, 'H|0⟩ = (|0⟩+|1⟩)/√2', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === Result: |+⟩ (superposition) ===
        ax = axes[0, 2]
        amplitudes = [1/np.sqrt(2), 1/np.sqrt(2)]
        ax.bar(['|0⟩', '|1⟩'], amplitudes, color=['blue', 'red'], alpha=0.7,
              edgecolor='black', linewidth=2)
        ax.set_ylabel('Amplitude', fontsize=12)
        ax.set_title('Result: |+⟩ = (|0⟩+|1⟩)/√2\nSuperposition',
                    fontsize=13, fontweight='bold')
        ax.set_ylim(-0.8, 1.2)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        for i, (label, amp) in enumerate(zip(['|0⟩', '|1⟩'], amplitudes)):
            ax.text(i, amp + 0.1, f'{amp:.3f}', ha='center', fontsize=10,
                   fontweight='bold')

        # === Zen analogy: Attachment ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle = plt.Circle((0.5, 0.6), 0.15, color='blue', alpha=0.6,
                           edgecolor='black', linewidth=3)
        ax.add_patch(circle)
        ax.text(0.5, 0.6, 'Attached\nto "Being"', ha='center', va='center',
               fontsize=12, fontweight='bold', color='white')

        ax.text(0.5, 0.3, 'Dualism: being OR non-being', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue'))

        ax.set_title('Initial: Attached to "Being"\nDualistic Thinking', fontsize=13, fontweight='bold')

        # === Zen analogy: Shattering ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ax.text(0.5, 0.5, 'KATSU!', ha='center', va='center',
               fontsize=36, fontweight='bold', color='red')

        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            x = 0.5 + 0.3 * np.cos(angle)
            y = 0.5 + 0.3 * np.sin(angle)
            ax.plot([0.5, x], [0.5, y], 'yellow', linewidth=3, alpha=0.7)

        ax.set_title('The Zen Shout / Koan\nShattering Attachment', fontsize=13, fontweight='bold')

        ax.text(0.5, 0.15, 'Breaking binary opposition', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow'))

        # === Zen analogy: Non-duality ===
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

        ax.text(0.5, 0.5, 'Non-dual', ha='center', va='center',
               fontsize=14, fontweight='bold', color='purple')

        ax.text(0.5, 0.3, 'Beyond being/non-being\nNeither this nor that', ha='center',
               fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen'))

        ax.set_title('Result: Non-Duality\nBeyond Binary', fontsize=13, fontweight='bold')

        fig.text(0.5, 0.98, 'Hadamard Gate vs Zen "Shattering Attachment"',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        plt.savefig('hadamard_gate_zen.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[HADAMARD GATE: CREATING SUPERPOSITION, SHATTERING DUALITY]")
        print("="*70)

        print("\nThe Mathematics of the Hadamard Gate:")
        print("  H = (1/√2) × [1   1]")
        print("                [1  -1]")

        print("\nAction:")
        print("  H|0⟩ = (|0⟩ + |1⟩) / √2 = |+⟩")
        print("  H|1⟩ = (|0⟩ − |1⟩) / √2 = |−⟩")

        print("\nSignificance:")
        print("  • Definite state → superposition")
        print("  • From '0 or 1' → 'both 0 and 1'")
        print("  • Shatters binary opposition")

        print("\nRole in Quantum Computing:")
        print("  • Creates superposition (the basis of quantum parallelism)")
        print("  • The first step in quantum algorithms")
        print("  • Used in: Grover's algorithm, Shor's algorithm")

        print("\nZen Analogy:")
        print("  Initial: attached to 'being' or 'non-being'")
        print("  → Dualistic thinking")

        print("\n  The Zen shout / koan: shattering attachment")
        print("  → Like the Hadamard gate shattering certainty")

        print("\n  Result: non-duality")
        print("  → Transcending the being/non-being binary")
        print("  → Like superposition transcending 0/1")

        print("\nDeep Analogy:")
        print("  Hadamard gate ≈ Zen 'shattering attachment'")
        print("  Superposition ≈ non-duality")
        print("  Measurement collapse ≈ arising of conceptual thought")

        print("\nHuineng, the Sixth Patriarch of Zen:")
        print("  'Think neither of good nor evil;")
        print("   at this very moment,")
        print("   what is your original face?'")
        print("  → Transcend the good/evil binary, point to the true self")
        print("  → Like superposition transcends the 0/1 binary")
        print("="*70)

# Run
hadamard_sim = HadamardGateSimulator()
hadamard_sim.visualize_hadamard_transformation()

class QuantumParallelismSimulator:
    """
    Quantum parallelism simulator
    Demonstrates: how to compute all possibilities simultaneously
    """

    def __init__(self):
        pass

    def visualize_quantum_parallelism(self):
        """
        Visualize quantum parallelism
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left panel: Classical sequential computation ===
        n_bits = 3
        n_states = 2 ** n_bits

        # Classical: must process one at a time
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
        ax1.set_title(f'Classical Computing: Sequential\n{n_states} Operations Required',
                     fontsize=14, fontweight='bold')

        ax1.text(0.5, -0.05, f'Time complexity: O({n_states})',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Right panel: Quantum parallel computation ===

        # Initial state
        rect_init = plt.Rectangle((0.1, 0.4), 0.15, 0.2,
                                 facecolor='lightblue', alpha=0.7,
                                 edgecolor='blue', linewidth=2)
        ax2.add_patch(rect_init)
        ax2.text(0.175, 0.5, '|0...0⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # Hadamard gates
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
        ax2.set_title(f'Quantum Computing: Parallel\n1 Operation!',
                     fontsize=14, fontweight='bold')

        ax2.text(0.5, -0.05, 'Time complexity: O(1)',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
                transform=ax2.transAxes)

        fig.text(0.5, 0.98, f'Quantum Parallelism: {n_states} States Computed Simultaneously',
                ha='center', fontsize=16, fontweight='bold')

        explanation = '''
        Classical: compute f(x) one at a time — requires 2^n operations
        Quantum: create superposition Σ|x⟩, compute all f(x) in one shot

        Zen analogy:
        Classical: one thought, one phenomenon (sequential)
        Quantum: one thought, all phenomena (simultaneous)
        Zen: "One mind, ten thousand dharmas" — all at once
        '''

        fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        plt.tight_layout()
        plt.subplots_adjust(top=0.9, bottom=0.15)
        plt.savefig('quantum_parallelism.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[QUANTUM PARALLELISM: COMPUTING ALL POSSIBILITIES AT ONCE]")
        print("="*70)

        print(f"\nProblem: compute f(x) for all x ∈ {{0,1}}^{n_bits}")
        print(f"Total possible inputs: {n_states}")

        print("\nClassical Computing:")
        print(f"  • Compute f(0), f(1), ..., f({n_states-1}) one by one")
        print(f"  • Requires {n_states} operations")
        print(f"  • Time complexity: O(2^n)")

        print("\nQuantum Computing:")
        print("  1. Create superposition: H⊗n|0⟩^n = Σ|x⟩")
        print("  2. Apply function: U_f Σ|x⟩ = Σ|x⟩|f(x)⟩")
        print("  3. All results computed in one operation!")
        print("  • Time complexity: O(1)")

        print("\nKey Techniques:")
        print("  • Superposition: represents all possibilities simultaneously")
        print("  • Quantum gates: act on all states at once")
        print("  • Quantum interference: amplifies correct answers")

        print("\nThe Catch:")
        print("  • Measurement causes collapse — you only get one result")
        print("  • Quantum interference needed to 'extract' information")

        print("\nZen Analogy:")
        print("  Classical thinking:")
        print("    One thought → one phenomenon (sequential)")
        print("    Think step by step, solve step by step")

        print("\n  Quantum / Zen:")
        print("    One thought → all phenomena (parallel)")
        print("    One moment of awakening — everything present at once")

        print("\nHuayan Buddhism's 'One Mind, Ten Thousand Dharmas':")
        print("  • A single moment of mind contains all phenomena")
        print("  • Not arising one by one")
        print("  • But all present simultaneously")

        print("\nQuantum parallelism ≈ One mind, ten thousand dharmas:")
        print("  • One superposition contains all possibilities")
        print("  • One operation acts on all possibilities")
        print("  • Transcends linear time")

        print("\nDeep Insight:")
        print("  Linear thinking: A → B → C (sequential)")
        print("  Quantum / Zen: A+B+C simultaneously (parallel)")
        print("  → Transcending the sequentiality of time")
        print("="*70)

# Run
parallelism_sim = QuantumParallelismSimulator()
parallelism_sim.visualize_quantum_parallelism()

def visualize_measurement_and_thought():
    """
    Visualize the correspondence between measurement collapse
    and the Zen concept of 'arising of thought'
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Quantum: before measurement (superposition) ===
    ax = axes[0, 0]

    states = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    amplitudes = [0.5, 0.5, 0.5, 0.5]

    ax.bar(states, amplitudes, color='purple', alpha=0.6,
          edgecolor='black', linewidth=2)
    ax.set_ylabel('Amplitude', fontsize=12)
    ax.set_title('Quantum: Before Measurement (Superposition)\nAll Possibilities Coexist',
                fontsize=13, fontweight='bold')
    ax.set_ylim(0, 0.8)
    ax.grid(True, alpha=0.3, axis='y')

    ax.text(0.5, 0.7, '|ψ⟩ = Σ|x⟩', transform=ax.transAxes,
           ha='center', fontsize=11, fontweight='bold', color='purple')

    # === Quantum: measurement (collapse) ===
    ax = axes[0, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, 'Measurement\nCollapse', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, '|10⟩', ha='center', fontsize=16,
           fontweight='bold', color='green',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Measurement: Collapse\nSuperposition → Definite State', fontsize=13, fontweight='bold')

    # === Zen: no-thought (non-duality) ===
    ax = axes[1, 0]

    thoughts = ['Joy', 'Anger', 'Sorrow', 'Delight', 'Love', 'Hate', 'Desire']
    np.random.seed(42)
    for thought in thoughts:
        x, y = np.random.random(2)
        ax.text(x, y, thought, fontsize=14, alpha=0.3,
               color=np.random.choice(['blue', 'red', 'green', 'purple']))

    circle = plt.Circle((0.5, 0.5), 0.15, color='gold', alpha=0.5,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'No-thought\nNon-dual', ha='center', va='center',
           fontsize=12, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Zen: No-Thought (Non-Duality)\nBeyond Binary Opposition', fontsize=13, fontweight='bold')

    # === Zen: arising of thought (attachment) ===
    ax = axes[1, 1]

    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.7),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax.text(0.6, 0.5, 'Thought\nArises', ha='left', fontsize=14,
           color='red', fontweight='bold')

    ax.text(0.5, 0.2, 'LOVE', ha='center', fontsize=20,
           fontweight='bold', color='red',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Arising of Thought: Attachment\nNo-Thought → Fixed Thought', fontsize=13, fontweight='bold')

    fig.text(0.5, 0.98, 'Measurement Collapse vs Arising of Thought',
            ha='center', fontsize=16, fontweight='bold')

    comparison = '''
    Quantum Measurement:                  Zen "Arising of Thought":
    • Before: superposition               • No-thought: non-dual, beyond opposites
    • All possibilities coexist           • Mind does not cling to any thought
    • Measurement: collapse               • Thought arises: attachment
    • One result selected                 • One thought grasped
    • Superposition lost                  • Falls into binary opposition

    Common ground:
    Observation / thought-arising → from "beyond duality" to "trapped in duality"
    Superposition / no-thought → definite state / fixed thought
    '''

    fig.text(0.5, 0.02, comparison, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.18)
    plt.savefig('measurement_collapse_thought.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[MEASUREMENT COLLAPSE vs ZEN 'ARISING OF THOUGHT']")
    print("="*70)

    print("\nQuantum Measurement:")
    print("  Before measurement: |ψ⟩ = Σα_i|i⟩ (superposition)")
    print("  → All possibilities coexist")
    print("  → Beyond the '0 or 1' binary")

    print("\n  During measurement: wave function collapse")
    print("  → Randomly selects one result |i⟩")
    print("  → Probability = |α_i|²")

    print("\n  After measurement: definite state |i⟩")
    print("  → Superposition lost")
    print("  → Back to the '0 or 1' binary")

    print("\nZen 'Arising of Thought':")
    print("  No-thought: the mind does not cling to any thought")
    print("  → Beyond the opposition of joy/sorrow, love/hate")
    print("  → Beyond the 'being/non-being' binary")
    print("  → Non-duality")

    print("\n  Thought arises: attachment to one thought")
    print("  → For example: attachment to 'love'")
    print("  → Immediately creates the 'love/hate' opposition")

    print("\n  Fixed thought: trapped in binary opposition")
    print("  → Joy/sorrow, good/bad, right/wrong")
    print("  → Non-duality lost")

    print("\nCorrespondence:")
    print("  Superposition ≈ no-thought")
    print("  Measurement ≈ arising of thought")
    print("  Collapse ≈ attachment")
    print("  Definite state ≈ fixed thought")

    print("\nHuineng, the Sixth Patriarch of Zen:")
    print("  'The original nature of the self is fundamentally pure.'")
    print("  → The original face is 'no-thought' (pure awareness)")

    print("\n  'Thought after thought, do not abide.'")
    print("  → Do not cling to any thought")
    print("  → Maintain the 'no-thought' state")
    print("  → Like maintaining superposition without collapse")

    print("\nDeep Analogy:")
    print("  • Measurement destroys superposition")
    print("    → Arising of thought destroys no-thought")
    print("  • Superposition is 'potential'")
    print("    → No-thought is 'transcendent'")
    print("  • Collapse is 'selection'")
    print("    → Attachment is 'fixation'")

    print("\nThe Question:")
    print("  • How to maintain superposition without collapse?")
    print("    → Quantum error correction, decoherence time")
    print("  • How to maintain no-thought without arising?")
    print("    → Meditation, mindful awareness")

    print("\nUltimate Insight:")
    print("  Quantum computing's power comes from 'maintaining superposition'")
    print("  Zen's wisdom comes from 'maintaining no-thought'")
    print("  Both are about transcending binary opposition")
    print("="*70)

# Run
visualize_measurement_and_thought()
