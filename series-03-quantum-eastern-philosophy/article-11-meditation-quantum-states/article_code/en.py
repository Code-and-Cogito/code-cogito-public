# Code & Cogito: Practice — Meditation and Quantum States
# Article: https://code-cogito.com/en/meditation-quantum-states-practice-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class BrainwaveSimulator:
    """
    Brainwave Simulator
    Demonstrates: brainwave signatures of different meditation states
    """

    def __init__(self):
        self.sampling_rate = 256  # Hz
        self.duration = 10  # seconds
        self.t = np.linspace(0, self.duration, self.duration * self.sampling_rate)

    def generate_brainwave(self, wave_type, amplitude=1.0):
        """
        Generate different types of brainwaves
        """
        if wave_type == 'delta':
            freq = 2  # 0.5-4 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'theta':
            freq = 6  # 4-8 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'alpha':
            freq = 10  # 8-12 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'beta':
            freq = 20  # 13-30 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'gamma':
            freq = 40  # 25-100 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        else:
            wave = np.zeros_like(self.t)

        # Add random noise
        noise = np.random.normal(0, 0.1, len(self.t))
        return wave + noise

    def visualize_meditation_states(self):
        """
        Visualize brainwave patterns across different meditation states
        """
        fig, axes = plt.subplots(3, 2, figsize=(18, 14))

        # === Normal Waking State ===
        ax = axes[0, 0]
        beta = self.generate_brainwave('beta', 1.0)
        alpha = self.generate_brainwave('alpha', 0.3)
        signal_normal = beta + alpha

        ax.plot(self.t[:512], signal_normal[:512], 'b-', linewidth=1)
        ax.set_xlabel('Time (s)', fontsize=11)
        ax.set_ylabel('Amplitude', fontsize=11)
        ax.set_title('Normal Waking State\nBeta-dominant (active thinking)',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Beginner Meditation ===
        ax = axes[0, 1]
        alpha_med = self.generate_brainwave('alpha', 1.5)
        beta_low = self.generate_brainwave('beta', 0.5)
        signal_beginner = alpha_med + beta_low

        ax.plot(self.t[:512], signal_beginner[:512], 'g-', linewidth=1)
        ax.set_xlabel('Time (s)', fontsize=11)
        ax.set_ylabel('Amplitude', fontsize=11)
        ax.set_title('Beginner Meditation\nAlpha-enhanced (relaxation)',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Deep Meditation (Theta) ===
        ax = axes[1, 0]
        theta = self.generate_brainwave('theta', 2.0)
        alpha_deep = self.generate_brainwave('alpha', 0.5)
        signal_deep = theta + alpha_deep

        ax.plot(self.t[:512], signal_deep[:512], 'purple', linewidth=1)
        ax.set_xlabel('Time (s)', fontsize=11)
        ax.set_ylabel('Amplitude', fontsize=11)
        ax.set_title('Deep Meditation\nTheta waves (deep relaxation)',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Advanced Meditator (Gamma) ===
        ax = axes[1, 1]
        gamma = self.generate_brainwave('gamma', 3.0)
        alpha_adv = self.generate_brainwave('alpha', 1.0)
        signal_advanced = gamma + alpha_adv

        ax.plot(self.t[:512], signal_advanced[:512], 'r-', linewidth=1)
        ax.set_xlabel('Time (s)', fontsize=11)
        ax.set_ylabel('Amplitude', fontsize=11)
        ax.set_title('Advanced Meditator\nGamma waves (intense focus)',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Power Spectral Density Comparison ===
        ax = axes[2, 0]

        # Compute power spectral density
        freqs_normal, psd_normal = signal.welch(signal_normal, self.sampling_rate)
        freqs_beginner, psd_beginner = signal.welch(signal_beginner, self.sampling_rate)
        freqs_advanced, psd_advanced = signal.welch(signal_advanced, self.sampling_rate)

        ax.semilogy(freqs_normal, psd_normal, 'b-', label='Normal', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_beginner, psd_beginner, 'g-', label='Beginner', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_advanced, psd_advanced, 'r-', label='Advanced', alpha=0.7, linewidth=2)

        ax.set_xlabel('Frequency (Hz)', fontsize=11)
        ax.set_ylabel('Power Spectral Density', fontsize=11)
        ax.set_title('Spectral Analysis\nBrainwave frequency distribution by state',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 50)

        # Label frequency bands
        ax.axvspan(0.5, 4, alpha=0.1, color='purple', label='Delta')
        ax.axvspan(4, 8, alpha=0.1, color='blue', label='Theta')
        ax.axvspan(8, 12, alpha=0.1, color='green', label='Alpha')
        ax.axvspan(13, 30, alpha=0.1, color='orange', label='Beta')
        ax.axvspan(30, 50, alpha=0.1, color='red', label='Gamma')

        # === Summary Panel ===
        ax = axes[2, 1]
        ax.axis('off')

        text = '''
        [Brainwaves & Meditation States]

        Brainwave Types (Frequency):
        * Delta (0.5-4 Hz): Deep sleep
        * Theta (4-8 Hz): Light sleep, deep meditation
        * Alpha (8-12 Hz): Relaxed, light meditation
        * Beta (13-30 Hz): Normal waking, thinking
        * Gamma (25-100 Hz): Intense focus, integration

        Meditation Progression:
        1. Beginner:
           -> Beta down (less mental chatter)
           -> Alpha up (more relaxation)

        2. Intermediate:
           -> Theta increases (deep relaxation)
           -> May enter meditative absorption

        3. Advanced (10,000+ hours):
           -> Gamma dramatically enhanced (increase >30x controls!)
           -> High synchrony across brain regions
           -> Extremely high consciousness integration

        Orch OR Theory Prediction:
        * Gamma 40Hz ~ quantum collapse frequency
        * Enhanced Gamma in advanced meditators
          may reflect quantum processes in
          microtubules

        Key Finding (Lutz, Davidson et al., 2004):
        * Large rise in gamma activity during meditation
        * Already higher at rest before meditating
        * Authors suggest possible neural changes
        '''

        ax.text(0.05, 0.5, text, fontsize=10, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='lightyellow',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('brainwave_meditation_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Brainwaves & Meditation: The Neuroscience Evidence]")
        print("="*70)

        print("\nFive types of brainwaves:")
        print("  1. Delta (0.5-4 Hz): Deep sleep")
        print("  2. Theta (4-8 Hz): Light sleep, deep meditation, creativity")
        print("  3. Alpha (8-12 Hz): Relaxed but alert, light meditation")
        print("  4. Beta (13-30 Hz): Normal waking, thinking, focusing")
        print("  5. Gamma (25-100 Hz): Intense focus, consciousness integration")

        print("\nHow brainwaves change with meditation:")
        print("  Beginner (a few weeks):")
        print("    * Beta decreases -> less mental chatter")
        print("    * Alpha increases -> more relaxation")

        print("\n  Intermediate (months to years):")
        print("    * Theta increases -> deep relaxation")
        print("    * May enter meditative absorption states")

        print("\n  Advanced (10,000+ hours):")
        print("    * Gamma dramatically enhanced (increase >30x controls!)")
        print("    * High synchrony across brain regions")
        print("    * Extremely high consciousness integration")

        print("\nDavidson Experiment (2004):")
        print("  * 8 Tibetan Buddhist monks")
        print("  * Accumulated meditation practice: 10,000-50,000 hours")
        print("  * Result: gamma rose over 30x as much as in controls")

        print("\nOrch OR Theory Prediction:")
        print("  * Quantum collapse frequency ~ 40 Hz")
        print("  * Gamma wave frequency ~ 40 Hz")
        print("  * A possible connection?")

        print("\nPossible explanation:")
        print("  * Gamma waves reflect quantum collapse in microtubules")
        print("  * Meditation enhances synchronization between microtubules")
        print("  * Producing stronger, more synchronized Gamma waves")

        print("\nCaveat:")
        print("  * This is speculative!")
        print("  * No direct evidence for quantum processes in microtubules")
        print("    during meditation")
        print("  * But the correlation is striking")
        print("="*70)

# Run
brainwave_sim = BrainwaveSimulator()
brainwave_sim.visualize_meditation_states()

class NeuroplasticitySimulator:
    """
    Neuroplasticity Simulator
    Demonstrates: a hand-set model of brain differences in long-term meditators
    """

    def __init__(self):
        pass

    def visualize_brain_changes(self):
        """
        Visualize meditation-induced brain changes
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        # === Gray Matter Density Changes ===
        ax = axes[0, 0]

        brain_regions = ['Hippocampus\n(Memory)', 'Prefrontal\n(Focus)', 'Insula\n(Empathy)',
                        'Amygdala\n(Fear)']
        control_group = [100, 100, 100, 100]
        meditators = [115, 120, 118, 85]  # Relative values

        x = np.arange(len(brain_regions))
        width = 0.35

        bars1 = ax.bar(x - width/2, control_group, width, label='Control Group',
                      color='lightblue', edgecolor='black', linewidth=1.5)
        bars2 = ax.bar(x + width/2, meditators, width, label='Meditators',
                      color='lightgreen', edgecolor='black', linewidth=1.5)

        ax.set_ylabel('Relative Gray Matter Density (%)', fontsize=11)
        ax.set_title('Gray Matter Density Changes\nLong-term Meditators vs Control',
                    fontsize=13, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(brain_regions, fontsize=10)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # Annotate changes
        for i, (c, m) in enumerate(zip(control_group, meditators)):
            change = m - c
            color = 'green' if change > 0 else 'red'
            ax.text(i, max(c, m) + 3, f'{change:+d}%', ha='center',
                   fontsize=10, fontweight='bold', color=color)

        # === Meditation Hours vs Gray Matter Density ===
        ax = axes[0, 1]

        hours = np.array([0, 1000, 5000, 10000, 20000, 40000])
        hippocampus = 100 + 20 * (1 - np.exp(-hours/15000))
        prefrontal = 100 + 25 * (1 - np.exp(-hours/12000))

        ax.plot(hours/1000, hippocampus, 'o-', linewidth=3, markersize=8,
               label='Hippocampus', color='blue')
        ax.plot(hours/1000, prefrontal, 's-', linewidth=3, markersize=8,
               label='Prefrontal Cortex', color='green')

        ax.set_xlabel('Meditation Hours (thousands)', fontsize=11)
        ax.set_ylabel('Relative Gray Matter Density (%)', fontsize=11)
        ax.set_title('Dose-Response Relationship\nMore practice, greater effect',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # === Default Mode Network (DMN) Activity ===
        ax = axes[0, 2]

        states = ['Rest\n(Normal)', 'Rest\n(Meditator)', 'Task\n(Normal)', 'Task\n(Meditator)']
        dmn_activity = [100, 70, 40, 30]
        colors = ['lightcoral', 'lightgreen', 'lightblue', 'lightgreen']

        bars = ax.bar(states, dmn_activity, color=colors, edgecolor='black',
                     linewidth=1.5)
        ax.set_ylabel('DMN Activity (%)', fontsize=11)
        ax.set_title('Default Mode Network (DMN)\nMeditators show less self-referential thinking',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # Annotate
        for bar, activity in zip(bars, dmn_activity):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 3,
                   f'{activity}%', ha='center', fontsize=10, fontweight='bold')

        # === Brain Structure Change Schematic ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Simplified brain outline
        from matplotlib.patches import Ellipse, FancyBboxPatch

        # Brain outline
        brain = Ellipse((0.5, 0.5), 0.6, 0.7, angle=0,
                       facecolor='lightgray', alpha=0.3,
                       edgecolor='black', linewidth=2)
        ax.add_patch(brain)

        # Regions that increase (green)
        regions_increase = [
            (0.35, 0.7, 'Prefrontal\n+20%', 'lightgreen'),
            (0.5, 0.3, 'Hippocampus\n+15%', 'lightgreen'),
            (0.65, 0.5, 'Insula\n+18%', 'lightgreen'),
        ]

        for x, y, label, color in regions_increase:
            circle = plt.Circle((x, y), 0.08, color=color, alpha=0.7,
                               edgecolor='darkgreen', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y-0.12, label, ha='center', fontsize=9,
                   fontweight='bold')

        # Region that decreases (red)
        circle_amygdala = plt.Circle((0.5, 0.6), 0.06, color='lightcoral',
                                    alpha=0.7, edgecolor='darkred', linewidth=2)
        ax.add_patch(circle_amygdala)
        ax.text(0.5, 0.52, 'Amygdala\n-15%', ha='center', fontsize=9,
               fontweight='bold')

        ax.set_title('Brain Structure Changes\nNeuroplasticity from long-term meditation',
                    fontsize=13, fontweight='bold')

        # === White Matter Connectivity Enhancement ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Left: Control group (sparse connections)
        ax.text(0.25, 0.95, 'Control Group', ha='center', fontsize=12,
               fontweight='bold')

        n_nodes = 6
        angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
        nodes_x = 0.25 + 0.15 * np.cos(angles)
        nodes_y = 0.5 + 0.15 * np.sin(angles)

        # Sparse connections
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.3:  # 30% connectivity
                    ax.plot([nodes_x[i], nodes_x[j]], [nodes_y[i], nodes_y[j]],
                           'gray', alpha=0.3, linewidth=1)

        # Nodes
        ax.scatter(nodes_x, nodes_y, s=200, c='lightblue',
                  edgecolors='blue', linewidths=2, zorder=5)

        # Right: Meditators (dense connections)
        ax.text(0.75, 0.95, 'Meditators', ha='center', fontsize=12,
               fontweight='bold')

        nodes_x2 = 0.75 + 0.15 * np.cos(angles)
        nodes_y2 = 0.5 + 0.15 * np.sin(angles)

        # Dense connections
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.8:  # 80% connectivity
                    ax.plot([nodes_x2[i], nodes_x2[j]], [nodes_y2[i], nodes_y2[j]],
                           'green', alpha=0.5, linewidth=2)

        # Nodes
        ax.scatter(nodes_x2, nodes_y2, s=200, c='lightgreen',
                  edgecolors='darkgreen', linewidths=2, zorder=5)

        ax.set_title('White Matter Connectivity\nMeditators show tighter inter-regional coupling',
                    fontsize=13, fontweight='bold')

        # === Summary ===
        ax = axes[1, 2]
        ax.axis('off')

        text_summary = '''
        [Neuroplasticity: Meditation Changes the Brain]

        Gray Matter Density Changes:
        + Hippocampus: +15% (memory, learning)
        + Prefrontal: +20% (decision-making, focus)
        + Insula: +18% (empathy)
        - Amygdala: -15% (fear, stress)

        White Matter Connectivity:
        * Stronger inter-regional connections
        * More efficient information transfer
        * More integrated brain network

        Default Mode Network (DMN):
        * Self-referential thinking reduced
        * Mind-wandering reduced
        * Present-moment awareness enhanced

        Time Effect:
        * Effects increase with meditation hours
        * 10,000+ hours: significant changes
        * But beginners (weeks) also benefit

        Key Takeaway:
        Contemplative practice is not just
        a psychological trick --
        the brain may differ structurally too.

        This is measurable
        evidence that may reflect neuroplasticity.
        '''

        ax.text(0.05, 0.5, text_summary, fontsize=9, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('neuroplasticity_meditation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Neuroplasticity: How Meditation Changes the Brain]")
        print("="*70)

        print("\nGray matter density changes (long-term meditators vs control):")
        print("  Regions that increase:")
        print("    * Hippocampus: +15% (memory, learning)")
        print("    * Prefrontal cortex: +20% (decision-making, focus, self-control)")
        print("    * Insula: +18% (interoception, empathy)")
        print("  Regions that decrease:")
        print("    * Amygdala: -15% (fear, stress response)")

        print("\nWhite matter connectivity:")
        print("  * Stronger connections between brain regions")
        print("  * More efficient information transfer")
        print("  * More integrated brain network")

        print("\nDefault Mode Network (DMN):")
        print("  * DMN: the brain's activity when 'doing nothing'")
        print("  * Associated with self-referential thinking, mind-wandering")
        print("  * Meditators show 30% less DMN activity")
        print("  -> Less ego-centric thinking")
        print("  -> More present-moment awareness")

        print("\nTime effect (dose-response):")
        print("  * Effects increase with meditation hours")
        print("  * 10,000 hours: significant changes")
        print("  * But beginners (8 weeks) also show measurable effects")

        print("\nKey studies:")
        print("  * Davidson et al. (2004): Advanced meditators")
        print("  * Lazar et al. (2005): Cortical thickness")
        print("  * Holzel et al. (2011): 8-week mindfulness program")

        print("\nNeuroplasticity:")
        print("  * The brain can change its structure based on experience")
        print("  * Structural differences remain debated; cause is unsettled")
        print("  * Contemplative practice has a biological basis")

        print("\nPhilosophical significance:")
        print("  * Eastern contemplative traditions say: 'Practice transforms the mind'")
        print("  * Modern neuroscience is asking:")
        print("    Does practice change the brain (the physical basis of mind)?")
        print("  * Theory and practice converge")
        print("="*70)

# Run
neuro_sim = NeuroplasticitySimulator()
neuro_sim.visualize_brain_changes()

def visualize_vipassana_measurement():
    """
    Visualize the analogy between Vipassana meditation and quantum measurement
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Quantum: Before Measurement (Superposition) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Multiple possibilities
    possibilities = ['|0>', '|1>', '|2>', '|3>']
    positions = [(0.3, 0.7), (0.7, 0.7), (0.3, 0.3), (0.7, 0.3)]

    for poss, pos in zip(possibilities, positions):
        circle = plt.Circle(pos, 0.08, color='purple', alpha=0.3,
                           edgecolor='purple', linewidth=2)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], poss, ha='center', va='center',
               fontsize=11, fontweight='bold')

    # Connecting lines (entanglement)
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]],
                   'purple', alpha=0.2, linewidth=1.5)

    ax.text(0.5, 0.9, 'Before Measurement: Superposition', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, '|psi> = Sum(alpha_i|i>)\nAll possibilities coexist',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

    # === Quantum: Measurement (Collapse) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Measurement
    ax.text(0.5, 0.80, '[ Measurement ]', ha='center', fontsize=16, fontweight='bold')

    # Arrow
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))

    # Result
    circle = plt.Circle((0.5, 0.3), 0.12, color='green', alpha=0.7,
                       edgecolor='darkgreen', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, '|2>', ha='center', va='center',
           fontsize=14, fontweight='bold', color='white')

    ax.text(0.5, 0.1, 'After Measurement: Definite State\nWave function collapse',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === Vipassana: Before Observation (Chaotic Thoughts) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Chaotic thoughts
    thoughts = ['Anger', 'Joy', 'Grief', 'Fear', 'Love', 'Hate', 'Desire', 'Craving']
    np.random.seed(42)
    for thought in thoughts:
        x, y = np.random.random(2) * 0.6 + 0.2
        ax.text(x, y, thought, fontsize=11, alpha=0.4,
               color=np.random.choice(['red', 'blue', 'green', 'purple']))

    # Center: unclear mind
    circle = plt.Circle((0.5, 0.5), 0.12, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'Mind\nChaos', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.9, 'Before Observation: Chaotic Thoughts', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, 'Thoughts swirling\nUnclear, uncertain',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Vipassana: Awareness (Observation) ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Awareness
    ax.text(0.5, 0.80, '[ Awareness ]', ha='center', fontsize=16, fontweight='bold',
           color='goldenrod')

    # Arrow
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='gold'))

    # Illuminated thought
    circle = plt.Circle((0.5, 0.3), 0.12, color='yellow', alpha=0.7,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, 'Anger', ha='center', va='center',
           fontsize=16, fontweight='bold')

    # Dissolving
    ax.text(0.7, 0.3, '-> dissolves', ha='left', fontsize=10,
           color='gray', style='italic')

    ax.text(0.5, 0.1, 'With awareness: thought is illuminated\nLoses its power, dissolves',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Main title
    fig.text(0.5, 0.98, 'Vipassana Meditation vs Quantum Measurement',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('vipassana_measurement_analogy.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Vipassana Meditation and Quantum Measurement: A Deep Analogy]")
    print("="*70)

    print("\nQuantum measurement:")
    print("  Before measurement: system in superposition")
    print("    -> |psi> = Sum(alpha_i|i>)")
    print("    -> All possibilities coexist")

    print("\n  During measurement: observer intervenes")
    print("    -> Wave function collapses")

    print("\n  After measurement: system in definite state")
    print("    -> |psi> -> |i>")
    print("    -> One definite outcome")

    print("\nVipassana meditation:")
    print("  Before observation: chaotic thoughts")
    print("    -> Anger, joy, grief, fear... swirling")
    print("    -> Unclear, uncertain")

    print("\n  During observation: awareness arises")
    print("    -> 'Watching' the thought")
    print("    -> Neither chasing nor suppressing")

    print("\n  After observation: thought is illuminated")
    print("    -> Thought loses its power")
    print("    -> Naturally dissolves")

    print("\nShared structure:")
    print("  1. 'Observation' is the key action")
    print("  2. Before observation: uncertain, chaotic")
    print("  3. During observation: intervention, illumination")
    print("  4. After observation: definite or dissolved")

    print("\nCorrespondence:")
    print("  Superposition ~ chaotic thoughts")
    print("  Measurement ~ awareness")
    print("  Collapse ~ thought appearing/dissolving")
    print("  Observer ~ awareness itself")

    print("\nKey insight:")
    print("  * 'Observation' changes 'the observed'")
    print("  * In quantum mechanics, this is a physical law")
    print("  * In Vipassana, this is a psychological experience")
    print("  * The structural parallel is remarkable")

    print("\nImportant caveat:")
    print("  * This is an analogy, not an equivalence")
    print("  * Psychological processes != quantum processes")
    print("  * But the structural correspondence merits reflection")
    print("="*70)

# Run
visualize_vipassana_measurement()

def visualize_no_mind_superposition():
    """
    Visualize the correspondence between no-mind and superposition states
    """

    fig = plt.figure(figsize=(18, 10))

    # === Top Left: Attached Mind (Definite State) ===
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # A single thought (attachment)
    circle = plt.Circle((0.5, 0.5), 0.2, color='red', alpha=0.7,
                       edgecolor='darkred', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.5, 'Love', ha='center', va='center',
            fontsize=24, fontweight='bold', color='white')

    # Arrows pointing inward (attachment)
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax1.annotate('', xy=(0.5, 0.5), xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red'))

    ax1.set_title('Attached Mind: Fixated on one thought\n"Love" -> generates its opposite "Hate"',
                 fontsize=13, fontweight='bold')

    # === Top Right: No-Mind (Superposition) ===
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # Multiple thoughts present (but no attachment)
    emotions = ['Joy', 'Anger', 'Sorrow', 'Delight', 'Love', 'Hate']
    angles = np.linspace(0, 2*np.pi, len(emotions), endpoint=False)

    for emotion, angle in zip(emotions, angles):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        circle = plt.Circle((x, y), 0.08, color='lightblue', alpha=0.5,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, emotion, ha='center', va='center',
                fontsize=11)

    # Center: emptiness / openness
    circle_center = plt.Circle((0.5, 0.5), 0.12, color='gold', alpha=0.7,
                              edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.5, 'No-Mind', ha='center', va='center',
            fontsize=12, fontweight='bold')

    ax2.set_title('No-Mind: Thoughts arise but do not stick\nBeyond opposites, remaining open',
                 fontsize=13, fontweight='bold')

    # === Bottom Left: Quantum Definite State (|0>) ===
    ax3 = fig.add_subplot(2, 2, 3)

    states = ['|0>', '|1>']
    probs = [1.0, 0.0]

    bars = ax3.bar(states, probs, color=['blue', 'lightgray'],
                  edgecolor='black', linewidth=2, alpha=0.7)
    ax3.set_ylabel('Probability', fontsize=11)
    ax3.set_title('Quantum Definite State\n|0>: Completely determined',
                 fontsize=13, fontweight='bold')
    ax3.set_ylim(0, 1.2)
    ax3.grid(True, alpha=0.3, axis='y')

    # === Bottom Right: Quantum Superposition ===
    ax4 = fig.add_subplot(2, 2, 4)

    n_states = 4
    states2 = [f'|{i}>' for i in range(n_states)]
    probs2 = [0.5, 0.3, 0.15, 0.05]

    bars2 = ax4.bar(states2, probs2, color='purple',
                   edgecolor='black', linewidth=2, alpha=0.6)
    ax4.set_ylabel('Amplitude Squared (Probability)', fontsize=11)
    ax4.set_title('Quantum Superposition\n|psi> = Sum(alpha_i|i>): Multiple possibilities',
                 fontsize=13, fontweight='bold')
    ax4.set_ylim(0, 0.6)
    ax4.grid(True, alpha=0.3, axis='y')

    # Main title
    fig.text(0.5, 0.98, 'No-Mind vs Superposition: Openness and Potentiality',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('no_mind_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[No-Mind and Superposition: Openness and Potentiality]")
    print("="*70)

    print("\nAttached mind (definite state):")
    print("  * Fixated on a single thought")
    print("  * Example: fixated on 'Love'")
    print("  * This generates the opposition of 'Love/Hate'")
    print("  * Openness is lost")
    print("  * Like quantum definite state |0>")

    print("\nNo-mind (superposition):")
    print("  * Thoughts come and go without sticking")
    print("  * No attachment to any thought")
    print("  * Beyond binary oppositions")
    print("  * Maintaining openness")
    print("  * Like quantum superposition Sum(alpha_i|i>)")

    print("\nHuineng, the Sixth Patriarch of Zen:")
    print("  'How unexpected -- the original nature is inherently pure.'")
    print("  -> Our true nature is no-mind (clarity)")

    print("\n  'Thought after thought, not dwelling'")
    print("  -> Not clinging to any thought")
    print("  -> Maintaining the state of no-mind")

    print("\nThe challenge of quantum computing:")
    print("  * Maintain superposition without collapse")
    print("  * Prevent decoherence")
    print("  * Extend coherence time")

    print("\nThe challenge of meditation:")
    print("  * Maintain no-mind without attachment")
    print("  * Prevent fixation")
    print("  * Extend periods of clarity")

    print("\nCorrespondence:")
    print("  Superposition ~ no-mind")
    print("  Definite state ~ attached mind")
    print("  Measurement/environment ~ arising thought/stimulus")
    print("  Decoherence ~ loss of clarity")

    print("\nShared insight:")
    print("  * No-mind/superposition is not 'nothingness'")
    print("  * It is a more fundamental, richer state")
    print("  * Full of infinite potentiality")
    print("  * Transcending fixed binary oppositions")

    print("\nUltimate insight:")
    print("  Both no-mind and superposition point to:")
    print("  a state beyond fixation, brimming")
    print("  with potentiality and openness")
    print("="*70)

# Run
visualize_no_mind_superposition()
