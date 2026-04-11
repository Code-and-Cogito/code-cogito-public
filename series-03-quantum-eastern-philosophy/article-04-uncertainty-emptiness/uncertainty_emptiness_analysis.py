"""
Uncertainty Principle vs Buddhist Emptiness - Free Version
Season 2 Article 04: Basic Visualizations

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #04/12

This free version includes:
- Gaussian wave packet uncertainty demonstration (2 sub-plots)
- Position-momentum uncertainty tradeoff curve
- Dependent origination network (emptiness visualization)

Requirements:
pip install numpy matplotlib networkx
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("  UNCERTAINTY PRINCIPLE vs BUDDHIST EMPTINESS - Free Version")
print("  Season 2 Article 04 | Quantum Mechanics Meets Eastern Philosophy")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Gaussian Wave Packets & Uncertainty Trade-off
# ============================================================================

def wave_packet_uncertainty():
    """
    Gaussian wave packet demonstration.
    Shows that narrowing position uncertainty (Delta_x) necessarily
    widens momentum uncertainty (Delta_p), and vice versa.
    This is not measurement error -- it is a mathematical property of waves.
    """
    print("\n[Visualization 1] Gaussian Wave Packets & Uncertainty Principle")
    print("-" * 70)

    x = np.linspace(-10, 10, 1000)

    # Narrow wave packet: position well-defined, momentum uncertain
    sigma_narrow = 0.5
    psi_narrow = np.exp(-x**2 / (4 * sigma_narrow**2))

    # Wide wave packet: position uncertain, momentum well-defined
    sigma_wide = 2.0
    psi_wide = np.exp(-x**2 / (4 * sigma_wide**2))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Narrow packet
    ax1.plot(x, psi_narrow, linewidth=3, color='#FF6B6B')
    ax1.fill_between(x, psi_narrow, alpha=0.3, color='#FF6B6B')
    ax1.axvspan(-sigma_narrow, sigma_narrow, alpha=0.15, color='cyan',
                label=f'Delta_x = {sigma_narrow}')
    ax1.set_xlabel('Position x', fontsize=12)
    ax1.set_ylabel('|psi(x)|^2', fontsize=12)
    ax1.set_title('Narrow Wave Packet\nDelta_x small  -->  Delta_p LARGE',
                  fontsize=13, fontweight='bold')
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=10)
    ax1.text(0, 0.85, 'Position\nWELL-DEFINED', ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # Wide packet
    ax2.plot(x, psi_wide, linewidth=3, color='#4ECDC4')
    ax2.fill_between(x, psi_wide, alpha=0.3, color='#4ECDC4')
    ax2.axvspan(-sigma_wide, sigma_wide, alpha=0.15, color='cyan',
                label=f'Delta_x = {sigma_wide}')
    ax2.set_xlabel('Position x', fontsize=12)
    ax2.set_ylabel('|psi(x)|^2', fontsize=12)
    ax2.set_title('Wide Wave Packet\nDelta_x LARGE  -->  Delta_p small',
                  fontsize=13, fontweight='bold')
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.text(0, 0.45, 'Position\nPOORLY DEFINED', ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    fig.suptitle('Heisenberg Uncertainty Principle:  Delta_x * Delta_p >= hbar/2',
                 fontsize=15, fontweight='bold', y=1.02)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('wave_packet_uncertainty.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Heisenberg Uncertainty Principle:")
    print("  Delta_x * Delta_p >= hbar/2")
    print()
    print("  You CANNOT have BOTH:")
    print("  - Well-defined position (Delta_x small)")
    print("  - Well-defined momentum (Delta_p small)")
    print()
    print("  This is NOT measurement error!")
    print("  It is a FUNDAMENTAL mathematical property of waves.")
    print("  The particle genuinely does not possess both values simultaneously.")

# ============================================================================
# Visualization 2: Uncertainty Trade-off Curve
# ============================================================================

def uncertainty_tradeoff():
    """
    Position-momentum uncertainty trade-off.
    The allowed region lies above the Heisenberg limit curve.
    Below the curve is physically forbidden.
    """
    print("\n[Visualization 2] Position-Momentum Uncertainty Trade-off")
    print("-" * 70)

    delta_x = np.linspace(0.1, 10, 200)
    hbar = 1.0  # normalized units
    delta_p_min = hbar / (2 * delta_x)  # Heisenberg lower bound

    plt.figure(figsize=(13, 8))
    plt.plot(delta_x, delta_p_min, linewidth=3, color='#9370DB',
             label='Heisenberg limit: Delta_x * Delta_p = hbar/2')
    plt.fill_between(delta_x, delta_p_min, 5, alpha=0.2, color='#9370DB',
                     label='Allowed region (above curve)')
    plt.fill_between(delta_x, 0, delta_p_min, alpha=0.15, color='red',
                     label='FORBIDDEN region (violates HUP)')

    plt.xlabel('Position uncertainty  Delta_x', fontsize=12)
    plt.ylabel('Momentum uncertainty  Delta_p', fontsize=12)
    plt.title('Heisenberg Uncertainty Principle:  Delta_x * Delta_p >= hbar/2\n'
              'No state can exist in the forbidden region',
              fontsize=14, fontweight='bold')
    plt.xlim(0, 10)
    plt.ylim(0, 5)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)

    plt.text(1.5, 3.5, 'Precise position\n--> Imprecise momentum',
             fontsize=11, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    plt.text(6.5, 0.8, 'Precise momentum\n--> Imprecise position',
             fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    plt.tight_layout()
    plt.savefig('uncertainty_tradeoff.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Key insight:")
    print("  A particle does NOT have simultaneous definite position and momentum.")
    print("  Not because we cannot measure -- because they genuinely DO NOT EXIST.")
    print("  Heisenberg: ontological, not epistemological.")
    print("  Nagarjuna:  no svabhava (inherent nature) -- same structural insight.")

# ============================================================================
# Visualization 3: Emptiness as Dependent Origination Network
# ============================================================================

def emptiness_network():
    """
    Buddhist concept of emptiness (sunyata) visualized as a
    dependent origination network. A 'table' has no independent
    existence -- it depends on wood, carpenter, tools, concept, observer.
    Parallels: a particle has no independent 'position' or 'momentum' --
    properties depend on the measurement context.
    """
    print("\n[Visualization 3] Emptiness: Dependent Origination Network")
    print("-" * 70)

    G = nx.DiGraph()

    nodes = ['Table', 'Wood', 'Carpenter', 'Tools',
             'Concept\n"table"', 'Observer', 'Culture']
    G.add_nodes_from(nodes)

    edges = [
        ('Wood', 'Table'),
        ('Carpenter', 'Table'),
        ('Tools', 'Table'),
        ('Concept\n"table"', 'Table'),
        ('Observer', 'Concept\n"table"'),
        ('Culture', 'Concept\n"table"'),
        ('Carpenter', 'Tools'),
        ('Culture', 'Carpenter'),
    ]
    G.add_edges_from(edges)

    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    node_colors = ['#FF6B6B' if n == 'Table' else '#FFD700' for n in G.nodes()]
    node_sizes = [4000 if n == 'Table' else 2500 for n in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                           edgecolors='black', linewidths=2)
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='#4ECDC4', arrows=True,
                           arrowsize=20, width=2, arrowstyle='->')

    plt.title('Buddhist Emptiness: Dependent Origination\n'
              '"Table" has no independent existence (no svabhava)',
              fontsize=14, fontweight='bold')
    plt.text(0.5, -0.05,
             'Nagarjuna: "Whatever is dependently co-arisen, '
             'that is explained to be emptiness."\n'
             'Table depends on: wood, carpenter, tools, concept, observer...\n'
             'None exist independently  -->  All are "empty" of inherent nature',
             ha='center', fontsize=10, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
             transform=plt.gca().transAxes)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig('emptiness_network.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Buddhist Emptiness (Sunyata):")
    print("  - NOT 'nothing exists'")
    print("  - BUT 'nothing exists INDEPENDENTLY'")
    print("  - Everything arises from conditions (dependent origination)")
    print()
    print("  Quantum parallel:")
    print("  - Particle properties do not exist independently of measurement")
    print("  - Position depends on measurement basis")
    print("  - Momentum depends on measurement setup")
    print("  - No 'inherent' position or momentum (no svabhava)")
    print()
    print("  Heart Sutra: 'Form is emptiness; emptiness is form'")
    print("  Uncertainty: Properties are not intrinsic -- they emerge from interaction")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...\n")

wave_packet_uncertainty()
uncertainty_tradeoff()
emptiness_network()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("  FREE VERSION COMPLETE")
print("=" * 70)
print("\nGenerated plots:")
print("  1. wave_packet_uncertainty.png  -- Narrow vs wide Gaussian packets")
print("  2. uncertainty_tradeoff.png     -- Delta_x vs Delta_p trade-off curve")
print("  3. emptiness_network.png        -- Dependent origination network")
print()
print("Key parallels explored:")
print("  Heisenberg (1927): Particles have no fixed properties")
print("  Nagarjuna (2nd c.): All phenomena have no fixed essence (svabhava)")
print("  Both say: 'Fixedness is not a fundamental feature of reality'")
print("=" * 70)
