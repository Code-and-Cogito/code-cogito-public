"""
The Eve of the Quantum Revolution -- When Newton's Universe Began to Crumble
Season 2 Article 01: Free Version

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #01/12

This script recreates three historic physics discoveries using Python:
  1. Black-body radiation: the Ultraviolet Catastrophe vs Planck's quantum rescue
  2. The photoelectric effect: Einstein's light-quantum hypothesis
  3. The death of determinism: 240 years from Newton to Heisenberg

Requirements:
    pip install numpy matplotlib scipy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# ---------------------------------------------------------------------------
# Font configuration
# ---------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("The Eve of the Quantum Revolution")
print("Season 2 Article 01 -- Free Version")
print("Series: Quantum Mechanics Meets Eastern Philosophy #01/12")
print("=" * 70)
print()

# ===========================================================================
# Model 1: Black-Body Radiation -- Visualizing the "Ultraviolet Catastrophe"
# ===========================================================================

def planck_law(wavelength, T):
    """Planck's law (quantum theory)"""
    return (8 * np.pi * h * c / wavelength**5) / (np.exp(h * c / (wavelength * k * T)) - 1)


def rayleigh_jeans_law(wavelength, T):
    """Rayleigh-Jeans law (classical theory)"""
    return 8 * np.pi * k * T / wavelength**4


def visualize_blackbody_radiation():
    """Visualize black-body radiation: classical vs quantum at T=5000K."""

    print("\n[Model 1] Black-Body Radiation at 5000 K")
    print("-" * 70)

    wavelength_nm = np.linspace(100, 3000, 1000)
    wavelength_m = wavelength_nm * 1e-9
    T = 5000  # Approximate surface temperature of the Sun

    planck_intensity = planck_law(wavelength_m, T)
    rayleigh_intensity = rayleigh_jeans_law(wavelength_m, T)

    fig, ax = plt.subplots(figsize=(14, 9))

    # Quantum theory (blue solid line)
    ax.plot(wavelength_nm, planck_intensity * 1e-13,
            'b-', linewidth=2.5, label="Planck's Law (Quantum Theory)")

    # Classical theory (red dashed line) -- only long wavelengths; short wavelengths blow up
    mask = wavelength_nm > 500
    ax.plot(wavelength_nm[mask], rayleigh_intensity[mask] * 1e-13,
            'r--', linewidth=2, label='Rayleigh-Jeans Law (Classical Theory)')

    # UV Catastrophe zone
    uv_region = wavelength_nm < 400
    ax.fill_between(wavelength_nm[uv_region], 0,
                    np.max(planck_intensity * 1e-13) * 1.2,
                    alpha=0.2, color='purple',
                    label='UV Catastrophe Zone (classical prediction: infinity)')

    # Visible light region
    visible_region = (wavelength_nm >= 380) & (wavelength_nm <= 750)
    ax.fill_between(wavelength_nm[visible_region], 0,
                    np.max(planck_intensity * 1e-13) * 1.2,
                    alpha=0.1, color='yellow', label='Visible Light Region')

    ax.set_xlabel('Wavelength (nm)', fontsize=14)
    ax.set_ylabel('Radiation Intensity (arbitrary units)', fontsize=14)
    ax.set_title(
        f'Black-Body Radiation: The "Ultraviolet Catastrophe" vs Quantum Rescue\n'
        f'Temperature T = {T} K',
        fontsize=16, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(100, 2000)
    ax.set_ylim(0, np.max(planck_intensity * 1e-13) * 1.1)

    ax.text(200, np.max(planck_intensity * 1e-13) * 0.85,
            'Classical theory predicts\ninfinite intensity here!\n-> "Ultraviolet Catastrophe"',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

    ax.text(850, np.max(planck_intensity * 1e-13) * 0.55,
            "Planck's formula matches experiment\n-> Energy must be quantized!",
            fontsize=11, bbox=dict(boxstyle='round', facecolor='blue', alpha=0.3))

    plt.subplots_adjust(left=0.10, right=0.95, top=0.90, bottom=0.10)
    plt.savefig('blackbody_radiation.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Verify with Wien's displacement law and Stefan-Boltzmann law
    peak_wavelength = 2.898e-3 / T
    print(f"\n[Wien's Displacement Law]")
    print(f"  Temperature T = {T} K")
    print(f"  Peak wavelength lambda_max = {peak_wavelength*1e9:.1f} nm")

    stefan_boltzmann = 5.67e-8
    total_power = stefan_boltzmann * T**4
    print(f"\n[Stefan-Boltzmann Law]")
    print(f"  Total radiated power proportional to T^4 = {total_power:.2e} W/m2")


# ===========================================================================
# Model 2: The Photoelectric Effect -- Einstein's Light Quanta
# ===========================================================================

def photoelectric_effect_simulation():
    """Photoelectric effect simulation with five metals."""

    print("\n[Model 2] Photoelectric Effect")
    print("-" * 70)

    metals = {
        'Sodium (Na)': 2.28,
        'Aluminum (Al)': 4.08,
        'Copper (Cu)': 4.70,
        'Zinc (Zn)': 4.31,
        'Silver (Ag)': 4.73
    }

    wavelengths = np.linspace(200, 600, 100)
    frequencies = c / (wavelengths * 1e-9)
    photon_energies = h * frequencies / 1.6e-19  # Convert to eV

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 9))

    # --- Left plot: Cutoff frequencies for different metals ---
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    for (metal, work_function), color in zip(metals.items(), colors):
        kinetic_energy = photon_energies - work_function
        kinetic_energy[kinetic_energy < 0] = 0

        ax1.plot(wavelengths, kinetic_energy,
                 linewidth=2, label=f'{metal} (W0={work_function} eV)', color=color)

        cutoff_wavelength = h * c / (work_function * 1.6e-19) * 1e9
        ax1.axvline(cutoff_wavelength, color=color, linestyle='--', alpha=0.5)

    # Collect cutoff wavelengths and stagger labels to avoid overlap
    cutoff_data = []
    for (metal, work_function), color in zip(metals.items(), colors):
        cutoff_wavelength = h * c / (work_function * 1.6e-19) * 1e9
        cutoff_data.append((cutoff_wavelength, metal.split()[0], color))

    # Sort by wavelength so we can stagger
    cutoff_data.sort(key=lambda x: x[0])
    y_positions = [4.0, 4.6, 5.2, 4.0, 4.6]  # stagger heights
    for i, (cw, name, color) in enumerate(cutoff_data):
        ax1.annotate(f'{cw:.0f}nm',
                     xy=(cw, 0), xytext=(cw, y_positions[i]),
                     fontsize=8, color=color, ha='center',
                     arrowprops=dict(arrowstyle='->', color=color, alpha=0.6))

    ax1.set_xlabel('Wavelength of Light (nm)', fontsize=13)
    ax1.set_ylabel('Photoelectron Kinetic Energy (eV)', fontsize=13)
    ax1.set_title('Photoelectric Effect: Frequency Determines Electron Energy\n'
                  'KE = hv - W0',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=9, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(200, 600)
    ax1.set_ylim(0, 6)
    ax1.axvspan(380, 600, alpha=0.08, color='yellow')

    # --- Right plot: Light intensity vs number of electrons (not energy) ---
    intensities = np.array([1, 2, 5, 10])
    wavelength_fixed = 300  # nm
    photon_energy_fixed = h * c / (wavelength_fixed * 1e-9) / 1.6e-19

    work_function_Na = metals['Sodium (Na)']

    if photon_energy_fixed > work_function_Na:
        electron_counts = intensities * 100
        electron_energy = photon_energy_fixed - work_function_Na

        bars = ax2.bar(intensities, electron_counts, width=0.8,
                       color='skyblue', edgecolor='navy', linewidth=2)

        for bar, count in zip(bars, electron_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
                     f'{int(count)} e-\n({electron_energy:.2f} eV)',
                     ha='center', fontsize=9,
                     bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    ax2.set_xlabel('Light Intensity (relative)', fontsize=13)
    ax2.set_ylabel('Number of Ejected Electrons', fontsize=13)
    ax2.set_title(
        f'Intensity Controls Electron Count (Not Energy)\n'
        f'Metal: Sodium, Wavelength: {wavelength_fixed} nm',
        fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_ylim(0, 1400)

    ax2.text(0.97, 0.97,
             'Key Insight:\n'
             'Higher intensity -> more electrons\n'
             'But each electron has the SAME energy!\n'
             'Electron energy depends only on frequency\n\n'
             'Classical wave theory cannot explain this!\n'
             '-> Light must be particles (photons)',
             fontsize=10, transform=ax2.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.subplots_adjust(left=0.07, right=0.97, top=0.88, bottom=0.10, wspace=0.25)
    plt.savefig('photoelectric_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --- Virtual lab printout ---
    print("\n" + "=" * 60)
    print("[Photoelectric Effect Virtual Lab]")
    print("=" * 60)

    chosen_metal = 'Zinc (Zn)'
    work_function = metals[chosen_metal]
    print(f"\nSelected: {chosen_metal}")
    print(f"Work function W0 = {work_function} eV")
    print(f"Cutoff wavelength lambda_0 = {h * c / (work_function * 1.6e-19) * 1e9:.1f} nm")

    test_wavelengths = [200, 300, 400, 500]
    print("\nExperimental Results:")
    print("-" * 60)
    print(f"{'Wavelength(nm)':<16} {'Photon E (eV)':<16} {'Electron KE(eV)':<16} {'Result'}")
    print("-" * 60)

    for wl in test_wavelengths:
        photon_e = h * c / (wl * 1e-9) / 1.6e-19
        ke = photon_e - work_function
        if ke > 0:
            result = "Electron ejected!"
        else:
            result = "No ejection"
        print(f"{wl:<16} {photon_e:<16.2f} {max(0, ke):<16.2f} {result}")


# ===========================================================================
# Model 3: The Death of Determinism -- From Newton to Heisenberg
# ===========================================================================

def determinism_timeline():
    """Visualize the transformation of physics' worldview over 240 years.
    Two-panel design: left = vertical timeline, right = certainty curve."""

    print("\n[Model 3] The Death of Determinism")
    print("-" * 70)

    events = [
        (1687, "Newton: Principia",          "Deterministic universe, F=ma",           'classical', 1.0),
        (1814, "Laplace's Demon",             "Give me initial conditions, I predict all", 'classical', 1.0),
        (1865, "Maxwell: Electromagnetism",    "Unified E, M, light -- universe is knowable", 'classical', 0.9),
        (1900, "Planck: Quantum Hypothesis",   "Energy is quantized: E=nhv",             'dawn',      0.5),
        (1905, "Einstein: Light Quanta",       "Light is particles: E=hv",               'dawn',      0.4),
        (1913, "Bohr: Atomic Model",           "Quantized orbits: n=1,2,3...",           'dawn',      0.3),
        (1923, "de Broglie: Matter Waves",     "Particles are waves: lambda=h/p",        'revolution', 0.2),
        (1925, "Heisenberg: Matrix Mechanics", "Farewell to visualization",              'revolution', 0.1),
        (1926, "Schrodinger: Wave Equation",   "Wave function psi, probability",         'revolution', 0.1),
        (1927, "Heisenberg: Uncertainty",      "Dx*Dp >= h-bar/2, certainty is dead",    'revolution', 0.0),
    ]

    era_colors = {
        'classical':  '#4A90D9',
        'dawn':       '#F5A623',
        'revolution': '#D0021B',
    }
    era_bg = {
        'classical':  '#DAEAF6',
        'dawn':       '#FFF3D6',
        'revolution': '#FDDEDE',
    }

    fig, (ax_timeline, ax_curve) = plt.subplots(1, 2, figsize=(22, 14),
                                                 gridspec_kw={'width_ratios': [3, 2]})

    # ===== LEFT PANEL: Vertical Timeline =====
    n = len(events)
    y_positions = list(range(n - 1, -1, -1))  # top to bottom

    for i, (year, person, desc, era, cert) in enumerate(events):
        y = y_positions[i]
        color = era_colors[era]
        bg = era_bg[era]

        # Timeline dot
        ax_timeline.scatter(0.3, y, s=200, c=color, edgecolor='white',
                           linewidth=2, zorder=5)

        # Year label (left side)
        ax_timeline.text(0.15, y, str(year), fontsize=13, fontweight='bold',
                        ha='right', va='center', color=color)

        # Event card (right side)
        ax_timeline.text(0.5, y + 0.12, person, fontsize=12, fontweight='bold',
                        ha='left', va='center', color='#333333')
        ax_timeline.text(0.5, y - 0.18, desc, fontsize=10,
                        ha='left', va='center', color='#666666', style='italic')

        # Background band
        ax_timeline.axhspan(y - 0.45, y + 0.45, xmin=0.0, xmax=1.0,
                           facecolor=bg, alpha=0.4, zorder=0)

    # Vertical line connecting dots
    ax_timeline.plot([0.3, 0.3], [-0.4, n - 0.6], color='#999999',
                    linewidth=2, zorder=1)

    # Era labels on the far left
    ax_timeline.text(-0.15, 8, 'CLASSICAL\nERA', fontsize=11, fontweight='bold',
                    ha='center', va='center', color=era_colors['classical'],
                    bbox=dict(boxstyle='round,pad=0.4', facecolor=era_bg['classical'], alpha=0.8))
    ax_timeline.text(-0.15, 5, 'QUANTUM\nDAWN', fontsize=11, fontweight='bold',
                    ha='center', va='center', color=era_colors['dawn'],
                    bbox=dict(boxstyle='round,pad=0.4', facecolor=era_bg['dawn'], alpha=0.8))
    ax_timeline.text(-0.15, 1.5, 'QUANTUM\nREVOLUTION', fontsize=11, fontweight='bold',
                    ha='center', va='center', color=era_colors['revolution'],
                    bbox=dict(boxstyle='round,pad=0.4', facecolor=era_bg['revolution'], alpha=0.8))

    ax_timeline.set_xlim(-0.4, 2.2)
    ax_timeline.set_ylim(-0.8, n - 0.2)
    ax_timeline.axis('off')
    ax_timeline.set_title('Timeline of Events', fontsize=16, fontweight='bold', pad=15)

    # ===== RIGHT PANEL: Certainty Curve =====
    years = [e[0] for e in events]
    certs = [e[4] for e in events]
    colors_list = [era_colors[e[3]] for e in events]

    ax_curve.plot(years, certs, 'k-', linewidth=2.5, alpha=0.7, zorder=2)
    ax_curve.scatter(years, certs, c=colors_list, s=180,
                    edgecolor='black', linewidth=1.5, zorder=5)

    # Background era shading
    ax_curve.axvspan(1680, 1900, facecolor=era_bg['classical'], alpha=0.5)
    ax_curve.axvspan(1900, 1923, facecolor=era_bg['dawn'], alpha=0.5)
    ax_curve.axvspan(1923, 1935, facecolor=era_bg['revolution'], alpha=0.5)

    # Only label a few key points to avoid clutter
    key_labels = {
        1687: 'Newton',
        1900: 'Planck',
        1927: 'Heisenberg',
    }
    for year, cert in zip(years, certs):
        if year in key_labels:
            ax_curve.annotate(key_labels[year],
                            xy=(year, cert),
                            xytext=(8, 12), textcoords='offset points',
                            fontsize=10, fontweight='bold',
                            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    ax_curve.set_xlabel('Year', fontsize=13)
    ax_curve.set_ylabel('Degree of "Certainty"', fontsize=13)
    ax_curve.set_title('The Fall of Certainty', fontsize=16, fontweight='bold', pad=15)
    ax_curve.set_xlim(1680, 1935)
    ax_curve.set_ylim(-0.15, 1.15)
    ax_curve.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax_curve.set_yticklabels(['Fully\nUncertain', '', 'Partially\nCertain', '', 'Fully\nCertain'])
    ax_curve.grid(True, alpha=0.3)

    # Arrow annotation for the dramatic drop
    ax_curve.annotate('',
                     xy=(1927, 0.0), xycoords='data',
                     xytext=(1687, 1.0), textcoords='data',
                     arrowprops=dict(arrowstyle='->', color='red',
                                    lw=2, alpha=0.3,
                                    connectionstyle='arc3,rad=-0.2'))
    ax_curve.text(1810, 0.3, '240 years:\nfrom certainty\nto uncertainty',
                 fontsize=11, ha='center', color='red', alpha=0.6,
                 style='italic')

    fig.suptitle('From Certainty to Uncertainty: 240 Years of Shifting Worldviews in Physics',
                fontsize=18, fontweight='bold', y=0.98)
    plt.subplots_adjust(left=0.03, right=0.97, top=0.92, bottom=0.04, wspace=0.15)
    plt.savefig('determinism_timeline.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --- Worldview comparison table ---
    print("\n" + "=" * 70)
    print("[Three Worldviews in Physics]")
    print("=" * 70)

    worldviews = [
        {'Era': 'Classical (1687-1900)', 'Key Figures': 'Newton, Laplace',
         'Core Belief': 'Determinism', 'Universe Metaphor': 'Precision clockwork',
         'Causality': 'Past determines future',
         'Free Will': 'An illusion (all is predetermined)',
         'Role of God': 'The Prime Mover'},
        {'Era': 'Quantum Dawn (1900-1925)', 'Key Figures': 'Planck, Einstein',
         'Core Belief': 'Energy is discontinuous', 'Universe Metaphor': 'A glitching clock',
         'Causality': 'Still causal, but with limits',
         'Free Will': 'Uncertain',
         'Role of God': '"Does not play dice" (Einstein insisted)'},
        {'Era': 'Quantum Revolution (1925-present)', 'Key Figures': 'Heisenberg, Schrodinger, Bohr',
         'Core Belief': 'Fundamental uncertainty', 'Universe Metaphor': 'A probability cloud',
         'Causality': 'Only probabilities, no certainties',
         'Free Will': 'Possibly real (room exists)',
         'Role of God': '"Does play dice" (Bohr)'}
    ]

    for wv in worldviews:
        print(f"\n[{wv['Era']}]")
        for key, value in wv.items():
            if key != 'Era':
                print(f"  {key:<18}: {value}")


# ===========================================================================
# Run all models
# ===========================================================================

print("\nGenerating visualizations...\n")

visualize_blackbody_radiation()
photoelectric_effect_simulation()
determinism_timeline()

# ===========================================================================
# Summary
# ===========================================================================

print("\n" + "=" * 70)
print("All visualizations complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. blackbody_radiation.png    -- Classical vs Quantum at 5000 K")
print("  2. photoelectric_effect.png   -- Five metals + intensity analysis")
print("  3. determinism_timeline.png   -- 240 years, 10 key events")
print()
print("Key takeaways:")
print("  - Planck's constant h = 6.626e-34 J*s changed physics forever")
print("  - Light is both wave and particle (wave-particle duality)")
print("  - The universe is not deterministic; uncertainty is fundamental")
print("  - Eastern philosophy (Tao Te Ching, Heart Sutra) resonates with")
print("    quantum insights about the limits of language and knowledge")
print("=" * 70)
