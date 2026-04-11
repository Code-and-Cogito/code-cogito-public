"""
Article 12: Ultimate Legacy - What We Inherited After 500 Years
Free Highlights: Cross-Article Network & Legacy Impact Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito
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

# Influence matrix: how much each article's theme influences the next
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
ax.set_title('Cross-Article Influence Matrix: 500 Years of Ideas', fontsize=14)
ax.set_xlabel('Influenced By →', fontsize=11)
ax.set_ylabel('← Influences', fontsize=11)
plt.colorbar(im, label='Influence Strength (0-10)')
plt.tight_layout()
plt.savefig('influence_matrix.png', dpi=150)
plt.show()

# --- 2. Legacy Pillars ---

pillars = ['Scientific\nMethod', 'Individual\nRights', 'Democratic\nGovernance', 'Free\nMarkets', 'Secular\nEthics']
renaissance_contribution = [85, 70, 60, 55, 65]
modern_relevance = [95, 90, 85, 80, 75]

x = np.arange(len(pillars))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, renaissance_contribution, width,
       label='Renaissance Contribution', color='#D4AF37', edgecolor='black')
ax.bar(x + width/2, modern_relevance, width,
       label='Modern Relevance', color='#1565C0', edgecolor='black')

ax.set_ylabel('Score (0-100)', fontsize=12)
ax.set_title('The Five Pillars of Renaissance Legacy', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(pillars, fontsize=10)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('legacy_pillars.png', dpi=150)
plt.show()

# --- 3. The 500-Year Arc ---

centuries = ['14th', '15th', '16th', '17th', '18th', '19th']
innovation = [20, 65, 80, 70, 85, 95]
freedom = [10, 25, 30, 35, 60, 75]
knowledge = [15, 40, 55, 65, 80, 95]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(centuries, innovation, 'o-', linewidth=2.5, label='Innovation', color='#FF9800', markersize=8)
ax.plot(centuries, freedom, 's-', linewidth=2.5, label='Individual Freedom', color='#1565C0', markersize=8)
ax.plot(centuries, knowledge, '^-', linewidth=2.5, label='Knowledge Access', color='#4CAF50', markersize=8)

ax.set_xlabel('Century', fontsize=12)
ax.set_ylabel('Score (0-100)', fontsize=12)
ax.set_title('The 500-Year Arc: How Renaissance Ideas Grew', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('500_year_arc.png', dpi=150)
plt.show()

print("\n=== Legacy Analysis Summary ===")
total_influence = influence.sum(axis=1)
most_influential = np.argmax(total_influence)
print(f"Most influential article: {articles[most_influential].replace(chr(10), ' ')} (score: {total_influence[most_influential]})")
print(f"Strongest single link: Humanism -> Enlightenment (9/10)")
print(f"Innovation growth 14th->19th century: {innovation[0]} -> {innovation[-1]}")
print("Full analysis: premium includes complete network graph,")
print("causal chain simulation, and modern AI/climate parallel analysis.")
