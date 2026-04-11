"""
Copenhagen Interpretation vs Kyoto School - Free Version
Season 2, Article 02: The Double-Slit Experiment, Yin-Yang Complementarity,
and the Observer Effect

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #02/12

This standalone free script includes:
- Double-slit interference pattern (observed vs unobserved)
- Taiji (yin-yang) diagram representing Bohr's complementarity principle
- Observer effect comparison

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

def double_slit_comparison():
    """
    Double-slit experiment: side-by-side comparison of wave behavior
    (unobserved) vs particle behavior (observed).

    When we do not observe which slit the photon passes through, two waves
    superpose and produce an interference pattern. The moment we place a
    detector to determine which slit was chosen, the interference vanishes.
    This is the core shock of the Copenhagen Interpretation: observation
    itself changes physical reality.
    """
    print("\n[Visualization 1] Double-Slit Experiment: Observer Effect")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    y = np.linspace(-5, 5, 500)

    # --- Left panel: Unobserved (wave behavior) ---
    slit1_pos = -1.0
    slit2_pos = 1.0
    wavelength = 0.5

    wave1 = np.sin(2 * np.pi * (y - slit1_pos) / wavelength)
    wave2 = np.sin(2 * np.pi * (y - slit2_pos) / wavelength)

    total_wave = wave1 + wave2
    intensity_unobs = np.abs(total_wave) ** 2
    intensity_unobs = intensity_unobs / np.max(intensity_unobs)

    ax1.fill_between(y, 0, intensity_unobs, alpha=0.7, color='blue')
    ax1.plot(y, intensity_unobs, 'b-', linewidth=2)
    ax1.set_xlabel('Screen Position', fontsize=13)
    ax1.set_ylabel('Photon Hit Count', fontsize=13)
    ax1.set_title('Unobserved: Interference Pattern Appears (Wave)',
                  fontsize=13, fontweight='bold', color='blue')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 1.35)
    ax1.text(0, 1.25, 'Multiple peaks = Interference\nPhoton behaves as a "wave"',
             ha='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # --- Right panel: Observed (particle behavior) ---
    slit1_pattern = np.exp(-(y - (-1.0)) ** 2 / 0.5)
    slit2_pattern = np.exp(-(y - (1.0)) ** 2 / 0.5)

    intensity_obs = slit1_pattern + slit2_pattern
    intensity_obs = intensity_obs / np.max(intensity_obs)

    ax2.fill_between(y, 0, intensity_obs, alpha=0.7, color='red')
    ax2.plot(y, intensity_obs, 'r-', linewidth=2)
    ax2.set_xlabel('Screen Position', fontsize=13)
    ax2.set_ylabel('Photon Hit Count', fontsize=13)
    ax2.set_title('Observed: Interference Vanishes (Particle)',
                  fontsize=13, fontweight='bold', color='red')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 1.35)
    ax2.text(0, 1.25, 'Two peaks = No interference\nPhoton behaves as a "particle"',
             ha='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    fig.text(0.5, 0.01,
             'Key insight: Observation changes the outcome! '
             'This is not measurement error -- it is the nature of quantum reality.\n'
             'Zen perspective: Observer and observed were never separate to begin with.',
             ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.subplots_adjust(bottom=0.16, left=0.07, right=0.97, top=0.92, wspace=0.25)
    plt.savefig('double_slit_observer_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("  - Left panel: clear interference fringes (multiple peaks)")
    print("  - Right panel: two peaks only, no interference")
    print("  Copenhagen: observation changes reality")
    print("  Zen:        observer and observed were never separate")


# ============================================================================
# Visualization 2: Taiji (Yin-Yang) Symbol - Bohr's Complementarity
# ============================================================================

def taiji_complementarity():
    """
    The Taiji (yin-yang) symbol that Bohr chose for his coat of arms in 1947,
    with the Latin motto 'Contraria sunt complementa' (Opposites are
    complementary).

    Bohr recognized that yin-yang precisely expresses the mathematical
    structure of complementarity: wave and particle are not contradictions
    but complementary aspects of a single reality.
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
    ax1.set_title("Taiji Symbol\nBohr's Coat of Arms (1947)",
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
    ax2.set_title('Wave-Particle Duality (Bohr, 1927)\nComplementarity Principle',
                  fontsize=12, fontweight='bold', pad=25)
    ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.25, 1.15))

    plt.subplots_adjust(left=0.05, right=0.92, top=0.88, bottom=0.08, wspace=0.3)
    plt.savefig('taiji_complementarity.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("  Bohr's coat of arms: Taiji (yin-yang)")
    print("  Latin motto: 'Contraria sunt complementa'")
    print("  Yin-Yang     <-> |0> and |1>")
    print("  Unity of Opp.<-> Superposition alpha|0>+beta|1>")
    print("  Complementarity <-> Non-commuting observables [x,p]=ihbar")


# ============================================================================
# Visualization 3: Observer Effect - Quantum vs Zen Parallel
# ============================================================================

def observer_effect_parallel():
    """
    A simple demonstration of the observer effect alongside the Zen teaching
    of 'no subject-object split.'

    Huineng, the Sixth Patriarch of Zen, was asked whether the flag or the
    wind is moving. He answered: 'Neither the flag nor the wind is moving.
    It is your mind that moves.' Compare this with Copenhagen's insistence
    that the observer cannot be separated from the observed system.
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
    ax1.set_ylabel('Probability', fontsize=12)
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
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_title('WITH Observer\nTwo Peaks (Particle)',
                  fontsize=13, fontweight='bold')
    ax2.grid(alpha=0.3)

    plt.subplots_adjust(left=0.07, right=0.97, top=0.90, bottom=0.10, wspace=0.25)
    plt.savefig('observer_effect_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("  Copenhagen Interpretation:")
    print("    - Without observation: particle behaves as wave")
    print("    - With observation: wave function collapses to particle")
    print("  Zen parallel:")
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
print("Key parallels between Copenhagen and Kyoto:")
print("  - No definite state before measurement <-> No fixed nature before naming")
print("  - Observer effect <-> No subject-object split")
print("  - Complementarity <-> Non-duality")
print("  - Probabilistic interpretation <-> Dependent origination")
print("  - No objective reality <-> No inherent nature (emptiness)")
print("=" * 70)
