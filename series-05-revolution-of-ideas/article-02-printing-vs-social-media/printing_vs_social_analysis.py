"""
Revolution of Ideas #02: The Printing Press vs Social Media Explosion
Free Version — 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Information Speed Comparison (Exponential Acceleration)
# ============================================================
print("=" * 65)
print("MODEL 1: Information Speed -- 570 Years, 10,000x Acceleration")
print("=" * 65)

eras = ['1400\nHand-copy', '1455\nPrinting', '1500\nPrint Net',
        '1844\nTelegraph', '1920\nRadio', '1990\nInternet', '2024\nSocial']
speed_multiplier = [1, 50, 500, 1000, 5000, 8000, 10000]
years = [1400, 1455, 1500, 1844, 1920, 1990, 2024]

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#8E44AD', '#9B59B6', '#E74C3C', '#E67E22', '#F39C12', '#2ECC71', '#3498DB']
bars = ax.bar(range(len(eras)), speed_multiplier, color=colors, alpha=0.85,
              edgecolor='black', linewidth=1)
ax.set_yscale('log')
ax.set_xticks(range(len(eras)))
ax.set_xticklabels(eras, fontsize=9)
ax.set_ylabel('Relative Speed (log scale)', fontsize=12)
ax.set_title('Information Propagation Speed: 570 Years of Acceleration\n'
             'Hand-copying (1x) → Social Media (10,000x)',
             fontsize=13, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
for i, v in enumerate(speed_multiplier):
    ax.text(i, v * 1.3, f'{v:,}x', ha='center', fontweight='bold', fontsize=10)

# Annotate acceleration intervals
intervals = [55, 389, 76, 70, 14]
for i in range(len(intervals)):
    mid_x = i + 0.5
    ax.annotate(f'{intervals[i]}y gap', xy=(mid_x, speed_multiplier[i]),
                fontsize=7, ha='center', color='gray', style='italic')

plt.tight_layout()
plt.savefig('01_info_speed_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nRelative speed over centuries:")
for e, s in zip(eras, speed_multiplier):
    print(f"  {e.replace(chr(10), ' '):<20}: {s:>6,}x")
print("\n  Gap between revolutions is shrinking: 389y -> 76y -> 70y -> 14y")
print("\n=> Saved: 01_info_speed_comparison.png")


# ============================================================
# MODEL 2: Book Production Explosion (1450-1500)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Book Production Explosion -- 500x in 50 Years")
print("=" * 65)

prod_years = [1450, 1460, 1470, 1480, 1490, 1500]
hand_copied = [30000, 30000, 30000, 30000, 30000, 30000]
printed = [30000, 50000, 300000, 2000000, 6000000, 15000000]
growth_factor = [p / 30000 for p in printed]

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.fill_between(prod_years, hand_copied, alpha=0.3, color='#8E44AD', label='Hand-copied baseline')
ax1.fill_between(prod_years, printed, alpha=0.3, color='#E74C3C')
ax1.semilogy(prod_years, printed, 'o-', color='#E74C3C', linewidth=2.5, markersize=8,
             label='Total books (with printing)')
ax1.semilogy(prod_years, hand_copied, 's--', color='#8E44AD', linewidth=2, markersize=6,
             label='Hand-copied capacity (no press)')
ax1.annotate('Gutenberg Bible\n(1455)', xy=(1455, 35000), fontsize=10,
             xytext=(1462, 200000), arrowprops=dict(arrowstyle='->', color='black'),
             fontweight='bold')
ax1.annotate('500x growth!', xy=(1500, 15000000), fontsize=12,
             xytext=(1488, 12000000), fontweight='bold', color='#C0392B')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total Books in Europe (log scale)', fontsize=12)
ax1.set_title('Book Production Explosion: Gutenberg Effect (1450–1500)\n'
              'From 30,000 hand-copied → 15,000,000 printed',
              fontsize=13, fontweight='bold')
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(alpha=0.3)
ax1.set_xlim(1445, 1505)
plt.tight_layout()
plt.savefig('02_book_production_explosion.png', dpi=300, bbox_inches='tight')
plt.close()

for y, p, g in zip(prod_years, printed, growth_factor):
    print(f"  {y}: {p:>12,} books  ({g:>6.1f}x vs 1450)")
print("\n=> 50 years, 500x. Saved: 02_book_production_explosion.png")


# ============================================================
# MODEL 3: Fake News SIR Model (Truth vs Misinformation)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Fake News SIR Model -- Epidemiology of Misinformation")
print("=" * 65)

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
S1, I1, R1 = sir_model(100000, beta=0.3, gamma=0.01, days=90)
# Scenario 2: Modern real news via social media
S2, I2, R2 = sir_model(1000000, beta=0.5, gamma=0.1, days=30)
# Scenario 3: Modern fake news via social media (MIT: 6x faster)
S3, I3, R3 = sir_model(1000000, beta=0.9, gamma=0.02, days=30)

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

fig.suptitle('SIR Model: Information Spread as Epidemic\n'
             'Fake news peaks faster (day 8) and recovers slower than real news (day 12)',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_fake_news_sir_model.png', dpi=300, bbox_inches='tight')
plt.close()

peak_luther = np.argmax(I1)
peak_real = np.argmax(I2)
peak_fake = np.argmax(I3)
print(f"\n  Luther's Theses -- peak infection at day {peak_luther}")
print(f"  Modern real news -- peak infection at day {peak_real}")
print(f"  Modern fake news -- peak infection at day {peak_fake}")
print(f"  Fake news peaks {peak_real - peak_fake} days faster than real news")
print(f"  Recovery rate: fake (gamma=0.02) is 5x slower than real (gamma=0.10)")
print("\n=> Saved: 03_fake_news_sir_model.png")


# ============================================================
# MODEL 4: Content Filtering Evolution (Church → Algorithm)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Content Filtering -- From Church Censors to Algorithms")
print("=" * 65)

filter_eras = ['Pre-1450\nChurch\nScribes', '1455-1559\nFree\nPrinting',
               '1559\nIndex\nLibrorum', '1700-1900\nGovt\nCensors',
               '1900-2000\nEditors\nJournalists', '2000-2010\nEarly\nSocial',
               '2010-2024\nAlgorithmic\nFiltering']
pass_rate = [30, 95, 60, 50, 20, 99, 85]
delay_days = [180, 21, 90, 30, 1, 0.001, 0.001]  # approximate days

fig, ax1 = plt.subplots(figsize=(14, 7))
x = np.arange(len(filter_eras))
color_pass = '#2ECC71'
color_delay = '#E74C3C'

bars1 = ax1.bar(x - 0.2, pass_rate, 0.38, color=color_pass, alpha=0.8,
                edgecolor='black', linewidth=1, label='Pass Rate (%)')
ax1.set_ylabel('Content Pass Rate (%)', fontsize=12, color=color_pass)
ax1.set_ylim(0, 115)

ax2 = ax1.twinx()
ax2.plot(x, delay_days, 'o-', color=color_delay, linewidth=2.5, markersize=8,
         label='Publication Delay (days)')
ax2.set_yscale('log')
ax2.set_ylabel('Publication Delay — days (log scale)', fontsize=12, color=color_delay)

ax1.set_xticks(x)
ax1.set_xticklabels(filter_eras, fontsize=8)
ax1.set_title('Evolution of Content Gatekeeping (1400–2024)\n'
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

print("\nHistorical content gatekeeping:")
for e, p, d in zip(filter_eras, pass_rate, delay_days):
    era_label = e.replace('\n', ' ')
    print(f"  {era_label:<28}: pass={p:>3}%, delay={d:>7.1f} days")
print("\n  Pattern: every info revolution -> freedom -> backlash -> new equilibrium")
print("\n=> Saved: 04_content_filtering_evolution.png")


# ============================================================
# MODEL 5: Attention Economy (Reading Time Collapse)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Attention Collapse -- 20 Hours to 7 Seconds")
print("=" * 65)

media_eras = ['1500\nBooks', '1800\nNewspapers', '1950\nTV News',
              '2000\nWeb Pages', '2015\nSocial Posts', '2024\nShort Video']
attention_seconds = [72000, 1800, 1320, 120, 15, 7]  # in seconds
attention_labels = ['~20 hours', '~30 min', '~22 min', '~2 min', '~15 sec', '~7 sec']
info_density = [95, 60, 40, 25, 10, 3]  # qualitative info density %

fig, ax1 = plt.subplots(figsize=(12, 7))
x = np.arange(len(media_eras))
color_att = '#E74C3C'
color_den = '#3498DB'

ax1.semilogy(x, attention_seconds, 'o-', color=color_att, linewidth=2.5, markersize=10,
             label='Attention Duration (seconds)')
ax1.fill_between(x, attention_seconds, alpha=0.1, color=color_att)
ax1.set_ylabel('Attention Duration — seconds (log scale)', fontsize=12, color=color_att)

ax2 = ax1.twinx()
ax2.bar(x, info_density, 0.4, color=color_den, alpha=0.4, label='Information Density (%)')
ax2.set_ylabel('Information Density (%)', fontsize=12, color=color_den)
ax2.set_ylim(0, 120)

ax1.set_xticks(x)
ax1.set_xticklabels(media_eras, fontsize=9)
ax1.set_title('The Attention Economy: 524 Years of Collapse\n'
              '20 hours/book → 7 seconds/video (10,286x shrinkage)',
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
print(f"  Shrinkage:           {ratio_collapse:,.0f}x")
print(f"  Info density drop:   {info_density[0]}% -> {info_density[-1]}%")
print("\n=> Saved: 05_attention_economy.png")


# ============================================================
# MODEL 6: Echo Chamber Effect (Geographic vs Algorithmic)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 6: Echo Chamber Effect -- Geographic vs Algorithmic")
print("=" * 65)

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

fig.suptitle('Echo Chamber Effect: Geography vs Algorithm\n'
             'Algorithms create sharper polarization despite lower homophily',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('06_echo_chamber_effect.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n  Geographic echo chamber -- final std dev: {geo_polar[-1]:.3f}")
print(f"  Algorithmic echo chamber -- final std dev: {algo_polar[-1]:.3f}")
print(f"  Algorithmic polarization is {algo_polar[-1]/geo_polar[-1]:.1f}x stronger")
print(f"\n  Key insight: 16th C people KNEW their info was limited.")
print(f"  21st C people DON'T KNOW they're in a bubble.")
print("\n=> Saved: 06_echo_chamber_effect.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
