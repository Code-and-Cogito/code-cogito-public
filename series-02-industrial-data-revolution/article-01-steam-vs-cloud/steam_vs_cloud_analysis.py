"""
Steam vs Cloud Computing - Free Version
Series 2 (Industrial Revolution Meets the Data Revolution), Article 01

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic Bass diffusion S-curve
- Simple cost comparison chart
- Basic market share overview

NOTE ON THE DATA: every input series below (UK steam-engine counts, the steam
and cloud cost series, the 2024 market shares) is ILLUSTRATIVE. The numbers are
set by the author for teaching and are NOT verified historical statistics or
vendor records. The only real-world anchor is the 2006 EC2 launch price of
$0.10 per hour. Everything the script prints is the result of feeding those
series into a model, so read it as "in this model", not as a historical fact.

For complete version with 11 sub-plots, see premium content.

Requirements:
pip install numpy pandas matplotlib scipy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Steam vs Cloud Computing - Free Version")
print("Series 2 - Article 01")
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

    # Illustrative decade-by-decade engine counts set by the author.
    # These are NOT historical statistics (no published series is being quoted).
    steam_data = {
        'year': [1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850],
        'count': [100, 280, 520, 1100, 2200, 4500, 8500, 15000, 25000, 38000]
    }

    df_steam = pd.DataFrame(steam_data)
    df_steam['t'] = df_steam['year'] - 1760

    # Fit bounds for (p, q, m). Note: with these bounds the fit ends up on the
    # lower bound for both p and q (see the note printed below), so q/p is
    # decided by the bounds more than by the data.
    lower_bounds = [0.001, 0.05, 10000]
    upper_bounds = [0.05, 1.0, 100000]
    popt, _ = curve_fit(bass_model, df_steam['t'].values, df_steam['count'].values,
                        p0=[0.01, 0.3, 50000],
                        bounds=(lower_bounds, upper_bounds))

    t_predict = np.linspace(0, 100, 500)
    count_predict = bass_model(t_predict, *popt)

    plt.figure(figsize=(12, 7))
    plt.plot(t_predict + 1760, count_predict, 'b-', linewidth=2.5, label='Bass Model (fitted)')
    plt.scatter(df_steam['year'], df_steam['count'], color='red', s=100, zorder=5,
                label='Illustrative data (author-set)')
    plt.axvline(x=1776, color='green', linestyle='--', alpha=0.7,
                label="1776: first commercial Watt engines")

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Steam Engines', fontsize=12)
    plt.title('UK Steam Engine Adoption: S-shaped Diffusion\n1760-1850 (illustrative data)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('technology_adoption_bass.png', dpi=300, bbox_inches='tight')
    plt.show()

    p, q, m = popt
    print(f"\n  Innovation coefficient (p): {p:.4f}")
    print(f"  Imitation coefficient (q): {q:.4f}")
    print(f"  q/p ratio: {q/p:.1f} (imitation dominates)")

    # Peak of the adoption RATE of the fitted Bass curve: t* = ln(q/p) / (p + q)
    peak_year = int(round(1760 + np.log(q / p) / (p + q)))
    print(f"  Peak adoption growth in this model: around {peak_year}")
    print(f"  Lag after 1776 (first commercial Watt engines): {peak_year - 1776} years")

    # Be explicit when the optimizer stopped on a bound
    at_bound = [name for name, val, lo, hi in zip(['p', 'q', 'm'], popt, lower_bounds, upper_bounds)
                if np.isclose(val, lo, rtol=1e-3) or np.isclose(val, hi, rtol=1e-3)]
    if at_bound:
        print(f"  Note: {' and '.join(at_bound)} hit a fit bound, so q/p and the peak year mostly")
        print("        reflect the chosen bounds rather than being estimated from the data.")

# ============================================================================
# Visualization 2: Cost Comparison (Simple)
# ============================================================================

def cost_comparison_simple():
    """Simple cost reduction comparison"""
    print("\n[Visualization 2] Cost Reduction Comparison")
    print("-" * 70)

    # Illustrative cost series set by the author (10 points each); not official statistics.
    # steam_cost: notional units, spanning 1760-1850 (90 years).
    # ec2_price: USD per hour, spanning 2006-2024 (18 years). Only the first value
    #            (0.10, the 2006 EC2 launch price) is a real anchor; the rest are illustrative.
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
    plt.title('Cost Reduction: Steam Engine vs Cloud Computing\n(Normalized, illustrative series)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('cost_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    steam_drop = (1 - steam_cost[-1]/steam_cost[0]) * 100
    cloud_drop = (1 - ec2_price[-1]/ec2_price[0]) * 100
    print(f"\n  Steam cost reduction: {steam_drop:.1f}% over 90 years (illustrative series)")
    print(f"  Cloud cost reduction: {cloud_drop:.1f}% over 18 years (illustrative series)")

# ============================================================================
# Visualization 3: Market Share Overview (Basic)
# ============================================================================

def market_share_basic():
    """Basic cloud market share pie chart"""
    print("\n[Visualization 3] Cloud Market Share (2024, author's rough estimate)")
    print("-" * 70)

    # Rough 2024 shares (%) set by the author for illustration; NOT an official statistic.
    # Published estimates differ by analyst firm and period, so check a current
    # source before quoting any of these numbers.
    market = {'AWS': 32, 'Azure': 23, 'Google Cloud': 11, 'Alibaba': 4, 'Others': 30}
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#D3D3D3']

    named = {name: share for name, share in market.items() if name != 'Others'}
    top3 = sum(sorted(named.values(), reverse=True)[:3])

    plt.figure(figsize=(10, 8))
    plt.pie(market.values(), labels=market.keys(), autopct='%1.0f%%',
            startangle=90, colors=colors, explode=(0.1, 0.05, 0, 0, 0),
            textprops={'fontsize': 12, 'weight': 'bold'})
    plt.title(f"Global Cloud Market Share (2024, author's rough estimate)\nTop 3 = {top3}% in this estimate",
              fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('market_growth.png', dpi=300, bbox_inches='tight')
    plt.show()

    # HHI = sum of squared market shares (shares in percent, so the maximum is 10,000).
    # 'Others' is a long tail of many small providers, so it is left out of the sum:
    # counting it as ONE firm would add 30**2 = 900 points and overstate concentration.
    # The value below is therefore a lower bound that assumes a fully fragmented tail.
    hhi = sum(share ** 2 for share in named.values())

    # Bands follow the 1,500 / 2,500 cut-offs used in the article's HHI table.
    if hhi >= 2500:
        classification = 'Highly concentrated'
    elif hhi >= 1500:
        classification = 'Moderately concentrated'
    else:
        classification = 'Competitive'

    print(f"\n  HHI Index (named providers only, 'Others' left out): {hhi:.0f}")
    print(f"  Market classification: {classification}")
    print("  (bands: below 1,500 competitive, 1,500-2,500 moderate, above 2,500 high)")
    print("  Note: the HHI values in the article's table are a separate rough estimate")
    print("        by the author, not computed by this script.")

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
print("\nGenerated plots (in the current directory):")
print("  1. technology_adoption_bass.png - Steam engine adoption S-curve")
print("  2. cost_comparison.png - Cost reduction comparison")
print("  3. market_growth.png - Cloud market share")
print("\n[Premium Version Includes]")
print("  - Full Bass model with adoption rate analysis (2 sub-plots)")
print("  - Detailed cost curves with exponential decay fitting (3 sub-plots)")
print("  - Historical coal vs cloud market concentration (3 sub-plots)")
print("  - AWS global distribution inequality analysis (2 sub-plots)")
print("  - Future scenario quadrant analysis (1 sub-plot)")
print("  - Total: 11 professional sub-plots")
print("=" * 70)
