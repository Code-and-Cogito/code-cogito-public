"""
Data Archaeology: Reconstructing Britain's Economic Transformation (1760-1840) - Free Version
Season 3 Article 11: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic GDP growth trend
- Simple urbanization bar chart
- Economic structure pie chart

For complete version with 11 sub-plots, see premium content.

Requirements:
pip install numpy pandas matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Data Archaeology: Britain's Economic Transformation - Free Version")
print("Season 3 Article 11")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: GDP Growth Trend (Basic)
# ============================================================================

def gdp_growth_basic():
    """Basic UK GDP growth trend 1760-1850"""
    print("\n[Visualization 1] UK GDP Growth Trend")
    print("-" * 70)

    # Maddison Project style GDP estimates (index, 1760=100)
    years = np.array([1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850])
    gdp_index = np.array([100, 108, 115, 128, 145, 165, 190, 225, 270, 330])

    # Calculate decade growth rates
    growth_rates = []
    for i in range(1, len(gdp_index)):
        decade_span = (years[i] - years[i-1])
        annual_rate = ((gdp_index[i] / gdp_index[i-1]) ** (1.0 / decade_span) - 1) * 100
        growth_rates.append(annual_rate)
    growth_rates = np.array(growth_rates)
    growth_years = (years[:-1] + years[1:]) / 2

    # Pre/post averages
    pre_mask = growth_years < 1800
    post_mask = growth_years >= 1800
    avg_pre = np.mean(growth_rates[pre_mask])
    avg_post = np.mean(growth_rates[post_mask])

    plt.figure(figsize=(12, 7))
    plt.plot(years, gdp_index, 'b-o', linewidth=2.5, markersize=8, label='GDP Index (1760=100)')

    # Trend lines
    z_pre = np.polyfit(years[years <= 1800], np.log(gdp_index[years <= 1800]), 1)
    z_post = np.polyfit(years[years >= 1800], np.log(gdp_index[years >= 1800]), 1)
    years_pre = np.linspace(1760, 1800, 50)
    years_post = np.linspace(1800, 1850, 50)
    plt.plot(years_pre, np.exp(np.polyval(z_pre, years_pre)),
             'g--', linewidth=2, alpha=0.7, label=f'Pre-1800 trend ({avg_pre:.1f}%/yr)')
    plt.plot(years_post, np.exp(np.polyval(z_post, years_post)),
             'r--', linewidth=2, alpha=0.7, label=f'Post-1800 trend ({avg_post:.1f}%/yr)')

    plt.axvline(x=1800, color='orange', linestyle=':', linewidth=2, alpha=0.8,
                label='Structural Break ~1800')

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP Index (1760=100)', fontsize=12)
    plt.title('UK GDP Growth with Structural Break\n1760-1850 (Maddison Estimates)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('s3_11_gdp_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  GDP grew {gdp_index[-1]/gdp_index[0]:.1f}x from 1760 to 1850")
    print(f"  Pre-industrial avg growth: {avg_pre:.2f}%/yr")
    print(f"  Post-industrial avg growth: {avg_post:.2f}%/yr")

# ============================================================================
# Visualization 2: City Population Growth (Simple)
# ============================================================================

def urbanization_basic():
    """Simple city population growth bar chart"""
    print("\n[Visualization 2] City Population Growth")
    print("-" * 70)

    cities = {
        'Manchester': [18000, 25000, 42000, 75000, 130000, 182000, 235000, 300000],
        'Birmingham': [70000, 73000, 78000, 87000, 110000, 144000, 183000, 230000],
        'Leeds': [16000, 20000, 30000, 53000, 83000, 123000, 152000, 172000],
        'London': [740000, 800000, 900000, 960000, 1100000, 1350000, 1650000, 2360000]
    }

    # Show start vs end comparison
    city_names = list(cities.keys())
    pop_start = [cities[c][0] / 1000 for c in city_names]
    pop_end = [cities[c][-1] / 1000 for c in city_names]
    growth_x = [cities[c][-1] / cities[c][0] for c in city_names]

    x = np.arange(len(city_names))
    width = 0.35

    plt.figure(figsize=(12, 7))
    bars1 = plt.bar(x - width/2, pop_start, width, label='1750', color='#3498db', alpha=0.8)
    bars2 = plt.bar(x + width/2, pop_end, width, label='1850', color='#e74c3c', alpha=0.8)

    # Add growth multiple labels
    for i, (xi, mult) in enumerate(zip(x, growth_x)):
        plt.text(xi, max(pop_start[i], pop_end[i]) + 50, f'{mult:.0f}x',
                 ha='center', fontsize=12, fontweight='bold', color='#2c3e50')

    plt.xticks(x, city_names, fontsize=12)
    plt.ylabel('Population (thousands)', fontsize=12)
    plt.title('City Population Growth: 1750 vs 1850\n(Numbers show growth multiple)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('s3_11_urbanization_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n  Population growth (1750 → 1850):")
    for city in city_names:
        mult = cities[city][-1] / cities[city][0]
        print(f"    {city:12s}: {cities[city][0]:>10,} → {cities[city][-1]:>10,}  ({mult:.1f}x)")

# ============================================================================
# Visualization 3: Economic Structure Comparison (Basic)
# ============================================================================

def economic_structure_basic():
    """Basic economic structure pie chart comparison"""
    print("\n[Visualization 3] Economic Structure: 1760 vs 1850")
    print("-" * 70)

    sectors = ['Agriculture', 'Industry', 'Services']
    data_1760 = [70, 20, 10]
    data_1850 = [22, 45, 33]
    colors = ['#27ae60', '#e67e22', '#3498db']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    ax1.pie(data_1760, labels=sectors, autopct='%1.0f%%', startangle=90,
            colors=colors, textprops={'fontsize': 12, 'weight': 'bold'})
    ax1.set_title('1760\nPre-Industrial', fontsize=14, fontweight='bold')

    ax2.pie(data_1850, labels=sectors, autopct='%1.0f%%', startangle=90,
            colors=colors, textprops={'fontsize': 12, 'weight': 'bold'})
    ax2.set_title('1850\nPost-Industrial', fontsize=14, fontweight='bold')

    fig.suptitle('Economic Structure Transformation\nBritain 1760 vs 1850',
                 fontsize=16, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig('s3_11_structure_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  1760: Agriculture {data_1760[0]}%, Industry {data_1760[1]}%, Services {data_1760[2]}%")
    print(f"  1850: Agriculture {data_1850[0]}%, Industry {data_1850[1]}%, Services {data_1850[2]}%")
    print(f"  Agriculture fell {data_1760[0] - data_1850[0]} percentage points")
    print(f"  Industry rose {data_1850[1] - data_1760[1]} percentage points")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 11 sub-plots, see premium content)\n")

gdp_growth_basic()
urbanization_basic()
economic_structure_basic()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. s3_11_gdp_basic.png - GDP growth with structural break")
print("  2. s3_11_urbanization_basic.png - City population comparison")
print("  3. s3_11_structure_basic.png - Economic structure 1760 vs 1850")
print("\n[Premium Version Includes]")
print("  - Full GDP analysis with growth rate bars & per capita trend (3 sub-plots)")
print("  - Detailed urbanization with city heatmap & urban/rural ratio (2 sub-plots)")
print("  - Economic structure stacked area chart & pie comparison (2 sub-plots)")
print("  - Patent/innovation network analysis with network graph (2 sub-plots)")
print("  - Trade data with export composition & trade balance (2 sub-plots)")
print("  - Total: 11 professional sub-plots")
print("=" * 70)
