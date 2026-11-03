"""
Alienation Mathematics - Free Version
Series 2 (Industrial Revolution Meets the Data Revolution), Article 03: Sample Visualizations

Author: Wina Wu
Date: 2025-12 (revised 2026-09 to match the fact-checked article)

NOTE ON THE DATA
Every input in this script is an illustrative setting chosen by the author to show how
the model works. None of it is measured, survey or historical data.
- The 0-1 worker profiles (ownership, autonomy, creativity, social connection) and the
  autonomy-dimension scores are hand-set. They were set so that the formulas below
  reproduce the values in the article's illustrative table: alienation index
  Artisan 0.19 / Factory worker 0.75 / Gig worker 0.69, and autonomy index
  Gig worker 0.30 vs Factory worker 0.11.
- Read every printed number as "in this model", not as a historical fact.

This free version includes:
- Alienation Index Era Comparison (1 sub-plot): bar chart of alienation scores for three eras
- Alienation Trend Across Eras (1 sub-plot): index by representative worker type, 1800-2024
- Gig vs Factory Autonomy (1 sub-plot): four-dimension autonomy index and its gap
Total: 3 sample sub-plots

For the full 14 sub-plots including heatmaps, sentiment analysis (NLP demos on
simulated data), radar charts, and algorithm alienation deep dive, see the premium version.

Requirements:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# 'DejaVu Sans' ships with matplotlib and is the fallback if the other fonts are missing
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("Alienation Mathematics - Free Sample Version")
print("Series 2 - Article 03")
print("=" * 70)
print("Note: all inputs are illustrative settings, not measured data.")
print()


# ============================================================================
# Model: alienation index (same model as in the article)
# ============================================================================

class AlienationModel:
    """
    Mathematical model of Marx's alienation theory.
    Alienation = f(ownership, autonomy, creativity, social_connection)
    Each dimension is scored 0-1 (0 = total alienation, 1 = no alienation).
    Alienation index = 1 - weighted sum of the four scores.
    """

    def __init__(self):
        self.weights = {
            'ownership': 0.30,          # Product ownership
            'autonomy': 0.25,           # Labor autonomy
            'creativity': 0.25,         # Creative engagement
            'social_connection': 0.20,  # Social bonds
        }

    def calculate_alienation(self, ownership, autonomy, creativity, social_connection):
        weighted_sum = (
            self.weights['ownership'] * ownership +
            self.weights['autonomy'] * autonomy +
            self.weights['creativity'] * creativity +
            self.weights['social_connection'] * social_connection
        )
        return 1 - weighted_sum  # Alienation index: 1 - positive indicators


# ILLUSTRATIVE worker profiles (hand-set by the author, NOT measured data).
# The scores were chosen so that the formula reproduces the article's illustrative
# table (Artisan 0.19, Factory worker 0.75, Gig worker 0.69). The article does not
# publish the inputs behind its table, so these are this script's own settings.
# The 'autonomy' input here is the *apparent* autonomy of the job (what the worker
# can see); it is a different quantity from the four-dimension autonomy index in Plot 3.
PROFILES = {
    'Artisan (1800)': dict(ownership=0.90, autonomy=0.85, creativity=0.75, social_connection=0.70),
    'Factory Worker (1900)': dict(ownership=0.10, autonomy=0.20, creativity=0.20, social_connection=0.60),
    'Gig Worker (2024)': dict(ownership=0.10, autonomy=0.50, creativity=0.30, social_connection=0.40),
}

model = AlienationModel()
SCORES = {name: model.calculate_alienation(**p) for name, p in PROFILES.items()}
ARTISAN = SCORES['Artisan (1800)']
FACTORY = SCORES['Factory Worker (1900)']
GIG = SCORES['Gig Worker (2024)']


# ============================================================================
# Plot 1: Alienation Index Era Comparison (1 sub-plot)
# ============================================================================

def alienation_era_comparison():
    """
    Bar chart comparing the alienation index of three illustrative worker profiles.
    Formula: alienation = 1.0 - 0.3*ownership - 0.25*autonomy
                                - 0.25*creativity - 0.2*social_connection
    """
    print("\n[Plot 1] Alienation Index Era Comparison (illustrative profiles)")
    print("-" * 70)

    eras = ['Artisan\n(1800)', 'Factory Worker\n(1900)', 'Gig Worker\n(2024)']
    alienation_scores = [ARTISAN, FACTORY, GIG]
    colors = ['#2E86AB', '#A23B72', '#F18F01']

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(eras, alienation_scores, color=colors, alpha=0.85,
                  edgecolor='white', linewidth=2, width=0.55)

    for bar, score in zip(bars, alienation_scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{score:.2f}', ha='center', va='bottom', fontsize=16, fontweight='bold')

    ax.set_ylabel('Alienation Index (0 = none, 1 = total)', fontsize=12)
    ax.set_title('Alienation Index Across Eras (illustrative profiles, not measured data)\n'
                 'alienation = 1.0 - 0.3×ownership - 0.25×autonomy - 0.25×creativity - 0.2×social',
                 fontsize=13, fontweight='bold')
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5,
               label='Reference line at 0.5 (arbitrary midpoint)')
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)

    # Add context table below bars (the hand-set inputs; 100% = no alienation on that dimension)
    def pct(name, key):
        return f"{PROFILES[name][key] * 100:.0f}%"

    names = list(PROFILES.keys())
    table_data = [
        ['Product Ownership'] + [pct(n, 'ownership') for n in names],
        ['Work Autonomy (apparent)'] + [pct(n, 'autonomy') for n in names],
        ['Creativity'] + [pct(n, 'creativity') for n in names],
        ['Social Connection'] + [pct(n, 'social_connection') for n in names],
    ]
    table = ax.table(cellText=table_data,
                     colLabels=['Input (illustrative)', 'Artisan', 'Factory', 'Gig Worker'],
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
    plt.savefig('alienation_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  - Artisan (1800): {ARTISAN:.2f} (pre-industrial baseline)")
    print(f"  - Factory worker (1900): {FACTORY:.2f} (industrial-era factory work)")
    print(f"  - Gig worker (2024): {GIG:.2f} (approaches the factory level, {FACTORY - GIG:.2f} below it)")


# ============================================================================
# Plot 2: Alienation Trend Across Eras (1 sub-plot)
# ============================================================================

def historical_alienation_trend():
    """
    Alienation index of one representative worker type per era, 1800-2024.
    Three points are computed by the model above; two are the article's table values
    (their input profiles are not part of this script). No values are interpolated.
    """
    print("\n[Plot 2] Alienation Trend Across Eras (representative worker types)")
    print("-" * 70)

    # (year, label, index, computed_here)
    points = [
        (1800, 'Artisan', ARTISAN, True),
        (1900, 'Factory worker', FACTORY, True),
        # Office worker (1960) and knowledge worker (2000): values taken from the
        # article's illustrative table; this script has no input profiles for them.
        (1960, 'Office worker', 0.58, False),
        (2000, 'Knowledge worker', 0.45, False),
        (2024, 'Gig worker', GIG, True),
    ]
    years = [p[0] for p in points]
    values = [p[2] for p in points]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(years, values, '-', color='#E63946', linewidth=2.5, alpha=0.8, zorder=2)
    ax.fill_between(years, values, alpha=0.12, color='#E63946')

    computed = [p for p in points if p[3]]
    from_table = [p for p in points if not p[3]]
    ax.scatter([p[0] for p in computed], [p[2] for p in computed], s=110, zorder=3,
               facecolor='#E63946', edgecolor='#E63946', linewidth=2.5,
               label='Computed by this script (illustrative profiles)')
    ax.scatter([p[0] for p in from_table], [p[2] for p in from_table], s=110, zorder=3,
               facecolor='white', edgecolor='#E63946', linewidth=2.5,
               label="Value from the article's table (inputs not in this script)")

    peak_year = years[int(np.argmax(values))]
    # Vertical label offsets (points) chosen so the annotation boxes do not overlap
    label_offsets = {1800: 28, 1900: -55, 1960: 28, 2000: -50, 2024: 32}
    for year, label, value, _ in points:
        note = f'{year}: {label}\n{value:.2f}'
        if year == peak_year:
            note += '\n(highest of the five)'
        offset_y = label_offsets[year]
        ax.annotate(note, xy=(year, value),
                    xytext=(0, offset_y), textcoords='offset points',
                    ha='center', fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.9))

    ax.set_xlabel('Year (representative worker type of the era)', fontsize=12)
    ax.set_ylabel('Alienation Index', fontsize=12)
    ax.set_title('Alienation Index Across Eras, 1800-2024\n'
                 'Illustrative model output, not measured data',
                 fontsize=13, fontweight='bold')
    ax.set_xlim(1770, 2050)
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.5, color='orange', linestyle='--', alpha=0.5,
               label='Reference line at 0.5 (arbitrary midpoint)')
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig('alienation_trend.png', dpi=150, bbox_inches='tight')
    plt.show()

    for year, label, value, computed_here in points:
        source = 'computed here' if computed_here else "article table value"
        print(f"  - {year} {label}: {value:.2f} ({source})")
    peak = points[int(np.argmax(values))]
    print(f"  - Highest of the five: {peak[1]} ({peak[0]}) at {peak[2]:.2f}; "
          f"the gig worker ({GIG:.2f}) is {peak[2] - GIG:.2f} below it")


# ============================================================================
# Plot 3: Gig vs Factory Autonomy (1 sub-plot)
# ============================================================================

def gig_vs_factory_autonomy():
    """
    Four-dimension labor autonomy index for a gig worker and a factory worker.
    The gig worker looks freer on paper, but the freedom sits in the one dimension
    you can see (time control); the rules of the work stay hidden.
    """
    print("\n[Plot 3] Gig vs Factory Autonomy (illustrative scores)")
    print("-" * 70)

    dim_keys = ['time', 'decision', 'method', 'transparency']
    dim_labels = ['Time\nControl', 'Decision\nAuthority', 'Method\nChoice', 'Information\nTransparency']

    # Weights of the composite index: this script's own choice. The article does not
    # publish its weights; these were set so the composite reproduces its 0.30 and 0.11.
    weights = {'decision': 0.40, 'time': 0.25, 'method': 0.20, 'transparency': 0.15}

    # Gig worker: the four scores published in the article (0-1).
    gig = {'time': 0.70, 'decision': 0.20, 'method': 0.15, 'transparency': 0.10}
    # Factory worker: ILLUSTRATIVE scores set by the author. The article only gives the
    # composite (0.11); the split below is this script's assumption (fixed shifts, tight
    # methods, but known rules and a visible foreman).
    factory = {'time': 0.10, 'decision': 0.05, 'method': 0.10, 'transparency': 0.30}

    def autonomy_index(scores):
        return sum(weights[k] * scores[k] for k in dim_keys)

    gig_index = autonomy_index(gig)
    factory_index = autonomy_index(factory)

    gig_vals = [gig[k] for k in dim_keys]
    factory_vals = [factory[k] for k in dim_keys]

    x = np.arange(len(dim_keys))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))
    bars_gig = ax.bar(x - width/2, gig_vals, width,
                      label='Gig worker (2024)',
                      color='#F4A261', alpha=0.85, edgecolor='white', linewidth=1.5)
    bars_fac = ax.bar(x + width/2, factory_vals, width,
                      label='Factory worker (1900), illustrative scores',
                      color='#A23B72', alpha=0.85, edgecolor='white', linewidth=1.5)

    for bars in (bars_gig, bars_fac):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.015, f'{h:.2f}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='#264653')

    # Shade the one dimension where the gig worker looks free
    ax.axvspan(-0.5, 0.5, color='#fff3cd', alpha=0.5, zorder=0)
    ax.text(0, 0.93, 'the freedom you can see', ha='center', va='center', fontsize=9,
            style='italic', color='#7a5c00')
    ax.text(2, 0.93, 'the constraints you cannot see', ha='center', va='center', fontsize=9,
            style='italic', color='#7a5c00')

    ax.set_xlabel('Autonomy Dimension', fontsize=12)
    ax.set_ylabel('Autonomy Score (0 = none, 1 = full)', fontsize=12)
    ax.set_title('Gig Worker vs Factory Worker Autonomy (illustrative, not measured data)\n'
                 '"Be your own boss" - visible freedom vs hidden constraints',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dim_labels, fontsize=10)
    ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.0, 0.88))
    ax.set_ylim(0, 1.0)
    ax.grid(axis='y', alpha=0.3)

    # Summary text box
    summary = ('Autonomy Index = 0.40×decision + 0.25×time + 0.20×method + 0.15×transparency\n'
               f'Gig worker: {gig_index:.2f}  |  Factory worker: {factory_index:.2f}  '
               '(looks freer on paper)')
    ax.text(0.63, 0.58, summary, transform=ax.transAxes, fontsize=10,
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3cd', alpha=0.9))

    plt.tight_layout()
    plt.savefig('autonomy_gap.png', dpi=150, bbox_inches='tight')
    plt.show()

    diffs = {k: gig[k] - factory[k] for k in dim_keys}
    widest = max(diffs, key=lambda k: diffs[k])
    lower = [k for k in dim_keys if diffs[k] < 0]
    names = {'time': 'Time control', 'decision': 'Decision authority',
             'method': 'Method choice', 'transparency': 'Information transparency'}
    print("  Autonomy index (0.40*decision + 0.25*time + 0.20*method + 0.15*transparency):")
    print(f"  - Gig worker: {gig_index:.2f} | Factory worker: {factory_index:.2f} "
          "(the gig worker looks freer on paper)")
    print(f"  - Widest gap in the gig worker's favor: {names[widest]} "
          f"({gig[widest]:.2f} vs {factory[widest]:.2f})")
    for k in lower:
        print(f"  - The gig worker scores lower than the factory worker on {names[k].lower()} "
              f"({gig[k]:.2f} vs {factory[k]:.2f}): the rules stay hidden")
    print("  - 'Be your own boss' masks algorithmic control of the parts you cannot see")


# ============================================================================
# Execute All Plots
# ============================================================================

alienation_era_comparison()
historical_alienation_trend()
gig_vs_factory_autonomy()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("Free Sample Version Finished!")
print("=" * 70)
print()
print("Generated files:")
print("  1. alienation_comparison.png  (1 sub-plot)")
print("  2. alienation_trend.png       (1 sub-plot)")
print("  3. autonomy_gap.png           (1 sub-plot)")
print("  Total: 3 sample sub-plots")
print()
print("  [Premium Version Includes] 14 sub-plots, among them:")
print("  - Alienation heatmap across all dimensions")
print("  - Worker diary sentiment analysis (NLP demo on simulated data)")
print("  - Gig worker social media sentiment & word frequency (simulated data)")
print("  - Labor autonomy radar chart (artisan vs factory vs gig worker)")
print("  - Algorithm alienation deep dive (creators & consumers)")
print("=" * 70)
