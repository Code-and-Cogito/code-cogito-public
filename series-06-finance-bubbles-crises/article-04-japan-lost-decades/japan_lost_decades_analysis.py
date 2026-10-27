"""
Finance, Bubbles & Crises #04: Japan's Lost 30 Years vs Taiwan's Housing Crisis
Free Version -- 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install matplotlib numpy

DATA NOTES -- read before quoting any number
  Real-world reference figures (each one is cited again in a comment where it is used):
    - Taiwan 2020 census: about 1.66 million vacant homes = 18.5% of the stock (includes
      occasionally used homes and unsold new units). Ministry of the Interior (MOI) narrower
      "low-use (electricity)" definition: about 910,000 homes = 9.8% (H2 2024).
    - Taiwan Ministry of Finance (MOF), 2025: 41,188 people hold 3+ non-owner-occupied homes
      (about 6.9% of the roughly 599,000 people who hold non-owner-occupied homes).
    - Births: Japan 2023 727,277 (MHLW); Taiwan 2015 213,093 and 2023 133,895 (MOI, by date of birth).
    - Taiwan population: National Development Council (NDC) 2024 projection, medium scenario,
      about 23.4 million (2024) -> about 15.0 million (2070).
    - Zombie firms: Caballero, Hoshi & Kashyap (AER, 2008); Japan FSA major-bank NPL ratios.
    - US average effective property-tax rate: about 0.9% (about 0.3-2% by state).
  Everything else is a hand-set ILLUSTRATIVE input, not an official series: the price-to-income
  series, the Taiwan tax / holding-cost estimate, the US / Japan / UK / Singapore comparison bars
  (except the US tax rate), the vacancy-vs-price path, the Japan population path, the zombie and
  bad-debt tables, the life-milestone estimates and the "cultural resonance" scores.
  The charts mark these inputs as "illustrative" (hatched bars or labels).
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Price-to-Income Ratio Trajectory — Tokyo vs Taipei
# ============================================================
print("=" * 65)
print("MODEL 1: Price-to-Income Ratio -- Tokyo vs Taipei (illustrative series)")
print("=" * 65)

# Illustrative, hand-set values scaled to published Tokyo-area new-condo and Taiwan MOI (Taipei)
# price-to-income figures. NOT an official year-by-year series.
# For reference, MOI Q3 2024: Taipei 16.6x, New Taipei 14.0x, nationwide 10.8x
# (median home price / median household disposable income).
japan_years  = [1980, 1983, 1985, 1987, 1989, 1991, 1993,
                1995, 1998, 2000, 2003, 2005, 2008, 2010,
                2013, 2015, 2018, 2020]
# Japan: Tokyo (illustrative values)
japan_ratios = [8.2, 9.1, 10.5, 14.8, 18.4, 16.2, 12.1,
                10.3, 8.5, 7.8, 7.2, 7.5, 8.1, 7.9,
                8.3, 9.0, 10.2, 10.8]

tw_years  = [2002, 2004, 2006, 2008, 2010, 2012, 2014,
             2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# Taiwan: Taipei (illustrative values; MOI figures are only an order-of-magnitude reference)
tw_ratios = [6.1, 6.8, 8.2, 8.9, 10.1, 12.6, 14.1,
             14.8, 13.5, 14.1, 15.2, 16.2, 16.1, 15.8, 16.0]

jp_peak = max(japan_ratios)
jp_peak_yr = japan_years[japan_ratios.index(jp_peak)]
tw_peak = max(tw_ratios)
tw_peak_yr = tw_years[tw_ratios.index(tw_peak)]
jp_trough = min(japan_ratios[japan_ratios.index(jp_peak):])

print(f"  Japan peak: {jp_peak:.1f}x ({jp_peak_yr})")
print(f"  Taiwan peak: {tw_peak:.1f}x ({tw_peak_yr})")
print(f"  Japan decline from peak: {(jp_peak - jp_trough)/jp_peak*100:.0f}%")
print(f"  Taiwan: holding steady near peak ({tw_ratios[-1]:.1f}x)")
print("  Rule of thumb (not an official standard): 3-6x | Warning: 10x | Danger: 15x+ (author thresholds)")
print("  Note: hand-set illustrative series, not official data")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Price-to-Income Ratio: Tokyo vs Taipei (illustrative series)\n'
             'Japan: fireworks (4 years) | Taiwan: boiling frog (19 years)',
             fontsize=14, fontweight='bold')

# Panel 1: Time series
ax = axes[0]
ax.plot(japan_years, japan_ratios, 'o-', color='#E74C3C', linewidth=2.5, markersize=5,
        label='Tokyo')
ax.plot(tw_years, tw_ratios, 's-', color='#3498DB', linewidth=2.5, markersize=5,
        label='Taipei')
ax.axhspan(3, 6, alpha=0.1, color='green', label='Rule of thumb (3-6x)')
ax.axhline(y=15, color='red', linestyle='--', alpha=0.5, label='Danger zone (15x+, author threshold)')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Price-to-Income Ratio', fontsize=11)
ax.set_title('Trajectories (illustrative, hand-set)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: Bubble phase comparison
ax = axes[1]
phases = ['Pre-rise\n(baseline)', 'Slow\nclimb', 'Acceleration', 'Peak /\nPlateau', 'Post-peak']
# Japan: 1980, 1985, 1987, 1989 (peak), 2003 (trough); Taiwan: 2002, 2006, 2012, 2021 (peak), 2024
jp_phases = [8.2, 10.5, 14.8, 18.4, 7.2]
tw_phases = [6.1, 8.2, 12.6, 16.2, 16.0]
x = np.arange(len(phases))
w = 0.35
ax.bar(x - w/2, jp_phases, w, color='#E74C3C', alpha=0.8, label='Japan (crash)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, tw_phases, w, color='#3498DB', alpha=0.8, label='Taiwan (plateau)',
       edgecolor='black', linewidth=1)
ax.axhline(y=6, color='green', linestyle='--', alpha=0.5, label='Rule of thumb upper end (6x)')
ax.set_xticks(x)
ax.set_xticklabels(phases, fontsize=9)
ax.set_ylabel('Price-to-Income Ratio', fontsize=11)
ax.set_title('Phase Comparison (illustrative)', fontsize=12, fontweight='bold')
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
ax.set_title('Crash vs Plateau: Two Shapes (illustrative)', fontsize=12, fontweight='bold')
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

# --- Real-world reference figures (Taiwan) ---
# Vacancy: 2020 Population & Housing Census, about 1.66 million vacant homes = 18.5% of the stock
#   (includes occasionally used homes and unsold new units).
# MOI narrower "low-use (electricity)" definition: about 910,000 homes = 9.8% (H2 2024).
# 3+ holders: MOF 2025, 41,188 people hold 3+ non-owner-occupied homes; the denominator is the
#   roughly 599,000 people who hold non-owner-occupied homes (about 6.9%).
TW_VACANCY_PCT = 18.5
TW_VACANT_HOMES_M = 1.66
TW_LOW_USE_HOMES_K = 910
TW_LOW_USE_PCT = 9.8
TW_HOLDERS_3PLUS = 41_188
TW_HOLDERS_NONOWNER = 599_000
tw_3plus_pct = round(TW_HOLDERS_3PLUS / TW_HOLDERS_NONOWNER * 100, 1)

# --- Tax / holding cost ---
# Taiwan 0.1% of market value = AUTHOR'S ROUGH ESTIMATE for a self-use home (house tax is levied on
#   assessed value, which is well below market value; land value tax is extra).
# USA 0.9% = average effective property-tax rate (about 0.3-2% depending on the state).
# All other US / Japan / UK / Singapore numbers are hand-set ILLUSTRATIVE values.
# The US / Japan "3+ properties" share is not comparable with Taiwan's MOF definition, so it is NaN.
hoarding_categories = ['Vacant homes\n(% of stock)', '3+ non-owner-\noccupied homes\n(% of holders)',
                       'Effective\ntax rate', 'Holding cost\n(annual)']
tw_values = [TW_VACANCY_PCT, tw_3plus_pct, 0.1, 0.1]    # %, %, %, % of market value
us_values = [10.0, np.nan, 0.9, 0.9]
jp_values = [13.5, np.nan, 1.0, 1.0]
# True = sourced figure; False = illustrative value or author estimate (drawn hatched)
tw_sourced = [True, True, False, False]
us_sourced = [False, False, True, True]
jp_sourced = [False, False, False, False]


def hatch_unsourced(bars, sourced):
    """Hatch the bars that are illustrative values or author estimates."""
    for bar, ok in zip(bars, sourced):
        if not ok:
            bar.set_hatch('//')


hatch_patch = Patch(facecolor='white', edgecolor='black', hatch='//',
                    label='Hatched = illustrative /\nauthor estimate')

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Housing Hoarding: Taiwan vs International Standards\n'
             'Very low holding costs make property an attractive savings vehicle '
             '(author estimate)',
             fontsize=14, fontweight='bold')

# Panel 1: Taiwan vs international comparison
ax = axes[0]
x = np.arange(len(hoarding_categories))
w = 0.25
b_tw = ax.bar(x - w, tw_values, w, color='#E74C3C', alpha=0.8, label='Taiwan',
              edgecolor='black', linewidth=1)
b_us = ax.bar(x, us_values, w, color='#3498DB', alpha=0.8, label='USA',
              edgecolor='black', linewidth=1)
b_jp = ax.bar(x + w, jp_values, w, color='#F39C12', alpha=0.8, label='Japan',
              edgecolor='black', linewidth=1)
hatch_unsourced(b_tw, tw_sourced)
hatch_unsourced(b_us, us_sourced)
hatch_unsourced(b_jp, jp_sourced)
for i in range(len(hoarding_categories)):
    if np.isnan(us_values[i]):
        ax.text(x[i], tw_values[i] + 1.2, 'US / Japan:\nno comparable\nfigure',
                ha='center', fontsize=7, style='italic')
ax.set_xticks(x)
ax.set_xticklabels(hoarding_categories, fontsize=9)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title('Holding Costs & Vacancy Rates', fontsize=12, fontweight='bold')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + [hatch_patch], labels + [hatch_patch.get_label()], fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Cost of holding a NT$30M property
ax = axes[1]
countries = ['Taiwan', 'Japan', 'USA', 'UK', 'Singapore']
annual_cost_pct = [0.1, 1.0, 0.9, 1.2, 0.5]
cost_sourced = [False, False, True, False, False]   # only the US average is a sourced figure
annual_cost_ntd = [c / 100 * 30000000 for c in annual_cost_pct]  # Based on NT$30M property
colors_hold = ['#E74C3C', '#F39C12', '#3498DB', '#2ECC71', '#8E44AD']
bars = ax.bar(countries, [c / 10000 for c in annual_cost_ntd], color=colors_hold,
              alpha=0.8, edgecolor='black', linewidth=1)
hatch_unsourced(bars, cost_sourced)
ax.set_ylabel('Annual holding cost (NT$ 10K)', fontsize=11)
ax.set_title('Annual Cost of Holding a NT$30M Property', fontsize=12, fontweight='bold')
for bar, v, pct in zip(bars, annual_cost_ntd, annual_cost_pct):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'NT${v/1000:,.0f}K\n({pct}%)', ha='center', fontsize=9, fontweight='bold')
ax.set_ylim(0, max(annual_cost_ntd) / 10000 * 1.2)
ax.legend(handles=[hatch_patch], fontsize=9, loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Vacancy paradox — empty homes vs price
ax = axes[2]
# Illustrative hand-set path; only the 2020 vacancy value (18.5%) is the census figure.
# The price index is a hand-set illustrative index, not a published series.
tw_vacancy_years = [2010, 2012, 2014, 2016, 2018, 2020]
tw_vacancy_rate = [17.5, 18.0, 18.5, 18.8, 18.5, TW_VACANCY_PCT]
tw_price_index = [80, 95, 105, 108, 100, 112]
ax2 = ax.twinx()
ax.plot(tw_vacancy_years, tw_vacancy_rate, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=7, label='Vacancy rate (%)')
ax2.plot(tw_vacancy_years, tw_price_index, 's-', color='#E74C3C', linewidth=2.5,
         markersize=7, label='Price index')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Vacancy Rate (%)', color='#8E44AD', fontsize=11)
ax2.set_ylabel('Price Index (illustrative, hand-set)', color='#E74C3C', fontsize=11)
ax.set_title('The Paradox: More Vacancies, Higher Prices?\n'
             '(illustrative path; only 2020 = census 18.5%)', fontsize=11, fontweight='bold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='center left')
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_housing_hoarding.png', dpi=300, bbox_inches='tight')
plt.close()

tw_cost = annual_cost_ntd[0]
us_cost = annual_cost_ntd[2]
print(f"  Taiwan vacancy: {TW_VACANCY_PCT}% ({TW_VACANT_HOMES_M}M vacant homes, 2020 census)")
print(f"  MOI low-use (electricity) definition: about {TW_LOW_USE_HOMES_K}K homes "
      f"({TW_LOW_USE_PCT}%, H2 2024)")
print(f"  Holders of 3+ non-owner-occupied homes: {TW_HOLDERS_3PLUS:,} people "
      f"({tw_3plus_pct}% of about {TW_HOLDERS_NONOWNER:,} such holders, MOF 2025)")
print(f"  Effective tax rate: Taiwan {tw_values[2]}% (author estimate) vs USA ~{us_values[2]}% (average)")
print(f"  Annual holding cost on NT$30M: Taiwan NT${tw_cost/1000:,.0f}K (author estimate) "
      f"vs USA ~NT${us_cost/1000:,.0f}K")
print("  Note: US / Japan / UK / Singapore bars other than the US tax rate are illustrative")
print("=> Saved: 02_housing_hoarding.png")


# ============================================================
# MODEL 3: Demographics Doom Loop — Japan vs Taiwan
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Demographics Doom Loop -- Japan vs Taiwan")
print("=" * 65)

# Fertility series
jp_fert_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023]
jp_fertility = [1.54, 1.42, 1.36, 1.26, 1.39, 1.45, 1.34, 1.20]
tw_fert_years = [2000, 2005, 2010, 2015, 2018, 2020, 2022, 2023]
tw_fertility = [1.68, 1.12, 0.90, 1.18, 1.06, 0.99, 0.87, 0.87]
jp_span = jp_fert_years[-1] - jp_fert_years[0]      # 1990 -> 2023 = 33 years
tw_i15 = tw_fert_years.index(2015)
tw_span = tw_fert_years[-1] - tw_fert_years[tw_i15]  # 2015 -> 2023 = 8 years

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Demographics Doom Loop: Housing Unaffordability -> Population Collapse\n'
             f'Japan took {jp_span} years to decline | Taiwan is doing it in {tw_span}',
             fontsize=14, fontweight='bold')

# Panel 1: Fertility rate comparison
ax = axes[0]
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
# Births (10K): Japan 1990 about 122 (rounded); Japan 2023 727,277 (MHLW);
#   Taiwan 2015 213,093 and 2023 133,895 (MOI, by date of birth).
jp_1990 = [1.54, 122, 25.9, 12.1]
jp_2023 = [1.20, 72.7, 29.7, 29.1]
tw_2015 = [1.18, 21.3, 30.0, 12.5]
tw_2023 = [0.87, 13.4, 31.0, 18.4]
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

# Panel 3: Population outlook
ax = axes[2]
# Taiwan: NDC (National Development Council) 2024 population projections, medium scenario:
#   about 23.4 million (2024) -> about 15.0 million (2070); the 2070 scenario range is about
#   14.4 to 15.8 million. Only these published end points are plotted; the dashed line between
#   them is a visual connector (the real NDC path is not exactly a straight line).
tw_proj_years = [2024, 2070]
tw_proj_pop = [23.4, 15.0]            # millions
tw_proj_range_2070 = (14.4, 15.8)     # millions
# Japan: hand-set ILLUSTRATIVE path (10K persons), not an official projection
gen_years = [2023, 2035, 2045, 2055, 2065, 2075]
jp_pop = [12500, 11900, 11200, 10400, 9700, 9100]
ax.plot(tw_proj_years, tw_proj_pop, 'o--', color='#3498DB',
        linewidth=2.5, markersize=7, label='Taiwan (millions, NDC medium scenario)')
ax.errorbar([2070], [tw_proj_pop[-1]],
            yerr=[[tw_proj_pop[-1] - tw_proj_range_2070[0]],
                  [tw_proj_range_2070[1] - tw_proj_pop[-1]]],
            fmt='none', ecolor='#3498DB', capsize=6, linewidth=2)
for yr, val in zip(tw_proj_years, tw_proj_pop):
    ax.annotate(f'{val}M', (yr, val), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=9, fontweight='bold', color='#3498DB')
ax.plot(gen_years, [p / 100 for p in jp_pop], 's-', color='#E74C3C',
        linewidth=2.5, markersize=7, label='Japan (millions, illustrative)')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Population (millions)', fontsize=11)
ax.set_title('Population Outlook\n(Taiwan: NDC medium scenario | Japan: illustrative)',
             fontsize=11, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_demographics.png', dpi=300, bbox_inches='tight')
plt.close()

# Each generation relative to the previous one: 1 - TFR / replacement level
replacement_rate = 2.1
tw_tfr_2023 = tw_fertility[-1]
shrink_pct = (1 - tw_tfr_2023 / replacement_rate) * 100     # about 58.6 -> "about 59%"

print(f"  Japan fertility: {jp_fertility[0]:.2f} ({jp_fert_years[0]}) -> "
      f"{jp_fertility[-1]:.2f} ({jp_fert_years[-1]}) -- {jp_span} years")
print(f"  Taiwan fertility: {tw_fertility[tw_i15]:.2f} ({tw_fert_years[tw_i15]}) -> "
      f"{tw_tfr_2023:.2f} ({tw_fert_years[-1]}) -- {tw_span} years")
print(f"  At {tw_tfr_2023} vs the replacement level {replacement_rate}, each generation is about "
      f"{shrink_pct:.0f}% smaller than the last (ignoring migration and mortality changes)")
print(f"  Taiwan population, NDC medium scenario: {tw_proj_pop[0]}M ({tw_proj_years[0]}) -> "
      f"about {tw_proj_pop[-1]}M ({tw_proj_years[-1]}); 2070 range "
      f"{tw_proj_range_2070[0]}-{tw_proj_range_2070[1]}M")
print("=> Saved: 03_demographics.png")


# ============================================================
# MODEL 4: Zombie Companies — Japan's Lesson
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Zombie Companies -- Japan's Lesson for Taiwan")
print("=" * 65)

# Published reference points (NOT plotted -- the chart inputs below are hand-set illustrations):
#   Caballero, Hoshi & Kashyap (AER, 2008): zombie = firm receiving subsidized credit (interest paid
#   below the best market rate). Their share of listed firms is above 25% in every year after 1994
#   and about 30% in the early 2000s (about 15% by assets); the sample ends around 2002.
#   Japan FSA major-bank NPL ratio: 8.4% (March 2002) -> 1.8% (March 2006).
# The arrays below are ILLUSTRATIVE inputs (hand-set, not statistics). They do not reproduce the
# published series; e.g. the hand-set 1995 share (15%) is below the published figure.
zombie_years = [1995, 2000, 2005, 2010]
zombie_pct = [15, 26, 22, 12]            # illustrative, % of listed companies
zombie_employ = [12, 19, 16, 9]          # illustrative, % of employment
book_bad_debt = [3.5, 5.4, 4.0, 2.5]     # illustrative "book" bad-debt rate, NOT official data
actual_bad_debt = [12.5, 17.5, 12.5, 6.5]  # author's estimate of the "true" rate

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("Zombie Companies: Japan's Warning (illustrative inputs)\n"
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
ax.set_title('Japan: Zombie Company Prevalence\n(illustrative inputs)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Book vs actual bad debt
ax = axes[1]
ax.plot(zombie_years, book_bad_debt, 'o-', color='#3498DB', linewidth=2.5,
        markersize=8, label='Book bad-debt rate (illustrative)')
ax.plot(zombie_years, actual_bad_debt, 's-', color='#E74C3C', linewidth=2.5,
        markersize=8, label='Actual bad-debt rate (author estimate)')
ax.fill_between(zombie_years, book_bad_debt, actual_bad_debt,
                alpha=0.2, color='#E74C3C', label='Hidden bad debt')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Bad Debt Rate (%)', fontsize=11)
ax.set_title('Book vs Actual Bad Debt\n(illustrative inputs)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 3: Impact on economy
ax = axes[2]
impacts = ['Credit to\nNew Firms', 'Productivity\nGrowth', 'Innovation\nIndex',
           'Young Worker\nOpportunity']
# Illustrative magnitudes (hand-set). Caballero et al. (2008) find that healthy firms in zombie-heavy
# industries invest and hire less; the other effects shown here are the author's inference.
zombie_impact = [-60, -40, -35, -55]
colors_z = plt.cm.Reds(np.linspace(0.3, 0.8, len(impacts)))
bars = ax.barh(impacts, [abs(z) for z in zombie_impact], color=colors_z,
               edgecolor='black', linewidth=1)
ax.set_xlabel('Reduction (%, illustrative)', fontsize=11)
ax.set_title('Zombie Impact on Economy\n(illustrative magnitudes)', fontsize=12, fontweight='bold')
for bar, v in zip(bars, zombie_impact):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}%', va='center', fontweight='bold', fontsize=10, color='#E74C3C')
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_zombie_companies.png', dpi=300, bbox_inches='tight')
plt.close()

bad_debt_gap = max(a - b for a, b in zip(actual_bad_debt, book_bad_debt))
print("  Chart inputs are hand-set illustrations, not published statistics.")
print("  Published estimate (Caballero-Hoshi-Kashyap, 2008): about 30% of listed firms were "
      "zombies in the early 2000s (about 15% by assets)")
print("  Published FSA major-bank NPL ratio: 8.4% (Mar 2002) -> 1.8% (Mar 2006)")
print(f"  Illustrative hidden bad-debt gap: up to {bad_debt_gap:.0f} percentage points")
print("=> Saved: 04_zombie_companies.png")


# ============================================================
# MODEL 5: Lost Generation — Taiwan vs Japan Life Trajectories
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Lost Generation -- Taiwan vs Japan (illustrative estimates)")
print("=" * 65)

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle("Lost Generation: Housing Prices Don't Just Destroy Wealth -- They Destroy Futures\n"
             "Japan's Ice Age Gen (1990s) vs Taiwan's Suffocating Youth (2020s) -- illustrative estimates",
             fontsize=14, fontweight='bold')

# Panel 1: Taiwan generation gap
milestones = ['Home by 30', 'Married\nby 35', 'First Buy\nAge', 'Mortgage/\nIncome',
              'Down Payment\n(yrs income)']
# Hand-set ILLUSTRATIVE estimates of the order of magnitude, not survey results. The 1990-2000 cohort
# is only about 24-34 years old in 2024, so its values are partly projections.
# Down payment (years of income) = price-to-income ratio x 20-30% down payment:
#   born 1965-75: price-to-income about 6-8x -> about 1-2.5 years (midpoint ~1.8)
#   born 1990-2000: price-to-income about 16x -> about 3-5 years (midpoint ~4)
tw_prev = [40, 80, 31, 27, 1.8]
tw_now = [17, 57, 40, 45, 4.0]

ax = axes[0]
x = np.arange(len(milestones))
w = 0.35
ax.bar(x - w/2, tw_prev, w, color='#3498DB', alpha=0.8, label='Born 1965-75',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, tw_now, w, color='#E74C3C', alpha=0.8, label='Born 1990-2000 (partly projected)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(milestones, fontsize=8)
ax.set_ylabel('Value (% or years)', fontsize=11)
ax.set_title("Taiwan's Generation Gap (illustrative)", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Japan's ice age generation
jp_milestones = ['Employment\nat Grad', 'Formal Job\nat 30', 'Home\nat 35',
                 'Married\nat 40', 'Lifetime\nIncome (%)']
# Hand-set ILLUSTRATIVE values. The "Ice Age" (employment ice age) cohort is roughly those born
# c.1970-84, who graduated c.1993-2004; there is no single official definition.
jp_prev = [95, 90, 60, 90, 100]
jp_ice = [62, 55, 28, 58, 65]

ax = axes[1]
x = np.arange(len(jp_milestones))
ax.bar(x - w/2, jp_prev, w, color='#F39C12', alpha=0.8, label='Born 1955-65',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, jp_ice, w, color='#E74C3C', alpha=0.8, label='Ice Age (born c.1970-84)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(jp_milestones, fontsize=8)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title("Japan's Ice Age Generation (illustrative)", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Shared vocabulary of despair
ax = axes[2]
vocab = ['Giving up\non housing', 'Small\nhappiness', 'Temp work\nculture',
         'Social\nwithdrawal']
jp_labels = ['Freeter', 'Satori-\nsedai', 'Haken', 'Hikikomori']
tw_labels = ['Tangping\n(Lie flat)', 'Xiao-\nquexing', 'Moonlight\nclan', 'Home\nhermit']
# Hand-set 0-100 scores invented for illustration; they are not measured. Origins of the words differ:
# tangping is a mainland Chinese internet term (2021); xiaoquexing was coined by Haruki Murakami (1986).
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
ax.set_xlabel('Cultural Resonance Score (illustrative, 0-100)', fontsize=11)
ax.set_title('Vocabulary of Despair (illustrative scores)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_lost_generation.png', dpi=300, bbox_inches='tight')
plt.close()

print("  All values in this model are hand-set illustrative estimates, not survey results.")
print(f"  Taiwan: homeownership by 30 falls from {tw_prev[0]}% to {tw_now[0]}% "
      "(1990-2000 cohort partly projected)")
print(f"  Taiwan: first purchase age shifts from {tw_prev[2]} to {tw_now[2]} "
      f"(+{tw_now[2] - tw_prev[2]} years)")
print(f"  Taiwan: down payment about {tw_prev[4]} -> {tw_now[4]} years of income "
      "(price-to-income x 20-30%)")
# Reference figure, not used in the charts: share of men never married at age 50 (national census
# based "lifetime unmarried rate", IPSS). NOT re-verified in the 2026-09 fact-check.
print("  Japan: lifetime unmarried rate (men, age 50) rose from 5.6% (1990) to 28.3% (2020)")
print("=> Saved: 05_lost_generation.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
