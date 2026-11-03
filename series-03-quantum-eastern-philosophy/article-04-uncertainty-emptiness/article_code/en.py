# Code & Cogito: The Uncertainty Principle vs Buddhist "Emptiness" — Nothing Has an Inherent Nature
# Article: https://code-cogito.com/en/uncertainty-principle-buddhist-emptiness-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class UncertaintyPrinciple:
    """
    Uncertainty Principle Interactive Experiment
    Demonstrates: the trade-off between position uncertainty and momentum uncertainty
    """

    def __init__(self):
        self.hbar = 1.0  # Reduced Planck constant (arbitrary units)

    def gaussian_wavepacket(self, x, x0, sigma_x, k0):
        """
        Gaussian wave packet
        x0: center position
        sigma_x: position standard deviation (uncertainty)
        k0: center wave number (corresponding momentum p0 = hbar * k0)
        """
        return (1 / (2 * np.pi * sigma_x**2)**0.25) * \
               np.exp(-((x - x0)**2) / (4 * sigma_x**2)) * \
               np.exp(1j * k0 * x)

    def momentum_distribution(self, psi_x, dx):
        """
        Compute momentum-space wave function from position-space wave function
        using Fourier transform
        """
        psi_k = fft(psi_x) * dx
        return psi_k

    def visualize_uncertainty(self, sigma_x_values=[0.5, 1.0, 2.0, 4.0]):
        """
        Visualize wave packets with different position uncertainties
        """
        x = np.linspace(-20, 20, 2000)
        dx = x[1] - x[0]

        fig, axes = plt.subplots(2, len(sigma_x_values), figsize=(18, 10))

        for i, sigma_x in enumerate(sigma_x_values):
            # Generate wave packet
            psi_x = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

            # Position-space probability density
            prob_x = np.abs(psi_x)**2

            # Momentum space
            psi_k = self.momentum_distribution(psi_x, dx)
            k = fftfreq(len(x), dx) * 2 * np.pi
            prob_k = np.abs(psi_k)**2

            # Reorder (fft output needs rearranging)
            k_sorted_idx = np.argsort(k)
            k_sorted = k[k_sorted_idx]
            prob_k_sorted = prob_k[k_sorted_idx]

            # Calculate uncertainties
            delta_x = sigma_x
            delta_k = 1 / (2 * sigma_x)
            delta_p = self.hbar * delta_k
            uncertainty_product = delta_x * delta_p

            # === Top row: Position space ===
            ax = axes[0, i]
            ax.plot(x, prob_x, 'b-', linewidth=2)
            ax.fill_between(x, 0, prob_x, alpha=0.3, color='blue')
            ax.set_xlabel('Position x', fontsize=11)
            ax.set_ylabel('|ψ(x)|²', fontsize=11)
            ax.set_title(f'Position Uncertainty\nΔx = {delta_x:.2f}',
                        fontsize=12, fontweight='bold', color='blue')
            ax.grid(True, alpha=0.3)
            ax.set_xlim(-15, 15)
            ax.axvspan(-delta_x, delta_x, alpha=0.2, color='cyan',
                      label=f'Δx = {delta_x:.2f}')
            ax.legend(fontsize=9)

            # === Bottom row: Momentum space ===
            ax = axes[1, i]
            center_idx = len(k_sorted) // 2
            plot_range = 500
            k_plot = k_sorted[center_idx-plot_range:center_idx+plot_range]
            prob_k_plot = prob_k_sorted[center_idx-plot_range:center_idx+plot_range]

            if np.max(prob_k_plot) > 0:
                prob_k_plot = prob_k_plot / np.max(prob_k_plot)

            ax.plot(k_plot, prob_k_plot, 'r-', linewidth=2)
            ax.fill_between(k_plot, 0, prob_k_plot, alpha=0.3, color='red')
            ax.set_xlabel('Wave number k (momentum p=ℏk)', fontsize=11)
            ax.set_ylabel('|ψ(k)|²', fontsize=11)
            ax.set_title(f'Momentum Uncertainty\nΔp = {delta_p:.2f}',
                        fontsize=12, fontweight='bold', color='red')
            ax.grid(True, alpha=0.3)

            color = 'green' if uncertainty_product >= self.hbar/2 else 'red'
            ax.text(0.5, 0.9,
                   f'Δx·Δp = {uncertainty_product:.3f}\n(ℏ/2 = {self.hbar/2:.3f})',
                   transform=ax.transAxes, ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor=color, alpha=0.5))

        fig.text(0.5, 0.98, 'Uncertainty Principle: Smaller Δx → Larger Δp',
                ha='center', fontsize=16, fontweight='bold')
        fig.text(0.5, 0.02,
                'Key Insight: This is not measurement error — it is a mathematical property of waves!\n'
                'You cannot make a wave packet both narrow (well-defined position) and spectrally pure (well-defined momentum)',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(top=0.93, bottom=0.1)
        plt.savefig('uncertainty_principle_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()

    def interactive_measurement(self):
        """
        Interactive measurement: observe the effect of measurement order
        """
        print("\n" + "="*70)
        print("  UNCERTAINTY PRINCIPLE — INTERACTIVE EXPERIMENT")
        print("="*70)

        x = np.linspace(-10, 10, 1000)
        sigma_x = 1.0
        psi = self.gaussian_wavepacket(x, x0=0, sigma_x=sigma_x, k0=5)

        print("\nInitial state:")
        print(f"  Position uncertainty  Δx ≈ {sigma_x:.2f}")
        print(f"  Momentum uncertainty  Δp ≈ {self.hbar/(2*sigma_x):.2f}")
        print(f"  Uncertainty product   Δx·Δp ≈ {sigma_x * self.hbar/(2*sigma_x):.3f}")
        print(f"  Heisenberg lower bound ℏ/2 = {self.hbar/2:.3f}")

        print("\nExperiment 1: Measure position first, then momentum")
        print("  → After measuring position, the wave function collapses to a point")
        print("  → Now Δx → 0, therefore Δp → ∞")
        print("  → Momentum becomes completely uncertain!")

        print("\nExperiment 2: Measure momentum first, then position")
        print("  → After measuring momentum, the wave function becomes a plane wave")
        print("  → Now Δp → 0, therefore Δx → ∞")
        print("  → Position becomes completely uncertain!")

        print("\nConclusion:")
        print("  • Measurement order matters (x̂ and p̂ don't commute)")
        print("  • Measuring one quantity disturbs the other")
        print("  • This is not an instrument problem — it is a law of nature")

        print("\nBuddhist parallel:")
        print("  • Nothing has a fixed 'inherent nature'")
        print("  • Properties depend on how we observe")
        print("  • Different perspectives reveal different aspects")
        print("="*70)

# Run
experiment = UncertaintyPrinciple()
experiment.visualize_uncertainty(sigma_x_values=[0.5, 1.0, 2.0, 4.0])
experiment.interactive_measurement()

def visualize_emptiness():
    """
    Visualizing 'Emptiness'
    Demonstrates: how an object's properties depend on the conditions of observation
    """

    fig = plt.figure(figsize=(16, 12))

    # === Example: The "Emptiness" of a Cup ===

    # Subplot 1: Different angles reveal different shapes
    ax1 = fig.add_subplot(2, 3, 1)
    circle = plt.Circle((0.5, 0.5), 0.3, fill=False, edgecolor='blue', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.1, 'Top view: Circle', ha='center', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Subplot 2: Side view: rectangle
    ax2 = fig.add_subplot(2, 3, 2)
    rect = plt.Rectangle((0.2, 0.2), 0.6, 0.6, fill=False, edgecolor='red', linewidth=3)
    ax2.add_patch(rect)
    ax2.text(0.5, 0.1, 'Side view: Rectangle', ha='center', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # Subplot 3: The question
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.text(0.5, 0.5, 'Q: What is the cup\'s\n"true shape"?\n\nA: There is no\n"fixed shape"!\n\nShape depends on\nthe viewing angle',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')

    # === Quantum analogy: The "position" of a particle ===

    # Subplot 4: Position measurement
    ax4 = fig.add_subplot(2, 3, 4)
    x = np.linspace(-5, 5, 1000)
    psi_position = np.exp(-x**2)
    ax4.plot(x, psi_position, 'b-', linewidth=3)
    ax4.fill_between(x, 0, psi_position, alpha=0.3, color='blue')
    ax4.set_xlabel('Position', fontsize=11)
    ax4.set_ylabel('Probability', fontsize=11)
    ax4.set_title('Measure "Position"\n→ Position well-defined', fontsize=12, fontweight='bold', color='blue')
    ax4.grid(True, alpha=0.3)

    # Subplot 5: Momentum measurement
    ax5 = fig.add_subplot(2, 3, 5)
    k = np.linspace(-5, 5, 1000)
    psi_momentum = np.exp(-(k-2)**2/4)
    ax5.plot(k, psi_momentum, 'r-', linewidth=3)
    ax5.fill_between(k, 0, psi_momentum, alpha=0.3, color='red')
    ax5.set_xlabel('Momentum', fontsize=11)
    ax5.set_ylabel('Probability', fontsize=11)
    ax5.set_title('Measure "Momentum"\n→ Momentum well-defined', fontsize=12, fontweight='bold', color='red')
    ax5.grid(True, alpha=0.3)

    # Subplot 6: Conclusion
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.text(0.5, 0.5, 'Q: What is the particle\'s\n"true state"?\n\nA: There are no\n"fixed properties"!\n\nProperties depend on\nthe measurement',
            ha='center', va='center', fontsize=13,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')

    # Title and comparison notes
    fig.text(0.5, 0.98, 'Structural Parallel: "Emptiness" and "Uncertainty"',
            ha='center', fontsize=16, fontweight='bold')
    fig.text(0.5, 0.02,
            'Buddhism: Things have no "inherent nature" (fixed essence) — properties manifest depending on conditions\n'
            'Quantum Mechanics: Particles have no "definite properties" — properties are determined by measurement\n'
            'Common ground: "Fixedness" is not a fundamental feature of reality',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.12)
    plt.savefig('emptiness_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Text explanation
    print("\n" + "="*70)
    print("  THREE LAYERS OF EMPTINESS")
    print("="*70)

    print("\n1. Emptiness Is Not Nothingness")
    print("   Heart Sutra: 'Form is emptiness; emptiness is form'")
    print("   → Things exist, but they have no fixed essence")

    print("\n2. Emptiness Is Dependent Origination")
    print("   Nagarjuna: 'Whatever is dependently co-arisen is explained to be emptiness'")
    print("   → Everything exists in dependence on conditions")

    print("\n3. Emptiness Dissolves Attachment")
    print("   → There is no fixed 'self'")
    print("   → There are no fixed 'things'")
    print("   → Realizing emptiness, we let go of clinging")

    print("\nParallel with the Uncertainty Principle:")
    print("   • A particle has no fixed 'position' or 'momentum'")
    print("   • Properties depend on the method of measurement")
    print("   • There are no 'objective properties' independent of observation")

    print("\nShared insight:")
    print("   The world is not composed of 'objects with fixed properties'")
    print("   but of 'relationships that manifest under conditions'")
    print("="*70)

# Run
visualize_emptiness()

import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

def indras_net_quantum():
    """
    Indra's Net and Quantum Entanglement
    Demonstrates: everything is interconnected — changing one affects all
    """

    fig = plt.figure(figsize=(18, 12))

    # === Left plot: Indra's Net (2D network) ===
    ax1 = fig.add_subplot(2, 2, 1)

    n = 5
    G = nx.grid_2d_graph(n, n)
    pos = {(i, j): (i, j) for i, j in G.nodes()}

    nx.draw_networkx_nodes(G, pos, node_color='gold', node_size=800,
                          edgecolors='black', linewidths=2, ax=ax1)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, ax=ax1)

    highlight_node = (2, 2)
    nx.draw_networkx_nodes(G, pos, nodelist=[highlight_node],
                          node_color='red', node_size=1000,
                          edgecolors='black', linewidths=3, ax=ax1)

    ax1.set_title("Indra's Net: Each jewel reflects all others\nChange one, and every reflection changes",
                 fontsize=13, fontweight='bold')
    ax1.axis('off')
    ax1.text(2, -0.5, 'Huayan Buddhism: One is all, and all is one',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === Right plot: Quantum entanglement network (3D) ===
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')

    n_particles = 8
    positions = np.random.randn(n_particles, 3)

    ax2.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='cyan', s=300, edgecolors='black', linewidth=2, alpha=0.8)

    for i in range(n_particles):
        for j in range(i+1, n_particles):
            ax2.plot([positions[i, 0], positions[j, 0]],
                    [positions[i, 1], positions[j, 1]],
                    [positions[i, 2], positions[j, 2]],
                    'b-', alpha=0.2, linewidth=1)

    ax2.scatter([positions[0, 0]], [positions[0, 1]], [positions[0, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    ax2.set_title('Quantum Entanglement: Non-local correlations\nMeasure one particle, affect them all',
                 fontsize=13, fontweight='bold')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    # === Bottom left: Entangled state mathematics ===
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.axis('off')

    text = '''
    Entangled State (Bell State):

    |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2

    Properties:
    • Particles A and B are inseparable
    • Measure A → instantly know B
    • A's state cannot be defined alone
    • The whole ≠ sum of parts

    Bell's Inequality (1964):
    If particles have "local realism"
    → a certain inequality must hold

    Experimental results (1982-2022):
    The inequality is violated!
    → No local realism
    → Entanglement is real
    '''

    ax3.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Bottom right: Indra's Net vs Entanglement ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    comparison = '''
    Indra's Net vs Quantum Entanglement

    Indra's Net:
    • Each jewel contains the entire net
    • Change one jewel, the whole net shifts
    • The part is the whole
    • One is all

    Quantum Entanglement:
    • Each particle carries information about the whole system
    • Measure one particle, affect all entangled partners
    • Individual particle states cannot be defined alone
    • The whole is irreducible

    Common ground:
    → No truly "independent" parts
    → Everything is interdependent
    → Changing a part = changing the whole
    '''

    ax4.text(0.1, 0.5, comparison, fontsize=11, va='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.savefig('indras_net_entanglement.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Detailed text output
    print("\n" + "="*70)
    print("  INDRA'S NET AND QUANTUM ENTANGLEMENT")
    print("="*70)

    print("\nIndra's Net (from the Avatamsaka Sutra):")
    print("  • An infinite net of jewels")
    print("  • Each jewel reflects every other jewel")
    print("  • Infinite recursion, mutual illumination")
    print("  → One is all, and all is one")

    print("\nQuantum Entanglement:")
    print("  • Two or more particles exist in an entangled state")
    print("  • |ψ⟩ = (|↑↓⟩ - |↓↑⟩) / √2")
    print("  • Measuring one particle instantly affects its partners")
    print("  • Correlations persist even across light-years")

    print("\nExperimental evidence:")
    print("  • 1982: Aspect's experiment confirms entanglement")
    print("  • 2015: 'Loophole-free' Bell tests")
    print("  • 2022: Nobel Prize in Physics")

    print("\nPhilosophical implications:")
    print("  • No particle is truly 'independent'")
    print("  • The universe is an indivisible whole")
    print("  • 'Separation' is an illusion")

    print("\nBuddhist 'Dependent Origination':")
    print("  • 'This arising, that arises; this ceasing, that ceases'")
    print("  • All phenomena mutually condition one another")
    print("  • There is no independently existing 'self' or 'thing'")

    print("\nShared insight:")
    print("  The world is not 'a collection of independent entities'")
    print("  but 'an interdependent web of relationships'")
    print("="*70)

# Run
indras_net_quantum()

def self_as_entanglement():
    """
    The 'Emptiness' of Self
    Demonstrates: how the 'self' is a convergence of causes and conditions,
    with no independent inherent nature
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # === Left panel: The classical notion of "self" ===
    circle_self = plt.Circle((0.5, 0.5), 0.15, color='red', alpha=0.7,
                            edgecolor='black', linewidth=3)
    ax1.add_patch(circle_self)
    ax1.text(0.5, 0.5, 'Self', ha='center', va='center', fontsize=20,
            fontweight='bold', color='white')

    external_things = [
        (0.2, 0.8, 'Family'),
        (0.8, 0.8, 'Friends'),
        (0.1, 0.5, 'Work'),
        (0.9, 0.5, 'Body'),
        (0.2, 0.2, 'Memories'),
        (0.8, 0.2, 'Thoughts'),
    ]

    for x, y, label in external_things:
        circle = plt.Circle((x, y), 0.08, color='lightblue', alpha=0.5,
                           edgecolor='gray', linewidth=1.5)
        ax1.add_patch(circle)
        ax1.text(x, y, label, ha='center', va='center', fontsize=10)
        ax1.annotate('', xy=(x, y), xytext=(0.5, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black', alpha=0.5))

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Classical View: An Independent "Self"\n"I" possess body, memories, thoughts...',
                 fontsize=14, fontweight='bold')
    ax1.text(0.5, 0.05, 'Assumption: there exists an independent "self" at the core',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === Right panel: Buddhist "No-Self" (Anātman) ===
    elements = [
        (0.3, 0.7, 'Form'),
        (0.7, 0.7, 'Feeling'),
        (0.5, 0.5, 'Perception'),
        (0.3, 0.3, 'Volition'),
        (0.7, 0.3, 'Consciousness'),
    ]

    for x, y, label in elements:
        circle = plt.Circle((x, y), 0.1, color='lightgreen', alpha=0.6,
                           edgecolor='green', linewidth=2)
        ax2.add_patch(circle)
        ax2.text(x, y, label, ha='center', va='center', fontsize=12,
                fontweight='bold')

    for i, (x1, y1, _) in enumerate(elements):
        for x2, y2, _ in elements[i+1:]:
            ax2.plot([x1, x2], [y1, y2], 'g-', alpha=0.3, linewidth=2)

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Buddhist View: The Five Aggregates — No-Self\nNo independent "I", only interdependent conditions',
                 fontsize=14, fontweight='bold')
    ax2.text(0.5, 0.05, 'Reality: "I" is a temporary convergence of Five Aggregates (form, feeling, perception, volition, consciousness)',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('self_emptiness.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Quantum analogy
    print("\n" + "="*70)
    print("  THE EMPTINESS OF SELF: THE SELF AS AN ENTANGLED STATE")
    print("="*70)

    print("\nThe Buddhist 'Five Aggregates' (skandhas):")
    print("  1. Form (rupa):         body, matter")
    print("  2. Feeling (vedana):    sensations")
    print("  3. Perception (samjna): concepts, recognition")
    print("  4. Volition (samskara): will, behavioral tendencies")
    print("  5. Consciousness (vijnana): awareness")

    print("\nBuddhist teaching:")
    print("  • There is no independent 'self'")
    print("  • 'Self' is merely a temporary configuration of the Five Aggregates")
    print("  • Aggregates converge → the illusion of 'self' arises")
    print("  • Aggregates disperse → 'self' disappears")

    print("\nQuantum analogy:")
    print("  • A particle has no independent 'state'")
    print("  • 'State' is a projection onto a measurement basis")
    print("  • A system can be decomposed into different bases:")
    print("    |ψ⟩ = Σ cᵢ|φᵢ⟩ (position basis)")
    print("    |ψ⟩ = Σ dⱼ|χⱼ⟩ (momentum basis)")
    print("  • No 'essential' state — only expressions relative to a basis")

    print("\nHow the 'self' resembles an entangled state:")
    print("  |self⟩ = α|body⟩|memory⟩|environment⟩... (simplified)")
    print("  ")
    print("  • 'Self' is entangled with body (change the body → 'self' changes)")
    print("  • 'Self' is entangled with memory (amnesia → 'self' changes)")
    print("  • 'Self' is entangled with environment (new context → 'self' changes)")
    print("  • There is no 'core self' independent of all these")

    print("\nPractical implications:")
    print("  • Clinging to a fixed 'self' is the root of suffering")
    print("  • Realizing 'no-self' can bring liberation")
    print("  • This does not mean 'I don't exist' — it means 'I have no fixed essence'")
    print("  • 'I' exists dependently — when conditions change, 'I' changes")

    print("\nA deep question:")
    print("  If 'I' has no inherent nature, then who is reading these words?")
    print("  Answer: The process of reading is happening, but there is no independent 'reader.'")
    print("  Just as wave function collapse happens, but there is no independent 'particle.'")
    print("="*70)

# Run
self_as_entanglement()
