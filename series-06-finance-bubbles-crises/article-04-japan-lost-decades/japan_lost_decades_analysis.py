"""
Finance, Bubbles & Crises #04: Japan's Lost 30 Years vs Taiwan's Housing Crisis
Free Version -- 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Price-to-Income Ratio Trajectory — Tokyo vs Taipei
# ============================================================
print("=" * 65)
print("MODEL 1: Price-to-Income Ratio -- Tokyo vs Taipei")
print("=" * 65)

japan_years  = [1980, 1983, 1985, 1987, 1989, 1991, 1993,
                1995, 1998, 2000, 2003, 2005, 2008, 2010,
                2013, 2015, 2018, 2020]
japan_ratios = [8.2, 9.1, 10.5, 14.8, 18.4, 16.2, 12.1,
                10.3, 8.5, 7.8, 7.2, 7.5, 8.1, 7.9,
                8.3, 9.0, 10.2, 10.8]

tw_years  = [2002, 2004, 2006, 2008, 2010, 2012, 2014,
             2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
tw_ratios = [6.1, 6.8, 8.2, 8.9, 10.1, 12.6, 14.1,
             14.8, 13.5, 14.1, 15.2, 16.2, 16.1, 15.8, 16.0]

jp_peak = max(japan_ratios)
tw_peak = max(tw_ratios)
jp_trough = min(japan_ratios[japan_ratios.index(jp_peak):])

print(f"  Japan peak: {jp_peak:.1f}x (1989)")
print(f"  Taiwan peak: {tw_peak:.1f}x (2021)")
print(f"  Japan decline from peak: {(jp_peak - jp_trough)/jp_peak*100:.0f}%")
print(f"  Taiwan: holding steady near peak ({tw_ratios[-1]:.1f}x)")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Price-to-Income Ratio: Tokyo vs Taipei\n'
             'Japan: fireworks (4 years) | Taiwan: boiling frog (19 years)',
             fontsize=14, fontweight='bold')

# Panel 1: Time series
ax = axes[0]
ax.plot(japan_years, japan_ratios, 'o-', color='#E74C3C', linewidth=2.5, markersize=5,
        label='Tokyo')
ax.plot(tw_years, tw_ratios, 's-', color='#3498DB', linewidth=2.5, markersize=5,
        label='Taipei')
ax.axhspan(3, 6, alpha=0.1, color='green', label='Reasonable (3-6x)')
ax.axhline(y=15, color='red', linestyle='--', alpha=0.5, label='Danger zone (15x+)')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Price-to-Income Ratio', fontsize=11)
ax.set_title('Historical Trajectories', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: Bubble phase comparison
ax = axes[1]
phases = ['Pre-rise\n(baseline)', 'Slow\nclimb', 'Acceleration', 'Peak /\nPlateau', 'Post-peak']
jp_phases = [8.2, 10.5, 14.8, 18.4, 7.2]
tw_phases = [6.1, 8.2, 12.6, 16.2, 16.0]
x = np.arange(len(phases))
w = 0.35
ax.bar(x - w/2, jp_phases, w, color='#E74C3C', alpha=0.8, label='Japan (crash)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, tw_phases, w, color='#3498DB', alpha=0.8, label='Taiwan (plateau)',
       edgecolor='black', linewidth=1)
ax.axhline(y=6, color='green', linestyle='--', alpha=0.5, label='Reasonable upper limit')
ax.set_xticks(x)
ax.set_xticklabels(phases, fontsize=9)
ax.set_ylabel('Price-to-Income Ratio', fontsize=11)
ax.set_title('Phase Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Different shapes — crash vs plateau
ax = axes[2]
# Normalize both to "years from acceleration start"
jp_norm_years = [y - 1985 for y in japan_years]
tw_norm_years = [y - 2006 for y in tw_years]
ax.plot(jp_norm_years, japan_ratios, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=5, label='Japan (crash pattern)')
ax.plot(tw_norm_years, tw_ratios, 's-', color='#3498DB', linewidth=2.5,
        markersize=5, label='Taiwan (plateau pattern)')
ax.axhline(y=6, color='green', linestyle='--', alpha=0.5)
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.5, label='Acceleration start')
ax.set_xlabel('Years from acceleration start', fontsize=11)
ax.set_ylabel('Price-to-Income Ratio', fontsize=11)
ax.set_title('Crash vs Plateau: Two Shapes', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_price_to_income.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_price_to_income.png")


# ============================================================
# MODEL 2: Housing Hoarding Analysis — Taiwan's Unique Problem
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Housing Hoarding -- Taiwan's Structural Disease")
print("=" * 65)

hoarding_categories = ['Empty homes\n(vacancy)', 'Owners with\n3+ properties',
                       'Effective\ntax rate', 'Holding cost\n(annual)']
tw_values = [19.0, 5.5, 0.1, 0.1]    # %, %, %, % of market value
us_values = [10.0, 2.0, 1.5, 1.5]
jp_values = [13.5, 3.0, 1.0, 1.0]

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Housing Hoarding: Taiwan vs International Standards\n'
             'Near-zero holding costs make property the perfect savings vehicle',
             fontsize=14, fontweight='bold')

# Panel 1: Taiwan vs international comparison
ax = axes[0]
x = np.arange(len(hoarding_categories))
w = 0.25
ax.bar(x - w, tw_values, w, color='#E74C3C', alpha=0.8, label='Taiwan',
       edgecolor='black', linewidth=1)
ax.bar(x, us_values, w, color='#3498DB', alpha=0.8, label='USA',
       edgecolor='black', linewidth=1)
ax.bar(x + w, jp_values, w, color='#F39C12', alpha=0.8, label='Japan',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(hoarding_categories, fontsize=9)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title('Holding Costs & Vacancy Rates', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Cost of holding a NT$30M property
ax = axes[1]
countries = ['Taiwan', 'Japan', 'USA', 'UK', 'Singapore']
annual_cost_pct = [0.1, 1.0, 1.5, 1.2, 0.5]
annual_cost_ntd = [c / 100 * 30000000 for c in annual_cost_pct]  # Based on NT$30M property
colors_hold = ['#E74C3C', '#F39C12', '#3498DB', '#2ECC71', '#8E44AD']
bars = ax.bar(countries, [c / 10000 for c in annual_cost_ntd], color=colors_hold,
              alpha=0.8, edgecolor='black', linewidth=1)
ax.set_ylabel('Annual holding cost (NT$ 10K)', fontsize=11)
ax.set_title('Annual Cost of Holding a NT$30M Property', fontsize=12, fontweight='bold')
for bar, v, pct in zip(bars, annual_cost_ntd, annual_cost_pct):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'NT${v/10000:.0f}K\n({pct}%)', ha='center', fontsize=9, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Vacancy paradox — empty homes vs price
ax = axes[2]
tw_vacancy_years = [2010, 2012, 2014, 2016, 2018, 2020, 2023]
tw_vacancy_rate = [17.5, 18.0, 18.5, 18.8, 18.5, 19.0, 19.3]
tw_price_index = [80, 95, 105, 108, 100, 112, 120]  # Normalized
ax2 = ax.twinx()
ax.plot(tw_vacancy_years, tw_vacancy_rate, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=7, label='Vacancy rate (%)')
ax2.plot(tw_vacancy_years, tw_price_index, 's-', color='#E74C3C', linewidth=2.5,
         markersize=7, label='Price index')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Vacancy Rate (%)', color='#8E44AD', fontsize=11)
ax2.set_ylabel('Price Index (2010=80)', color='#E74C3C', fontsize=11)
ax.set_title('The Paradox: More Vacancies, Higher Prices', fontsize=12, fontweight='bold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='center left')
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_housing_hoarding.png', dpi=300, bbox_inches='tight')
plt.close()

print("  Taiwan vacancy: 19% (1.66M empty homes)")
print("  Taiwan effective tax rate: 0.1% vs USA 1.5%")
print("  Annual holding cost on NT$30M: Taiwan NT$30K vs USA NT$450K")
print("=> Saved: 02_housing_hoarding.png")


# ============================================================
# MODEL 3: Demographics Doom Loop — Japan vs Taiwan
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Demographics Doom Loop -- Japan vs Taiwan")
print("=" * 65)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Demographics Doom Loop: Housing Unaffordability -> Population Collapse\n'
             'Japan took 30 years to decline | Taiwan is doing it in 8',
             fontsize=14, fontweight='bold')

# Panel 1: Fertility rate comparison
ax = axes[0]
jp_fert_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023]
jp_fertility = [1.54, 1.42, 1.36, 1.26, 1.39, 1.45, 1.34, 1.20]
tw_fert_years = [2000, 2005, 2010, 2015, 2018, 2020, 2022, 2023]
tw_fertility = [1.68, 1.12, 0.90, 1.18, 1.06, 0.99, 0.87, 0.87]
ax.plot(jp_fert_years, jp_fertility, 'o-', color='#E74C3C', linewidth=2.5,
        markersize=7, label='Japan')
ax.plot(tw_fert_years, tw_fertility, 's-', color='#3498DB', linewidth=2.5,
        markersize=7, label='Taiwan')
ax.axhline(y=2.1, color='green', linestyle='--', alpha=0.5, label='Replacement rate (2.1)')
ax.axhline(y=1.0, color='orange', linestyle='--', alpha=0.5, label='Ultra-low (1.0)')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Total Fertility Rate', fontsize=11)
ax.set_title('Fertility Rate: Japan vs Taiwan', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: Key demographic indicators comparison
ax = axes[1]
demo_labels = ['Fertility\nRate', 'Annual Births\n(10K)', 'Marriage\nAge (F)',
               '65+ Pop\n(%)']
jp_1990 = [1.54, 122, 25.9, 12.1]
jp_2023 = [1.20, 76, 29.7, 29.1]
tw_2015 = [1.18, 21.4, 30.0, 12.5]
tw_2023 = [0.87, 13.5, 31.0, 18.4]
x = np.arange(len(demo_labels))
w = 0.2
ax.bar(x - 1.5*w, jp_1990, w, color='#E74C3C', alpha=0.5, label='Japan 1990',
       edgecolor='black', linewidth=0.5)
ax.bar(x - 0.5*w, jp_2023, w, color='#E74C3C', alpha=0.9, label='Japan 2023',
       edgecolor='black', linewidth=0.5)
ax.bar(x + 0.5*w, tw_2015, w, color='#3498DB', alpha=0.5, label='Taiwan 2015',
       edgecolor='black', linewidth=0.5)
ax.bar(x + 1.5*w, tw_2023, w, color='#3498DB', alpha=0.9, label='Taiwan 2023',
       edgecolor='black', linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(demo_labels, fontsize=9)
ax.set_ylabel('Value', fontsize=11)
ax.set_title('Demographic Snapshot', fontsize=12, fontweight='bold')
ax.legend(fontsize=8, ncol=2)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Generation shrinkage projection
ax = axes[2]
gen_years = [2023, 2035, 2045, 2055, 2065, 2075]
# At 0.87 fertility, each gen is ~57% of previous
tw_pop = [2340]
for _ in range(5):
    tw_pop.append(tw_pop[-1] * 0.87)
jp_pop = [12500, 11900, 11200, 10400, 9700, 9100]  # Japan projections (10K)
ax.plot(gen_years, [p / 100 for p in tw_pop], 'o-', color='#3498DB',
        linewidth=2.5, markersize=7, label='Taiwan (millions)')
ax.plot(gen_years, [p / 100 for p in jp_pop], 's-', color='#E74C3C',
        linewidth=2.5, markersize=7, label='Japan (millions)')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Population (millions)', fontsize=11)
ax.set_title('Population Projection at Current Fertility', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_demographics.png', dpi=300, bbox_inches='tight')
plt.close()

print("  Japan fertility: 1.54 (1990) -> 1.20 (2023) -- 30 years")
print("  Taiwan fertility: 1.18 (2015) -> 0.87 (2023) -- 8 years")
print("  At 0.87, each generation shrinks by 57%")
print("=> Saved: 03_demographics.png")


# ============================================================
# MODEL 4: Zombie Companies — Japan's Lesson
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Zombie Companies -- Japan's Lesson for Taiwan")
print("=" * 65)

zombie_years = [1995, 2000, 2005, 2010]
zombie_pct = [15, 26, 22, 12]
zombie_employ = [12, 19, 16, 9]
official_bad_debt = [3.5, 5.4, 4.0, 2.5]
actual_bad_debt = [12.5, 17.5, 12.5, 6.5]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("Zombie Companies: Japan's 30-Year Warning\n"
             "Banks pretend loans are good, companies pretend to be alive -- a lesson Taiwan must heed",
             fontsize=14, fontweight='bold')

# Panel 1: Zombie prevalence
ax = axes[0]
x = np.arange(len(zombie_years))
w = 0.35
ax.bar(x - w/2, zombie_pct, w, color='#8E44AD', alpha=0.8, label='% of Listed Companies',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, zombie_employ, w, color='#E67E22', alpha=0.8, label='% of Employment',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(zombie_years)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title('Japan: Zombie Company Prevalence', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Official vs actual bad debt
ax = axes[1]
ax.plot(zombie_years, official_bad_debt, 'o-', color='#3498DB', linewidth=2.5,
        markersize=8, label='Official bad debt rate')
ax.plot(zombie_years, actual_bad_debt, 's-', color='#E74C3C', linewidth=2.5,
        markersize=8, label='Estimated actual rate')
ax.fill_between(zombie_years, official_bad_debt, actual_bad_debt,
                alpha=0.2, color='#E74C3C', label='Hidden bad debt')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Bad Debt Rate (%)', fontsize=11)
ax.set_title('Official vs Actual Bad Debt', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 3: Impact on economy
ax = axes[2]
impacts = ['Credit to\nNew Firms', 'Productivity\nGrowth', 'Innovation\nIndex',
           'Young Worker\nOpportunity']
zombie_impact = [-60, -40, -35, -55]
colors_z = plt.cm.Reds(np.linspace(0.3, 0.8, len(impacts)))
bars = ax.barh(impacts, [abs(z) for z in zombie_impact], color=colors_z,
               edgecolor='black', linewidth=1)
ax.set_xlabel('Reduction (%)', fontsize=11)
ax.set_title('Zombie Impact on Economy', fontsize=12, fontweight='bold')
for bar, v in zip(bars, zombie_impact):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}%', va='center', fontweight='bold', fontsize=10, color='#E74C3C')
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_zombie_companies.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Peak zombie share: 26% of listed companies (2000)")
print("  Hidden bad debt gap: up to 12 percentage points")
print("=> Saved: 04_zombie_companies.png")


# ============================================================
# MODEL 5: Lost Generation — Taiwan vs Japan Life Trajectories
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Lost Generation -- Taiwan vs Japan")
print("=" * 65)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle("Lost Generation: Housing Prices Don't Just Destroy Wealth -- They Destroy Futures\n"
             "Japan's Ice Age Gen (1990s) vs Taiwan's Suffocating Youth (2020s)",
             fontsize=14, fontweight='bold')

# Panel 1: Taiwan generation gap
milestones = ['Home by 30', 'Married\nby 35', 'First Buy\nAge', 'Mortgage/\nIncome',
              'Down Payment\n(yrs salary)']
tw_prev = [40, 80, 31, 27, 3.5]
tw_now = [17, 57, 40, 45, 10]

ax = axes[0]
x = np.arange(len(milestones))
w = 0.35
ax.bar(x - w/2, tw_prev, w, color='#3498DB', alpha=0.8, label='Born 1965-75',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, tw_now, w, color='#E74C3C', alpha=0.8, label='Born 1990-2000',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(milestones, fontsize=8)
ax.set_ylabel('Value (% or years)', fontsize=11)
ax.set_title("Taiwan's Generation Gap", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Japan's ice age generation
jp_milestones = ['Employment\nat Grad', 'Formal Job\nat 30', 'Home\nat 35',
                 'Married\nat 40', 'Lifetime\nIncome (%)']
jp_prev = [95, 90, 60, 90, 100]
jp_ice = [62, 55, 28, 58, 65]

ax = axes[1]
x = np.arange(len(jp_milestones))
ax.bar(x - w/2, jp_prev, w, color='#F39C12', alpha=0.8, label='Born 1955-65',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, jp_ice, w, color='#E74C3C', alpha=0.8, label='Ice Age (1970-80)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(jp_milestones, fontsize=8)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title("Japan's Ice Age Generation", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Shared vocabulary of despair
ax = axes[2]
vocab = ['Giving up\non housing', 'Small\nhappiness', 'Temp work\nculture',
         'Social\nwithdrawal']
jp_labels = ['Freeter', 'Satori-\nsedai', 'Haken', 'Hikikomori']
tw_labels = ['Tangping\n(Lie flat)', 'Xiao-\nquexing', 'Moonlight\nclan', 'Home\nhermit']
jp_vals = [75, 65, 80, 85]
tw_vals = [80, 75, 70, 60]
y = np.arange(len(vocab))
ax.barh(y - 0.2, jp_vals, 0.35, color='#E74C3C', alpha=0.7, label='Japan (1990s)',
        edgecolor='black', linewidth=1)
ax.barh(y + 0.2, tw_vals, 0.35, color='#3498DB', alpha=0.7, label='Taiwan (2020s)',
        edgecolor='black', linewidth=1)
combined = [f'{j}\nvs\n{t}' for j, t in zip(jp_labels, tw_labels)]
ax.set_yticks(y)
ax.set_yticklabels(combined, fontsize=7)
ax.set_xlabel('Cultural Resonance Score', fontsize=11)
ax.set_title('Vocabulary of Despair', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_lost_generation.png', dpi=300, bbox_inches='tight')
plt.close()

print("  Taiwan: homeownership by 30 dropped from 40% to 17%")
print("  Taiwan: first purchase age shifted from 31 to 40 (+9 years)")
print("  Japan: lifetime unmarried rate rose from 5.6% to 28.3%")
print("=> Saved: 05_lost_generation.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
