"""
Unified Reality - Free Version
Series 3 Article 12 (Finale): Basic Visualizations

Author: Wina Wu
Date: 2026-10

NOTE: Every score in this script (the 11 correspondence scores and the five
theme scores) is hand-set by the author for illustration. They are subjective
ratings, not measurements, and they are not computed from any data set.

Requirements:
pip install numpy matplotlib networkx
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Unified Reality - Free Version (Finale)")
print("Series 3 Article 12")
print("=" * 70)

# Visualization 1: 11 Correspondences Network
def correspondences_network_basic():
    print("\n[Visualization 1] 11 Core Correspondences Network")
    fig, ax = plt.subplots(figsize=(20, 16))

    # 11 correspondences with hand-set illustrative scores (author-assigned,
    # 0-10; not measured or computed). Quantum side first, Eastern side second,
    # so that node colours match the legend.
    correspondences = [
        ('Wave-Particle\nDuality', 'Emptiness\n(Sunyata)', 9),
        ('Copenhagen\nInterpretation', 'Kyoto School\nPhilosophy', 8),
        ('Superposition', 'Dao\n(The Way)', 9),
        ('Uncertainty\nPrinciple', 'Sunyata\n(Emptiness)', 10),
        ('Entanglement', "Indra's Net", 10),
        ('Many-Worlds\nInterpretation', 'Infinite Realms\n(Huayan)', 7),
        ('Quantum Field\nTheory', 'Yogacara\n(Mind-Only)', 8),
        ('EPR State', 'Dependent\nOrigination', 9),
        ('Quantum Mind\nTheory', 'Mind Philosophy\n(Xinxue)', 7),
        ('Quantum\nComputing', 'Non-duality\n(Advaita)', 8),
        ('Quantum State\nCoherence', 'Meditation\nPractice', 8),
    ]

    G = nx.Graph()
    for qm, ep, weight in correspondences:
        G.add_edge(qm, ep, weight=weight/10)

    # Position nodes with more spacing
    pos = nx.spring_layout(G, k=3.5, iterations=100, seed=42)

    # Draw nodes
    qm_nodes = [c[0] for c in correspondences]
    ep_nodes = [c[1] for c in correspondences]

    nx.draw_networkx_nodes(G, pos, nodelist=qm_nodes, node_color='lightblue',
                          node_size=4000, alpha=0.8, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=ep_nodes, node_color='lightgreen',
                          node_size=4000, alpha=0.8, ax=ax)

    # Draw edges with varying width based on similarity
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    nx.draw_networkx_edges(G, pos, width=[w*8 for w in weights],
                          alpha=0.5, edge_color='gray', ax=ax)

    # Draw labels with smaller font to avoid overlap
    nx.draw_networkx_labels(G, pos, font_size=7, font_weight='bold', ax=ax)

    ax.text(0.5, 0.98, '11 Core Correspondences\nQuantum Mechanics <-> Eastern Philosophy',
           ha='center', va='top', transform=ax.transAxes,
           fontsize=16, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    ax.text(0.02, 0.02, 'Blue: Quantum Mechanics\nGreen: Eastern Philosophy\nLine thickness: author-assigned illustrative score',
           transform=ax.transAxes, fontsize=10,
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.axis('off')
    plt.tight_layout()
    plt.savefig('correspondences_network_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > 11 correspondences network visualized")
    return correspondences

# Visualization 2: 5 Common Patterns
def five_patterns_basic():
    print("\n[Visualization 2] Five Recurring Themes (illustrative scores)")
    fig, ax = plt.subplots(figsize=(14, 10))

    patterns = [
        'Relationality',
        'Observer\nParticipation',
        'Transcending\nDuality',
        'Fundamental\nUncertainty',
        'Wholeness'
    ]

    # Hand-set illustrative scores (not computed from data).
    # The article distils three patterns (relationality, the participatory role
    # of the observer, transcending binary opposition); this chart also lists
    # Fundamental Uncertainty and Wholeness. "Observer Participation" follows
    # Wheeler-style readings (speculative), not Bohr's own view.
    scores = [9.2, 8.5, 8.8, 8.7, 8.3]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

    bars = ax.barh(patterns, scores, color=colors, edgecolor='black', linewidth=2)

    # Add value labels
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(score + 0.1, i, f'{score:.1f}/10', va='center', fontsize=11, fontweight='bold')

    ax.set_xlabel('Author-assigned illustrative score (0-10)', fontsize=12)
    ax.set_title('Five Recurring Themes (illustrative scores)',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.grid(alpha=0.3, axis='x')

    # Add explanation
    ax.text(0.5, -0.15,
           'Five themes identified by the author;\nscores are hand-set and illustrative',
           ha='center', transform=ax.transAxes, fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.savefig('five_patterns_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > Five recurring themes visualized")
    return scores

# Visualization 3: Two Paths Converging
def two_paths_basic():
    print("\n[Visualization 3] Two Paths, Compared")
    fig, ax = plt.subplots(figsize=(16, 12))

    # Two paths
    ax.text(0.15, 0.9, 'Western Science', ha='center', fontsize=13,
           fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightblue',
           edgecolor='blue', linewidth=3))

    ax.text(0.85, 0.9, 'Eastern Philosophy', ha='center', fontsize=13,
           fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightgreen',
           edgecolor='green', linewidth=3))

    # Methods
    western_methods = [
        'Experiment',
        'Mathematics',
        'Theory',
        'Technology'
    ]

    eastern_methods = [
        'Meditation',
        'Direct Experience',
        'Contemplation',
        'Enlightenment (Satori)'
    ]

    # Western path
    for i, method in enumerate(western_methods):
        y = 0.75 - i*0.12
        ax.text(0.15, y, method, ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))
        if i < len(western_methods) - 1:
            ax.arrow(0.15, y-0.05, 0, -0.04, head_width=0.03, head_length=0.02,
                    fc='blue', ec='blue', linewidth=2)

    # Eastern path
    for i, method in enumerate(eastern_methods):
        y = 0.75 - i*0.12
        ax.text(0.85, y, method, ha='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
        if i < len(eastern_methods) - 1:
            ax.arrow(0.85, y-0.05, 0, -0.04, head_width=0.03, head_length=0.02,
                    fc='green', ec='green', linewidth=2)

    # Arrows from each path to the shared themes (a comparison, not a proof)
    ax.arrow(0.15, 0.27, 0.27, -0.15, head_width=0.04, head_length=0.03,
            fc='purple', ec='purple', linewidth=3, linestyle='--')
    ax.arrow(0.85, 0.27, -0.27, -0.15, head_width=0.04, head_length=0.03,
            fc='purple', ec='purple', linewidth=3, linestyle='--')

    # Shared themes (the author's interpretation)
    ax.text(0.5, 0.05, "SHARED THEMES\n(author's interpretation)\n\n" +
           'Relationality - Participation\n' +
           'Non-duality - Uncertainty - Wholeness',
           ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='gold', edgecolor='red', linewidth=3))

    ax.text(0.5, 0.35, 'COMPARISON', ha='center', fontsize=11,
           fontweight='bold', color='purple')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Two Paths, Compared',
                fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('two_paths_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > Two paths comparison visualized")

# Execute
correspondences = correspondences_network_basic()
theme_scores = five_patterns_basic()
two_paths_basic()

# Means are computed from the hand-set scores above (illustrative, not measured)
mean_corr = float(np.mean([c[2] for c in correspondences]))
mean_themes = float(np.mean(theme_scores))

print("\n" + "=" * 70)
print("Free Version Complete (Finale)!")
print("=" * 70)
print("\nSummary:")
print("  - 11 correspondences between quantum mechanics & Eastern philosophy")
print("  - 5 recurring themes: Relationality, Observer Participation,")
print("    Transcending Duality, Fundamental Uncertainty, Wholeness")
print("  - Two paths (Science & Philosophy) compared side by side")
print(f"  - Mean of the 11 hand-set correspondence scores: {mean_corr:.2f}/10")
print(f"  - Mean of the 5 hand-set theme scores: {mean_themes:.2f}/10")
print("  - All scores are the author's illustrative ratings, not measurements")
print("\nSeries 3 Complete! Thank you for the journey!")
print("=" * 70)
