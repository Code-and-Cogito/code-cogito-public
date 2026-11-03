"""
Copenhagen Interpretation vs Kyoto School - Free Version
Series 3, Article 02: The Double-Slit Experiment, Yin-Yang Complementarity,
and the Observer Effect

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #02/12

This standalone free script includes:
- A toy double-slit model (observed vs unobserved)
- A taijitu (yin-yang) diagram next to a schematic of Bohr's complementarity
- Observer effect comparison

About the data:
- Every curve below is a hand-set illustrative model (slit positions,
  wavelength and peak widths are chosen by hand). None of it is measured data
  or a physical simulation, so no real-world numbers are computed here.
- The parallels between Copenhagen and Kyoto are this series' interpretive
  framing, not scientific findings.

Sources for the facts quoted in comments and printed text:
- Bohr's coat of arms (1947, when he received Denmark's Order of the
  Elephant) shows a taijitu with the motto "Contraria sunt complementa".
  Wikipedia, "Niels Bohr".
- The swirl-and-dots taijitu drawn here is the Ming-dynasty form (swirl:
  Zhao Huiqian, 1370s; dotted standard form: Lai Zhide, 1525-1604). Zhou
  Dunyi's 11th-century Taiji diagram is a different design.
  Wikipedia, "Taijitu".
- Complementarity: N. Bohr, "The Quantum Postulate and the Recent Development
  of Atomic Theory", Nature 121 (1928), 580-590 (from his 1927 Como lecture).
- Huineng's flag-and-wind story: Platform Sutra.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Copenhagen vs Kyoto School - Free Version")
print("Quantum Mechanics Meets Eastern Philosophy #02/12")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Double-Slit Experiment - Observed vs Unobserved
# ============================================================================

def count_peaks(curve, floor=0.5):
    """Count interior local maxima above `floor` (curves are normalised to 1)."""
    core = curve[1:-1]
    return int(np.sum((core > curve[:-2]) & (core >= curve[2:]) & (core > floor)))


def double_slit_comparison():
    """
    Double-slit experiment: side-by-side comparison of wave behavior
    (unobserved) vs particle behavior (observed).

    Toy model, illustrative only: the slit positions, the wavelength and the
    peak width are hand-set. Both curves are normalised to a peak of 1, so the
    y-axis is relative intensity, not a count of photons. A real double-slit
    pattern also sits under a broad single-slit envelope, which this toy model
    leaves out, and the two-peak curve is a schematic (two Gaussians at the
    slit positions), not a computed which-path distribution.

    When we do not record which slit the photon passes through, the two
    contributions superpose and produce an interference pattern. When a
    detector records which slit was used ("observation" here means a
    which-path measurement, not a conscious observer), the interference
    disappears. In the Copenhagen reading, the measurement itself changes
    what can be observed.
    """
    print("\n[Visualization 1] Double-Slit Experiment: Observer Effect")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    y = np.linspace(-5, 5, 500)

    # --- Left panel: Unobserved (wave behavior) ---
    # Hand-set illustrative inputs (not measured values)
    slit1_pos = -1.0
    slit2_pos = 1.0
    wavelength = 0.5
    peak_width = 0.5  # sigma of each Gaussian in the "observed" panel

    wave1 = np.sin(2 * np.pi * (y - slit1_pos) / wavelength)
    wave2 = np.sin(2 * np.pi * (y - slit2_pos) / wavelength)

    total_wave = wave1 + wave2
    intensity_unobs = np.abs(total_wave) ** 2
    intensity_unobs = intensity_unobs / np.max(intensity_unobs)

    ax1.fill_between(y, 0, intensity_unobs, alpha=0.7, color='blue')
    ax1.plot(y, intensity_unobs, 'b-', linewidth=2)
    ax1.set_xlabel('Screen Position', fontsize=13)
    ax1.set_ylabel('Relative Intensity (normalised)', fontsize=13)
    ax1.set_title('Unobserved: Interference Pattern Appears (Wave)',
                  fontsize=13, fontweight='bold', color='blue')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 1.35)
    ax1.text(0, 1.25, 'Multiple peaks = Interference\nPhoton behaves as a "wave"',
             ha='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # --- Right panel: Observed (particle behavior) ---
    slit1_pattern = np.exp(-(y - slit1_pos) ** 2 / (2 * peak_width ** 2))
    slit2_pattern = np.exp(-(y - slit2_pos) ** 2 / (2 * peak_width ** 2))

    intensity_obs = slit1_pattern + slit2_pattern
    intensity_obs = intensity_obs / np.max(intensity_obs)

    ax2.fill_between(y, 0, intensity_obs, alpha=0.7, color='red')
    ax2.plot(y, intensity_obs, 'r-', linewidth=2)
    ax2.set_xlabel('Screen Position', fontsize=13)
    ax2.set_ylabel('Relative Intensity (normalised)', fontsize=13)
    ax2.set_title('Observed: Interference Vanishes (Particle)',
                  fontsize=13, fontweight='bold', color='red')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 1.35)
    ax2.text(0, 1.25, 'Two peaks = No interference\nPhoton behaves as a "particle"',
             ha='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    fig.text(0.5, 0.01,
             'Key insight: a measurement that records which slit was used changes the outcome. '
             'In the Copenhagen reading this is not measurement error.\n'
             "Zen parallel (this series' interpretive framing): observer and observed are not separate.\n"
             'Illustrative toy model: slit positions, wavelength and peak width are hand-set; '
             'not measured data or a physical simulation.',
             ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.subplots_adjust(bottom=0.22, left=0.07, right=0.97, top=0.92, wspace=0.25)
    plt.savefig('double_slit_observer_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    # The counts below are computed from the curves, not typed in by hand
    n_peaks_unobs = count_peaks(intensity_unobs)
    n_peaks_obs = count_peaks(intensity_obs)
    print(f"  Toy-model inputs (hand-set, illustrative): slits at {slit1_pos:+.1f} and "
          f"{slit2_pos:+.1f}, wavelength {wavelength}, peak width (sigma) {peak_width}")
    print(f"  - Left panel:  {n_peaks_unobs} evenly spaced interference peaks")
    print(f"  - Right panel: {n_peaks_obs} peaks (one per slit), no interference")
    print("  Copenhagen reading: the measurement changes what can be observed")
    print("  Zen parallel (interpretive): observer and observed are not separate")


# ============================================================================
# Visualization 2: Taiji (Yin-Yang) Symbol - Bohr's Complementarity
# ============================================================================

def taiji_complementarity():
    """
    The taijitu (yin-yang) symbol that Bohr put on his coat of arms in 1947,
    with the Latin motto 'Contraria sunt complementa' (Opposites are
    complementary).

    The motto shows that Bohr chose the symbol to evoke complementarity: wave
    and particle are complementary aspects of one phenomenon. The claim that
    the symbol "precisely expresses the mathematical structure" of
    complementarity is this article's interpretation, not something Bohr said.

    The swirl-and-dots form drawn here is the Ming-dynasty taijitu (Zhou
    Dunyi's 11th-century diagram looks different). The right-hand polar plot
    is a schematic (two half-discs), not data.
    """
    print("\n[Visualization 2] Taiji Symbol - Bohr's Complementarity Principle")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # --- Left: Taiji (yin-yang) symbol ---
    # Draw proper yin-yang using arcs and circles
    theta_full = np.linspace(0, 2 * np.pi, 500)

    # Outer circle (white fill first)
    ax1.fill(np.cos(theta_full), np.sin(theta_full), color='white',
             edgecolor='black', linewidth=3, zorder=1)

    # Black half (right side): large semicircle
    theta_right = np.linspace(-np.pi / 2, np.pi / 2, 250)
    x_right = np.cos(theta_right)
    y_right = np.sin(theta_right)

    # Upper small semicircle (black, center at (0, 0.5), radius 0.5)
    theta_upper = np.linspace(np.pi / 2, -np.pi / 2, 250)
    x_upper = 0.5 * np.cos(theta_upper)
    y_upper = 0.5 + 0.5 * np.sin(theta_upper)

    # Lower small semicircle (black goes around, center at (0, -0.5), radius 0.5)
    theta_lower = np.linspace(np.pi / 2, -np.pi / 2, 250)
    x_lower = -0.5 * np.cos(theta_lower)
    y_lower = -0.5 + 0.5 * np.sin(theta_lower)

    # Build black region path: right semicircle -> upper small arc -> lower small arc
    # Black region: right large semicircle + upper small semicircle (bulging left)
    # + lower small semicircle (bulging right)
    # Path: start at bottom (0,-1), go right semicircle to (0,1),
    #        then upper small semicircle from (0,1) to (0,0),
    #        then lower small semicircle from (0,0) to (0,-1)
    theta_main_right = np.linspace(-np.pi / 2, np.pi / 2, 300)
    x_main = np.cos(theta_main_right)
    y_main = np.sin(theta_main_right)

    # Upper small arc: from (0,1) curving left to (0,0)
    theta_up = np.linspace(np.pi / 2, -np.pi / 2, 150)
    x_up = 0.5 * np.cos(theta_up + np.pi)  # bulge left
    y_up = 0.5 + 0.5 * np.sin(theta_up)

    # Lower small arc: from (0,0) curving right to (0,-1)
    theta_lo = np.linspace(np.pi / 2, -np.pi / 2, 150)
    x_lo = 0.5 * np.cos(theta_lo)  # bulge right
    y_lo = -0.5 + 0.5 * np.sin(theta_lo)

    # Combine into one polygon for the black region
    x_black = np.concatenate([x_main, x_up, x_lo])
    y_black = np.concatenate([y_main, y_up, y_lo])

    ax1.fill(x_black, y_black, color='black', zorder=2)

    # Small circles (dots): white dot in black region, black dot in white region
    circle_white = plt.Circle((0, 0.5), 0.12, color='white', zorder=4)
    circle_black = plt.Circle((0, -0.5), 0.12, color='black', zorder=4)
    ax1.add_patch(circle_white)
    ax1.add_patch(circle_black)

    # Re-draw outer border
    ax1.plot(np.cos(theta_full), np.sin(theta_full), 'k-', linewidth=3, zorder=5)

    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.7, 1.4)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title("Taijitu (Ming-dynasty form)\nThe symbol on Bohr's 1947 coat of arms",
                  fontsize=14, fontweight='bold', pad=10)
    ax1.text(0, -1.5, '"Contraria sunt complementa"\n(Opposites are complementary)',
             ha='center', fontsize=11, style='italic')

    # --- Right: Wave-particle complementarity (polar plot) ---
    ax2.remove()  # Remove the Cartesian axes, replace with polar
    ax2 = fig.add_subplot(122, projection='polar')

    theta_wave = np.linspace(0, np.pi, 100)
    r_wave = np.ones_like(theta_wave)
    ax2.fill_between(theta_wave, 0, r_wave, alpha=0.7, color='blue',
                     label='Wave nature')

    theta_particle = np.linspace(np.pi, 2 * np.pi, 100)
    r_particle = np.ones_like(theta_particle)
    ax2.fill_between(theta_particle, 0, r_particle, alpha=0.7, color='red',
                     label='Particle nature')

    ax2.set_ylim(0, 1.2)
    ax2.set_title('Wave-Particle Duality (Bohr, 1927)\nComplementarity Principle (schematic)',
                  fontsize=12, fontweight='bold', pad=25)
    ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.25, 1.15))

    plt.subplots_adjust(left=0.05, right=0.92, top=0.88, bottom=0.08, wspace=0.3)
    plt.savefig('taiji_complementarity.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("  Bohr's coat of arms (1947): taijitu (yin-yang) with the motto below")
    print("  Latin motto: 'Contraria sunt complementa'")
    print("  Interpretive mappings (this series' framing, not physics equivalences):")
    print("  Yin-Yang     <-> |0> and |1>")
    print("  Unity of Opp.<-> Superposition alpha|0>+beta|1>")
    print("  Complementarity <-> Non-commuting observables [x,p]=ihbar")


# ============================================================================
# Visualization 3: Observer Effect - Quantum vs Zen Parallel
# ============================================================================

def observer_effect_parallel():
    """
    A toy demonstration of the observer effect alongside the Zen teaching of
    'no subject-object split.' Both curves are hand-set illustrations, not
    measured data.

    Huineng, the Sixth Patriarch of Zen (Platform Sutra): two monks were
    arguing about whether the flag or the wind was moving. Huineng said:
    'Neither the flag nor the wind is moving. It is your mind that moves.'
    Compare this with Copenhagen's insistence that the observer cannot be
    separated from the observed system (an interpretive parallel).
    """
    print("\n[Visualization 3] Observer Effect: Quantum vs Zen")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    x = np.linspace(-5, 5, 1000)

    # --- Left: Without observer (wave interference) ---
    wave_pattern = np.cos(2 * np.pi * x) ** 2
    ax1.plot(x, wave_pattern, linewidth=2.5, color='#4ECDC4')
    ax1.fill_between(x, wave_pattern, alpha=0.3, color='#4ECDC4')
    ax1.set_xlabel('Position', fontsize=12)
    ax1.set_ylabel('Relative Probability (illustrative)', fontsize=12)
    ax1.set_title('WITHOUT Observer\nInterference Pattern (Wave)',
                  fontsize=13, fontweight='bold')
    ax1.grid(alpha=0.3)

    # --- Right: With observer (particle) ---
    particle_left = np.exp(-(x + 1.5) ** 2 / 0.5)
    particle_right = np.exp(-(x - 1.5) ** 2 / 0.5)
    particle_pattern = particle_left + particle_right
    particle_pattern = particle_pattern / np.max(particle_pattern)

    ax2.plot(x, particle_pattern, linewidth=2.5, color='#FF6B6B')
    ax2.fill_between(x, particle_pattern, alpha=0.3, color='#FF6B6B')
    ax2.set_xlabel('Position', fontsize=12)
    ax2.set_ylabel('Relative Count (illustrative)', fontsize=12)
    ax2.set_title('WITH Observer\nTwo Peaks (Particle)',
                  fontsize=13, fontweight='bold')
    ax2.grid(alpha=0.3)

    fig.text(0.5, 0.01,
             'Illustrative curves with hand-set parameters; not measured data.',
             ha='center', fontsize=10)
    plt.subplots_adjust(left=0.07, right=0.97, top=0.90, bottom=0.14, wspace=0.25)
    plt.savefig('observer_effect_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("  Copenhagen Interpretation:")
    print("    - Without which-path information: interference pattern (wave-like)")
    print("    - With a which-path measurement: no interference (particle-like);")
    print("      Copenhagen describes this as wave function collapse")
    print("  Zen parallel (interpretive):")
    print("    - Huineng: 'Neither flag nor wind moves. Your mind moves.'")
    print("    - Before naming: no distinction; after naming: fixed categories")


# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...\n")

double_slit_comparison()
taiji_complementarity()
observer_effect_parallel()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. double_slit_observer_effect.png  - Observed vs unobserved")
print("  2. taiji_complementarity.png        - Yin-Yang & wave-particle duality")
print("  3. observer_effect_comparison.png   - Observer effect parallel")
print()
print("Illustrative curves only: every input is hand-set, nothing is measured.")
print()
print("Key parallels between Copenhagen and Kyoto")
print("(interpretive analogies, this series' framing rather than scientific findings):")
print("  - No definite state before measurement <-> No fixed nature before naming")
print("  - Observer effect <-> No subject-object split")
print("  - Complementarity <-> Non-duality")
print("  - Probabilistic interpretation <-> Dependent origination")
print("  - No objective reality (Copenhagen reading; other interpretations disagree)")
print("      <-> No inherent nature (emptiness)")
print("=" * 70)
