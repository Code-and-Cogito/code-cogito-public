"""
Quantum Entanglement vs Dependent Origination - Free Version
Series 3 (Quantum Mechanics Meets Eastern Philosophy), Article 08: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic twelve links of dependent origination (circle)
- Simple entanglement state visualization
- Basic Bell inequality demonstration

For complete version with 12 sub-plots, see premium content.

What is computed and what is not:
- The quantum CHSH value S is computed from an idealised, noise-free model
  with the standard textbook analyzer angles (illustrative settings, not the
  settings of any specific experiment).
- The local hidden-variable limit S <= 2 is a mathematical bound.
- The 'experiment' value (S ~ 2.7) is a hard-coded, rounded reference value,
  not the output of any simulation here.
- The Buddhist-physics parallels are conceptual analogies, not physics results.

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
print("Series 3 Article 08")
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
    print("  Traditional teaching: break any link -> the cycle ends -> Nirvana")
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
    print("    - Measurement outcomes on A and B are correlated (no signal can be sent this way)")

# ============================================================================
# Visualization 3: Bell Inequality Violation (Simple)
# ============================================================================

def bell_inequality_basic():
    """
    Simple demonstration of Bell inequality violation
    """
    print("\n[Visualization 3] Bell Inequality Violation")
    print("-" * 70)

    # Analyzer angles (degrees -> radians): the standard textbook CHSH choice.
    # These are illustrative settings for an idealised, noise-free model,
    # not the settings of any specific experiment.
    angles = np.array([0, 22.5, 45, 67.5]) * np.pi / 180

    # CHSH form of Bell's inequality:
    #   S = |E(a,b) - E(a,b')| + |E(a',b) + E(a',b')|
    #   Local hidden-variable models: S <= 2
    #   Quantum mechanics (ideal):    S can reach 2*sqrt(2) ~ 2.828
    # Idealised singlet-type correlation used here: E = -cos(2*(angle_a - angle_b))

    a, b, ap, bp = 0, 1, 2, 3  # angle indices

    E_ab = -np.cos(2*(angles[a] - angles[b]))
    E_abp = -np.cos(2*(angles[a] - angles[bp]))
    E_apb = -np.cos(2*(angles[ap] - angles[b]))
    E_apbp = -np.cos(2*(angles[ap] - angles[bp]))

    S_quantum = abs(E_ab - E_abp) + abs(E_apb + E_apbp)

    # Local hidden-variable limit: a mathematical bound, not a measurement.
    S_LOCAL_BOUND = 2.0

    # Hard-coded, rounded reference value -- NOT computed by this script.
    # It is the approximate S usually quoted for the early (1982) Aspect photon
    # experiments. Real experiments report S with an uncertainty, so see the
    # Aspect et al. (1982) papers listed in the article's references for exact
    # figures.
    S_EXPERIMENT_APPROX = 2.7

    fig, ax = plt.subplots(figsize=(12, 8))

    # Bar chart
    categories = ['Local hidden-variable\nlimit', 'Quantum prediction\n(ideal model)',
                  'Experiment\n(Aspect 1982, approx.,\nhard-coded)']
    values = [S_LOCAL_BOUND, S_quantum, S_EXPERIMENT_APPROX]
    bar_labels = [f'{S_LOCAL_BOUND:.1f} (limit)', f'{S_quantum:.3f}',
                  f'~{S_EXPERIMENT_APPROX:.1f}']
    colors = ['lightblue', 'lightcoral', 'lightgreen']

    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=2)

    # Local hidden-variable limit line
    ax.axhline(y=S_LOCAL_BOUND, color='blue', linestyle='--', linewidth=2,
               label='Local hidden-variable limit (S=2)')

    # Values on bars
    for bar, text in zip(bars, bar_labels):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
               text, ha='center', va='bottom', fontsize=14, fontweight='bold')

    ax.set_ylabel("Bell's S Parameter (CHSH)", fontsize=12)
    ax.set_title("Bell (CHSH) Inequality Violation\n" +
                "Quantum predictions exceed the local hidden-variable limit",
                fontsize=13, fontweight='bold')
    ax.set_ylim(0, 3.7)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(alpha=0.3, axis='y')

    # Explanation
    ax.text(1, 3.6,
           'Local hidden-variable models: S <= 2\n' +
           'Quantum mechanics (ideal): S up to 2*sqrt(2) ~ 2.828\n' +
           'Experiment (Aspect 1982): S ~ 2.7 (approx., hard-coded)\n\n' +
           '-> LOCAL hidden-variable theories are ruled out\n' +
           '-> Non-local theories are not excluded',
           ha='center', va='top', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

    plt.tight_layout()
    plt.savefig('bell_inequality_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Bell's Inequality (CHSH form):")
    print(f"  If a local hidden-variable model holds -> S <= 2")
    print(f"  ")
    print(f"  Results:")
    print(f"  Local hidden-variable limit:       S <= {S_LOCAL_BOUND:.1f}")
    print(f"  Quantum prediction (ideal model):  S = {S_quantum:.3f}")
    print(f"  Experiment (Aspect 1982):          S ~ {S_EXPERIMENT_APPROX:.1f} (approx., hard-coded reference value)")
    print(f"  ")
    print(f"  CONCLUSION:")
    print(f"  Measured S values above 2 rule out LOCAL hidden-variable theories")
    print(f"  -> Particles cannot have purely local, independent properties")
    print(f"  -> Non-local theories (e.g. Bohmian mechanics) are not excluded")

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
print("\n[Reading Notes - conceptual analogies, not physics results]")
print("  - Buddha: 'Because this exists, that exists'")
print("  - Bell: violating the inequality rules out LOCAL hidden-variable theories")
print("  - Dependent origination and quantum entanglement can be read side by side (analogy, not equivalence)")
print("  - No svabhava (self-nature) echoes 'no purely local independent properties' (analogy)")
print("  - Relational ontology: relations before entities (a philosophical reading)")
print("  - Nagarjuna's 'neither existence nor non-existence' echoes superposition (conceptual parallel)")
print("=" * 70)
