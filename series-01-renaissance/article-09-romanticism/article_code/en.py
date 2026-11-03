# Code & Cogito: Romanticism: When Poets Rebel Against Philosophers
# Article: https://code-cogito.com/en/romanticism-poets-vs-philosophers-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
"""
Romanticism vs. Enlightenment: Sentiment Analysis
Code & Cogito — Digital Rebirth of the Renaissance #09
"""

import numpy as np
from collections import Counter

# ============================================================
# PART 1: Emotional vocabulary analysis
# Compare word choices between Enlightenment and Romantic texts
# ============================================================

# Representative passages (simplified for demonstration)
# Each list contains characteristic vocabulary from major works

enlightenment_vocab = {
    'reason': 45, 'nature': 30, 'law': 38, 'knowledge': 35,
    'truth': 28, 'principle': 25, 'order': 22, 'liberty': 20,
    'science': 18, 'progress': 17, 'rational': 16, 'method': 15,
    'universal': 14, 'society': 13, 'rights': 12, 'virtue': 11,
    'duty': 10, 'understanding': 22, 'judgment': 9, 'clarity': 8,
    'evidence': 12, 'logic': 11, 'system': 14, 'moral': 10
}

romantic_vocab = {
    'heart': 42, 'soul': 38, 'beauty': 35, 'love': 50,
    'nature': 48, 'dream': 30, 'passion': 28, 'solitude': 22,
    'spirit': 25, 'wild': 20, 'sublime': 18, 'sorrow': 24,
    'eternal': 16, 'imagination': 22, 'wonder': 19, 'darkness': 17,
    'storm': 15, 'yearning': 14, 'melancholy': 13, 'mystery': 16,
    'infinite': 18, 'freedom': 20, 'wanderer': 11, 'ruin': 12
}

# ============================================================
# PART 2: Emotional dimensions scoring
# Rate works across five Romantic dimensions
# ============================================================

# Score each work on five dimensions (0-10 scale)
# [Emotion, Nature, Individualism, Sublime, Nostalgia]

works = {
    # Enlightenment works
    "Locke: Essay Concerning\nHuman Understanding": [2, 3, 3, 1, 1],
    "Voltaire:\nCandide":                           [4, 2, 5, 2, 2],
    "Kant: Critique of\nPure Reason":               [1, 2, 3, 3, 1],
    "Hume: Treatise of\nHuman Nature":               [3, 2, 4, 1, 1],
    # Romantic works
    "Wordsworth:\nLyrical Ballads":                  [9, 10, 7, 7, 6],
    "Shelley:\nFrankenstein":                        [8, 5, 9, 9, 4],
    "Beethoven:\nSymphony No. 9":                    [10, 6, 9, 10, 5],
    "Friedrich:\nWanderer":                          [7, 10, 10, 10, 8],
    "Turner:\nThe Slave Ship":                       [9, 9, 6, 10, 3],
    "Byron:\nChilde Harold":                         [9, 8, 10, 8, 9],
    "Hugo:\nLes Miserables":                         [10, 4, 8, 7, 6],
    "Goethe:\nThe Sorrows of Werther":               [10, 7, 9, 6, 5],
}

dimensions = ['Emotion', 'Nature', 'Individualism', 'Sublime', 'Nostalgia']

# ============================================================
# Visualization 1: Vocabulary comparison (bar chart)
# ============================================================

# Top 12 words from each era
enl_top = sorted(enlightenment_vocab.items(), key=lambda x: x[1], reverse=True)[:12]
rom_top = sorted(romantic_vocab.items(), key=lambda x: x[1], reverse=True)[:12]

words_e, counts_e = zip(*enl_top)
words_r, counts_r = zip(*rom_top)

y_pos = np.arange(len(words_e))

axes[0].barh(y_pos, counts_e, color='#2E86AB', alpha=0.85, height=0.6)
axes[0].set_yticks(y_pos)
axes[0].set_yticklabels(words_e, fontsize=11)
axes[0].invert_yaxis()
axes[0].set_xlabel('Relative Frequency', fontsize=12)
axes[0].set_title('Enlightenment: Top Vocabulary', fontsize=14, fontweight='bold')

axes[1].barh(y_pos, counts_r, color='#C41E3A', alpha=0.85, height=0.6)
axes[1].set_yticks(y_pos)
axes[1].set_yticklabels(words_r, fontsize=11)
axes[1].invert_yaxis()
axes[1].set_xlabel('Relative Frequency', fontsize=12)
axes[1].set_title('Romanticism: Top Vocabulary', fontsize=14, fontweight='bold')

# ============================================================
# Visualization 2: Radar chart — Romantic dimensions
# ============================================================

def radar_chart(ax, values, label, color, alpha=0.25):
    """Draw a single radar polygon on the given axes."""
    N = len(dimensions)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values_plot = values + [values[0]]
    angles += angles[:1]
    ax.plot(angles, values_plot, 'o-', color=color, linewidth=2, label=label)
    ax.fill(angles, values_plot, color=color, alpha=alpha)

# Average scores for each era
enl_works = [v for k, v in works.items() if any(
    name in k for name in ['Locke', 'Voltaire', 'Kant', 'Hume'])]
rom_works = [v for k, v in works.items() if any(
    name in k for name in ['Wordsworth', 'Shelley', 'Beethoven', 'Friedrich',
                           'Turner', 'Byron', 'Hugo', 'Goethe'])]

enl_avg = np.mean(enl_works, axis=0).tolist()
rom_avg = np.mean(rom_works, axis=0).tolist()

N = len(dimensions)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

radar_chart(ax, enl_avg, 'Enlightenment (avg)', '#2E86AB', 0.15)
radar_chart(ax, rom_avg, 'Romanticism (avg)', '#C41E3A', 0.2)

# Overlay individual Romantic works for texture
for name, scores in works.items():
    if any(r in name for r in ['Beethoven', 'Friedrich', 'Shelley']):
        short = name.split('\n')[-1]
        radar_chart(ax, scores, short, '#E8A838', 0.05)

# ============================================================
# Print summary statistics
# ============================================================

print("=" * 60)
print("ROMANTICISM vs. ENLIGHTENMENT: DIMENSIONAL ANALYSIS")
print("=" * 60)

for i, dim in enumerate(dimensions):
    e_val = enl_avg[i]
    r_val = rom_avg[i]
    diff = r_val - e_val
    print(f"\n{dim}:")
    print(f"  Enlightenment avg: {e_val:.1f}/10")
    print(f"  Romanticism avg:   {r_val:.1f}/10")
    print(f"  Difference:        {'+' if diff > 0 else ''}{diff:.1f}")

print("\n" + "=" * 60)
print("The data confirms what the poets already knew:")
print("Romanticism amplified every emotional dimension")
print("that the Enlightenment had muted.")
print("=" * 60)
