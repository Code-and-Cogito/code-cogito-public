"""
Quantum Entanglement vs Dependent Origination - Free Version
Season 2 Article 08: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic twelve links of dependent origination (circle)
- Simple entanglement state visualization
- Basic Bell inequality demonstration

For complete version with 12 sub-plots, see premium content.

Requirements:
pip install numpy matplotlib networkx
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Quantum Entanglement vs Dependent Origination - Free Version")
print("Season 2 Article 08")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Twelve Links of Dependent Origination
# ============================================================================

def twelve_links_basic():
    """
    Basic circular visualization of twelve links of dependent origination
    """
    print("\n[Visualization 1] Twelve Links of Dependent Origination")
    print("-" * 70)

    # 12 links in English
    twelve_links = [
        '1. Ignorance', '2. Formation', '3. Consciousness',
        '4. Name-Form', '5. Six Senses', '6. Contact',
        '7. Feeling', '8. Craving', '9. Clinging',
        '10. Becoming', '11. Birth', '12. Old age\n    -Death'
    ]

    fig, ax = plt.subplots(figsize=(16, 16))

    # Create circular graph
    G = nx.DiGraph()
    for i in range(12):
        G.add_edge(i, (i+1)%12)

    # Circular layout
    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    pos = {i: (np.cos(angles[i]), np.sin(angles[i])) for i in range(12)}

    # Draw
    nx.draw_networkx_nodes(G, pos, node_color='lightcoral',
                           node_size=5000, alpha=0.8, ax=ax)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=3,
                           arrows=True, arrowsize=30,
                           arrowstyle='->', ax=ax,
                           connectionstyle='arc3,rad=0.1')

    # Labels
    for i, label in enumerate(twelve_links):
        x, y = pos[i]
        ax.text(x, y, label, ha='center', va='center',
               fontsize=9, fontweight='bold')

    # Center text
    ax.text(0, 0, 'Twelve Links\nof\nDependent Origination\n\n'
                   '"Because this exists,\nthat exists.\n'
                   'Because this arises,\nthat arises."',
           ha='center', va='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Twelve Links of Dependent Origination (Pratityasamutpada)\n' +
                'The Cycle of Rebirth and Suffering',
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('twelve_links_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Twelve Links (Pratityasamutpada):")
    print("  Each link depends on the previous one")
    print("  Break any link -> the cycle ends -> Nirvana")
    print("  ")
    print("  Key insight:")
    print("  'Because this exists, that exists'")
    print("  'Because this ceases, that ceases'")
    print("  ")
    print("  NO independent existence")
    print("  EVERYTHING depends on conditions")

# ============================================================================
# Visualization 2: Entangled State (Basic)
# ============================================================================

def entangled_state_basic():
    """
    Basic visualization of quantum entangled state
    """
    print("\n[Visualization 2] Quantum Entangled State")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # Plot 1: Separable state
    ax1.text(0.25, 0.7, 'Particle A', ha='center', fontsize=12, fontweight='bold')
    ax1.text(0.75, 0.7, 'Particle B', ha='center', fontsize=12, fontweight='bold')

    # State A
    circle_a = plt.Circle((0.25, 0.5), 0.15, color='lightblue', alpha=0.7,
                         edgecolor='black', linewidth=2)
    ax1.add_patch(circle_a)
    ax1.text(0.25, 0.5, '|psi_A>', ha='center', va='center', fontsize=14)

    # State B
    circle_b = plt.Circle((0.75, 0.5), 0.15, color='lightgreen', alpha=0.7,
                         edgecolor='black', linewidth=2)
    ax1.add_patch(circle_b)
    ax1.text(0.75, 0.5, '|psi_B>', ha='center', va='center', fontsize=14)

    # Tensor product
    ax1.text(0.5, 0.5, 'x', ha='center', va='center', fontsize=20, fontweight='bold')

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    ax1.set_title('Separable State\n' +
                 '|psi> = |psi_A> x |psi_B>\n' +
                 'A and B are INDEPENDENT',
                 fontsize=12, fontweight='bold')

    ax1.text(0.5, 0.2,
            'Classical view:\n' +
            'Particles have independent properties\n' +
            'Can describe each particle separately',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    # Plot 2: Entangled state
    ax2.text(0.5, 0.9, 'Entangled State', ha='center', fontsize=12, fontweight='bold')

    # Combined system
    ellipse = plt.matplotlib.patches.Ellipse((0.5, 0.5), 0.6, 0.4,
                                            color='lightcoral', alpha=0.5,
                                            edgecolor='black', linewidth=3)
    ax2.add_patch(ellipse)

    # Particles inside (cannot separate)
    ax2.scatter([0.35, 0.65], [0.5, 0.5], c=['blue', 'red'],
               s=300, zorder=5, edgecolors='black', linewidths=2)
    ax2.text(0.35, 0.5, 'A', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    ax2.text(0.65, 0.5, 'B', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')

    # Entanglement symbol
    ax2.plot([0.35, 0.65], [0.5, 0.5], 'k-', linewidth=2)
    ax2.text(0.5, 0.55, 'Entangled', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_title('Entangled State\n' +
                 '|psi> = (|up,down> - |down,up>)/sqrt(2)\n' +
                 'A and B are INSEPARABLE',
                 fontsize=12, fontweight='bold')

    ax2.text(0.5, 0.15,
            'Quantum reality:\n' +
            'Particles do NOT have independent properties\n' +
            'CANNOT describe each particle separately\n' +
            'System exists as a WHOLE',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('entangled_state_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Separable state: |psi> = |psi_A> x |psi_B>")
    print("    - Can describe A and B independently")
    print("    - Classical picture")
    print("  ")
    print("  Entangled state: |psi> = (|up,down> - |down,up>)/sqrt(2)")
    print("    - CANNOT describe A and B independently")
    print("    - Quantum inseparability")
    print("    - Measuring A instantly affects B")

# ============================================================================
# Visualization 3: Bell Inequality Violation (Simple)
# ============================================================================

def bell_inequality_basic():
    """
    Simple demonstration of Bell inequality violation
    """
    print("\n[Visualization 3] Bell Inequality Violation")
    print("-" * 70)

    # Angle combinations
    angles = np.array([0, 22.5, 45, 67.5]) * np.pi / 180

    # Classical prediction (local realism)
    classical_predictions = []
    for i in range(4):
        for j in range(4):
            if i != j:
                correlation = np.cos(2*(angles[i] - angles[j]))
                classical_predictions.append(abs(correlation))

    # Quantum prediction
    quantum_correlations = []
    for i in range(4):
        for j in range(4):
            if i != j:
                correlation = -np.cos(2*(angles[i] - angles[j]))
                quantum_correlations.append(correlation)

    # Bell's S parameter
    # S = |E(a,b) - E(a,b')| + |E(a',b) + E(a',b')|
    # Classical: S <= 2
    # Quantum: S can reach 2*sqrt(2) ~ 2.828

    a, b, ap, bp = 0, 1, 2, 3  # angle indices

    E_ab = -np.cos(2*(angles[a] - angles[b]))
    E_abp = -np.cos(2*(angles[a] - angles[bp]))
    E_apb = -np.cos(2*(angles[ap] - angles[b]))
    E_apbp = -np.cos(2*(angles[ap] - angles[bp]))

    S_quantum = abs(E_ab - E_abp) + abs(E_apb + E_apbp)

    fig, ax = plt.subplots(figsize=(12, 8))

    # Bar chart
    categories = ['Classical\nLimit', 'Quantum\nPrediction', 'Experimental\nResult']
    values = [2.0, S_quantum, 2.7]  # Experimental ~2.7
    colors = ['lightblue', 'lightcoral', 'lightgreen']

    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=2)

    # Classical limit line
    ax.axhline(y=2.0, color='blue', linestyle='--', linewidth=2, label='Classical limit (S=2)')

    # Values on bars
    for i, (bar, val) in enumerate(zip(bars, values)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
               f'{val:.3f}', ha='center', va='bottom', fontsize=14, fontweight='bold')

    ax.set_ylabel("Bell's S Parameter", fontsize=12)
    ax.set_title("Bell Inequality Violation\n" +
                "Quantum mechanics VIOLATES classical predictions!",
                fontsize=13, fontweight='bold')
    ax.set_ylim(0, 3.5)
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3, axis='y')

    # Explanation
    ax.text(1, 3.2,
           'Classical (local realism): S <= 2\n' +
           'Quantum mechanics: S ~ 2.828\n' +
           'Experiment (1982 Aspect): S ~ 2.7\n\n' +
           '-> LOCAL REALISM is FALSE!\n' +
           '-> Particles do NOT have definite properties',
           ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('bell_inequality_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Bell's Inequality:")
    print(f"  If local realism is true -> S <= 2")
    print(f"  ")
    print(f"  Results:")
    print(f"  Classical prediction: S = 2.000")
    print(f"  Quantum prediction:   S = {S_quantum:.3f}")
    print(f"  Experimental (1982):  S ~ 2.700")
    print(f"  ")
    print(f"  CONCLUSION:")
    print(f"  Quantum mechanics VIOLATES Bell inequality")
    print(f"  -> Local realism is FALSE")
    print(f"  -> Particles have NO definite properties before measurement")
    print(f"  -> Properties DEPEND on measurement context")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 12 sub-plots, see premium content)\n")

twelve_links_basic()
entangled_state_basic()
bell_inequality_basic()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. twelve_links_basic.png - Dependent origination cycle")
print("  2. entangled_state_basic.png - Separable vs entangled")
print("  3. bell_inequality_basic.png - Bell inequality violation")
print("\n[Premium Version Includes]")
print("  - Dependent origination network complete (4 sub-plots)")
print("  - Entanglement & relational ontology (3 sub-plots)")
print("  - Bell inequality verification detailed (3 sub-plots)")
print("  - Emptiness & superposition (2 sub-plots)")
print("  - Total: 12 professional sub-plots")
print("\n[Key Findings]")
print("  - Buddha: 'Because this exists, that exists'")
print("  - Bell: Particles have NO independent properties")
print("  - Dependent origination ~ Quantum entanglement")
print("  - No svabhava (self-nature) ~ No definite properties")
print("  - Relational ontology: Relations precede entities")
print("  - Nagarjuna was RIGHT: Neither existence nor non-existence")
print("=" * 70)
