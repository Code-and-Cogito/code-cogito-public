"""
Alienation Mathematics - Free Version
Season 3 Article 10: Sample Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Alienation Index Era Comparison (1 sub-plot): bar chart of alienation scores across eras
- Historical Alienation Trend (1 sub-plot): trend line from 1750 to 2024
- Apparent vs Actual Autonomy (1 sub-plot): gig worker autonomy gap
Total: 3 sample sub-plots

For the full 14 sub-plots including heatmaps, sentiment analysis,
radar charts, and algorithm alienation deep dive, see the premium version.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Alienation Mathematics - Free Sample Version")
print("Season 3 Article 10")
print("=" * 70)
print()

# ============================================================================
# Plot 1: Alienation Index Era Comparison (1 sub-plot)
# ============================================================================

def alienation_era_comparison():
    """
    Bar chart comparing alienation index across three eras.
    Based on formula: alienation = 1.0 - 0.3*ownership - 0.25*autonomy
                                   - 0.25*creativity - 0.2*social_connection
    """
    print("\n[Plot 1] Alienation Index Era Comparison")
    print("-" * 70)

    eras = ['Artisan\n(1800)', 'Factory Worker\n(1900)', 'Gig Worker\n(2024)']
    alienation_scores = [0.20, 0.70, 0.75]
    colors = ['#2E86AB', '#A23B72', '#F18F01']

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(eras, alienation_scores, color=colors, alpha=0.85,
                  edgecolor='white', linewidth=2, width=0.55)

    for bar, score in zip(bars, alienation_scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{score:.2f}', ha='center', va='bottom', fontsize=16, fontweight='bold')

    ax.set_ylabel('Alienation Index (0 = none, 1 = total)', fontsize=12)
    ax.set_title('Marx\'s Alienation Index Across Eras\n'
                 'alienation = 1.0 - 0.3×ownership - 0.25×autonomy - 0.25×creativity - 0.2×social',
                 fontsize=13, fontweight='bold')
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Critical threshold')
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)

    # Add context table below bars
    table_data = [
        ['Product Ownership', '100%', '0%', '0%'],
        ['Work Autonomy', '90%', '20%', '30% (actual)'],
        ['Creativity', '80%', '10%', '15%'],
        ['Social Connection', '70%', '40%', '20%'],
    ]
    table = ax.table(cellText=table_data,
                     colLabels=['Dimension', 'Artisan', 'Factory', 'Gig Worker'],
                     cellLoc='center', loc='bottom',
                     bbox=[0.0, -0.45, 1.0, 0.3])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#264653')
            cell.set_text_props(color='white', fontweight='bold')
        elif col == 0:
            cell.set_facecolor('#f0f0f0')
        cell.set_edgecolor('white')

    plt.subplots_adjust(bottom=0.30)
    plt.savefig('s3_a10_free_alienation_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  ✓ Artisan alienation: 0.20 (pre-industrial baseline)")
    print(f"  ✓ Factory worker: 0.70 (Marx's industrial era)")
    print(f"  ✓ Gig worker: 0.75 (algorithmic control exceeds factory alienation)")


# ============================================================================
# Plot 2: Historical Alienation Trend (1 sub-plot)
# ============================================================================

def historical_alienation_trend():
    """
    Historical trend line of alienation index from 1750 to 2024.
    Shows how alienation evolved through different economic eras.
    """
    print("\n[Plot 2] Historical Alienation Trend")
    print("-" * 70)

    years = [1750, 1800, 1850, 1900, 1950, 1970, 2000, 2010, 2020, 2024]
    alienation_trend = [0.15, 0.20, 0.45, 0.70, 0.65, 0.55, 0.50, 0.55, 0.68, 0.75]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(years, alienation_trend, 'o-', color='#E63946', linewidth=2.5, markersize=9,
            markerfacecolor='white', markeredgewidth=2.5, markeredgecolor='#E63946')
    ax.fill_between(years, alienation_trend, alpha=0.12, color='#E63946')

    # Annotate key periods
    annotations = {
        (1800, 0.20): 'Artisan era\n(pre-industrial)',
        (1900, 0.70): 'Factory system\npeak alienation',
        (1970, 0.55): 'Welfare state\nbrief recovery',
        (2024, 0.75): 'Gig economy\nnew historical peak'
    }
    for (x_pos, y_pos), label in annotations.items():
        offset_y = 22 if y_pos < 0.6 else -30
        ax.annotate(label, xy=(x_pos, y_pos),
                    xytext=(0, offset_y), textcoords='offset points',
                    ha='center', fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.9))

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Alienation Index', fontsize=12)
    ax.set_title('Historical Alienation Trend (1750-2024)\n'
                 'From Artisan Workshop to Algorithm-Controlled Gig Work',
                 fontsize=13, fontweight='bold')
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.5, color='orange', linestyle='--', alpha=0.5, label='Critical threshold')
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig('s3_a10_free_alienation_trend.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  ✓ Lowest alienation: 1750 (0.15) - artisan workshop era")
    print(f"  ✓ First peak: 1900 (0.70) - factory system under industrial capitalism")
    print(f"  ✓ Brief decline: 1970 (0.55) - welfare state and labor protections")
    print(f"  ✓ New peak: 2024 (0.75) - gig economy surpasses factory-era alienation")


# ============================================================================
# Plot 3: Apparent vs Actual Autonomy (1 sub-plot)
# ============================================================================

def apparent_vs_actual_autonomy():
    """
    Bar chart showing the gap between perceived and real autonomy
    for gig workers. Exposes the 'freedom illusion' of platform work.
    """
    print("\n[Plot 3] Apparent vs Actual Gig Worker Autonomy")
    print("-" * 70)

    dimensions = ['Decision\nPower', 'Time\nControl', 'Method\nChoice',
                  'Pace\nSetting', 'Tool\nSelection', 'Output\nQuality']

    apparent = [60, 70, 55, 50, 45, 40]
    actual =   [15, 35, 20, 10, 15, 25]

    x = np.arange(len(dimensions))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))
    bars_app = ax.bar(x - width/2, apparent, width,
                      label='Apparent Autonomy (platform marketing)',
                      color='#F4A261', alpha=0.85, edgecolor='white', linewidth=1.5)
    bars_act = ax.bar(x + width/2, actual, width,
                      label='Actual Autonomy (measured reality)',
                      color='#E63946', alpha=0.85, edgecolor='white', linewidth=1.5)

    # Add gap annotations
    for i in range(len(dimensions)):
        gap = apparent[i] - actual[i]
        ax.annotate('', xy=(x[i] + width/2, actual[i]),
                    xytext=(x[i] - width/2, apparent[i]),
                    arrowprops=dict(arrowstyle='<->', color='#264653', lw=1.5))
        ax.text(x[i], max(apparent[i], actual[i]) + 3,
                f'Gap: {gap}%', ha='center', fontsize=9,
                color='#264653', fontweight='bold')

    # Add value labels on bars
    for bar in bars_app:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h - 4, f'{h}%',
                ha='center', va='top', fontsize=9, color='white', fontweight='bold')
    for bar in bars_act:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h - 4, f'{h}%',
                ha='center', va='top', fontsize=9, color='white', fontweight='bold')

    ax.set_xlabel('Autonomy Dimension', fontsize=12)
    ax.set_ylabel('Autonomy Score (%)', fontsize=12)
    ax.set_title('Gig Worker Autonomy: Perception vs Reality\n'
                 '"Be your own boss" - The Algorithmic Freedom Illusion',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions, fontsize=10)
    ax.legend(fontsize=10, loc='upper right')
    ax.set_ylim(0, 85)
    ax.grid(axis='y', alpha=0.3)

    # Summary text box
    avg_gap = np.mean(np.array(apparent) - np.array(actual))
    autonomy_apparent = 0.4 * apparent[0] + 0.3 * apparent[1] + 0.3 * apparent[2]
    autonomy_actual = 0.4 * actual[0] + 0.3 * actual[1] + 0.3 * actual[2]
    summary = (f'Autonomy Index (0.4×decision + 0.3×time + 0.3×method)\n'
               f'Apparent: {autonomy_apparent:.0f}  |  Actual: {autonomy_actual:.0f}  |  '
               f'Avg Gap: {avg_gap:.0f}%')
    ax.text(0.5, 0.02, summary, transform=ax.transAxes, fontsize=10,
            ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3cd', alpha=0.9))

    plt.tight_layout()
    plt.savefig('s3_a10_free_autonomy_gap.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  ✓ Average perception gap: {avg_gap:.0f}% across all dimensions")
    print(f"  ✓ Largest gap: Time Control ({apparent[1] - actual[1]}%)")
    print(f"  ✓ Autonomy index: apparent {autonomy_apparent:.0f} vs actual {autonomy_actual:.0f}")
    print(f"  ✓ 'Be your own boss' narrative masks algorithmic control")


# ============================================================================
# Execute All Plots
# ============================================================================

alienation_era_comparison()
historical_alienation_trend()
apparent_vs_actual_autonomy()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Sample Version Finished!")
print("=" * 70)
print()
print("Generated files:")
print("  1. s3_a10_free_alienation_comparison.png  (1 sub-plot)")
print("  2. s3_a10_free_alienation_trend.png       (1 sub-plot)")
print("  3. s3_a10_free_autonomy_gap.png           (1 sub-plot)")
print(f"  Total: 3 sample sub-plots")
print()
print("  ╔══════════════════════════════════════════════════════════╗")
print("  ║  Upgrade to Premium for 14 sub-plots including:        ║")
print("  ║  • Alienation heatmap across all dimensions             ║")
print("  ║  • Worker diary NLP sentiment analysis                  ║")
print("  ║  • Gig worker social media sentiment & word frequency   ║")
print("  ║  • Labor autonomy radar chart (4-era comparison)        ║")
print("  ║  • Algorithm alienation deep dive (creators & consumers)║")
print("  ╚══════════════════════════════════════════════════════════╝")
print("=" * 70)
