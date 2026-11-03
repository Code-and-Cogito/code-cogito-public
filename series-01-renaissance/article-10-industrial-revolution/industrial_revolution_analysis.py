"""
Article 10: Industrial Revolution - The Price of Progress
Free Highlights: GDP Hockey Stick, Urbanization & the Human Cost
Series: The Digital Rebirth of the Renaissance | Code & Cogito

DATA NOTES (read before quoting any number from this script)
- Chart 1 (GDP): the three series are hand-set, rounded, ILLUSTRATIVE values that
  sketch the general long-run shape. They are NOT copied from the Maddison
  Project Database, and the UK series rises much more steeply than the published
  one (Maddison Project Database 2023, constant 2011 int. $, via Our World in
  Data: about +181% from 1750 to 1900, versus +462% here). For the real series,
  see the free Starter Notebook (Maddison Project GDP, 1500-2022).
- Chart 2 (urbanization): approximate census-based anchor years only
  (about 17% in 1750, about 30% in 1801, 54% in 1851, 77% in 1901; sources:
  Britannica "Urbanization", Wikipedia "Demographics of the Victorian era").
  Definitions of "urban" and the area covered (England and Wales vs Great
  Britain) differ between sources. Straight lines between anchors are
  interpolation, not data.
- Chart 3 (working conditions): illustrative bars set by the author, not
  measured statistics. Reference points behind them:
    work hours   factory days of 14-16 hours (History Crunch; Striking Women),
                 about 50 hours/week in agriculture c.1750 (Voth), a 10-hour
                 day for women and children after the 1847 Factories Act
    child labor  about 25% of the workforce in the 1830s is a rough estimate;
                 published figures vary widely with the age cutoff and industry
    life exp.    the 22 years is the average found for specific groups in the
                 worst-hit industrial towns (Chadwick 1842; University of
                 Liverpool 2017), NOT a national average. England overall rose
                 from about 35 (c.1781) to about 40 (c.1851) (Wrigley &
                 Schofield, via History Skills)
    literacy, real wages   hand-set, no source
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 1. GDP Per Capita: Britain's Industrial Leap ---
# ILLUSTRATIVE, hand-set values (rounded, general long-run shape only).
# They are NOT taken from the Maddison Project Database; see DATA NOTES above.

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
ax.set_ylabel('GDP Per Capita (illustrative values)', fontsize=12)
ax.set_title("Britain's Industrial Leap: GDP Per Capita Over 900 Years\n"
             "(hand-set illustrative values, not Maddison Project data)", fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('gdp_hockey_stick.png', dpi=150)
plt.show()

# --- 2. Urbanization Rate ---
# Approximate census-based anchor years (share of population living in towns):
# about 17% in 1750, about 30% in 1801 (first census), 54% in 1851 (first
# majority-urban census), 77% in 1901. Sources: Britannica "Urbanization",
# Wikipedia "Demographics of the Victorian era". Figures are approximate and
# differ by source and by area covered. Only these anchors are plotted; the
# straight lines between them are interpolation, not data.

urban_years = [1750, 1801, 1851, 1901]
urban_pct = [17, 30, 54, 77]
rural_pct = [100 - u for u in urban_pct]

fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(urban_years, urban_pct, rural_pct,
             labels=['Urban', 'Rural'],
             colors=['#455A64', '#81C784'], alpha=0.8)
ax.plot(urban_years, urban_pct, 'o', color='white', markeredgecolor='#263238',
        markersize=7, zorder=3)
for i, (yr, pct) in enumerate(zip(urban_years, urban_pct)):
    align = 'left' if i == 0 else ('right' if i == len(urban_years) - 1 else 'center')
    ax.annotate(f'{pct}%', (yr, pct), textcoords='offset points', xytext=(0, 10),
                ha=align, fontsize=11, fontweight='bold', color='#1B1B1B')
ax.set_xlim(urban_years[0], urban_years[-1])
ax.set_ylim(0, 100)
ax.set_xticks(urban_years)
ax.set_xlabel('Year (census anchor years)', fontsize=12)
ax.set_ylabel('Population (%)', fontsize=12)
ax.set_title("Britain: From Rural to Urban Society\n"
             "(approximate figures; lines between anchor years are interpolation)", fontsize=13)
ax.legend(loc='upper left', fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('urbanization.png', dpi=150)
plt.show()

# --- 3. Working Conditions: The Human Cost ---
# ILLUSTRATIVE bars set by the author (see DATA NOTES for the reference points).
# Life expectancy: the peak bar (22) is the average for specific groups in the
# worst-hit industrial towns, not a national average (England overall: about
# 35 in c.1781 -> about 40 in c.1851).

metrics = ['Work Hours\n(per day)', 'Child Labor\n(% of workforce,\nrough estimate)',
           'Life Expectancy\n(years; peak bar =\nworst-hit towns)', 'Literacy\n(%)',
           'Real Wages\n(index)']
pre_industrial = [10, 20, 35, 30, 100]
peak_industrial = [16, 25, 22, 45, 80]
late_industrial = [10, 5, 42, 85, 200]

x = np.arange(len(metrics))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6.4))
ax.bar(x - width, pre_industrial, width, label='Pre-Industrial (1750)', color='#81C784')
ax.bar(x, peak_industrial, width, label='Peak Industrial (1830)', color='#D32F2F')
ax.bar(x + width, late_industrial, width, label='Late Industrial (1900)', color='#1565C0')

ax.set_ylabel('Value (units differ by metric)', fontsize=12)
ax.set_title('Industrial Revolution: Progress at What Cost?\n(illustrative values set by the author)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=9)
ax.legend()
ax.grid(axis='y', alpha=0.3)
fig.text(0.5, 0.012,
         "Illustrative values, not measured statistics. The life-expectancy peak bar (22 years) covers specific groups in the "
         "worst-hit industrial towns;\nEngland's national life expectancy rose from about 35 (c.1781) to about 40 (c.1851).",
         ha='center', fontsize=8, color='#444444')
plt.tight_layout(rect=(0, 0.06, 1, 1))
plt.savefig('working_conditions.png', dpi=150)
plt.show()

uk_growth = (gdp_uk[-1] / gdp_uk[6] - 1) * 100
europe_growth = (gdp_europe[-1] / gdp_europe[6] - 1) * 100
world_growth = (gdp_world[-1] / gdp_world[6] - 1) * 100

print("\n=== Industrial Revolution Summary ===")
print(f"UK GDP growth 1750-1900: {uk_growth:.0f}% (Europe {europe_growth:.0f}%, world {world_growth:.0f}%)")
print("  -> hand-set illustrative series, not Maddison Project data")
print(f"Urbanization {urban_years[0]}-{urban_years[-1]}: {urban_pct[0]}% -> {urban_pct[-1]}% "
      f"(majority urban by {urban_years[2]}: {urban_pct[2]}%; approximate)")
print(f"Child labor at peak: roughly {peak_industrial[1]}% of the workforce (rough estimate; varies with age cutoff and industry)")
print(f"Life expectancy: {pre_industrial[2]} years pre-industrial baseline vs {peak_industrial[2]} years "
      "for specific groups in the worst-hit industrial towns")
print("  -> not a national average: England overall rose from about 35 to about 40 (c.1781-c.1851)")
print("Chart 3 values are illustrative (set by the author), not measured statistics.")
print("Full analysis: the Deep Dive Pack adds an industrialization dashboard (GDP, cotton,")
print("coal, steam engines, railways), a three-phase regression of GDP per capita, a")
print("13-indicator correlation heatmap, a Kuznets curve and a 500-run Monte Carlo counterfactual.")
