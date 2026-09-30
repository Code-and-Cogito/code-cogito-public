"""
Meditation & Quantum States - Free Version
Series 3, Article 11 of 12: Basic Visualizations

Author: Wina Wu
Date: 2025-01

Requirements:
pip install numpy matplotlib

Data note (what is real and what is illustrative):
- Real-world reference (text output and one chart annotation):
  Lutz, Greischar, Rawlings, Ricard & Davidson (2004), "Long-term meditators
  self-induce high-amplitude gamma synchrony during mental practice", PNAS
  101(46), 16369-16373. Eight long-term Buddhist practitioners (10,000-50,000
  hours of practice over 15-40 years) vs. controls. Reported: the gamma (25-42 Hz)
  to slow-wave ratio was already higher at rest, and during meditation the adjusted
  average increase in gamma activity was more than 30 times that of the controls.
- Everything else in the charts (sine waves, bar heights, probabilities) is
  hand-set and illustrative. It shows direction and structure, not measured EEG data.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Meditation & Quantum States - Free Version")
print("Series 3, Article 11 of 12")
print("=" * 70)

# Visualization 1: Brain Wave Types
def brainwave_types_basic():
    print("\n[Visualization 1] Five Brain Wave Types")
    fig, ax = plt.subplots(figsize=(16, 9))

    time = np.linspace(0, 2, 1000)
    y_offset = 0

    # Schematic sine waves: one representative frequency per band, NOT EEG recordings.
    # Band edges are conventional and differ between sources. Gamma is often given
    # as ~25-100 Hz (Lutz et al. 2004 analysed 25-42 Hz).
    waves = [
        ('Delta', 2, '0.5-4', 'Deep sleep'),
        ('Theta', 6, '4-8', 'Light sleep, deep meditation'),
        ('Alpha', 10, '8-12', 'Relaxed, light meditation'),
        ('Beta', 20, '13-30', 'Normal waking, thinking'),
        ('Gamma', 40, '25-100', 'High focus, consciousness integration'),
    ]

    colors = ['blue', 'green', 'orange', 'red', 'purple']

    for i, (name, freq, range_hz, desc) in enumerate(waves):
        y_offset = -i * 2
        wave = np.sin(2 * np.pi * freq * time) + y_offset
        ax.plot(time, wave, color=colors[i], linewidth=2, label=f'{name} {range_hz} Hz')
        ax.text(2.05, y_offset, desc, fontsize=9, va='center')

    ax.set_xlabel('Time (s)', fontsize=11)
    ax.set_ylabel('Amplitude (offset for clarity)', fontsize=11)
    ax.set_title('Five Types of Brain Waves\nDifferent frequencies reflect different states of consciousness',
                fontsize=13, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.set_xlim(0, 3.0)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig('brainwave_types_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: Brain wave types visualized")

# Visualization 2: Meditation Stages
def meditation_stages_basic():
    print("\n[Visualization 2] Meditation Brain Wave Changes")
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))

    # NOTE: every bar height below (normal / beginner / advanced) is a hand-set,
    # illustrative relative-power value, NOT measured data. Only the annotation in the
    # last panel refers to a real result (Lutz et al. 2004, PNAS 101(46)).
    # Normal waking state
    wave_types = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']
    normal = [0.1, 0.2, 0.3, 0.6, 0.2]

    ax1.bar(wave_types, normal, color=['blue', 'green', 'orange', 'red', 'purple'],
           edgecolor='black', linewidth=1.5, alpha=0.7)
    ax1.set_ylabel('Relative Power (illustrative)', fontsize=11)
    ax1.set_title('Normal Waking State', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 1)
    ax1.text(2, 0.8, 'Dominated by\nBeta waves', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # Beginner meditation
    beginner = [0.15, 0.35, 0.55, 0.25, 0.15]

    ax2.bar(wave_types, beginner, color=['blue', 'green', 'orange', 'red', 'purple'],
           edgecolor='black', linewidth=1.5, alpha=0.7)
    ax2.set_ylabel('Relative Power (illustrative)', fontsize=11)
    ax2.set_title('Beginner Meditation (0-1 year)', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 1)
    ax2.text(2, 0.8, 'Alpha increases\nBeta decreases', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    # Advanced meditation
    advanced = [0.1, 0.25, 0.35, 0.15, 0.85]

    ax3.bar(wave_types, advanced, color=['blue', 'green', 'orange', 'red', 'purple'],
           edgecolor='black', linewidth=1.5, alpha=0.7)
    ax3.set_ylabel('Relative Power (illustrative)', fontsize=11)
    ax3.set_title('Advanced Meditation (10,000+ hours)', fontsize=12, fontweight='bold')
    ax3.set_ylim(0, 1)
    # Real result (Lutz et al. 2004): 8 long-term practitioners, 10,000-50,000 h over
    # 15-40 years; adjusted average gamma (25-42 Hz) increase during meditation was
    # more than 30-fold that of controls (this is NOT the ratio of the bars above).
    ax3.text(3.6, 0.99, 'Gamma: increase\n>30x that of controls\n(Lutz et al., 2004)', ha='center',
            va='top', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='red', linewidth=2))

    fig.text(0.5, 0.01, 'Bar heights are hand-set illustrative values, not measured data. '
             'Annotation: Lutz et al. (2004), PNAS 101(46), 16369-16373.',
             ha='center', fontsize=9, style='italic')
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig('meditation_stages_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: Meditation stages compared")

# Visualization 3: No-thought vs Superposition
def nothought_superposition_basic():
    print("\n[Visualization 3] No-thought vs Superposition")
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 15))

    # Ordinary mind (with thoughts)
    ax1.text(0.5, 0.92, 'Ordinary Mind (With Thought)', ha='center', fontsize=12, fontweight='bold')
    thoughts = ['Good/Bad', 'Self/Other', 'Right/Wrong', 'Like/Dislike']
    y_pos = [0.7, 0.55, 0.4, 0.25]
    for thought, y in zip(thoughts, y_pos):
        ax1.text(0.5, y, thought, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7,
                         edgecolor='red', linewidth=2))
    ax1.text(0.5, 0.05, 'Fixed concepts\nDualistic thinking', ha='center',
            fontsize=9, style='italic')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')

    # No-thought mind
    ax2.text(0.5, 0.92, 'No-thought Mind (Wu-Nian)', ha='center', fontsize=12, fontweight='bold')
    circle = plt.Circle((0.5, 0.5), 0.25, color='lightgreen', alpha=0.5,
                        edgecolor='darkgreen', linewidth=3)
    ax2.add_patch(circle)
    ax2.text(0.5, 0.5, 'Clear\nOpen\nNon-dual', ha='center', fontsize=11, fontweight='bold')
    ax2.text(0.5, 0.05, 'No fixed concepts\nFull of potential', ha='center',
            fontsize=9, style='italic')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    # Classical state (definite)
    ax3.text(0.5, 0.9, 'Classical State (Definite)', ha='center', fontsize=12, fontweight='bold',
            transform=ax3.transAxes)
    ax3.bar(['|0>', '|1>'], [1, 0], color=['lightblue', 'lightgray'],
           edgecolor='black', linewidth=2)
    ax3.set_ylabel('Probability', fontsize=10)
    ax3.text(0.5, 0.5, 'Definite\nEither 0 OR 1', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7),
            transform=ax3.transAxes)
    ax3.set_ylim(0, 1.2)

    # Quantum superposition
    ax4.text(0.5, 0.9, 'Quantum Superposition', ha='center', fontsize=12, fontweight='bold',
            transform=ax4.transAxes)
    ax4.bar(['|0>', '|1>'], [0.5, 0.5], color=['lightblue', 'lightcoral'],
           edgecolor='black', linewidth=2, alpha=0.7)
    # Wavy overlay
    ax4.fill_between([-0.2, 1.2], [0, 0], [0.6, 0.6], alpha=0.2, color='purple')
    ax4.set_ylabel('Probability Amplitude', fontsize=10)
    ax4.text(0.5, 0.5, 'Superposition\nBoth 0 AND 1', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
            transform=ax4.transAxes)
    ax4.set_ylim(0, 1.2)

    # Add connection annotation
    fig.text(0.5, 0.48, 'STRUCTURAL PARALLEL', ha='center', fontsize=11,
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('nothought_superposition_basic.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("  Done: No-thought vs superposition compared")

# Execute
brainwave_types_basic()
meditation_stages_basic()
nothought_superposition_basic()

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nKey Points:")
print("  - Brain waves: Delta, Theta, Alpha, Beta, Gamma")
print("  - Long-term meditators (Lutz et al. 2004): gamma increase >30x that of controls")
print("  - No-thought (Wu-Nian) ~ Superposition (Die-Jia-Tai): a structural analogy")
print("  - Both: Open state full of potential")
print("  - Holding superposition vs. decoherence ~ holding no-mind vs. attachment")
print("  - Note: chart values (waves, bars) are illustrative, not measured data")
print("=" * 70)
