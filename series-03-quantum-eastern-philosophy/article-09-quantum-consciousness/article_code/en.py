# Code & Cogito: Quantum Consciousness vs Eastern Philosophy of Mind -- Is the Mind a Quantum Process?
# Article: https://code-cogito.com/en/quantum-consciousness-eastern-philosophy-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class QuantumConsciousnessSimulator:
    """
    Quantum Consciousness Simulator
    Demonstrates how measurement/observation affects a quantum system
    """

    def __init__(self):
        pass

    def visualize_measurement_consciousness(self):
        """
        Visualize the relationship between measurement and consciousness
        """
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Before measurement (superposition) ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')

        # Generate Bloch sphere representation of superposition
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax1.plot_surface(x, y, z, alpha=0.3, color='cyan')

        # Superposition state vector
        theta, phi = np.pi/4, np.pi/4
        sx = np.sin(theta) * np.cos(phi)
        sy = np.sin(theta) * np.sin(phi)
        sz = np.cos(theta)

        ax1.quiver(0, 0, 0, sx, sy, sz, color='purple',
                  arrow_length_ratio=0.1, linewidth=3)

        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('Before Measurement: Superposition\n|psi> = alpha|0> + beta|1>',
                     fontsize=13, fontweight='bold')

        # === Panel 2: During measurement (observer intervention) ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # Eye (observer)
        eye = plt.Circle((0.5, 0.7), 0.15, color='blue', alpha=0.6,
                        edgecolor='darkblue', linewidth=3)
        ax2.add_patch(eye)
        ax2.text(0.5, 0.7, '👁', ha='center', va='center', fontsize=40)

        # Arrow pointing down
        ax2.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=5, color='red'))
        ax2.text(0.6, 0.475, 'Observation\nMeasurement', ha='left', fontsize=12,
                color='red', fontweight='bold')

        # Quantum system
        rect = plt.Rectangle((0.35, 0.25), 0.3, 0.15,
                            facecolor='purple', alpha=0.5,
                            edgecolor='purple', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(0.5, 0.325, 'Quantum\nSystem', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        ax2.set_title('During Measurement: Observer Intervenes\nWave function about to collapse',
                     fontsize=13, fontweight='bold')

        # === Panel 3: After measurement (collapse) ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')

        # Bloch sphere
        ax3.plot_surface(x, y, z, alpha=0.3, color='lightblue')

        # Collapsed to |0> (north pole)
        ax3.quiver(0, 0, 0, 0, 0, 1, color='red',
                  arrow_length_ratio=0.1, linewidth=3)

        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('Z')
        ax3.set_title('After Measurement: Collapse\n|psi> -> |0>',
                     fontsize=13, fontweight='bold')

        # === Panel 4: Classical view ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        text_classical = '''
        Classical View (Materialism):

        * Matter exists independently of observers
        * Observation merely "discovers"
        * Consciousness is an epiphenomenon
        * The brain is a classical computer

        Problem:
        -> Cannot explain the measurement problem
        -> Cannot explain the unity of consciousness
        '''

        ax4.text(0.1, 0.5, text_classical, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # === Panel 5: Quantum consciousness view ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')

        text_quantum = '''
        Quantum Consciousness (Orch OR):

        * Consciousness is a quantum process
        * It occurs in microtubules
        * Consciousness causes wave function collapse
        * Each collapse = a moment of awareness

        Strengths:
        -> Explains the unity of consciousness
        -> Explains non-computability
        -> Links quantum mechanics to consciousness
        '''

        ax5.text(0.1, 0.5, text_quantum, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.8))

        # === Panel 6: Eastern philosophy of mind ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text_eastern = '''
        Eastern Philosophy of Mind / Zen:

        * Mind is the ground of all phenomena
        * Apart from mind, things cannot be discussed
        * Mind is not identical with the brain
        * Mind has ontological primacy

        Wang Yangming:
        "Outside the mind, there are no things"

        Zen:
        "Directly pointing to the mind,
         seeing one's nature"

        Common ground:
        -> Mind/consciousness has ontological status
        -> Observation participates in creating reality
        '''

        ax6.text(0.1, 0.5, text_eastern, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # Main title
        fig.text(0.5, 0.98, 'Quantum Measurement and Consciousness: Three Perspectives',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        plt.savefig('quantum_measurement_consciousness.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("QUANTUM MEASUREMENT AND CONSCIOUSNESS")
        print("="*70)

        print("\nThe Measurement Problem:")
        print("  * Before measurement: system in superposition")
        print("  * During measurement: wave function collapses")
        print("  * After measurement: system in definite state")
        print("  * The question: what causes collapse?")

        print("\nThree Answers:")
        print("\n1. Copenhagen Interpretation (standard):")
        print("   -> The measuring apparatus causes collapse")
        print("   -> But the apparatus is also a quantum system")
        print("   -> Infinite regress problem")

        print("\n2. Many-Worlds Interpretation:")
        print("   -> No collapse; the universe branches")
        print("   -> Consciousness plays no special role")

        print("\n3. Von Neumann / Orch OR:")
        print("   -> Consciousness causes collapse")
        print("   -> Consciousness has a privileged status")

        print("\nCorresponding Eastern Views:")
        print("  Wang Yangming: 'Outside the mind, there are no things'")
        print("  -> Apart from mind, things cannot be defined")

        print("\n  Zen: 'Seeing one's true nature'")
        print("  -> Direct realization of the mind's essence")

        print("\nCommon Ground:")
        print("  * Observer/mind plays a central role")
        print("  * 'Objective reality' depends on the subject")
        print("  * Mind/consciousness is not a byproduct")

        print("\nKey Questions:")
        print("  * Does consciousness truly cause collapse?")
        print("  * If so, what is the mechanism?")
        print("  * Is Orch OR correct?")
        print("  * Or do we need entirely new physics?")
        print("="*70)

# Run
simulator = QuantumConsciousnessSimulator()
simulator.visualize_measurement_consciousness()

class OrchORSimulator:
    """
    Orch OR Theory Simulation
    Demonstrates how microtubules might give rise to consciousness
    """

    def __init__(self):
        self.hbar = 1.054571817e-34  # Reduced Planck constant (J*s)
        self.c = 299792458  # Speed of light (m/s)

    def calculate_collapse_time(self, delta_mass):
        """
        Calculate objective collapse time
        tau = hbar / (Delta_M * c^2)
        """
        delta_energy = delta_mass * self.c**2
        tau = self.hbar / delta_energy
        return tau

    def visualize_orch_or(self):
        """
        Visualize Orch OR theory
        """
        fig = plt.figure(figsize=(18, 10))

        # === Panel 1: Microtubule structure ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.axis('off')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        # Microtubule (cylindrical structure)
        from matplotlib.patches import Rectangle, Circle

        # Draw simplified microtubule
        for i in range(5):
            y = 0.2 + i * 0.15
            # Tubulin proteins
            circle1 = Circle((0.3, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle2 = Circle((0.5, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle3 = Circle((0.7, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            ax1.add_patch(circle1)
            ax1.add_patch(circle2)
            ax1.add_patch(circle3)

        # Connecting lines
        for i in range(4):
            y = 0.2 + i * 0.15
            ax1.plot([0.3, 0.3], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.5, 0.5], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.7, 0.7], [y+0.04, y+0.11], 'b-', alpha=0.5)

        ax1.set_title('Microtubule Structure\nTubulin Arrangement', fontsize=13, fontweight='bold')

        ax1.text(0.5, 0.05, 'Diameter: ~25 nm\nLength: several micrometers',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))

        # === Panel 2: Quantum superposition ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # Two states of tubulin
        circle_left = Circle((0.3, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='darkred', linewidth=2)
        circle_right = Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                             edgecolor='darkblue', linewidth=2)
        ax2.add_patch(circle_left)
        ax2.add_patch(circle_right)

        ax2.text(0.3, 0.5, 'State |0>', ha='center', va='center',
                fontsize=10, fontweight='bold')
        ax2.text(0.7, 0.5, 'State |1>', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # Double arrow
        ax2.annotate('', xy=(0.68, 0.5), xytext=(0.32, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
        ax2.text(0.5, 0.55, '+', ha='center', fontsize=16, fontweight='bold')

        ax2.text(0.5, 0.7, 'Superposition: alpha|0> + beta|1>', ha='center',
                fontsize=11, fontweight='bold', color='purple')

        ax2.set_title('Quantum Superposition of Tubulin', fontsize=13, fontweight='bold')

        # === Panel 3: Objective collapse ===
        ax3 = fig.add_subplot(2, 3, 3)

        # Time axis
        t = np.linspace(0, 0.03, 100)

        # "Size" of superposition (energy/mass difference)
        mass_diff = 1e-8 * (1 - np.exp(-t/0.01))  # kg

        ax3.plot(t * 1000, mass_diff * 1e8, 'b-', linewidth=3)
        ax3.axhline(1e-8 * 1e8, color='red', linestyle='--', linewidth=2,
                   label='Collapse threshold')

        # Mark the collapse point
        collapse_idx = np.where(mass_diff >= 1e-8 * 0.99)[0][0]
        ax3.scatter([t[collapse_idx] * 1000], [mass_diff[collapse_idx] * 1e8],
                   c='red', s=200, zorder=5, edgecolors='black', linewidth=2)
        ax3.text(t[collapse_idx] * 1000, mass_diff[collapse_idx] * 1e8 + 0.05,
                'Collapse!', ha='center', fontsize=11, fontweight='bold',
                color='red')

        ax3.set_xlabel('Time (ms)', fontsize=12)
        ax3.set_ylabel('Mass difference (x10^-8 kg)', fontsize=12)
        ax3.set_title('Objective Collapse Process\nSuperposition accumulates to threshold',
                     fontsize=13, fontweight='bold')
        ax3.legend(fontsize=10)
        ax3.grid(True, alpha=0.3)

        # === Panel 4: Collapse time calculation ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        # Calculate collapse time for different mass differences
        masses = np.logspace(-12, -6, 100)  # kg
        times = [self.calculate_collapse_time(m) * 1000 for m in masses]  # ms

        ax4_plot = fig.add_axes([0.1, 0.1, 0.25, 0.35])
        ax4_plot.loglog(masses, times, 'g-', linewidth=3)
        ax4_plot.set_xlabel('Mass difference (kg)', fontsize=11)
        ax4_plot.set_ylabel('Collapse time (ms)', fontsize=11)
        ax4_plot.set_title('Penrose Formula: tau = hbar/(Delta_M*c^2)',
                          fontsize=12, fontweight='bold')
        ax4_plot.grid(True, alpha=0.3)

        # Mark brain parameters
        brain_mass = 1e-8
        brain_time = self.calculate_collapse_time(brain_mass) * 1000
        ax4_plot.scatter([brain_mass], [brain_time], c='red', s=100,
                        zorder=5, edgecolors='black', linewidth=2)
        ax4_plot.text(brain_mass * 3, brain_time,
                     f'Brain\n~{brain_time:.1f} ms',
                     fontsize=9, color='red', fontweight='bold')

        # === Panel 5: Consciousness timeline ===
        ax5 = fig.add_subplot(2, 3, 5)

        # Simulate consciousness "refresh"
        n_updates = 10
        update_times = np.linspace(0, 0.25, n_updates)

        for i, t_update in enumerate(update_times):
            ax5.scatter([t_update * 1000], [1], c='purple', s=300,
                       alpha=0.7, edgecolors='black', linewidth=2)
            ax5.text(t_update * 1000, 1.1, f'{i+1}', ha='center',
                    fontsize=9, fontweight='bold')

        ax5.plot([0, 250], [1, 1], 'gray', linestyle='--', alpha=0.3)
        ax5.set_xlabel('Time (ms)', fontsize=12)
        ax5.set_title('"Quantum Refresh" of Consciousness\nEach collapse = one moment of awareness',
                     fontsize=13, fontweight='bold')
        ax5.set_ylim(0.5, 1.5)
        ax5.set_yticks([])
        ax5.grid(True, alpha=0.3, axis='x')

        # Frequency annotation
        ax5.text(125, 0.7, f'Frequency: ~40 Hz\n(matches brain gamma waves)',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === Panel 6: Orch OR summary ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text_summary = '''
        Orch OR Theory Summary:

        1. Tubulin proteins in quantum superposition
           |psi> = alpha|0> + beta|1>

        2. Superposition duration:
           tau = hbar / (Delta_M * c^2)

        3. When Delta_M is large enough:
           Spacetime curvature becomes significant
           -> Spontaneous collapse (objective reduction)

        4. Each collapse = moment of consciousness
           Collapse frequency ~40 Hz

        5. The brain orchestrates these collapses
           -> Unified conscious experience

        Key Predictions:
        * Anesthetics affect tubulin quantum states
        * Consciousness depends on quantum coherence
        * Consciousness is non-algorithmic

        Controversies:
        * Brain temperature too high?
        * Decoherence too rapid?
        * Does objective collapse exist?
        '''

        ax6.text(0.1, 0.5, text_summary, fontsize=9, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('orch_or_simulation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("ORCH OR THEORY: THE QUANTUM CONSCIOUSNESS HYPOTHESIS")
        print("="*70)

        print("\nPenrose-Hameroff (1996):")
        print("  * Orchestrated Objective Reduction")

        print("\nCore Mechanism:")
        print("  1. Tubulin proteins in quantum superposition")
        print("  2. Superposition persists for a duration")
        print("  3. When mass difference Delta_M is large enough")
        print("  4. Spacetime curvature becomes significant")
        print("  5. Spontaneous collapse (objective reduction)")
        print("  6. Each collapse = one moment of consciousness")

        print("\nPenrose Formula:")
        print(f"  tau = hbar / (Delta_M * c^2)")
        print(f"  hbar = {self.hbar:.3e} J*s")
        print(f"  c = {self.c:.0f} m/s")

        print("\nBrain Parameters (estimated):")
        brain_mass = 1e-8  # kg
        brain_tau = self.calculate_collapse_time(brain_mass)
        print(f"  Delta_M ~ {brain_mass:.0e} kg")
        print(f"  tau ~ {brain_tau * 1000:.1f} ms")
        print(f"  Frequency ~ {1/brain_tau:.0f} Hz")

        print("\nExperimental Evidence (2014):")
        print("  * Quantum vibrations found in microtubules at body temperature")
        print("  * But this does not fully prove Orch OR")

        print("\nControversy:")
        print("  Supporters: Explains unity and non-computability of consciousness")
        print("  Critics: Brain too warm, decoherence too rapid")

        print("\nPenrose (2020 Nobel Prize lecture):")
        print("  'I don't know whether consciousness is quantum.")
        print("   But if we want to understand consciousness, we need new physics.'")
        print("="*70)

# Run
orch_sim = OrchORSimulator()
orch_sim.visualize_orch_or()

def visualize_zen_enlightenment_collapse():
    """
    Visualize the analogy between Zen enlightenment and wave function collapse
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Panel 1: Delusion (before measurement) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Delusion (Before Measurement)', ha='center',
           fontsize=14, fontweight='bold')

    # Confused mind (superposition state)
    np.random.seed(42)
    for _ in range(30):
        x, y = np.random.random(2)
        ax.text(x, y, 'thought', fontsize=10, alpha=0.5,
               color=np.random.choice(['gray', 'darkgray']),
               rotation=np.random.randint(-30, 30))

    # Center: obscured mind
    circle = plt.Circle((0.5, 0.5), 0.15, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'Mind\nObscured', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.15, 'Scattered thoughts swirling\nLike a superposition state', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Panel 2: Awakening (during measurement) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Awakening (During Measurement)', ha='center',
           fontsize=14, fontweight='bold')

    # Flash (sudden awakening)
    for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        ax.plot([0.5, x], [0.5, y], 'yellow', linewidth=3, alpha=0.8)

    # Center: illuminated mind
    circle = plt.Circle((0.5, 0.5), 0.15, color='gold', alpha=0.9,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'Mind\nAwakened', ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(0.5, 0.15, 'Instant awakening\nLike wave function collapse', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === Panel 3: Post-awakening (after measurement) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Post-Awakening (After Measurement)', ha='center',
           fontsize=14, fontweight='bold')

    # Clear mind (definite state)
    circle = plt.Circle((0.5, 0.5), 0.2, color='lightblue', alpha=0.7,
                       edgecolor='blue', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'Original\nMind\nClear', ha='center', va='center',
           fontsize=12, fontweight='bold', color='darkblue')

    # Surrounding: clarity
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax.text(x, y, 'clarity', fontsize=9, alpha=0.6, color='blue')

    ax.text(0.5, 0.15, 'Mind illuminated, nature seen\nLike a definite state', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 4: Comparison summary ===
    ax = axes[1, 1]
    ax.axis('off')

    comparison = '''
    [Zen Enlightenment vs Wave Function Collapse]

    Zen Buddhism:
    * Delusion: Scattered thoughts, mind obscured
    * Awakening: Sudden insight, seeing true nature
    * Post-awakening: Original mind, clear

    Quantum Mechanics:
    * Before measurement: Superposition, indeterminate
    * During measurement: Wave function collapse
    * After measurement: Definite state

    Similarities:
    + Both are discontinuous changes
    + Both are instantaneous (quantum leap)
    + Both involve the role of "observation"
    + Both transition from indeterminate -> determinate

    Zen "sudden awakening":
    * Not gradual
    * Sudden
    * Unpredictable
    * Irreversible

    Wave function collapse:
    * Not continuous
    * Instantaneous
    * Random (probabilistic)
    * Irreversible

    Deep analogy:
    "Seeing one's true nature" = consciousness causing collapse?
    '''

    ax.text(0.1, 0.5, comparison, fontsize=10, va='center',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                    edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('zen_enlightenment_collapse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("ZEN ENLIGHTENMENT AND WAVE FUNCTION COLLAPSE: AN ANALOGY")
    print("="*70)

    print("\nZen's 'Seeing One's True Nature' (Kensho):")
    print("  * Illuminate the mind: understand one's own mind")
    print("  * See the nature: perceive one's true nature (Buddha-nature)")
    print("  * Methods: zazen, koan, the shout and the stick")
    print("  * Result: sudden awakening")

    print("\nHuineng's Sudden Awakening:")
    print("  Heard: 'Let the mind arise without dwelling on anything'")
    print("  -> Instantly awakened")

    print("\n  His verse:")
    print("  'Bodhi is fundamentally not a tree,")
    print("   Nor is the bright mirror a stand.")
    print("   Originally there is not a single thing --")
    print("   Where could dust alight?'")

    print("\nProperties of Zen 'Sudden Awakening':")
    print("  * Discontinuous: not gradual")
    print("  * Instantaneous: happens suddenly")
    print("  * Unpredictable: one cannot know when it will occur")
    print("  * Irreversible: once awakened, no turning back")

    print("\nProperties of Wave Function Collapse:")
    print("  * Discontinuous: quantum leap")
    print("  * Instantaneous: no transitional process")
    print("  * Random: only probabilities can be predicted")
    print("  * Irreversible: cannot be undone after collapse")

    print("\nDepth of the Analogy:")
    print("  Delusion (scattered thoughts) ~ Superposition (indeterminate)")
    print("  Awakening (sudden insight) ~ Collapse (measurement)")
    print("  Post-awakening (clarity) ~ Definite state (outcome)")

    print("\nQuestions:")
    print("  * Is 'seeing one's true nature' consciousness causing collapse?")
    print("  * Is 'observing one's own mind' a form of 'measurement'?")
    print("  * Is the Zen 'mind' a quantum process?")

    print("\nPossible Answers:")
    print("  * Both Zen and quantum mechanics point to:")
    print("    the central role of observation/mind")
    print("  * Both 'sudden awakening' and 'collapse' are")
    print("    instantaneous transitions from indeterminate to determinate")
    print("  * But the Zen 'mind' may transcend")
    print("    what physics defines as 'consciousness'")
    print("="*70)

# Run
visualize_zen_enlightenment_collapse()

def visualize_mind_principle_observer():
    """
    Visualize Wang Yangming's 'Mind Is Principle' and the Observer Effect
    """

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # === Panel 1: Classical view (things outside the mind) ===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    ax1.text(0.5, 0.95, 'Classical View: Things Outside Mind', ha='center',
            fontsize=14, fontweight='bold', transform=ax1.transAxes)

    # Matter outside
    rect_matter = plt.Rectangle((0.6, 0.4), 0.25, 0.3,
                                facecolor='blue', alpha=0.6,
                                edgecolor='black', linewidth=2)
    ax1.add_patch(rect_matter)
    ax1.text(0.725, 0.55, 'Matter\n(Objective)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Mind inside
    circle_mind = plt.Circle((0.25, 0.55), 0.1, color='red', alpha=0.6,
                            edgecolor='black', linewidth=2)
    ax1.add_patch(circle_mind)
    ax1.text(0.25, 0.55, 'Mind\n(Subjective)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Arrow: matter -> mind (passive reception)
    ax1.annotate('', xy=(0.35, 0.55), xytext=(0.6, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax1.text(0.475, 0.6, 'Perception', ha='center', fontsize=10)

    ax1.text(0.5, 0.15, 'Matter independent of mind\nMind passively receives', ha='center',
            fontsize=10, transform=ax1.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 2: Wang Yangming's "Mind Is Principle" ===
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    ax2.text(0.5, 0.95, 'Wang Yangming: Mind Is Principle', ha='center',
            fontsize=14, fontweight='bold', transform=ax2.transAxes)

    # Mind at center
    circle_mind = plt.Circle((0.5, 0.55), 0.15, color='gold', alpha=0.7,
                            edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_mind)
    ax2.text(0.5, 0.55, 'Mind\n(Ontological\nGround)', ha='center', va='center',
            fontsize=11, fontweight='bold')

    # Things manifesting from mind
    manifestations = [
        (0.25, 0.75, 'Thing 1'),
        (0.75, 0.75, 'Thing 2'),
        (0.25, 0.35, 'Thing 3'),
        (0.75, 0.35, 'Thing 4'),
    ]

    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.07, color='lightblue', alpha=0.6,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, label, ha='center', va='center', fontsize=9)

        # Arrow: mind -> things
        ax2.annotate('', xy=(x, y), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=2, color='orange',
                                  alpha=0.6))

    ax2.text(0.5, 0.15, '"Outside the mind, there are no things"\nThings manifest through mind', ha='center',
            fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === Panel 3: Quantum observer effect ===
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    ax3.text(0.5, 0.95, 'Quantum Mechanics: Observer Effect', ha='center',
            fontsize=14, fontweight='bold', transform=ax3.transAxes)

    # Observer
    circle_observer = plt.Circle((0.5, 0.75), 0.1, color='purple', alpha=0.7,
                                edgecolor='indigo', linewidth=2)
    ax3.add_patch(circle_observer)
    ax3.text(0.5, 0.75, 'Observer', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Arrow downward (observation)
    ax3.annotate('', xy=(0.5, 0.45), xytext=(0.5, 0.65),
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax3.text(0.6, 0.55, 'Observation\nMeasurement', ha='left', fontsize=10,
            color='red', fontweight='bold')

    # Quantum system (superposition -> definite)
    # Superposition
    circle_left = plt.Circle((0.35, 0.35), 0.06, color='red', alpha=0.3,
                            edgecolor='red', linewidth=1.5)
    circle_right = plt.Circle((0.65, 0.35), 0.06, color='blue', alpha=0.3,
                             edgecolor='blue', linewidth=1.5)
    ax3.add_patch(circle_left)
    ax3.add_patch(circle_right)

    # Superposition indicator
    ax3.plot([0.35, 0.65], [0.35, 0.35], 'gray', linestyle=':', alpha=0.5)
    ax3.text(0.5, 0.3, 'Superposition', ha='center', fontsize=9, color='gray')

    # Collapsed state
    circle_result = plt.Circle((0.5, 0.15), 0.08, color='green', alpha=0.7,
                              edgecolor='darkgreen', linewidth=2)
    ax3.add_patch(circle_result)
    ax3.text(0.5, 0.15, 'Definite\nState', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    ax3.annotate('', xy=(0.5, 0.23), xytext=(0.5, 0.29),
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))

    ax3.text(0.5, 0.05, 'Observation creates reality\nProperties depend on measurement', ha='center',
            fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Main title
    fig.text(0.5, 0.98, 'The Role of "Mind": Three Perspectives',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig('mind_principle_observer.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("WANG YANGMING'S 'MIND IS PRINCIPLE' AND THE OBSERVER EFFECT")
    print("="*70)

    print("\nWang Yangming's Philosophy of Mind:")
    print("  Core: 'Mind is Principle' (xin ji li)")
    print("  -> Outside the mind, there are no things or principles")
    print("  -> Apart from mind, one cannot discuss the existence or meaning of things")

    print("\nThe Enlightenment at Longchang (1508):")
    print("  'The Way of the Sage is complete in my own nature.")
    print("   I was wrong to seek principle in external things!'")
    print("  -> Seeking truth externally was a mistake")
    print("  -> Principle resides within the mind")

    print("\n'Unity of Knowledge and Action':")
    print("  * Genuine knowledge necessarily leads to action")
    print("  * Knowledge and action cannot be separated")
    print("  * Example: truly knowing fire burns -> not touching fire")

    print("\nThe Quantum Observer Effect:")
    print("  * Before measurement: particle in superposition")
    print("  * During measurement: wave function collapses")
    print("  * After measurement: particle in definite state")
    print("  -> The observer participates in creating reality")

    print("\nCorrespondences:")
    print("  Wang Yangming: 'Outside the mind, there are no things'")
    print("  Quantum: Without observation, there are no definite properties")

    print("\n  Wang Yangming: Things manifest through mind")
    print("  Quantum: Properties are determined by measurement")

    print("\nDifferences:")
    print("  * Wang Yangming's 'mind':")
    print("    Not merely individual consciousness")
    print("    But ontological ground, universal mind")
    print("  * Quantum 'observer':")
    print("    Can be a measuring instrument")
    print("    Does not necessarily require consciousness")

    print("\nShared Insight:")
    print("  * 'Objective reality' depends on the subject")
    print("  * Subject and object cannot be separated")
    print("  * The 'thing-in-itself' is unknowable")

    print("\nDeep Questions:")
    print("  * Is Wang Yangming's 'mind' = the quantum 'observer'?")
    print("  * Does 'Mind is Principle' = 'observation creates reality'?")
    print("  * Or do they point to different levels of truth?")
    print("="*70)

# Run
visualize_mind_principle_observer()
