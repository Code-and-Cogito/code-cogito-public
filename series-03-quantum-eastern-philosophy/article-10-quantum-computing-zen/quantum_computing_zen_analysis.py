"""
Quantum Computing vs Zen - Free Version
Season 2 Article 10: Basic Visualizations

Author: Wina Wu
Date: 2025-12

Requirements:
pip install numpy matplotlib scipy
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Quantum Computing vs Zen - Free Version")
print("Season 2 Article 10")
print("=" * 70)

# Visualization 1: Qubit Superposition on Bloch Sphere
def bloch_sphere_basic():
    print("\n[Visualization 1] Qubit on Bloch Sphere")
    fig = plt.figure(figsize=(13, 11))
    ax = fig.add_subplot(111, projection='3d')

    # Sphere
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, alpha=0.1, color='cyan')

    # Axes
    ax.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', linewidth=2)
    ax.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', linewidth=2)
    ax.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', linewidth=2)

    # States
    ax.plot([0], [0], [1], 'ro', markersize=15, label='|0> (North)')
    ax.plot([0], [0], [-1], 'bo', markersize=15, label='|1> (South)')
    ax.plot([1], [0], [0], 'go', markersize=15, label='|+> = (|0>+|1>)/sqrt(2)')

    # Superposition state
    theta, phi = np.pi/3, np.pi/4
    sx = np.sin(theta)*np.cos(phi)
    sy = np.sin(theta)*np.sin(phi)
    sz = np.cos(theta)
    ax.quiver(0, 0, 0, sx, sy, sz, color='purple', arrow_length_ratio=0.15, linewidth=3)
    ax.plot([sx], [sy], [sz], 'mo', markersize=12, label='|psi> Superposition')

    ax.text(0, 0, 1.3, '|0>', fontsize=14, fontweight='bold')
    ax.text(0, 0, -1.3, '|1>', fontsize=14, fontweight='bold')
    ax.set_xlabel('X', fontsize=11)
    ax.set_ylabel('Y', fontsize=11)
    ax.set_zlabel('Z', fontsize=11)
    ax.set_title('Bloch Sphere: Qubit States\nBoth 0 AND 1 Simultaneously', fontsize=13, fontweight='bold')
    ax.legend(fontsize=9, loc='upper left')
    plt.savefig('bloch_sphere_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: Bloch sphere visualized")

# Visualization 2: Hadamard Gate Effect
def hadamard_gate_basic():
    print("\n[Visualization 2] Hadamard Gate")
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))

    # Before H gate
    ax1.bar(['|0>', '|1>'], [1, 0], color=['lightblue', 'lightgray'], edgecolor='black', linewidth=2)
    ax1.set_ylabel('Probability', fontsize=11)
    ax1.set_ylim(0, 1.2)
    ax1.set_title('BEFORE Hadamard\n|0> (Definite)', fontsize=12, fontweight='bold')
    ax1.text(0.5, 0.9, '0 or 1\n(Binary)', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # H gate
    ax2.text(0.5, 0.7, 'H', ha='center', va='center', fontsize=80, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='black', linewidth=3))
    ax2.text(0.5, 0.3, 'Hadamard Gate\nBreaking 0/1 Opposition', ha='center', fontsize=11)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_title('Hadamard Gate\nBreaking Duality', fontsize=12, fontweight='bold')

    # After H gate
    ax3.bar(['|0>', '|1>'], [0.5, 0.5], color=['lightblue', 'lightcoral'],
           edgecolor='black', linewidth=2, alpha=0.7)
    # Wavy overlay
    x_wave = np.linspace(0, 1, 100)
    y_wave = 0.5 * (1 + 0.1*np.sin(2*np.pi*10*x_wave))
    ax3.fill_between([-0.3, 1.3], [0, 0], [y_wave.max(), y_wave.max()],
                    alpha=0.2, color='purple')
    ax3.set_ylabel('Probability Amplitude', fontsize=11)
    ax3.set_ylim(0, 1.2)
    ax3.set_title('AFTER Hadamard\n|+> = (|0>+|1>)/sqrt(2) (Superposition)', fontsize=12, fontweight='bold')
    ax3.text(0.5, 0.9, 'Both 0 AND 1\n(Non-dual)', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    plt.tight_layout()
    plt.savefig('hadamard_gate_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: Hadamard gate effect shown")

# Visualization 3: Measurement Collapse
def measurement_collapse_basic():
    print("\n[Visualization 3] Measurement vs Arising Thought")
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 15))

    # Quantum: Before measurement
    ax1.text(0.5, 0.9, 'Quantum: BEFORE Measurement', ha='center', fontsize=12, fontweight='bold')
    ax1.bar(['|0>', '|1>'], [0.5, 0.5], color=['lightblue', 'lightcoral'],
           edgecolor='black', linewidth=2, alpha=0.6)
    ax1.set_ylabel('Probability', fontsize=11)
    ax1.text(0.5, 0.3, 'Superposition\nBoth 0 AND 1', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax1.set_ylim(0, 1)

    # Quantum: After measurement
    ax2.text(0.5, 0.9, 'Quantum: AFTER Measurement', ha='center', fontsize=12, fontweight='bold')
    ax2.bar(['|0>', '|1>'], [1, 0], color=['lightblue', 'lightgray'],
           edgecolor='black', linewidth=2)
    ax2.set_ylabel('Probability', fontsize=11)
    ax2.text(0.5, 0.3, 'Collapsed\nDefinite |0>', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax2.set_ylim(0, 1.2)

    # Zen: No-thought
    ax3.text(0.5, 0.9, 'Zen: No-Thought (Wu-Nian)', ha='center', fontsize=12, fontweight='bold')
    circle = plt.Circle((0.5, 0.5), 0.3, color='lightgreen', alpha=0.5, edgecolor='black', linewidth=3)
    ax3.add_patch(circle)
    ax3.text(0.5, 0.5, 'Wu-Nian\nNo discrimination\nAll possibilities', ha='center', fontsize=10)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')

    # Zen: Thought arises
    ax4.text(0.5, 0.9, 'Zen: Thought Arises (Qi-Nian)', ha='center', fontsize=12, fontweight='bold')
    ax4.text(0.5, 0.5, '"This is good"\n-> Discrimination', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='red', linewidth=3))
    ax4.text(0.5, 0.2, 'Falls into duality', ha='center', fontsize=9, style='italic')
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis('off')

    plt.tight_layout()
    plt.savefig('measurement_collapse_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: Measurement vs Qi-Nian compared")

# Execute
bloch_sphere_basic()
hadamard_gate_basic()
measurement_collapse_basic()

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nKey Findings:")
print("  - Qubit: Both 0 AND 1 simultaneously")
print("  - Zen: Neither existence nor non-existence (Fei-You Fei-Wu)")
print("  - Hadamard gate breaks 0/1 duality")
print("  - Zen breaks conceptual duality")
print("  - Measurement collapses superposition")
print("  - Thought (Qi-Nian) breaks no-thought")
print("  - Similarity: 8.8/10")
print("=" * 70)
