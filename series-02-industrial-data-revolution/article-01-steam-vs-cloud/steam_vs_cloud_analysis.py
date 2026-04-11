"""
Steam vs Cloud Computing - Free Version
Season 3 Article 08: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic Bass diffusion S-curve
- Simple cost comparison chart
- Basic market share overview

For complete version with 11 sub-plots, see premium content.

Requirements:
pip install numpy pandas matplotlib scipy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Steam vs Cloud Computing - Free Version")
print("Season 3 Article 08")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Bass Diffusion S-Curve (Basic)
# ============================================================================

def bass_diffusion_basic():
    """Basic Bass diffusion model for steam engine adoption"""
    print("\n[Visualization 1] Steam Engine Adoption S-Curve")
    print("-" * 70)

    def bass_model(t, p, q, m):
        return m * (1 - np.exp(-(p+q)*t)) / (1 + (q/p) * np.exp(-(p+q)*t))

    steam_data = {
        'year': [1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850],
        'count': [100, 280, 520, 1100, 2200, 4500, 8500, 15000, 25000, 38000]
    }

    df_steam = pd.DataFrame(steam_data)
    df_steam['t'] = df_steam['year'] - 1760

    popt, _ = curve_fit(bass_model, df_steam['t'].values, df_steam['count'].values,
                        p0=[0.01, 0.3, 50000],
                        bounds=([0.001, 0.05, 10000], [0.05, 1.0, 100000]))

    t_predict = np.linspace(0, 100, 500)
    count_predict = bass_model(t_predict, *popt)

    plt.figure(figsize=(12, 7))
    plt.plot(t_predict + 1760, count_predict, 'b-', linewidth=2.5, label='Bass Model')
    plt.scatter(df_steam['year'], df_steam['count'], color='red', s=100, zorder=5, label='Historical Data')
    plt.axvline(x=1776, color='green', linestyle='--', alpha=0.7, label="1776: Watt's Engine")

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Steam Engines', fontsize=12)
    plt.title('UK Steam Engine Adoption: S-shaped Diffusion\n1760-1850',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('s3_08_bass_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    p, q, m = popt
    print(f"\n  Innovation coefficient (p): {p:.4f}")
    print(f"  Imitation coefficient (q): {q:.4f}")
    print(f"  q/p ratio: {q/p:.1f} (imitation dominates)")

# ============================================================================
# Visualization 2: Cost Comparison (Simple)
# ============================================================================

def cost_comparison_simple():
    """Simple cost reduction comparison"""
    print("\n[Visualization 2] Cost Reduction Comparison")
    print("-" * 70)

    steam_cost = np.array([12, 11, 10, 8, 6.5, 5, 4.5, 4, 3.5, 3])
    ec2_price = np.array([0.10, 0.085, 0.068, 0.052, 0.040, 0.032, 0.026, 0.021, 0.017, 0.0135])

    steam_norm = steam_cost / steam_cost[0] * 100
    cloud_norm = ec2_price / ec2_price[0] * 100
    progress = np.linspace(0, 100, len(steam_norm))

    plt.figure(figsize=(12, 7))
    plt.plot(progress, steam_norm, 'r-o', linewidth=2.5, markersize=8,
             label='Steam Engine (90 years)', alpha=0.8)
    plt.plot(progress, cloud_norm, 'b-s', linewidth=2.5, markersize=8,
             label='Cloud Computing (18 years)', alpha=0.8)

    plt.xlabel('Time Progress (%)', fontsize=12)
    plt.ylabel('Cost (% of initial)', fontsize=12)
    plt.title('Cost Reduction: Steam Engine vs Cloud Computing\n(Normalized)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('s3_08_cost_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    steam_drop = (1 - steam_cost[-1]/steam_cost[0]) * 100
    cloud_drop = (1 - ec2_price[-1]/ec2_price[0]) * 100
    print(f"\n  Steam cost reduction: {steam_drop:.1f}% over 90 years")
    print(f"  Cloud cost reduction: {cloud_drop:.1f}% over 18 years")

# ============================================================================
# Visualization 3: Market Share Overview (Basic)
# ============================================================================

def market_share_basic():
    """Basic cloud market share pie chart"""
    print("\n[Visualization 3] Cloud Market Share (2024)")
    print("-" * 70)

    market = {'AWS': 32, 'Azure': 23, 'Google Cloud': 11, 'Alibaba': 4, 'Others': 30}
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#D3D3D3']

    plt.figure(figsize=(10, 8))
    plt.pie(market.values(), labels=market.keys(), autopct='%1.0f%%',
            startangle=90, colors=colors, explode=(0.1, 0.05, 0, 0, 0),
            textprops={'fontsize': 12, 'weight': 'bold'})
    plt.title('Global Cloud Market Share (2024)\nTop 3 control 66%',
              fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('s3_08_market_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    hhi = sum([s**2 for s in market.values()])
    print(f"\n  HHI Index: {hhi:.0f}")
    print(f"  Market classification: {'Moderately concentrated' if hhi >= 1500 else 'Competitive'}")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 11 sub-plots, see premium content)\n")

bass_diffusion_basic()
cost_comparison_simple()
market_share_basic()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. s3_08_bass_basic.png - Steam engine adoption S-curve")
print("  2. s3_08_cost_basic.png - Cost reduction comparison")
print("  3. s3_08_market_basic.png - Cloud market share")
print("\n[Premium Version Includes]")
print("  - Full Bass model with adoption rate analysis (2 sub-plots)")
print("  - Detailed cost curves with exponential decay fitting (3 sub-plots)")
print("  - Historical coal vs cloud market concentration (3 sub-plots)")
print("  - AWS global distribution inequality analysis (2 sub-plots)")
print("  - Future scenario quadrant analysis (1 sub-plot)")
print("  - Total: 11 professional sub-plots")
print("=" * 70)
