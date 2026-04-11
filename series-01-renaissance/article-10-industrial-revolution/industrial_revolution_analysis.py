"""
Article 10: Industrial Revolution - The Price of Progress
Free Highlights: Productivity Explosion & Urbanization Analysis
Series: The Digital Rebirth of the Renaissance | Code & Cogito
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. GDP Per Capita: Britain's Industrial Leap ---
# Data based on Maddison Project estimates (1990 international dollars)

years = [1000, 1200, 1400, 1500, 1600, 1700, 1750, 1800, 1850, 1900]
gdp_uk =     [400, 450,  500,  550,  600,  700,  800, 1200, 2300, 4500]
gdp_europe = [400, 430,  480,  520,  560,  610,  650,  800, 1200, 2500]
gdp_world =  [450, 440,  430,  420,  430,  440,  450,  500,  600,  900]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, gdp_uk, 'o-', linewidth=2.5, color='#1565C0', label='Britain', markersize=6)
ax.plot(years, gdp_europe, 's-', linewidth=2.5, color='#FF9800', label='Europe Average', markersize=6)
ax.plot(years, gdp_world, '^-', linewidth=2.5, color='#4CAF50', label='World Average', markersize=6)
ax.axvspan(1760, 1840, alpha=0.1, color='gray', label='Industrial Revolution')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('GDP Per Capita (1990 int. $)', fontsize=12)
ax.set_title('Britain\'s Industrial Leap: GDP Per Capita Over 900 Years', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('gdp_hockey_stick.png', dpi=150)
plt.show()

# --- 2. Urbanization Rate ---

decades = ['1750', '1780', '1800', '1820', '1840', '1860', '1880', '1900']
urban_pct = [20, 25, 30, 35, 45, 55, 65, 75]
rural_pct = [80, 75, 70, 65, 55, 45, 35, 25]

fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(range(len(decades)), urban_pct, rural_pct,
             labels=['Urban', 'Rural'],
             colors=['#455A64', '#81C784'], alpha=0.8)
ax.set_xticks(range(len(decades)))
ax.set_xticklabels(decades)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (%)', fontsize=12)
ax.set_title('Britain: From Rural to Urban Society', fontsize=14)
ax.legend(loc='center right', fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('urbanization.png', dpi=150)
plt.show()

# --- 3. Working Conditions: The Human Cost ---

metrics = ['Work Hours\n(per day)', 'Child Labor\n(%)', 'Life Expectancy\n(years)', 'Literacy\n(%)', 'Real Wages\n(index)']
pre_industrial = [10, 20, 40, 30, 100]
peak_industrial = [16, 50, 28, 45, 80]
late_industrial = [10, 5, 50, 85, 200]

x = np.arange(len(metrics))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, pre_industrial, width, label='Pre-Industrial (1750)', color='#81C784')
ax.bar(x, peak_industrial, width, label='Peak Industrial (1830)', color='#D32F2F')
ax.bar(x + width, late_industrial, width, label='Late Industrial (1900)', color='#1565C0')

ax.set_ylabel('Value', fontsize=12)
ax.set_title('Industrial Revolution: Progress at What Cost?', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=9)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('working_conditions.png', dpi=150)
plt.show()

print("\n=== Industrial Revolution Summary ===")
print(f"UK GDP growth 1750-1900: {(gdp_uk[-1]/gdp_uk[6]-1)*100:.0f}%")
print(f"Urbanization 1750-1900: {urban_pct[0]}% -> {urban_pct[-1]}%")
print(f"Life expectancy drop at peak: {pre_industrial[2]} -> {peak_industrial[2]} years")
print("Full analysis: premium includes factory output simulation,")
print("Luddite vs innovation model, and inequality Gini coefficient.")
