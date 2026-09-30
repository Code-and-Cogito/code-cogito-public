"""
Article 04: Perspective - The Math Behind Renaissance Art
Free Highlights: 3D-to-2D Projection & Vanishing Point Demo
Series: The Digital Rebirth of the Renaissance | Code & Cogito

Note on the numbers: the projection scale (f / z) is computed. The depth /
proportion / spatial scores in section 3 are ILLUSTRATIVE values assigned by
the author (no scoring rubric, not measurements); they only show a trend.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Perspective Projection: 3D Cube -> 2D ---

focal_length = 5.0

# 3D cube: front face at z=5, back face at z=10
# (centred on the viewing axis, x and y from -1 to 1, so the vanishing point
#  sits in the middle of the drawing; the article snippet uses a 0..1 cube,
#  but the scale f/z depends only on z and is identical)
vertices_3d = np.array([
    [-1, -1, 5], [1, -1, 5], [1, 1, 5], [-1, 1, 5],
    [-1, -1, 10], [1, -1, 10], [1, 1, 10], [-1, 1, 10]
])

edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
         (0,4),(1,5),(2,6),(3,7)]

# Project: x2d = x3d * f / z3d
vertices_2d = np.zeros((8, 2))
for i, (x, y, z) in enumerate(vertices_3d):
    vertices_2d[i] = [x * focal_length / z, y * focal_length / z]

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
for e0, e1 in edges:
    ax.plot([vertices_2d[e0,0], vertices_2d[e1,0]],
            [vertices_2d[e0,1], vertices_2d[e1,1]], 'b-', linewidth=1.5)
ax.plot(0, 0, 'ro', markersize=8, label='Vanishing Point')
ax.set_title('Perspective Projection: 3D Cube on 2D Canvas', fontsize=14)
ax.set_xlabel('X (projected)')
ax.set_ylabel('Y (projected)')
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('perspective_cube_projection.png', dpi=150)
plt.show()

# --- 2. One-Point Perspective: Converging Lines ---
# Schematic drawing only: the lines are drawn to meet at the vanishing point,
# they are not computed from a painting or from the projection above.

fig, ax = plt.subplots(figsize=(10, 6))
vp = (0.5, 0.5)  # vanishing point (normalized)
n_lines = 8

for i in range(n_lines):
    t = i / (n_lines - 1)
    start_x = t
    ax.plot([start_x, vp[0]], [0, vp[1]], 'b-', alpha=0.6, linewidth=1)
    ax.plot([start_x, vp[0]], [1, vp[1]], 'b-', alpha=0.6, linewidth=1)

ax.plot(*vp, 'ro', markersize=12, zorder=5, label='Vanishing Point')
ax.axhline(y=vp[1], color='gray', linestyle='--', alpha=0.5, label='Horizon Line')

# Floor grid
for d in np.linspace(0, 1, 6):
    y = vp[1] * d
    w = 1 - d * 0.8
    ax.plot([0.5 - w/2, 0.5 + w/2], [y, y], 'g-', alpha=0.4)

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_title('One-Point Perspective: All Lines Converge', fontsize=14)
ax.legend()
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('one_point_perspective.png', dpi=150)
plt.show()

# --- 3. Depth Perception: Medieval vs Renaissance ---
# ILLUSTRATIVE scores (0-100) assigned by the author's judgement: there is no
# scoring rubric and nothing here was measured. They only show the trend from
# medieval to Renaissance art. "Brunelleschi" stands for his perspective panels
# (mirror demonstration, c.1413-1420; the exact date is not recorded and the
# panel is lost).

data = {
    'Work': ['Medieval Icon\n(1200)', 'Giotto\n(1305)', 'Brunelleschi\n(c.1413-20)', 'Last Supper\n(1498)'],
    'Depth': [15, 45, 85, 95],
    'Proportion': [25, 55, 90, 95],
    'Spatial': [20, 50, 88, 95]
}

x = np.arange(len(data['Work']))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, data['Depth'], width, label='Depth Perception', color='#2196F3')
ax.bar(x, data['Proportion'], width, label='Proportion Consistency', color='#FF9800')
ax.bar(x + width, data['Spatial'], width, label='Spatial Coherence', color='#4CAF50')

ax.set_xlabel('Artwork / Year')
ax.set_ylabel('Illustrative score (0-100)')
ax.set_title('Spatial Quality: Medieval vs Renaissance Art\n'
             '(illustrative scores assigned by the author, not measurements)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(data['Work'])
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('depth_comparison.png', dpi=150)
plt.show()

print("\n=== Perspective Analysis Summary ===")
print(f"Depth score 1200->1498 (illustrative): {data['Depth'][0]} -> {data['Depth'][-1]}")
print(f"Projection scale at z=5:  {focal_length/5:.2f}")
print(f"Projection scale at z=10: {focal_length/10:.2f}")
print("Deep Dive Pack adds a projection-matrix demo, vanishing-point geometry")
print("diagrams and a Monte Carlo simulation of vanishing-point error.")
