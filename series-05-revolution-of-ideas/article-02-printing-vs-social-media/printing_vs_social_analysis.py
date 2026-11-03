"""
Revolution of Ideas #02: The Printing Press vs Social Media Explosion
Free Version — 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install matplotlib numpy

What is real, what is illustrative
  Models 1, 2, 4 and 5 plot HAND-SET ILLUSTRATIVE values (the author's rough scale for
  comparison). They are not measured data, not historical statistics and not model results.
  Models 3 and 6 are parameter-driven simulations: their outputs follow from the input
  assumptions (beta, gamma, homophily, ...), not from empirical data.
  Real-world figures quoted in the article (MIT/Science 2018, Reuters Institute, ...) are
  listed with sources in the article's References section; this script only borrows the
  direction of the MIT finding and does not fit any model to it.
"""

import sys

import matplotlib.pyplot as plt
import numpy as np

# Keep printing robust on consoles that cannot encode the Greek letters used in the Model 3 table
try:
    sys.stdout.reconfigure(errors='replace')
except (AttributeError, ValueError):
    pass

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Information Speed Comparison (illustrative relative scale)
# ============================================================
print("=" * 65)
print("MODEL 1: Information Speed -- Illustrative Relative Scale (570 Years)")
print("=" * 65)
print("Hand-set illustrative values, not measured data and not a model result.")

eras = ['1400\nHand-copy', '1455\nPrinting', '1500\nPrint Net',
        '1844\nTelegraph', '1920\nRadio', '1990\nInternet', '2024\nSocial']
# ILLUSTRATIVE: relative speeds set by hand by the author (1x = hand-copying); no source
speed_multiplier = [1, 50, 500, 1000, 5000, 8000, 10000]
years = [1400, 1455, 1500, 1844, 1920, 1990, 2024]

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#8E44AD', '#9B59B6', '#E74C3C', '#E67E22', '#F39C12', '#2ECC71', '#3498DB']
bars = ax.bar(range(len(eras)), speed_multiplier, color=colors, alpha=0.85,
              edgecolor='black', linewidth=1)
ax.set_yscale('log')
ax.set_ylim(0.6, 150000)
ax.set_xticks(range(len(eras)))
ax.set_xticklabels(eras, fontsize=9)
ax.set_ylabel('Relative Speed (illustrative scale, log)', fontsize=12)
ax.set_title('Information Propagation Speed: 570 Years (illustrative hand-set scale, not measured data)\n'
             'Hand-copying (1x) → Social Media (10,000x) on this scale',
             fontsize=13, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
for i, v in enumerate(speed_multiplier):
    ax.text(i, v * 1.3, f'{v:,}x', ha='center', fontweight='bold', fontsize=10)

# Gaps between the revolution milestones (bar index pairs):
# Printing (1455) -> Telegraph (1844) -> Radio (1920) -> Internet (1990) -> Social media.
# The last gap is counted from Facebook's 2004 launch, although the bar is drawn at 2024.
gap_spans = [(1, 3, 389), (3, 4, 76), (4, 5, 70), (5, 6, 14)]
for a, b, gap in gap_spans:
    ax.annotate('', xy=(a, 30000), xytext=(b, 30000),
                arrowprops=dict(arrowstyle='<->', color='gray'))
    ax.text((a + b) / 2, 38000, f'{gap}y gap', ha='center', fontsize=8,
            color='gray', style='italic')

plt.tight_layout()
plt.savefig('01_info_speed_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nRelative speed on the illustrative scale:")
for e, s in zip(eras, speed_multiplier):
    print(f"  {e.replace(chr(10), ' '):<20}: {s:>6,}x")
print("\n  Gap between revolutions is shrinking: 389y -> 76y -> 70y -> 14y")
print("  (printing 1455 -> telegraph 1844 -> radio 1920 -> internet 1990 -> social media,")
print("   counted from Facebook's 2004 launch)")
print("\n=> Saved: 01_info_speed_comparison.png")


# ============================================================
# MODEL 2: Book Production Explosion (1450-1500, illustrative curve)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Book Production Explosion -- Illustrative Curve, 1450-1500")
print("=" * 65)
print("Hand-set decade values, not year-by-year statistics.")

prod_years = [1450, 1460, 1470, 1480, 1490, 1500]
# ILLUSTRATIVE: the 30,000 starting point and the decade values are set by hand.
# Only the end point is anchored to scholarship: roughly 10-20 million copies in total were
# printed by 1500 (Febvre & Martin, The Coming of the Book; British Library ISTC), so the
# hand-set 15,000,000 falls inside that range of estimates.
hand_copied = [30000, 30000, 30000, 30000, 30000, 30000]
printed = [30000, 50000, 300000, 2000000, 6000000, 15000000]

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.fill_between(prod_years, hand_copied, alpha=0.3, color='#8E44AD', label='Hand-copied baseline (illustrative)')
ax1.fill_between(prod_years, printed, alpha=0.3, color='#E74C3C')
ax1.semilogy(prod_years, printed, 'o-', color='#E74C3C', linewidth=2.5, markersize=8,
             label='Total books, with printing (illustrative)')
ax1.semilogy(prod_years, hand_copied, 's--', color='#8E44AD', linewidth=2, markersize=6,
             label='Hand-copied capacity, no press (illustrative)')
ax1.annotate('Gutenberg Bible\n(1455)', xy=(1455, 35000), fontsize=10,
             xytext=(1462, 200000), arrowprops=dict(arrowstyle='->', color='black'),
             fontweight='bold')
ax1.annotate('~15 million by 1500 (hand-set)\nScholarly estimate: 10–20 million copies in total',
             xy=(1500, 15000000), fontsize=10,
             xytext=(1466, 4500000), fontweight='bold', color='#C0392B')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Books in Europe (illustrative, log scale)', fontsize=12)
ax1.set_title('Book Production, 1450–1500 (illustrative hand-set values, not statistics)\n'
              'From 30,000 hand-copied → 15,000,000 printed by 1500 (within the 10–20 million scholarly estimate)',
              fontsize=12, fontweight='bold')
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(alpha=0.3)
ax1.set_xlim(1445, 1505)
plt.tight_layout()
plt.savefig('02_book_production_explosion.png', dpi=300, bbox_inches='tight')
plt.close()

for y, p in zip(prod_years, printed):
    print(f"  {y}: {p:>12,} books  (illustrative)")
print(f"\n=> Illustrative curve ends at {printed[-1]:,} by 1500 "
      "(scholarly estimate of copies printed in total by 1500: 10-20 million).")
print("   Saved: 02_book_production_explosion.png")


# ============================================================
# MODEL 3: Fake News SIR Model (Truth vs Misinformation)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Fake News SIR Model -- Epidemiology of Misinformation")
print("=" * 65)
print("Parameter-driven simulation: every beta and gamma below is an assumed input.")

def sir_model(population, beta, gamma, days, initial_infected=10):
    """SIR model: simulate information spread as epidemic."""
    S, I, R = [population - initial_infected], [initial_infected], [0]
    for _ in range(days):
        s, i, r = S[-1], I[-1], R[-1]
        new_infected = beta * s * i / population
        new_recovered = gamma * i
        S.append(s - new_infected)
        I.append(i + new_infected - new_recovered)
        R.append(r + new_recovered)
    return np.array(S), np.array(I), np.array(R)

# Scenario 1: Luther's 95 Theses via printing press (1517)
# beta=0.3: moderate transmission (print speed limits), gamma=0.01: very low recovery (no fact-checking)
S1, I1, R1 = sir_model(100000, beta=0.3, gamma=0.01, days=90)
# Scenario 2: Modern real news via social media
# beta=0.5: higher transmission, gamma=0.1: moderate recovery (fact-checking exists)
S2, I2, R2 = sir_model(1000000, beta=0.5, gamma=0.1, days=30)
# Scenario 3: Modern fake news via social media
# beta=0.9: very high transmission (illustrative value, not derived from the MIT study's 6x),
# gamma=0.02: very low recovery (assumed)
# (Direction borrowed from Vosoughi, Roy & Aral 2018, Science 359: false stories spread faster;
#  the values themselves are not fitted to that paper.)
S3, I3, R3 = sir_model(1000000, beta=0.9, gamma=0.02, days=30)

# Key metrics
peak_luther = np.max(I1)
peak_real = np.max(I2)
peak_fake = np.max(I3)
day_peak_luther = np.argmax(I1)
day_peak_real = np.argmax(I2)
day_peak_fake = np.argmax(I3)
total_reached_luther = R1[-1] + I1[-1]
total_reached_real = R2[-1] + I2[-1]
total_reached_fake = R3[-1] + I3[-1]

# The 30-day window may end before the real-news peak: run the same scenario longer to see it
real_window_days = len(I2) - 1
real_not_peaked = day_peak_real == real_window_days
_, I2_long, _ = sir_model(1000000, beta=0.5, gamma=0.1, days=90)
day_peak_real_long = int(np.argmax(I2_long))
peak_real_long = np.max(I2_long)

fig, axes = plt.subplots(1, 3, figsize=(20, 7))
days1 = np.arange(len(S1))
days2 = np.arange(len(S2))
days3 = np.arange(len(S3))

for ax, days_arr, S, I, R, title, pop in [
    (axes[0], days1, S1, I1, R1, "Luther's Theses (1517)\nβ=0.3, γ=0.01", 100000),
    (axes[1], days2, S2, I2, R2, "Modern Real News\nβ=0.5, γ=0.1", 1000000),
    (axes[2], days3, S3, I3, R3, "Modern Fake News\nβ=0.9, γ=0.02", 1000000),
]:
    ax.plot(days_arr, S / pop * 100, 'b-', linewidth=2, label='Susceptible')
    ax.plot(days_arr, I / pop * 100, 'r-', linewidth=2.5, label='Infected (spreading)')
    ax.plot(days_arr, R / pop * 100, 'g-', linewidth=2, label='Recovered (debunked)')
    ax.set_xlabel('Days', fontsize=11)
    ax.set_ylabel('% of Population', fontsize=11)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    ax.axvline(x=np.argmax(I), color='red', linestyle='--', alpha=0.5)

if real_not_peaked:
    real_txt = f"real news is still rising at day {day_peak_real} (end of the window)"
else:
    real_txt = f"real news on day {day_peak_real}"
fig.suptitle('SIR Model: Information Spread as Epidemic (parameter-driven simulation)\n'
             f'Fake news peaks on day {day_peak_fake}; {real_txt}. '
             'Recovery rates are assumed inputs.',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_fake_news_sir_model.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n=== Information Spread SIR Model: Three Scenarios Compared ===\n")
print(f"{'Metric':<20} {'Luther Theses(1517)':<20} {'Modern Real News':<20} {'Modern Fake News':<20}")
print("-" * 80)
print(f"{'Population':<20} {'100,000':<20} {'1,000,000':<20} {'1,000,000':<20}")
print(f"{'Spread rate(β)':<20} {'0.30':<20} {'0.50':<20} {'0.90':<20}")
print(f"{'Recovery rate(γ)':<20} {'0.01':<20} {'0.10':<20} {'0.02':<20}")
reach_luther = f"{total_reached_luther / 100000 * 100:.1f}%"
reach_real = f"{total_reached_real / 1000000 * 100:.1f}%"
reach_fake = f"{total_reached_fake / 1000000 * 100:.1f}%"
print(f"{'Peak infected':<20} {peak_luther:<20,.0f} {peak_real:<20,.0f} {peak_fake:<20,.0f}")
print(f"{'Days to peak':<20} {day_peak_luther:<20} {day_peak_real:<20} {day_peak_fake:<20}")
print(f"{'Total reached':<20} {total_reached_luther:<20,.0f} {total_reached_real:<20,.0f} {total_reached_fake:<20,.0f}")
print(f"{'Reach rate':<20} {reach_luther:<20} {reach_real:<20} {reach_fake:<20}")

print(f"\n  Luther's Theses -- peak infection at day {day_peak_luther}")
if real_not_peaked:
    print(f"  Modern real news -- no peak within the {real_window_days}-day window (still rising at day {day_peak_real})")
    print(f"    Run for 90 days instead: peak at day {day_peak_real_long} with {peak_real_long:,.0f} infected")
else:
    print(f"  Modern real news -- peak infection at day {day_peak_real}")
print(f"  Modern fake news -- peak infection at day {day_peak_fake}")
print(f"  In this model fake news peaks {day_peak_real_long - day_peak_fake} days before real news "
      "(real news taken from the 90-day run)")
print("  Recovery rate: fake (gamma=0.02) is 5x slower than real (gamma=0.10) "
      "(input assumption, not a result)")
print("  Spread rates (beta) are illustrative inputs too; they are not derived from the MIT 6x figure")
print("\n=> Saved: 03_fake_news_sir_model.png")


# ============================================================
# MODEL 4: Content Filtering Evolution (Church → Algorithm, illustrative scores)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Content Filtering -- From Church Censors to Algorithms")
print("=" * 65)
print("Hand-set illustrative scores (pass rate, delay), not tracked or measured data.")

filter_eras = ['Pre-1450\nChurch\nScribes', '1455-1559\nPatchy Local\nControls',
               '1559\nIndex\nLibrorum', '1700-1900\nGovt\nCensors',
               '1900-2000\nEditors\nJournalists', '2000-2010\nEarly\nSocial',
               '2010-2024\nAlgorithmic\nFiltering']
# ILLUSTRATIVE: rough scores set by hand, no source
pass_rate = [30, 95, 60, 50, 20, 99, 85]
delay_days = [180, 21, 90, 30, 1, 0.001, 0.001]  # illustrative, approximate days

fig, ax1 = plt.subplots(figsize=(14, 7))
x = np.arange(len(filter_eras))
color_pass = '#2ECC71'
color_delay = '#E74C3C'

bars1 = ax1.bar(x - 0.2, pass_rate, 0.38, color=color_pass, alpha=0.8,
                edgecolor='black', linewidth=1, label='Pass Rate (%, illustrative)')
ax1.set_ylabel('Content Pass Rate (%, illustrative score)', fontsize=12, color=color_pass)
ax1.set_ylim(0, 115)

ax2 = ax1.twinx()
ax2.plot(x, delay_days, 'o-', color=color_delay, linewidth=2.5, markersize=8,
         label='Publication Delay (days, illustrative)')
ax2.set_yscale('log')
ax2.set_ylabel('Publication Delay — days (illustrative, log scale)', fontsize=12, color=color_delay)

ax1.set_xticks(x)
ax1.set_xticklabels(filter_eras, fontsize=8)
ax1.set_title('Evolution of Content Gatekeeping (1400–2024) — illustrative hand-set scores, not measured data\n'
              'Pass rate oscillates; delay collapses to near-zero',
              fontsize=13, fontweight='bold')

for i, v in enumerate(pass_rate):
    ax1.text(i - 0.2, v + 2, f'{v}%', ha='center', fontweight='bold', fontsize=9)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper right')
ax1.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('04_content_filtering_evolution.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nHistorical content gatekeeping (illustrative scores):")
for e, p, d in zip(filter_eras, pass_rate, delay_days):
    era_label = e.replace('\n', ' ')
    print(f"  {era_label:<32}: pass={p:>3}%, delay={d:>7g} days")
print("\n  Pattern (the author's reading): every info revolution -> freedom -> backlash -> new equilibrium")
print("\n=> Saved: 04_content_filtering_evolution.png")


# ============================================================
# MODEL 5: Attention Economy (illustrative content length)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Content Length Collapse -- 20 Hours to 7 Seconds (illustrative)")
print("=" * 65)
print("Hand-set content lengths: roughly how long a book or a post takes to finish.")
print("This is not measured attention and has no source.")

media_eras = ['1500\nBooks', '1800\nNewspapers', '1950\nTV News',
              '2000\nWeb Pages', '2015\nSocial Posts', '2024\nShort Video']
# ILLUSTRATIVE: content lengths set by hand, in seconds
attention_seconds = [72000, 1800, 1320, 120, 15, 7]
attention_labels = ['~20 hours', '~30 min', '~22 min', '~2 min', '~15 sec', '~7 sec']
info_density = [95, 60, 40, 25, 10, 3]  # qualitative, hand-set score (%)

fig, ax1 = plt.subplots(figsize=(12, 7))
x = np.arange(len(media_eras))
color_att = '#E74C3C'
color_den = '#3498DB'

ax1.semilogy(x, attention_seconds, 'o-', color=color_att, linewidth=2.5, markersize=10,
             label='Content Length (seconds, illustrative)')
ax1.fill_between(x, attention_seconds, alpha=0.1, color=color_att)
ax1.set_ylabel('Content Length — seconds (illustrative, log scale)', fontsize=12, color=color_att)

ax2 = ax1.twinx()
ax2.bar(x, info_density, 0.4, color=color_den, alpha=0.4, label='Information Density (%, hand-set score)')
ax2.set_ylabel('Information Density (%, hand-set score)', fontsize=12, color=color_den)
ax2.set_ylim(0, 120)

ax1.set_xticks(x)
ax1.set_xticklabels(media_eras, fontsize=9)
ax1.set_title('Content Length, 524 Years (illustrative hand-set values, not measured attention)\n'
              '20 hours/book → 7 seconds/video (10,286x shrinkage on these values)',
              fontsize=13, fontweight='bold')

for i, (v, lbl) in enumerate(zip(attention_seconds, attention_labels)):
    ax1.annotate(lbl, xy=(i, v), xytext=(i + 0.15, v * 1.8),
                 fontsize=9, fontweight='bold', color=color_att)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper right')
ax1.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('05_attention_economy.png', dpi=300, bbox_inches='tight')
plt.close()

ratio_collapse = attention_seconds[0] / attention_seconds[-1]
print(f"\n  1500 (Books):        {attention_labels[0]}")
print(f"  2024 (Short Video):  {attention_labels[-1]}")
print(f"  Shrinkage:           {ratio_collapse:,.0f}x  (on the hand-set values)")
print(f"  Info density drop:   {info_density[0]}% -> {info_density[-1]}%  (hand-set score)")
print("\n=> Saved: 05_attention_economy.png")


# ============================================================
# MODEL 6: Echo Chamber Effect (Geographic vs Algorithmic)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 6: Echo Chamber Effect -- Geographic vs Algorithmic")
print("=" * 65)
print("Parameter-driven simulation: the outcome depends on the parameters chosen below.")

np.random.seed(42)

def simulate_echo_chamber(n_agents, n_steps, homophily, algorithm_boost=0.0):
    """Simulate opinion polarization in a network.
    homophily: tendency to connect with similar opinions (0-1)
    algorithm_boost: extra push toward extreme (algorithmic amplification)
    """
    opinions = np.random.normal(0, 0.3, n_agents)  # start near center
    polarization_history = []
    for step in range(n_steps):
        for i in range(n_agents):
            # pick neighbor: with probability=homophily, pick similar opinion
            if np.random.random() < homophily:
                diffs = np.abs(opinions - opinions[i])
                diffs[i] = np.inf
                j = np.argmin(diffs)  # most similar
            else:
                j = np.random.randint(n_agents)
            # influence
            opinions[i] += 0.05 * (opinions[j] - opinions[i])
            # algorithmic amplification pushes toward extremes
            if algorithm_boost > 0:
                opinions[i] += algorithm_boost * np.sign(opinions[i]) * 0.02
        # clip to [-1, 1]
        opinions = np.clip(opinions, -1, 1)
        polarization_history.append(np.std(opinions))
    return opinions, polarization_history

n_agents = 200
n_steps = 80

# 16th century: geographic echo chamber (high homophily, no algorithm)
geo_opinions, geo_polar = simulate_echo_chamber(n_agents, n_steps, homophily=0.7, algorithm_boost=0.0)
# 21st century: algorithmic echo chamber (moderate homophily + algorithm boost)
algo_opinions, algo_polar = simulate_echo_chamber(n_agents, n_steps, homophily=0.5, algorithm_boost=1.5)

fig, axes = plt.subplots(1, 3, figsize=(20, 7))

# Panel 1: Polarization over time
axes[0].plot(range(n_steps), geo_polar, color='#8E44AD', linewidth=2.5,
             label='16th C Geographic')
axes[0].plot(range(n_steps), algo_polar, color='#E74C3C', linewidth=2.5,
             label='21st C Algorithmic')
axes[0].set_xlabel('Time Steps', fontsize=11)
axes[0].set_ylabel('Opinion Std Dev (polarization)', fontsize=11)
axes[0].set_title('Polarization Over Time', fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)

# Panel 2: Geographic opinion distribution
axes[1].hist(geo_opinions, bins=30, color='#8E44AD', alpha=0.7, edgecolor='black')
axes[1].set_xlabel('Opinion Spectrum (-1 to +1)', fontsize=11)
axes[1].set_ylabel('Count', fontsize=11)
axes[1].set_title('Geographic Echo Chamber\n(16th century)', fontsize=12, fontweight='bold')
axes[1].axvline(x=0, color='gray', linestyle='--', alpha=0.5)
axes[1].set_xlim(-1.1, 1.1)

# Panel 3: Algorithmic opinion distribution
axes[2].hist(algo_opinions, bins=30, color='#E74C3C', alpha=0.7, edgecolor='black')
axes[2].set_xlabel('Opinion Spectrum (-1 to +1)', fontsize=11)
axes[2].set_ylabel('Count', fontsize=11)
axes[2].set_title('Algorithmic Echo Chamber\n(21st century)', fontsize=12, fontweight='bold')
axes[2].axvline(x=0, color='gray', linestyle='--', alpha=0.5)
axes[2].set_xlim(-1.1, 1.1)

fig.suptitle('Echo Chamber Effect: Geography vs Algorithm (parameter-driven simulation)\n'
             'Algorithms create sharper polarization despite lower homophily — a product of the parameters chosen',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('06_echo_chamber_effect.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n  Simulation: {n_agents} agents, {n_steps} steps, random seed 42")
print(f"  Geographic echo chamber (homophily 0.7, no algorithm) -- final std dev: {geo_polar[-1]:.3f}")
print(f"  Algorithmic echo chamber (homophily 0.5, algorithm boost 1.5) -- final std dev: {algo_polar[-1]:.3f}")
print(f"  Algorithmic polarization is {algo_polar[-1]/geo_polar[-1]:.1f}x stronger in this simulation")
print(f"\n  Interpretation (the author's reading, not a simulation output):")
print(f"  16th C people KNEW their info was limited; 21st C people may not notice they're in a bubble.")
print("\n=> Saved: 06_echo_chamber_effect.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
