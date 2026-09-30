"""
Article 05: Humanism - From God-Centered to Human-Centered
Free Highlights: three illustrative charts (influence scatter, paradigm radar,
text-discovery timeline)
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTE
- Sections 1 and 2 use hand-set, author-assigned ILLUSTRATIVE numbers (influence
  scores, connection counts, God-centeredness scores). They are not measurements.
- No network metric (betweenness centrality etc.) is computed in this script.
  The NetworkX snippet discussed in the article appears in the article only.
- Section 3 uses dates typed in by hand from standard accounts, as labels only.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Humanist Network: Key Thinkers (ILLUSTRATIVE INPUTS) ---
# 'era'         = rough "year active" marker chosen by the author. It is neither a
#                 birth year nor an exact event date (the article's chain diagram uses
#                 slightly different illustrative dates, e.g. Boccaccio 1360,
#                 Ficino 1470, Erasmus 1510).
# 'influence'   = subjective 0-100 score assigned by the author, not computed from data.
# 'connections' = hand-set number of links to other thinkers, not derived from a graph.

thinkers = {
    'Petrarch': {'era': 1340, 'influence': 95, 'connections': 6},
    'Boccaccio': {'era': 1350, 'influence': 70, 'connections': 4},
    'Ficino': {'era': 1462, 'influence': 90, 'connections': 8},
    'Pico': {'era': 1486, 'influence': 85, 'connections': 7},
    'Erasmus': {'era': 1500, 'influence': 92, 'connections': 9},
    'More': {'era': 1516, 'influence': 78, 'connections': 5},
}

fig, ax = plt.subplots(figsize=(10, 6))
names = list(thinkers.keys())
eras = [t['era'] for t in thinkers.values()]
influence = [t['influence'] for t in thinkers.values()]
connections = [t['connections'] * 50 for t in thinkers.values()]

scatter = ax.scatter(eras, influence, s=connections, c=influence,
                     cmap='YlOrRd', alpha=0.7, edgecolors='black')
for i, name in enumerate(names):
    ax.annotate(name, (eras[i], influence[i]), textcoords="offset points",
                xytext=(0, 12), ha='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Year Active (approximate marker)', fontsize=12)
ax.set_ylabel('Influence Score (illustrative, 0-100)', fontsize=12)
ax.set_title('Renaissance Humanists: Influence Over Time\n'
             '(illustrative author-assigned scores, not measured data)', fontsize=14)
ax.text(0.01, 0.01, 'Bubble size = hand-set number of connections',
        transform=ax.transAxes, fontsize=9, color='gray', va='bottom')
ax.set_xlim(1320, 1530)
ax.set_ylim(64, 100)
ax.grid(True, alpha=0.3)
plt.colorbar(scatter, label='Influence (illustrative)')
plt.tight_layout()
plt.savefig('humanist_network.png', dpi=150)
plt.show()

# --- 2. Paradigm Shift: God-Centered vs Human-Centered (ILLUSTRATIVE SCORES) ---
# Both profiles are 0-100 "God-centeredness" scores assigned by the author to draw the
# traditional God-centered -> human-centered narrative. They are not measured from
# texts; the article presents that narrative as the traditional account and the
# author's reading, not as a finding of this analysis.

categories = ['Source of\nTruth', 'Purpose\nof Life', 'Education\nGoal', 'Art\nSubject', 'Authority']
medieval = [95, 90, 85, 92, 95]    # God-centered scores
humanist = [30, 25, 20, 15, 35]    # God-centered scores (lower = more human-centered)

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]
medieval += medieval[:1]
humanist += humanist[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, medieval, 'o-', linewidth=2, label='Medieval (God-centered)', color='#8B0000')
ax.fill(angles, medieval, alpha=0.15, color='#8B0000')
ax.plot(angles, humanist, 'o-', linewidth=2, label='Humanist (Human-centered)', color='#1565C0')
ax.fill(angles, humanist, alpha=0.15, color='#1565C0')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_ylim(0, 100)
ax.set_title('Paradigm Shift: God-Centered → Human-Centered\n'
             '(illustrative; higher = more God-centered)', fontsize=13, pad=25)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.tight_layout()
plt.savefig('paradigm_shift_radar.png', dpi=150)
plt.show()

# --- 3. Key Text Discoveries and Events Timeline ---
# Dates are typed in by hand from standard accounts and used only to place labels.
# - 1345: Petrarch found Cicero's letters (to Atticus etc.) in the Chapter Library
#   (Biblioteca Capitolare) of Verona, not in Avignon.
# - 1453: Greek scholars and manuscripts were already reaching Italy well before the
#   fall of Constantinople (Chrysoloras taught Greek in Florence from 1397; Aurispa
#   brought 238 Greek manuscripts to Venice in 1423), so 1453 is a marker, not a start.
# - 1462: Cosimo de' Medici began supporting Ficino around this year (Careggi property
#   formally given in 1463; Corpus Hermeticum first, 1463). Ficino's Latin Plato was
#   finished in draft c.1468-69 and printed in 1484, so 1462 is NOT the year it was completed.

discoveries = [
    (1345, 'Cicero\'s Letters', 'Petrarch, Verona'),
    (1416, 'Quintilian', 'Poggio'),
    (1417, 'Lucretius', 'Poggio'),
    (1453, 'Fall of Constantinople', 'Greek scholars head west'),
    (1462, 'Cosimo backs Ficino', 'Latin Plato: c.1468-69'),
    (1486, '900 Theses', 'Pico'),
]

fig, ax = plt.subplots(figsize=(12, 4))
years = [d[0] for d in discoveries]
ax.scatter(years, [1]*len(years), s=200, c='#D4AF37', edgecolors='black', zorder=5)
for i, (year, text, person) in enumerate(discoveries):
    offset = 0.3 if i % 2 == 0 else -0.3
    ax.annotate(f'{year}\n{text}\n({person})', (year, 1),
                textcoords="offset points", xytext=(0, 40 if i % 2 == 0 else -50),
                ha='center', fontsize=8, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='gray'))

ax.axhline(y=1, color='gray', linewidth=2)
ax.set_xlim(1330, 1500)
ax.set_ylim(0, 2)
ax.set_yticks([])
ax.set_xlabel('Year', fontsize=12)
ax.set_title('Key Text Discoveries and Events That Fueled Humanism', fontsize=14)
plt.tight_layout()
plt.savefig('text_discovery_timeline.png', dpi=150)
plt.show()

# Summary values are read from the hand-set dictionary above (illustrative inputs).
most_connected = max(thinkers, key=lambda n: thinkers[n]['connections'])
most_influential = max(thinkers, key=lambda n: thinkers[n]['influence'])

print("\n=== Humanism Analysis Summary (illustrative inputs) ===")
print(f"Most connected thinker: {most_connected} "
      f"({thinkers[most_connected]['connections']} connections, hand-set)")
print(f"Highest influence score: {most_influential} "
      f"({thinkers[most_influential]['influence']}, author-assigned)")
print("No network metric is computed here; the NetworkX snippet is in the article.")
print("Timeline marker: 1453 (Fall of Constantinople); Greek learning was already")
print("reaching Italy earlier, e.g. Chrysoloras teaching in Florence from 1397.")
print("Deep Dive Pack adds NetworkX centrality analysis, a Monte Carlo network-")
print("resilience simulation, and a notebook + 20-thinker CSV.")
