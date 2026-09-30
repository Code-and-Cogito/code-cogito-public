#!/usr/bin/env python3
"""Free highlight code from Code & Cogito Renaissance Series.
Article 03: Da Vinci's Vitruvian Man - Body proportions and the golden-ratio myth.

Note: the golden-ratio navel used below is a MODEL ASSUMPTION, not a measurement.
Neither Vitruvius nor Leonardo mentions it; linking the navel to the golden ratio
became popular only from the 19th century on.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

# === Body Proportions (head-length = 1 unit) ===

PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ~ 1.618
HEAD = 1.0

# Simple fractions of height, as in Vitruvius and Leonardo's annotations (see the article):
# head 1/8, face 1/10, hand 1/10, foot 1/7 (Vitruvius gives 1/6; Leonardo wrote 1/7),
# arm span = height. Shoulder width (1/4 of height) is a simple-fraction model setting.
BODY_PROPORTIONS = {
    'Head length': HEAD,                      # 1/8 of height
    'Face length': HEAD * 8 / 10,             # 1/10 of height (hairline to chin)
    'Height': HEAD * 8,
    'Arm span': HEAD * 8,                     # arm span = height (the square)
    'Navel to top': HEAD * 8 - (HEAD * 8 / PHI),
    'Navel to feet': HEAD * 8 / PHI,          # assumption: navel at the golden section, not measured
    'Shoulder width': HEAD * 2,               # 1/4 of height
    'Hand length': HEAD * 8 / 10,             # 1/10 of height (same as face length)
    'Foot length': HEAD * 8 / 7               # 1/7 of height (Leonardo; Vitruvius: 1/6)
}

print("=" * 60)
print("Vitruvian Man: Body Proportion Analysis")
print("=" * 60)

print(f"\n{'Body Part':<20} {'Ratio (heads)':<15} {'Value':<10}")
print("-" * 45)
for part, value in BODY_PROPORTIONS.items():
    print(f"{part:<20} {value/HEAD:<15.3f} {value:<10.3f}")
print("Note: 'Navel to top' / 'Navel to feet' are model settings (navel at height/phi), not measurements.")

# === Golden Ratio Check (not an independent test) ===
# The navel was placed at height/phi above the soles, so this ratio equals phi by
# construction. It recovers the assumption; it does not verify anything about Leonardo.

navel_ratio = BODY_PROPORTIONS['Navel to feet'] / BODY_PROPORTIONS['Navel to top']

print(f"\n[Golden Ratio Check]")
print(f"Navel division ratio: {navel_ratio:.6f}")
print(f"Golden ratio phi:     {PHI:.6f}")
print(f"Error:                {abs(navel_ratio - PHI):.6f}")
print(f"=> Equals phi by construction: the navel was placed at height/phi (an assumption, not a measurement).")

print(f"\n[Key Findings]")
print(f"  Height = 8 head-lengths (classic drawing proportion)")
print(f"  Arm span = Height (body fits in a square)")
print(f"  Navel placed at the golden section (assumption; not in Vitruvius or Leonardo)")
print(f"  Circle centered on the navel when arms and legs are spread")

# === Visualization: Simplified Vitruvian Man ===

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

height = BODY_PROPORTIONS['Height']
arm_span = BODY_PROPORTIONS['Arm span']
navel_y = BODY_PROPORTIONS['Navel to feet']

# Left: Circle (arms and legs spread)
circle_radius = navel_y  # navel-to-sole distance, so the spread feet touch the circle
circle = Circle((0, navel_y), circle_radius, fill=False,
                edgecolor='#4169E1', linewidth=2, linestyle='--')
ax1.add_patch(circle)

head_radius = HEAD / 2
head = Circle((0, height - head_radius), head_radius, fill=False,
              edgecolor='black', linewidth=2)
ax1.add_patch(head)

ax1.plot([0, 0], [navel_y, height - HEAD], 'k-', linewidth=3)
ax1.plot([-BODY_PROPORTIONS['Shoulder width']/2, BODY_PROPORTIONS['Shoulder width']/2],
         [height - HEAD, height - HEAD], 'k-', linewidth=3)

arm_length = arm_span / 2
ax1.plot([0, -arm_length], [height - HEAD*1.5, height - HEAD*2], 'k-', linewidth=2)
ax1.plot([0, arm_length], [height - HEAD*1.5, height - HEAD*2], 'k-', linewidth=2)

leg_angle = np.pi / 6
leg_length = navel_y
ax1.plot([0, -leg_length*np.sin(leg_angle)], [navel_y, navel_y - leg_length*np.cos(leg_angle)], 'k-', linewidth=3)
ax1.plot([0, leg_length*np.sin(leg_angle)], [navel_y, navel_y - leg_length*np.cos(leg_angle)], 'k-', linewidth=3)

ax1.plot(0, navel_y, 'ro', markersize=10)
ax1.text(0.3, navel_y, 'Navel\n(set at golden section)', fontsize=9, color='red', fontweight='bold')
ax1.set_xlim(-5.5, 5.5)
ax1.set_ylim(-2, 10)
ax1.set_aspect('equal')
ax1.set_title('Circle: Center at Navel', fontsize=13, fontweight='bold')
ax1.axis('off')

# Right: Square (standing straight)
rect = Rectangle((-arm_span/2, 0), arm_span, height, fill=False,
                 edgecolor='#C41E3A', linewidth=2, linestyle='--')
ax2.add_patch(rect)

head2 = Circle((0, height - head_radius), head_radius, fill=False,
               edgecolor='black', linewidth=2)
ax2.add_patch(head2)

ax2.plot([0, 0], [0, height - HEAD], 'k-', linewidth=3)
ax2.plot([-BODY_PROPORTIONS['Shoulder width']/2, BODY_PROPORTIONS['Shoulder width']/2],
         [height - HEAD, height - HEAD], 'k-', linewidth=3)

ax2.plot([0, -arm_span/2], [height - HEAD*1.5, height - HEAD*2.5], 'k-', linewidth=2)
ax2.plot([0, arm_span/2], [height - HEAD*1.5, height - HEAD*2.5], 'k-', linewidth=2)

ax2.plot([0, -0.5], [0, 0], 'k-', linewidth=3)
ax2.plot([0, 0.5], [0, 0], 'k-', linewidth=3)
ax2.plot([-0.5, -0.5], [0, navel_y*0.01], 'k-', linewidth=3)
ax2.plot([0.5, 0.5], [0, navel_y*0.01], 'k-', linewidth=3)

ax2.plot(0, navel_y, 'ro', markersize=10)
ax2.annotate(f'Height / phi = {navel_y:.2f}', xy=(0, navel_y),
             xytext=(1.5, navel_y+0.5), fontsize=9, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax2.set_xlim(-5.5, 5.5)
ax2.set_ylim(-1, 9.5)
ax2.set_aspect('equal')
ax2.set_title('Square: Arm Span = Height', fontsize=13, fontweight='bold')
ax2.axis('off')

fig.suptitle("Da Vinci's Vitruvian Man: Body as Universe",
             fontsize=16, fontweight='bold', y=0.98)
fig.text(0.5, 0.02, "Simplified model: the navel is placed at height/phi above the soles by assumption "
         "(not a measurement; not in Vitruvius or Leonardo).",
         ha='center', fontsize=10, color='dimgray')
plt.tight_layout()
plt.savefig('vitruvian_man_basic.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved: vitruvian_man_basic.png")
