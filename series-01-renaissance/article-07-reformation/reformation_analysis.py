"""
Article 07: The Reformation - When Authority Crumbles
Free Highlights: Reformation Timeline, Authority Radar & Religious-War Death Toll
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTES (what is real, what is illustrative)
- Timeline: historical event dates (95 Theses 1517 ... Peace of Westphalia 1648).
- Authority radar: ILLUSTRATIVE. The 0-100 scores are hand-set by the author to
  demonstrate the chart. They are not measured data.
- War deaths: rough estimates from the secondary literature. Sources differ
  widely, so the Thirty Years' War is drawn as a range (see section 3).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

# --- 1. Reformation Timeline ---

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

# --- 2. Authority Structure: Before vs After (ILLUSTRATIVE scores) ---
# NOTE: the 0-100 scores below are hand-set by the author to demonstrate the
# radar chart. They are illustrative judgements, not measured historical data.

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
ax.set_title('Authority Before & After Reformation\n(illustrative scores set by the author, not measured data)',
             fontsize=13, pad=25)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('authority_radar.png', dpi=150)
plt.show()

# --- 3. Religious Wars: Death Toll ---
# Rough (low, high) estimates of total deaths. Sources differ widely and count
# different things (battle deaths only vs. also famine and disease), so read
# these as orders of magnitude, not exact figures.
#   German Peasants' War (1524-25): ~100,000 peasants killed (the figure used in
#       the article; roughly 300,000 people took part in the uprising).
#   French Wars of Religion (1562-98): ~3 million is a rough round figure only;
#       estimates vary widely.
#   Thirty Years' War (1618-48): 4.5-8 million soldiers and civilians, from
#       battle, famine and disease (Wikipedia, "Thirty Years' War"). The article
#       uses the same range; 8 million is the upper end, not a settled count.

wars = ['German Peasants\nWar (1524-25)', 'French Wars of\nReligion (1562-98)', 'Thirty Years\nWar (1618-48)']
deaths_low = [100000, 3000000, 4500000]
deaths_high = [100000, 3000000, 8000000]
colors = ['#FF9800', '#D32F2F', '#8B0000']


def fmt(n):
    """Compact number label: 100,000 or 3.0M."""
    return f'{n / 1e6:.1f}M' if n >= 1_000_000 else f'{n:,.0f}'


def range_label(low, high):
    return f'~{fmt(low)}' if low == high else f'{fmt(low)}-{fmt(high)}'


fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(wars, deaths_low, color=colors, edgecolor='black')
for i, (low, high) in enumerate(zip(deaths_low, deaths_high)):
    if high > low:  # hatched extension = uncertainty range up to the high estimate
        ax.barh(i, high - low, left=low, color=colors[i], alpha=0.35,
                hatch='//', edgecolor='black')
    ax.text(high + 100000, i, range_label(low, high),
            va='center', fontsize=11, fontweight='bold')

ax.set_xlim(0, max(deaths_high) * 1.3)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M'))
ax.set_xlabel('Estimated deaths (rough; sources differ widely)', fontsize=12)
ax.set_title('The Price of Religious Reform: Major Conflicts', fontsize=14)
ax.legend(handles=[Patch(facecolor='gray', edgecolor='black', label='Low estimate'),
                   Patch(facecolor='gray', alpha=0.35, hatch='//', edgecolor='black',
                         label='Range up to high estimate')],
          loc='lower right')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('religious_wars_deaths.png', dpi=150)
plt.show()

total_low, total_high = sum(deaths_low), sum(deaths_high)

print("\n=== Reformation Analysis Summary ===")
print(f"Timeline span: {1648-1517} years (1517-1648)")
print(f"Estimated deaths in the 3 conflicts shown: ~{total_low/1e6:.1f}-{total_high/1e6:.1f} million (rough; sources differ widely)")
print(f"Largest conflict: Thirty Years War ({deaths_low[-1]:,}-{deaths_high[-1]:,} dead)")
print("Note: the authority radar scores are illustrative (set by the author), not measured data.")
print("Full analysis: the Deep Dive Pack adds a 14-city spread network,")
print("pamphlet print analysis, territorial-share charts and war-death charts.")
