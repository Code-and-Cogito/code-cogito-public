"""
Article 08: The Enlightenment - The Age of Reason
Free Highlights: Philosopher Network & Ideas Influence Map
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Enlightenment Thinker Influence Network ---

thinkers = {
    'Locke': {'year': 1689, 'influence': 95, 'domain': 'Politics'},
    'Newton': {'year': 1687, 'influence': 98, 'domain': 'Science'},
    'Voltaire': {'year': 1734, 'influence': 90, 'domain': 'Philosophy'},
    'Montesquieu': {'year': 1748, 'influence': 88, 'domain': 'Politics'},
    'Rousseau': {'year': 1762, 'influence': 92, 'domain': 'Philosophy'},
    'Hume': {'year': 1739, 'influence': 85, 'domain': 'Philosophy'},
    'Kant': {'year': 1781, 'influence': 96, 'domain': 'Philosophy'},
    'Smith': {'year': 1776, 'influence': 93, 'domain': 'Economics'},
}

domain_colors = {'Politics': '#D32F2F', 'Science': '#1565C0',
                 'Philosophy': '#FF9800', 'Economics': '#4CAF50'}

fig, ax = plt.subplots(figsize=(12, 6))
for name, data in thinkers.items():
    color = domain_colors[data['domain']]
    ax.scatter(data['year'], data['influence'], s=data['influence']*5,
              c=color, alpha=0.7, edgecolors='black', linewidth=1.5)
    ax.annotate(name, (data['year'], data['influence']),
                textcoords="offset points", xytext=(0, 12),
                ha='center', fontsize=10, fontweight='bold')

for domain, color in domain_colors.items():
    ax.scatter([], [], c=color, s=100, label=domain)

ax.set_xlabel('Year of Key Work', fontsize=12)
ax.set_ylabel('Influence Score', fontsize=12)
ax.set_title('Enlightenment Thinkers: Influence by Domain', fontsize=14)
ax.legend(title='Domain')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('enlightenment_thinkers.png', dpi=150)
plt.show()

# --- 2. Reason vs Tradition: The Shift ---

decades = ['1680s', '1700s', '1720s', '1740s', '1760s', '1780s']
reason_score = [30, 45, 60, 72, 82, 90]
tradition_score = [90, 80, 65, 50, 35, 25]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(decades, reason_score, 'o-', linewidth=2.5, color='#1565C0',
        label='Reason & Empiricism', markersize=8)
ax.plot(decades, tradition_score, 's-', linewidth=2.5, color='#8B0000',
        label='Tradition & Authority', markersize=8)
ax.fill_between(range(len(decades)), reason_score, tradition_score,
                alpha=0.1, color='gray')

ax.axvline(x=2, color='gray', linestyle='--', alpha=0.5)
ax.annotate('Tipping Point\n(~1720s)', (2, 62), fontsize=10, ha='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Intellectual Dominance (%)', fontsize=12)
ax.set_title('The Great Shift: Reason Overtakes Tradition', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reason_vs_tradition.png', dpi=150)
plt.show()

# --- 3. Enlightenment Ideas -> Revolutions ---

ideas_impact = {
    'Natural Rights\n(Locke)': [90, 95, 70],
    'Separation of\nPowers (Montesquieu)': [85, 60, 80],
    'Social Contract\n(Rousseau)': [70, 90, 85],
    'Free Markets\n(Smith)': [80, 40, 90],
}

labels = list(ideas_impact.keys())
american = [v[0] for v in ideas_impact.values()]
french = [v[1] for v in ideas_impact.values()]
industrial = [v[2] for v in ideas_impact.values()]

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, american, width, label='American Rev. (1776)', color='#1565C0')
ax.bar(x, french, width, label='French Rev. (1789)', color='#D32F2F')
ax.bar(x + width, industrial, width, label='Industrial Rev.', color='#4CAF50')

ax.set_ylabel('Influence Score', fontsize=12)
ax.set_title('Enlightenment Ideas → Revolutionary Impact', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('ideas_to_revolutions.png', dpi=150)
plt.show()

print("\n=== Enlightenment Analysis Summary ===")
print(f"Most influential thinker: Newton (score: {thinkers['Newton']['influence']})")
print(f"Span of movement: {1781-1687} years")
print(f"Key idea for American Rev: Natural Rights (Locke, score=90)")
print("Full analysis: premium includes citation network analysis,")
print("Terror phase modeling, and Sapere Aude diffusion simulation.")
