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

About the Orch OR numbers (fact-checked 2026-09):
- tau ~ 25 ms / ~40 Hz is the timescale Orch OR proponents take from gamma-band
  brain rhythms (Hameroff & Penrose 2014, Phys. Life Rev. 11:39-78). It is a set
  value, not something this script derives.
- Penrose's objective-reduction estimate is tau ~ hbar / E_G, where E_G is the
  gravitational self-energy of the difference between the two superposed mass
  distributions (Penrose 1996, Gen. Relativ. Gravit. 28:581-600).
- The demo below uses the simplified stand-in tau = hbar / (Delta_M * c^2) with a
  hand-set, purely illustrative Delta_M. It is NOT Penrose's formula and its
  absolute values should not be read literally.

Requirements:
pip install numpy matplotlib
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
            'Observer interacts (Wigner: consciousness?)\n'
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
    print("  Common summary (von Neumann-Wigner reading):")
    print("  Collapse requires the observer's CONSCIOUSNESS")
    print("  Caveat: von Neumann himself did not explicitly claim this;")
    print("  the reading comes mainly from later interpreters such as Wigner")

# ============================================================================
# Visualization 2: Orch OR Concept (Simple)
# ============================================================================

# Physical constants (CODATA)
HBAR = 1.054571817e-34  # J*s, reduced Planck constant
C_LIGHT = 299792458.0   # m/s, speed of light

def calculate_collapse_time(delta_m):
    """
    Simplified demo formula: tau = hbar / (Delta_M * c^2), in seconds.

    NOTE: this is NOT Penrose's formula. Penrose's objective-reduction estimate
    is tau ~ hbar / E_G, where E_G is the gravitational self-energy of the
    difference between the two superposed mass distributions (Penrose 1996,
    Gen. Relativ. Gravit. 28:581-600). Delta_M * c^2 is only a rough stand-in
    that shows the scaling idea (larger mass difference -> faster collapse).
    It is vastly larger than E_G, so the absolute values come out many orders
    of magnitude too short.
    """
    return HBAR / (delta_m * C_LIGHT**2)

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

    ax2.set_xlabel('Time (schematic, not to scale)', fontsize=11)
    ax2.set_ylabel('Quantum Coherence', fontsize=11)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Orch OR: tau ~ h-bar/E_G (gravitational self-energy)\n'
                 'Proponents quote ~25 ms (~40 Hz) - a value set from gamma rhythms',
                 fontsize=11)

    ax2.text(0.5, 0.05,
            'Penrose-Hameroff (proposed): each collapse = one conscious moment\n'
            'Consciousness = sequence of orchestrated collapse events',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('orch_or_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Orch OR Theory (proposed, speculative):")
    print("  1. Hypothesis: microtubules in neurons support quantum-coherent states")
    print("  2. Superposition is proposed to build up until objective reduction (OR)")
    print("  3. Penrose proposes that OR is triggered by quantum gravity")
    print("  4. Each collapse = ONE moment of consciousness")
    print("  5. Brain orchestrates these collapses -> unified experience")
    print("  ")

    # Illustrative, hand-set input: NOT a measured brain value and NOT taken
    # from Penrose's or Hameroff's papers. It only feeds the simplified demo formula.
    delta_m_demo = 1e-8                       # kg (illustrative)
    tau_demo = calculate_collapse_time(delta_m_demo)   # seconds

    # Literature-cited Orch OR timescale: proponents take ~25 ms from ~40 Hz
    # gamma synchrony and back out how many tubulins would have to be in
    # superposition (Hameroff & Penrose 2014). It is a set value, not derived here.
    tau_literature = 25e-3                    # s
    freq_literature = 1.0 / tau_literature    # Hz
    gap_orders = np.log10(tau_literature / tau_demo)

    print("  Simplified demo formula (NOT Penrose's E_G): tau = h-bar / (Delta_M * c^2)")
    print(f"  Illustrative Delta_M = {delta_m_demo:.0e} kg -> tau = {tau_demo:.2e} s")
    print(f"  Literature timescale (set from gamma rhythms): tau ~ {tau_literature*1000:.0f} ms"
          f" -> ~{freq_literature:.0f} Hz")
    print(f"  Gap: the demo value is ~10^{gap_orders:.0f} times shorter than 25 ms;")
    print("  it comes from the simplification (Delta_M * c^2 instead of E_G), not from the theory")
    print("  ")
    print("  Speculative and highly controversial. Note: Penrose's 2020 Nobel Prize")
    print("  was for black-hole physics, not for Orch OR.")

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

    fig.text(0.5, -0.02, 'A descriptive analogy, not an equivalence',
            ha='center', va='top', fontsize=10, style='italic')

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
    print("  This is a descriptive analogy, not an equivalence: it is the author's own")
    print("  comparison, not a result recognized in physics or Buddhist scholarship.")
    print("  Open question: is the parallel profound or superficial?")

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
print("  - Von Neumann-Wigner reading: collapse requires consciousness")
print("    (von Neumann himself was more cautious)")
print("  - Penrose-Hameroff (Orch OR, speculative): consciousness arises from")
print("    orchestrated quantum collapses")
print("  - Orch OR numbers: ~25 ms / ~40 Hz is set from gamma rhythms; the simplified")
print("    demo formula gives a very different value (see the Orch OR section above)")
print("  - Wang Yangming: Mind is the principle (Xin Ji Li)")
print("  - Zen: Enlightenment is described as sudden (dunwu)")
print("  - Parallel (descriptive analogy, not equivalence): both are described")
print("    as sudden, irreversible transitions")
print("  - Question: Is consciousness fundamental or emergent?")
print("=" * 70)
