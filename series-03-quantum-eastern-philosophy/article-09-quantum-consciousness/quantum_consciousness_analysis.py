"""
Quantum Consciousness vs Eastern Mind Philosophy - Free Version
Season 2 Article 09: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic quantum measurement and collapse
- Simple Orch OR concept illustration
- Zen enlightenment metaphor

For complete version with 12 sub-plots, see premium content.

Requirements:
pip install numpy matplotlib scipy
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Quantum Consciousness vs Eastern Mind Philosophy - Free Version")
print("Season 2 Article 09")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Quantum Measurement and Collapse
# ============================================================================

def quantum_measurement_basic():
    """
    Basic visualization of quantum measurement and wave function collapse
    """
    print("\n[Visualization 1] Quantum Measurement and Collapse")
    print("-" * 70)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))

    # State 1: Superposition before measurement
    ax1.text(0.5, 0.9, 'BEFORE Measurement', ha='center',
            fontsize=13, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.5, 0.82, 'Quantum Superposition State', ha='center', fontsize=11,
            transform=ax1.transAxes)

    # Superposition state
    states = ['|0>', '|1>']
    probs = [0.5, 0.5]
    colors_super = ['lightblue', 'lightcoral']

    bars1 = ax1.bar(states, probs, color=colors_super,
                    edgecolor='black', linewidth=2, alpha=0.7)

    # Wavy overlay to indicate superposition
    x_wave = np.linspace(0, 1, 100)
    for i in range(2):
        y_wave = 0.5 * (1 + 0.1*np.sin(2*np.pi*5*x_wave))
        ax1.fill_between([i-0.3, i+0.3], [0, 0], [y_wave.max(), y_wave.max()],
                        alpha=0.2, color=colors_super[i])

    ax1.set_ylabel('Probability Amplitude', fontsize=11)
    ax1.set_ylim(0, 1)
    ax1.set_title('|psi> = (|0> + |1>)/sqrt(2)\nBOTH states simultaneously',
                 fontsize=11)
    ax1.grid(alpha=0.3, axis='y')

    ax1.text(0.5, 0.25,
            'Particle is in SUPERPOSITION\n'
            'No definite value\n'
            'Probability: 50% each',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
            transform=ax1.transAxes)

    # State 2: Measurement act
    ax2.text(0.5, 0.9, 'DURING Measurement', ha='center',
            fontsize=13, fontweight='bold', transform=ax2.transAxes)
    ax2.text(0.5, 0.82, 'Observer Interaction', ha='center', fontsize=11,
            transform=ax2.transAxes)

    # Eye symbol for observer
    circle = plt.Circle((0.5, 0.6), 0.15, color='lightgreen',
                       edgecolor='black', linewidth=3)
    ax2.add_patch(circle)
    ax2.plot([0.5], [0.6], 'ko', markersize=20)
    ax2.text(0.5, 0.6, 'EYE', ha='center', va='center', fontsize=12,
            fontweight='bold', color='white')

    # Arrows to both states
    ax2.arrow(0.5, 0.4, -0.15, -0.15, head_width=0.05, head_length=0.03,
             fc='gray', ec='gray', linewidth=2)
    ax2.arrow(0.5, 0.4, 0.15, -0.15, head_width=0.05, head_length=0.03,
             fc='gray', ec='gray', linewidth=2)

    ax2.text(0.25, 0.15, '|0>', ha='center', fontsize=14,
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    ax2.text(0.75, 0.15, '|1>', ha='center', fontsize=14,
            bbox=dict(boxstyle='round', facecolor='lightcoral'))

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    ax2.text(0.5, 0.05,
            'Consciousness observes\n'
            'Wave function COLLAPSES',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # State 3: After collapse
    ax3.text(0.5, 0.9, 'AFTER Measurement', ha='center',
            fontsize=13, fontweight='bold', transform=ax3.transAxes)
    ax3.text(0.5, 0.82, 'Definite State', ha='center', fontsize=11,
            transform=ax3.transAxes)

    # Collapsed to one state (randomly choose)
    np.random.seed(42)
    collapsed_state = np.random.choice([0, 1])
    probs_collapsed = [0, 0]
    probs_collapsed[collapsed_state] = 1.0

    colors_collapsed = ['lightgray', 'lightgray']
    colors_collapsed[collapsed_state] = colors_super[collapsed_state]

    bars3 = ax3.bar(states, probs_collapsed, color=colors_collapsed,
                    edgecolor='black', linewidth=2, alpha=1.0)

    ax3.set_ylabel('Probability', fontsize=11)
    ax3.set_ylim(0, 1.2)
    ax3.set_title(f'Collapsed to |{collapsed_state}>\nDEFINITE value',
                 fontsize=11)
    ax3.grid(alpha=0.3, axis='y')

    # Mark the collapsed state
    ax3.text(collapsed_state, 1.1, 'V', ha='center', fontsize=24,
            color='green', fontweight='bold')

    ax3.text(0.5, 0.25,
            f'Particle is NOW in state |{collapsed_state}>\n'
            'Definite value\n'
            'IRREVERSIBLE',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
            transform=ax3.transAxes)

    plt.tight_layout()
    plt.savefig('quantum_measurement_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Before: Superposition |psi> = (|0>+|1>)/sqrt(2)")
    print(f"  During: Observer (consciousness?) interacts")
    print(f"  After: Collapsed to |{collapsed_state}>")
    print(f"  ")
    print(f"  Von Neumann's claim:")
    print(f"  Collapse requires CONSCIOUSNESS")
    print(f"  Without observer -> no definite state")

# ============================================================================
# Visualization 2: Orch OR Concept (Simple)
# ============================================================================

def orch_or_basic():
    """
    Simple illustration of Orch OR theory concept
    """
    print("\n[Visualization 2] Orch OR Theory Concept")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # Plot 1: Microtubule structure
    ax1.text(0.5, 0.95, 'Microtubules in Neurons', ha='center',
            fontsize=13, fontweight='bold')

    # Draw simplified neuron
    soma = plt.Circle((0.5, 0.7), 0.15, color='lightblue',
                     edgecolor='black', linewidth=2, alpha=0.7)
    ax1.add_patch(soma)
    ax1.text(0.5, 0.7, 'Neuron\nSoma', ha='center', va='center', fontsize=9)

    # Dendrites
    ax1.plot([0.5, 0.2], [0.7, 0.85], 'k-', linewidth=3)
    ax1.plot([0.5, 0.8], [0.7, 0.85], 'k-', linewidth=3)

    # Axon with microtubules
    ax1.plot([0.5, 0.5], [0.55, 0.2], 'k-', linewidth=4)

    # Microtubules inside axon (small circles)
    for y in np.linspace(0.52, 0.22, 8):
        mt = plt.Circle((0.5, y), 0.02, color='red',
                       edgecolor='darkred', linewidth=1)
        ax1.add_patch(mt)

    ax1.text(0.7, 0.4, 'Microtubules\n(~25 nm diameter)',
            fontsize=9, bbox=dict(boxstyle='round', facecolor='pink', alpha=0.7))
    ax1.arrow(0.68, 0.38, -0.12, -0.08, head_width=0.02, head_length=0.01,
             fc='red', ec='red')

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    ax1.set_title('Penrose-Hameroff Hypothesis:\n'
                 'Quantum processes in microtubules',
                 fontsize=11)

    # Plot 2: Quantum collapse as consciousness moment
    ax2.text(0.5, 0.95, 'Orchestrated Objective Reduction (Orch OR)',
            ha='center', fontsize=13, fontweight='bold')

    # Timeline of quantum states
    t = np.linspace(0, 1, 100)

    # Build-up phase (quantum coherence)
    buildup_region = t < 0.4
    ax2.fill_between(t[buildup_region], 0, 0.5, color='lightblue', alpha=0.5)
    ax2.text(0.2, 0.6, 'Quantum\nSuperposition\nBuilds Up',
            ha='center', fontsize=9, bbox=dict(boxstyle='round',
            facecolor='lightblue', alpha=0.7))

    # Collapse moment
    collapse_point = 0.4
    ax2.axvline(x=collapse_point, color='red', linewidth=4, linestyle='--')
    ax2.text(collapse_point, 0.85, 'COLLAPSE\nConsciousness\nMoment',
            ha='center', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow'))

    # After collapse
    after_region = t >= 0.4
    ax2.fill_between(t[after_region], 0, 0.5, color='lightgreen', alpha=0.5)
    ax2.text(0.7, 0.6, 'Definite State\nClassical\nInformation',
            ha='center', fontsize=9, bbox=dict(boxstyle='round',
            facecolor='lightgreen', alpha=0.7))

    ax2.set_xlabel('Time', fontsize=11)
    ax2.set_ylabel('Quantum Coherence', fontsize=11)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('tau = h-bar/(Delta-E) ~ 25ms (40Hz)\n'
                 'Matches conscious "refresh rate"!',
                 fontsize=11)

    ax2.text(0.5, 0.05,
            'Penrose-Hameroff: Each collapse = one conscious moment\n'
            'Consciousness = series of quantum computations',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('orch_or_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Orch OR Theory:")
    print(f"  1. Microtubules in neurons have quantum properties")
    print(f"  2. Quantum superposition builds up over ~25ms")
    print(f"  3. Spontaneous collapse due to quantum gravity")
    print(f"  4. Each collapse = ONE moment of consciousness")
    print(f"  5. Brain orchestrates these collapses -> unified experience")
    print(f"  ")
    print(f"  Collapse time: tau ~ h-bar/(Delta-M * c^2) ~ 25ms")
    print(f"  Frequency: ~40 Hz (gamma oscillations)")
    print(f"  ")
    print(f"  VERY controversial but Nobel Prize 2020!")

# ============================================================================
# Visualization 3: Zen Enlightenment Metaphor
# ============================================================================

def zen_enlightenment_metaphor():
    """
    Metaphorical comparison between quantum collapse and Zen enlightenment
    """
    print("\n[Visualization 3] Zen Enlightenment Metaphor")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # Plot 1: Quantum collapse
    ax1.text(0.5, 0.95, 'Quantum Collapse', ha='center',
            fontsize=14, fontweight='bold')

    # Before collapse: uncertainty
    ellipse1 = plt.matplotlib.patches.Ellipse((0.5, 0.7), 0.5, 0.3,
                                             color='lightblue', alpha=0.5,
                                             edgecolor='blue', linewidth=2)
    ax1.add_patch(ellipse1)
    ax1.text(0.5, 0.7, 'Superposition\n(Uncertainty)',
            ha='center', va='center', fontsize=11, fontweight='bold')

    # Arrow down (collapse)
    ax1.arrow(0.5, 0.5, 0, -0.15, head_width=0.08, head_length=0.05,
             fc='red', ec='red', linewidth=4)
    ax1.text(0.68, 0.42, 'COLLAPSE', fontsize=10, fontweight='bold', color='red')

    # After collapse: definite
    star_x = [0.5, 0.55, 0.7, 0.58, 0.62, 0.5, 0.38, 0.42, 0.3, 0.45]
    star_y = [0.3, 0.23, 0.23, 0.17, 0.08, 0.13, 0.08, 0.17, 0.23, 0.23]
    ax1.fill(star_x, star_y, color='yellow', edgecolor='orange', linewidth=2)
    ax1.text(0.5, 0.18, 'Definite State', ha='center', va='center',
            fontsize=10, fontweight='bold')

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')

    ax1.text(0.5, 0.02,
            'Instantaneous\n'
            'Irreversible\n'
            'Observer-dependent',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    # Plot 2: Zen enlightenment
    ax2.text(0.5, 0.95, 'Zen Enlightenment (Dunwu / Satori)', ha='center',
            fontsize=14, fontweight='bold')

    # Before enlightenment: delusion
    ellipse2 = plt.matplotlib.patches.Ellipse((0.5, 0.7), 0.5, 0.3,
                                             color='gray', alpha=0.5,
                                             edgecolor='black', linewidth=2)
    ax2.add_patch(ellipse2)
    ax2.text(0.5, 0.7, 'Delusion\n(Ignorance)',
            ha='center', va='center', fontsize=11, fontweight='bold')

    # Lightning bolt (sudden enlightenment)
    lightning_x = [0.5, 0.55, 0.52, 0.58, 0.5, 0.48, 0.42, 0.45]
    lightning_y = [0.5, 0.45, 0.4, 0.35, 0.28, 0.35, 0.4, 0.45]
    ax2.fill(lightning_x, lightning_y, color='yellow', edgecolor='gold', linewidth=3)
    ax2.text(0.68, 0.42, 'SATORI', fontsize=10, fontweight='bold', color='darkred')

    # After enlightenment: clarity
    star2_x = [0.5, 0.55, 0.7, 0.58, 0.62, 0.5, 0.38, 0.42, 0.3, 0.45]
    star2_y = [0.3, 0.23, 0.23, 0.17, 0.08, 0.13, 0.08, 0.17, 0.23, 0.23]
    ax2.fill(star2_x, star2_y, color='gold', edgecolor='darkorange', linewidth=2)
    ax2.text(0.5, 0.18, 'Kensho\n(Seeing True Nature)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    ax2.text(0.5, 0.02,
            'Instantaneous\n'
            'Irreversible\n'
            'Self-realization',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('zen_enlightenment_metaphor.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Parallels:")
    print(f"  ")
    print(f"  Quantum Collapse          Zen Enlightenment")
    print(f"  ----------------          -----------------")
    print(f"  Superposition             Delusion/Ignorance")
    print(f"  Collapse moment           Satori/Dunwu")
    print(f"  Definite state            Enlightened mind")
    print(f"  Instantaneous             Instantaneous")
    print(f"  Irreversible              Irreversible")
    print(f"  Observer-dependent        Self-realization")
    print(f"  ")
    print(f"  Similarity: STRUCTURAL (~8/10)")
    print(f"  But: Is this profound or superficial?")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 12 sub-plots, see premium content)\n")

quantum_measurement_basic()
orch_or_basic()
zen_enlightenment_metaphor()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. quantum_measurement_basic.png - Measurement and collapse")
print("  2. orch_or_basic.png - Orch OR theory concept")
print("  3. zen_enlightenment_metaphor.png - Zen enlightenment parallel")
print("\n[Premium Version Includes]")
print("  - Quantum measurement complete (4 sub-plots)")
print("  - Orch OR theory detailed simulation (3 sub-plots)")
print("  - Zen enlightenment vs collapse (3 sub-plots)")
print("  - Mind-as-principle vs observer effect (2 sub-plots)")
print("  - Total: 12 professional sub-plots")
print("\n[Key Findings]")
print("  - Von Neumann: Collapse requires consciousness")
print("  - Penrose-Hameroff: Consciousness IS quantum process")
print("  - Wang Yangming: Mind is the principle (Xin Ji Li)")
print("  - Zen: Enlightenment is instant, irreversible")
print("  - Parallel: Both involve instantaneous, irreversible transitions")
print("  - Question: Is consciousness fundamental or emergent?")
print("=" * 70)
