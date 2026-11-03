# Code & Cogito: Many-Worlds Interpretation vs Huayan Buddhism's "Infinite Interpenetration" — Endless Parallel Universes
# Article: https://code-cogito.com/en/many-worlds-interpretation-huayan-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class MultiverseSimulator:
    """
    Many-Worlds Universe Splitting Simulator
    Demonstrates how each measurement causes the universe to branch
    """

    def __init__(self):
        self.worlds = []

    def initialize(self):
        """Initialize with a single world"""
        self.worlds = [{'id': 0, 'history': [], 'amplitude': 1.0}]

    def quantum_measurement(self, n_outcomes=2):
        """
        Perform a quantum measurement
        n_outcomes: number of possible outcomes (typically 2)
        """
        new_worlds = []

        for world in self.worlds:
            # Each world splits into n_outcomes new worlds
            for outcome in range(n_outcomes):
                new_world = {
                    'id': len(new_worlds),
                    'history': world['history'] + [outcome],
                    'amplitude': world['amplitude'] / np.sqrt(n_outcomes)
                }
                new_worlds.append(new_world)

        self.worlds = new_worlds
        return len(self.worlds)

    def visualize_branching(self, n_measurements=5):
        """
        Visualize the universe branching tree
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

        # === Left panel: tree diagram ===
        self.initialize()

        # Track the number of worlds at each step
        steps = [0]
        world_counts = [1]

        # Calculate positions
        max_level = n_measurements
        level_positions = {}  # {level: [world_ids]}

        for level in range(max_level + 1):
            level_positions[level] = []

        # Initial world
        level_positions[0] = [0]

        # Draw the initial world
        ax1.scatter([0], [0], s=300, c='green', zorder=5,
                   edgecolors='black', linewidth=2)
        ax1.text(0, -0.3, 'Initial\nUniverse', ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # Perform measurements step by step
        for measurement in range(1, n_measurements + 1):
            n_worlds = self.quantum_measurement(n_outcomes=2)
            steps.append(measurement)
            world_counts.append(n_worlds)

            # Calculate positions for this level
            n_worlds_this_level = 2 ** measurement
            y_positions = np.linspace(-n_worlds_this_level/4,
                                     n_worlds_this_level/4,
                                     n_worlds_this_level)

            # Draw connecting lines and nodes
            prev_level_size = 2 ** (measurement - 1)
            prev_y_positions = np.linspace(-prev_level_size/4,
                                          prev_level_size/4,
                                          prev_level_size)

            for i in range(n_worlds_this_level):
                parent_idx = i // 2
                ax1.plot([measurement-1, measurement],
                        [prev_y_positions[parent_idx], y_positions[i]],
                        'b-', alpha=0.3, linewidth=1)
                color = 'red' if i % 2 == 0 else 'blue'
                ax1.scatter([measurement], [y_positions[i]],
                           s=100, c=color, zorder=5, alpha=0.6,
                           edgecolors='black', linewidth=0.5)

        ax1.set_xlabel('Number of Measurements', fontsize=13)
        ax1.set_ylabel('World Branches', fontsize=13)
        ax1.set_title(f'Many-Worlds Universe Branching Tree\n{n_measurements} measurements → {2**n_measurements} worlds',
                     fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.2)
        ax1.set_xlim(-0.5, n_measurements + 0.5)

        red_patch = mpatches.Patch(color='red', label='Outcome 0 (e.g., cat dead)', alpha=0.6)
        blue_patch = mpatches.Patch(color='blue', label='Outcome 1 (e.g., cat alive)', alpha=0.6)
        ax1.legend(handles=[red_patch, blue_patch], fontsize=10)

        # === Right panel: world count growth ===
        ax2.plot(steps, world_counts, 'ro-', linewidth=3, markersize=10, label='Actual world count')
        ax2.fill_between(steps, 0, world_counts, alpha=0.3, color='red')

        theory_counts = [2**i for i in steps]
        ax2.plot(steps, theory_counts, 'b--', linewidth=2, label='Theory: 2^n', alpha=0.7)

        ax2.set_xlabel('Number of Measurements (n)', fontsize=13)
        ax2.set_ylabel('Number of Worlds', fontsize=13)
        ax2.set_title('Exponential Growth of World Count\nThe Many-Worlds Ontological Explosion',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.set_yscale('log')

        for step, count in zip(steps[::2], world_counts[::2]):
            ax2.text(step, count * 1.5, f'{count} worlds',
                    ha='center', fontsize=9,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.savefig('multiverse_branching.png', dpi=300, bbox_inches='tight')
        plt.show()

        # Data output
        print("\n" + "="*70)
        print("MANY-WORLDS UNIVERSE BRANCHING")
        print("="*70)
        print(f"\nInitial state: 1 universe")
        print(f"After 1 measurement: {2**1} worlds (universe splits in two)")
        print(f"After 2 measurements: {2**2} worlds")
        print(f"After 3 measurements: {2**3} worlds")
        print(f"After 4 measurements: {2**4} worlds")
        print(f"After 5 measurements: {2**5} worlds")
        print(f"\nAfter n measurements: 2^n worlds")
        print(f"\nExamples:")
        print(f"  * 10 measurements = {2**10:,} worlds")
        print(f"  * 20 measurements = {2**20:,} worlds")
        print(f"  * 30 measurements = {2**30:,} worlds")
        print(f"  * 100 measurements = {2**100:.2e} worlds")
        print(f"\nThe universe undergoes ~10^50 quantum events per second...")
        print(f"The number of worlds: beyond imagination!")
        print("="*70)

    def compare_interpretations(self):
        """
        Compare different interpretations of quantum measurement
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # === Copenhagen interpretation ===
        ax = axes[0, 0]
        ax.text(0.5, 0.7, 'Copenhagen Interpretation', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, 'Superposition\n|psi>', ha='center', va='center', fontsize=11)

        ax.annotate('', xy=(0.7, 0.6), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red'))
        ax.text(0.6, 0.65, 'Measurement\nCollapse', ha='center', fontsize=10, color='red')

        circle2 = plt.Circle((0.7, 0.6), 0.1, color='red', alpha=0.7)
        ax.add_patch(circle2)
        ax.text(0.7, 0.6, '|0>', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.text(0.7, 0.3, 'OR', ha='center', fontsize=12, fontweight='bold')

        circle3 = plt.Circle((0.7, 0.2), 0.1, color='blue', alpha=0.7)
        ax.add_patch(circle3)
        ax.text(0.7, 0.2, '|1>', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.text(0.5, 0.05, 'Wave function collapses\nOnly one outcome', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        # === Many-Worlds interpretation ===
        ax = axes[0, 1]
        ax.text(0.5, 0.7, 'Many-Worlds Interpretation', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle1 = plt.Circle((0.3, 0.5), 0.15, color='purple', alpha=0.5)
        ax.add_patch(circle1)
        ax.text(0.3, 0.5, 'Superposition\n|psi>', ha='center', va='center', fontsize=11)

        ax.annotate('', xy=(0.7, 0.6), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.annotate('', xy=(0.7, 0.2), xytext=(0.5, 0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.text(0.6, 0.4, 'Universe\nSplits', ha='center', fontsize=10, color='green')

        circle2 = plt.Circle((0.7, 0.6), 0.1, color='red', alpha=0.7)
        ax.add_patch(circle2)
        ax.text(0.7, 0.6, '|0>', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')
        ax.text(0.85, 0.6, 'World A', ha='left', fontsize=9)

        circle3 = plt.Circle((0.7, 0.2), 0.1, color='blue', alpha=0.7)
        ax.add_patch(circle3)
        ax.text(0.7, 0.2, '|1>', ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')
        ax.text(0.85, 0.2, 'World B', ha='left', fontsize=9)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.text(0.5, 0.05, 'Wave function never collapses\nAll outcomes occur', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

        # === Huayan Buddhism ===
        ax = axes[1, 0]
        ax.text(0.5, 0.9, 'Huayan: Infinite Interpenetration', ha='center', fontsize=16,
               fontweight='bold', transform=ax.transAxes)

        circle_center = plt.Circle((0.5, 0.5), 0.08, color='gold', alpha=0.8,
                                  edgecolor='black', linewidth=2)
        ax.add_patch(circle_center)
        ax.text(0.5, 0.5, 'One\nDust', ha='center', va='center', fontsize=10,
               fontweight='bold')

        n_worlds = 12
        angles = np.linspace(0, 2*np.pi, n_worlds, endpoint=False)
        for i, angle in enumerate(angles):
            x = 0.5 + 0.3 * np.cos(angle)
            y = 0.5 + 0.3 * np.sin(angle)
            circle = plt.Circle((x, y), 0.05, color='lightblue', alpha=0.6,
                               edgecolor='blue', linewidth=1)
            ax.add_patch(circle)
            ax.text(x, y, f'Realm\n{i+1}', ha='center', va='center', fontsize=7)
            ax.plot([0.5, x], [0.5, y], 'gray', alpha=0.3, linewidth=1)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.text(0.5, 0.05, 'One dust mote contains infinite realms\nAll realms mutually contain each other', ha='center', fontsize=10,
               transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        # === Comparison summary ===
        ax = axes[1, 1]
        ax.axis('off')

        comparison_text = '''
        Copenhagen vs Many-Worlds vs Huayan

        Copenhagen Interpretation:
        * Wave function collapses
        * Only one outcome
        * Probability: fundamental uncertainty

        Many-Worlds Interpretation:
        * Wave function never collapses
        * All outcomes occur (different worlds)
        * Probability: which world "I" end up in

        Huayan Buddhism:
        * All phenomena coexist simultaneously
        * Infinite interpenetrating realms
        * Perception: determined by karma

        Common Ground:
        - Multiple "realities" coexist
        - Observer-relativity
        - Infinite possibilities
        '''

        ax.text(0.1, 0.5, comparison_text, fontsize=11, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                        edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('interpretations_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()

# Run
simulator = MultiverseSimulator()
simulator.visualize_branching(n_measurements=5)
simulator.compare_interpretations()

class QuantumBiography:
    """
    Quantum Biography: How many worlds does "I" exist in?
    """

    def __init__(self):
        self.decisions = []

    def add_decision(self, description, n_choices=2):
        """
        Add a life decision
        description: description of the decision
        n_choices: number of possible choices
        """
        self.decisions.append({
            'description': description,
            'n_choices': n_choices
        })

    def calculate_parallel_lives(self):
        """
        Calculate the number of parallel lives
        """
        total_worlds = 1
        for decision in self.decisions:
            total_worlds *= decision['n_choices']
        return total_worlds

    def visualize_life_tree(self):
        """
        Visualize the life decision tree
        """
        # Example decisions
        self.decisions = [
            {'description': 'What to eat for breakfast?', 'n_choices': 3},
            {'description': 'Which major in college?', 'n_choices': 5},
            {'description': 'Accept this job offer?', 'n_choices': 2},
            {'description': 'Confess your feelings?', 'n_choices': 2},
            {'description': 'Move to a new city?', 'n_choices': 2},
        ]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

        # === Left panel: decision tree ===
        cumulative_worlds = [1]
        for i, decision in enumerate(self.decisions):
            cumulative_worlds.append(cumulative_worlds[-1] * decision['n_choices'])

        for level, n_worlds in enumerate(cumulative_worlds):
            if level < 4:  # Only draw first few levels to avoid clutter
                y_positions = np.linspace(-n_worlds/10, n_worlds/10,
                                         min(n_worlds, 20))

                for y in y_positions[:min(n_worlds, 20)]:
                    ax1.scatter([level], [y], s=50, c='blue', alpha=0.5,
                              edgecolors='black', linewidth=0.5)

                if level > 0:
                    prev_n_worlds = cumulative_worlds[level-1]
                    prev_y_positions = np.linspace(-prev_n_worlds/10,
                                                   prev_n_worlds/10,
                                                   min(prev_n_worlds, 20))

                    for prev_y in prev_y_positions[:min(prev_n_worlds, 20)]:
                        for y in y_positions[:min(n_worlds, 20)]:
                            if abs(y - prev_y) < n_worlds/5:
                                ax1.plot([level-1, level], [prev_y, y],
                                       'gray', alpha=0.1, linewidth=0.5)

        ax1.set_xlabel('Life Decision Points', fontsize=13)
        ax1.set_ylabel('Parallel Life Branches', fontsize=13)
        ax1.set_title('Your Parallel Lives Tree\nEvery decision creates a new you',
                     fontsize=14, fontweight='bold')
        ax1.set_xticks(range(len(self.decisions) + 1))
        ax1.set_xticklabels(['Birth'] + [d['description'][:15]+'...'
                                       for d in self.decisions],
                           rotation=45, ha='right', fontsize=9)
        ax1.grid(True, alpha=0.2)

        # === Right panel: parallel life count ===
        decision_labels = ['Birth'] + [f"Decision {i+1}" for i in range(len(self.decisions))]

        ax2.bar(range(len(cumulative_worlds)), cumulative_worlds,
               color='purple', alpha=0.7, edgecolor='black', linewidth=1.5)

        ax2.set_xlabel('Life Stage', fontsize=13)
        ax2.set_ylabel('Number of Parallel Lives', fontsize=13)
        ax2.set_title('How Many Worlds Do You Exist In?', fontsize=14, fontweight='bold')
        ax2.set_yscale('log')
        ax2.set_xticks(range(len(cumulative_worlds)))
        ax2.set_xticklabels(decision_labels, rotation=45, ha='right', fontsize=10)
        ax2.grid(True, alpha=0.3, axis='y')

        for i, n_worlds in enumerate(cumulative_worlds):
            ax2.text(i, n_worlds * 1.5, f'{n_worlds:,}',
                    ha='center', fontsize=9,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.savefig('quantum_biography.png', dpi=300, bbox_inches='tight')
        plt.show()

        # Statistics
        total = self.calculate_parallel_lives()

        print("\n" + "="*70)
        print("YOUR PARALLEL LIVES")
        print("="*70)
        print("\nExample decisions:")
        for i, decision in enumerate(self.decisions, 1):
            print(f"  {i}. {decision['description']} ({decision['n_choices']} choices)")

        print(f"\nResult:")
        print(f"  * These decisions create {total:,} parallel versions of 'you'")
        print(f"  * Each version has a different life trajectory")
        print(f"  * Each version believes it is the only one")

        print(f"\nIn reality:")
        print(f"  * You make about 35,000 decisions per day")
        print(f"  * Each decision has on average 2-3 options")
        print(f"  * One day: ~2^35000 worlds")
        print(f"  * One lifetime: an incomprehensibly large number!")

        print(f"\nPhilosophical questions:")
        print(f"  * Which 'you' is the 'real you'?")
        print(f"  * Do the other versions of you wonder the same thing?")
        print(f"  * What does your 'uniqueness' even mean?")

        print(f"\nHuayan Buddhism's answer:")
        print(f"  * All versions of 'you' are real")
        print(f"  * 'Self' was never singular")
        print(f"  * 'One is all': each self contains every self")
        print("="*70)

# Run
biography = QuantumBiography()
biography.visualize_life_tree()

def visualize_huayan_fractals():
    """
    Huayan's "One Dust Mote Contains All Directions" — Fractal visualization
    Demonstrates the structure of infinite recursion
    """

    fig = plt.figure(figsize=(18, 12))

    # === Panel 1: Mandelbrot set (the classic fractal example) ===
    ax1 = fig.add_subplot(2, 2, 1)

    def mandelbrot(c, max_iter=100):
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter

    width, height = 800, 800
    xmin, xmax = -2.5, 1.0
    ymin, ymax = -1.25, 1.25

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y

    mandelbrot_set = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = mandelbrot(C[i, j], max_iter=50)

    im1 = ax1.imshow(mandelbrot_set, extent=[xmin, xmax, ymin, ymax],
                    cmap='hot', interpolation='bilinear', origin='lower')
    ax1.set_title('Mandelbrot Set: Infinite Detail\nZoom into any region and find similar structures',
                 fontsize=13, fontweight='bold')
    ax1.set_xlabel('Real Part')
    ax1.set_ylabel('Imaginary Part')
    plt.colorbar(im1, ax=ax1, label='Iteration Count')

    # === Panel 2: Sierpinski triangle (recursive structure) ===
    ax2 = fig.add_subplot(2, 2, 2)

    def sierpinski(ax, order, points):
        """Draw a Sierpinski triangle"""
        if order == 0:
            triangle = plt.Polygon(points, fill=True,
                                  facecolor='blue', edgecolor='black',
                                  linewidth=0.5, alpha=0.6)
            ax.add_patch(triangle)
        else:
            p1, p2, p3 = points
            m12 = (p1 + p2) / 2
            m23 = (p2 + p3) / 2
            m31 = (p3 + p1) / 2
            sierpinski(ax, order-1, np.array([p1, m12, m31]))
            sierpinski(ax, order-1, np.array([m12, p2, m23]))
            sierpinski(ax, order-1, np.array([m31, m23, p3]))

    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3)/2])

    sierpinski(ax2, order=5, points=np.array([p1, p2, p3]))

    ax2.set_xlim(-0.1, 1.1)
    ax2.set_ylim(-0.1, 1.0)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Sierpinski Triangle: Self-Similarity\nEach sub-triangle contains the whole structure',
                 fontsize=13, fontweight='bold')

    # === Panel 3: Huayan world structure ===
    ax3 = fig.add_subplot(2, 2, 3)

    circle_center = plt.Circle((0.5, 0.5), 0.1, color='gold', alpha=0.9,
                              edgecolor='black', linewidth=3)
    ax3.add_patch(circle_center)
    ax3.text(0.5, 0.5, 'One\nDust', ha='center', va='center', fontsize=14,
            fontweight='bold')

    n_layer1 = 6
    angles1 = np.linspace(0, 2*np.pi, n_layer1, endpoint=False)
    layer1_radius = 0.25

    for angle in angles1:
        x = 0.5 + layer1_radius * np.cos(angle)
        y = 0.5 + layer1_radius * np.sin(angle)

        circle = plt.Circle((x, y), 0.06, color='lightblue', alpha=0.7,
                           edgecolor='blue', linewidth=2)
        ax3.add_patch(circle)
        ax3.text(x, y, 'Realm', ha='center', va='center', fontsize=10)
        ax3.plot([0.5, x], [0.5, y], 'gray', alpha=0.5, linewidth=2)

        n_layer2 = 4
        angles2 = np.linspace(0, 2*np.pi, n_layer2, endpoint=False)
        layer2_radius = 0.03

        for angle2 in angles2:
            x2 = x + layer2_radius * np.cos(angle2)
            y2 = y + layer2_radius * np.sin(angle2)

            circle2 = plt.Circle((x2, y2), 0.015, color='lightgreen',
                                alpha=0.5, edgecolor='green', linewidth=0.5)
            ax3.add_patch(circle2)
            ax3.plot([x, x2], [y, y2], 'green', alpha=0.3, linewidth=0.5)

    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('Huayan: One Dust Mote Contains All Realms\nRealm within realm, without end',
                 fontsize=13, fontweight='bold')

    ax3.text(0.5, 0.05, '"Within one dust mote, worlds as numerous as dust"\nInfinite recursion',
            ha='center', fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === Panel 4: Comparison summary ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    Fractals vs Huayan "Infinite Interpenetration"

    Mathematical Fractals:
    * Self-similarity
    * Infinite detail
    * Part contains the whole
    * Zoom in to find the same structure

    Huayan "Infinite Interpenetration":
    * One dust mote contains all directions
    * All realms mutually contain each other
    * Subtle mutual containment
    * Infinite recursion

    Common Structure:
    - Infinite nesting
    - Part = Whole
    - Every level is complete
    - Without limit

    Many-Worlds Interpretation:
    * Universe constantly splits
    * Each world splits again
    * Branching tree grows without bound
    * Exponential explosion

    Shared Insight of All Three:
    "Infinity" is not "very large"
    It is a property of structure itself
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center',
            family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                     edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('huayan_fractals.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("HUAYAN'S FRACTAL STRUCTURE")
    print("="*70)
    print("\nMathematical analogy:")
    print("  * Fractals: self-similar, infinite detail")
    print("  * Mandelbrot set: zoom into any region, find similar structures")
    print("  * Sierpinski triangle: each sub-triangle = the whole")
    print("\nDeep insight:")
    print("  'Infinity' is not a quantity concept")
    print("  It is a property of structure itself")
    print("  Part is whole, whole is part")
    print("="*70)

# Run
visualize_huayan_fractals()

def visualize_time_multiverse():
    """
    The Many-Worlds of Time
    Demonstrates how past, present, and future mutually contain one another
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

    # === Left panel: quantum temporal branching ===
    times = np.array([0, 1, 2, 3, 4])

    ax1.scatter([0], [0], s=500, c='green', zorder=5,
               edgecolors='black', linewidth=3)
    ax1.text(0, -0.5, 't=0\nInitial', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # t=1: splits into 2
    y1 = [-1, 1]
    for y in y1:
        ax1.scatter([1], [y], s=300, c='blue', zorder=5,
                   edgecolors='black', linewidth=2, alpha=0.7)
        ax1.plot([0, 1], [0, y], 'b-', alpha=0.5, linewidth=2)

    # t=2: each splits into 2 more
    y2 = [-1.5, -0.5, 0.5, 1.5]
    for i, y in enumerate(y2):
        parent_y = y1[i//2]
        ax1.scatter([2], [y], s=200, c='red', zorder=5,
                   edgecolors='black', linewidth=1.5, alpha=0.6)
        ax1.plot([1, 2], [parent_y, y], 'r-', alpha=0.4, linewidth=1.5)

    # t=3: continue splitting
    y3 = np.linspace(-2, 2, 8)
    for i, y in enumerate(y3):
        parent_y = y2[i//2]
        ax1.scatter([3], [y], s=100, c='purple', zorder=5,
                   edgecolors='black', linewidth=1, alpha=0.5)
        ax1.plot([2, 3], [parent_y, y], 'purple', alpha=0.3, linewidth=1)

    # t=4: even more splitting
    y4 = np.linspace(-2.5, 2.5, 16)
    for i, y in enumerate(y4):
        parent_y = y3[i//2]
        ax1.scatter([4], [y], s=50, c='orange', zorder=5,
                   edgecolors='black', linewidth=0.5, alpha=0.4)
        ax1.plot([3, 4], [parent_y, y], 'orange', alpha=0.2, linewidth=0.5)

    ax1.set_xlabel('Time', fontsize=13)
    ax1.set_ylabel('World Branches', fontsize=13)
    ax1.set_title('Quantum Many-Worlds: Time Branches Toward the Future\nThe past is singular, the future is multiple',
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.2)
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-3, 3)

    ax1.text(2, 2.5, f't=2: {4} worlds', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))
    ax1.text(4, 2.8, f't=4: {16} worlds', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    # === Right panel: Huayan's ten time-periods ===
    past_center = np.array([0.2, 0.5])
    present_center = np.array([0.5, 0.5])
    future_center = np.array([0.8, 0.5])

    circle_past = plt.Circle(past_center, 0.15, color='blue', alpha=0.3,
                            edgecolor='blue', linewidth=3)
    ax2.add_patch(circle_past)
    ax2.text(past_center[0], past_center[1], 'Past',
            ha='center', va='center', fontsize=14, fontweight='bold')

    circle_present = plt.Circle(present_center, 0.15, color='green', alpha=0.3,
                               edgecolor='green', linewidth=3)
    ax2.add_patch(circle_present)
    ax2.text(present_center[0], present_center[1], 'Present',
            ha='center', va='center', fontsize=14, fontweight='bold')

    circle_future = plt.Circle(future_center, 0.15, color='red', alpha=0.3,
                              edgecolor='red', linewidth=3)
    ax2.add_patch(circle_future)
    ax2.text(future_center[0], future_center[1], 'Future',
            ha='center', va='center', fontsize=14, fontweight='bold')

    connections = [
        (past_center, present_center),
        (present_center, future_center),
        (past_center, future_center),
        (present_center, past_center),
        (future_center, present_center),
        (future_center, past_center),
    ]

    for start, end in connections:
        ax2.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', lw=2, alpha=0.4,
                                  color='gray', connectionstyle="arc3,rad=.3"))

    positions_text = [
        (0.1, 0.8, 'Past of\nPast'),
        (0.1, 0.5, 'Present\nof Past'),
        (0.1, 0.2, 'Future\nof Past'),
        (0.5, 0.8, 'Past of\nPresent'),
        (0.5, 0.2, 'Future of\nPresent'),
        (0.9, 0.8, 'Past of\nFuture'),
        (0.9, 0.5, 'Present\nof Future'),
        (0.9, 0.2, 'Future\nof Future'),
    ]

    for x, y, label in positions_text:
        circle_small = plt.Circle((x, y), 0.06, color='yellow', alpha=0.5,
                                 edgecolor='orange', linewidth=1)
        ax2.add_patch(circle_small)
        ax2.text(x, y, label, ha='center', va='center', fontsize=7)

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Huayan "Ten Time-Periods": Times Mutually Contain Each Other\nPast holds future, future holds past',
                 fontsize=14, fontweight='bold')

    ax2.text(0.5, 0.05, '"The Eighth Gate: Distinct Dharmas of Ten Time-Periods"\nA single thought-moment contains all three times',
            ha='center', fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('time_multiverse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("THE MANY-WORLDS OF TIME")
    print("="*70)

    print("\nQuantum Many-Worlds:")
    print("  * Time branches toward the future")
    print("  * The past: singular")
    print("  * The future: multiple (exponential growth)")
    print("  * Time is unidirectional")

    print("\nHuayan 'Ten Time-Periods':")
    print("  1. Past of the past")
    print("  2. Present of the past")
    print("  3. Future of the past")
    print("  4. Past of the present")
    print("  5. Present of the present")
    print("  6. Future of the present")
    print("  7. Past of the future")
    print("  8. Present of the future")
    print("  9. Future of the future")
    print("  10. All three times taken together as one")

    print("\nComparison:")
    print("  Quantum: time moves forward, branches increase")
    print("  Huayan: time has no fixed direction, all times mutually contain each other")
    print("="*70)

# Run
visualize_time_multiverse()
