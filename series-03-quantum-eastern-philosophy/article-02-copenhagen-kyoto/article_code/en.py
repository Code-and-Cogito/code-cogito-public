# Code & Cogito: The Copenhagen Interpretation vs. the Kyoto School — A Dialogue Between Two Wisdoms
# Article: https://code-cogito.com/en/copenhagen-interpretation-vs-kyoto-school-en/
# All the code blocks of the article, in order. Program output is kept as comments.

# | |ψ⟩ = Σ cᵢ|φᵢ⟩

# | Δx · Δp ≥ ℏ/2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class DoubleSlit:
    """
    Double-slit experiment simulation.
    Demonstrates the dramatic difference between observed and unobserved behavior.
    """

    def __init__(self):
        self.observed = False
        self.screen_resolution = 500

    def simulate_unobserved(self):
        """Unobserved: photon behaves as a wave, producing interference fringes"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # Two slit sources
        slit1_pos = -1.0
        slit2_pos = 1.0
        wavelength = 0.5

        # Waves from each slit
        wave1 = np.sin(2 * np.pi * (y - slit1_pos) / wavelength)
        wave2 = np.sin(2 * np.pi * (y - slit2_pos) / wavelength)

        # Superposition (interference)
        total_wave = wave1 + wave2
        intensity = np.abs(total_wave)**2
        intensity = intensity / np.max(intensity)

        return y, intensity

    def simulate_observed(self):
        """Observed: measuring which slit each photon passes through destroys interference"""
        y = np.linspace(-5, 5, self.screen_resolution)

        # After observation, each photon passes through only one slit
        slit1_pattern = np.exp(-(y - (-1.0))**2 / 0.5)
        slit2_pattern = np.exp(-(y - (1.0))**2 / 0.5)

        # Simple addition (no interference)
        intensity = slit1_pattern + slit2_pattern
        intensity = intensity / np.max(intensity)

        return y, intensity

    def visualize_comparison(self):
        """Side-by-side comparison: observed vs. unobserved"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Left panel: unobserved (wave behavior)
        y_unobs, intensity_unobs = self.simulate_unobserved()
        ax1.fill_between(y_unobs, 0, intensity_unobs, alpha=0.7, color='blue')
        ax1.plot(y_unobs, intensity_unobs, 'b-', linewidth=2)
        ax1.set_xlabel('Screen Position', fontsize=13)
        ax1.set_ylabel('Photon Hit Count', fontsize=13)
        ax1.set_title('Unobserved: Interference Pattern Appears (Wave)',
                     fontsize=14, fontweight='bold', color='blue')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.2)
        ax1.text(0, 1.1, 'Multiple peaks = Interference\nPhoton behaves as a "wave"',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

        # Right panel: observed (particle behavior)
        y_obs, intensity_obs = self.simulate_observed()
        ax2.fill_between(y_obs, 0, intensity_obs, alpha=0.7, color='red')
        ax2.plot(y_obs, intensity_obs, 'r-', linewidth=2)
        ax2.set_xlabel('Screen Position', fontsize=13)
        ax2.set_ylabel('Photon Hit Count', fontsize=13)
        ax2.set_title('Observed: Interference Vanishes (Particle)',
                     fontsize=14, fontweight='bold', color='red')
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 1.2)
        ax2.text(0, 1.1, 'Two peaks = No interference\nPhoton behaves as a "particle"',
                ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        fig.text(0.5, 0.02,
                'Key insight: Observation changes the outcome! This is not measurement error — it is the nature of quantum reality.\n'
                'Zen perspective: Observer and observed were never separate to begin with.',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.12)
        plt.savefig('double_slit_observer_effect.png', dpi=300, bbox_inches='tight')
        plt.show()

# Run
experiment = DoubleSlit()
experiment.visualize_comparison()

print("\n" + "="*70)
print("[ Double-Slit Experiment: The Observer Effect ]")
print("="*70)
print("Quantum mechanics: Observation changes reality")
print("Zen Buddhism:      Observer and observed were never separate")

def taiji_and_complementarity():
    """Yin-yang diagram and the complementarity principle"""
    fig = plt.figure(figsize=(16, 6))

    # Left panel: Classical yin-yang (taijitu)
    ax1 = fig.add_subplot(131)
    theta = np.linspace(0, 2*np.pi, 1000)

    # S-curve boundary
    r_yin = 1 + 0.5 * np.sin(theta)
    r_yang = 1 - 0.5 * np.sin(theta)

    # Draw yin and yang
    ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
            color='black', alpha=0.8)
    ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
            color='white', edgecolor='black', linewidth=2)

    # Yang within yin (white dot)
    circle_yang = plt.Circle((0, 0.5), 0.15, color='white', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yang)

    # Yin within yang (black dot)
    circle_yin = plt.Circle((0, -0.5), 0.15, color='black', ec='black', linewidth=1.5)
    ax1.add_patch(circle_yin)

    # Outer circle
    circle_outer = plt.Circle((0, 0), 1.5, fill=False, edgecolor='black', linewidth=3)
    ax1.add_patch(circle_outer)

    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Taijitu (Ming-dynasty form)\nUnity of Opposites',
                 fontsize=13, fontweight='bold')

    ax1.text(0, -2.3, 'Yang contains yin; yin contains yang\nOpposites are interdependent',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Middle panel: Wave-particle duality
    ax2 = fig.add_subplot(132, projection='polar')

    theta_wave = np.linspace(0, np.pi, 100)
    r_wave = np.ones_like(theta_wave)
    ax2.fill_between(theta_wave, 0, r_wave, alpha=0.7, color='blue', label='Wave nature')

    theta_particle = np.linspace(np.pi, 2*np.pi, 100)
    r_particle = np.ones_like(theta_particle)
    ax2.fill_between(theta_particle, 0, r_particle, alpha=0.7, color='red', label='Particle nature')

    ax2.set_ylim(0, 1.2)
    ax2.set_title('Wave-Particle Duality (Bohr, 1927)\nComplementarity Principle',
                 fontsize=13, fontweight='bold', pad=20)
    ax2.legend(loc='upper right')

    # Right panel: Bloch sphere
    ax3 = fig.add_subplot(133, projection='3d')

    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax3.plot_surface(x, y, z, alpha=0.2, color='gray')

    # Mark special states
    ax3.scatter([0], [0], [1], c='blue', s=200, label='|0⟩')
    ax3.scatter([0], [0], [-1], c='red', s=200, label='|1⟩')
    ax3.scatter([1], [0], [0], c='purple', s=200, label='Superposition')

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('Bloch Sphere: Quantum State Space', fontsize=13, fontweight='bold')
    ax3.legend()

    plt.tight_layout()
    plt.savefig('taiji_complementarity.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[ Mathematical Correspondence: Yin-Yang and Complementarity ]")
    print("="*70)
    print("Yin-Yang       <-> |0> and |1>")
    print("Unity of Opp.  <-> Superposition alpha|0>+beta|1>")
    print("Complementarity<-> Non-commuting observables [x,p]=ihbar")
    print("="*70)

# Run
taiji_and_complementarity()

def wave_function_collapse_zen():
    """Wave function collapse vs. Zen awakening (satori)"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    times = ['Before Measurement', 'During Measurement', 'After Measurement']
    x = np.linspace(-5, 5, 1000)

    # Top row: Quantum mechanics
    for i, (ax, time_label) in enumerate(zip(axes[0], times)):
        if i < 2:
            # Before measurement: wave packet
            psi_real = np.exp(-x**2/2) * np.cos(3*x)
            prob = np.exp(-x**2)

            ax.plot(x, psi_real, 'b-', label='Re(psi)', linewidth=1.5)
            ax.fill_between(x, 0, prob, alpha=0.3, color='purple', label='Probability density')
            ax.set_title(f'{time_label}\nInfinite Possibilities', fontsize=12, fontweight='bold')
            ax.text(0, 1.3, 'Particle is "here AND there"',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
        else:
            # After measurement: collapse
            measured_pos = 1.5
            collapsed = np.zeros_like(x)
            collapsed[np.abs(x - measured_pos) < 0.1] = 10

            ax.bar(x[np.abs(x - measured_pos) < 0.1],
                  collapsed[np.abs(x - measured_pos) < 0.1],
                  width=0.1, color='red', alpha=0.8)
            ax.set_title(f'{time_label}\nDefinite Position', fontsize=12, fontweight='bold', color='red')
            ax.text(0, 11, f'Particle found at x={measured_pos}',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

        ax.set_xlabel('Position x')
        ax.set_ylabel('Wave Function')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-1.5, 12)

    # Bottom row: Zen Buddhism
    zen_states = [
        ('Delusion', 'blue', 'Before awakening'),
        ('Seeking', 'purple', 'Awareness arising'),
        ('Satori', 'red', 'Awakening')
    ]

    for i, (ax, (state, color, desc)) in enumerate(zip(axes[1], zen_states)):
        if i < 2:
            # Before awakening: scattered mind
            np.random.seed(42 + i)
            n_thoughts = 50
            thoughts_x = np.random.randn(n_thoughts) * 2
            thoughts_y = np.random.randn(n_thoughts) * 2

            ax.scatter(thoughts_x, thoughts_y, s=100, alpha=0.6, c=color)
            ax.set_title(f'{state}\n{desc}', fontsize=12, fontweight='bold', color=color)
            ax.text(0, 5, 'Scattered thoughts',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
        else:
            # After awakening: clear mind
            circle = plt.Circle((0, 0), 2, color=color, alpha=0.5)
            ax.add_patch(circle)
            ax.plot(0, 0, 'o', markersize=30, color='gold',
                   markeredgecolor='red', markeredgewidth=3)
            ax.set_title(f'{state}\n{desc}', fontsize=12, fontweight='bold', color=color)
            ax.text(0, 4, 'Satori! "From the beginning,\nnot a thing exists"',
                   ha='center', fontsize=10,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

    fig.text(0.5, 0.98,
            'Wave Function Collapse vs. Zen Awakening: The Moment of Observation',
            ha='center', fontsize=16, fontweight='bold')

    fig.text(0.5, 0.02,
            'Quantum: At the instant of measurement, possibility becomes reality\n'
            'Zen: At the instant of awareness, delusion becomes true nature',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.subplots_adjust(top=0.95, bottom=0.12)
    plt.savefig('collapse_vs_enlightenment.png', dpi=300, bbox_inches='tight')
    plt.show()

# Run
wave_function_collapse_zen()
