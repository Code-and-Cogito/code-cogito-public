# Code & Cogito: Da Vinci's Anatomical Revolution
# Article: https://code-cogito.com/en/da-vinci-anatomy-revolution-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np

# Set font

print("=" * 60)
print("Vitruvian Man Body Proportion Analysis")
print("=" * 60)

# ===== Part 1: Calculate Body Proportions =====

# Golden Ratio
PHI = (1 + np.sqrt(5)) / 2  # ≈ 1.618

# Base unit: head length = 1
HEAD = 1.0

# Vitruvian body proportions (head length as base unit)
BODY_PROPORTIONS = {
    'Head': HEAD,
    'Face': HEAD * 8/10,              # Face = 1/10 height = 0.8x head
    'Height': HEAD * 8,               # Height = 8 heads
    'Arm span': HEAD * 8,             # Arm span = height
    'Navel to crown': HEAD * 8 - (HEAD * 8 / PHI),
    'Navel to sole': HEAD * 8 / PHI, # Assumption: navel at the golden section (a set value, not a measurement)
    'Shoulder width': HEAD * 2,
    'Palm length': HEAD * 8/10,       # Palm = face
    'Foot length': HEAD * 8/7
}

print("\n[Body Proportion Table]")
print(f"{'Body Part':<18} {'Ratio (heads)':<15} {'Value':<10}")
print("-" * 45)

for part, value in BODY_PROPORTIONS.items():
    ratio = value / HEAD
    print(f"{part:<18} {ratio:<15.3f} {value:<10.3f}")

# Check the golden ratio: the navel was placed using PHI, so this returns PHI by construction (not an independent test)
navel_ratio = BODY_PROPORTIONS['Navel to sole'] / BODY_PROPORTIONS['Navel to crown']

print(f"\n[Golden Ratio Check]")
print(f"Navel division ratio: {navel_ratio:.3f}")
print(f"Golden ratio phi: {PHI:.3f}")
print(f"Error: {abs(navel_ratio - PHI):.4f}")

if abs(navel_ratio - PHI) < 0.01:
    print("=> Matches the input: the navel was placed at the golden section by assumption")
else:
    print("=> Deviation from golden ratio detected")

print(f"\n[Key Findings]")
print(f"- The human body is not random; it follows mathematical rules")
print(f"- Navel position: set at the golden section in this model (an assumption, not a measurement)")
print(f"- Height = 8 head lengths (the classic artistic proportion)")
print(f"- Arm span = height (forming a perfect square)")
print(f"\n=> The body as microcosm: mathematics as aesthetics")

# ===== Part 2: Vitruvian Man Visualization =====

height = BODY_PROPORTIONS['Height']
arm_span = BODY_PROPORTIONS['Arm span']
navel_y = BODY_PROPORTIONS['Navel to sole']

# === Left: Human in Circle (arms and legs spread) ===

# Draw circle (centered on navel)
circle_radius = arm_span / 2
circle = Circle((0, navel_y), circle_radius,
               fill=False, edgecolor='#4169E1', linewidth=2, linestyle='--')

# Simplified human figure
head_radius = HEAD / 2
head = Circle((0, height - head_radius), head_radius,
             fill=False, edgecolor='black', linewidth=2)

# Torso
torso_width = BODY_PROPORTIONS['Shoulder width']

# Arms (spread)
arm_length = arm_span / 2

# Legs (spread, touching the circle)
leg_angle = np.pi / 6  # 30 degrees
leg_length = navel_y
left_leg_x = -leg_length * np.sin(leg_angle)
left_leg_y = navel_y - leg_length * np.cos(leg_angle)

right_leg_x = leg_length * np.sin(leg_angle)
right_leg_y = navel_y - leg_length * np.cos(leg_angle)

# Annotation

# === Right: Human in Square (legs together, arms level) ===

# Draw square
square_side = height
square = Rectangle((-square_side/2, 0), square_side, square_side,
                  fill=False, edgecolor='#C41E3A', linewidth=2, linestyle='--')

# Head
head2 = Circle((0, height - head_radius), head_radius,
              fill=False, edgecolor='black', linewidth=2)

# Torso

# Arms (horizontal)

# Legs (together)

# Golden ratio annotation

print("\n=> Visualization complete: vitruvian_man.png")
print("=> Da Vinci's Vitruvian Man: the perfect union of math and art")
