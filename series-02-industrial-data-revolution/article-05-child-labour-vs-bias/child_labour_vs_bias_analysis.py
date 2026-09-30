"""
Child Labor vs AI Bias - Free Version
Series 2 (Industrial Revolution meets Data Revolution), Article 05: Basic Visualizations

Author: Wina Wu
Date: 2025-12 (data notes and labels updated 2026-09 to match the fact-checked article)

This free version includes:
- Basic child labor trends chart
- Simple facial recognition bias comparison
- Basic historical comparison overview

The Deep Dive Pack adds 5 multi-panel figure files (12 sub-plots in total).

DATA NOTES (please read before quoting any number from this script):
- Child labor series (Visualization 1): ILLUSTRATIVE reconstruction. The values are
  hand-set to demonstrate the mechanism; they are NOT an official dataset and were
  not matched to primary sources. They are also not the same table as the code
  block printed in the article (which is an illustrative reconstruction too).
- Facial recognition (Visualization 2): only the two extremes, 0.8% and 34.7%, are
  figures reported by Buolamwini & Gebru (2018), "Gender Shades", Proceedings of
  Machine Learning Research 81. The two middle values (7.1%, 12.0%) are widely
  repeated secondary estimates that could not be verified against the paper.
- Historical comparison (Visualization 3): hand-set illustrative scores on a 0-10
  scale. They are a subjective structuring device, not measurements.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Child Labor vs AI Bias - Free Version")
print("Series 2, Article 05")
print("=" * 70)
print()

# ============================================================================
# Visualization 1: Child Labor Trends (Basic)
# ============================================================================

def child_labor_basic():
    """Basic child labor trends 1800-1900 (illustrative reconstruction)"""
    print("\n[Visualization 1] Child Labor Trends (1800-1900) - illustrative data")
    print("-" * 70)

    # ILLUSTRATIVE reconstruction, not an official dataset: hand-set rates (%) per
    # industry, chosen to demonstrate the rise-and-fall mechanism. They have not been
    # matched to primary sources, so do not quote them as historical statistics.
    years = [1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900]
    child_labor_pct = {
        'Textiles': [25, 30, 35, 38, 35, 28, 20, 15, 10, 7, 5],
        'Mining': [15, 18, 22, 25, 20, 12, 8, 5, 3, 2, 1],
        'Chimney': [10, 12, 14, 15, 10, 5, 3, 1, 0.5, 0, 0],
        'Other': [20, 22, 25, 28, 25, 20, 15, 12, 8, 5, 3]
    }

    # Simple average of the four illustrative series. The industry rates are not
    # additive, so summing them would not give a rate (it could exceed 100%).
    avg_rate = [sum(child_labor_pct[ind][i] for ind in child_labor_pct) / len(child_labor_pct)
                for i in range(len(years))]

    colors = {'Textiles': '#E74C3C', 'Mining': '#8B4513', 'Chimney': '#2C3E50', 'Other': '#F39C12'}

    plt.figure(figsize=(14, 8))

    for industry, rates in child_labor_pct.items():
        plt.plot(years, rates, '-o', linewidth=2.5, markersize=7,
                 color=colors[industry], label=industry, alpha=0.8)

    plt.plot(years, avg_rate, 'k--', linewidth=3, markersize=9, label='Average of 4 series',
             alpha=0.6, marker='D')

    y_top = max(max(rates) for rates in child_labor_pct.values()) * 1.3
    plt.ylim(-2, y_top)

    # Key legislation markers
    legislation = {1833: 'Factory Act', 1842: 'Mines Act', 1878: 'Factory &\nWorkshop Act'}
    for year, name in legislation.items():
        plt.axvline(x=year, color='green', linestyle='--', alpha=0.5, linewidth=1.5)
        plt.text(year + 1, y_top * 0.95, name, fontsize=9, color='darkgreen',
                 fontweight='bold', rotation=0, va='top')

    plt.xlabel('Year', fontsize=13)
    plt.ylabel('Child Labor Rate (%, illustrative)', fontsize=13)
    plt.title('Child Labor Rates in Britain (1800-1900)\n'
              'Illustrative reconstruction, not an official dataset',
              fontsize=15, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(1795, 1905)

    # Annotate peak of the average series
    peak_idx = int(np.argmax(avg_rate))
    plt.annotate(f'Peak of average: {avg_rate[peak_idx]:.1f}%\n({years[peak_idx]})',
                 xy=(years[peak_idx], avg_rate[peak_idx]),
                 xytext=(years[0] + 5, y_top * 0.85),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=12, fontweight='bold', color='red')

    plt.tight_layout()
    plt.savefig('child_labor.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Peak of the average illustrative rate: {years[peak_idx]} ({avg_rate[peak_idx]:.1f}%)")
    print(f"  By 1900: {avg_rate[-1]:.1f}% (down from {avg_rate[0]:.1f}% in 1800)")
    print(f"  Textiles has the highest illustrative rate, peaking at {max(child_labor_pct['Textiles'])}%")
    print("  (Hand-set illustrative values, not an official dataset)")

# ============================================================================
# Visualization 2: Facial Recognition Bias (Simple)
# ============================================================================

def facial_recognition_basic():
    """Simple facial recognition error rate comparison"""
    print("\n[Visualization 2] Facial Recognition Bias")
    print("-" * 70)

    # Group labels follow the simplified wording used in the article. The original
    # study (Buolamwini & Gebru, 2018, "Gender Shades", PMLR 81) grouped subjects by
    # skin type (Fitzpatrick scale), not by race.
    demographics = ['White\nMale', 'White\nFemale', 'Black\nMale', 'Black\nFemale']
    # Error rates (%). Verified: 0.8 (white men) and 34.7 (Black women) are the two
    # extremes reported by the study. Not verified: 7.1 and 12.0 are widely repeated
    # secondary estimates that could not be matched to the paper.
    error_rates = [0.8, 7.1, 12.0, 34.7]
    verified = [True, False, False, True]

    colors = ['#27AE60', '#2ECC71', '#E67E22', '#E74C3C']

    plt.figure(figsize=(12, 8))
    bars = plt.bar(demographics, error_rates, color=colors, alpha=0.85,
                   edgecolor='white', linewidth=2)

    # Hatch the bars whose values are secondary estimates
    for bar, is_verified in zip(bars, verified):
        if not is_verified:
            bar.set_hatch('//')

    # Add value labels
    for bar, val in zip(bars, error_rates):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.8,
                 f'{val}%', ha='center', va='bottom', fontsize=13, fontweight='bold')

    # Illustrative reference line (not a regulatory or scientific standard)
    plt.axhline(y=5.0, color='green', linestyle='--', alpha=0.7, linewidth=2,
                label='Illustrative 5% reference line (not a standard)')

    # Highlight disparity between the two verified extremes
    ratio = error_rates[3] / error_rates[0]
    plt.annotate(f'{ratio:.0f}x higher\nthan White Male',
                 xy=(3, error_rates[3]),
                 xytext=(1.6, 30),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
                 fontsize=13, fontweight='bold', color='red')

    plt.xlabel('Demographic Group', fontsize=13)
    plt.ylabel('Error Rate (%)', fontsize=13)
    plt.title(f'Facial Recognition Error Rates by Demographics\n'
              f'Black Women: {ratio:.0f}x the Error Rate of White Men (0.8% vs 34.7%)',
              fontsize=15, fontweight='bold')
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, alpha=0.3, axis='y')

    plt.figtext(0.5, 0.005,
                'Solid bars (0.8%, 34.7%): the two extremes reported by Buolamwini & Gebru (2018).\n'
                'Hatched bars (7.1%, 12.0%): widely repeated secondary estimates, not verified against the paper.\n'
                'The study grouped subjects by skin type (Fitzpatrick scale), not by race.',
                ha='center', va='bottom', fontsize=10, color='dimgray')

    plt.tight_layout(rect=[0, 0.08, 1, 1])
    plt.savefig('facial_recognition_bias.png', dpi=300, bbox_inches='tight')
    plt.show()

    disparity = error_rates[3] / error_rates[0]
    print(f"\n  Lowest error rate: White Male ({error_rates[0]}%)")
    print(f"  Highest error rate: Black Female ({error_rates[3]}%)")
    print(f"  Disparity ratio: {disparity:.0f}x")
    print(f"  Groups above the illustrative 5% line: {sum(1 for r in error_rates if r > 5)}/{len(error_rates)}")
    print("  (0.8% and 34.7% are the study's extremes; 7.1% and 12.0% are unverified secondary estimates)")

# ============================================================================
# Visualization 3: Historical Comparison Overview
# ============================================================================

def historical_comparison_basic():
    """Basic comparison between child labor and AI bias (illustrative scores)"""
    print("\n[Visualization 3] Historical Comparison: Then vs Now - illustrative scores")
    print("-" * 70)

    # Hand-set illustrative scores on a 0-10 scale. They are a subjective way to
    # structure the comparison, NOT measurements and NOT derived from any dataset.
    dimensions = ['Victim\nCount', 'Economic\nImpact', 'Visibility', 'Public\nAwareness',
                  'Legal\nResponse', 'Organized\nResistance']
    child_labor_scores = [9, 7, 9, 6, 7, 8]  # 1800s child labor (illustrative)
    ai_bias_scores = [8, 9, 2, 4, 3, 2]  # 2020s AI bias (illustrative)

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
    plt.ylabel('Illustrative score (0-10)', fontsize=13)
    plt.title('Child Labor (1800s) vs Algorithm Bias (2020s)\n'
              'Same Pattern, Different Century (hand-set illustrative scores, not measurements)',
              fontsize=15, fontweight='bold')
    plt.xticks(x, dimensions, fontsize=11)
    plt.legend(fontsize=12, loc='upper right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.ylim(0, 11)

    # Insight annotations
    plt.annotate('AI bias is LESS\nvisible than\nchild labor was',
                 xy=(2 + width/2, ai_bias_scores[2]),
                 xytext=(3.1, 9.0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=11, fontweight='bold', color='red')

    plt.annotate('Organized resistance\nstill nascent',
                 xy=(5 + width/2, ai_bias_scores[5]),
                 xytext=(4, 5),
                 arrowprops=dict(arrowstyle='->', color='orange', lw=2),
                 fontsize=11, fontweight='bold', color='orange')

    plt.tight_layout()
    plt.savefig('historical_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\n  Key pattern (in these illustrative scores): exploitation thrives when invisible")
    print(f"  Child labor visibility: {child_labor_scores[2]}/10 vs AI bias: {ai_bias_scores[2]}/10")
    print(f"  Organized resistance: Child labor {child_labor_scores[5]}/10 vs AI bias: {ai_bias_scores[5]}/10")
    print(f"  -> History says: change requires making the invisible visible")

# ============================================================================
# Execute All Visualizations
# ============================================================================

print("\nGenerating visualizations...")
print("(The Deep Dive Pack has 5 multi-panel figure files with 12 sub-plots in total)\n")

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
print("  1. child_labor.png - Child labor trends 1800-1900 (illustrative data)")
print("  2. facial_recognition_bias.png - Facial recognition bias")
print("  3. historical_comparison.png - Historical comparison overview (illustrative scores)")
print("\n[Deep Dive Pack Includes]")
print("  - Child labor time series with economic growth correlation (2 sub-plots)")
print("  - Regulation compliance: before/after Mines Act + regional enforcement (2 sub-plots)")
print("  - Algorithm bias: hiring + credit scoring + facial recognition (3 sub-plots)")
print("  - Vulnerable group impact: approval heatmap + economic loss (2 sub-plots)")
print("  - Fairness framework: metrics + radar chart + comparison table (3 sub-plots)")
print("  - Total: 5 multi-panel figure files containing 12 sub-plots")
print("=" * 70)
