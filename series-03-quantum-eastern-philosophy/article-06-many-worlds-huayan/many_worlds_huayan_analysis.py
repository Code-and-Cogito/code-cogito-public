"""
Many-Worlds Interpretation vs Huayan Infinite Interpenetration - Free Version
Season 2 Article 06: Standalone Visualizations

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #06/12

This script includes:
- Universe splitting tree (Many-Worlds branching)
- Parallel "yous" calculation
- Huayan fractal (Sierpinski triangle)

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Many-Worlds vs Huayan Infinite Interpenetration - Free Version")
print("Season 2 Article 06")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Universe Splitting Tree
# ============================================================================

def universe_splitting_tree():
    """
    Visualize universe splitting in Many-Worlds Interpretation.
    Each quantum measurement causes the universe to branch into
    all possible outcomes. After n measurements, 2^n worlds exist.
    """
    print("\n[Visualization 1] Universe Splitting Tree")
    print("-" * 70)

    n_measurements = 5

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

    # === Left panel: tree diagram ===
    # Draw initial world
    ax1.scatter([0], [0], s=300, c='green', zorder=5,
               edgecolors='black', linewidth=2)
    ax1.text(0, -0.3, 'Initial\nUniverse', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Track world counts
    steps = [0]
    world_counts = [1]

    for measurement in range(1, n_measurements + 1):
        n_worlds = 2 ** measurement
        steps.append(measurement)
        world_counts.append(n_worlds)

        # Calculate positions for this level
        y_positions = np.linspace(-n_worlds / 4, n_worlds / 4, n_worlds)

        # Previous level
        prev_size = 2 ** (measurement - 1)
        prev_y = np.linspace(-prev_size / 4, prev_size / 4, prev_size)

        for i in range(n_worlds):
            parent_idx = i // 2
            ax1.plot([measurement - 1, measurement],
                    [prev_y[parent_idx], y_positions[i]],
                    'b-', alpha=0.3, linewidth=1)
            color = 'red' if i % 2 == 0 else 'blue'
            ax1.scatter([measurement], [y_positions[i]],
                       s=100, c=color, zorder=5, alpha=0.6,
                       edgecolors='black', linewidth=0.5)

    ax1.set_xlabel('Number of Measurements', fontsize=13)
    ax1.set_ylabel('World Branches', fontsize=13)
    ax1.set_title(
        f'Many-Worlds Universe Branching Tree\n'
        f'{n_measurements} measurements -> {2**n_measurements} worlds',
        fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.2)
    ax1.set_xlim(-0.5, n_measurements + 0.5)

    import matplotlib.patches as mpatches
    red_patch = mpatches.Patch(color='red', label='Outcome 0 (e.g., cat dead)', alpha=0.6)
    blue_patch = mpatches.Patch(color='blue', label='Outcome 1 (e.g., cat alive)', alpha=0.6)
    ax1.legend(handles=[red_patch, blue_patch], fontsize=10)

    # === Right panel: exponential growth ===
    ax2.plot(steps, world_counts, 'ro-', linewidth=3, markersize=10,
            label='Actual world count')
    ax2.fill_between(steps, 0, world_counts, alpha=0.3, color='red')

    theory_counts = [2 ** i for i in steps]
    ax2.plot(steps, theory_counts, 'b--', linewidth=2,
            label='Theory: 2^n', alpha=0.7)

    ax2.set_xlabel('Number of Measurements (n)', fontsize=13)
    ax2.set_ylabel('Number of Worlds', fontsize=13)
    ax2.set_title('Exponential Growth of World Count\n'
                 'The Many-Worlds Ontological Explosion',
                 fontsize=14, fontweight='bold')
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')

    for step, count in zip(steps[::2], world_counts[::2]):
        ax2.text(step, count * 1.5, f'{count} worlds',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('universe_splitting_tree.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Data output
    print("\n" + "=" * 70)
    print("MANY-WORLDS UNIVERSE BRANCHING")
    print("=" * 70)
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
    print("=" * 70)


# ============================================================================
# Visualization 2: How Many Worlds Do "You" Exist In?
# ============================================================================

def parallel_yous():
    """
    Calculate number of parallel versions of 'you' based on
    everyday life decisions. Each choice creates new branches.
    """
    print("\n[Visualization 2] How Many Worlds Do 'You' Exist In?")
    print("-" * 70)

    # Example life decisions
    decisions = [
        {'description': 'What to eat for breakfast?', 'n_choices': 3},
        {'description': 'Which major in college?', 'n_choices': 5},
        {'description': 'Accept this job offer?', 'n_choices': 2},
        {'description': 'Confess your feelings?', 'n_choices': 2},
        {'description': 'Move to a new city?', 'n_choices': 2},
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # === Left panel: decision tree ===
    cumulative_worlds = [1]
    for decision in decisions:
        cumulative_worlds.append(cumulative_worlds[-1] * decision['n_choices'])

    for level, n_worlds in enumerate(cumulative_worlds):
        if level < 4:  # Only draw first few levels to avoid clutter
            y_positions = np.linspace(-n_worlds / 10, n_worlds / 10,
                                     min(n_worlds, 20))
            for y in y_positions[:min(n_worlds, 20)]:
                ax1.scatter([level], [y], s=50, c='blue', alpha=0.5,
                          edgecolors='black', linewidth=0.5)

            if level > 0:
                prev_n = cumulative_worlds[level - 1]
                prev_y = np.linspace(-prev_n / 10, prev_n / 10,
                                     min(prev_n, 20))
                for py in prev_y[:min(prev_n, 20)]:
                    for y in y_positions[:min(n_worlds, 20)]:
                        if abs(y - py) < n_worlds / 5:
                            ax1.plot([level - 1, level], [py, y],
                                   'gray', alpha=0.1, linewidth=0.5)

    ax1.set_xlabel('Life Decision Points', fontsize=13)
    ax1.set_ylabel('Parallel Life Branches', fontsize=13)
    ax1.set_title('Your Parallel Lives Tree\nEvery decision creates a new you',
                 fontsize=14, fontweight='bold')
    ax1.set_xticks(range(len(decisions) + 1))
    ax1.set_xticklabels(
        ['Birth'] + [d['description'][:15] + '...' for d in decisions],
        rotation=45, ha='right', fontsize=9)
    ax1.grid(True, alpha=0.2)

    # === Right panel: parallel life count ===
    decision_labels = ['Birth'] + [f"Decision {i+1}" for i in range(len(decisions))]

    ax2.bar(range(len(cumulative_worlds)), cumulative_worlds,
           color='purple', alpha=0.7, edgecolor='black', linewidth=1.5)

    ax2.set_xlabel('Life Stage', fontsize=13)
    ax2.set_ylabel('Number of Parallel Lives', fontsize=13)
    ax2.set_title('How Many Worlds Do You Exist In?',
                 fontsize=14, fontweight='bold')
    ax2.set_yscale('log')
    ax2.set_xticks(range(len(cumulative_worlds)))
    ax2.set_xticklabels(decision_labels, rotation=45, ha='right', fontsize=10)
    ax2.grid(True, alpha=0.3, axis='y')

    for i, n_worlds in enumerate(cumulative_worlds):
        ax2.text(i, n_worlds * 1.5, f'{n_worlds:,}',
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('parallel_yous.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Statistics
    total = 1
    for d in decisions:
        total *= d['n_choices']

    print("\n" + "=" * 70)
    print("YOUR PARALLEL LIVES")
    print("=" * 70)
    print("\nExample decisions:")
    for i, decision in enumerate(decisions, 1):
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
    print("=" * 70)


# ============================================================================
# Visualization 3: Huayan Fractal - Sierpinski Triangle
# ============================================================================

def huayan_fractal():
    """
    Fractal visualization representing Huayan's 'one contains all'.
    The Sierpinski triangle demonstrates self-similarity at all scales,
    mirroring Huayan's 'one dust mote contains all directions'.
    """
    print("\n[Visualization 3] Huayan Fractal - Sierpinski Triangle")
    print("-" * 70)

    def sierpinski(ax, order, points):
        """Draw a Sierpinski triangle recursively"""
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
            sierpinski(ax, order - 1, np.array([p1, m12, m31]))
            sierpinski(ax, order - 1, np.array([m12, p2, m23]))
            sierpinski(ax, order - 1, np.array([m31, m23, p3]))

    fig, ax = plt.subplots(figsize=(12, 10))

    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3) / 2])

    sierpinski(ax, order=5, points=np.array([p1, p2, p3]))

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.0)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title(
        'Huayan Buddhism: "One Contains All"\n'
        'Sierpinski Fractal - Infinite Self-Similarity',
        fontsize=14, fontweight='bold', pad=20)

    ax.text(0.5, -0.08,
           'Each small triangle contains the pattern of the whole.\n'
           'Huayan: "One dust mote contains ten directions"\n'
           'Infinite nesting, infinite reflection.',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
           transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('huayan_fractal.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "=" * 70)
    print("HUAYAN'S FRACTAL STRUCTURE")
    print("=" * 70)
    print("\nSierpinski Triangle properties:")
    print("  * Self-similar at all scales")
    print("  * Each part contains pattern of whole")
    print("  * Infinite complexity from simple rule")
    print("\nHuayan parallel:")
    print("  * One dharma contains all dharmas")
    print("  * Microcosm reflects macrocosm")
    print("  * Infinite realms within infinite realms")
    print("\nMathematical insight:")
    print("  Fractal self-similarity = Huayan's 'subtle mutual containment'")
    print("  Infinite nesting = infinite interpenetration")
    print("  Part = Whole")
    print("=" * 70)


# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...\n")

universe_splitting_tree()
parallel_yous()
huayan_fractal()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Visualization Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. universe_splitting_tree.png - Branching tree + exponential growth")
print("  2. parallel_yous.png - Life decision tree + parallel life count")
print("  3. huayan_fractal.png - Sierpinski triangle (Huayan metaphor)")
print("\nKey Findings:")
print("  - After n measurements -> 2^n parallel universes")
print("  - 5 decisions (3x5x2x2x2) = 120 parallel versions of 'you'")
print("  - Huayan: 'One dust mote contains all directions'")
print("  - Many-Worlds branching ~ Huayan's infinite interpenetration")
print("  - Both describe reality as infinite nested structure")
print("  - 'Infinity' is not a quantity -- it is a structural property")
print("=" * 70)
