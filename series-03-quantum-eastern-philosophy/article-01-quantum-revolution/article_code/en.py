# Code & Cogito: The Eve of the Quantum Revolution — When Newton's Universe Began to Crumble
# Article: https://code-cogito.com/en/quantum-revolution-newton-universe-collapse-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
# | nabla·E = rho/epsilon_0        (Gauss's law)
# | nabla·B = 0                    (No magnetic monopoles)
# | nabla x E = -dB/dt             (Faraday's law)
# | nabla x B = mu_0 J + mu_0 epsilon_0 dE/dt  (Ampere-Maxwell law)

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

def planck_law(wavelength, T):
    """Planck's law (quantum theory)"""
    return (8 * np.pi * h * c / wavelength**5) / (np.exp(h * c / (wavelength * k * T)) - 1)

def rayleigh_jeans_law(wavelength, T):
    """Rayleigh-Jeans law (classical theory)"""
    return 8 * np.pi * k * T / wavelength**4

def visualize_blackbody_radiation():
    """Visualize black-body radiation: classical vs quantum"""

    wavelength_nm = np.linspace(100, 3000, 1000)
    wavelength_m = wavelength_nm * 1e-9
    T = 5000  # Approximate surface temperature of the Sun

    planck_intensity = planck_law(wavelength_m, T)
    rayleigh_intensity = rayleigh_jeans_law(wavelength_m, T)

    fig, ax = plt.subplots(figsize=(12, 8))

    # Quantum theory (blue solid line)
    ax.plot(wavelength_nm, planck_intensity * 1e-13,
            'b-', linewidth=2.5, label="Planck's Law (Quantum Theory)")

    # Classical theory (red dashed line) — only for long wavelengths; short wavelengths blow up
    mask = wavelength_nm > 500
    ax.plot(wavelength_nm[mask], rayleigh_intensity[mask] * 1e-13,
            'r--', linewidth=2, label='Rayleigh-Jeans Law (Classical Theory)')

    # Mark the ultraviolet catastrophe zone and visible light region
    uv_region = wavelength_nm < 400
    ax.fill_between(wavelength_nm[uv_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.2, color='purple',
                     label='UV Catastrophe Zone (classical prediction: infinity)')

    visible_region = (wavelength_nm >= 380) & (wavelength_nm <= 750)
    ax.fill_between(wavelength_nm[visible_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.1, color='yellow', label='Visible Light Region')

    ax.set_xlabel('Wavelength (nm)', fontsize=14)
    ax.set_ylabel('Radiation Intensity (arbitrary units)', fontsize=14)
    ax.set_title(f'Black-Body Radiation: The "Ultraviolet Catastrophe" vs Quantum Rescue\nTemperature T = {T} K',
                 fontsize=16, fontweight='bold')
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(100, 2000)
    ax.set_ylim(0, np.max(planck_intensity * 1e-13) * 1.1)

    ax.text(200, np.max(planck_intensity * 1e-13) * 0.9,
            'Classical theory predicts\ninfinite intensity here!\n-> "Ultraviolet Catastrophe"',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

    ax.text(800, np.max(planck_intensity * 1e-13) * 0.6,
            "Planck's formula matches experiment\n-> Energy must be quantized!",
            fontsize=11, bbox=dict(boxstyle='round', facecolor='blue', alpha=0.3))

    plt.tight_layout()
    plt.savefig('blackbody_radiation.png', dpi=300, bbox_inches='tight')
    plt.show()

    peak_wavelength = 2.898e-3 / T
    print(f"\n[Wien's Displacement Law]")
    print(f"Temperature T = {T} K")
    print(f"Peak wavelength lambda_max = {peak_wavelength*1e9:.1f} nm")

    stefan_boltzmann = 5.67e-8
    total_power = stefan_boltzmann * T**4
    print(f"\n[Stefan-Boltzmann Law]")
    print(f"Total radiated power proportional to T^4 = {total_power:.2e} W/m2")

# Run
visualize_blackbody_radiation()

# | def photoelectric_effect_simulation():
# |     """Photoelectric effect simulation"""
# | 
# |     metals = {
# |         'Sodium (Na)': 2.28,
# |         'Aluminum (Al)': 4.08,
# |         'Copper (Cu)': 4.70,
# |         'Zinc (Zn)': 4.31,
# |         'Silver (Ag)': 4.73
# |     }
# | 
# |     wavelengths = np.linspace(200, 600, 100)
# |     frequencies = c / (wavelengths * 1e-9)
# |     photon_energies = h * frequencies / 1.6e-19  # Convert to eV

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Left plot: Cutoff frequencies for different metals
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    for (metal, work_function), color in zip(metals.items(), colors):
        kinetic_energy = photon_energies - work_function
        kinetic_energy[kinetic_energy < 0] = 0

        ax1.plot(wavelengths, kinetic_energy,
                linewidth=2, label=f'{metal} (W0={work_function} eV)', color=color)

        cutoff_wavelength = h * c / (work_function * 1.6e-19) * 1e9
        ax1.axvline(cutoff_wavelength, color=color, linestyle='--', alpha=0.5)
        ax1.text(cutoff_wavelength, 5, f'{cutoff_wavelength:.0f}nm',
                rotation=90, va='bottom', fontsize=9, color=color)

    ax1.set_xlabel('Wavelength of Light (nm)', fontsize=13)
    ax1.set_ylabel('Photoelectron Kinetic Energy (eV)', fontsize=13)
    ax1.set_title('Photoelectric Effect: Frequency Determines Electron Energy\nKE = hv - W0',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(200, 600)
    ax1.set_ylim(0, 6)
    ax1.axvspan(380, 750, alpha=0.1, color='yellow', label='Visible Light')

    # Right plot: Light intensity vs number of electrons (not energy)
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
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                    f'{int(count)} electrons\neach at {electron_energy:.2f} eV',
                    ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    ax2.set_xlabel('Light Intensity (relative)', fontsize=13)
    ax2.set_ylabel('Number of Ejected Electrons', fontsize=13)
    ax2.set_title(f'Photoelectric Effect: Intensity Controls Electron Count (Not Energy)\nMetal: Sodium, Wavelength: {wavelength_fixed} nm',
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    ax2.text(6, 800,
            'Key Insight:\n'
            'Higher intensity -> more electrons\n'
            'But each electron has the SAME energy!\n'
            'Electron energy depends only on frequency\n\n'
            'Classical wave theory cannot explain this!\n'
            '-> Light must be particles (photons)',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('photoelectric_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*60)
    print("[Photoelectric Effect Virtual Lab]")
    print("="*60)

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

# Run
photoelectric_effect_simulation()

# | Selected: Zinc (Zn)
# | Work function W0 = 4.31 eV
# | Cutoff wavelength lambda_0 = 287.7 nm
# | 
# | Wavelength(nm)   Photon E (eV)    Electron KE(eV)  Result
# | ------------------------------------------------------------
# | 200              6.20             1.89             Electron ejected!
# | 300              4.14             0.00             No ejection
# | 400              3.10             0.00             No ejection
# | 500              2.48             0.00             No ejection

# | def determinism_timeline():
# |     """Visualize the transformation of physics' worldview"""
# | 
# |     fig, ax = plt.subplots(figsize=(14, 10))
# | 
# |     events = [
# |         (1687, "Newton\nPrincipia", "Deterministic universe\nF=ma", 'blue', 1.0),
# |         (1814, "Laplace's\nDemon", "Give me initial conditions\nI know everything", 'blue', 1.0),
# |         (1865, "Maxwell\nElectromagnetics", "Unified E, M, light\nUniverse is knowable", 'blue', 0.9),
# |         (1900, "Planck\nQuantum Hypothesis", "Energy is quantized\nE=nhv", 'orange', 0.5),
# |         (1905, "Einstein\nLight Quanta", "Light is particles\nE=hv", 'orange', 0.4),
# |         (1913, "Bohr\nAtomic Model", "Quantized electron orbits\nn=1,2,3...", 'orange', 0.3),
# |         (1923, "de Broglie\nMatter Waves", "Particles are waves too\nlambda=h/p", 'red', 0.2),
# |         (1925, "Heisenberg\nMatrix Mechanics", "Farewell to visualization\nEverything is matrices", 'red', 0.1),
# |         (1926, "Schrodinger\nWave Mechanics", "Wave function psi\nProbability interpretation", 'red', 0.1),
# |         (1927, "Heisenberg\nUncertainty Principle", "Dx*Dp >= h-bar/2\nCertainty is dead", 'red', 0.0)
# |     ]

    years = [e[0] for e in events]
    certainties = [e[4] for e in events]

    # Background gradient: blue -> orange -> red
    for i in range(len(events)-1):
        ax.fill_between([events[i][0], events[i+1][0]], 0, 1,
                        alpha=0.3, color=events[i][3])

    # Certainty curve
    ax.plot(years, certainties, 'k-', linewidth=3, label='"Certainty" Index')
    ax.scatter(years, certainties, c=[e[3] for e in events],
              s=300, edgecolor='black', linewidth=2, zorder=5)

    # Annotate events
    for year, person, description, color, certainty in events:
        ax.text(year, certainty + 0.1, person,
               ha='center', fontsize=10, fontweight='bold')
        ax.text(year, certainty - 0.15, description,
               ha='center', fontsize=8, style='italic',
               bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

    # Three eras
    ax.text(1750, 0.95, 'Classical Era\n"The universe is a clock"',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(1910, 0.45, 'Quantum Dawn\n"Energy is discrete"',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    ax.text(1926, 0.05, 'Quantum Revolution\n"Uncertainty is fundamental"',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

    ax.set_xlim(1680, 1935)
    ax.set_ylim(-0.2, 1.15)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Degree of "Certainty"', fontsize=14)
    ax.set_title('From Certainty to Uncertainty: 240 Years of Shifting Worldviews in Physics',
                fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12, loc='upper right')
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_yticklabels(['Fully Uncertain\n(Quantum World)', 'Partially Certain\n(Transitional)', 'Fully Certain\n(Classical World)'])

    plt.tight_layout()
    plt.savefig('determinism_timeline.png', dpi=300, bbox_inches='tight')
    plt.show()

# |     print("\n" + "="*70)
# |     print("[Three Worldviews in Physics]")
# |     print("="*70)
# | 
# |     worldviews = [
# |         {'Era': 'Classical (1687-1900)', 'Key Figures': 'Newton, Laplace',
# |          'Core Belief': 'Determinism', 'Universe Metaphor': 'Precision clockwork',
# |          'Causality': 'Past determines future', 'Free Will': 'An illusion (all is predetermined)',
# |          'Role of God': 'The Prime Mover'},
# |         {'Era': 'Quantum Dawn (1900-1925)', 'Key Figures': 'Planck, Einstein',
# |          'Core Belief': 'Energy is discontinuous', 'Universe Metaphor': 'A glitching clock',
# |          'Causality': 'Still causal, but with limits', 'Free Will': 'Uncertain',
# |          'Role of God': '"Does not play dice" (Einstein insisted)'},
# |         {'Era': 'Quantum Revolution (1925-present)', 'Key Figures': 'Heisenberg, Schrodinger, Bohr',
# |          'Core Belief': 'Fundamental uncertainty', 'Universe Metaphor': 'A probability cloud',
# |          'Causality': 'Only probabilities, no certainties', 'Free Will': 'Possibly real (room exists)',
# |          'Role of God': '"Does play dice" (Bohr)'}
# |     ]
# | 
# |     for wv in worldviews:
# |         print(f"\n[{wv['Era']}]")
# |         for key, value in wv.items():
# |             if key != 'Era':
# |                 print(f"  {key:<18}: {value}")
# | 
# | # Run
# | determinism_timeline()
