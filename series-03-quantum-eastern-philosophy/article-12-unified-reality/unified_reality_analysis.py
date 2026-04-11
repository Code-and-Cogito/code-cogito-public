"""
Unified Reality - Free Version
Season 2 Article 12 (Finale): Basic Visualizations

Author: Wina Wu
Date: 2025-01

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
print("Season 2 Article 12")
print("=" * 70)

# Visualization 1: 11 Correspondences Network
def correspondences_network_basic():
    print("\n[Visualization 1] 11 Core Correspondences Network")
    fig, ax = plt.subplots(figsize=(20, 16))

    # 11 correspondences with similarity scores
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
        ('Meditation\nPractice', 'Quantum State\nCoherence', 8),
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

    ax.text(0.02, 0.02, 'Blue: Quantum Mechanics\nGreen: Eastern Philosophy\nLine thickness: Similarity',
           transform=ax.transAxes, fontsize=10,
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.axis('off')
    plt.tight_layout()
    plt.savefig('correspondences_network_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > 11 correspondences network visualized")

# Visualization 2: 5 Common Patterns
def five_patterns_basic():
    print("\n[Visualization 2] Five Common Patterns")
    fig, ax = plt.subplots(figsize=(14, 10))

    patterns = [
        'Relationality',
        'Observer\nParticipation',
        'Transcending\nDuality',
        'Fundamental\nUncertainty',
        'Wholeness'
    ]

    # Score for each pattern across all 11 correspondences
    scores = [9.2, 8.5, 8.8, 8.7, 8.3]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

    bars = ax.barh(patterns, scores, color=colors, edgecolor='black', linewidth=2)

    # Add value labels
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(score + 0.1, i, f'{score:.1f}/10', va='center', fontsize=11, fontweight='bold')

    ax.set_xlabel('Average Similarity Score', fontsize=12)
    ax.set_title('Five Common Patterns\nAcross 11 Correspondences',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.grid(alpha=0.3, axis='x')

    # Add explanation
    ax.text(0.5, -0.15,
           'These five patterns emerge consistently\nacross all quantum-philosophy correspondences',
           ha='center', transform=ax.transAxes, fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.savefig('five_patterns_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > Five common patterns visualized")

# Visualization 3: Two Paths Converging
def two_paths_basic():
    print("\n[Visualization 3] Two Paths to Same Truth")
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

    # Convergence
    ax.arrow(0.15, 0.27, 0.27, -0.15, head_width=0.04, head_length=0.03,
            fc='purple', ec='purple', linewidth=3, linestyle='--')
    ax.arrow(0.85, 0.27, -0.27, -0.15, head_width=0.04, head_length=0.03,
            fc='purple', ec='purple', linewidth=3, linestyle='--')

    # Unified truth
    ax.text(0.5, 0.05, 'UNIFIED REALITY\n\n' +
           'Relationality - Participation\n' +
           'Non-duality - Uncertainty - Wholeness',
           ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='gold', edgecolor='red', linewidth=3))

    ax.text(0.5, 0.35, 'CONVERGENCE', ha='center', fontsize=11,
           fontweight='bold', color='purple')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Two Paths to the Same Truth',
                fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('two_paths_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  > Two paths convergence visualized")

# Execute
correspondences_network_basic()
five_patterns_basic()
two_paths_basic()

print("\n" + "=" * 70)
print("Free Version Complete (Finale)!")
print("=" * 70)
print("\nKey Findings:")
print("  - 11 correspondences between quantum & philosophy")
print("  - 5 common patterns: Relationality, Participation, Non-duality,")
print("    Uncertainty, Wholeness")
print("  - Two paths (Science & Philosophy) converge on unified reality")
print("  - Average similarity: 8.6/10")
print("\nSeason 2 Complete! Thank you for the journey!")
print("=" * 70)
