"""
Article 05: Humanism - From God-Centered to Human-Centered
Free Highlights: Intellectual Network & Text Frequency Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Humanist Network: Key Thinkers ---

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

ax.set_xlabel('Year Active', fontsize=12)
ax.set_ylabel('Influence Score', fontsize=12)
ax.set_title('Renaissance Humanist Network: Influence Over Time', fontsize=14)
ax.grid(True, alpha=0.3)
plt.colorbar(scatter, label='Influence')
plt.tight_layout()
plt.savefig('humanist_network.png', dpi=150)
plt.show()

# --- 2. Paradigm Shift: God-Centered vs Human-Centered ---

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
ax.set_title('Paradigm Shift: God-Centered → Human-Centered', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('paradigm_shift_radar.png', dpi=150)
plt.show()

# --- 3. Key Text Discovery Timeline ---

discoveries = [
    (1345, 'Cicero\'s Letters', 'Petrarch'),
    (1416, 'Quintilian', 'Poggio'),
    (1417, 'Lucretius', 'Poggio'),
    (1453, 'Greek MSS to West', 'Fall of Constantinople'),
    (1462, 'Plato Complete', 'Ficino/Cosimo'),
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
ax.set_title('Key Text Discoveries That Fueled Humanism', fontsize=14)
plt.tight_layout()
plt.savefig('text_discovery_timeline.png', dpi=150)
plt.show()

print("\n=== Humanism Analysis Summary ===")
print(f"Most connected thinker: Erasmus ({thinkers['Erasmus']['connections']} connections)")
print(f"Most influential: Petrarch (score: {thinkers['Petrarch']['influence']})")
print(f"Key turning point: 1453 (Fall of Constantinople)")
print("Full analysis: premium includes complete network graph,")
print("text frequency NLP analysis, and influence propagation model.")
