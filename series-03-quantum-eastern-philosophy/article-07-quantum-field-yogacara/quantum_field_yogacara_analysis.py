"""
Quantum Field Theory vs Yogacara Buddhism - Free Version
Season 2 Article 07: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic quantum field excitation demo
- Simple vacuum fluctuation visualization
- Basic eight consciousnesses diagram

For complete version with 12 sub-plots, see premium content.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Quantum Field Theory vs Yogacara - Free Version")
print("Season 2 Article 07")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Quantum Field Excitation (Basic)
# ============================================================================

def quantum_field_basic():
    """
    Basic visualization of quantum field and particle as excitation
    """
    print("\n[Visualization 1] Quantum Field: Particle as Excitation")
    print("-" * 70)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # 1D field
    x = np.linspace(0, 10, 1000)
    
    # Ground state (vacuum)
    vacuum = np.zeros_like(x)
    
    # Excited states (particles)
    particle1 = 0.5 * np.sin(2*np.pi*x) * np.exp(-(x-3)**2/0.5)
    particle2 = 0.8 * np.sin(3*np.pi*x) * np.exp(-(x-7)**2/0.3)
    
    # Plot 1: Vacuum state
    ax1.plot(x, vacuum, 'b-', linewidth=3, label='Vacuum (ground state |0⟩)')
    ax1.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax1.fill_between(x, -0.05, 0.05, alpha=0.2, color='lightblue')
    ax1.set_ylabel('Field Value φ(x)', fontsize=12)
    ax1.set_title('Quantum Field: Ground State (No Particles)',
                 fontsize=13, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(alpha=0.3)
    ax1.set_ylim(-1.5, 1.5)
    
    # Plot 2: Excited states
    total_field = vacuum + particle1 + particle2
    ax2.plot(x, total_field, 'r-', linewidth=3, label='Excited field (particles present)')
    ax2.plot(x, particle1, 'g--', linewidth=2, alpha=0.6, label='Particle 1')
    ax2.plot(x, particle2, 'm--', linewidth=2, alpha=0.6, label='Particle 2')
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax2.set_xlabel('Position x', fontsize=12)
    ax2.set_ylabel('Field Value φ(x)', fontsize=12)
    ax2.set_title('Quantum Field: Excited States (Particles = Field Excitations)',
                 fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(alpha=0.3)
    ax2.set_ylim(-1.5, 1.5)
    
    plt.tight_layout()
    plt.savefig('quantum_field_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n  KEY INSIGHT:")
    print(f"  Particles are NOT 'things'")
    print(f"  Particles are EXCITATIONS of the field")
    print(f"  Like ripples on water surface")
    print(f"  ")
    print(f"  Vacuum = field with no excitations")
    print(f"  Particle = localized excitation of field")

# ============================================================================
# Visualization 2: Vacuum Fluctuations (Virtual Particles)
# ============================================================================

def vacuum_fluctuations_basic():
    """
    Basic visualization of vacuum fluctuations (virtual particles)
    """
    print("\n[Visualization 2] Vacuum Fluctuations - Virtual Particles")
    print("-" * 70)
    
    np.random.seed(42)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Time evolution
    n_events = 50
    time_range = 100
    
    for i in range(n_events):
        # Random creation time and position
        t_create = np.random.uniform(0, time_range)
        x_pos = np.random.uniform(0, 10)
        
        # Lifetime according to ΔE·Δt ≥ ℏ/2
        # Higher energy → shorter lifetime
        energy = np.random.exponential(1) + 0.1
        lifetime = 5 / energy  # Roughly ℏ/(2ΔE)
        
        t_annihilate = t_create + lifetime
        
        if t_annihilate < time_range:
            # Plot particle-antiparticle pair
            # Particle (blue)
            ax.plot([t_create, t_annihilate], [x_pos, x_pos + 0.2],
                   'b-', linewidth=2, alpha=0.5)
            # Antiparticle (red)
            ax.plot([t_create, t_annihilate], [x_pos, x_pos - 0.2],
                   'r-', linewidth=2, alpha=0.5)
            
            # Creation event
            ax.scatter(t_create, x_pos, c='gold', s=100, zorder=5,
                      edgecolors='black', linewidths=1)
            # Annihilation event
            ax.scatter(t_annihilate, x_pos + 0.2, c='blue', s=50, zorder=5)
            ax.scatter(t_annihilate, x_pos - 0.2, c='red', s=50, zorder=5)
    
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Space', fontsize=12)
    ax.set_title('Vacuum Is Not Empty: Virtual Particle-Antiparticle Pairs\n' +
                'Constantly appearing and disappearing (ΔE·Δt ≥ ℏ/2)',
                fontsize=13, fontweight='bold')
    ax.set_xlim(0, time_range)
    ax.set_ylim(0, 10)
    
    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='b', linewidth=2, label='Particle'),
        Line2D([0], [0], color='r', linewidth=2, label='Antiparticle'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='gold',
              markersize=10, label='Creation', markeredgecolor='black'),
    ]
    ax.legend(handles=legend_elements, fontsize=11, loc='upper right')
    
    ax.text(50, 9,
           'Vacuum "borrows" energy ΔE for time Δt\n' +
           'As long as ΔE·Δt ≥ ℏ/2\n' +
           'Virtual particles appear and vanish',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('vacuum_fluctuations_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n  VACUUM is NOT empty!")
    print(f"  ")
    print(f"  Classical physics: Vacuum = nothing")
    print(f"  Quantum field theory: Vacuum = lowest energy state")
    print(f"  BUT: Virtual particles constantly pop in and out")
    print(f"  ")
    print(f"  Casimir effect (1948): Experimental proof")
    print(f"  Two metal plates attract even in vacuum")
    print(f"  Confirmed 1997")

# ============================================================================
# Visualization 3: Eight Consciousnesses (Yogacara)
# ============================================================================

def eight_consciousnesses_basic():
    """
    Basic diagram of eight consciousnesses in Yogacara Buddhism
    """
    print("\n[Visualization 3] Eight Consciousnesses (Yogacara Buddhism)")
    print("-" * 70)
    
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Eight levels
    levels = [
        '1-5. Five Sense\nConsciousnesses\n(Eye, Ear, Nose,\nTongue, Body)',
        '6. Mental\nConsciousness\n(Mano-vijnana)',
        '7. Manas\n(Self-consciousness)\n(Klista-manas)',
        '8. Alaya\n(Storehouse)\n(Alaya-vijnana)'
    ]
    
    y_positions = [0.25, 0.45, 0.65, 0.9]
    sizes = [0.16, 0.15, 0.15, 0.25]
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
    
    # Draw circles for each consciousness
    for i, (level, y, size, color) in enumerate(zip(levels, y_positions, sizes, colors)):
        circle = plt.Circle((0.5, y), size, color=color, alpha=0.7,
                           edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(0.5, y, level, ha='center', va='center', fontsize=9,
               fontweight='bold')
    
    # Arrows showing relationship
    for i in range(len(y_positions)-1):
        ax.annotate('', xy=(0.5, y_positions[i+1] - sizes[i+1]),
                   xytext=(0.5, y_positions[i] + sizes[i]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    
    # Alaya seeds
    n_seeds = 30
    for _ in range(n_seeds):
        angle = np.random.uniform(0, 2*np.pi)
        r = np.random.uniform(0.05, 0.20)
        x = 0.5 + r * np.cos(angle)
        y = 0.9 + r * np.sin(angle)
        ax.scatter(x, y, c='gold', s=20, alpha=0.6, edgecolors='black', linewidths=0.5)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.15, 1.25)
    ax.axis('off')
    ax.set_aspect('equal')
    
    ax.set_title('Eight Consciousnesses in Yogacara Buddhism\n' +
                'All phenomena are manifestations of consciousness',
                fontsize=13, fontweight='bold', pad=20)
    
    # Explanation
    ax.text(0.5, 0.03,
           'Alaya (Alaya-vijnana) = Storehouse consciousness\n' +
           'Contains all "seeds" (bija) of karmic potential\n' +
           'Seeds "manifest" (abhinirvtti) as phenomena\n' +
           'Like quantum field contains virtual particles',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('eight_consciousnesses_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n  Eight Consciousnesses (Asta-vijnana):")
    print(f"  1-5. Five senses (eye, ear, nose, tongue, body)")
    print(f"  6. Mental consciousness (mano-vijnana) - thinking, judging")
    print(f"  7. Manas (klista-manas) - self-consciousness, ego")
    print(f"  8. Alaya (alaya-vijnana) - storehouse consciousness")
    print(f"  ")
    print(f"  Alaya = fundamental consciousness")
    print(f"  Contains all karmic seeds (bija)")
    print(f"  Seeds manifest as phenomena (abhinirvtti)")
    print(f"  ")
    print(f"  PARALLEL to quantum field:")
    print(f"  Alaya ≈ Quantum vacuum (both contain potential)")
    print(f"  Seeds ≈ Virtual particles (both can manifest)")
    print(f"  Manifestation ≈ Field excitation (both create reality)")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 12 sub-plots, see premium content)\n")

quantum_field_basic()
vacuum_fluctuations_basic()
eight_consciousnesses_basic()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. quantum_field_basic.png - Field excitation demo")
print("  2. vacuum_fluctuations_basic.png - Virtual particles")
print("  3. eight_consciousnesses_basic.png - Yogacara eight consciousnesses")
print("\n[Premium Version Includes]")
print("  - Quantum field complete simulator (4 sub-plots)")
print("  - Virtual particles & Feynman diagrams (3 sub-plots)")
print("  - Eight consciousnesses detailed (3 sub-plots)")
print("  - Mind-matter debate visualization (2 sub-plots)")
print("  - Total: 12 professional sub-plots")
print("\n[Key Findings]")
print("  - Feynman: 'Particles are just field excitations'")
print("  - Yogacara: 'All phenomena are consciousness manifestations'")
print("  - Field ≈ Alaya consciousness (both fundamental)")
print("  - Particles ≈ Manifested dharmas (both temporary)")
print("  - Vacuum not empty ≈ Alaya contains seeds")
print("  - Virtual particles ≈ Karmic seeds manifesting")
print("=" * 70)
