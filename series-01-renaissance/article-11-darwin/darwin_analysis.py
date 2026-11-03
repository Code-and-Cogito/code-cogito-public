"""
Article 11: Darwin - Evolution's Philosophical Shock
Free Highlights: Natural Selection Simulation, Impact Radar & Timeline
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTES (what is real, what is illustrative)
- Natural selection simulation: a toy model, the same deer-herd model as the
  code block in the article (seed 42, 200 deer, the faster half survives,
  offspring = parent + N(0, 3) mutation). The numbers it prints are outputs of
  this model, not measurements of real deer. The trait has no upper limit, so
  the mean keeps rising; a real trait would hit physical limits and trade-offs.
- Impact radar: ILLUSTRATIVE. The 0-100 scores are hand-set by the author to
  demonstrate the chart. They are not measured data.
- Timeline: historical event years (Beagle voyage 1831 ... Descent of Man 1871).
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Natural Selection Simulation (same model as the article's code block) ---
# Each generation the faster half of the herd survives (top 50%), and every
# offspring inherits its parent's speed plus a small random mutation.
# There is no upper limit on speed in this toy model, so the mean keeps rising
# for all 50 generations. Real traits are capped by physiology and trade-offs.

np.random.seed(42)
generations = 50
pop_size = 200
mean_speeds = []
std_speeds = []

# Initial population: normal distribution, mean=50, std=10
population = np.random.normal(50, 10, pop_size)
first_population = population.copy()

for gen in range(generations):
    # Speed is recorded at the start of each generation, so the last recorded
    # value is generation 49 (50 recorded generations), as in the article.
    mean_speeds.append(np.mean(population))
    std_speeds.append(np.std(population))
    last_population = population

    # Selection: faster deer survive (top 50%)
    survivors = population[population >= np.median(population)]

    # Reproduction with variation
    offspring = []
    for _ in range(pop_size):
        parent = np.random.choice(survivors)
        child = parent + np.random.normal(0, 3)  # mutation
        offspring.append(child)
    population = np.array(offspring)

last_gen = len(mean_speeds) - 1
mean_arr = np.array(mean_speeds)
std_arr = np.array(std_speeds)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(range(len(mean_arr)), mean_arr, linewidth=2, color='#2E7D32', label='Mean speed')
ax1.fill_between(range(len(mean_arr)), mean_arr - std_arr, mean_arr + std_arr,
                 color='#2E7D32', alpha=0.15, label='\u00b11 std')
ax1.set_xlabel('Generation', fontsize=12)
ax1.set_ylabel('Average Speed', fontsize=12)
ax1.set_title('Natural Selection (toy model): Mean Speed Over Generations', fontsize=13)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left')

# Show the herd at the start vs at the last recorded generation
ax2.hist(first_population, bins=20, alpha=0.5, color='#1565C0', label='Generation 0')
ax2.hist(last_population, bins=20, alpha=0.5, color='#D32F2F', label=f'Generation {last_gen}')
ax2.set_xlabel('Speed', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)
ax2.set_title('Herd Speed Distribution: Start vs Last Recorded Generation', fontsize=13)
ax2.legend()

plt.tight_layout()
plt.savefig('natural_selection_sim.png', dpi=150)
plt.show()

# --- 2. Philosophical Impact of Evolution (ILLUSTRATIVE scores) ---

domains = ['Theology', 'Philosophy', 'Science', 'Society', 'Ethics']
# ILLUSTRATIVE: 0-100 scores hand-set by the author to demonstrate the radar
# chart. They are judgements, not measured data.
before_darwin = [95, 70, 50, 80, 85]  # illustrative score before Darwin
after_darwin = [40, 45, 95, 55, 50]   # illustrative score after Darwin

# Computed from the illustrative scores above (not a measured result)
theo = domains.index('Theology')
theology_before, theology_after = before_darwin[theo], after_darwin[theo]
theology_change = (theology_after / theology_before - 1) * 100

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
ax.set_title("Human 'Specialness' Before & After Darwin\n"
             "(illustrative scores set by the author, not measured data)",
             fontsize=13, pad=25)
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
print(f"Years from the start of the Beagle voyage ({evidence[0][0]}) "
      f"to the Origin ({evidence[4][0]}): {evidence[4][0] - evidence[0][0]}")
print(f"Deer-herd model (same as the article): mean speed "
      f"{mean_speeds[0]:.1f} -> {mean_speeds[-1]:.1f} "
      f"(+{(mean_speeds[-1] / mean_speeds[0] - 1) * 100:.0f}%) "
      f"from generation 0 to generation {last_gen}")
print("  (toy model: speed has no upper limit here, real traits do)")
print(f"Illustrative Theology score (set by the author, not measured data): "
      f"{theology_before} -> {theology_after} ({theology_change:.0f}%)")
print("Full analysis: the Deep Dive Pack adds a 100-generation beak-depth simulation")
print("for 14 Darwin's finch species, a finch family tree (UPGMA dendrogram),")
print("a step-by-step Jupyter Notebook and a CSV of finch measurements.")
