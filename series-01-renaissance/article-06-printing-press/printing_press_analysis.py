"""
Article 06: The Printing Press - How Ideas Went Viral
Free Highlights: Print Spread Simulation & Cost Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTE (please read): every number in this script is a hand-set, rounded,
illustrative value chosen to show the SHAPE of the story. None of it is a
measured historical series.
  - City dates: approximate first-press years for 8 selected cities. They have
    not been verified city by city, and the article's decade overview is rounded.
  - Decade production: arbitrary "illustrative units", far smaller than real
    book counts. For real-world scale see the article, e.g. Buringh & van
    Zanden (2009), Journal of Economic History 69(2): nearly 5 million
    manuscripts in 15th-century Western Europe, and more than 12 million
    printed books between 1454 and 1500.
  - Cost index: hand-set (1400 = 100). The "98%" is simply 100 -> 2 by
    construction; it is not a measured price series.
The article's headline figures (about 30,000 books in 1450, a popular estimate,
and about 12 million by 1500) are quoted estimates, not outputs of this script.
Section 4 below only does arithmetic on them.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Printing Press Spread Across Europe ---

# Illustrative: approximate first-press years (not verified city by city)
cities = {
    'Mainz': (1450, 50.0, 8.3),
    'Strasbourg': (1458, 48.6, 7.8),
    'Rome': (1465, 41.9, 12.5),
    'Venice': (1469, 45.4, 12.3),
    'Paris': (1470, 48.9, 2.3),
    'Nuremberg': (1470, 49.5, 11.1),
    'Florence': (1471, 43.8, 11.3),
    'London': (1476, 51.5, -0.1),
}

fig, ax = plt.subplots(figsize=(10, 6))
years = [c[0] for c in cities.values()]
lats = [c[1] for c in cities.values()]
lons = [c[2] for c in cities.values()]
sizes = [(1480 - y) * 30 for y in years]  # earlier = bigger

scatter = ax.scatter(lons, lats, s=sizes, c=years, cmap='YlOrRd_r',
                     alpha=0.7, edgecolors='black', linewidth=1.5)
for name, (year, lat, lon) in cities.items():
    ax.annotate(f'{name}\n({year})', (lon, lat), textcoords="offset points",
                xytext=(10, 5), fontsize=9)

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_title('Spread of Printing Across Europe, 1450-1480\n'
             '(8 selected cities, approximate dates)', fontsize=14)
plt.colorbar(scatter, label='Approx. year of first press')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('print_spread_map.png', dpi=150)
plt.show()

# --- 2. Book Production: Before vs After Gutenberg ---

decades = ['1400s', '1410s', '1420s', '1430s', '1440s', '1450s', '1460s', '1470s', '1480s', '1490s']
# Illustrative, hand-set values in arbitrary units per decade. They only show
# the SHAPE of the story (manuscripts fade, print takes off). They are NOT real
# book counts and are far smaller than real-world estimates (see DATA NOTE).
manuscript = [200, 220, 250, 280, 300, 310, 250, 180, 100, 50]
printed = [0, 0, 0, 0, 0, 20, 500, 3000, 8000, 15000]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(decades))
ax.bar(x - 0.2, manuscript, 0.35, label='Manuscripts (hand-copied)', color='#8B4513')
ax.bar(x + 0.2, printed, 0.35, label='Printed Books', color='#1565C0')
ax.axvline(x=4.5, color='red', linestyle='--', alpha=0.7, label='Gutenberg (c. 1450)')

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Books per decade (illustrative units, not real counts)', fontsize=12)
ax.set_title('Manuscripts vs Printed Books per Decade\n'
             '(illustrative, hand-set values)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(decades)
ax.legend()
ax.set_yscale('symlog', linthresh=10)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('book_production.png', dpi=150)
plt.show()

# --- 3. Cost of Books Over Time ---

years_cost = [1400, 1420, 1440, 1455, 1470, 1480, 1490, 1500]
# Illustrative, hand-set relative cost index (1400 = 100); not a measured price series.
cost_ratio = [100, 100, 100, 80, 20, 8, 4, 2]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years_cost, cost_ratio, 'o-', color='#D32F2F', linewidth=2.5, markersize=8)
ax.fill_between(years_cost, cost_ratio, alpha=0.15, color='#D32F2F')
ax.axvline(x=1455, color='gray', linestyle='--', alpha=0.7)
ax.annotate('Gutenberg Bible\n(c. 1455)', (1455, 85), fontsize=10,
            ha='center', fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Relative cost index (1400 = 100, hand-set)', fontsize=12)
ax.set_title('Illustrative Book Cost Index: 100 to 2 by 1500\n'
             '(hand-set values, not measured prices)', fontsize=14)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('book_cost_decline.png', dpi=150)
plt.show()

# --- 4. Arithmetic on the article's headline estimates ---
# The inputs below are the article's rounded, commonly cited estimates. They are
# quoted, NOT computed by this script: ~30,000 books in 1450 (a popular estimate;
# scholarly estimates vary widely) and ~12,000,000 by 1500 (in line with Buringh &
# van Zanden 2009). The population is a rounded ~70 million, used for both years.
# The annual-production pair is an illustrative input, not derived from the totals.
books_1450, books_1500 = 30_000, 12_000_000
population = 70_000_000
span_years = 1500 - 1450
growth_factor = books_1500 / books_1450
cagr = growth_factor ** (1 / span_years) - 1
annual_1450, annual_1500 = 500, 1_000_000  # illustrative

# --- Summary ---
mainz_to_london = cities['London'][0] - cities['Mainz'][0]
cost_drop = 100 * (1 - cost_ratio[-1] / cost_ratio[0])

print("\n=== Printing Press Analysis Summary ===")
print("(all inputs are hand-set illustrative values, see the DATA NOTE at the top)")
print(f"Years from Mainz to London (approximate first-press dates): {mainz_to_london} years")
print(f"Illustrative cost index (1400 = 100) by 1500: {cost_ratio[-1]}, a {cost_drop:.0f}% drop by construction")
print(f"Illustrative printed output, 1490s: ~{printed[-1]:,} (hand-set units, not a real count)")
print(f"Article estimate, total books: {books_1450:,} -> {books_1500:,} = {growth_factor:.0f}x "
      f"(CAGR over {span_years} years: {cagr:.1%})")
print(f"Books per person at a rounded {population / 1e6:.0f}M population: "
      f"1 per {population / books_1450:,.0f} (1450) -> 1 per {population / books_1500:.1f} (1500)")
print(f"Illustrative annual production: {annual_1450:,} -> {annual_1500:,} books/year = "
      f"{annual_1500 / annual_1450:,.0f}x")
print("Deep Dive Pack: 20-city dataset, geographic diffusion map, city-network analysis")
print("(betweenness centrality) and a generic distance-decay diffusion simulation.")
