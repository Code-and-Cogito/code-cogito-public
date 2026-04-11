"""
Child Labor vs AI Bias - Free Version
Season 3 Article 12: Basic Visualizations

Author: Wina Wu
Date: 2025-12

This free version includes:
- Basic child labor trends chart
- Simple facial recognition bias comparison
- Basic historical comparison overview

For complete version with 12 sub-plots, see premium content.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Child Labor vs AI Bias - Free Version")
print("Season 3 Article 12")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Child Labor Trends (Basic)
# ============================================================================

def child_labor_basic():
    """Basic child labor trends 1800-1900"""
    print("\n[Visualization 1] Child Labor Trends (1800-1900)")
    print("-" * 70)

    years = [1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900]
    child_labor_pct = {
        'Textiles': [25, 30, 35, 38, 35, 28, 20, 15, 10, 7, 5],
        'Mining': [15, 18, 22, 25, 20, 12, 8, 5, 3, 2, 1],
        'Chimney': [10, 12, 14, 15, 10, 5, 3, 1, 0.5, 0, 0],
        'Other': [20, 22, 25, 28, 25, 20, 15, 12, 8, 5, 3]
    }

    total = [sum(child_labor_pct[ind][i] for ind in child_labor_pct) for i in range(len(years))]

    colors = {'Textiles': '#E74C3C', 'Mining': '#8B4513', 'Chimney': '#2C3E50', 'Other': '#F39C12'}

    plt.figure(figsize=(14, 8))

    for industry, rates in child_labor_pct.items():
        plt.plot(years, rates, '-o', linewidth=2.5, markersize=7,
                 color=colors[industry], label=industry, alpha=0.8)

    plt.plot(years, total, 'k--', linewidth=3, markersize=9, label='Total',
             alpha=0.6, marker='D')

    # Key legislation markers
    legislation = {1833: 'Factory Act', 1842: 'Mines Act', 1878: 'Factory &\nWorkshop Act'}
    for year, name in legislation.items():
        plt.axvline(x=year, color='green', linestyle='--', alpha=0.5, linewidth=1.5)
        plt.text(year + 1, max(total) * 0.95, name, fontsize=9, color='darkgreen',
                 fontweight='bold', rotation=0)

    plt.xlabel('Year', fontsize=13)
    plt.ylabel('Child Labor Rate (%)', fontsize=13)
    plt.title('Child Labor Rates in Britain (1800-1900)\nPeaked ~1830, Declined After Factory Acts',
              fontsize=15, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(1795, 1905)

    # Annotate peak
    peak_idx = np.argmax(total)
    plt.annotate(f'Peak: {total[peak_idx]:.0f}%\n({years[peak_idx]})',
                 xy=(years[peak_idx], total[peak_idx]),
                 xytext=(years[peak_idx] + 15, total[peak_idx] + 8),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=12, fontweight='bold', color='red')

    plt.tight_layout()
    plt.savefig('s3_12_child_labor_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Peak child labor: {years[peak_idx]} ({total[peak_idx]:.0f}% combined)")
    print(f"  By 1900: {total[-1]:.0f}% (down from {total[0]:.0f}%)")
    print(f"  Textiles was the worst offender, peaking at {max(child_labor_pct['Textiles'])}%")

# ============================================================================
# Visualization 2: Facial Recognition Bias (Simple)
# ============================================================================

def facial_recognition_basic():
    """Simple facial recognition error rate comparison"""
    print("\n[Visualization 2] Facial Recognition Bias")
    print("-" * 70)

    demographics = ['White\nMale', 'White\nFemale', 'Black\nMale', 'Black\nFemale',
                    'Asian\nMale', 'Asian\nFemale']
    error_rates = [0.8, 3.0, 12.0, 35.0, 5.0, 8.0]

    colors = ['#27AE60', '#2ECC71', '#E67E22', '#E74C3C', '#3498DB', '#5DADE2']

    plt.figure(figsize=(12, 8))
    bars = plt.bar(demographics, error_rates, color=colors, alpha=0.85,
                   edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val in zip(bars, error_rates):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.8,
                 f'{val}%', ha='center', va='bottom', fontsize=13, fontweight='bold')

    # Acceptable threshold
    plt.axhline(y=5.0, color='green', linestyle='--', alpha=0.7, linewidth=2,
                label='Acceptable Threshold (5%)')

    # Highlight disparity
    plt.annotate(f'{error_rates[3]/error_rates[0]:.0f}x higher\nthan White Male!',
                 xy=(3, error_rates[3]),
                 xytext=(4.3, 30),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
                 fontsize=13, fontweight='bold', color='red')

    plt.xlabel('Demographic Group', fontsize=13)
    plt.ylabel('Error Rate (%)', fontsize=13)
    plt.title('Facial Recognition Error Rates by Demographics\nBlack Women Face 44x Higher Error Than White Men',
              fontsize=15, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('s3_12_facial_recognition_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    disparity = error_rates[3] / error_rates[0]
    print(f"\n  Lowest error rate: White Male ({error_rates[0]}%)")
    print(f"  Highest error rate: Black Female ({error_rates[3]}%)")
    print(f"  Disparity ratio: {disparity:.0f}x")
    print(f"  Groups above 5% threshold: {sum(1 for r in error_rates if r > 5)}/{len(error_rates)}")

# ============================================================================
# Visualization 3: Historical Comparison Overview
# ============================================================================

def historical_comparison_basic():
    """Basic comparison between child labor and AI bias"""
    print("\n[Visualization 3] Historical Comparison: Then vs Now")
    print("-" * 70)

    # Comparison metrics (normalized to 0-10 scale)
    dimensions = ['Victim\nCount', 'Economic\nImpact', 'Visibility', 'Public\nAwareness',
                  'Legal\nResponse', 'Organized\nResistance']
    child_labor_scores = [9, 7, 9, 6, 7, 8]  # 1800s child labor
    ai_bias_scores = [8, 9, 2, 4, 3, 2]  # 2020s AI bias

    x = np.arange(len(dimensions))
    width = 0.35

    plt.figure(figsize=(14, 8))

    bars1 = plt.bar(x - width/2, child_labor_scores, width,
                    label='Child Labor (1800s)', color='#8B4513', alpha=0.85,
                    edgecolor='white', linewidth=1.5)
    bars2 = plt.bar(x + width/2, ai_bias_scores, width,
                    label='Algorithm Bias (2020s)', color='#3498DB', alpha=0.85,
                    edgecolor='white', linewidth=1.5)

    # Add value labels
    for bar, val in zip(bars1, child_labor_scores):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.15,
                 str(val), ha='center', va='bottom', fontsize=12, fontweight='bold',
                 color='#8B4513')
    for bar, val in zip(bars2, ai_bias_scores):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.15,
                 str(val), ha='center', va='bottom', fontsize=12, fontweight='bold',
                 color='#3498DB')

    plt.xlabel('Dimension', fontsize=13)
    plt.ylabel('Score (0-10)', fontsize=13)
    plt.title('Child Labor (1800s) vs Algorithm Bias (2020s)\nSame Pattern, Different Century',
              fontsize=15, fontweight='bold')
    plt.xticks(x, dimensions, fontsize=11)
    plt.legend(fontsize=12, loc='upper right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.ylim(0, 11)

    # Insight annotations
    plt.annotate('AI bias is LESS\nvisible than\nchild labor was',
                 xy=(2 + width/2, ai_bias_scores[2]),
                 xytext=(3.5, 7),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=11, fontweight='bold', color='red')

    plt.annotate('Organized resistance\nstill nascent',
                 xy=(5 + width/2, ai_bias_scores[5]),
                 xytext=(4, 5),
                 arrowprops=dict(arrowstyle='->', color='orange', lw=2),
                 fontsize=11, fontweight='bold', color='orange')

    plt.tight_layout()
    plt.savefig('s3_12_comparison_basic.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Key pattern: exploitation thrives when invisible")
    print(f"  Child labor visibility: {child_labor_scores[2]}/10 vs AI bias: {ai_bias_scores[2]}/10")
    print(f"  Organized resistance: Child labor {child_labor_scores[5]}/10 vs AI bias: {ai_bias_scores[5]}/10")
    print(f"  -> History says: change requires making the invisible visible")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(For complete version with 12 sub-plots, see premium content)\n")

child_labor_basic()
facial_recognition_basic()
historical_comparison_basic()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print("\nGenerated plots:")
print("  1. s3_12_child_labor_basic.png - Child labor trends 1800-1900")
print("  2. s3_12_facial_recognition_basic.png - Facial recognition bias")
print("  3. s3_12_comparison_basic.png - Historical comparison overview")
print("\n[Premium Version Includes]")
print("  - Child labor time series with economic growth correlation (2 sub-plots)")
print("  - Regulation compliance: before/after Mines Act + regional enforcement (2 sub-plots)")
print("  - Algorithm bias: hiring + credit scoring + facial recognition (3 sub-plots)")
print("  - Vulnerable group impact: approval heatmap + economic loss (2 sub-plots)")
print("  - Fairness framework: metrics + radar chart + comparison table (3 sub-plots)")
print("  - Total: 12 professional sub-plots")
print("=" * 70)
