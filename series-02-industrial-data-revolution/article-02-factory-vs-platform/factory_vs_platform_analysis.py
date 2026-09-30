"""
Factory Discipline vs Platform Algorithms - Free Version
Series 2 (Industrial Revolution meets the Data Revolution), Article 02

Author: Wina Wu
Date: 2025-12 (last revised 2026-09 to match the fact-checked article)

This free version includes:
- Basic TayloristFactory output distribution (1 plot)
- Basic Uber earnings distribution (1 plot)
- Basic comparison chart (1 plot)
- A text-only income-volatility check (the GigEconomyModel shown in the article)

For complete version with 14 sub-plots, see premium content.

READ THIS FIRST - what the numbers are, and what they are not
-------------------------------------------------------------
Everything below is a toy model with hand-set, ILLUSTRATIVE inputs:
- Factory: task times, efficiency spread, fatigue rate and task mix.
- Uber-style driver: rating spread, 22% commission, $12 fare, 2.5 trips/hour.
- Comparison chart: 0-1 scores set by hand from the mechanisms in the article.
- Income check: the fixed $100 daily wage and the four volatility factors.
Whatever is plotted or printed is the OUTPUT of those assumptions. None of it is
a measurement of a real factory, and none of it is an Uber statistic or real
driver earnings data.

Real-world reference points (from the article, NOT modelled in this script):
- Taylor's 1899 pig-iron experiment at Bethlehem Steel Works (Bethlehem,
  Pennsylvania): pigs of about 92 lb (about 41.7 kg); loading per handler rose
  from about 12.5 to 47.5 long tons per day.
  Source: F. W. Taylor, The Principles of Scientific Management (1911),
  https://www.gutenberg.org/ebooks/6435

Requirements:
pip install numpy pandas matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


def gini(values):
    """Gini coefficient of non-negative values (0 = equal, 1 = maximally unequal)."""
    x = np.sort(np.asarray(values, dtype=float))
    n = len(x)
    return 2 * np.sum(np.arange(1, n + 1) * x) / (n * x.sum()) - (n + 1) / n


print("=" * 70)
print("Factory Discipline vs Platform Algorithms - Free Version")
print("Series 2, Article 02")
print("=" * 70)
print("All inputs are hand-set illustrative assumptions (toy models),")
print("not measurements of real factories or real Uber drivers.")
print()

# ============================================================================
# Visualization 1: TayloristFactory Output Distribution (Basic)
# ============================================================================

def taylorist_basic():
    """Basic Taylor factory worker output distribution."""
    print("\n[Visualization 1] Taylor Factory Worker Output")
    print("-" * 70)

    np.random.seed(42)

    # ILLUSTRATIVE inputs (hand-set, not calibrated to any real factory):
    # standard minutes per task, rest minutes per hour, and a worker-efficiency
    # spread of N(1.0, 0.15). Output is in arbitrary "units".
    n_workers = 50
    work_hours = 10
    standard_times = {'task_A': 3.2, 'task_B': 5.1, 'task_C': 4.7, 'rest': 10.0}
    worker_efficiency = np.random.normal(1.0, 0.15, n_workers)
    worker_efficiency = np.clip(worker_efficiency, 0.5, 1.5)

    effective_minutes = work_hours * 60 - work_hours * standard_times['rest']
    tasks = ['task_A', 'task_B', 'task_C']
    weights = [0.4, 0.35, 0.25]

    daily_output = np.zeros(n_workers)
    for i in range(n_workers):
        output = 0
        for hour in range(work_hours):
            # Illustrative fatigue curve: -3% speed per hour, floored at 0.4
            fatigue = max(1.0 - 0.03 * hour, 0.4)
            hour_minutes = 60 - standard_times['rest']
            for task, w in zip(tasks, weights):
                task_time = standard_times[task] / (worker_efficiency[i] * fatigue)
                output += (hour_minutes * w) / task_time
        daily_output[i] = output

    plt.figure(figsize=(12, 7))
    plt.hist(daily_output, bins=15, color='#2E86AB', edgecolor='white', alpha=0.85)
    plt.axvline(np.mean(daily_output), color='red', linestyle='--', linewidth=2,
                label=f'平均 = {np.mean(daily_output):.1f} 單位')
    plt.xlabel('每日產出 (單位)', fontsize=12)
    plt.ylabel('工人數量', fontsize=12)
    plt.title('泰勒制工廠：工人每日產出分佈\n(Taylorist Factory: Daily Worker Output)',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('taylor_output.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  Mean output: {np.mean(daily_output):.1f} units/worker/day")
    print(f"  Std: {np.std(daily_output):.1f} units")
    print("  (arbitrary units from hand-set inputs; not Taylor's Bethlehem figures)")


# ============================================================================
# Visualization 2: Uber Earnings Distribution (Basic)
# ============================================================================

def uber_basic():
    """Basic Uber driver daily earnings distribution."""
    print("\n[Visualization 2] Uber Driver Earnings")
    print("-" * 70)

    np.random.seed(42)

    # ILLUSTRATIVE inputs (hand-set, not Uber data): a rating spread of
    # N(4.7, 0.2) clipped to 4.0-5.0, a round 22% commission (NOT an official
    # Uber figure), a $12 average fare and 2.5 trips per hour. The dollar
    # amounts are not calibrated to real driver earnings.
    n_drivers = 50
    work_hours = 10
    driver_ratings = np.random.normal(4.7, 0.2, n_drivers)
    driver_ratings = np.clip(driver_ratings, 4.0, 5.0)
    platform_commission = 0.22
    base_fare = 12.0
    trips_per_hour = 2.5

    rating_bonus = (driver_ratings - 4.0) / 1.0
    daily_gross = np.zeros(n_drivers)
    for i in range(n_drivers):
        trip_rate = trips_per_hour * (0.7 + 0.3 * rating_bonus[i])
        total_trips = trip_rate * work_hours
        variation = np.random.normal(1.0, 0.15)
        daily_gross[i] = total_trips * base_fare * variation

    daily_net = daily_gross * (1 - platform_commission)

    plt.figure(figsize=(12, 7))
    plt.hist(daily_net, bins=15, color='#1ABC9C', edgecolor='white', alpha=0.85)
    plt.axvline(np.mean(daily_net), color='red', linestyle='--', linewidth=2,
                label=f'平均 = ${np.mean(daily_net):.0f}')
    plt.axvline(np.median(daily_net), color='orange', linestyle=':', linewidth=2,
                label=f'中位數 = ${np.median(daily_net):.0f}')
    plt.xlabel('每日淨收入 (美元)', fontsize=12)
    plt.ylabel('司機數量', fontsize=12)
    plt.title('Uber 司機每日收入分佈 (扣除22%平台抽成)\n'
              '(Uber Driver Daily Net Earnings)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('uber_earnings.png', dpi=150, bbox_inches='tight')
    plt.show()

    print(f"  Mean daily net: ${np.mean(daily_net):.2f}")
    print(f"  Median daily net: ${np.median(daily_net):.2f}")
    # Article: "a daily-income Gini of about 0.1" in the simulated UberAlgorithm
    # model. This simplified free version prints about 0.08 (seed 42): the gap
    # between drivers is modest; the article's point is about the dispatch rules
    # the drivers cannot see, not about the size of the gap.
    print(f"  Gini of daily net income: {gini(daily_net):.2f}")
    print("  (toy model with hand-set inputs; not real Uber driver earnings)")


# ============================================================================
# Visualization 3: Basic Comparison Chart
# ============================================================================

def basic_comparison():
    """Basic comparison of Taylor vs Uber management dimensions."""
    print("\n[Visualization 3] Taylor vs Uber Basic Comparison")
    print("-" * 70)

    categories = ['監控可見度', '工人時間自主', '規則透明度',
                   '收入穩定性', '管理成本']
    categories_en = ['Surveillance visibility', 'Worker time autonomy',
                     'Rule transparency', 'Income stability', 'Management cost']
    # HAND-SET illustrative scores on a 0-1 scale, chosen to encode the
    # mechanisms discussed in the article. They are NOT measured data.
    taylor = [0.9, 0.1, 0.8, 0.9, 0.7]
    uber = [0.2, 0.7, 0.2, 0.3, 0.3]

    x = np.arange(len(categories))
    width = 0.35

    plt.figure(figsize=(12, 7))
    bars1 = plt.bar(x - width / 2, taylor, width, label='泰勒制 (1900s)',
                    color='#E67E22', edgecolor='white', linewidth=1.5)
    bars2 = plt.bar(x + width / 2, uber, width, label='Uber 演算法 (2015+)',
                    color='#8E44AD', edgecolor='white', linewidth=1.5)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, h + 0.02,
                     f'{h:.1f}', ha='center', va='bottom', fontsize=10,
                     fontweight='bold')

    plt.xticks(x, categories, fontsize=11)
    plt.ylabel('指標值 (0=低, 1=高)', fontsize=12)
    plt.title('泰勒制 vs 演算法管理：關鍵維度比較\n'
              '(Taylor vs Algorithm: Key Dimensions)',
              fontsize=14, fontweight='bold')
    plt.ylim(0, 1.15)
    plt.legend(fontsize=11)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('discipline_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("  Hand-set illustrative scores (0-1):")
    for name, t, u in zip(categories_en, taylor, uber):
        print(f"    {name}: Taylor {t:.1f} vs Uber {u:.1f}")
    print("  Taylor: high visibility, low autonomy, high transparency")
    print("  Uber: low visibility, high autonomy, low transparency")


# ============================================================================
# Income Volatility Check (text only): the GigEconomyModel shown in the article
# ============================================================================

def gig_income_check():
    """Fixed wage vs gig income, 100 workers x 365 days (no plot)."""
    print("\n[Income Volatility Check] Fixed wage vs gig income")
    print("-" * 70)

    np.random.seed(42)

    # ILLUSTRATIVE inputs (hand-set): a traditional worker earns a fixed $100
    # per day; the gig worker's $100 base is multiplied by four random factors.
    n_workers = 100
    n_days = 365
    base_daily = 100
    earnings = np.zeros((n_workers, n_days))
    for w in range(n_workers):
        for d in range(n_days):
            day_of_week = d % 7
            # Demand fluctuation: weekends (days 5, 6) high, weekdays low
            demand = np.random.uniform(1.2, 1.5) if day_of_week in [5, 6] \
                else np.random.uniform(0.8, 1.1)
            # Personal efficiency variation (fatigue, illness)
            efficiency = np.clip(np.random.normal(1.0, 0.15), 0.5, 1.5)
            # Platform algorithm fluctuation (rating changes, dispatch adjustments)
            algorithm = np.clip(np.random.normal(1.0, 0.2), 0.6, 1.4)
            # Competitive pressure (number of other drivers online)
            competition = np.random.uniform(0.85, 1.15)
            earnings[w, d] = max(0, base_daily * demand *
                                 efficiency * algorithm * competition)

    mean_income = earnings.mean()
    cv = earnings.std() / mean_income
    low_share = (earnings < 50).mean()
    low_days_per_worker = (earnings < 50).sum(axis=1).mean()

    print(f"  Traditional worker: fixed ${base_daily}/day (zero variance)")
    print(f"  Gig worker mean daily income: ${mean_income:.2f}")
    print(f"  Coefficient of variation: {cv * 100:.1f}%")
    print(f"  Days under $50: {low_share * 100:.1f}% "
          f"(about {low_days_per_worker:.1f} days per worker per year)")
    print("  (model output under hand-set assumptions; not measured Uber data)")


# ============================================================================
# Execute All Visualizations
# ============================================================================

taylorist_basic()
uber_basic()
basic_comparison()
gig_income_check()

# ============================================================================
# Premium Content Notice
# ============================================================================

print("\n" + "=" * 70)
print("Free Version Complete!")
print("=" * 70)
print()
print("This free version includes 3 basic visualizations and 1 text-only income check.")
print()
print("Premium version includes 14 professional sub-plots:")
print("  - TayloristFactory simulation (4 sub-plots)")
print("    Worker output, efficiency vs fatigue, schedule, cost structure")
print("  - UberAlgorithm simulation (4 sub-plots)")
print("    Earnings distribution, rating vs earnings, surge pricing, revenue split")
print("  - Two-systems comparison (3 sub-plots)")
print("    Surveillance metrics, worker autonomy radar, information asymmetry")
print("  - Gig economy income stability (2 sub-plots)")
print("    Monthly volatility, income Lorenz curve with Gini coefficient")
print("  - Algorithm black box visualization (1 sub-plot)")
print("    Decision tree opacity comparison")
print()
print("Upgrade to premium for the complete analysis!")
