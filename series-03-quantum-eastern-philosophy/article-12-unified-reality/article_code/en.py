# Code & Cogito: Conclusion — Toward a Unified View of Reality
# Article: https://code-cogito.com/en/unified-view-reality-conclusion-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class RelationalOntologyVisualizer:
    """
    Relational Ontology Visualization
    Demonstrates: relationships are prior to entities
    """

    def __init__(self):
        pass

    def visualize_ontologies(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === Top-left: Western substance ontology ===
        ax = axes[0, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        entities = ['A', 'B', 'C', 'D']
        positions = [(0.2, 0.7), (0.8, 0.7), (0.2, 0.3), (0.8, 0.3)]

        for entity, pos in zip(entities, positions):
            circle = Circle(pos, 0.12, facecolor='lightblue',
                          edgecolor='blue', linewidth=3)
            ax.add_patch(circle)
            ax.text(pos[0], pos[1], entity, ha='center', va='center',
                   fontsize=16, fontweight='bold')
            ax.text(pos[0], pos[1]-0.18, f'Property_{entity}', ha='center',
                   fontsize=9, style='italic', color='gray')

        ax.plot([0.2, 0.8], [0.7, 0.7], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)
        ax.plot([0.2, 0.8], [0.3, 0.3], 'gray', linestyle='--',
               linewidth=1.5, alpha=0.3)

        ax.text(0.5, 0.95, 'Western Substance Ontology', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, 'Substances are primary\nRelations are secondary',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Top-right: Eastern/Quantum relational ontology ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        G = nx.complete_graph(6)
        pos_network = nx.spring_layout(G, center=(0.5, 0.5), k=0.3, seed=42)

        for edge in G.edges():
            x_coords = [pos_network[edge[0]][0], pos_network[edge[1]][0]]
            y_coords = [pos_network[edge[0]][1], pos_network[edge[1]][1]]
            ax.plot(x_coords, y_coords, 'purple', linewidth=3, alpha=0.5)

        for node, pos in pos_network.items():
            circle = Circle(pos, 0.05, facecolor='lightgreen',
                          edgecolor='darkgreen', linewidth=2, alpha=0.7)
            ax.add_patch(circle)

        ax.text(0.5, 0.95, 'Eastern/Quantum Relational Ontology', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.05, 'Relations are primary\nEntities emerge from relations',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Bottom-left: Quantum entanglement example ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        circle1 = Circle((0.3, 0.5), 0.1, facecolor='red',
                        edgecolor='darkred', linewidth=3, alpha=0.6)
        circle2 = Circle((0.7, 0.5), 0.1, facecolor='blue',
                        edgecolor='darkblue', linewidth=3, alpha=0.6)
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        ax.text(0.3, 0.5, 'Particle 1', ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')
        ax.text(0.7, 0.5, 'Particle 2', ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        x = np.linspace(0.3, 0.7, 100)
        y = 0.5 + 0.05 * np.sin(20 * (x - 0.3))
        ax.plot(x, y, 'purple', linewidth=4, alpha=0.7)

        ax.text(0.5, 0.62, 'Entangled', ha='center', fontsize=11,
               fontweight='bold', color='purple')
        ax.text(0.5, 0.8, 'Quantum Entanglement: Inseparable', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.15, '|psi> = (|01> + |10>) / sqrt(2)\nCannot be written as |psi_1> x |psi_2>\nParticles have no independent states',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Bottom-right: Dependent origination example ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        causes = ['Ignorance', 'Formation', 'Consciousness', 'Name-Form',
                  'Six Senses', 'Contact', 'Feeling', 'Craving',
                  'Clinging', 'Becoming', 'Birth', 'Aging-Death']
        n = len(causes)
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)

        radius = 0.35
        for i, (cause, angle) in enumerate(zip(causes, angles)):
            x = 0.5 + radius * np.cos(angle)
            y = 0.5 + radius * np.sin(angle)

            circle = Circle((x, y), 0.05, facecolor='orange',
                          edgecolor='darkorange', linewidth=2, alpha=0.7)
            ax.add_patch(circle)
            ax.text(x, y, cause, ha='center', va='center',
                   fontsize=6, fontweight='bold')

            next_angle = angles[(i+1) % n]
            x_next = 0.5 + radius * np.cos(next_angle)
            y_next = 0.5 + radius * np.sin(next_angle)

            arrow = FancyArrowPatch((x, y), (x_next, y_next),
                                   arrowstyle='->', mutation_scale=15,
                                   linewidth=2, color='darkorange', alpha=0.5)
            ax.add_patch(arrow)

        ax.text(0.5, 0.95, 'Buddhist Dependent Origination: Mutual Dependence', ha='center',
               fontsize=13, fontweight='bold')
        ax.text(0.5, 0.08, '"When this exists, that comes to be"\nNothing exists in isolation',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, 'Pattern 1: The Relational Nature of Reality',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('relational_ontology.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Pattern 1: The Relational Nature of Reality]")
        print("="*70)

        print("\nWestern traditional ontology (a long-standing mainstream strand since Aristotle):")
        print("  - Substance is primary")
        print("  - Attributes belong to substances")
        print("  - Relations are secondary")
        print("  - Example: 'Socrates is a human'")
        print("    -> Socrates (substance) has 'humanity' (attribute)")

        print("\nThe quantum mechanical challenge:")
        print("  - Entangled particles have no independent states of their own")
        print("  - Quantum entanglement: |psi> != |psi_1> x |psi_2>")
        print("  - Entangled particles cannot be described independently")
        print("  - Relations are prior to entities")

        print("\nInsights from Eastern philosophy:")
        print("  - Buddhist sunyata: all things lack inherent self-nature")
        print("  - Dependent origination: 'when this exists, that comes to be'")
        print("  - Huayan: one is all, all is one")
        print("  - No independently existing 'substance'")

        print("\nShared conclusion:")
        print("  Reality is not composed of 'independent entities'")
        print("  It is composed of 'relationships'")
        print("  Relations are primary; entities 'emerge' from relations")

        print("\nPhilosophical significance:")
        print("  - This challenges one long-standing strand of Western metaphysics")
        print("  - It calls for 'relational ontology'")
        print("  - Eastern philosophy has similar relational ideas (the author's analogy)")
        print("  - Some interpretations of quantum mechanics resonate with it, but physics has not confirmed a philosophical thesis")

        print("\nPractical significance:")
        print("  - We are one with the world")
        print("  - There is no independent 'self'")
        print("  - To harm others is to harm oneself")
        print("  - A foundation for environmental ethics")
        print("="*70)

# Run
visualizer = RelationalOntologyVisualizer()
visualizer.visualize_ontologies()

class ParticipationVisualizer:
    """
    Participatory Reality Visualization
    Demonstrates: the observer is not external
    """

    def __init__(self):
        pass

    def visualize_observer_roles(self):
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))

        # === Top-left: Classical physics — objective realism ===
        ax = axes[0, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        world_rect = FancyBboxPatch((0.3, 0.4), 0.4, 0.3,
                                   boxstyle="round,pad=0.02",
                                   facecolor='lightblue', alpha=0.7,
                                   edgecolor='blue', linewidth=3)
        ax.add_patch(world_rect)
        ax.text(0.5, 0.55, 'The World\n(Objective Reality)', ha='center', va='center',
               fontsize=12, fontweight='bold')

        observer_circle = Circle((0.5, 0.15), 0.08, facecolor='yellow',
                                edgecolor='orange', linewidth=3, alpha=0.8)
        ax.add_patch(observer_circle)
        ax.text(0.5, 0.15, 'Observer', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow = FancyArrowPatch((0.5, 0.4), (0.5, 0.23),
                               arrowstyle='->', mutation_scale=30,
                               linewidth=3, color='green')
        ax.add_patch(arrow)
        ax.text(0.55, 0.32, 'Information', ha='left', fontsize=10, color='green')

        ax.text(0.5, 0.9, 'Classical Physics: Objective Realism', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.02, 'The world is independent of observers\n"Objective" description is possible',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Top-right: Quantum mechanics — participatory realism ===
        ax = axes[0, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_circle = Circle((0.5, 0.5), 0.4, facecolor='lightgreen',
                           alpha=0.2, edgecolor='green', linewidth=3)
        ax.add_patch(big_circle)
        ax.text(0.5, 0.88, 'Total System', ha='center', fontsize=11,
               fontweight='bold', color='green')

        system_circle = Circle((0.4, 0.55), 0.15, facecolor='lightblue',
                              edgecolor='blue', linewidth=3, alpha=0.7)
        ax.add_patch(system_circle)
        ax.text(0.4, 0.55, 'Quantum\nSystem', ha='center', va='center',
               fontsize=10, fontweight='bold')

        observer_circle2 = Circle((0.6, 0.45), 0.15, facecolor='yellow',
                                 edgecolor='orange', linewidth=3, alpha=0.7)
        ax.add_patch(observer_circle2)
        ax.text(0.6, 0.45, 'Observer', ha='center', va='center',
               fontsize=10, fontweight='bold')

        arrow1 = FancyArrowPatch((0.4, 0.55), (0.6, 0.45),
                                arrowstyle='<->', mutation_scale=20,
                                linewidth=3, color='purple')
        ax.add_patch(arrow1)
        ax.text(0.5, 0.52, 'Interaction', ha='center', fontsize=9,
               color='purple', fontweight='bold')

        ax.text(0.5, 0.9, 'Quantum Mechanics: Participatory Realism', ha='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.08, 'Apparatus and system are inseparable\nResults depend on the experimental setup',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Bottom-left: Idealism (incorrect interpretation) ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        big_brain = Circle((0.5, 0.6), 0.25, facecolor='pink',
                          edgecolor='red', linewidth=3, alpha=0.6)
        ax.add_patch(big_brain)
        ax.text(0.5, 0.6, 'Mind', ha='center', va='center',
               fontsize=14, fontweight='bold')

        small_world = Circle((0.5, 0.3), 0.08, facecolor='lightblue',
                           edgecolor='blue', linewidth=2, alpha=0.6)
        ax.add_patch(small_world)
        ax.text(0.5, 0.3, 'World', ha='center', va='center',
               fontsize=8)

        arrow2 = FancyArrowPatch((0.5, 0.5), (0.5, 0.38),
                                arrowstyle='->', mutation_scale=25,
                                linewidth=3, color='red')
        ax.add_patch(arrow2)

        ax.text(0.5, 0.9, 'Idealism (Incorrect Interpretation)', ha='center',
               fontsize=14, fontweight='bold', color='red')
        ax.text(0.5, 0.08, 'The world is created by the mind\nThis is NOT what quantum mechanics says!',
               ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Bottom-right: The correct understanding ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        theta = np.linspace(0, 2*np.pi, 100)
        r = 0.3
        x_circle = 0.5 + r * np.cos(theta)
        y_circle = 0.5 + r * np.sin(theta)

        ax.fill_between(x_circle[25:75], y_circle[25:75], 0.5,
                       color='yellow', alpha=0.6)
        ax.fill_between(x_circle[:25], 0.5, y_circle[:25],
                       color='lightblue', alpha=0.6)
        ax.fill_between(x_circle[75:], 0.5, y_circle[75:],
                       color='lightblue', alpha=0.6)

        circle_outline = Circle((0.5, 0.5), 0.3, fill=False,
                               edgecolor='black', linewidth=3)
        ax.add_patch(circle_outline)

        ax.text(0.35, 0.5, 'Mind', ha='center', va='center',
               fontsize=14, fontweight='bold')
        ax.text(0.65, 0.5, 'Matter', ha='center', va='center',
               fontsize=14, fontweight='bold')
        ax.text(0.5, 0.5, 'Not-Two', ha='center', va='center',
               fontsize=11, fontweight='bold', color='purple')

        ax.text(0.5, 0.9, 'Correct Understanding: Mind-Matter Non-Duality', ha='center',
               fontsize=14, fontweight='bold', color='purple')
        ax.text(0.5, 0.12, 'Mind and matter are mutually dependent\nInseparable\nThe shared insight of QM and Eastern philosophy',
               ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        fig.text(0.5, 0.98, 'Pattern 2: The Participatory Role of the Observer',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('participatory_reality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Pattern 2: The Participatory Role of the Observer]")
        print("="*70)

        print("\nAssumptions of classical physics:")
        print("  - The world exists independently of the observer")
        print("  - The observer can describe the world 'objectively'")
        print("  - Observation does not change the observed")
        print("  - 'Mind' and 'matter' are completely separate")

        print("\nDiscoveries of quantum mechanics:")
        print("  - Measurement changes the system")
        print("  - Apparatus and system are inseparable (no conscious observer is required)")
        print("  - Properties cannot be discussed independently of observation")
        print("  - Bohr's position: quantum phenomena can be described unambiguously only together with the whole experimental arrangement")

        print("\nInsights from Eastern philosophy:")
        print("  - Wang Yangming: 'There are no things outside the mind'")
        print("  - Kyoto School: subject and object are not-two")
        print("  - Zen: the observer and the observed are not-two")
        print("  - Huayan: principle and phenomena interpenetrate without obstruction")

        print("\nImportant clarification:")
        print("  This does NOT mean 'the world is created by the mind' (idealism)")
        print("  Rather, it means 'mind and matter are inseparable'")
        print("  Just as quantum mechanics does NOT say 'consciousness creates reality'")
        print("  But rather 'what can be said depends on the whole experimental arrangement'")

        print("\nJohn Wheeler:")
        print("  'Participatory Universe'")
        print("  - The observer is a participant in the universe")
        print("  - Not an external spectator")
        print("  - On Wheeler's proposal, our questions and their recorded answers help shape reality (speculative, not a consensus view)")
        print("="*70)

# Run
participation_viz = ParticipationVisualizer()
participation_viz.visualize_observer_roles()

class BeyondDualityVisualizer:
    """
    Beyond Duality Visualization
    Demonstrates: descriptions beyond either/or thinking
    """

    def __init__(self):
        pass

    def visualize_beyond_duality(self):
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Classical binary logic ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.axis('off')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        circle_A = Circle((0.3, 0.5), 0.15, facecolor='blue',
                         edgecolor='darkblue', linewidth=3, alpha=0.7)
        circle_not_A = Circle((0.7, 0.5), 0.15, facecolor='red',
                             edgecolor='darkred', linewidth=3, alpha=0.7)
        ax1.add_patch(circle_A)
        ax1.add_patch(circle_not_A)

        ax1.text(0.3, 0.5, 'A', ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')
        ax1.text(0.7, 0.5, 'Not-A', ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')
        ax1.text(0.5, 0.5, 'or', ha='center', va='center',
                fontsize=12, fontweight='bold')

        ax1.text(0.5, 0.85, 'Classical Logic\nExcluded Middle', ha='center',
                fontsize=12, fontweight='bold')
        ax1.text(0.5, 0.12, 'A or Not-A\nCannot be both A and Not-A',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

        # === Panel 2: Quantum superposition ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        circle_A2 = Circle((0.4, 0.5), 0.18, facecolor='blue',
                          edgecolor='darkblue', linewidth=3, alpha=0.5)
        circle_not_A2 = Circle((0.6, 0.5), 0.18, facecolor='red',
                              edgecolor='darkred', linewidth=3, alpha=0.5)
        ax2.add_patch(circle_A2)
        ax2.add_patch(circle_not_A2)

        ax2.text(0.35, 0.5, '|0>', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.65, 0.5, '|1>', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax2.text(0.5, 0.5, 'Super-\nposition', ha='center', va='center',
                fontsize=10, fontweight='bold', color='purple')

        ax2.text(0.5, 0.85, 'Quantum Superposition\nBeyond Excluded Middle', ha='center',
                fontsize=12, fontweight='bold')
        ax2.text(0.5, 0.12, '|psi> = alpha|0> + beta|1>\nA superposition of 0 and 1',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

        # === Panel 3: Zen non-duality ===
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.axis('off')
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)

        circle_you = Circle((0.4, 0.5), 0.18, facecolor='yellow',
                          edgecolor='orange', linewidth=3, alpha=0.4)
        circle_wu = Circle((0.6, 0.5), 0.18, facecolor='white',
                          edgecolor='gray', linewidth=3, alpha=0.4)
        ax3.add_patch(circle_you)
        ax3.add_patch(circle_wu)

        ax3.text(0.35, 0.5, 'Being', ha='center', va='center',
                fontsize=16, fontweight='bold')
        ax3.text(0.65, 0.5, 'Non-\nBeing', ha='center', va='center',
                fontsize=14, fontweight='bold')
        ax3.text(0.5, 0.5, 'Not-Two', ha='center', va='center',
                fontsize=12, fontweight='bold', color='gold')

        ax3.text(0.5, 0.85, 'Zen Non-Duality\nBeyond Opposites', ha='center',
                fontsize=12, fontweight='bold')
        ax3.text(0.5, 0.12, 'Neither being nor non-being\nBoth being and non-being',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Panel 4: Wave-particle duality ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)

        x_wave = np.linspace(0.1, 0.45, 100)
        y_wave = 0.5 + 0.1 * np.sin(20 * x_wave)
        ax4.plot(x_wave, y_wave, 'b-', linewidth=3)
        ax4.text(0.275, 0.35, 'Wave', ha='center', fontsize=12,
                fontweight='bold', color='blue')

        ax4.scatter([0.65, 0.75, 0.85], [0.5, 0.55, 0.45],
                   s=200, c='red', edgecolors='darkred', linewidths=2)
        ax4.text(0.75, 0.35, 'Particle', ha='center', fontsize=12,
                fontweight='bold', color='red')

        ax4.text(0.5, 0.5, '=', ha='center', va='center',
                fontsize=20, fontweight='bold')

        ax4.text(0.5, 0.85, 'Wave-Particle Duality', ha='center',
                fontsize=12, fontweight='bold')
        ax4.text(0.5, 0.12, 'Wave or particle behaviour\nComplementarity',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # === Panel 5: Form is emptiness ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')
        ax5.set_xlim(0, 1)
        ax5.set_ylim(0, 1)

        square = plt.Rectangle((0.15, 0.4), 0.2, 0.2,
                               facecolor='orange', alpha=0.7,
                               edgecolor='darkorange', linewidth=3)
        ax5.add_patch(square)
        ax5.text(0.25, 0.5, 'Form', ha='center', va='center',
                fontsize=16, fontweight='bold')

        circle_empty = Circle((0.75, 0.5), 0.12, facecolor='white',
                             edgecolor='black', linewidth=3, linestyle='--')
        ax5.add_patch(circle_empty)
        ax5.text(0.75, 0.5, 'Emptiness', ha='center', va='center',
                fontsize=13, fontweight='bold')

        ax5.annotate('', xy=(0.63, 0.5), xytext=(0.35, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
        ax5.text(0.49, 0.55, 'is', ha='center', fontsize=10,
                color='purple', fontweight='bold')

        ax5.text(0.5, 0.85, 'Form Is Emptiness', ha='center',
                fontsize=12, fontweight='bold')
        ax5.text(0.5, 0.12, 'Phenomenon is essence\nEssence is phenomenon',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Panel 6: Summary ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        summary_text = (
            "[Beyond Binary Opposition]\n\n"
            "Classical logic (Aristotle):\n"
            "  Excluded middle: A or Not-A\n"
            "  Non-contradiction: not both A and Not-A\n\n"
            "Quantum Mechanics & Eastern Philosophy:\n\n"
            "  Quantum: superposition, wave-particle duality\n"
            "  Zen: neither being nor non-being\n"
            "  Buddhism: form is emptiness\n"
            "  Daoism: being and non-being arise together\n\n"
            "Shared insight:\n"
            "  Reality transcends binary logic\n"
            "  Superposition does not make a contradiction true, but black-and-white is not enough\n"
            "  This is not contradiction, but transcendence"
        )

        ax6.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=9, family='monospace',
                bbox=dict(boxstyle='round', facecolor='white',
                         alpha=0.9, edgecolor='black', linewidth=2))

        fig.text(0.5, 0.98, 'Pattern 3: Transcending Binary Opposition',
                ha='center', fontsize=16, fontweight='bold')

        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.savefig('beyond_duality.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Pattern 3: Transcending Binary Opposition]")
        print("="*70)

        print("\nClassical logic (since Aristotle):")
        print("  1. Law of Excluded Middle:")
        print("     A or Not-A (one must be true)")
        print("  2. Law of Non-Contradiction:")
        print("     Cannot be both A and Not-A")

        print("\nThe quantum mechanical challenge:")
        print("  - Wave-particle duality: light shows wave-like or particle-like behaviour depending on the experimental arrangement")
        print("  - Superposition: |psi> = alpha|0> + beta|1> (a superposition of 0 and 1)")
        print("  - Complementarity principle: wave and particle are complementary")
        print("  - Schrodinger's cat: a superposition of dead and alive before measurement (a 1935 thought experiment)")

        print("\nInsights from Eastern philosophy:")
        print("  - Zen: neither being nor non-being, both being and non-being")
        print("  - Buddhism: form is emptiness, emptiness is form")
        print("  - Daoism: being and non-being give rise to each other")
        print("  - Huayan: unobstructed interpenetration of principle and phenomena")

        print("\nNagarjuna's Middle Way (Madhyamaka):")
        print("  'Neither arising nor ceasing, neither permanent nor annihilated,")
        print("   neither one nor different, neither coming nor going.'")
        print("  -> Transcending all binary oppositions")
        print("="*70)

# Run
duality_viz = BeyondDualityVisualizer()
duality_viz.visualize_beyond_duality()

def visualize_convergence():
    """
    Visualize the convergence of science and philosophy
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

    # === Left panel: Two paths ===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    science_x = [0.2] * 10
    science_y = np.linspace(0.1, 0.7, 10)

    milestones_science = [
        (0.15, 'Blackbody Radiation\n1900'),
        (0.25, 'Matter Waves\n1924'),
        (0.35, 'Uncertainty Principle\n1927'),
        (0.45, 'Entanglement\n1935'),
        (0.55, "Bell's Inequality\n1964"),
        (0.65, 'Quantum Computing\n1980s'),
    ]

    for y, label in milestones_science:
        ax1.plot(0.2, y, 'o', markersize=12, color='blue')
        ax1.text(0.05, y, label, ha='right', fontsize=8)

    ax1.plot(science_x, science_y, 'b-', linewidth=3, alpha=0.5)
    ax1.text(0.2, 0.08, 'Scientific Path', ha='center', fontsize=12,
            fontweight='bold', color='blue')

    phil_x = [0.8] * 10
    phil_y = np.linspace(0.1, 0.7, 10)

    milestones_phil = [
        (0.15, 'The Buddha\n5th c. BCE'),
        (0.25, 'Nagarjuna\nc. 200 CE'),
        (0.35, 'Huayan School\n7th-8th c. CE'),
        (0.45, 'Zen Buddhism\nc. 700 CE'),
        (0.55, 'Wang Yangming\n1508 CE'),
        (0.65, 'Kyoto School\n1900s'),
    ]

    for y, label in milestones_phil:
        ax1.plot(0.8, y, 'o', markersize=12, color='orange')
        ax1.text(0.95, y, label, ha='left', fontsize=8)

    ax1.plot(phil_x, phil_y, color='orange', linewidth=3, alpha=0.5)
    ax1.text(0.8, 0.08, 'Philosophical/Contemplative Path', ha='center', fontsize=12,
            fontweight='bold', color='orange')

    # Convergence point
    convergence_y = 0.85
    ax1.plot([0.2, 0.5], [0.7, convergence_y], 'b-', linewidth=3)
    ax1.plot([0.8, 0.5], [0.7, convergence_y], color='orange', linewidth=3)

    ax1.scatter(0.5, convergence_y, s=500, marker='*',
               color='gold', edgecolors='black', linewidths=2, zorder=5)
    ax1.text(0.5, convergence_y, 'Convergence', ha='center', va='center',
            fontsize=11, fontweight='bold')

    ax1.text(0.5, 0.95, 'A Unified View of Reality', ha='center',
            fontsize=14, fontweight='bold', color='purple')

    ax1.set_title('The Remarkable Convergence of Two Paths', fontsize=14, fontweight='bold')

    # === Right panel: Shared insights ===
    ax2.axis('off')

    insights_text = (
        "[Three Shared Insights]\n\n"
        "1. The Relational Nature of Reality\n"
        "   Science: quantum entanglement, non-locality\n"
        "   Philosophy: dependent origination, Indra's Net\n"
        "   -> Relations are prior to entities\n\n"
        "2. The Participatory Role of the Observer\n"
        "   Science: measurement problem, wave function collapse\n"
        "   Philosophy: nothing outside the mind, non-duality\n"
        "   -> Mind and matter are inseparable\n\n"
        "3. Transcending Binary Opposition\n"
        "   Science: wave-particle duality, complementarity\n"
        "   Philosophy: non-duality, the Middle Way\n"
        "   -> A new logic is needed\n\n"
        "---\n\n"
        "Two radically different paths:\n"
        "  Science: outward observation, mathematical modeling\n"
        "  Philosophy: inward experience, conceptual reflection\n\n"
        "Arriving at similar conclusions on these three points!\n\n"
        "This suggests:\n"
        "They may be touching\n"
        "the same deep truth about reality.\n\n"
        "---\n\n"
        "But a caveat:\n"
        "  This does not mean they are identical\n"
        "  Science has verifiability\n"
        "  Philosophy has direct experience\n"
        "  The two complement, not replace, each other"
    )

    ax2.text(0.5, 0.5, insights_text, ha='center', va='center',
            fontsize=9.5, family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow',
                     alpha=0.9, edgecolor='purple', linewidth=3))

    ax2.set_title('The Truth They Share', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('paths_convergence.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[The Remarkable Convergence of Two Paths]")
    print("="*70)

    print("\nScientific path:")
    print("  Method: observation, mathematical modeling, repeatable verification")
    print("  Milestones:")
    print("    1900: Planck (blackbody radiation)")
    print("    1924: de Broglie (matter waves: duality extended to matter)")
    print("    1927: Heisenberg (uncertainty principle)")
    print("    1935: EPR paradox (entanglement)")
    print("    1964: Bell's inequality")
    print("    1980s: quantum computing")

    print("\nPhilosophical/contemplative path:")
    print("  Method: introspective meditation, philosophical reasoning, direct experience")
    print("  Milestones:")
    print("    5th century BCE: The Buddha (dependent origination; emptiness systematised later by Nagarjuna)")
    print("    c. 200 CE: Nagarjuna (Middle Way)")
    print("    7th-8th century CE: Huayan school (Indra's Net)")
    print("    c. 700 CE: Zen Buddhism (non-duality)")
    print("    1508 CE: Wang Yangming (Longchang enlightenment; mind is principle)")
    print("    1900s: Kyoto School (Nishida Kitaro)")

    print("\nA remarkable convergence:")
    print("  Two radically different paths")
    print("  arriving at similar conclusions on these three points!")
    print("="*70)

# Run
visualize_convergence()
