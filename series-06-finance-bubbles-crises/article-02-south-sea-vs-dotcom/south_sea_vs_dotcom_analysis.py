"""
Finance, Bubbles & Crises #02: South Sea Bubble vs Dot-com Bubble
Free Version -- 5 Illustrative Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install matplotlib numpy

DATA NOTE -- please read
------------------------
These five models are illustrations, not empirical studies.

  * Hand-set inputs (marked ILLUSTRATIVE in the code; NOT measured data):
    the P/E paths and "historical average" P/E in Model 1, the "who profits"
    returns in Model 2, every value in Model 3, the bias scores in Model 4 and
    the intermediate points of the NASDAQ path in Model 5.
  * Values taken from sources (the source is named in a comment next to each):
    US IPO counts and first-day returns (Ritter), the "nearly 200" share
    projects of 1720 (Scott's tally, as cited by Odlyzko), South Sea share-price
    milestones and Newton's figures (Odlyzko), Pets.com figures (SEC filings)
    and the NASDAQ Composite peak and low.

Search this file for "ILLUSTRATIVE" to find every hand-set input.
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
print("(all P/E values are hand-set ILLUSTRATIVE inputs)")
print("=" * 65)

# ILLUSTRATIVE: hand-set P/E path, not historical records (1719-1721, quarterly)
ss_quarters = ['1719Q1','1719Q2','1719Q3','1719Q4',
               '1720Q1','1720Q2','1720Q3','1720Q4',
               '1721Q1','1721Q2']
ss_pe = np.array([12, 14, 15, 18, 35, 85, 160, 105, 15, 11])
ss_hist_avg = 14  # ILLUSTRATIVE: assumed "historical average" P/E

# ILLUSTRATIVE: hand-set P/E path, not market data (1998-2002, quarterly)
nq_quarters = ['1998Q1','1998Q2','1998Q3','1998Q4',
               '1999Q1','1999Q2','1999Q3','1999Q4',
               '2000Q1','2000Q2','2000Q3','2000Q4',
               '2001Q1','2001Q2','2001Q3','2001Q4',
               '2002Q1','2002Q2']
nq_pe = np.array([22, 25, 24, 30, 38, 50, 65, 95,
                  120, 150, 85, 55, 40, 35, 28, 22, 18, 16])
nq_hist_avg = 20  # ILLUSTRATIVE: assumed "historical average" P/E

ss_deviation = ss_pe / ss_hist_avg
nq_deviation = nq_pe / nq_hist_avg


def aligned_corr(nq_start):
    """Correlate the 10 South Sea quarters with 10 NASDAQ quarters from nq_start."""
    return np.corrcoef(ss_deviation[:10], nq_deviation[nq_start:nq_start + 10])[0, 1]


def quarters_to_revert(dev, threshold=1.5):
    """Quarters from the peak onward whose deviation is still above the threshold."""
    peak = int(np.argmax(dev))
    return int(np.sum(dev[peak:] > threshold))


# The result depends on how the two curves are lined up: the main figure uses
# the NASDAQ quarters starting at 1999Q1 (index 4); the scan below shows how far
# the coefficient moves when the start is shifted.
corr = aligned_corr(4)

print(f"\n  South Sea peak deviation: {ss_deviation.max():.1f}x "
      f"(at {ss_quarters[np.argmax(ss_deviation)]})")
print(f"  NASDAQ peak deviation:    {nq_deviation.max():.1f}x "
      f"(at {nq_quarters[np.argmax(nq_deviation)]})")
print(f"  Correlation (NASDAQ from 1999Q1): {corr:.2f}")
print(f"  Alignment check: start at 1998Q4 -> {aligned_corr(3):.2f}, "
      f"start at 1998Q3 -> {aligned_corr(2):.2f}  (it depends on the alignment)")

ss_first_danger = next(q for q, d in zip(ss_quarters, ss_deviation) if d > 3)
nq_first_danger = next(q for q, d in zip(nq_quarters, nq_deviation) if d > 3)
print(f"  First quarter above the 3x line (the 3x line is an arbitrary choice): "
      f"South Sea {ss_first_danger}, NASDAQ {nq_first_danger}")
print("  Quarters to revert (dev < 1.5x):")
print(f"    South Sea: {quarters_to_revert(ss_deviation)} quarters")
print(f"    NASDAQ:    {quarters_to_revert(nq_deviation)} quarters")

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle("'This Time Is Different' Index -- P/E Deviation from an Assumed Historical Average\n"
             "Hand-set illustrative values | Correlation: {:.2f} (depends on alignment) | "
             "3x line: author's choice".format(corr),
             fontsize=14, fontweight='bold')

# Panel 1: South Sea P/E
ax = axes[0]
colors_ss = ['#E74C3C' if d > 3 else '#F39C12' if d > 1.5 else '#3498DB' for d in ss_deviation]
ax.bar(range(len(ss_quarters)), ss_pe, color=colors_ss, edgecolor='black', linewidth=1)
ax.axhline(y=ss_hist_avg, color='green', linestyle='--', linewidth=2, label=f'Assumed avg P/E={ss_hist_avg}')
ax.axhline(y=ss_hist_avg*3, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='3x line')
ax.set_xticks(range(len(ss_quarters)))
ax.set_xticklabels(ss_quarters, rotation=45, fontsize=8)
ax.set_ylabel('P/E Ratio (illustrative)', fontsize=11)
ax.set_title('South Sea Company (1719-1721, illustrative)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 2: NASDAQ P/E
ax = axes[1]
colors_nq = ['#E74C3C' if d > 3 else '#F39C12' if d > 1.5 else '#3498DB' for d in nq_deviation]
ax.bar(range(len(nq_quarters)), nq_pe, color=colors_nq, edgecolor='black', linewidth=1)
ax.axhline(y=nq_hist_avg, color='green', linestyle='--', linewidth=2, label=f'Assumed avg P/E={nq_hist_avg}')
ax.axhline(y=nq_hist_avg*3, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='3x line')
ax.set_xticks(range(len(nq_quarters)))
ax.set_xticklabels(nq_quarters, rotation=45, fontsize=8)
ax.set_ylabel('P/E Ratio (illustrative)', fontsize=11)
ax.set_title('NASDAQ Tech Stocks (1998-2002, illustrative)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Deviation overlay
ax = axes[2]
ax.plot(range(len(ss_deviation)), ss_deviation, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=6, label='South Sea')
ax.plot(range(len(nq_deviation)), nq_deviation, 's-', color='#E67E22', linewidth=2.5,
        markersize=5, label='NASDAQ (as typed, not shifted)')
ax.axhline(y=3, color='red', linestyle='--', linewidth=2, alpha=0.7, label='3x line (author\'s choice)')
ax.axhline(y=1, color='green', linestyle='--', linewidth=1, alpha=0.5, label='Assumed average')
ax.set_xlabel('Quarter Index', fontsize=11)
ax.set_ylabel('Deviation (multiples of assumed avg)', fontsize=11)
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

# --- Sourced counts ---------------------------------------------------------
# 1720: "nearly 200" share projects were announced in 1719-20 (Scott's tally, as
# cited by Odlyzko, "An undertaking of great advantage, but nobody to know what
# it is", Financial History, 2020). They were announced projects, not all were
# ever formed, and they are not IPOs in the modern sense. 200 is only a plotting
# value standing in for "nearly 200".
south_sea_projects = 200

# US IPOs: Jay R. Ritter, "Initial Public Offerings: Updated Statistics",
# Table 1 (University of Florida): number of IPOs and average first-day return (%).
# https://site.warrington.ufl.edu/ritter/files/IPO-Statistics.pdf
ritter_years = [1997, 1998, 1999, 2000]
ritter_ipos = [474, 283, 476, 380]
ritter_first_day = [14.0, 21.9, 71.2, 56.3]
dotcom_ipos = ritter_ipos[2] + ritter_ipos[3]  # 1999 + 2000 = 856
dotcom_weighted_return = (sum(n * r for n, r in zip(ritter_ipos[2:], ritter_first_day[2:]))
                          / dotcom_ipos)

# ILLUSTRATIVE: hand-set "who profits" returns (author-assigned, NOT measured data)
roles = ['Company\nFounders', 'Underwriters\n/Banks', 'Early\nInvestors',
         'Retail\nInvestors']
profit_pct = [25, 35, 28, -88]

print("\n  1720 London: nearly 200 share projects announced "
      "(Scott's tally via Odlyzko; not all were formed)")
print("  US IPOs (Ritter, Table 1):")
for y, n, r in zip(ritter_years, ritter_ipos, ritter_first_day):
    print(f"    {y}: {n:>4} IPOs, average first-day return {r:.1f}%")
print(f"  1997-2000 total: {sum(ritter_ipos):,} IPOs")
print(f"  1999-2000 total: {dotcom_ipos} IPOs; first-day return weighted by "
      f"number of deals: {dotcom_weighted_return:.1f}%")
print("  Panel 3 ('who profits') uses hand-set ILLUSTRATIVE returns, not measured data.")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('IPO Mania: 1720 London vs 1999-2000 USA\n'
             'Different century, same playbook: sell exciting stories, collect real money',
             fontsize=14, fontweight='bold')

# Panel 1: scale of the two manias (counts are not like-for-like)
ax = axes[0]
labels_p1 = ['1720 London\n(share projects\nannounced)', '1999-2000 USA\n(IPOs)']
vals_p1 = [south_sea_projects, dotcom_ipos]
text_p1 = ['nearly 200', f'{dotcom_ipos}']
bars = ax.bar(labels_p1, vals_p1, color=['#8E44AD', '#E67E22'], alpha=0.85,
              edgecolor='black', linewidth=1)
for bar, t in zip(bars, text_p1):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15, t,
            ha='center', fontweight='bold', fontsize=12)
ax.set_ylabel('Count', fontsize=11)
ax.set_ylim(0, 1000)
ax.set_title('Scale (not like-for-like)', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Panel 2: Ritter's yearly counts and first-day returns
ax = axes[1]
xs = np.arange(len(ritter_years))
ax.bar(xs, ritter_ipos, color='#E67E22', alpha=0.8, edgecolor='black', linewidth=1)
for i, v in enumerate(ritter_ipos):
    ax.text(i, v + 12, str(v), ha='center', fontweight='bold', fontsize=10)
ax.set_xticks(xs)
ax.set_xticklabels(ritter_years)
ax.set_ylabel('US IPOs per year (count)', fontsize=11)
ax.set_ylim(0, 900)
ax2 = ax.twinx()
ax2.plot(xs, ritter_first_day, 'o-', color='#2C3E50', linewidth=2.5, markersize=8)
for i, v in enumerate(ritter_first_day):
    ax2.text(i, v + 4, f'{v:.1f}%', ha='center', color='#2C3E50',
             fontweight='bold', fontsize=10)
ax2.set_ylabel('Average first-day return (%)', fontsize=11)
ax2.set_ylim(0, 100)
ax.set_title('US IPOs and first-day returns (Ritter)', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Who profits from IPO mania (ILLUSTRATIVE)
ax = axes[2]
colors_p = ['#27AE60' if p > 0 else '#E74C3C' for p in profit_pct]
bars = ax.bar(roles, profit_pct, color=colors_p, edgecolor='black', linewidth=1)
ax.axhline(y=0, color='black', linewidth=1.5)
ax.set_ylabel('Illustrative return (%)', fontsize=11)
ax.set_title('Who Profits from IPO Mania?\n(hand-set illustrative values, not measured)',
             fontsize=12, fontweight='bold')
for bar, v in zip(bars, profit_pct):
    y_pos = v + 3 if v > 0 else v - 8
    ax.text(bar.get_x() + bar.get_width()/2, y_pos, f'{v:+d}%',
            ha='center', fontweight='bold', fontsize=11)
ax.set_ylim(-110, 55)
ax.grid(axis='y', alpha=0.3)

fig.text(0.5, -0.01,
         "Sources: 1720 count = Scott's tally via Odlyzko (2020); US IPO counts and first-day returns = "
         "Ritter, Initial Public Offerings: Updated Statistics (Table 1).\n"
         "The two counts measure different things. Panel 3 is illustrative only.",
         ha='center', fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_ipo_mania.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 02_ipo_mania.png")


# ============================================================
# MODEL 3: Promise vs Reality Gap
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Promise vs Reality -- The Gap That Kills")
print("(illustrative index values, NOT dollars or measured data)")
print("=" * 65)

# ILLUSTRATIVE: hand-set index values in arbitrary units. The "promise" of each
# company's story is normalised to 100; "delivered" is what the story delivered,
# in the same arbitrary units. These are NOT dollar amounts, market sizes or
# revenues. (An earlier version labelled similar numbers "$M"; those labels
# implied sourced figures, which they were not.)
companies = ['South Sea\nCompany', 'Pets.com', 'Webvan', 'Boo.com', 'eToys']
promised = [100, 100, 100, 100, 100]
delivered = [0.1, 12, 7, 2, 8]
ratio = [p / d for p, d in zip(promised, delivered)]
# ILLUSTRATIVE: approximate, hand-typed months from launch to collapse
survival_months = [96, 9, 24, 18, 24]

# SOURCED (printed, not charted): Pets.com Inc., Form 10-Q for the quarter ended
# 30 Sep 2000, SEC EDGAR -- first nine months of 2000, in $ millions (about).
petscom_sales = 25.78
petscom_cost_of_goods = 32.67
petscom_operating_loss = 86.7
print("\n  Pets.com, first nine months of 2000 (SEC Form 10-Q, about):")
print(f"    Sales ${petscom_sales:.1f}M, cost of goods ${petscom_cost_of_goods:.1f}M "
      f"-> ${petscom_cost_of_goods/petscom_sales:.2f} of cost per $1 of goods sold")
print(f"    Operating loss ${petscom_operating_loss:.1f}M "
      f"= {petscom_operating_loss/petscom_sales:.1f}x sales")
print("  (The chart below uses the illustrative index values, not these filed figures.)")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Promise vs Reality: The Gap Between Story and Result\n'
             'Illustrative index values (hand-set, arbitrary units) -- not dollars, not measured data',
             fontsize=14, fontweight='bold')

# Panel 1: Promise vs Reality bars
ax = axes[0]
x = np.arange(len(companies))
w = 0.35
ax.bar(x - w/2, promised, w, color='#3498DB', alpha=0.8, label='Promise (= 100)',
       edgecolor='black', linewidth=1)
ax.bar(x + w/2, delivered, w, color='#E74C3C', alpha=0.8, label='Delivered (illustrative)',
       edgecolor='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(companies, fontsize=9)
ax.set_ylabel('Illustrative index (arbitrary units)', fontsize=11)
ax.set_title('Promise vs Delivered (illustrative)', fontsize=12, fontweight='bold')
ax.set_ylim(0, 125)
ax.legend(fontsize=9, loc='upper right')
ax.grid(axis='y', alpha=0.3)

# Panel 2: Promise/Reality ratio
ax = axes[1]
colors_r = ['#E74C3C' if r > 10 else '#F39C12' for r in ratio]
bars = ax.bar(range(len(companies)), [min(r, 100) for r in ratio], color=colors_r,
              edgecolor='black', linewidth=1)
ax.axhline(y=1, color='green', linestyle='--', linewidth=2, label='Promise = Reality')
ax.set_xticks(range(len(companies)))
ax.set_xticklabels(companies, fontsize=9)
ax.set_ylabel('Promise/Delivered ratio (illustrative)', fontsize=11)
ax.set_title('The "Delusion Multiplier" (illustrative)', fontsize=12, fontweight='bold')
for i, (bar, r) in enumerate(zip(bars, ratio)):
    label = f'{r:.0f}x' if r < 100 else '100x+'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            label, ha='center', fontweight='bold', fontsize=10)
ax.set_ylim(0, 115)
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
ax.set_xlabel('Months Until Collapse (approximate, hand-typed)', fontsize=11)
ax.set_title('Survival Time (approximate)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 115)
for i, m in enumerate(months_sorted):
    ax.text(m + 1, i, f'~{m} mo', va='center', fontweight='bold', fontsize=10)
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

# South Sea share-price milestones in 1720 (GBP, approximate; price series differ
# slightly). Source: Odlyzko (2019), "Newton's financial misadventures in the
# South Sea Bubble", Notes and Records of the Royal Society 73(1); Odlyzko (2020).
timeline_labels = ['Jan\n1720', 'Mar', 'End\nMay', 'Early\nJun', 'Early\nAug',
                   'End\nSep', 'End\nDec']
ss_price = [128, 330, 550, 890, 1000, 150, 100]
# (end of 1720: about 100-125 depending on the series; 100 is plotted)

# Newton's figures (GBP), following Odlyzko (2019): sold much of his holding in
# spring 1720 for a profit of about 20,000 (older accounts: 7,000); bought back
# around mid-June at about twice the price; total loss at least 10,000 (family
# lore: 20,000).
newton_figures = [20000, 7000, -10000, -20000]
newton_labels = ['Spring sale:\nprofit\n(Odlyzko)', 'Spring sale:\nprofit\n(older accounts)',
                 'Total loss\n(at least,\nOdlyzko)', 'Total loss\n(family lore)']
newton_value_text = ['+20,000\n(about)', '+7,000', '-10,000\n(at least)', '-20,000']

# ILLUSTRATIVE: author-assigned bias scores (0-100), NOT measured. Newton left no
# record of his motives, so attributing his loss to these biases is a later reading.
biases = ['FOMO\n(Fear of\nMissing Out)', 'Social\nProof', 'Loss\nAversion',
          'Sunk Cost\nFallacy', 'Overconfidence']
impact = [95, 85, 90, 70, 80]

print("\n  South Sea share price, approximate milestones (GBP):")
for lbl, p in zip(timeline_labels, ss_price):
    print(f"    {lbl.replace(chr(10), ' '):<12} {p:>5}")
print("  Newton (Odlyzko): sold much of his holding in spring 1720 (profit about 20,000;")
print("    older accounts: 7,000), bought back around mid-June at about twice the price;")
print("    total loss at least 10,000 (family lore: 20,000).")
print("  Quote: reportedly he 'could not calculate the madness of the people' (earliest")
print("    record: notes of 1756, published 1820; the heavenly-bodies half is a later addition).")
print("  Panel 3 bias scores are hand-set ILLUSTRATIVE values, not measured data.")

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle("Newton and the South Sea Bubble: Even a Genius Lost Money\n"
             'Reportedly he "could not calculate the madness of the people" '
             '(earliest record: notes of 1756, published 1820)',
             fontsize=14, fontweight='bold')

# Panel 1: Price with Newton's actions
ax = axes[0]
ax.plot(range(len(ss_price)), ss_price, 'o-', color='#2C3E50', linewidth=2.5, markersize=6)
ax.fill_between(range(len(ss_price)), ss_price, alpha=0.1, color='#3498DB')
# Spring 1720: sold much of the holding (shaded span Mar -> end May)
ax.axvspan(1, 2, color='#2ECC71', alpha=0.2)
ax.annotate('Spring 1720: sold much of\nhis holding (profit about\n20,000; older accounts 7,000)',
            xy=(1.5, 440), xytext=(0.0, 700), ha='left', fontsize=9, fontweight='bold',
            color='#1E8449', arrowprops=dict(arrowstyle='->', color='#1E8449'))
# Mid-June: bought back at about twice the price
ax.scatter(3, ss_price[3], s=250, color='#E74C3C', zorder=5, edgecolors='black', linewidths=2)
ax.annotate('Bought back around\nmid-June at about\ntwice the price', xy=(3, ss_price[3]),
            xytext=(2.6, 250), ha='center', fontsize=9, fontweight='bold', color='#E74C3C',
            arrowprops=dict(arrowstyle='->', color='#E74C3C'))
# End of 1720: total loss
ax.scatter(6, ss_price[6], s=250, color='#8B0000', zorder=5, edgecolors='black', linewidths=2)
ax.annotate('Total loss: at least 10,000\n(family lore: 20,000)', xy=(6, ss_price[6]),
            xytext=(5.3, 800), ha='center', fontsize=9, fontweight='bold', color='#8B0000',
            arrowprops=dict(arrowstyle='->', color='#8B0000'))
ax.set_xlim(-0.3, 6.6)
ax.set_xticks(range(len(timeline_labels)))
ax.set_xticklabels(timeline_labels, fontsize=9)
ax.set_ylabel('South Sea Stock Price (GBP, approximate)', fontsize=11)
ax.set_title("Newton's Trading Timeline\n(milestones are not evenly spaced in time)",
             fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)

# Panel 2: Newton's figures
ax = axes[1]
colors_d = ['#27AE60', '#27AE60', '#E74C3C', '#E74C3C']
bars = ax.bar(newton_labels, newton_figures, color=colors_d, edgecolor='black', linewidth=1)
ax.axhline(y=0, color='black', linewidth=1.5)
ax.set_ylabel('Profit/Loss (GBP)', fontsize=11)
ax.set_ylim(-29000, 27000)
ax.set_title("Newton's Figures: Published Estimates\n(Odlyzko vs older accounts / family lore)",
             fontsize=12, fontweight='bold')
for bar, v, t in zip(bars, newton_figures, newton_value_text):
    y_pos = v + 600 if v > 0 else v - 600
    ax.text(bar.get_x() + bar.get_width()/2, y_pos, t, ha='center',
            va='bottom' if v > 0 else 'top', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Cognitive biases (ILLUSTRATIVE)
ax = axes[2]
colors_b = plt.cm.Reds(np.linspace(0.3, 0.9, len(biases)))
bars = ax.barh(biases, impact, color=colors_b, edgecolor='black', linewidth=1)
ax.set_xlabel('Illustrative score (0-100, author-assigned, not measured)', fontsize=11)
ax.set_title("Biases Often Blamed for Newton's Loss\n(a later reading; his motives are undocumented)",
             fontsize=12, fontweight='bold')
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
# MODEL 5: Peak to Bottom -- How Fast Did Prices Fall?
# (File name 05_collapse_chain.png is kept; this plots price paths,
#  it is not a contagion or credit-chain model.)
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Peak to Bottom -- How Fast Did Prices Fall?")
print("=" * 65)

# South Sea: approximate milestones counted from the early-August 1720 peak
# (about 1,000), per Odlyzko: about 150 at the end of September, about 100-125 at
# the end of the year (100 is used here).
ss_peak_price = 1000
ss_months_from_peak = [0, 2, 5]
ss_prices_after_peak = [1000, 150, 100]
ss_pct_of_peak = [p / ss_peak_price * 100 for p in ss_prices_after_peak]

# NASDAQ Composite: close of 5,048.62 on 10 Mar 2000; low of about 1,114 in Oct
# 2002 (about 31 months later).
nq_peak, nq_low, nq_months_to_low = 5048.62, 1114.0, 31
nq_decline = (1 - nq_low / nq_peak) * 100
# ILLUSTRATIVE: the intermediate points are hand-typed; only the first and the
# last point of this path come from the figures above.
nq_months_from_peak = [0, 2, 4, 6, 8, 10, 12, 18, 24, nq_months_to_low]
nq_pct_of_peak = [100, 75, 60, 48, 40, 35, 32, 28, 24, nq_low / nq_peak * 100]

ss_fall_sep = 100 - ss_pct_of_peak[1]   # peak -> end of September
ss_fall_end = 100 - ss_pct_of_peak[2]   # peak -> end of year
ss_speed_sep = ss_fall_sep / ss_months_from_peak[1]
ss_speed_end = ss_fall_end / ss_months_from_peak[2]
nq_speed = nq_decline / nq_months_to_low

print("\n  South Sea (1,000 -> about 150 by end Sep -> about 100 at year-end):")
print(f"    peak to end of September (~{ss_months_from_peak[1]} months): -{ss_fall_sep:.0f}%  "
      f"(~{ss_speed_sep:.1f} points of peak value per month)")
print(f"    peak to year-end (~{ss_months_from_peak[2]} months): -{ss_fall_end:.0f}%  "
      f"(~{ss_speed_end:.1f} points per month); with 125 instead of 100: "
      f"-{100 - 125 / ss_peak_price * 100:.1f}%")
print(f"  NASDAQ Composite ({nq_peak:,.2f} -> about {nq_low:,.0f}, ~{nq_months_to_low} months):")
print(f"    decline: -{nq_decline:.0f}%  (~{nq_speed:.1f} points of peak value per month)")
print("  The NASDAQ path in panel 1 has hand-typed ILLUSTRATIVE intermediate points.")

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Peak to Bottom: South Sea vs NASDAQ Composite\n'
             'South Sea: about 5 months to roughly -85% to -90% | '
             'NASDAQ: about 31 months to -78%',
             fontsize=14, fontweight='bold')

# Panel 1: Decline trajectories
ax = axes[0]
ax.plot(ss_months_from_peak, ss_pct_of_peak, 'o-', color='#8E44AD', linewidth=2.5,
        markersize=8, label='South Sea (1720, milestones only)')
ax.fill_between(ss_months_from_peak, ss_pct_of_peak, alpha=0.15, color='#8E44AD')
ax.plot(nq_months_from_peak, nq_pct_of_peak, 's-', color='#E67E22', linewidth=2.5,
        markersize=8, label='NASDAQ (2000-02, intermediate points illustrative)')
ax.fill_between(nq_months_from_peak, nq_pct_of_peak, alpha=0.15, color='#E67E22')
ax.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='50% decline')
ax.set_xlabel('Months from Peak', fontsize=11)
ax.set_ylabel('% of Peak Value', fontsize=11)
ax.set_title('Decline Trajectory Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: Average speed of the decline (points of peak value lost per month)
ax = axes[1]
speed_labels = ['South Sea\npeak to end-Sep\n(~2 months)', 'South Sea\npeak to year-end\n(~5 months)',
                'NASDAQ\npeak to Oct 2002\n(~31 months)']
speeds = [ss_speed_sep, ss_speed_end, nq_speed]
bars = ax.bar(speed_labels, speeds, color=['#8E44AD', '#8E44AD', '#E67E22'], alpha=0.8,
              edgecolor='black', linewidth=1)
for bar, v in zip(bars, speeds):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8, f'{v:.1f}',
            ha='center', fontweight='bold', fontsize=11)
ax.set_ylabel('Average points of peak value lost per month', fontsize=11)
ax.set_title('Average Speed of the Decline', fontsize=12, fontweight='bold')
ax.set_ylim(0, 50)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Peak-to-trough decline
ax = axes[2]
events = ['South Sea\n(1720)', 'NASDAQ Composite\n(2000-02)']
values = [87.5, nq_decline]
texts = ['about 85-90%\n(1,000 to 100-150 pounds)', f'{nq_decline:.0f}%\n({nq_peak:,.0f} to about {nq_low:,.0f})']
bars = ax.bar(events, values, color=['#8E44AD', '#E67E22'], edgecolor='black',
              linewidth=1, alpha=0.85)
ax.set_ylabel('Peak-to-trough decline (%)', fontsize=11)
ax.set_title('Peak-to-Trough Decline (approximate)', fontsize=12, fontweight='bold')
for bar, t in zip(bars, texts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            t, ha='center', va='bottom', fontweight='bold', fontsize=10)
ax.set_ylim(0, 115)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_collapse_chain.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 05_collapse_chain.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 5 MODELS COMPLETE")
print("Output files: 01-05_*.png")
print("Reminder: inputs marked ILLUSTRATIVE in the code are hand-set, not measured data.")
print("=" * 65)
