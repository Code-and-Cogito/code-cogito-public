"""
Article 06: The Printing Press - How Ideas Went Viral
Free Highlights: Print Spread Simulation & Cost Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Printing Press Spread Across Europe ---

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
ax.set_title('Spread of Printing Press Across Europe (1450-1480)', fontsize=14)
plt.colorbar(scatter, label='Year Established')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('print_spread_map.png', dpi=150)
plt.show()

# --- 2. Book Production: Before vs After Gutenberg ---

decades = ['1400s', '1410s', '1420s', '1430s', '1440s', '1450s', '1460s', '1470s', '1480s', '1490s']
manuscript = [200, 220, 250, 280, 300, 310, 250, 180, 100, 50]
printed = [0, 0, 0, 0, 0, 20, 500, 3000, 8000, 15000]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(decades))
ax.bar(x - 0.2, manuscript, 0.35, label='Manuscripts (hand-copied)', color='#8B4513')
ax.bar(x + 0.2, printed, 0.35, label='Printed Books', color='#1565C0')
ax.axvline(x=4.5, color='red', linestyle='--', alpha=0.7, label='Gutenberg (1450)')

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Books Produced (estimated)', fontsize=12)
ax.set_title('Book Production Revolution: Manuscripts vs Printed', fontsize=14)
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
cost_ratio = [100, 100, 100, 80, 20, 8, 4, 2]  # relative to 1400 baseline

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years_cost, cost_ratio, 'o-', color='#D32F2F', linewidth=2.5, markersize=8)
ax.fill_between(years_cost, cost_ratio, alpha=0.15, color='#D32F2F')
ax.axvline(x=1455, color='gray', linestyle='--', alpha=0.7)
ax.annotate('Gutenberg Bible\n(1455)', (1455, 85), fontsize=10,
            ha='center', fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Relative Cost (1400 = 100)', fontsize=12)
ax.set_title('Cost of a Book: 98% Drop in 50 Years', fontsize=14)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('book_cost_decline.png', dpi=150)
plt.show()

print("\n=== Printing Press Analysis Summary ===")
print(f"Years from Mainz to London: {1476-1450} years")
print(f"Book cost reduction by 1500: {100-2}%")
print(f"Printed books by 1490s: ~{printed[-1]:,}")
print("Full analysis: premium includes viral spread simulation,")
print("Luther's 95 Theses diffusion model, and literacy rate impact.")
