"""
Article 07: The Reformation - When Authority Crumbles
Free Highlights: Religious Authority Network & Conflict Timeline
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Protestant Spread Timeline ---

events = [
    (1517, "95 Theses\n(Luther)", 1),
    (1521, "Diet of Worms\n(Excommunication)", 2),
    (1534, "Act of Supremacy\n(Henry VIII)", 3),
    (1536, "Calvin in\nGeneva", 4),
    (1545, "Council of\nTrent", 5),
    (1555, "Peace of\nAugsburg", 6),
    (1618, "Thirty Years\nWar begins", 7),
    (1648, "Peace of\nWestphalia", 8),
]

fig, ax = plt.subplots(figsize=(14, 5))
years = [e[0] for e in events]
labels = [e[1] for e in events]
colors = ['#D32F2F', '#D32F2F', '#1565C0', '#FF9800', '#4CAF50', '#4CAF50', '#D32F2F', '#4CAF50']

ax.scatter(years, [1]*len(years), s=300, c=colors, edgecolors='black', zorder=5)
for i, (year, label, _) in enumerate(events):
    offset = 50 if i % 2 == 0 else -60
    ax.annotate(f'{year}\n{label}', (year, 1), textcoords="offset points",
                xytext=(0, offset), ha='center', fontsize=8,
                arrowprops=dict(arrowstyle='->', color='gray'))

ax.axhline(y=1, color='gray', linewidth=2)
ax.set_xlim(1510, 1660)
ax.set_ylim(0, 2)
ax.set_yticks([])
ax.set_title('The Reformation: From 95 Theses to Westphalia (1517-1648)', fontsize=14)
plt.tight_layout()
plt.savefig('reformation_timeline.png', dpi=150)
plt.show()

# --- 2. Authority Structure: Before vs After ---

categories = ['Religious\nAuthority', 'Political\nCentralization', 'Individual\nConscience', 'Bible\nAccess', 'Intellectual\nFreedom']
before = [95, 80, 10, 5, 15]
after = [40, 60, 75, 80, 65]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]
before += before[:1]
after += after[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, before, 'o-', linewidth=2, label='Pre-Reformation', color='#8B0000')
ax.fill(angles, before, alpha=0.15, color='#8B0000')
ax.plot(angles, after, 'o-', linewidth=2, label='Post-Reformation', color='#1565C0')
ax.fill(angles, after, alpha=0.15, color='#1565C0')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_ylim(0, 100)
ax.set_title('Authority Before & After Reformation', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('authority_radar.png', dpi=150)
plt.show()

# --- 3. Religious Wars: Death Toll ---

wars = ['German Peasants\nWar (1524-25)', 'French Wars of\nReligion (1562-98)', 'Thirty Years\nWar (1618-48)']
deaths = [100000, 3000000, 8000000]
colors = ['#FF9800', '#D32F2F', '#8B0000']

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(wars, deaths, color=colors, edgecolor='black')
for bar, d in zip(bars, deaths):
    ax.text(bar.get_width() + 100000, bar.get_y() + bar.get_height()/2,
            f'{d:,.0f}', va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Estimated Deaths', fontsize=12)
ax.set_title('The Price of Religious Reform: Major Conflicts', fontsize=14)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('religious_wars_deaths.png', dpi=150)
plt.show()

print("\n=== Reformation Analysis Summary ===")
print(f"Duration of upheaval: {1648-1517} years")
print(f"Estimated total deaths: ~{sum(deaths):,}")
print(f"Largest conflict: Thirty Years War ({deaths[-1]:,} dead)")
print("Full analysis: premium includes Protestant spread network,")
print("pamphlet distribution model, and religious demographics shift.")
