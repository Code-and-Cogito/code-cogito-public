"""
Quantum Entanglement vs Indra's Net - Free Version
Season 2 Article 05: Basic Visualizations

Author: Wina @ Code & Cogito
Date: 2026-03 (revised 2026-09 to match the fact-checked article)

This free version includes:
- EPR correlation function (quantum vs classical)
- Bell inequality (CHSH) visualization
- Indra's Net basic network

Data notes (mirrors the "About the data" note in the article):
- The EPR points are a simulation, not experimental data. Alice's result is a
  fair 50/50 coin flip; Bob's result is drawn from the quantum joint
  probability for the angle difference. This is a sampling shortcut that
  reproduces the quantum statistics on a computer; it does not mean a signal
  travels from Alice to Bob.
- The "classical" curve in the EPR chart is an illustrative piecewise-linear
  shape used for teaching. It is not computed from a specific hidden-variable
  model.
- The quantum CHSH value is computed from E(a, b) = -cos(a - b) with the
  angles a = 0, a' = pi/2, b = pi/4, b' = 3*pi/4 (|S| = 2*sqrt(2) = 2.828).
- The three experimental S values are the ones reported in the papers:
    Aspect, Grangier & Roger (1982), Phys. Rev. Lett. 49, 91:  S = 2.697 +/- 0.015
    Weihs et al. (Zeilinger group, 1998), Phys. Rev. Lett. 81, 5039:  S = 2.73 +/- 0.02
    Yin et al. (Pan group, Micius, 2017), Science 356, 1140:  S = 2.37 +/- 0.09
- The Indra's Net graph (12 jewels) is illustrative; the net in the texts is
  infinite.

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
    EPR experiment correlation: quantum prediction vs a simulation.
    Quantum: E(theta) = -cos(theta)
    Classical curve: illustrative linear shape (not a computed model)
    """
    print("\n[Visualization 1] EPR Correlation: Quantum vs Classical")
    print("-" * 70)

    angles = np.linspace(0, np.pi, 100)

    # Quantum prediction (Bell singlet state)
    quantum_corr = -np.cos(angles)

    # Illustrative classical curve: a hand-set piecewise-linear shape used for
    # teaching (same as in the article). It is NOT computed from a specific
    # local hidden-variable model.
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

    # Simulated points. Alice is fixed at 0 degrees, Bob at `angle`.
    # Alice's outcome: the singlet's marginal probability is always 50/50.
    # Bob's outcome: sampled from the singlet joint probability,
    #   P(opposite results) = cos^2(angle / 2), so that E = -cos(angle).
    # This is a sampling shortcut that reproduces the quantum statistics; it is
    # not a signal sent from Alice to Bob.
    np.random.seed(42)
    n_trials = 1000
    sim_angles = np.linspace(0, np.pi, 50)
    sim_corrs = []
    for angle in sim_angles:
        results_a = []
        results_b = []
        prob_opposite = np.cos(angle / 2) ** 2
        for _ in range(n_trials):
            result_a = +1 if np.random.random() < 0.5 else -1
            result_b = -result_a if np.random.random() < prob_opposite else result_a
            results_a.append(result_a)
            results_b.append(result_b)
        sim_corrs.append(np.mean(np.array(results_a) * np.array(results_b)))

    # How closely the simulated points follow -cos(theta)
    max_dev = np.max(np.abs(np.array(sim_corrs) - (-np.cos(sim_angles))))

    ax.scatter(sim_angles * 180 / np.pi, sim_corrs, c='red', s=50,
               label=f'Simulated ({n_trials} pairs per angle)', alpha=0.6, zorder=5)

    ax.plot(angles * 180 / np.pi, classical_corr, 'g--', linewidth=2,
            label='Classical curve (illustrative, linear)', alpha=0.7)

    ax.fill_between(angles * 180 / np.pi, quantum_corr, classical_corr,
                     alpha=0.15, color='yellow', label='Region where the curves differ')

    ax.set_xlabel("Bob's measurement angle (degrees)", fontsize=13)
    ax.set_ylabel('Correlation function E(0, theta)', fontsize=13)
    ax.set_title('EPR Experiment: Quantum vs. Classical Correlations\n'
                 'Alice fixed at 0 degrees', fontsize=15, fontweight='bold')
    # Legend below the axes so it does not cover the key-angle labels
    ax.legend(fontsize=11, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)

    # Annotate key angles
    for angle_deg in [0, 45, 90, 135, 180]:
        angle_rad = angle_deg * np.pi / 180
        # round + 0.0 avoids the label "-0.00" at 90 degrees
        corr_val = round(float(-np.cos(angle_rad)), 2) + 0.0
        ax.axvline(angle_deg, color='gray', linestyle=':', alpha=0.5)
        # Offset annotations to avoid overlap with data points
        if corr_val < 0:
            y_offset = corr_val - 0.2
        else:
            y_offset = corr_val + 0.1
        ax.annotate(f'{angle_deg}°: {corr_val:.2f}',
                     xy=(angle_deg, corr_val),
                     xytext=(angle_deg, y_offset),
                     ha='center', fontsize=9,
                     arrowprops=dict(arrowstyle='->', color='gray', alpha=0.5),
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax.text(0.5, -0.27,
            "Red points: simulation sampled from the quantum joint probability "
            "(reproduces the statistics, not a signal from Alice to Bob).\n"
            "Green dashed curve: illustrative shape, not a computed hidden-variable model.",
            ha='center', va='top', fontsize=9, style='italic',
            transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('epr_correlations.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Quantum prediction:   E(theta) = -cos(theta)")
    print(f"  Classical curve:      illustrative linear shape (not a computed model)")
    print(f"  Simulation:           {n_trials} pairs per angle, {len(sim_angles)} angles, seed 42")
    print(f"  Simulated points vs -cos(theta): max |deviation| = {max_dev:.3f}")
    print(f"  (Bob's result is sampled from the quantum joint probability, so the")
    print(f"   points follow the quantum curve by construction; no signal is sent.)")
    print(f"\n  Key angles:")
    key_notes = {0: "perfect anti-correlation", 90: "no correlation",
                 180: "perfect correlation"}
    for angle_deg in [0, 45, 90, 135, 180]:
        # round + 0.0 avoids printing "-0.00" at 90 degrees
        e_val = round(float(-np.cos(np.radians(angle_deg))), 2) + 0.0
        note = f" ({key_notes[angle_deg]})" if angle_deg in key_notes else ""
        label = f"theta={angle_deg}:"
        print(f"    {label:<10s} E = {e_val:+.2f}{note}")

# ============================================================================
# Visualization 2: Bell Inequality (CHSH) Test
# ============================================================================

def bell_inequality_test():
    """
    CHSH Bell inequality test.
    Classical limit: |S| <= 2
    Quantum prediction: |S| = 2*sqrt(2) ~ 2.828
    Returns the quantum S value computed below.
    """
    print("\n[Visualization 2] Bell Inequality (CHSH) Test")
    print("-" * 70)

    # Optimal measurement angles for S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
    # with E = -cos. Note b' = 3*pi/4: with b' = -pi/4 the four terms cancel
    # and S = 0 (no violation), so that choice would not show the maximum.
    a, a_prime = 0, np.pi / 2
    b, b_prime = np.pi / 4, 3 * np.pi / 4

    # Quantum prediction: E(a,b) = -cos(a - b)
    E_ab = -np.cos(a - b)
    E_ab_prime = -np.cos(a - b_prime)
    E_a_prime_b = -np.cos(a_prime - b)
    E_a_prime_b_prime = -np.cos(a_prime - b_prime)
    S_quantum = E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime
    # The sign of S depends on the angle convention, so test |S|
    violated = abs(S_quantum) > 2.0

    theories = ['Classical\nLimit', 'Quantum\nPrediction',
                'Aspect\n(1982)', 'Zeilinger\n(1998)',
                'Micius Satellite\n(2017)']
    # Measured values as reported in the papers:
    #   Aspect, Grangier & Roger, PRL 49, 91 (1982):          2.697 +/- 0.015
    #   Weihs et al. (Zeilinger group), PRL 81, 5039 (1998):  2.73 +/- 0.02
    #   Yin et al. (Pan group, Micius), Science 356, 1140 (2017): 2.37 +/- 0.09
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

    verdict = ('Violated! Quantum mechanics wins' if violated
               else 'Not violated')
    ax.text(0.5, 0.95, verdict,
            ha='center', va='top', fontsize=11,
            color='red' if violated else 'green', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
            transform=ax.transAxes)

    ax.text(0.5, -0.12,
            "Quantum bar: computed from E(a,b) = -cos(a - b). "
            "Other bars: values reported in the papers "
            "(Aspect, Grangier & Roger 1982; Weihs et al. 1998; Yin et al. 2017).",
            ha='center', va='top', fontsize=9, style='italic',
            transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('bell_inequality_test.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  CHSH Inequality: |S| <= 2 (if local realism holds)")
    print(f"  Angles: a=0, a'=90, b=45, b'=135 degrees")
    print(f"  Quantum prediction:   S = {S_quantum:.4f}, |S| = {abs(S_quantum):.4f}")
    print(f"  Aspect (1982):        S = 2.697 +/- 0.015 (measured)")
    print(f"  Zeilinger (1998):     S ~ 2.73 +/- 0.02")
    print(f"  Micius 1200km (2017): S ~ 2.37 +/- 0.09")
    if violated:
        print(f"\n  Conclusion: Bell inequality VIOLATED (|S| = {abs(S_quantum):.4f} > 2)")
    else:
        print(f"\n  Conclusion: Bell inequality NOT violated (|S| = {abs(S_quantum):.4f} <= 2)")
    print(f"  No local hidden variables. Einstein was wrong.")
    print(f"  2022 Nobel Prize: Aspect, Clauser, Zeilinger")

    return S_quantum

# ============================================================================
# Visualization 3: Indra's Net Network
# ============================================================================

def indras_net_network():
    """
    Indra's Net visualization using a fully connected graph.
    Every jewel reflects all other jewels.
    Illustrative: 12 jewels keep the picture readable; the net in the texts
    is infinite.
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

    plt.text(0.5, -0.17,
             f"Illustrative graph: {n_jewels} jewels, {G.number_of_edges()} mutual "
             "reflections (the net in the texts is infinite).",
             ha='center', va='top', fontsize=9, style='italic',
             transform=plt.gca().transAxes)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig('indras_net_network.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Illustrative model: complete graph of {n_jewels} jewels, "
          f"{G.number_of_edges()} mutual reflections")
    print(f"\n  Indra's Net (Huayan Buddhism, 7th century):")
    print(f"    - Each jewel reflects ALL other jewels")
    print(f"    - Each reflection contains all reflections")
    print(f"    - Infinite recursion, mutual illumination")
    print(f"\n  Parallel to Quantum Entanglement:")
    print(f"    - Non-separability: entangled state cannot be decomposed")
    print(f"    - Holism: the whole is in every part")
    print(f"    - Non-locality: instant mutual influence regardless of distance")
    print(f"    - Relational ontology: no independent existence")
    # Source: Zanning, Song Gaoseng zhuan, fascicle 5 (biography of Fazang):
    # ten mirrors (eight directions plus above and below) around a Buddha
    # image lit by one torch. The same passage says the mirror room was set up
    # for students; the Empress Wu version is a later, popular retelling.
    print(f"\n  Fazang's mirror room (7th century):")
    print(f"    Ten mirrors around a Buddha statue, lit by a single torch")
    print(f"    Infinite reflections, layer upon layer")
    print(f"    A direct demonstration of 'one is all'")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...\n")

epr_correlation()
S_quantum = bell_inequality_test()
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
print("  - Quantum correlation E(theta) = -cos(theta) is not the linear classical shape")
if abs(S_quantum) > 2.0:
    print(f"  - Bell inequality violated: |S| = {abs(S_quantum):.3f} > 2.0")
else:
    print(f"  - Bell inequality not violated: |S| = {abs(S_quantum):.3f} <= 2.0")
print("  - Experiments confirm (1982-2022): no local hidden variables")
print("  - Einstein's 'spooky actions at a distance' are real")
print("  - Huayan's Indra's Net: ancient insight into non-separability")
print("  - The universe is an indivisible whole")
print("=" * 70)
