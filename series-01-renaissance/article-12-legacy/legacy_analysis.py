"""
Article 12: Ultimate Legacy - What We Inherited After 500 Years
Free Highlights: Cross-Article Influence Matrix & Legacy Impact (illustrative)
Series: The Digital Rebirth of the Renaissance | Code & Cogito

NOTE ON THE DATA: every number in this script (the influence matrix, the
pillar scores and the century indexes) is a hand-set rating chosen by the
author to sketch a narrative. None of it is measured or taken from a dataset,
so treat the charts as an illustration of the argument, not as evidence.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. The Grand Narrative: 12 Articles Connected ---

articles = [
    'Florence\n(Network)', 'Medici\n(Finance)', 'Da Vinci\n(Anatomy)',
    'Perspective\n(Math)', 'Humanism\n(Philosophy)', 'Printing\n(Technology)',
    'Reformation\n(Authority)', 'Enlightenment\n(Reason)', 'Romanticism\n(Emotion)',
    'Industry\n(Progress)', 'Darwin\n(Evolution)', 'Legacy\n(Synthesis)'
]

# Influence matrix (ILLUSTRATIVE, hand-set 0-10 ratings by the author).
# Row i = the theme that influences, column j = the theme that is influenced:
# influence[i][j] is how strongly the author rates the influence of theme i on theme j.
# The diagonal is 0 (a theme does not influence itself); the ratings are subjective.
influence = np.array([
    [0, 8, 6, 5, 4, 3, 2, 2, 1, 1, 1, 5],  # Florence
    [5, 0, 9, 4, 7, 5, 3, 3, 2, 4, 1, 5],  # Medici
    [3, 2, 0, 9, 6, 4, 2, 5, 4, 3, 7, 5],  # Da Vinci
    [4, 1, 7, 0, 5, 3, 2, 6, 3, 4, 3, 5],  # Perspective
    [5, 4, 5, 4, 0, 6, 8, 9, 4, 3, 5, 7],  # Humanism
    [3, 3, 3, 2, 5, 0, 9, 7, 3, 5, 4, 6],  # Printing
    [2, 2, 1, 1, 7, 8, 0, 8, 5, 3, 3, 6],  # Reformation
    [2, 3, 3, 4, 8, 5, 6, 0, 9, 7, 6, 8],  # Enlightenment
    [1, 1, 4, 3, 4, 2, 3, 8, 0, 5, 4, 6],  # Romanticism
    [2, 4, 2, 3, 3, 6, 3, 7, 5, 0, 7, 7],  # Industry
    [1, 1, 6, 2, 5, 4, 4, 7, 4, 6, 0, 8],  # Darwin
    [5, 5, 5, 5, 7, 6, 6, 8, 6, 7, 8, 0],  # Legacy
])

fig, ax = plt.subplots(figsize=(12, 10))
im = ax.imshow(influence, cmap='YlOrRd', aspect='auto')
ax.set_xticks(range(12))
ax.set_yticks(range(12))
ax.set_xticklabels([a.split('\n')[0] for a in articles], rotation=45, ha='right', fontsize=9)
ax.set_yticklabels([a.split('\n')[0] for a in articles], fontsize=9)
ax.set_title('Cross-Article Influence Matrix: 500 Years of Ideas (illustrative ratings)', fontsize=14)
ax.set_xlabel('Influenced theme (column)', fontsize=11)
ax.set_ylabel('Influencing theme (row)', fontsize=11)
plt.colorbar(im, label='Influence Strength (0-10, hand-set)')
plt.tight_layout()
plt.savefig('influence_matrix.png', dpi=150)
plt.show()

# --- 2. Legacy Pillars ---

pillars = ['Scientific\nMethod', 'Individual\nRights', 'Democratic\nGovernance', 'Free\nMarkets', 'Secular\nEthics']
# ILLUSTRATIVE hand-set 0-100 scores (the author's judgement, not measured data)
renaissance_contribution = [85, 70, 60, 55, 65]
modern_relevance = [95, 90, 85, 80, 75]

x = np.arange(len(pillars))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, renaissance_contribution, width,
       label='Renaissance Contribution', color='#D4AF37', edgecolor='black')
ax.bar(x + width/2, modern_relevance, width,
       label='Modern Relevance', color='#1565C0', edgecolor='black')

ax.set_ylabel('Score (0-100, hand-set)', fontsize=12)
ax.set_title('The Five Pillars of Renaissance Legacy (illustrative scores)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(pillars, fontsize=10)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('legacy_pillars.png', dpi=150)
plt.show()

# --- 3. The 500-Year Arc ---

centuries = ['14th', '15th', '16th', '17th', '18th', '19th']
# ILLUSTRATIVE hand-set 0-100 indexes, not measured series
innovation = [20, 65, 80, 70, 85, 95]
freedom = [10, 25, 30, 35, 60, 75]
knowledge = [15, 40, 55, 65, 80, 95]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(centuries, innovation, 'o-', linewidth=2.5, label='Innovation', color='#FF9800', markersize=8)
ax.plot(centuries, freedom, 's-', linewidth=2.5, label='Individual Freedom', color='#1565C0', markersize=8)
ax.plot(centuries, knowledge, '^-', linewidth=2.5, label='Knowledge Access', color='#4CAF50', markersize=8)

ax.set_xlabel('Century', fontsize=12)
ax.set_ylabel('Index (0-100, hand-set)', fontsize=12)
ax.set_title('The 500-Year Arc: How Renaissance Ideas Grew (illustrative index)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('500_year_arc.png', dpi=150)
plt.show()

# --- 4. Summary (computed from the hand-set ratings above) ---

def label(i):
    return articles[i].replace(chr(10), ' ')

print("\n=== Legacy Analysis Summary ===")
print("All scores are hand-set by the author (illustrative ratings, not measured data).")

# Total outgoing influence = sum of a row (the theme's ratings toward the other 11)
total_influence = influence.sum(axis=1)
most_influential = int(np.argmax(total_influence))
print(f"Highest total outgoing influence rating: {label(most_influential)} "
      f"(score: {int(total_influence[most_influential])} of a possible {10 * (len(articles) - 1)})")
# The synthesis article is rated to touch every theme, so also show the runner-up
ranked = [int(i) for i in np.argsort(-total_influence, kind='stable')]
runner_up = next(i for i in ranked if i != most_influential)
print(f"  Next highest: {label(runner_up)} (score: {int(total_influence[runner_up])})")

# Strongest single link(s): several cells can share the top rating
top = int(influence.max())
top_links = [(int(i), int(j)) for i, j in np.argwhere(influence == top)]
print(f"Highest single link rating: {top}/10, shared by {len(top_links)} links:")
for i, j in top_links:
    print(f"  {label(i)} -> {label(j)}")

print(f"Innovation index (illustrative) 14th->19th century: {innovation[0]} -> {innovation[-1]}")
for k in range(1, len(innovation)):
    if innovation[k] < innovation[k - 1]:
        print(f"  (not a straight climb: {innovation[k - 1]} -> {innovation[k]} in the {centuries[k]} century)")

print("Full analysis: the Deep Dive Pack adds an influence network graph, PageRank and")
print("betweenness centrality, theme clustering, a give-vs-receive influence flow and a")
print("map from each theme to a present-day parallel.")
