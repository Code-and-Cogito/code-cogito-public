"""
Finance, Bubbles & Crises #02: South Sea Bubble vs Dot-com Bubble
Free Version -- 5 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: P/E Deviation -- "This Time Is Different" Index
# ============================================================
print("=" * 65)
print("MODEL 1: P/E Deviation -- 'This Time Is Different' Index")
print("=" * 65)

ss_quarters = ['1719Q1','1719Q2','1719Q3','1719Q4',
               '1720Q1','1720Q2','1720Q3','1720Q4',
               '1721Q1','1721Q2']
ss_pe = np.array([12, 14, 15, 18, 35, 85, 160, 105, 15, 11])
ss_hist_avg = 14

nq_quarters = ['1998Q1','1998Q2','1998Q3','1998Q4',
               '1999Q1','1999Q2','1999Q3','1999Q4',
               '2000Q1','2000Q2','2000Q3','2000Q4',
               '2001Q1','2001Q2','2001Q3','2001Q4',
               '2002Q1','2002Q2']
nq_pe = np.array([22, 25, 24, 30, 38, 50, 65, 95,
                  120, 150, 85, 55, 40, 35, 28, 22, 18, 16])
nq_hist_avg = 20

ss_deviation = ss_pe / ss_hist_avg
nq_deviation = nq_pe / nq_hist_avg

corr = np.corrcoef(ss_deviation[:10], nq_deviation[4:14])[0, 1]

print(f"\n  South Sea peak deviation: {ss_deviation.max():.1f}x "
      f"(at {ss_quarters[np.argmax(ss_deviation)]})")
print(f"  NASDAQ peak deviation:    {nq_deviation.max():.1f}x "
      f"(at {nq_quarters[np.argmax(nq_deviation)]})")
print(f"  Correlation: {corr:.2f}")

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("'This Time Is Different' Index -- P/E Deviation from Historical Average\n"
             "Correlation: {:.2f} | Danger zone: >3x historical average".format(corr),
             fontsize=14, fontweight='bold')

# Panel 1: South Sea P/E
ax = axes[0]
colors_ss = ['#E74C3C' if d > 3 else '#F39C12' if d > 1.5 else '#3498DB' for d in ss_deviation]
ax.bar(range(len(ss_quarters)), ss_pe, color=colors_ss, edgecolor='black', linewidth=1)
ax.axhline(y=ss_hist_avg, color='green', linestyle='--', linewidth=2, label=f'Hist avg P/E={ss_hist_avg}')
ax.axhline(y=ss_hist_avg*3, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Danger (3x)')
ax.set_xticks(range(len(ss_quarters)))
ax.set_xticklabels(ss_quarters, rotation=45, fontsize=8)
ax.set_ylabel('P/E Ratio', fontsize=11)
ax.set_title('South Sea Company (1719-1721)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: NASDAQ P/E
ax = axes[1]
colors_nq = ['#E74C3C' if d > 3 else '#F39C12' if d > 1.5 else '#3498DB' for d in nq_deviation]
ax.bar(range(len(nq_quarters)), nq_pe, color=colors_nq, edgecolor='black', linewidth=1)
ax.axhline(y=nq_hist_avg, color='green', linestyle='--', linewidth=2, label=f'Hist avg P/E={nq_hist_avg}')
ax.axhline(y=nq_hist_avg*3, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Danger (3x)')
ax.set_xticks(range(len(nq_quarters)))
ax.set_xticklabels(nq_quarters, rotation=45, fontsize=8)
ax.set_ylabel('P/E Ratio', fontsize=11)
ax.set_title('NASDAQ Tech Stocks (1998-2002)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Deviation overlay
ax = axes[2]
ax.plot(range(len(ss_deviation)), ss_deviation, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=6, label='South Sea')
ax.plot(range(len(nq_deviation)), nq_deviation, 's-', color='#E67E22', linewidth=2.5,
        markersize=5, label='NASDAQ (shifted)')
ax.axhline(y=3, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Danger threshold (3x)')
ax.axhline(y=1, color='green', linestyle='--', linewidth=1, alpha=0.5, label='Historical average')
ax.set_xlabel('Quarter Index', fontsize=11)
ax.set_ylabel('Deviation (multiples of hist avg)', fontsize=11)
ax.set_title('Deviation Curves Overlaid', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_pe_deviation.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_pe_deviation.png")


# ============================================================
# MODEL 2: IPO Mania Comparison
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: IPO Mania -- 1720 London vs 1999-2000 USA")
print("=" * 65)

ipo_metrics = ['Total IPOs', 'Had Real\nBusiness (%)', 'Survived\n1 Year (%)',
               'First-day\nReturn (%)', 'Underwriter\nFees (%)']
south_sea = [190, 20, 8, 50, 15]
dotcom = [858, 35, 52, 71, 7]

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('IPO Mania: 1720 London vs 1999-2000 Silicon Valley\n'
             'Different century, same playbook: sell exciting stories, collect real money',
             fontsize=14, fontweight='bold')

# Panel 1: Side-by-side comparison
ax = axes[0]
x = np.arange(len(ipo_metrics))
w = 0.35
ax.barh(x - w/2, south_sea, w, color='#8E44AD', alpha=0.8, label='South Sea (1720)',
        edgecolor='black', linewidth=1)
ax.barh(x + w/2, dotcom, w, color='#E67E22', alpha=0.8, label='Dot-com (1999-2000)',
        edgecolor='black', linewidth=1)
ax.set_yticks(x)
ax.set_yticklabels(ipo_metrics, fontsize=9)
ax.set_xlabel('Value', fontsize=11)
ax.set_title('IPO Metrics Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3)

# Panel 2: IPO survival funnel
ax = axes[1]
stages_ipo = ['IPO\nLaunched', 'Had Real\nBusiness', 'Survived\n1 Year', 'Survived\n5 Years']
ss_funnel = [100, 20, 8, 3]
dc_funnel = [100, 35, 52, 22]
ax.plot(range(4), ss_funnel, 'o-', color='#8E44AD', linewidth=2.5, markersize=10,
        label='South Sea era')
ax.fill_between(range(4), ss_funnel, alpha=0.1, color='#8E44AD')
ax.plot(range(4), dc_funnel, 's-', color='#E67E22', linewidth=2.5, markersize=10,
        label='Dot-com era')
ax.fill_between(range(4), dc_funnel, alpha=0.1, color='#E67E22')
ax.set_xticks(range(4))
ax.set_xticklabels(stages_ipo, fontsize=9)
ax.set_ylabel('% Surviving', fontsize=11)
ax.set_title('IPO Survival Funnel', fontsize=12, fontweight='bold')
for i, (s, d) in enumerate(zip(ss_funnel, dc_funnel)):
    ax.text(i, s + 3, f'{s}%', ha='center', color='#8E44AD', fontweight='bold', fontsize=10)
    ax.text(i, d + 3, f'{d}%', ha='center', color='#E67E22', fontweight='bold', fontsize=10)
ax.legend(fontsize=10)
ax.grid(alpha=0.3)
ax.set_ylim(0, 115)

# Panel 3: Who profits from IPO mania
ax = axes[2]
roles = ['Company\nFounders', 'Underwriters\n/Banks', 'Early\nInvestors',
         'Retail\nInvestors']
profit_pct = [25, 35, 28, -88]
colors_p = ['#27AE60' if p > 0 else '#E74C3C' for p in profit_pct]
bars = ax.bar(roles, profit_pct, color=colors_p, edgecolor='black', linewidth=1)
ax.axhline(y=0, color='black', linewidth=1.5)
ax.set_ylabel('Avg Return (%)', fontsize=11)
ax.set_title('Who Profits from IPO Mania?', fontsize=12, fontweight='bold')
for bar, v in zip(bars, profit_pct):
    y_pos = v + 3 if v > 0 else v - 8
    ax.text(bar.get_x() + bar.get_width()/2, y_pos, f'{v:+d}%',
            ha='center', fontweight='bold', fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_ipo_mania.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 02_ipo_mania.png")


# ============================================================
# MODEL 3: Promise vs Reality Gap
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Promise vs Reality -- The Gap That Kills")
print("=" * 65)

companies = ['South Sea\nCompany', 'Pets.com', 'Webvan', 'Boo.com', 'eToys']
promised_revenue = [100, 230, 500, 200, 300]  # claimed market size ($M equiv)
actual_revenue = [0.1, 28.9, 35, 3.5, 24]     # actual revenue ($M)
ratio = [p/a if a > 0 else 1000 for p, a in zip(promised_revenue, actual_revenue)]
survival_months = [96, 9, 24, 18, 24]

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Promise vs Reality: The Gap That Kills Bubbles\n'
             'When stories replace fundamentals, the ending is always the same',
             fontsize=14, fontweight='bold')

# Panel 1: Promise vs Reality bars
ax = axes[0]
x = np.arange(len(companies))
w = 0.35
ax.bar(x - w/2, promised_revenue, w, color='#3498DB', alpha=0.8, label='Promised Market ($M)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, actual_revenue, w, color='#E74C3C', alpha=0.8, label='Actual Revenue ($M)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(companies, fontsize=9)
ax.set_ylabel('$ Millions', fontsize=11)
ax.set_title('Promise vs Actual Revenue', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: Promise/Reality ratio
ax = axes[1]
colors_r = ['#E74C3C' if r > 10 else '#F39C12' for r in ratio]
bars = ax.bar(range(len(companies)), [min(r, 50) for r in ratio], color=colors_r,
              edgecolor='black', linewidth=1)
ax.axhline(y=1, color='green', linestyle='--', linewidth=2, label='Promise = Reality')
ax.set_xticks(range(len(companies)))
ax.set_xticklabels(companies, fontsize=9)
ax.set_ylabel('Promise/Reality Ratio', fontsize=11)
ax.set_title('The Delusion Multiplier', fontsize=12, fontweight='bold')
for i, (bar, r) in enumerate(zip(bars, ratio)):
    label = f'{r:.0f}x' if r < 100 else '1000x+'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            label, ha='center', fontweight='bold', fontsize=10)
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Survival timeline
ax = axes[2]
sorted_idx = np.argsort(survival_months)
companies_sorted = [companies[i] for i in sorted_idx]
months_sorted = [survival_months[i] for i in sorted_idx]
colors_s = plt.cm.RdYlGn(np.linspace(0.1, 0.5, len(companies)))
ax.barh(range(len(companies_sorted)), months_sorted, color=colors_s,
        edgecolor='black', linewidth=1)
ax.set_yticks(range(len(companies_sorted)))
ax.set_yticklabels(companies_sorted, fontsize=9)
ax.set_xlabel('Months Until Collapse', fontsize=11)
ax.set_title('Survival Time', fontsize=12, fontweight='bold')
for i, m in enumerate(months_sorted):
    ax.text(m + 1, i, f'{m} mo', va='center', fontweight='bold', fontsize=10)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_promise_vs_reality.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 03_promise_vs_reality.png")


# ============================================================
# MODEL 4: Rationality Collapse -- Newton's Lesson
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Rationality Collapse -- Even Newton Lost")
print("=" * 65)

timeline_labels = ['Jan\n1720', 'Mar', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Dec\n1720']
ss_price = [128, 330, 500, 890, 950, 1000, 500, 124]
newton_actions = {
    1: ('1st Buy', '#27AE60'),
    2: ('Sell +7K', '#2ECC71'),
    4: ('2nd Buy\n(FOMO)', '#E74C3C'),
    7: ('Stuck\n-20K', '#8B0000'),
}

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle("Newton's Lesson: Intelligence Cannot Defeat Crowd Psychology\n"
             '"I can calculate the motions of heavenly bodies, but not the madness of people"',
             fontsize=14, fontweight='bold')

# Panel 1: Price with Newton's actions
ax = axes[0]
ax.plot(range(len(ss_price)), ss_price, 'o-', color='#2C3E50', linewidth=2.5, markersize=6)
ax.fill_between(range(len(ss_price)), ss_price, alpha=0.1, color='#3498DB')
y_offsets = [80, 100, 60, -120]
offset_idx = 0
for idx, (label, color) in newton_actions.items():
    ax.scatter(idx, ss_price[idx], s=250, color=color, zorder=5,
              edgecolors='black', linewidths=2)
    ax.annotate(label, (idx, ss_price[idx]),
                textcoords="offset points", xytext=(0, y_offsets[offset_idx]),
                ha='center', fontsize=9, fontweight='bold', color=color,
                arrowprops=dict(arrowstyle='->', color=color))
    offset_idx += 1
ax.set_xticks(range(len(timeline_labels)))
ax.set_xticklabels(timeline_labels, fontsize=9)
ax.set_ylabel('South Sea Stock Price (GBP)', fontsize=11)
ax.set_title("Newton's Trading Timeline", fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

# Panel 2: Decision analysis
ax = axes[1]
decisions = ['1st Buy\n(Rational)', '1st Sell\n(Rational)', '2nd Buy\n(FOMO)', 'Final\nResult']
returns = [7000, 7000, -20000, -13000]
colors_d = ['#27AE60', '#27AE60', '#E74C3C', '#E74C3C']
bars = ax.bar(decisions, returns, color=colors_d, edgecolor='black', linewidth=1)
ax.axhline(y=0, color='black', linewidth=1.5)
ax.set_ylabel('Profit/Loss (GBP)', fontsize=11)
ax.set_title('Decision-by-Decision P&L', fontsize=12, fontweight='bold')
for bar, v in zip(bars, returns):
    y_pos = v + 500 if v > 0 else v - 1200
    ax.text(bar.get_x() + bar.get_width()/2, y_pos,
            f'{v:+,}', ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Cognitive biases at play
ax = axes[2]
biases = ['FOMO\n(Fear of\nMissing Out)', 'Social\nProof', 'Loss\nAversion',
          'Sunk Cost\nFallacy', 'Overconfidence']
impact = [95, 85, 90, 70, 80]
colors_b = plt.cm.Reds(np.linspace(0.3, 0.9, len(biases)))
bars = ax.barh(biases, impact, color=colors_b, edgecolor='black', linewidth=1)
ax.set_xlabel('Impact Score (0-100)', fontsize=11)
ax.set_title('Cognitive Biases That Defeated Newton', fontsize=12, fontweight='bold')
for bar, v in zip(bars, impact):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{v}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 110)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_rationality_collapse.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_rationality_collapse.png")


# ============================================================
# MODEL 5: Collapse Chain -- From Peak to Bottom
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Collapse Chain -- Mean Reversion Speed")
print("=" * 65)

# South Sea: price from peak to bottom
ss_months_from_peak = [0, 1, 2, 3, 4, 5, 6]
ss_pct_of_peak = [100, 80, 50, 30, 18, 14, 12.4]

# NASDAQ: price from peak to bottom
nq_months_from_peak = [0, 2, 4, 6, 8, 10, 12, 18, 24, 30]
nq_pct_of_peak = [100, 75, 60, 48, 40, 35, 32, 28, 24, 22]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Collapse Chain: From Peak to Bottom\n'
             'South Sea: 6 months to -88% | NASDAQ: 30 months to -78%',
             fontsize=14, fontweight='bold')

# Panel 1: Decline trajectories
ax = axes[0]
ax.plot(ss_months_from_peak, ss_pct_of_peak, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=8, label='South Sea (1720)')
ax.fill_between(ss_months_from_peak, ss_pct_of_peak, alpha=0.15, color='#8E44AD')
ax.plot(nq_months_from_peak, nq_pct_of_peak, 's-', color='#E67E22', linewidth=2.5,
        markersize=8, label='NASDAQ (2000-02)')
ax.fill_between(nq_months_from_peak, nq_pct_of_peak, alpha=0.15, color='#E67E22')
ax.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='50% decline')
ax.set_xlabel('Months from Peak', fontsize=11)
ax.set_ylabel('% of Peak Value', fontsize=11)
ax.set_title('Decline Trajectory Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

# Panel 2: Speed of crash (% lost per month)
ax = axes[1]
ss_speed = [-(ss_pct_of_peak[i+1] - ss_pct_of_peak[i]) for i in range(len(ss_pct_of_peak)-1)]
nq_speed_raw = [-(nq_pct_of_peak[i+1] - nq_pct_of_peak[i]) /
                 (nq_months_from_peak[i+1] - nq_months_from_peak[i])
                for i in range(len(nq_pct_of_peak)-1)]
ax.bar(np.arange(len(ss_speed)) - 0.18, ss_speed, 0.35, color='#8E44AD', alpha=0.8,
       label='South Sea (%/month)', edgecolor='black', linewidth=1)
nq_x = np.arange(len(nq_speed_raw))
ax.bar(nq_x + 0.18, nq_speed_raw[:len(nq_x)], 0.35, color='#E67E22', alpha=0.8,
       label='NASDAQ (%/month)', edgecolor='black', linewidth=1)
ax.set_xlabel('Period Index', fontsize=11)
ax.set_ylabel('% Lost per Month', fontsize=11)
ax.set_title('Crash Speed Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Total destruction
ax = axes[2]
events = ['South Sea\n(1720)', 'NASDAQ\n(2000)', 'Dot-com\nCompanies\nDestroyed',
          'Market Cap\nEvaporated']
values = [87.6, 78, 48, 78]
units = ['% decline', '% decline', '% of IPOs', '% of NASDAQ']
colors_c = ['#8E44AD', '#E67E22', '#E74C3C', '#C0392B']
bars = ax.bar(events, values, color=colors_c, edgecolor='black', linewidth=1, alpha=0.85)
ax.set_ylabel('Percentage', fontsize=11)
ax.set_title('Total Destruction Metrics', fontsize=12, fontweight='bold')
for bar, v, u in zip(bars, values, units):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{v}%\n({u})', ha='center', fontweight='bold', fontsize=9)
ax.set_ylim(0, 105)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_collapse_chain.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 05_collapse_chain.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("=" * 65)
