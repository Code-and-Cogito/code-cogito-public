"""
Article 11: Darwin - Evolution's Philosophical Shock
Free Highlights: Natural Selection Simulation & Impact Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simple Natural Selection Simulation ---

np.random.seed(42)
generations = 50
pop_size = 100
trait_mean = [50.0]  # starting average trait value
trait_std = [15.0]
selection_pressure = 0.6  # top 60% survive

for gen in range(generations):
    population = np.random.normal(trait_mean[-1], trait_std[-1], pop_size)
    survivors = np.sort(population)[int(pop_size * (1 - selection_pressure)):]
    trait_mean.append(np.mean(survivors))
    trait_std.append(np.std(survivors) * 1.05)  # mutation adds variance

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(range(len(trait_mean)), trait_mean, linewidth=2, color='#2E7D32')
ax1.set_xlabel('Generation', fontsize=12)
ax1.set_ylabel('Average Trait Value', fontsize=12)
ax1.set_title('Natural Selection: Trait Shift Over Generations', fontsize=13)
ax1.grid(True, alpha=0.3)

# Show initial vs final distribution
pop_initial = np.random.normal(50, 15, 1000)
pop_final = np.random.normal(trait_mean[-1], trait_std[-1], 1000)
ax2.hist(pop_initial, bins=30, alpha=0.5, color='#1565C0', label='Generation 0')
ax2.hist(pop_final, bins=30, alpha=0.5, color='#D32F2F', label=f'Generation {generations}')
ax2.set_xlabel('Trait Value', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)
ax2.set_title('Population Distribution Shift', fontsize=13)
ax2.legend()

plt.tight_layout()
plt.savefig('natural_selection_sim.png', dpi=150)
plt.show()

# --- 2. Philosophical Impact of Evolution ---

domains = ['Theology', 'Philosophy', 'Science', 'Society', 'Ethics']
before_darwin = [95, 70, 50, 80, 85]  # certainty in human specialness
after_darwin = [40, 45, 95, 55, 50]   # certainty after evolution

angles = np.linspace(0, 2 * np.pi, len(domains), endpoint=False).tolist()
angles += angles[:1]
before_darwin += before_darwin[:1]
after_darwin += after_darwin[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, before_darwin, 'o-', linewidth=2, label='Pre-Darwin', color='#8B0000')
ax.fill(angles, before_darwin, alpha=0.15, color='#8B0000')
ax.plot(angles, after_darwin, 'o-', linewidth=2, label='Post-Darwin', color='#1565C0')
ax.fill(angles, after_darwin, alpha=0.15, color='#1565C0')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=11)
ax.set_ylim(0, 100)
ax.set_title("Human 'Specialness' Before & After Darwin", fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('darwin_impact_radar.png', dpi=150)
plt.show()

# --- 3. Evidence Timeline ---

evidence = [
    (1831, 'Beagle Voyage\nbegins'),
    (1835, 'Galapagos\nFinches'),
    (1838, 'Malthus\ninsight'),
    (1858, 'Wallace\nletter'),
    (1859, 'Origin of\nSpecies'),
    (1871, 'Descent\nof Man'),
]

fig, ax = plt.subplots(figsize=(12, 4))
years = [e[0] for e in evidence]
ax.scatter(years, [1]*len(years), s=250, c='#D4AF37', edgecolors='black', zorder=5)

for i, (year, label) in enumerate(evidence):
    offset = 45 if i % 2 == 0 else -50
    ax.annotate(f'{year}\n{label}', (year, 1), textcoords="offset points",
                xytext=(0, offset), ha='center', fontsize=9,
                arrowprops=dict(arrowstyle='->', color='gray'))

ax.axhline(y=1, color='gray', linewidth=2)
ax.set_xlim(1825, 1878)
ax.set_ylim(0, 2)
ax.set_yticks([])
ax.set_title("Darwin's Journey: From Observation to Revolution", fontsize=14)
plt.tight_layout()
plt.savefig('darwin_timeline.png', dpi=150)
plt.show()

print("\n=== Darwin Analysis Summary ===")
print(f"Years from voyage to publication: {1859-1831}")
print(f"Trait shift after {generations} generations: {trait_mean[0]:.1f} -> {trait_mean[-1]:.1f}")
print(f"Theology certainty drop: {95} -> {40} (-58%)")
print("Full analysis: premium includes speciation simulation,")
print("phylogenetic tree builder, and Social Darwinism critique model.")
