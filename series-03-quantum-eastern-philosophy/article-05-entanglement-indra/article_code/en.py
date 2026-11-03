# Code & Cogito: Quantum Entanglement vs. Indra's Net — The Universe as an Indivisible Whole
# Article: https://code-cogito.com/en/quantum-entanglement-vs-indra-s-net-the-universe-as-an-indivisible-whole-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Font configuration
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

class EPRExperiment:
    """
    EPR Experiment Simulation
    Demonstrates: non-local correlations in quantum entanglement
    """

    def __init__(self):
        self.n_trials = 1000

    def create_entangled_pair(self):
        """
        Create entangled state: |psi> = (|up-down> - |down-up>) / sqrt(2)
        Returns: shared phase
        """
        # Random phase (but measurements are always anti-correlated)
        phase = np.random.uniform(0, 2*np.pi)
        return phase

    def measure_spin(self, phase, angle):
        """
        Measure spin along a given axis.
        angle: measurement angle (radians)
        Returns: +1 (up) or -1 (down)
        """
        # Quantum mechanical prediction: probability = cos^2(theta/2)
        prob_up = np.cos((angle - phase) / 2)**2

        if np.random.random() < prob_up:
            return +1  # spin up
        else:
            return -1  # spin down

    def run_epr_experiment(self, angle_A, angle_B):
        """
        Run the EPR experiment.
        angle_A: Alice's measurement angle
        angle_B: Bob's measurement angle
        Returns: (results_A list, results_B list, correlation function)
        """
        results_A = []
        results_B = []

        for _ in range(self.n_trials):
            # Alice's result: the entangled state's marginal probability is always 50/50
            result_A = +1 if np.random.random() < 0.5 else -1

            # Bob's result: correlated with Alice via the singlet joint probability, not an independent measurement
            prob_diff = np.cos((angle_A - angle_B) / 2)**2
            result_B = -result_A if np.random.random() < prob_diff else result_A

            results_A.append(result_A)
            results_B.append(result_B)

        # Compute correlation function E(a,b) = <A * B>
        correlation = np.mean(np.array(results_A) * np.array(results_B))

        return results_A, results_B, correlation

    def visualize_correlations(self):
        """
        Visualize correlation functions at different measurement angles.
        """
        angles = np.linspace(0, np.pi, 50)
        correlations_quantum = []
        correlations_classical = []

        for angle in angles:
            _, _, corr_q = self.run_epr_experiment(0, angle)
            correlations_quantum.append(corr_q)

            # Classical prediction (local hidden variables)
            corr_c = -1 + 2*angle/np.pi
            correlations_classical.append(corr_c)

        # Quantum mechanical theoretical prediction
        correlations_theory = -np.cos(angles)

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(angles * 180/np.pi, correlations_theory, 'b-',
               linewidth=3, label='QM theoretical prediction', alpha=0.7)
        ax.scatter(angles * 180/np.pi, correlations_quantum,
                  c='red', s=50, label=f'Simulated results ({self.n_trials} trials)',
                  alpha=0.6, zorder=5)
        ax.plot(angles * 180/np.pi, correlations_classical, 'g--',
               linewidth=2, label='Classical prediction (local realism)', alpha=0.7)

        ax.set_xlabel("Bob's measurement angle (degrees)", fontsize=13)
        ax.set_ylabel('Correlation function E(0, theta)', fontsize=13)
        ax.set_title('EPR Experiment: Quantum vs. Classical Correlations\nAlice fixed at 0 degrees',
                    fontsize=15, fontweight='bold')
        ax.legend(fontsize=12, loc='upper right')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='black', linewidth=0.5)

        # Annotate key angles
        key_angles = [0, 45, 90, 135, 180]
        for angle in key_angles:
            angle_rad = angle * np.pi / 180
            corr_theory = -np.cos(angle_rad)
            ax.axvline(angle, color='gray', linestyle=':', alpha=0.5)
            ax.text(angle, corr_theory - 0.15, f'{angle}\n{corr_theory:.2f}',
                   ha='center', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

        plt.tight_layout()
        plt.savefig('epr_correlations.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[EPR Experiment Results]")
        print("="*70)
        print(f"\nNumber of trials: {self.n_trials}")
        print("\nKey findings:")
        print("  - Quantum correlation: E(theta) = -cos(theta)")
        print("  - Classical prediction: E(theta) = linear function")
        print("  - Experiment matches quantum prediction, not classical")
        print("\nImplications:")
        print("  - Entanglement is real")
        print("  - There are no hidden variables")
        print("  - Einstein was wrong")
        print("="*70)

    def demonstrate_nonlocality(self):
        """
        Demonstrate non-locality through three measurement scenarios.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Three scenarios
        scenarios = [
            (0, 0, 'Alice & Bob\nsame direction'),
            (0, np.pi/4, 'Alice at 0\nBob at 45'),
            (0, np.pi/2, 'Alice at 0\nBob at 90'),
        ]

        for idx, (angle_A, angle_B, title) in enumerate(scenarios):
            ax = axes[idx]

            results_A, results_B, correlation = self.run_epr_experiment(angle_A, angle_B)

            # Plot outcome distribution
            n_up_up = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == 1)
            n_up_down = sum(1 for a, b in zip(results_A, results_B) if a == 1 and b == -1)
            n_down_up = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == 1)
            n_down_down = sum(1 for a, b in zip(results_A, results_B) if a == -1 and b == -1)

            categories = ['Up-Up', 'Up-Down', 'Down-Up', 'Down-Down']
            counts = [n_up_up, n_up_down, n_down_up, n_down_down]
            colors = ['green', 'blue', 'orange', 'red']

            bars = ax.bar(categories, counts, color=colors, alpha=0.7, edgecolor='black', linewidth=2)

            ax.set_ylabel('Observation count', fontsize=12)
            ax.set_title(f'{title}\nCorrelation E = {correlation:.3f}',
                        fontsize=13, fontweight='bold')
            ax.set_ylim(0, self.n_trials * 0.8)
            ax.grid(True, alpha=0.3, axis='y')

            # Label counts
            for bar, count in zip(bars, counts):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                       f'{count}\n({count/self.n_trials*100:.1f}%)',
                       ha='center', va='bottom', fontsize=10)

        fig.text(0.5, 0.02,
                'Key insight: no matter the distance, measurement outcomes are always correlated!\n'
                'This is not pre-arrangement — it is genuine "action at a distance."',
                ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig('epr_nonlocality.png', dpi=300, bbox_inches='tight')
        plt.show()

# Run
experiment = EPRExperiment()
experiment.visualize_correlations()
experiment.demonstrate_nonlocality()

class BellInequality:
    """
    Bell inequality (CHSH form) verification.
    """

    def __init__(self):
        self.n_trials = 10000

    def quantum_correlation(self, angle_A, angle_B):
        """
        Quantum mechanical prediction for the correlation function.
        E(a, b) = -cos(a - b)
        """
        return -np.cos(angle_A - angle_B)

    def local_realism_correlation(self, angle_A, angle_B, hidden_var):
        """
        Local realism (hidden variable) prediction.
        hidden_var: lambda in [0, 2*pi]
        """
        result_A = +1 if np.cos(angle_A - hidden_var) > 0 else -1
        result_B = +1 if np.cos(angle_B - hidden_var + np.pi) > 0 else -1
        return result_A * result_B

    def compute_chsh_quantum(self):
        """
        Compute the CHSH value for quantum mechanics.
        S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
        """
        # Optimal angle choices
        a = 0
        a_prime = np.pi / 2
        b = np.pi / 4
        b_prime = 3 * np.pi / 4

        E_ab = self.quantum_correlation(a, b)
        E_ab_prime = self.quantum_correlation(a, b_prime)
        E_a_prime_b = self.quantum_correlation(a_prime, b)
        E_a_prime_b_prime = self.quantum_correlation(a_prime, b_prime)

        S_quantum = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime

        return S_quantum, (E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime)

    def compute_chsh_local(self):
        """
        Compute the CHSH value for local realism.
        Average over all possible values of lambda.
        """
        a = 0
        a_prime = np.pi / 2
        b = np.pi / 4
        b_prime = 3 * np.pi / 4

        lambdas = np.linspace(0, 2*np.pi, self.n_trials)

        E_ab_list = []
        E_ab_prime_list = []
        E_a_prime_b_list = []
        E_a_prime_b_prime_list = []

        for lam in lambdas:
            E_ab_list.append(self.local_realism_correlation(a, b, lam))
            E_ab_prime_list.append(self.local_realism_correlation(a, b_prime, lam))
            E_a_prime_b_list.append(self.local_realism_correlation(a_prime, b, lam))
            E_a_prime_b_prime_list.append(self.local_realism_correlation(a_prime, b_prime, lam))

        E_ab = np.mean(E_ab_list)
        E_ab_prime = np.mean(E_ab_prime_list)
        E_a_prime_b = np.mean(E_a_prime_b_list)
        E_a_prime_b_prime = np.mean(E_a_prime_b_prime_list)

        S_local = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime

        return S_local, (E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime)

    def visualize_bell_test(self):
        """
        Visualize the Bell inequality test.
        """
        S_quantum, E_quantum = self.compute_chsh_quantum()
        S_local, E_local = self.compute_chsh_local()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # === Left panel: CHSH value comparison ===
        categories = ['Quantum\nMechanics', 'Local\nRealism', "Bell's\nLimit"]
        values = [S_quantum, S_local, 2.0]
        colors = ['red', 'blue', 'green']

        bars = ax1.bar(categories, np.abs(values), color=colors, alpha=0.7,
                      edgecolor='black', linewidth=2)

        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{val:.3f}',
                    ha='center', va='bottom', fontsize=14, fontweight='bold')

        ax1.axhline(2.0, color='green', linestyle='--', linewidth=3,
                   label="Bell's limit |S| <= 2")
        ax1.axhline(2*np.sqrt(2), color='red', linestyle=':', linewidth=2,
                   label=f'Quantum limit |S| = 2*sqrt(2) ~ {2*np.sqrt(2):.3f}')

        ax1.set_ylabel('|S| value', fontsize=13)
        ax1.set_title('CHSH Inequality Test\nQuantum Mechanics vs. Local Realism',
                     fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.set_ylim(0, 3)

        if abs(S_quantum) > 2:
            verdict = 'Violated! Quantum mechanics wins'
            verdict_color = 'red'
        else:
            verdict = 'Not violated'
            verdict_color = 'green'

        ax1.text(0.5, 2.5, f'Verdict: {verdict}',
                ha='center', fontsize=13, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=verdict_color, alpha=0.5))

        # === Right panel: Four correlation functions ===
        labels = ['E(a,b)', 'E(a,b\')', 'E(a\',b)', 'E(a\',b\')']
        x_pos = np.arange(len(labels))

        quantum_vals = E_quantum
        local_vals = E_local

        width = 0.35
        bars1 = ax2.bar(x_pos - width/2, quantum_vals, width,
                       label='Quantum Mechanics', color='red', alpha=0.7,
                       edgecolor='black', linewidth=1.5)
        bars2 = ax2.bar(x_pos + width/2, local_vals, width,
                       label='Local Realism', color='blue', alpha=0.7,
                       edgecolor='black', linewidth=1.5)

        ax2.set_ylabel('Correlation function E', fontsize=13)
        ax2.set_title('Correlation Functions for Four Measurement Settings', fontsize=14, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(labels, fontsize=11)
        ax2.legend(fontsize=11)
        ax2.axhline(0, color='black', linewidth=0.5)
        ax2.grid(True, alpha=0.3, axis='y')

        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + 0.03 if height > 0 else height - 0.08,
                        f'{height:.2f}',
                        ha='center', va='bottom' if height > 0 else 'top', fontsize=9)

        plt.tight_layout()
        plt.savefig('bell_inequality_test.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("[Bell Inequality Test Results]")
        print("="*70)
        print(f"\nCHSH inequality: |S| <= 2 (if local realism holds)")
        print(f"\nQuantum mechanics prediction:")
        print(f"  S = {S_quantum:.4f}")
        print(f"  |S| = {abs(S_quantum):.4f} > 2  -- Inequality violated!")
        print(f"\nLocal realism (hidden variables):")
        print(f"  S = {S_local:.4f}")
        print(f"  |S| = {abs(S_local):.4f} <= 2  -- Inequality satisfied")
        print(f"\nExperimental results (1982-2022):")
        print(f"  - Aspect (1982):    S = 2.697 +/- 0.015 (measured)")
        print(f"  - Zeilinger (1998): S ~ 2.73 +/- 0.02")
        print(f"  - Pan (2017):       S ~ 2.37 +/- 0.09 (1,200 km)")
        print(f"\nConclusion:")
        print(f"  Quantum mechanics is correct")
        print(f"  Local realism (hidden variable theory) is wrong")
        print(f"  Einstein's hope is dashed")
        print("="*70)

# Run
bell_test = BellInequality()
bell_test.visualize_bell_test()

import networkx as nx
from itertools import combinations

def indras_net_3d():
    """
    3D visualization of Indra's Net.
    Demonstrates: infinite mutual reflection.
    """

    fig = plt.figure(figsize=(18, 12))

    # === Top-left: Grid-based Indra's Net ===
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')

    # Create 3D grid
    n = 4
    nodes = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

    # Plot nodes
    xs, ys, zs = zip(*nodes)
    ax1.scatter(xs, ys, zs, c='gold', s=200, edgecolors='black',
               linewidth=2, alpha=0.8)

    # Plot connections (only adjacent nodes)
    for node1, node2 in combinations(nodes, 2):
        distance = sum((a-b)**2 for a, b in zip(node1, node2))
        if distance == 1:  # adjacent only
            ax1.plot([node1[0], node2[0]],
                    [node1[1], node2[1]],
                    [node1[2], node2[2]],
                    'gray', alpha=0.3, linewidth=1)

    # Highlight one node
    highlight = (1, 1, 1)
    ax1.scatter([highlight[0]], [highlight[1]], [highlight[2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    # Highlight its neighbors
    neighbors = [(i, j, k) for i, j, k in nodes
                if sum((a-b)**2 for a, b in zip((i,j,k), highlight)) == 1]
    if neighbors:
        nx_list, ny_list, nz_list = zip(*neighbors)
        ax1.scatter(nx_list, ny_list, nz_list,
                   c='orange', s=300, edgecolors='red', linewidth=2, alpha=0.8)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title("Indra's Net (3D Grid)\nEach jewel linked to neighbors",
                 fontsize=13, fontweight='bold')

    # === Top-right: Fully connected Indra's Net ===
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')

    n_nodes = 8
    np.random.seed(42)
    positions = np.random.randn(n_nodes, 3) * 2

    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            ax2.plot([positions[i, 0], positions[j, 0]],
                    [positions[i, 1], positions[j, 1]],
                    [positions[i, 2], positions[j, 2]],
                    'b-', alpha=0.1, linewidth=0.5)

    ax2.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
               c='cyan', s=300, edgecolors='black', linewidth=2, alpha=0.8)

    highlight_idx = 0
    ax2.scatter([positions[highlight_idx, 0]],
               [positions[highlight_idx, 1]],
               [positions[highlight_idx, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    for j in range(1, n_nodes):
        ax2.plot([positions[highlight_idx, 0], positions[j, 0]],
                [positions[highlight_idx, 1], positions[j, 1]],
                [positions[highlight_idx, 2], positions[j, 2]],
                'r-', alpha=0.5, linewidth=2)

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title("Indra's Net (Fully Connected)\nTouch one jewel, the whole net responds",
                 fontsize=13, fontweight='bold')

    # === Bottom-left: Quantum entanglement network ===
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')

    n_particles = 10
    np.random.seed(43)
    particle_pos = np.random.randn(n_particles, 3) * 2

    for i in range(n_particles):
        for j in range(i+1, n_particles):
            strength = np.random.random()
            ax3.plot([particle_pos[i, 0], particle_pos[j, 0]],
                    [particle_pos[i, 1], particle_pos[j, 1]],
                    [particle_pos[i, 2], particle_pos[j, 2]],
                    'g-', alpha=strength*0.3, linewidth=1)

    ax3.scatter(particle_pos[:, 0], particle_pos[:, 1], particle_pos[:, 2],
               c='lightgreen', s=300, edgecolors='darkgreen',
               linewidth=2, alpha=0.8)

    highlight_idx = 3
    ax3.scatter([particle_pos[highlight_idx, 0]],
               [particle_pos[highlight_idx, 1]],
               [particle_pos[highlight_idx, 2]],
               c='red', s=500, edgecolors='black', linewidth=3, zorder=10)

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('Quantum Entanglement Network\nMeasure one particle, affect them all',
                 fontsize=13, fontweight='bold')

    # === Bottom-right: Summary panel ===
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    text = '''
    [Indra's Net vs. Quantum Entanglement]

    Huayan Buddhism (7th century):

    "In the palace of Indra hangs a net,
     At each node a jewel reflecting all,
     Each reflection holding every jewel,
     Layer upon layer, without end."

    ----------------------------------------

    Quantum Mechanics (20th century):

    Entangled state |psi> is inseparable
    Particles A and B are non-locally correlated
    Measure A --> instantly affects B
    The whole > the sum of its parts

    ----------------------------------------

    Shared insight:

    The universe is an indivisible whole
    Parts cannot exist apart from the whole
    Changing the local = changing the global
    "Separation" is an illusion

    Huayan: One is all, all is one
    QM: Entanglement = wholeness, inseparable
    '''

    ax4.text(0.1, 0.5, text, fontsize=11, va='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('indras_net_3d_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Indra's Net: A Quantum Insight from 1,300 Years Ago]")
    print("="*70)
    print("\nFazang's mirror room demonstration (7th century):")
    print("  - Ten mirrors around a Buddha statue")
    print("  - Lit by a single torch")
    print("  - Infinite reflections, layer upon layer")
    print("  --> A direct demonstration of 'one is all'")
    print("\nHuayan's Ten Mysterious Gates (Gate 4):")
    print("  'The Realm of Indra's Net'")
    print("  --> All phenomena reflect one another, like jewels in a net")
    print("\nModern quantum entanglement:")
    print("  - Bell state: |psi> = (|up-down> - |down-up>)/sqrt(2)")
    print("  - Measure A --> instantly determines B")
    print("  - An inseparable whole")
    print("\n2022 Nobel Prize in Physics:")
    print("  Awarded to Aspect, Clauser, Zeilinger")
    print("  For proving that quantum entanglement is real")
    print("="*70)

# Run
indras_net_3d()

def nonlocal_correlation_demo():
    """
    Non-local correlation demonstration.
    Experience "spooky action at a distance" firsthand.
    """

    fig = plt.figure(figsize=(16, 10))

    # Simulation parameters
    n_measurements = 50
    distance_light_years = [0.001, 0.1, 1, 10, 100, 1000]

    # === Upper panel: Distance does not weaken correlation ===
    ax1 = fig.add_subplot(2, 1, 1)

    correlations = []
    for distance in distance_light_years:
        corr = -np.cos(np.pi/4)  # fixed angle
        noise = np.random.randn() * 0.05  # experimental noise
        correlations.append(corr + noise)

    ax1.plot(distance_light_years, correlations, 'ro-',
            markersize=12, linewidth=3, label='Simulated (fixed value + noise)')
    ax1.axhline(correlations[0], color='blue', linestyle='--',
               linewidth=2, label=f'Theoretical value ~ {correlations[0]:.3f}')

    ax1.set_xscale('log')
    ax1.set_xlabel('Distance between particles (light-years)', fontsize=13)
    ax1.set_ylabel('Correlation strength', fontsize=13)
    ax1.set_title('Quantum Entanglement: Distance Does Not Weaken Correlation\n(Violating the principle of "locality")',
                 fontsize=15, fontweight='bold')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Annotate key distances
    annotations = [
        (0.001, "~63 AU (beyond Pluto's orbit)"),
        (1, '1 light-year'),
        (1000, '1,000 light-years\n(1% of Milky Way diameter)'),
    ]
    for distance, label in annotations:
        idx = distance_light_years.index(distance)
        ax1.annotate(label, xy=(distance, correlations[idx]),
                    xytext=(distance*3, correlations[idx]+0.1),
                    fontsize=10, ha='left',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6),
                    arrowprops=dict(arrowstyle='->', lw=1.5))

    ax1.text(0.5, 0.15,
            'Key: correlation strength remains constant regardless of distance!\n'
            'The influence is "instantaneous" -- no propagation time required.',
            transform=ax1.transAxes, ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # === Lower panel: Timeline simulation ===
    ax2 = fig.add_subplot(2, 1, 2)

    time_events = [
        (0, 'Alice and Bob receive\nentangled particle pair', 'green'),
        (1, 'Alice and Bob separate\nto 1,000 light-years apart', 'blue'),
        (2, 'Alice measures spin\n(t = 2 sec)', 'red'),
        (2.0000001, "Bob's particle\n'instantly' determined\n(no delay!)", 'red'),
        (3, 'At light speed, this\nwould take 1,000 years', 'gray'),
    ]

    for t, label, color in time_events:
        if t < 2.5:
            ax2.scatter([t], [1], s=500, c=color, zorder=5,
                       edgecolors='black', linewidth=2)
            ax2.text(t, 1.3, label, ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.5))

    ax2.plot([0, 3], [1, 1], 'k-', linewidth=3)
    ax2.set_xlim(-0.5, 3.5)
    ax2.set_ylim(0.5, 2)
    ax2.set_xlabel('Time (seconds)', fontsize=13)
    ax2.set_title('Quantum Entanglement Timeline: "Instantaneous" Influence',
                 fontsize=15, fontweight='bold')
    ax2.set_yticks([])
    ax2.grid(True, alpha=0.3, axis='x')

    ax2.annotate('', xy=(2.0000001, 0.9), xytext=(2, 0.9),
                arrowprops=dict(arrowstyle='->', lw=5, color='red'))
    ax2.text(2.00000005, 0.7, 'Instant!', ha='center', fontsize=12,
            fontweight='bold', color='red')

    ax2.plot([2, 3], [0.8, 0.8], 'gray', linestyle=':', linewidth=3)
    ax2.text(2.5, 0.65, 'Light speed: 1,000 years', ha='center',
            fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig('nonlocal_correlation_demo.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("[Non-locality: Beyond Space and Time]")
    print("="*70)
    print("\nExperimental facts:")
    print("  1. Alice and Bob share an entangled particle pair")
    print("  2. They separate to 1,000 light-years apart")
    print("  3. Alice measures --> Bob's particle is instantly determined")
    print("  4. Correlation strength does not diminish with distance")
    print("\nThree possible explanations:")
    print("  X Faster-than-light information transfer?")
    print("     --> Violates relativity")
    print("  X Particles 'pre-agreed' on outcomes?")
    print("     --> Ruled out by Bell's inequality")
    print("  O Entangled particles were always one whole")
    print("     --> No 'transmission' because there was no 'separation'")
    print("\nThe Huayan perspective:")
    print("  'All phenomena mutually condition each other'")
    print("  --> There is no independent 'particle A' and 'particle B'")
    print("  --> There is only the inseparable 'system AB'")
    print("  --> 'Separation' is an illusion")
    print("="*70)

# Run
nonlocal_correlation_demo()
