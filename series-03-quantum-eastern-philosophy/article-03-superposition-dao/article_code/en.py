# Code & Cogito: Quantum Superposition vs the Dao of Laozi and Zhuangzi — Between Being and Not-Being
# Article: https://code-cogito.com/en/quantum-superposition-taoism-dao-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
P(total) = P(possibility 1) + P(possibility 2)

# | P(total) = |α₁ + α₂|²

# | P(total) = |α₁|² + |α₂|² + 2Re(α₁*α₂*)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class SchrodingerCat:
    """
    Complete Schrödinger's Cat simulation.
    Includes: atom state, cat state, time evolution, and measurement.
    """

    def __init__(self, half_life=1.0):
        self.half_life = half_life
        self.lambda_decay = np.log(2) / half_life  # Decay constant

    def atom_state(self, t):
        """Quantum state of the atom at time t: |psi> = alpha|undecayed> + beta|decayed>"""
        alpha = np.sqrt(np.exp(-self.lambda_decay * t))
        beta = np.sqrt(1 - np.exp(-self.lambda_decay * t))
        return alpha, beta

    def cat_state(self, t):
        """Cat state evolving over time: |cat> = alpha|alive> + beta|dead>"""
        alpha, beta = self.atom_state(t)
        prob_alive = np.abs(alpha)**2
        prob_dead = np.abs(beta)**2
        return prob_alive, prob_dead

    def measure(self, t):
        """Open the box and measure the cat's state — wavefunction collapse"""
        prob_alive, prob_dead = self.cat_state(t)
        outcome = np.random.choice(['alive', 'dead'],
                                  p=[prob_alive, prob_dead])
        return outcome

    def visualize_evolution(self, max_time=3.0):
        """Visualize the cat's quantum state evolution over time"""
        times = np.linspace(0, max_time, 100)
        probs_alive = []
        probs_dead = []

        for t in times:
            p_alive, p_dead = self.cat_state(t)
            probs_alive.append(p_alive)
            probs_dead.append(p_dead)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # === Top panel: Probability evolution ===
        ax1.fill_between(times, 0, probs_alive, alpha=0.6, color='green', label='P(cat alive)')
        ax1.fill_between(times, 0, probs_dead, alpha=0.6, color='red', label='P(cat dead)')
        ax1.plot(times, probs_alive, 'g-', linewidth=2)
        ax1.plot(times, probs_dead, 'r-', linewidth=2)

        ax1.set_xlabel('Time (hours)', fontsize=13)
        ax1.set_ylabel('Probability', fontsize=13)
        ax1.set_title("Schrödinger's Cat: Superposition Evolving Over Time\n(Before opening the box)",
                     fontsize=15, fontweight='bold')
        ax1.legend(fontsize=12, loc='center right')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1.1)

        # Mark the half-life
        ax1.axvline(self.half_life, color='black', linestyle='--', linewidth=2,
                   label=f'Half-life = {self.half_life} hr')
        ax1.text(self.half_life + 0.1, 0.9,
                f'Half-life\nP(alive)=P(dead)=50%',
                fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

        ax1.text(max_time * 0.5, 0.3,
                'Key point: this is NOT "either dead or alive"!\n'
                'It is "genuinely both dead AND alive"!\n'
                'Quantum state |cat⟩ = α|alive⟩ + β|dead⟩',
                fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # === Bottom panel: Bloch sphere representation ===
        ax2 = fig.add_subplot(212, projection='3d')

        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='gray')

        for i, t in enumerate(times[::5]):
            alpha, beta = self.atom_state(t)
            theta = 2 * np.arctan2(np.abs(beta), np.abs(alpha))
            phi = 0
            x = np.sin(theta) * np.cos(phi)
            y = np.sin(theta) * np.sin(phi)
            z = np.cos(theta)
            color = plt.cm.RdYlGn(1 - t/max_time)
            ax2.scatter([x], [y], [z], c=[color], s=50, alpha=0.8)

        ax2.scatter([0], [0], [1], c='green', s=300, marker='o',
                   edgecolors='black', linewidth=2, label='t=0: |alive⟩')
        ax2.scatter([0], [0], [-1], c='red', s=300, marker='o',
                   edgecolors='black', linewidth=2, label=f't={max_time}: approaching |dead⟩')

        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title("Bloch Sphere: The Cat's Quantum State Trajectory", fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)

        plt.tight_layout()
        plt.savefig('schrodinger_cat_evolution.png', dpi=300, bbox_inches='tight')
        plt.show()

    def run_experiments(self, t, n_trials=100):
        """Run multiple experiments and collect statistics"""
        print("\n" + "="*70)
        print(f"[Schrödinger's Cat Experiment] Time t = {t} hours")
        print("="*70)

        prob_alive, prob_dead = self.cat_state(t)
        print(f"\nTheoretical prediction:")
        print(f"  P(cat alive) = {prob_alive:.2%}")
        print(f"  P(cat dead)  = {prob_dead:.2%}")

        results = [self.measure(t) for _ in range(n_trials)]
        count_alive = results.count('alive')
        count_dead = results.count('dead')

        print(f"\nExperimental results ({n_trials} measurements):")
        print(f"  Observed alive: {count_alive} times ({count_alive/n_trials:.2%})")
        print(f"  Observed dead:  {count_dead} times ({count_dead/n_trials:.2%})")

        print(f"\nKey insights:")
        print(f"  • Before each box opening, the cat is in superposition")
        print(f"  • Opening the box (measurement) causes wavefunction collapse")
        print(f"  • Different trials yield different results, but statistics match theory")
        print("="*70)

# Create the cat
cat = SchrodingerCat(half_life=1.0)

# Visualize evolution
cat.visualize_evolution(max_time=3.0)

# Run experiments
cat.run_experiments(t=0.5, n_trials=100)
cat.run_experiments(t=1.0, n_trials=100)
cat.run_experiments(t=2.0, n_trials=100)

def dao_you_wu_animation():
    """
    Dynamic visualization of "being and non-being give rise to each other."
    Demonstrates how being and non-being mutually generate and depend on each other.
    """

    fig = plt.figure(figsize=(16, 7)); ax1 = fig.add_subplot(121); ax2 = fig.add_subplot(122, projection='3d')
    theta = np.linspace(0, 2*np.pi, 1000)
    n_frames = 60

    def update(frame):
        ax1.clear()
        ax2.clear()
        rotation = 2 * np.pi * frame / n_frames

        # Taijitu (yin-yang symbol), rotating
        r_yin = 1 + 0.5 * np.sin(theta + rotation)
        r_yang = 1 - 0.5 * np.sin(theta + rotation)

        ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta),
                color='black', alpha=0.8, label='Non-being')
        ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
                color='white', edgecolor='black', linewidth=2, label='Being')

        # Eyes of the fish
        eye_x_yang = 0.5 * np.cos(rotation)
        eye_y_yang = 0.5 * np.sin(rotation)
        eye_x_yin = -0.5 * np.cos(rotation)
        eye_y_yin = -0.5 * np.sin(rotation)

        ax1.add_patch(plt.Circle((eye_x_yang, eye_y_yang), 0.15,
                                color='white', ec='black', linewidth=1.5))
        ax1.add_patch(plt.Circle((eye_x_yin, eye_y_yin), 0.15,
                               color='black', ec='black', linewidth=1.5))
        ax1.add_patch(plt.Circle((0, 0), 1.5, fill=False,
                                 edgecolor='black', linewidth=3))

        ax1.set_xlim(-2, 2)
        ax1.set_ylim(-2, 2)
        ax1.set_aspect('equal')
        ax1.axis('off')
        ax1.set_title('Taijitu: Being and Non-Being Give Rise to Each Other\n'
                      'Within "being" arises "non-being"; within "non-being" arises "being"',
                     fontsize=14, fontweight='bold')

        # === Right panel: Quantum superposition state (synchronized rotation) ===
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 30)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.1, color='gray')

        theta_q = np.pi/3
        phi_q = rotation
        x_state = np.sin(theta_q) * np.cos(phi_q)
        y_state = np.sin(theta_q) * np.sin(phi_q)
        z_state = np.cos(theta_q)

        ax2.quiver(0, 0, 0, x_state, y_state, z_state,
                  arrow_length_ratio=0.3, color='red', linewidth=3)
        ax2.scatter([0], [0], [1], c='blue', s=200, label='|0⟩ (being)')
        ax2.scatter([0], [0], [-1], c='green', s=200, label='|1⟩ (non-being)')
        ax2.plot([0, x_state], [0, y_state], [0, 0], 'r--', alpha=0.5, linewidth=1)

        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('Quantum Superposition: |ψ⟩ = α|being⟩ + β|non-being⟩\nEvolving over time',
                     fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1.5, 1.5])
        ax2.set_zlim([-1.5, 1.5])

    anim = FuncAnimation(fig, update, frames=n_frames,
                        interval=100, repeat=True)
    plt.tight_layout()
    plt.show()

    # Static version (for article illustrations)
    fig_static = plt.figure(figsize=(16, 7)); ax1 = fig_static.add_subplot(121); ax2 = fig_static.add_subplot(122, projection='3d')

    theta = np.linspace(0, 2*np.pi, 1000)
    r_yin = 1 + 0.5 * np.sin(theta)
    r_yang = 1 - 0.5 * np.sin(theta)

    ax1.fill(r_yin * np.cos(theta), r_yin * np.sin(theta), color='black', alpha=0.8)
    ax1.fill(r_yang * np.cos(theta + np.pi), r_yang * np.sin(theta + np.pi),
            color='white', edgecolor='black', linewidth=2)
    ax1.add_patch(plt.Circle((0, 0.5), 0.15, color='white', ec='black', lw=1.5))
    ax1.add_patch(plt.Circle((0, -0.5), 0.15, color='black', ec='black', lw=1.5))
    ax1.add_patch(plt.Circle((0, 0), 1.5, fill=False, ec='black', lw=3))

    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Laozi: Being and Non-Being Give Rise to Each Other\n'
                  'Within "non-being" lies "being"; within "being" lies "non-being"',
                 fontsize=14, fontweight='bold')
    ax1.text(0, -2.5, 'Opposites are not contradictions — they are two faces of the same whole',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax2 = fig_static.add_subplot(122, projection='3d')
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax2.plot_surface(x, y, z, alpha=0.1, color='gray')

    states = [
        (0, 0, 1, 'blue', '|0⟩ (pure being)'),
        (0, 0, -1, 'green', '|1⟩ (pure non-being)'),
        (1, 0, 0, 'red', '(|0⟩+|1⟩)/√2'),
        (0, 1, 0, 'purple', '(|0⟩+i|1⟩)/√2'),
    ]

    for x, y, z, color, label in states:
        ax2.scatter([x], [y], [z], c=color, s=200, label=label)
        if x != 0 or y != 0 or z != 1:
            ax2.quiver(0, 0, 0, x, y, z, arrow_length_ratio=0.2,
                      color=color, alpha=0.5, linewidth=2)

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('Quantum Mechanics: Superposition\n|ψ⟩ = α|being⟩ + β|non-being⟩',
                 fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('dao_you_wu_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Being and Non-Being vs Quantum Superposition]")
    print("="*70)
    print("\nLaozi, Dao De Jing:")
    print('  "Being and non-being give rise to each other;')
    print('   difficult and easy complete each other."')
    print("  -> Being and non-being are mutually dependent, inseparable")
    print("\nQuantum mechanics:")
    print("  |ψ⟩ = α|0⟩ + β|1⟩")
    print("  -> |0⟩ and |1⟩ coexist within the superposition")
    print("\nCommon ground:")
    print("  • Opposites are not either/or — they coexist simultaneously")
    print("  • The whole is greater than the sum of its parts")
    print("  • Distinctions are products of observation/naming, not of essence")
    print("="*70)

# Run
dao_you_wu_animation()

def zhuangzi_butterfly_dream():
    """
    Quantum interpretation of Zhuangzi's Butterfly Dream.
    Demonstrates: the entanglement between observer and observed.
    """

    fig = plt.figure(figsize=(16, 10))

    # === Top left: Superposition probability bar chart ===
    ax1 = fig.add_subplot(221)

    scenarios = {
        'Before dream\n(superposition)': [0.5, 0.5],
        'During dream\n(still superposed)': [0.5, 0.5],
        'After waking,\nmeasurement 1\n(collapse to Zhuangzi)': [1.0, 0.0],
        'After waking,\nmeasurement 2\n(collapse to butterfly)': [0.0, 1.0],
    }

    x = np.arange(len(scenarios))
    width = 0.35
    values_state1 = [v[0] for v in scenarios.values()]
    values_state2 = [v[1] for v in scenarios.values()]

    ax1.bar(x - width/2, values_state1, width, label='|Zhuangzi⟩', color='blue', alpha=0.7)
    ax1.bar(x + width/2, values_state2, width, label='|butterfly⟩', color='orange', alpha=0.7)

    ax1.set_ylabel('Probability', fontsize=13)
    ax1.set_title("Zhuangzi's Butterfly Dream: A Quantum Superposition Reading",
                  fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios.keys(), fontsize=10)
    ax1.legend(fontsize=12)
    ax1.set_ylim(0, 1.2)
    ax1.grid(True, alpha=0.3, axis='y')

    ax1.text(1.5, 0.8, 'Key: before measurement,\nZhuangzi and the butterfly\nare "equally real"!',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # === Bottom left: Zhuangzi's perspective ===
    ax2 = fig.add_subplot(223)
    ax2.text(0.5, 0.7, 'If Zhuangzi measures...', ha='center', fontsize=14,
            fontweight='bold', transform=ax2.transAxes)
    ax2.text(0.5, 0.5,
            'Wavefunction collapse:\n|ψ⟩ → |Zhuangzi⟩\n\n'
            'Conclusion:\n"I am Zhuangzi.\nI was just dreaming\nI was a butterfly."',
            ha='center', va='center', fontsize=12,
            transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.axis('off')

    # === Bottom right: Butterfly's perspective ===
    ax3 = fig.add_subplot(224)
    ax3.text(0.5, 0.7, 'If the butterfly measures...', ha='center', fontsize=14,
            fontweight='bold', transform=ax3.transAxes)
    ax3.text(0.5, 0.5,
            'Wavefunction collapse:\n|ψ⟩ → |butterfly⟩\n\n'
            'Conclusion:\n"I am a butterfly.\nI was just dreaming\nI was Zhuangzi."',
            ha='center', va='center', fontsize=12,
            transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax3.axis('off')

    # === Top right: 3D quantum state space ===
    ax4 = fig.add_subplot(222, projection='3d')

    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax4.plot_surface(x, y, z, alpha=0.1, color='gray')

    ax4.scatter([0], [0], [1], c='blue', s=300, label='|Zhuangzi⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([0], [0], [-1], c='orange', s=300, label='|butterfly⟩',
               edgecolors='black', linewidth=2)
    ax4.scatter([1], [0], [0], c='purple', s=300,
               label='Superposition\n(|Zhuangzi⟩+|butterfly⟩)/√2',
               edgecolors='black', linewidth=2)
    ax4.quiver(0, 0, 0, 1, 0, 0, arrow_length_ratio=0.3,
              color='purple', linewidth=3, alpha=0.7)

    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    ax4.set_title('Quantum State Space\nBefore measurement: superposition', fontsize=13, fontweight='bold')
    ax4.legend(fontsize=9, loc='upper left')

    plt.tight_layout()
    plt.savefig('zhuangzi_butterfly_quantum.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Text summary
    print("\n" + "="*70)
    print("[Quantum Interpretation of Zhuangzi's Butterfly Dream]")
    print("="*70)
    print("\nThe classical question (Zhuangzi):")
    print('  "Was it Zhuang Zhou dreaming he was a butterfly?')
    print('   Or a butterfly dreaming it was Zhuang Zhou?"')
    print("\nThe quantum answer:")
    print("  Before measurement, the system is in superposition:")
    print("    |ψ⟩ = (|Zhuangzi⟩ + |butterfly⟩) / √2")
    print('  There is no "absolutely real" answer!')
    print("\nDeeper significance:")
    print('  • There is no "objective reality" independent of the observer')
    print('  • "Real" and "dream" are relative, not absolute')
    print("  • Observer and observed cannot be separated")
    print("="*70)

# Run
zhuangzi_butterfly_dream()

def decoherence_simulation():
    """
    Decoherence simulation.
    Explains: why macroscopic objects (like cats) don't exhibit quantum superposition.
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    times = np.linspace(0, 10, 1000)

    # === (0,0) Microscopic particle: long coherence time ===
    ax = axes[0, 0]
    tau_coherence_micro = 10.0
    coherence_micro = np.exp(-times / tau_coherence_micro)

    ax.plot(times, coherence_micro, 'b-', linewidth=3, label='Coherence')
    ax.fill_between(times, 0, coherence_micro, alpha=0.3, color='blue')
    ax.axhline(0.5, color='red', linestyle='--', label='50% coherence')
    ax.set_xlabel('Time (arbitrary units)', fontsize=12)
    ax.set_ylabel('Coherence', fontsize=12)
    ax.set_title('Microscopic Particle (e.g., electron)\nLong coherence time → can maintain superposition',
                fontsize=13, fontweight='bold', color='blue')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'Coherence time τ = {tau_coherence_micro}\nQuantum effects observable',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === (0,1) Macroscopic object: extremely short coherence time ===
    ax = axes[0, 1]
    tau_coherence_macro = 0.001
    coherence_macro = np.exp(-times / tau_coherence_macro)

    ax.plot(times, coherence_macro, 'r-', linewidth=3, label='Coherence')
    ax.fill_between(times, 0, coherence_macro, alpha=0.3, color='red')
    ax.set_xlabel('Time (arbitrary units)', fontsize=12)
    ax.set_ylabel('Coherence', fontsize=12)
    ax.set_title('Macroscopic Object (e.g., cat)\nExtremely short coherence time → instant collapse',
                fontsize=13, fontweight='bold', color='red')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.text(5, 0.8, f'Coherence time τ ≈ {tau_coherence_macro}\nDecoheres almost instantly',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === (1,0) Number of environmental particles vs decoherence rate ===
    ax = axes[1, 0]

    n_particles = np.logspace(0, 10, 100)
    decoherence_rate = n_particles / 1e9

    ax.loglog(n_particles, decoherence_rate, 'g-', linewidth=3)
    ax.fill_between(n_particles, 1e-10, decoherence_rate, alpha=0.3, color='green')

    ax.scatter([1], [1e-9], s=200, c='blue', label='Single atom', zorder=5)
    ax.scatter([1e6], [1e-3], s=200, c='purple', label='Virus', zorder=5)
    ax.scatter([1e18], [1e9], s=200, c='red', label='Cat', zorder=5)

    ax.set_xlabel('Number of environmental particles (log scale)', fontsize=12)
    ax.set_ylabel('Decoherence rate (log scale)', fontsize=12)
    ax.set_title('Decoherence rate ∝ number of environmental particles\nLarger objects decohere faster',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, which='both')

    # === (1,1) Superposition survival time ===
    ax = axes[1, 1]

    objects = ['Electron', 'Molecule', 'Virus', 'Dust grain', 'Bacterium', 'Cat']
    coherence_times = [1e10, 1e5, 1e-3, 1e-10, 1e-15, 1e-40]
    colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red']

    y_pos = np.arange(len(objects))
    ax.barh(y_pos, np.log10(coherence_times), color=colors, alpha=0.7)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(objects, fontsize=12)
    ax.set_xlabel('Coherence time (log₁₀ seconds)', fontsize=12)
    ax.set_title('Coherence Time Across Scales\nWhy don\'t we see "both dead and alive" cats?',
                fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')

    ax.text(-20, 5.5,
           f"Cat's coherence time ≈ 10⁻⁴⁰ s\n(10⁵⁷ times shorter than\nthe age of the universe!)\n→ Superposition unobservable",
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.text(8, 0.5,
           f"Electron's coherence time ≈ 10¹⁰ s\n(~300 years)\n→ Quantum effects easily observed",
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('decoherence_explanation.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Decoherence: Why Schrödinger's Cat Doesn't Work in Practice]")
    print("="*70)
    print("\nThe question:")
    print('  If quantum superposition is real, why have we never seen')
    print('  a cat that is "both dead and alive"?')
    print("\nThe answer: Decoherence")
    print("  • Macroscopic objects interact with their environment countless times")
    print('  • Each interaction is effectively a "measurement"')
    print("  • Superposition collapses extremely rapidly")
    print("\nThe math:")
    print("  Coherence time τ ∝ 1 / (number of environmental particles)")
    print("  Electron:   τ ≈ 10¹⁰ seconds (observable)")
    print("  Virus:      τ ≈ 10⁻³ seconds")
    print("  Dust grain: τ ≈ 10⁻¹⁰ seconds")
    print("  Cat:        τ ≈ 10⁻⁴⁰ seconds (completely unobservable)")
    print("\nKey insights:")
    print("  1. Quantum superposition is real")
    print("  2. But macroscopic objects decohere too fast for us to see it")
    print('  3. It is not that "quantum mechanics doesn\'t apply to the macro world"')
    print('     but that "macroscopic objects are too difficult to isolate"')
    print("\nLaozi's perspective:")
    print('  "The Dao that can be spoken is not the eternal Dao."')
    print('  → Once observed/named, the "Dao" becomes "not the eternal Dao"')
    print('  → Decoherence is nature\'s own act of "observation"')
    print("="*70)

# Run
decoherence_simulation()
