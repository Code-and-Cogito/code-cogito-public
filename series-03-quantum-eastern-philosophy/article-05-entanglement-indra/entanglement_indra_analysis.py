"""
Quantum Entanglement vs Indra's Net - Free Version
Season 2 Article 05: Basic Visualizations

Author: Wina @ Code & Cogito
Date: 2026-03

This free version includes:
- EPR correlation function (quantum vs classical)
- Bell inequality (CHSH) visualization
- Indra's Net basic network

Requirements:
pip install numpy matplotlib networkx
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Quantum Entanglement vs Indra's Net")
print("Season 2 Article 05 | Code & Cogito")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: EPR Correlation Function
# ============================================================================

def epr_correlation():
    """
    EPR experiment correlation: quantum vs classical prediction.
    Quantum: E(theta) = -cos(theta)
    Classical (local hidden variables): linear approximation
    """
    print("\n[Visualization 1] EPR Correlation: Quantum vs Classical")
    print("-" * 70)

    angles = np.linspace(0, np.pi, 100)

    # Quantum prediction (Bell singlet state)
    quantum_corr = -np.cos(angles)

    # Classical prediction (local hidden variables, best linear bound)
    classical_corr = np.where(
        angles <= np.pi / 2,
        1 - 2 * angles / np.pi,
        -1.0
    )

    # Quantum mechanical theoretical prediction (smooth)
    theory = -np.cos(angles)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(angles * 180 / np.pi, theory, 'b-', linewidth=3,
            label='QM theoretical prediction', alpha=0.7)

    # Simulated experiment points
    np.random.seed(42)
    n_trials = 1000
    sim_angles = np.linspace(0, np.pi, 50)
    sim_corrs = []
    for angle in sim_angles:
        results_a = []
        results_b = []
        for _ in range(n_trials):
            phase = np.random.uniform(0, 2 * np.pi)
            prob_up_a = np.cos((0 - phase) / 2) ** 2
            result_a = +1 if np.random.random() < prob_up_a else -1
            prob_up_b = np.cos((angle - (phase + np.pi)) / 2) ** 2
            result_b = +1 if np.random.random() < prob_up_b else -1
            results_a.append(result_a)
            results_b.append(result_b)
        sim_corrs.append(np.mean(np.array(results_a) * np.array(results_b)))

    ax.scatter(sim_angles * 180 / np.pi, sim_corrs, c='red', s=50,
               label=f'Simulated results ({n_trials} trials)', alpha=0.6, zorder=5)

    ax.plot(angles * 180 / np.pi, classical_corr, 'g--', linewidth=2,
            label='Classical prediction (local realism)', alpha=0.7)

    ax.fill_between(angles * 180 / np.pi, quantum_corr, classical_corr,
                     alpha=0.15, color='yellow', label='Violation region')

    ax.set_xlabel("Bob's measurement angle (degrees)", fontsize=13)
    ax.set_ylabel('Correlation function E(0, theta)', fontsize=13)
    ax.set_title('EPR Experiment: Quantum vs. Classical Correlations\n'
                 'Alice fixed at 0 degrees', fontsize=15, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)

    # Annotate key angles
    for angle_deg in [0, 45, 90, 135, 180]:
        angle_rad = angle_deg * np.pi / 180
        corr_val = -np.cos(angle_rad)
        ax.axvline(angle_deg, color='gray', linestyle=':', alpha=0.5)
        # Offset annotations to avoid overlap with data points
        if corr_val < 0:
            y_offset = corr_val - 0.2
        else:
            y_offset = corr_val + 0.1
        ax.annotate(f'{angle_deg}\u00b0: {corr_val:.2f}',
                     xy=(angle_deg, corr_val),
                     xytext=(angle_deg, y_offset),
                     ha='center', fontsize=9,
                     arrowprops=dict(arrowstyle='->', color='gray', alpha=0.5),
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.savefig('epr_correlations.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Quantum prediction:  E(theta) = -cos(theta)")
    print(f"  Classical prediction: linear function")
    print(f"  Experiment matches quantum, not classical!")
    print(f"\n  Key angles:")
    print(f"    theta=0:   E = -1.00 (perfect anti-correlation)")
    print(f"    theta=45:  E = -0.71")
    print(f"    theta=90:  E =  0.00 (no correlation)")
    print(f"    theta=180: E = +1.00 (perfect correlation)")

# ============================================================================
# Visualization 2: Bell Inequality (CHSH) Test
# ============================================================================

def bell_inequality_test():
    """
    CHSH Bell inequality test.
    Classical limit: |S| <= 2
    Quantum prediction: |S| = 2*sqrt(2) ~ 2.828
    """
    print("\n[Visualization 2] Bell Inequality (CHSH) Test")
    print("-" * 70)

    # Optimal measurement angles
    a, a_prime = 0, np.pi / 2
    b, b_prime = np.pi / 4, -np.pi / 4

    # Quantum prediction: E(a,b) = -cos(a - b)
    E_ab = -np.cos(a - b)
    E_ab_prime = -np.cos(a - b_prime)
    E_a_prime_b = -np.cos(a_prime - b)
    E_a_prime_b_prime = -np.cos(a_prime - b_prime)
    S_quantum = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime

    theories = ['Classical\nLimit', 'Quantum\nPrediction',
                'Aspect\n(1982)', 'Zeilinger\n(1998)',
                'Micius Satellite\n(2017)']
    s_values = [2.0, abs(S_quantum), 2.697, 2.73, 2.37]
    colors = ['#4ECDC4', '#FF6B6B', '#FFD700', '#9370DB', '#FF8C42']

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.bar(theories, s_values, color=colors, alpha=0.8,
                  edgecolor='black', linewidth=2)

    ax.axhline(y=2.0, color='red', linestyle='--', linewidth=2,
               label='Classical Limit |S| = 2')
    ax.axhline(y=2 * np.sqrt(2), color='green', linestyle=':', linewidth=2,
               label=f'Quantum Maximum |S| = 2*sqrt(2) ~ {2*np.sqrt(2):.3f}')

    for bar, val in zip(bars, s_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.05,
                f'{val:.3f}', ha='center', fontsize=13, fontweight='bold')

    ax.set_ylabel('CHSH Parameter |S|', fontsize=12)
    ax.set_title("Bell's Inequality Test: Classical Limit vs Quantum Prediction\n"
                 "All experiments violate the classical limit",
                 fontsize=14, fontweight='bold')
    ax.set_ylim(0, 3.4)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3)

    ax.text(0.5, 0.95, 'Violated! Quantum mechanics wins',
            ha='center', va='top', fontsize=11, color='red', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
            transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('bell_inequality_test.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  CHSH Inequality: |S| <= 2 (if local realism holds)")
    print(f"  Quantum prediction:   |S| = {abs(S_quantum):.4f}")
    print(f"  Aspect (1982):        S = 2.697 +/- 0.015")
    print(f"  Zeilinger (1998):     S ~ 2.73 +/- 0.02")
    print(f"  Micius 1200km (2017): S ~ 2.37 +/- 0.09")
    print(f"\n  Conclusion: Bell inequality VIOLATED")
    print(f"  No local hidden variables. Einstein was wrong.")
    print(f"  2022 Nobel Prize: Aspect, Clauser, Zeilinger")

# ============================================================================
# Visualization 3: Indra's Net Network
# ============================================================================

def indras_net_network():
    """
    Indra's Net visualization using a fully connected graph.
    Every jewel reflects all other jewels.
    """
    print("\n[Visualization 3] Indra's Net - Basic Network")
    print("-" * 70)

    n_jewels = 12
    G = nx.complete_graph(n_jewels)

    plt.figure(figsize=(12, 12))
    pos = nx.circular_layout(G)

    # Draw all edges (mutual reflections)
    nx.draw_networkx_edges(G, pos, edge_color='#4ECDC4', alpha=0.15, width=1)

    # Draw all nodes (jewels)
    nx.draw_networkx_nodes(G, pos, node_color='#FFD700', node_size=800,
                           edgecolors='black', linewidths=2)

    # Highlight center jewel and its connections
    center_node = 0
    nx.draw_networkx_nodes(G, pos, nodelist=[center_node],
                           node_color='#FF6B6B', node_size=1200,
                           edgecolors='black', linewidths=3)

    center_edges = [(center_node, i) for i in range(1, n_jewels)]
    nx.draw_networkx_edges(G, pos, edgelist=center_edges,
                           edge_color='red', width=2.5, alpha=0.6)

    labels = {i: f'{i+1}' for i in range(n_jewels)}
    labels[center_node] = 'Center'
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_weight='bold')

    plt.title("Indra's Net (Huayan Buddhism)\n"
              "Every jewel reflects all others -- One is all, all is one",
              fontsize=14, fontweight='bold')

    plt.text(0.5, -0.02,
             '"In the palace of Indra hangs an infinite net of jewels.\n'
             'Each jewel reflects every other jewel.\n'
             'Each reflection contains within it every other reflection.\n'
             'Layer upon layer, without end." -- Avatamsaka Sutra',
             ha='center', va='top', fontsize=10, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
             transform=plt.gca().transAxes)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig('indras_net_network.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Indra's Net (Avatamsaka Sutra, 7th century):")
    print(f"    - Each jewel reflects ALL other jewels")
    print(f"    - Each reflection contains all reflections")
    print(f"    - Infinite recursion, mutual illumination")
    print(f"\n  Parallel to Quantum Entanglement:")
    print(f"    - Non-separability: entangled state cannot be decomposed")
    print(f"    - Holism: the whole is in every part")
    print(f"    - Non-locality: instant mutual influence regardless of distance")
    print(f"    - Relational ontology: no independent existence")
    print(f"\n  Fazang's mirror room (7th century):")
    print(f"    Mirrors on eight surfaces + one candle = infinite reflections")
    print(f"    A direct demonstration of 'one is all'")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...\n")

epr_correlation()
bell_inequality_test()
indras_net_network()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Visualizations Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. epr_correlations.png - Quantum vs classical correlation")
print("  2. bell_inequality_test.png - CHSH inequality test")
print("  3. indras_net_network.png - Indra's Net network")
print("\nKey Findings:")
print("  - Quantum correlation E(theta) = -cos(theta) exceeds classical limits")
print("  - Bell inequality violated: |S| = 2.828 > 2.0")
print("  - Experiments confirm (1982-2022): no local hidden variables")
print("  - Einstein's 'spooky action at a distance' is real")
print("  - Huayan's Indra's Net: ancient insight into non-separability")
print("  - The universe is an indivisible whole")
print("=" * 70)
