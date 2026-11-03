# Code & Cogito: Quantum Field Theory vs. Buddhist Yogacara — Is Matter a Manifestation of Mind?
# Article: https://code-cogito.com/en/quantum-field-theory-yogacara-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class QuantumFieldSimulator:
    """
    Quantum Field Simulator
    Demonstrates how field excitations give rise to particles
    """

    def __init__(self, size=100):
        self.size = size
        self.x = np.linspace(-10, 10, size)
        self.y = np.linspace(-10, 10, size)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def field_vacuum(self):
        """Vacuum state: the field's ground state with tiny quantum fluctuations"""
        fluctuation = np.random.randn(self.size, self.size) * 0.1
        return fluctuation

    def field_one_particle(self, x0=0, y0=0, k=1):
        """One-particle state: a localized field excitation (Gaussian wave packet)"""
        R = np.sqrt((self.X - x0)**2 + (self.Y - y0)**2)
        particle = 2.0 * np.exp(-R**2 / 2) * np.cos(k * R)
        vacuum = self.field_vacuum()
        return particle + vacuum

    def field_two_particles(self, x1=-3, y1=0, x2=3, y2=0):
        """Two-particle state: two localized excitations"""
        R1 = np.sqrt((self.X - x1)**2 + (self.Y - y1)**2)
        R2 = np.sqrt((self.X - x2)**2 + (self.Y - y2)**2)
        particle1 = 2.0 * np.exp(-R1**2 / 2) * np.cos(2 * R1)
        particle2 = 2.0 * np.exp(-R2**2 / 2) * np.cos(2 * R2)
        vacuum = self.field_vacuum()
        return particle1 + particle2 + vacuum

    def visualize_field_states(self):
        """Visualize different field states"""
        fig = plt.figure(figsize=(18, 12))

        # === Vacuum state ===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')
        vacuum = self.field_vacuum()
        surf1 = ax1.plot_surface(self.X, self.Y, vacuum, cmap='coolwarm',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax1.set_title('Vacuum State |0>\nGround State (Quantum Fluctuations)',
                     fontsize=13, fontweight='bold')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Field Amplitude')
        ax1.set_zlim(-3, 3)

        # === One-particle state ===
        ax2 = fig.add_subplot(2, 3, 2, projection='3d')
        one_particle = self.field_one_particle(x0=0, y0=0)
        surf2 = ax2.plot_surface(self.X, self.Y, one_particle, cmap='viridis',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax2.set_title('One-Particle State a-dag|0>\nLocalized Field Excitation',
                     fontsize=13, fontweight='bold')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Field Amplitude')
        ax2.set_zlim(-3, 3)

        # === Two-particle state ===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')
        two_particles = self.field_two_particles()
        surf3 = ax3.plot_surface(self.X, self.Y, two_particles, cmap='plasma',
                                linewidth=0, antialiased=True, alpha=0.8)
        ax3.set_title('Two-Particle State a-dag a-dag|0>\nTwo Localized Excitations',
                     fontsize=13, fontweight='bold')
        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('Field Amplitude')
        ax3.set_zlim(-3, 3)

        # === Vacuum energy density (cross-section) ===
        ax4 = fig.add_subplot(2, 3, 4)
        vacuum_slice = vacuum[self.size//2, :]
        ax4.plot(self.x, vacuum_slice, 'b-', linewidth=2)
        ax4.fill_between(self.x, 0, vacuum_slice, alpha=0.3, color='blue')
        ax4.set_xlabel('Position X', fontsize=11)
        ax4.set_ylabel('Field Amplitude', fontsize=11)
        ax4.set_title('Vacuum Quantum Fluctuations (X Cross-Section)', fontsize=12, fontweight='bold')
        ax4.grid(True, alpha=0.3)
        ax4.axhline(0, color='black', linewidth=0.5)

        # === One-particle energy density (cross-section) ===
        ax5 = fig.add_subplot(2, 3, 5)
        one_particle_slice = one_particle[self.size//2, :]
        ax5.plot(self.x, one_particle_slice, 'g-', linewidth=2)
        ax5.fill_between(self.x, 0, one_particle_slice, alpha=0.3, color='green')
        ax5.set_xlabel('Position X', fontsize=11)
        ax5.set_ylabel('Field Amplitude', fontsize=11)
        ax5.set_title('Particle = Localized Field Excitation (X Cross-Section)', fontsize=12, fontweight='bold')
        ax5.grid(True, alpha=0.3)
        ax5.axhline(0, color='black', linewidth=0.5)

        # === Comparison panel ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text = '''
        [QFT vs. Yogacara]

        Quantum Field Theory:
        * Field = fundamental reality
        * Particles = field excitations
        * Vacuum != nothingness

        Yogacara Buddhism:
        * Consciousness = fundamental reality
        * Phenomena = consciousness-manifestations
        * Alaya-vijnana != emptiness

        Shared Insight:
        > "Matter" is not fundamental
        > "Field / Consciousness" is
        > Appearance depends on excitation
        '''

        ax6.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('quantum_field_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Quantum Fields and Particles]")
        print("="*70)
        print("\nClassical physics: Particle = fundamental entity with fixed position and velocity")
        print("Quantum field theory: Field = fundamental entity, Particle = field excitation")
        print("\nYogacara analogy:")
        print("  Alaya-vijnana ~ quantum field")
        print("  Seeds ~ latent excitation modes of the field")
        print("  Manifestation ~ actual field excitation (particle)")
        print("\nQFT: 'Particles are not things. Particles are merely field excitations.'")
        print("Yogacara: 'Phenomena are not things. Phenomena are merely consciousness-manifestations.'")
        print("="*70)

# Run
simulator = QuantumFieldSimulator(size=100)
simulator.visualize_field_states()

class VirtualParticleSimulator:
    """Virtual particle simulator: illustrates particle-antiparticle creation
    and annihilation in the quantum vacuum"""

    def __init__(self):
        pass

    def visualize_vacuum_fluctuations(self):
        """Visualize vacuum fluctuations"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left panel: spacetime diagram of virtual particle creation/annihilation ===
        t = np.linspace(0, 10, 1000)
        n_pairs = 15
        np.random.seed(42)

        for i in range(n_pairs):
            t_create = np.random.uniform(0, 10)
            lifetime = np.random.exponential(0.5)
            t_annihilate = t_create + lifetime
            if t_annihilate > 10:
                t_annihilate = 10

            x_particle = np.random.uniform(-2, 2)
            x_antiparticle = -x_particle

            ax1.plot([t_create, t_annihilate], [x_particle, x_particle],
                    'r-', linewidth=2, alpha=0.6)
            ax1.plot([t_create, t_annihilate], [x_antiparticle, x_antiparticle],
                    'b--', linewidth=2, alpha=0.6)

            ax1.scatter([t_create], [x_particle], c='red', s=100,
                       zorder=5, edgecolors='black', linewidth=1)
            ax1.scatter([t_create], [x_antiparticle], c='blue', s=100,
                       zorder=5, edgecolors='black', linewidth=1)
            ax1.scatter([t_annihilate], [x_particle], c='purple', s=150,
                       marker='*', zorder=5, edgecolors='black', linewidth=1)

            ax1.plot([t_create, t_create], [x_particle, x_antiparticle],
                    'gray', linestyle=':', alpha=0.3, linewidth=1)
            ax1.plot([t_annihilate, t_annihilate], [x_particle, x_antiparticle],
                    'purple', linestyle=':', alpha=0.5, linewidth=1.5)

        ax1.set_xlabel('Time', fontsize=13)
        ax1.set_ylabel('Spatial Position', fontsize=13)
        ax1.set_title('Virtual Particle Creation/Annihilation in the Vacuum\nHeisenberg Uncertainty: dE*dt >= hbar/2',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, 10)
        ax1.set_ylim(-3, 3)

        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='r', linewidth=2, label='Particle'),
            Line2D([0], [0], color='b', linewidth=2, linestyle='--', label='Antiparticle'),
            Line2D([0], [0], marker='*', color='purple', markersize=12,
                  linestyle='None', label='Annihilation'),
        ]
        ax1.legend(handles=legend_elements, fontsize=11)

        # === Right panel: Feynman diagram (electron-electron scattering) ===
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        ax2.text(0.5, 0.95, 'Feynman Diagram: Electron-Electron Scattering',
                ha='center', fontsize=14, fontweight='bold',
                transform=ax2.transAxes)

        # Incoming and outgoing electrons
        ax2.arrow(0.1, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.25, 'e-', fontsize=12, ha='center')
        ax2.arrow(0.1, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.15, 0.75, 'e-', fontsize=12, ha='center')

        # Virtual photon exchange
        ax2.plot([0.35, 0.35], [0.3, 0.7], 'r', linewidth=3,
                linestyle='dotted', alpha=0.7)
        ax2.text(0.42, 0.5, 'Virtual\nPhoton\ngamma*', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        ax2.arrow(0.35, 0.3, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.25, 'e-', fontsize=12, ha='center')
        ax2.arrow(0.35, 0.7, 0.25, 0, head_width=0.03, head_length=0.03,
                 fc='blue', ec='blue', linewidth=2)
        ax2.text(0.55, 0.75, 'e-', fontsize=12, ha='center')

        explanation = '''
        Feynman Diagram Rules:
        * Solid lines -> real particles
        * Dashed lines -> virtual particles
        * Vertices -> interactions

        Virtual Photon Properties:
        * Extremely short-lived
        * Cannot be directly observed
        * But genuinely affects interactions
        '''
        ax2.text(0.5, 0.15, explanation, fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        plt.tight_layout()
        plt.savefig('virtual_particles_feynman.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Virtual Particles and Vacuum Energy]")
        print("="*70)
        print("\nHeisenberg Uncertainty Principle: dE * dt >= hbar/2")
        print("-> Virtual particle-antiparticle pairs constantly arise and annihilate in the vacuum")
        print("\nCasimir Effect (predicted 1948, experimentally confirmed 1997):")
        print("  -> Proof: the vacuum is not empty!")
        print("\nYogacara analogy:")
        print("  Alaya-vijnana = vacuum (brimming with potential)")
        print("  Seeds ripening = virtual particles materializing")
        print("  Manifestation dissolving = virtual particles annihilating")
        print("\nProfound insight: 'Emptiness' is not 'nothingness' -- 'emptiness' is fullness of potential")
        print("="*70)

# Run
virtual_sim = VirtualParticleSimulator()
virtual_sim.visualize_vacuum_fluctuations()

def visualize_eight_consciousnesses():
    """Visualize the eight-consciousness structure of Yogacara Buddhism"""

    fig = plt.figure(figsize=(18, 12))

    # === Eight-consciousness hierarchy ===
    ax1 = fig.add_subplot(2, 2, (1, 2))
    ax1.axis('off')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    consciousnesses = [
        (9, '8th Consciousness\nAlaya-vijnana\n(Storehouse)', 'gold', 2.5, 'All-Seed Consciousness\nFundamental Ground'),
        (7.5, '7th Consciousness\nManas', 'orange', 2.0, 'Constant Self-Grasping\nRoot of Ego'),
        (6, '6th Consciousness\nMental Consciousness', 'red', 1.8, 'Thinking, Judgment\nMemory, Imagination'),
        (4.8, 'Eye', 'lightblue', 0.8, 'Vision'),
        (4.0, 'Ear', 'lightblue', 0.8, 'Hearing'),
        (3.2, 'Nose', 'lightblue', 0.8, 'Smell'),
        (2.4, 'Tongue', 'lightblue', 0.8, 'Taste'),
        (1.6, 'Body', 'lightblue', 0.8, 'Touch'),
    ]

    for y, label, color, width, description in consciousnesses:
        rect = plt.Rectangle((5-width/2, y-0.3), width, 0.6,
                            facecolor=color, edgecolor='black',
                            linewidth=2, alpha=0.7)
        ax1.add_patch(rect)
        ax1.text(5, y, label, ha='center', va='center',
                fontsize=11, fontweight='bold')
        ax1.text(8, y, description, ha='left', va='center',
                fontsize=9,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Arrows: first five consciousnesses -> sixth consciousness
    for y in [4.8, 4.0, 3.2, 2.4, 1.6]:
        ax1.annotate('', xy=(5, 6), xytext=(5.5, y),
                    arrowprops=dict(arrowstyle='->', lw=1.5,
                                  color='blue', alpha=0.5))
    # Sixth <-> Seventh <-> Eighth
    ax1.annotate('', xy=(5, 7.5), xytext=(5, 6.3),
                arrowprops=dict(arrowstyle='<->', lw=2, color='red', alpha=0.6))
    ax1.annotate('', xy=(5, 9), xytext=(5, 7.8),
                arrowprops=dict(arrowstyle='<->', lw=2, color='purple', alpha=0.6))

    ax1.set_title('Yogacara: Hierarchy of the Eight Consciousnesses', fontsize=16, fontweight='bold')

    # === Three Transformations diagram ===
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    circle_center = plt.Circle((0.5, 0.7), 0.15, color='gold', alpha=0.7,
                              edgecolor='black', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.7, 'Alaya-vijnana\n8th Consc.', ha='center', va='center',
            fontsize=11, fontweight='bold')

    # Maturation transformation
    ax2.annotate('', xy=(0.2, 0.4), xytext=(0.4, 0.6),
                arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
    ax2.text(0.2, 0.4, 'Body &\nWorld', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.text(0.1, 0.55, 'Maturation\n(Manifests World)', ha='center', fontsize=8, color='blue')

    # Deliberative transformation
    circle_manas = plt.Circle((0.8, 0.7), 0.1, color='orange', alpha=0.6,
                             edgecolor='black', linewidth=2)
    ax2.add_patch(circle_manas)
    ax2.text(0.8, 0.7, 'Manas\n7th Consc.', ha='center', va='center', fontsize=9)
    ax2.annotate('', xy=(0.8, 0.7), xytext=(0.65, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax2.text(0.725, 0.75, 'Deliberation\n(Grasps Self)', ha='center', fontsize=8, color='red')

    # Object-apprehending transformation
    ax2.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='green'))
    ax2.text(0.5, 0.3, 'First Six\nConsc.', ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.6, 0.42, 'Apprehension\n(Cognizes Objects)', ha='center', fontsize=8, color='green')

    ax2.set_title('Three Transformations: How Consciousness Manifests Reality', fontsize=13, fontweight='bold')

    # === Seed-Manifestation cycle ===
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    rect_alaya = plt.Rectangle((0.2, 0.6), 0.6, 0.3,
                               facecolor='gold', edgecolor='black',
                               linewidth=3, alpha=0.6)
    ax3.add_patch(rect_alaya)
    ax3.text(0.5, 0.75, 'Alaya-vijnana (Seed Repository)', ha='center',
            fontsize=12, fontweight='bold')

    seed_positions = [(0.3, 0.7), (0.4, 0.65), (0.5, 0.7), (0.6, 0.65), (0.7, 0.7)]
    for x, y in seed_positions:
        circle = plt.Circle((x, y), 0.03, color='brown', alpha=0.8)
        ax3.add_patch(circle)
        ax3.text(x, y, 'S', ha='center', va='center', fontsize=7, color='white')

    ax3.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.6),
                arrowprops=dict(arrowstyle='->', lw=4, color='blue'))
    ax3.text(0.6, 0.5, 'Seeds Ripen\ninto Manifestation', ha='left', fontsize=11, color='blue',
            fontweight='bold')

    manifestations = [
        (0.2, 0.3, 'Form'), (0.35, 0.25, 'Sound'), (0.5, 0.3, 'Smell'),
        (0.65, 0.25, 'Taste'), (0.8, 0.3, 'Touch'),
    ]
    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.05, color='lightgreen', alpha=0.8,
                           edgecolor='darkgreen', linewidth=2)
        ax3.add_patch(circle)
        ax3.text(x, y, label, ha='center', va='center', fontsize=10)

    ax3.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.4),
                arrowprops=dict(arrowstyle='->', lw=4, color='red',
                              connectionstyle="arc3,rad=.5"))
    ax3.text(0.3, 0.5, 'Manifestation\nPerfumes New Seeds', ha='right', fontsize=11, color='red',
            fontweight='bold')
    ax3.set_title('Seeds and Manifestation: The Endless Cycle', fontsize=13, fontweight='bold')
    ax3.text(0.5, 0.05, 'Seeds -> Manifestation -> New Seeds -> Manifestation ...',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('eight_consciousnesses.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[The Eight Consciousnesses of Yogacara]")
    print("="*70)
    print("\nFirst five: Eye, Ear, Nose, Tongue, Body (sensory consciousnesses)")
    print("Sixth: Mental consciousness (thinking, judgment, memory)")
    print("Seventh: Manas (constant self-grasping, root of ego)")
    print("Eighth: Alaya-vijnana (storehouse consciousness, source of all phenomena)")
    print("\nThree Transformations:")
    print("  1. Maturation (8th) -> manifests body and world")
    print("  2. Deliberation (7th) -> grasps 'self'")
    print("  3. Apprehension (first six) -> cognizes objects")
    print("\nSeed-Manifestation cycle: Seeds -> Manifestation -> New Seeds -> ...")
    print("\nQuantum analogy:")
    print("  Alaya-vijnana ~ quantum field | Seeds ~ field excitation modes")
    print("  Manifestation ~ actual particles | Perfuming ~ field evolution")
    print("="*70)

# Run
visualize_eight_consciousnesses()

def visualize_mind_matter_debate():
    """Visualize the mind-matter debate through a quantum lens"""

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Materialism (classical) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, 'Materialism (Classical Physics)', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_matter = plt.Circle((0.3, 0.5), 0.15, color='blue', alpha=0.6,
                              edgecolor='black', linewidth=3)
    ax.add_patch(circle_matter)
    ax.text(0.3, 0.5, 'Matter\n(Objective)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_mind = plt.Circle((0.7, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='black', linewidth=2)
    ax.add_patch(circle_mind)
    ax.text(0.7, 0.5, 'Mind\n(Subjective)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, 'Determines', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, 'Matter is fundamental; mind is a byproduct',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
           transform=ax.transAxes)

    # === Idealism (classical) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, 'Idealism (Classical Philosophy)', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_mind = plt.Circle((0.3, 0.5), 0.15, color='red', alpha=0.6,
                            edgecolor='black', linewidth=3)
    ax.add_patch(circle_mind)
    ax.text(0.3, 0.5, 'Mind\n(Substance)', ha='center', va='center',
           fontsize=12, fontweight='bold')
    circle_matter = plt.Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                              edgecolor='black', linewidth=2)
    ax.add_patch(circle_matter)
    ax.text(0.7, 0.5, 'Matter\n(Appearance)', ha='center', va='center', fontsize=10)
    ax.annotate('', xy=(0.6, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(0.525, 0.55, 'Manifests', ha='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.1, 'Mind is fundamental; matter is a manifestation of mind',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
           transform=ax.transAxes)

    # === Quantum Mechanics ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, 'Quantum Mechanics', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle1 = plt.Circle((0.45, 0.55), 0.12, color='red', alpha=0.4,
                        edgecolor='red', linewidth=2)
    circle2 = plt.Circle((0.55, 0.45), 0.12, color='blue', alpha=0.4,
                        edgecolor='blue', linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.text(0.45, 0.55, 'Observer', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.text(0.55, 0.45, 'System', ha='center', va='center',
           fontsize=11, fontweight='bold')
    ax.annotate('', xy=(0.55, 0.5), xytext=(0.45, 0.5),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.25, 'Observation affects the system\nThe system also affects observation', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(0.5, 0.05, 'Mind and matter are inseparable',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
           transform=ax.transAxes)

    # === Yogacara ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.9, 'Yogacara Buddhism', ha='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)

    circle_consciousness = plt.Circle((0.5, 0.5), 0.18, color='gold', alpha=0.6,
                                     edgecolor='black', linewidth=3)
    ax.add_patch(circle_consciousness)
    ax.text(0.5, 0.5, 'Consciousness\n(Alaya-vijnana)', ha='center', va='center',
           fontsize=12, fontweight='bold')

    manifestations = [
        (0.3, 0.75, 'Form'), (0.7, 0.75, 'Sound'), (0.25, 0.5, 'Smell'),
        (0.75, 0.5, 'Taste'), (0.3, 0.25, 'Touch'), (0.7, 0.25, 'Mental\nObjects'),
    ]
    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.06, color='lightblue', alpha=0.7,
                           edgecolor='blue', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)

        dx = x - 0.5
        dy = y - 0.5
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length
        dy_norm = dy / length
        start_x = 0.5 + dx_norm * 0.18
        start_y = 0.5 + dy_norm * 0.18
        end_x = x - dx_norm * 0.06
        end_y = y - dy_norm * 0.06
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='purple', alpha=0.6))

    ax.text(0.5, 0.05, 'All phenomena are consciousness-only\nEverything is a manifestation of mind',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
           transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('mind_matter_debate.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Mind vs. Matter: Quantum and Yogacara Perspectives]")
    print("="*70)
    print("\nMaterialism: Matter determines consciousness; objective reality is independent of the observer")
    print("Idealism: Mind is the only reality; matter is a manifestation of mind")
    print("Quantum Mechanics: The observer affects the system; mind and matter cannot be separated")
    print("Yogacara: The three realms are mind alone; all phenomena are consciousness-only")
    print("\nShared insight of QFT and Yogacara:")
    print("  Field/consciousness is the ground; particles/phenomena are appearances")
    print("  There are no particles independent of the field; no phenomena independent of consciousness")
    print("\nA possible answer:")
    print("  Neither 'matter' nor 'mind' is the most fundamental")
    print("  What is fundamental is 'field / consciousness'")
    print("  The two may be different facets of the same reality")
    print("="*70)

# Run
visualize_mind_matter_debate()
