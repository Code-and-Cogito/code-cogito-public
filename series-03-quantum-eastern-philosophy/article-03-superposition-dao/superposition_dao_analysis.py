"""
Quantum Superposition vs the Dao of Laozi and Zhuangzi
Series 3, Article 03 | Free Version

Author: Wina @ Code & Cogito
Series: Quantum Mechanics Meets Eastern Philosophy #03/12

This standalone free script includes:
  1. Schrodinger's Cat probability evolution
  2. Taiji (Yin-Yang) diagram: Being and Non-being
  3. Zhuangzi's Butterfly Dream superposition illustration

DATA NOTES (read before quoting any number from the plots):
  - Nothing here is measured data. Every input is a hand-set illustrative
    value: the 1-hour half-life (the usual textbook telling of the cat
    thought experiment; a modelling choice), the 0.5 / 1 / 2 h sample times,
    the 100 simulated box-openings per time, the equal 50/50 amplitudes in
    the butterfly panel, and the layout of the taiji drawing.
  - The simulated box-openings use a fixed random seed (RANDOM_SEED below),
    so the printed counts are identical on every run. Set it to None to get
    a different sample each time.
  - The Dao/quantum mappings (Yang = Being, Yin = Non-being, Zhuangzi and
    butterfly as two basis states) are illustrative analogies drawn in the
    article, not physical models.
  - The decoherence simulation from the article is not part of this free
    script.

Requirements:
    pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Fixed seed so the simulated box-openings print the same counts on every run.
# Set to None for a different random sample each time.
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

print("=" * 70)
print("Quantum Superposition vs the Dao of Laozi and Zhuangzi")
print("Series 3 Article 03 | Free Version")
print("=" * 70)
print()

# ============================================================================
# Model 1: Schrodinger's Cat - Probability Evolution
# ============================================================================

class SchrodingerCat:
    """
    Schrodinger's Cat simulation (idealised model: one atom, exponential
    decay, no decoherence).
    Includes: atom state, cat state, time evolution, and measurement.
    """

    def __init__(self, half_life=1.0):
        # half_life is in hours. One hour follows the usual telling of the
        # thought experiment; it is a modelling choice, not a measured value.
        self.half_life = half_life
        self.lambda_decay = np.log(2) / half_life  # Decay constant

    def atom_state(self, t):
        """Quantum state of the atom at time t: |psi> = alpha|undecayed> + beta|decayed>"""
        alpha = np.sqrt(np.exp(-self.lambda_decay * t))
        beta = np.sqrt(1 - np.exp(-self.lambda_decay * t))
        return alpha, beta

    def cat_state(self, t):
        """Cat state evolving over time: |cat> = alpha|alive> + beta|dead>"""
        alpha, beta = self.atom_state(t)
        prob_alive = np.abs(alpha)**2
        prob_dead = np.abs(beta)**2
        return prob_alive, prob_dead

    def measure(self, t):
        """Open the box and measure the cat's state -- wavefunction collapse"""
        prob_alive, prob_dead = self.cat_state(t)
        outcome = np.random.choice(['alive', 'dead'],
                                   p=[prob_alive, prob_dead])
        return outcome


def schrodinger_cat_basic():
    """
    Schrodinger's cat probability evolution over time.
    The key insight (Copenhagen reading, as argued in the article):
    superposition is NOT ignorance -- it is genuine both-ness.
    """
    print("\n[Model 1] Schrodinger's Cat: Superposition Evolution")
    print("-" * 70)
    print(f"  Illustrative model: half-life = 1 h, random seed = {RANDOM_SEED}")

    cat = SchrodingerCat(half_life=1.0)
    max_time = 3.0
    times = np.linspace(0, max_time, 100)

    probs_alive = []
    probs_dead = []
    for t in times:
        p_alive, p_dead = cat.cat_state(t)
        probs_alive.append(p_alive)
        probs_dead.append(p_dead)

    plt.figure(figsize=(13, 7))
    plt.fill_between(times, 0, probs_alive, alpha=0.5, color='green', label='P(cat alive)')
    plt.fill_between(times, 0, probs_dead, alpha=0.5, color='red', label='P(cat dead)')
    plt.plot(times, probs_alive, 'g-', linewidth=2.5)
    plt.plot(times, probs_dead, 'r-', linewidth=2.5)

    plt.axhline(y=0.5, color='gray', linestyle='--', linewidth=2, alpha=0.5)
    plt.axvline(x=cat.half_life, color='black', linestyle='--', linewidth=2)
    plt.text(cat.half_life + 0.1, 0.92,
             f'Half-life\nP(alive) = P(dead) = 50%',
             fontsize=9, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    plt.text(max_time * 0.72, 0.55,
             'Copenhagen reading: this is NOT\n'
             '"either dead or alive"!\n'
             'It is "genuinely both\n'
             'dead AND alive"!\n'
             '|cat> = a|alive> + b|dead>',
             fontsize=9, ha='center',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    plt.xlabel('Time (hours) -- illustrative 1-hour half-life', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Schrodinger's Cat: Superposition Evolving Over Time\n"
              "(Before opening the box; idealised model)",
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=12, loc='center left')
    plt.grid(alpha=0.3)
    plt.ylim(0, 1.15)

    plt.tight_layout()
    plt.savefig('schrodinger_cat_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Run experiment simulations: each trial opens the box once and draws
    # alive/dead at random with the theoretical probabilities
    for t_exp in [0.5, 1.0, 2.0]:
        prob_alive, prob_dead = cat.cat_state(t_exp)
        n_trials = 100
        results = [cat.measure(t_exp) for _ in range(n_trials)]
        count_alive = results.count('alive')
        count_dead = results.count('dead')

        print(f"\n  t = {t_exp}h | Theory: P(alive)={prob_alive:.2%}, P(dead)={prob_dead:.2%}")
        print(f"           | Experiment ({n_trials} trials): alive={count_alive}, dead={count_dead}")

    print(f"\n  Key insight (Copenhagen reading):")
    print(f"  At t=1h (half-life): 50% alive, 50% dead")
    print(f"  But NOT 'either alive or dead, we don't know'")
    print(f"  Rather: 'genuinely in superposition of both states'")
    print(f"  Until measurement (opening box) causes wavefunction collapse")


# ============================================================================
# Model 2: Taiji (Yin-Yang) - Being and Non-being Mutual Arising
# ============================================================================

def taiji_you_wu():
    """
    Taiji symbol representing Laozi's 'Being and Non-being give rise to each other'.
    Parallels quantum superposition: |psi> = a|being> + b|non-being>.
    """
    print("\n[Model 2] Taiji: Being and Non-being Mutual Arising")
    print("-" * 70)

    fig, ax = plt.subplots(figsize=(10, 11))

    # Schematic drawing (Yang = white = Being, Yin = black = Non-being, as
    # mapped in the article). Left half black, right half white ...
    ax.add_patch(Wedge((0, 0), 1, 90, 270, facecolor='black', edgecolor='none'))
    ax.add_patch(Wedge((0, 0), 1, -90, 90, facecolor='white', edgecolor='none'))

    # ... then two half-size discs make the S-curve: black bulges into the
    # white side at the top, white bulges into the black side at the bottom
    ax.add_patch(Circle((0, 0.5), 0.5, facecolor='black', edgecolor='none'))
    ax.add_patch(Circle((0, -0.5), 0.5, facecolor='white', edgecolor='none'))

    # Fish eyes: a seed of white inside the black, a seed of black inside the white
    ax.add_patch(Circle((0, 0.5), 0.12, facecolor='white', edgecolor='none'))
    ax.add_patch(Circle((0, -0.5), 0.12, facecolor='black', edgecolor='none'))

    # Outer outline
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=3))

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.6, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.text(0.72, 0, 'Yang\n(Being)', ha='center', va='center',
            fontsize=11, fontweight='bold')
    ax.text(-0.72, 0, 'Yin\n(Non-being)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    ax.set_title('Taiji: Being and Non-Being Give Rise to Each Other\n'
                 '"The Dao that can be spoken is not the eternal Dao"',
                 fontsize=14, fontweight='bold', pad=15)
    ax.text(0, -1.5,
            'Opposites are not contradictions -- they are two faces of the same whole\n'
            'Quantum parallel: |psi> = a|being> + b|non-being>',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    plt.savefig('taiji_you_wu_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Laozi, Dao De Jing:")
    print("  Ch. 1: 'The Dao that can be spoken is not the eternal Dao'")
    print("  Ch. 2: 'Being and non-being give rise to each other'")
    print()
    print("  Quantum parallel:")
    print("  Before measurement: no definite state (like the unnamed Dao)")
    print("  After measurement: definite state (like named phenomena)")
    print("  Superposition IS the foundation -- definite states are its products")


# ============================================================================
# Model 3: Zhuangzi's Butterfly Dream
# ============================================================================

def butterfly_dream():
    """
    Quantum interpretation of Zhuangzi's Butterfly Dream.
    Before 'waking' (measurement): |psi> = a|Zhuangzi> + b|butterfly>.
    """
    print("\n[Model 3] Zhuangzi's Butterfly Dream: Quantum Interpretation")
    print("-" * 70)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Left: Superposition state (before waking)
    states = ['Zhuangzi', 'Butterfly']
    # Equal weights chosen for illustration; the story gives no numbers
    amplitudes = [1 / np.sqrt(2), 1 / np.sqrt(2)]
    probabilities = [a ** 2 for a in amplitudes]

    bars = ax1.bar(states, amplitudes, color=['#4ECDC4', '#FFD700'],
                   alpha=0.8, edgecolor='black', linewidth=2)
    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height + 0.05,
                 f'P = {prob:.0%}', ha='center', fontsize=12, fontweight='bold')

    ax1.set_ylabel('Probability Amplitude', fontsize=12)
    ax1.set_ylim(0, 1)
    ax1.set_title('Before "Waking" (Measurement)\n'
                  '|psi> = (|Zhuangzi> + |butterfly>) / sqrt(2)',
                  fontsize=13, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    ax1.text(0.5, 0.87, 'BOTH states coexist\n-- equally real!',
             ha='center', fontsize=10, style='italic',
             transform=ax1.transAxes,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # Right: After measurement (collapse)
    measurement_result = 'Zhuangzi'
    colors = ['#4ECDC4', 'lightgray']
    post_probs = [1.0, 0.0]

    bars = ax2.bar(states, post_probs, color=colors,
                   alpha=0.8, edgecolor='black', linewidth=2)
    for bar, prob in zip(bars, post_probs):
        height = bar.get_height()
        if height > 0:
            ax2.text(bar.get_x() + bar.get_width() / 2, height + 0.05,
                     f'P = {prob:.0%}', ha='center', fontsize=12, fontweight='bold')

    ax2.set_ylabel('Probability', fontsize=12)
    ax2.set_ylim(0, 1.2)
    ax2.set_title('After "Waking" (Measurement)\n'
                  'Wavefunction collapsed to |Zhuangzi>',
                  fontsize=13, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    ax2.text(0.5, 0.9, 'One possible outcome (50/50)\n-- could have gone either way',
             ha='center', fontsize=10, style='italic',
             transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

    plt.tight_layout()
    plt.savefig('butterfly_dream_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Zhuangzi's question (Qiwulun chapter of the Zhuangzi, paraphrased):")
    print("  'Was it Zhuang Zhou dreaming he was a butterfly?")
    print("   Or a butterfly dreaming it was Zhuang Zhou?'")
    print()
    print("  Quantum reading (an analogy, not physics):")
    print("  Before 'waking' (measurement): BOTH -- in superposition")
    print("  After 'waking' (measurement): one outcome collapses")
    print("  Which is 'real'? Both are, and neither is.")
    print("  There is no 'absolutely real' answer!")


# ============================================================================
# Execute All Models
# ============================================================================

print("\nGenerating visualizations...\n")

schrodinger_cat_basic()
taiji_you_wu()
butterfly_dream()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete")
print("=" * 70)
print("\nGenerated plots:")
print("  1. schrodinger_cat_basic.png  -- Probability evolution over time")
print("  2. taiji_you_wu_basic.png     -- Yin-Yang: being/non-being mutual arising")
print("  3. butterfly_dream_basic.png  -- Zhuangzi's superposition interpretation")
print("\nKey insights from this article (Copenhagen reading plus the article's analogies):")
print("  - Superposition is REAL, not ignorance")
print("  - Measurement creates definite state (like naming creates distinctions)")
print("  - Laozi's 'Dao' parallels the superposition before measurement")
print("  - Zhuangzi's butterfly dream = superposition of identities")
print("  - Determinacy is a product of observation, not a feature of reality")
print("=" * 70)
