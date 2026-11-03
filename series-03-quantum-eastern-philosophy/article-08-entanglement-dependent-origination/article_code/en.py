# Code & Cogito: Quantum Entanglement vs. Buddhist "Dependent Origination" — Nothing Exists Alone
# Article: https://code-cogito.com/en/quantum-entanglement-vs-buddhist-dependent-origination-nothing-exists-alone-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class DependentOriginationNetwork:
    """
    Dependent Origination Network Simulator
    Demonstrates: How all things are mutually conditioned
    """

    def __init__(self):
        self.G = nx.DiGraph()

    def create_twelve_links(self):
        """
        Create the Twelve Links of Dependent Origination network
        """
        # The twelve links
        links = [
            ('Ignorance', 'Formations'),
            ('Formations', 'Consciousness'),
            ('Consciousness', 'Name & Form'),
            ('Name & Form', 'Six Senses'),
            ('Six Senses', 'Contact'),
            ('Contact', 'Feeling'),
            ('Feeling', 'Craving'),
            ('Craving', 'Clinging'),
            ('Clinging', 'Becoming'),
            ('Becoming', 'Birth'),
            ('Birth', 'Aging & Death'),
            ('Aging & Death', 'Ignorance'),  # The cycle repeats
        ]

        self.G.add_edges_from(links)

    def visualize_twelve_links(self):
        """
        Visualize the Twelve Links of Dependent Origination
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

        # === Left panel: The Twelve Links cycle ===
        self.create_twelve_links()

        # Circular layout
        pos = nx.circular_layout(self.G)

        # Node colors (by category)
        node_colors = {
            'Ignorance': 'gray',
            'Formations': 'orange',
            'Consciousness': 'yellow',
            'Name & Form': 'lightblue',
            'Six Senses': 'lightgreen',
            'Contact': 'cyan',
            'Feeling': 'pink',
            'Craving': 'red',
            'Clinging': 'darkred',
            'Becoming': 'purple',
            'Birth': 'green',
            'Aging & Death': 'black',
        }

        colors = [node_colors[node] for node in self.G.nodes()]

        # Draw the network
        nx.draw_networkx_nodes(self.G, pos, node_color=colors,
                              node_size=1500, alpha=0.8,
                              edgecolors='black', linewidths=2, ax=ax1)

        nx.draw_networkx_labels(self.G, pos, font_size=10,
                               font_weight='bold', ax=ax1)

        nx.draw_networkx_edges(self.G, pos, edge_color='gray',
                              arrows=True, arrowsize=20, arrowstyle='->',
                              width=2, connectionstyle='arc3,rad=0.1', ax=ax1)

        ax1.set_title('The Twelve Links: The Mechanism of Cyclic Existence\n'
                     '"When this exists, that comes to be"',
                     fontsize=14, fontweight='bold')
        ax1.axis('off')

        # Add explanation
        explanation = '''
        The Twelve Links:

        1. Ignorance -> 2. Formations -> 3. Consciousness
        -> 4. Name & Form -> 5. Six Senses -> 6. Contact
        -> 7. Feeling -> 8. Craving -> 9. Clinging
        -> 10. Becoming -> 11. Birth -> 12. Aging & Death
        -> 1. Ignorance (the cycle repeats)

        Break any single link -> the entire chain collapses
        '''

        ax1.text(0.5, -1.3, explanation, ha='center', fontsize=10,
                transform=ax1.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === Right panel: Interdependence network ===

        # Create a more complex interdependence network
        elements = ['Water', 'Fire', 'Wood', 'Earth', 'Metal',
                    'Humans', 'Animals', 'Plants']
        G2 = nx.DiGraph()

        # Interdependence relations
        relations = [
            ('Water', 'Plants'), ('Water', 'Animals'), ('Water', 'Humans'),
            ('Fire', 'Humans'), ('Fire', 'Earth'),
            ('Wood', 'Fire'), ('Wood', 'Humans'),
            ('Earth', 'Plants'), ('Earth', 'Wood'),
            ('Metal', 'Humans'), ('Metal', 'Water'),
            ('Humans', 'Fire'), ('Humans', 'Wood'), ('Humans', 'Metal'),
            ('Animals', 'Humans'), ('Animals', 'Earth'),
            ('Plants', 'Animals'), ('Plants', 'Humans'), ('Plants', 'Earth'),
            ('Plants', 'Water'),  # Cycle
            ('Animals', 'Water'),  # Cycle
        ]

        G2.add_edges_from(relations)

        # Force-directed layout
        pos2 = nx.spring_layout(G2, k=2, iterations=50, seed=42)

        # Draw
        nx.draw_networkx_nodes(G2, pos2, node_color='lightblue',
                              node_size=2000, alpha=0.8,
                              edgecolors='darkblue', linewidths=2, ax=ax2)

        nx.draw_networkx_labels(G2, pos2, font_size=12,
                               font_weight='bold', ax=ax2)

        nx.draw_networkx_edges(G2, pos2, edge_color='gray', alpha=0.5,
                              arrows=True, arrowsize=15, arrowstyle='->',
                              width=1.5, connectionstyle='arc3,rad=0.2', ax=ax2)

        ax2.set_title('Universal Interdependence\n'
                     '"All phenomena are mutually conditioned"',
                     fontsize=14, fontweight='bold')
        ax2.axis('off')

        ax2.text(0.5, -0.1, 'Nothing exists in isolation\n'
                'Every element depends on others',
                ha='center', fontsize=11, transform=ax2.transAxes,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        plt.tight_layout()
        plt.savefig('dependent_origination_network.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("DEPENDENT ORIGINATION: This Being, That Becomes")
        print("="*70)

        print("\nThe Buddha's teaching:")
        print("  'When this exists, that comes to be;")
        print("   with the arising of this, that arises.'")
        print("  'When this does not exist, that does not come to be;")
        print("   with the cessation of this, that ceases.'")

        print("\nMeaning:")
        print("  - Because this exists, that exists")
        print("  - Because this does not exist, that does not exist")
        print("  - All phenomena are mutually conditioned")
        print("  - Nothing exists in isolation")

        print("\nThe Twelve Links:")
        print("  1. Ignorance (avidya)")
        print("  2. Formations (samskara)")
        print("  3. Consciousness (vijnana)")
        print("  4. Name-and-Form (namarupa)")
        print("  5. Six Sense Bases (sadayatana)")
        print("  6. Contact (sparsa)")
        print("  7. Feeling (vedana)")
        print("  8. Craving (trsna)")
        print("  9. Clinging (upadana)")
        print("  10. Becoming (bhava)")
        print("  11. Birth (jati)")
        print("  12. Aging & Death (jaramarana)")

        print("\nKey insights:")
        print("  - Each link depends on the one before it")
        print("  - Break any single link -> the entire chain collapses")
        print("  - Ignorance ceases -> Formations cease -> ... -> Aging & Death ceases")
        print("  - This is nirvana")

        print("\nModern examples:")
        print("  - Water depends on hydrogen and oxygen")
        print("  - Plants depend on water, sunlight, and soil")
        print("  - Animals depend on plants")
        print("  - Humans depend on animals, plants, water...")
        print("  - Everything is interdependent")

        print("\nPhilosophical implications:")
        print("  - 'Existence' is not absolute")
        print("  - 'Existence' is relational and dependent")
        print("  - Nothing has an independent 'intrinsic nature'")
        print("="*70)

# Run
network = DependentOriginationNetwork()
network.visualize_twelve_links()

class QuantumEntanglementOntology:
    """
    Quantum Entanglement and Relational Ontology
    Demonstrates: How parts cannot be separated from the whole
    """

    def __init__(self):
        pass

    def visualize_entanglement_ontology(self):
        """
        Visualize the ontological implications of entanglement
        """
        fig = plt.figure(figsize=(18, 12))

        # === Panel 1: Classical substance ontology ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')

        ax1.text(0.5, 0.95, 'Classical Substance Ontology', ha='center',
                fontsize=14, fontweight='bold', transform=ax1.transAxes)

        # Two independent particles
        circle_A = plt.Circle((0.3, 0.5), 0.12, color='red', alpha=0.6,
                             edgecolor='black', linewidth=3)
        circle_B = plt.Circle((0.7, 0.5), 0.12, color='blue', alpha=0.6,
                             edgecolor='black', linewidth=3)
        ax1.add_patch(circle_A)
        ax1.add_patch(circle_B)

        ax1.text(0.3, 0.5, 'Particle A\nIntrinsic\nnature', ha='center', va='center',
                fontsize=10, fontweight='bold')
        ax1.text(0.7, 0.5, 'Particle B\nIntrinsic\nnature', ha='center', va='center',
                fontsize=10, fontweight='bold')

        ax1.text(0.5, 0.2, 'Particles exist independently\nwith fixed properties', ha='center',
                fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
                transform=ax1.transAxes)

        # === Panel 2: Quantum relational ontology ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')

        ax2.text(0.5, 0.95, 'Quantum Relational Ontology', ha='center',
                fontsize=14, fontweight='bold', transform=ax2.transAxes)

        # Entangled state: a whole
        ellipse = plt.matplotlib.patches.Ellipse((0.5, 0.5), 0.7, 0.4,
                                                 color='purple', alpha=0.3,
                                                 edgecolor='purple', linewidth=3)
        ax2.add_patch(ellipse)

        circle_A2 = plt.Circle((0.35, 0.5), 0.08, color='red', alpha=0.5,
                              edgecolor='red', linewidth=2)
        circle_B2 = plt.Circle((0.65, 0.5), 0.08, color='blue', alpha=0.5,
                              edgecolor='blue', linewidth=2)
        ax2.add_patch(circle_A2)
        ax2.add_patch(circle_B2)

        ax2.text(0.35, 0.5, 'A', ha='center', va='center',
                fontsize=12, fontweight='bold')
        ax2.text(0.65, 0.5, 'B', ha='center', va='center',
                fontsize=12, fontweight='bold')

        ax2.annotate('', xy=(0.62, 0.5), xytext=(0.38, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))

        ax2.text(0.5, 0.7, 'Entangled State\n|psi>_AB', ha='center', va='center',
                fontsize=12, fontweight='bold', color='purple')

        ax2.text(0.5, 0.2, 'A and B are inseparable\nParts cannot be independently defined',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7),
                transform=ax2.transAxes)

        # === Panel 3: Buddhist dependent origination ontology ===
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')

        ax3.text(0.5, 0.95, 'Buddhist Dependent Origination', ha='center',
                fontsize=14, fontweight='bold', transform=ax3.transAxes)

        rect = plt.Rectangle((0.15, 0.3), 0.7, 0.4,
                            facecolor='gold', alpha=0.2,
                            edgecolor='gold', linewidth=3)
        ax3.add_patch(rect)

        elements = [
            (0.25, 0.55, 'D1'),
            (0.4, 0.45, 'D2'),
            (0.55, 0.6, 'D3'),
            (0.7, 0.5, 'D4'),
        ]

        for x, y, label in elements:
            circle = plt.Circle((x, y), 0.05, color='orange', alpha=0.6,
                               edgecolor='darkorange', linewidth=1.5)
            ax3.add_patch(circle)
            ax3.text(x, y, label, ha='center', va='center', fontsize=9)

        for i, (x1, y1, _) in enumerate(elements):
            for x2, y2, _ in elements[i+1:]:
                ax3.plot([x1, x2], [y1, y2], 'orange', alpha=0.3, linewidth=1.5)

        ax3.text(0.5, 0.7, 'Dharmadhatu', ha='center', va='center',
                fontsize=12, fontweight='bold', color='gold')

        ax3.text(0.5, 0.2, 'All dharmas lack intrinsic nature\n'
                'Everything is mutually conditioned',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
                transform=ax3.transAxes)

        # === Panel 4: The density matrix (mathematics) ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        text = '''
        Mathematics of Entanglement:

        Bell state:
        |psi> = (|up,down> - |down,up>)/sqrt(2)

        Reduced density matrix of particle A:
        rho_A = Tr_B(|psi><psi|)
             = (|up><up| + |down><down|)/2

        This is a mixed state, NOT a pure state!

        Implications:
        - Particle A has no definite state
        - A's state depends on the whole system AB
        - Parts cannot be separated from the whole

        Key insight:
        Relationships come before things
        '''

        ax4.text(0.1, 0.5, text, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        # === Panel 5: The formal structure of dependent origination ===
        ax5 = fig.add_subplot(2, 3, 5)
        ax5.axis('off')

        text2 = '''
        Formal Structure of Dependent Origination:

        If A exists -> B exists
        If B exists -> C exists
        If C exists -> A exists

        A <-> B <-> C <-> A (circular)

        There is no independent starting point
        There is no absolute "First Cause"

        Implications:
        - Nothing has "intrinsic nature"
        - "Existence" is relational
        - Everything arises conditionally

        Key insight:
        Dependent origination = emptiness
        '''

        ax5.text(0.1, 0.5, text2, fontsize=10, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        # === Panel 6: Comparative summary ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        comparison = '''
        ENTANGLEMENT vs. DEPENDENT ORIGINATION

        Quantum Entanglement:
        - Inseparable
        - Parts cannot be independently defined
        - Relationships before things
        - The whole is greater than the sum of parts

        Buddhist Dependent Origination:
        - Mutually conditioned
        - All dharmas lack intrinsic nature
        - Origination before existence
        - Reality is an indivisible whole

        Shared structure:
        * Rejects substance ontology
        * Affirms relational ontology
        * "Existence" is relational
        * Parts depend on the whole

        Profound insight:
        The universe is not a "collection of things"
        but a "web of relationships"
        '''

        ax6.text(0.1, 0.5, comparison, fontsize=10, va='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9,
                         edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('entanglement_ontology.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("RELATIONAL ONTOLOGY: The Shared Insight of Quantum Physics and Dependent Origination")
        print("="*70)

        print("\nClassical ontology (substance-based):")
        print("  - The universe is made of 'substances'")
        print("  - Substances have 'properties'")
        print("  - Relationships are secondary")
        print("  - Parts can be independently defined")

        print("\nQuantum ontology (relation-based):")
        print("  - The universe is a 'web of relationships'")
        print("  - There are no independent 'substances'")
        print("  - Relationships come before things")
        print("  - Parts depend on the whole")

        print("\nMathematical proof from entanglement:")
        print("  - |psi>_AB cannot be decomposed into |psi>_A tensor |psi>_B")
        print("  - Particle A's state is mixed, not pure")
        print("  - rho_A = Tr_B(|psi><psi|)")
        print("  -> Parts cannot be independently defined")

        print("\nFormal structure of dependent origination:")
        print("  - 'This being, that becomes'")
        print("  - A -> B -> C -> A (circular)")
        print("  - There is no independent starting point")
        print("  -> All dharmas lack intrinsic nature")

        print("\nShared insight:")
        print("  - 'Fixed essence' is an illusion")
        print("  - 'Independent substance' does not exist")
        print("  - The universe is an indivisible whole")
        print("  - Relationships constitute reality")
        print("="*70)

# Run
ontology = QuantumEntanglementOntology()
ontology.visualize_entanglement_ontology()

def visualize_emptiness_superposition():
    """
    Visualize the correspondence between 'emptiness' and superposition
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Panel 1: Eternalism (Being) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Eternalism (Being)', ha='center',
           fontsize=14, fontweight='bold')

    # A fixed substance
    rect = plt.Rectangle((0.3, 0.4), 0.4, 0.3,
                        facecolor='blue', alpha=0.7,
                        edgecolor='black', linewidth=3)
    ax.add_patch(rect)
    ax.text(0.5, 0.55, 'Substance\nFixed Essence', ha='center', va='center',
           fontsize=12, fontweight='bold', color='white')

    ax.text(0.5, 0.2, 'Error: Assumes things have permanent essence',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === Panel 2: Nihilism (Non-Being) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Nihilism (Non-Being)', ha='center',
           fontsize=14, fontweight='bold')

    # The void
    ax.text(0.5, 0.55, 'The Void\nNothing at all', ha='center', va='center',
           fontsize=14, fontweight='bold', color='gray')

    ax.text(0.5, 0.2, 'Error: Claims nothing exists whatsoever',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Panel 3: The Middle Way (Emptiness = Dependent Origination) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Middle Way: Emptiness = Dependent Origination', ha='center',
           fontsize=14, fontweight='bold')

    # Interdependent network
    nodes = [
        (0.3, 0.6), (0.5, 0.7), (0.7, 0.6),
        (0.3, 0.4), (0.5, 0.5), (0.7, 0.4),
    ]

    for x, y in nodes:
        circle = plt.Circle((x, y), 0.05, color='green', alpha=0.7,
                           edgecolor='darkgreen', linewidth=2)
        ax.add_patch(circle)

    # Connections
    for i, (x1, y1) in enumerate(nodes):
        for x2, y2 in nodes[i+1:]:
            distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
            if distance < 0.3:
                ax.plot([x1, x2], [y1, y2], 'green', alpha=0.4, linewidth=2)

    ax.text(0.5, 0.25, 'Correct: Things arise through conditions\nNeither being nor non-being',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === Panel 4: Quantum superposition ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, 'Quantum Superposition', ha='center',
           fontsize=14, fontweight='bold')

    # Superposition diagram
    circle_0 = plt.Circle((0.35, 0.55), 0.1, color='red', alpha=0.5,
                         edgecolor='red', linewidth=2)
    circle_1 = plt.Circle((0.65, 0.55), 0.1, color='blue', alpha=0.5,
                         edgecolor='blue', linewidth=2)
    ax.add_patch(circle_0)
    ax.add_patch(circle_1)

    ax.text(0.35, 0.55, '|0>', ha='center', va='center',
           fontsize=14, fontweight='bold')
    ax.text(0.65, 0.55, '|1>', ha='center', va='center',
           fontsize=14, fontweight='bold')

    # Double arrow
    ax.annotate('', xy=(0.62, 0.55), xytext=(0.38, 0.55),
               arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(0.5, 0.6, '+', ha='center', fontsize=16, fontweight='bold')

    ax.text(0.5, 0.4, '|psi> = a|0> + b|1>', ha='center',
           fontsize=11, fontweight='bold', color='purple')

    ax.text(0.5, 0.25, 'Neither |0> nor |1>\nBut also not "nothing at all"',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7))

    # Master title
    fig.text(0.5, 0.98, "Nagarjuna's 'Emptiness' and Quantum Superposition",
            ha='center', fontsize=16, fontweight='bold')

    # Bottom annotation
    explanation = '''
    Nagarjuna's Middle Way: Neither being nor non-being — transcending binary opposites
    Quantum superposition: Neither |0> nor |1> — transcending classical logic
    Common thread: Both go beyond the assumption of "fixed essence"
    '''

    fig.text(0.5, 0.02, explanation, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.1)
    plt.savefig('emptiness_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("NAGARJUNA'S 'EMPTINESS' AND QUANTUM SUPERPOSITION")
    print("="*70)

    print("\nNagarjuna refutes both extremes:")
    print("  1. Eternalism (Being): Assumes things have a fixed essence")
    print("     -> Wrong! Because everything changes")
    print("  2. Nihilism (Non-Being): Claims nothing exists at all")
    print("     -> Wrong! Because we clearly experience the world")

    print("\nNagarjuna's conclusion: The Middle Way")
    print("  - Things are 'not being' (no fixed essence)")
    print("  - Things are 'not non-being' (not completely non-existent)")
    print("  - Things 'are dependently originated' (arising through conditions)")

    print("\nQuantum superposition:")
    print("  - |psi> = a|0> + b|1>")
    print("  - 'Not |0>' (not definitely in |0>)")
    print("  - 'Not |1>' (not definitely in |1>)")
    print("  - 'Not nothing either' (superposition is real)")

    print("\nCorrespondence:")
    print("  Eternalism (Being) ~ Classical state (|0> or |1>)")
    print("  Nihilism (Non-Being) ~ Nothingness (no state at all)")
    print("  Middle Way (Emptiness = Dep. Origination) ~ Superposition (a|0>+b|1>)")

    print("\nShared structure:")
    print("  - Both transcend binary opposites")
    print("  - Both reject 'fixed essence'")
    print("  - Both affirm 'dependence'")

    print("\nNagarjuna's catuskoti (fourfold negation):")
    print("  For any proposition P:")
    print("  1. Is P true? -> No")
    print("  2. Is P false? -> No")
    print("  3. Is P both true and false? -> No")
    print("  4. Is P neither true nor false? -> No")
    print("  -> Transcend all concepts, point directly to reality")

    print("\nProfound insight:")
    print("  Classical logic: Being or non-being, pick one")
    print("  Quantum logic: Superposition, beyond the binary")
    print("  Nagarjuna's logic: Middle Way, beyond being and non-being")
    print("="*70)

# Run
visualize_emptiness_superposition()

def visualize_indra_net_holographic():
    """
    The holographic nature of Indra's Net and quantum entanglement
    """

    fig = plt.figure(figsize=(18, 10))

    # === Left panel: Indra's Net (3D) ===
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')

    # Create 3D grid
    n = 4
    positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                positions.append((i, j, k))

    positions = np.array(positions)

    # Draw jewels
    ax1.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='gold', s=200, edgecolors='black', linewidth=1.5,
               alpha=0.8)

    # Highlight one jewel
    highlight = np.array([1, 1, 1])
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3,
               zorder=10)

    # Draw connections to neighbors
    for pos in positions:
        distance = np.linalg.norm(pos - highlight)
        if 0 < distance <= 1.5:
            ax1.plot([highlight[0], pos[0]],
                    [highlight[1], pos[1]],
                    [highlight[2], pos[2]],
                    'r-', alpha=0.5, linewidth=2)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title("Indra's Net: Every Jewel Reflects All Others\n"
                 "Change one, and the whole net shimmers",
                 fontsize=14, fontweight='bold')

    # === Right panel: Entanglement network and holographic structure ===
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.axis('off')

    # Create entanglement network
    G = nx.complete_graph(8)
    pos = nx.circular_layout(G)

    # Draw all connections (entanglement links)
    nx.draw_networkx_edges(G, pos, edge_color='lightblue', alpha=0.3,
                          width=2, ax=ax2)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=800,
                          edgecolors='darkblue', linewidths=2,
                          alpha=0.8, ax=ax2)

    # Labels
    labels = {i: f'P{i+1}' for i in range(8)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10,
                           font_weight='bold', ax=ax2)

    # Highlight one node
    nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color='red',
                          node_size=1000, edgecolors='black',
                          linewidths=3, ax=ax2)

    # Emphasize connections from this node
    edges_from_0 = [(0, i) for i in range(1, 8)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_from_0,
                          edge_color='red', alpha=0.7, width=3, ax=ax2)

    ax2.set_title('Quantum Entanglement Network: Holographic Structure\n'
                 'Each particle contains information about the entire system',
                 fontsize=14, fontweight='bold')

    # Bottom annotation
    explanation = '''
    Indra's Net (Avatamsaka/Huayan Buddhism):
    - Every jewel reflects all other jewels
    - Change one jewel, and the whole net changes
    - The part contains the whole
    - Infinite mutual reflection

    Quantum Entanglement Network:
    - Every particle is entangled with all others
    - Measuring one particle affects all others
    - The part contains information about the whole (holography)
    - Non-local correlations

    Shared insight:
    * The universe is an indivisible whole
    * Part and whole are inseparable
    * One is all, all is one
    * Relationships constitute reality
    '''

    fig.text(0.5, 0.02, explanation, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)
    plt.savefig('indra_net_holographic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("INDRA'S NET AND QUANTUM HOLOGRAPHY")
    print("="*70)

    print("\nIndra's Net (Avatamsaka/Huayan Buddhism):")
    print("  - A vast net hanging in Indra's palace")
    print("  - A luminous jewel at every intersection")
    print("  - Each jewel reflects all other jewels")
    print("  - Each reflection contains all other reflections")
    print("  - Infinite recursion, endless interpenetration")

    print("\nThe holographic nature of quantum entanglement:")
    print("  - Entangled state: |psi>_AB cannot be decomposed")
    print("  - Measuring particle A -> instantly affects particle B")
    print("  - Each particle contains information about the entire system")
    print("  - Parts cannot be separated from the whole")

    print("\nThe Holographic Principle:")
    print("  - A major concept in physics")
    print("  - The information in a region can be encoded on its boundary")
    print("  - Volume information = Surface information")
    print("  - The 3D universe may be a 2D hologram")

    print("\nThe holographic nature of dependent origination:")
    print("  - 'This being, that becomes'")
    print("  - Everything is mutually conditioned")
    print("  - Change one phenomenon, and all phenomena change")
    print("  - Reality is an indivisible whole")

    print("\nUltimate insight:")
    print("  The universe is not a 'collection of parts'")
    print("  but an 'indivisible whole'")
    print("  'Separation' is an illusion")
    print("  'Oneness' is the deeper truth")
    print("="*70)

# Run
visualize_indra_net_holographic()
