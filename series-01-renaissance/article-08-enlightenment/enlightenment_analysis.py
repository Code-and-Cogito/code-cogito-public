"""
Article 08: The Enlightenment - The Age of Reason
Free Highlights: Landmark Works Scatter, Reason vs Tradition & Ideas-to-Revolutions Chart
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTES (what is real, what is illustrative)
- Years of key works: historical publication years of each thinker's landmark work
  (Newton: Principia 1687; Locke: Two Treatises of Government 1689; Voltaire: Lettres
  philosophiques 1734; Hume: Treatise of Human Nature 1739; Montesquieu: The Spirit of
  the Laws 1748; Rousseau: The Social Contract 1762; Smith: The Wealth of Nations 1776;
  Kant: Critique of Pure Reason 1781).
- Influence scores (section 1), the reason-vs-tradition curves (section 2) and the
  idea-to-revolution scores (section 3): ILLUSTRATIVE. They are hand-set by the author
  to demonstrate the charts. They are not measured data and not a scholarly ranking.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Enlightenment Thinker Influence Scores (illustrative) ---

# 'year' = publication year of the landmark work (see DATA NOTES above).
# 'influence' = ILLUSTRATIVE 0-100 score, hand-set by the author, not measured.
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
ax.set_ylabel('Influence Score (illustrative, hand-set)', fontsize=12)
ax.set_title('Enlightenment Thinkers: Influence by Domain (illustrative scores)', fontsize=14)
ax.legend(title='Domain')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('enlightenment_thinkers.png', dpi=150)
plt.show()

# --- 2. Reason vs Tradition: The Shift (illustrative) ---

# ILLUSTRATIVE curves: hand-set 0-100 index values to sketch the idea of a shift.
# They are not measured shares of anything (the two series do not sum to 100).
# The decades are every second decade, not a continuous series.
decades = ['1680s', '1700s', '1720s', '1740s', '1760s', '1780s']
reason_score = [30, 45, 60, 72, 82, 90]
tradition_score = [90, 80, 65, 50, 35, 25]

# Where do the two hand-set curves cross? (linear interpolation between samples)
gap = np.array(reason_score) - np.array(tradition_score)
first_lead = int(np.argmax(gap > 0))       # first sample where reason leads
x_cross = (first_lead - 1) + (-gap[first_lead - 1]) / (gap[first_lead] - gap[first_lead - 1])
y_cross = (reason_score[first_lead - 1]
           + (x_cross - (first_lead - 1)) * (reason_score[first_lead] - reason_score[first_lead - 1]))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(decades, reason_score, 'o-', linewidth=2.5, color='#1565C0',
        label='Reason & Empiricism', markersize=8)
ax.plot(decades, tradition_score, 's-', linewidth=2.5, color='#8B0000',
        label='Tradition & Authority', markersize=8)
ax.fill_between(range(len(decades)), reason_score, tradition_score,
                alpha=0.1, color='gray')

ax.axvline(x=x_cross, color='gray', linestyle='--', alpha=0.5)
ax.annotate('Crossover in this illustrative\nseries (between the\n1720s and 1740s samples)',
            (x_cross, y_cross), xytext=(x_cross, 48), fontsize=10, ha='center', va='top',
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.6))
ax.set_xlabel('Decade (every second decade shown)', fontsize=12)
ax.set_ylabel('Illustrative dominance index (0-100)', fontsize=12)
ax.set_title('The Great Shift: Reason Overtakes Tradition (illustrative)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reason_vs_tradition.png', dpi=150)
plt.show()

# --- 3. Enlightenment Ideas -> Revolutions (illustrative) ---

# ILLUSTRATIVE 0-100 scores, hand-set by the author: [American, French, Industrial].
# They express a rough judgement, not measured data.
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

ax.set_ylabel('Influence Score (illustrative, hand-set)', fontsize=12)
ax.set_title('Enlightenment Ideas → Revolutionary Impact (illustrative scores)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('ideas_to_revolutions.png', dpi=150)
plt.show()

# --- Summary: every printed number is computed from the data above ---

top_name = max(thinkers, key=lambda n: thinkers[n]['influence'])
first_year = min(t['year'] for t in thinkers.values())
last_year = max(t['year'] for t in thinkers.values())
top_idea = max(ideas_impact, key=lambda k: ideas_impact[k][0]).replace('\n', ' ')
top_idea_score = max(american)

print("\n=== Enlightenment Analysis Summary ===")
print(f"Highest illustrative influence score: {top_name}, score {thinkers[top_name]['influence']}")
print(f"Span of key works in this sample: {last_year - first_year} years ({first_year}-{last_year})")
print(f"Highest illustrative score for the American Rev: {top_idea}, score {top_idea_score}")
print("Note: all scores in this script are illustrative (set by the author), not measured data.")
print("Full analysis: the Deep Dive Pack adds a 20-node influence network scored with")
print("PageRank, betweenness and eigenvector centrality, a 3D philosophical spectrum,")
print("revolution-impact correlations and a static idea-diffusion model.")
