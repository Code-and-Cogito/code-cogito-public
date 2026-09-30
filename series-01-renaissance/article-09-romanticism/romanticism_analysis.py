"""
Article 09: Romanticism - The Emotional Rebellion
Free Highlights: Emotion vs Reason Analysis & Artistic Movement
Series: The Digital Rebirth of the Renaissance | Code & Cogito

What this script does: it draws three charts.
  1. Enlightenment vs Romanticism value scores (bar chart)
  2. A timeline of six landmark Romantic works (real, commonly cited dates)
  3. Theme scores for Romantic works (bar chart)

Data note: the numbers in sections 1 and 3 are ILLUSTRATIVE INPUTS set by the
author to make the contrast visible. They are not measured, counted or
surveyed data. Only the works and dates in section 2 are historical facts.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Romanticism vs Enlightenment Values ---

# ILLUSTRATIVE INPUTS: hand-set emphasis scores (0-100), not measured data.
values = ['Emotion', 'Nature', 'Individualism', 'Imagination', 'Tradition']
enlightenment = [20, 30, 40, 25, 35]
romanticism = [95, 90, 92, 95, 70]

x = np.arange(len(values))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, enlightenment, width, label='Enlightenment', color='#1565C0')
ax.bar(x + width/2, romanticism, width, label='Romanticism', color='#D32F2F')

ax.set_ylabel('Emphasis Score (0-100)', fontsize=12)
ax.set_title('Value Priorities: Enlightenment vs Romanticism', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(values, fontsize=11)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('enlightenment_vs_romanticism.png', dpi=150)
plt.show()

# --- 2. Key Romantic Works Timeline ---

# Historical data: (year, title, author, domain). Years are the commonly cited
# publication / completion / exhibition dates:
#   Werther published 1774, Lyrical Ballads published 1798 (Wordsworth and
#   Coleridge), Symphony No. 3 "Eroica" completed 1804 (premiered 1805),
#   Frankenstein published 1818 (Mary Shelley), Liberty Leading the People
#   painted 1830, The Slave Ship exhibited 1840.
works = [
    (1774, 'Sorrows of\nYoung Werther', 'Goethe', 'Literature'),
    (1798, 'Lyrical\nBallads', 'Wordsworth', 'Poetry'),
    (1804, 'Symphony\nNo.3', 'Beethoven', 'Music'),
    (1818, 'Frankenstein', 'Shelley', 'Literature'),
    (1830, 'Liberty Leading\nthe People', 'Delacroix', 'Painting'),
    (1840, 'The Slave\nShip', 'Turner', 'Painting'),
]

domain_colors = {'Literature': '#D32F2F', 'Poetry': '#FF9800',
                 'Music': '#4CAF50', 'Painting': '#1565C0'}

fig, ax = plt.subplots(figsize=(14, 5))
for year, title, author, domain in works:
    ax.scatter(year, 1, s=300, c=domain_colors[domain],
              edgecolors='black', zorder=5)

for i, (year, title, author, domain) in enumerate(works):
    offset = 50 if i % 2 == 0 else -55
    ax.annotate(f'{title}\n{author} ({year})', (year, 1),
                textcoords="offset points", xytext=(0, offset),
                ha='center', fontsize=8,
                arrowprops=dict(arrowstyle='->', color='gray'))

for domain, color in domain_colors.items():
    ax.scatter([], [], c=color, s=100, label=domain)

ax.axhline(y=1, color='gray', linewidth=2)
ax.set_xlim(1765, 1850)
ax.set_ylim(0, 2)
ax.set_yticks([])
ax.set_title('Key Romantic Works Across Art Forms', fontsize=14)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('romantic_works_timeline.png', dpi=150)
plt.show()

# --- 3. Dominant Romantic Themes ---

# ILLUSTRATIVE INPUTS: hand-set theme scores (percent), NOT counted from a
# corpus of works. The y-axis label below keeps the wording of the published
# figure; read the numbers as the author's illustrative scores.
themes = ['Nature\nSublime', 'Individual\nGenius', 'Medieval\nNostalgia', 'Exotic\nOrient', 'Revolution\n& Liberty']
frequency = [92, 85, 65, 58, 78]

fig, ax = plt.subplots(figsize=(10, 5))
colors = ['#2E7D32', '#D32F2F', '#8B4513', '#FF9800', '#1565C0']
bars = ax.bar(themes, frequency, color=colors, edgecolor='black')
for bar, f in zip(bars, frequency):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f'{f}%', ha='center', fontsize=11, fontweight='bold')

ax.set_ylabel('Theme Frequency in Major Works (%)', fontsize=12)
ax.set_title('Dominant Themes in Romantic Literature & Art', fontsize=14)
ax.set_ylim(0, 105)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('romantic_themes.png', dpi=150)
plt.show()

# --- Summary: values are computed from the lists defined above ---

top = int(np.argmax(frequency))
top_theme = themes[top].replace('\n', ' ')
years = [w[0] for w in works]

print("\n=== Romanticism Analysis Summary ===")
print(f"Highest-scoring theme (illustrative input): {top_theme} ({frequency[top]}%)")
print(f"Span of the {len(works)} featured works: {max(years) - min(years)} years ({min(years)}-{max(years)})")
print(f"Art-form categories shown: {len(domain_colors)} ({', '.join(domain_colors)})")
print("Note: value scores (section 1) and theme scores (section 3) are illustrative inputs, not measured data.")
print("Deep Dive Pack: 15-work dataset (1774-1862) scored on five dimensions, plus a cross-art-form heatmap.")
