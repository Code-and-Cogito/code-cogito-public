"""
Finance, Bubbles & Crises #03: 1929 Great Depression vs 2008 Financial Crisis
Free Version -- 6 Models (Basic Analysis)

GitHub: Code-and-Cogito/code-cogito-public
License: MIT

Requirements: pip install networkx matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# MODEL 1: Leverage Evolution -- From Simple to Networked
# ============================================================
print("=" * 65)
print("MODEL 1: Leverage Evolution -- 1920s vs 2000s")
print("=" * 65)

dimensions = ['Leverage\nMultiple', 'Min Margin\nReq (%)', 'Risk\nTransparency',
              'Contagion\nSpeed', 'Regulatory\nCoverage', 'System\nComplexity']
vals_1929 = [10, 10, 60, 30, 15, 20]
vals_2008 = [30, 5, 15, 90, 40, 95]

fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Leverage Evolution: 1920s Margin Trading vs 2000s Derivatives\n'
             'From linear dominos to networked spider webs -- 3x leverage, 10x complexity',
             fontsize=14, fontweight='bold')

# Panel 1: Side-by-side bars
ax = axes[0]
x = np.arange(len(dimensions))
w = 0.35
ax.barh(x - w/2, vals_1929, w, color='#2C3E50', alpha=0.8, label='1920s', edgecolor='black')
ax.barh(x + w/2, vals_2008, w, color='#E74C3C', alpha=0.8, label='2000s', edgecolor='black')
ax.set_yticks(x)
ax.set_yticklabels(dimensions, fontsize=9)
ax.set_xlabel('Score (0-100)', fontsize=11)
ax.set_title('Dimension Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3)

# Panel 2: Radar chart
ax = axes[1]
ax.remove()
ax = fig.add_subplot(1, 3, 2, polar=True)
angles = np.linspace(0, 2*np.pi, len(dimensions), endpoint=False).tolist()
angles += angles[:1]
r1 = vals_1929 + vals_1929[:1]
r2 = vals_2008 + vals_2008[:1]
ax.plot(angles, r1, 'o-', color='#2C3E50', linewidth=2, label='1920s')
ax.fill(angles, r1, alpha=0.15, color='#2C3E50')
ax.plot(angles, r2, 's-', color='#E74C3C', linewidth=2, label='2000s')
ax.fill(angles, r2, alpha=0.15, color='#E74C3C')
ax.set_xticks(angles[:-1])
ax.set_xticklabels([d.replace('\n', ' ') for d in dimensions], fontsize=7)
ax.set_ylim(0, 100)
ax.set_title('Risk Profile Radar', fontsize=12, fontweight='bold', pad=20)
ax.legend(loc='lower right', fontsize=9)

# Panel 3: Leverage chain illustration
ax = axes[2]
chain_1929 = ['Investor', 'Broker\n(Margin)', 'Stock\nMarket']
chain_2008 = ['Homeowner', 'Mortgage\nLender', 'MBS\nPackager', 'CDO\nCreator',
              'CDS\nInsurer', 'Global\nBanks']
y1 = np.ones(len(chain_1929)) * 0.7
y2 = np.ones(len(chain_2008)) * 0.3
x1 = np.linspace(0.1, 0.9, len(chain_1929))
x2 = np.linspace(0.05, 0.95, len(chain_2008))
for i, (xi, label) in enumerate(zip(x1, chain_1929)):
    ax.scatter(xi, 0.7, s=800, color='#2C3E50', zorder=5, edgecolors='black', linewidths=1.5)
    ax.text(xi, 0.7, label, ha='center', va='center', fontsize=7, color='white', fontweight='bold')
    if i < len(chain_1929) - 1:
        ax.annotate('', xy=(x1[i+1]-0.04, 0.7), xytext=(xi+0.04, 0.7),
                    arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=2))
for i, (xi, label) in enumerate(zip(x2, chain_2008)):
    ax.scatter(xi, 0.3, s=600, color='#E74C3C', zorder=5, edgecolors='black', linewidths=1.5)
    ax.text(xi, 0.3, label, ha='center', va='center', fontsize=6, color='white', fontweight='bold')
    if i < len(chain_2008) - 1:
        ax.annotate('', xy=(x2[i+1]-0.03, 0.3), xytext=(xi+0.03, 0.3),
                    arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=1.5))
ax.text(0.5, 0.85, '1929: Linear Chain (3 links)', ha='center', fontsize=10,
        fontweight='bold', color='#2C3E50')
ax.text(0.5, 0.15, '2008: Networked Chain (6+ links)', ha='center', fontsize=10,
        fontweight='bold', color='#E74C3C')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Contagion Chain Length', fontsize=12, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('01_leverage_evolution.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 01_leverage_evolution.png")


# ============================================================
# MODEL 2: Bank Run Agent-Based Simulation
# ============================================================
print("\n" + "=" * 65)
print("MODEL 2: Bank Run Agent-Based Simulation")
print("=" * 65)

random.seed(42)

class BankRunSimulation:
    def __init__(self, n_depositors=200, reserve_ratio=0.1,
                 panic_threshold=0.3, neighbor_influence=0.6):
        self.n = n_depositors
        self.reserve = reserve_ratio * n_depositors
        self.total_deposits = n_depositors
        self.panic_threshold = panic_threshold
        self.neighbor_influence = neighbor_influence
        self.states = [0] * n_depositors
        self.neighbors = [random.sample(range(n_depositors), 5)
                          for _ in range(n_depositors)]

    def step(self):
        new_states = self.states[:]
        for i in range(self.n):
            if self.states[i] == 1:
                continue
            neighbor_panic = sum(self.states[j] for j in self.neighbors[i])
            panic_ratio = neighbor_panic / len(self.neighbors[i])
            if panic_ratio >= self.panic_threshold:
                if random.random() < self.neighbor_influence:
                    new_states[i] = 1
                    self.reserve -= 1
            elif random.random() < 0.02:
                new_states[i] = 1
                self.reserve -= 1
        self.states = new_states
        return sum(self.states), self.reserve > 0

sim = BankRunSimulation()
results = []
for t in range(50):
    withdrawn, alive = sim.step()
    results.append({'step': t, 'withdrawn': withdrawn,
                    'pct': withdrawn/200*100, 'alive': alive})
    if not alive:
        break

withdraw_series = [r['withdrawn'] for r in results]
pct_series = [r['pct'] for r in results]
steps = [r['step'] for r in results]

for r in results:
    if r['step'] % 5 == 0 or not r['alive']:
        status = "Operating" if r['alive'] else "FAILED"
        print(f"  Step {r['step']:2d}: {r['withdrawn']:3d} withdrew "
              f"({r['pct']:5.1f}%) | Bank: {status}")

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Bank Run Agent-Based Model: Panic Contagion\n'
             'Each depositor watches 5 neighbors -- local panic triggers global collapse',
             fontsize=14, fontweight='bold')

ax = axes[0]
ax.plot(steps, pct_series, 'o-', color='#E74C3C', linewidth=2.5, markersize=4)
ax.fill_between(steps, pct_series, alpha=0.2, color='#E74C3C')
ax.axhline(y=10, color='green', linestyle='--', label='Reserve ratio (10%)')
ax.set_xlabel('Time Step', fontsize=11)
ax.set_ylabel('% Withdrawn', fontsize=11)
ax.set_title('Withdrawal Cascade', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

# Panel 2: New withdrawals per step
ax = axes[1]
new_per_step = [withdraw_series[0]] + [withdraw_series[i] - withdraw_series[i-1]
                                        for i in range(1, len(withdraw_series))]
ax.bar(steps, new_per_step, color='#E74C3C', alpha=0.8, edgecolor='black', linewidth=0.5)
ax.set_xlabel('Time Step', fontsize=11)
ax.set_ylabel('New Withdrawals This Step', fontsize=11)
ax.set_title('Contagion Acceleration', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Panel 3: Critical threshold analysis (multiple sims)
ax = axes[2]
random.seed(0)
thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]
collapse_steps = []
for thresh in thresholds:
    sim2 = BankRunSimulation(panic_threshold=thresh)
    for t2 in range(100):
        w2, alive2 = sim2.step()
        if not alive2:
            collapse_steps.append(t2)
            break
    else:
        collapse_steps.append(100)

colors_t = ['#E74C3C' if s < 30 else '#F39C12' if s < 60 else '#27AE60' for s in collapse_steps]
bars = ax.bar([f'{t:.0%}' for t in thresholds], collapse_steps, color=colors_t,
              edgecolor='black', linewidth=1)
ax.set_xlabel('Panic Threshold (neighbor ratio)', fontsize=11)
ax.set_ylabel('Steps Until Bank Failure', fontsize=11)
ax.set_title('Threshold Sensitivity', fontsize=12, fontweight='bold')
for bar, v in zip(bars, collapse_steps):
    label = f'{v}' if v < 100 else 'Survived'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            label, ha='center', fontweight='bold', fontsize=10)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('02_bank_run_agents.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 02_bank_run_agents.png")


# ============================================================
# MODEL 3: Credit Spiral -- Death Spiral Feedback Loop
# ============================================================
print("\n" + "=" * 65)
print("MODEL 3: Credit Spiral -- Negative Feedback Loop")
print("=" * 65)

def credit_spiral(initial_gdp=100, shock=-10, policy_response=0, rounds=10):
    gdp = initial_gdp + shock
    credit = 100
    asset_price = 100 + shock
    history = []
    for r in range(rounds):
        credit_change = (asset_price - 100) * 0.3 + policy_response * 0.5
        credit = max(10, credit + credit_change)
        gdp_change = credit_change * 0.2 + policy_response * 0.3
        gdp = max(50, gdp + gdp_change)
        asset_price = max(20, asset_price + gdp_change * 0.5 - 2)
        history.append({'round': r, 'gdp': gdp, 'credit': credit, 'asset': asset_price})
    return history

no_response = credit_spiral(policy_response=0)
with_response = credit_spiral(policy_response=5)

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Credit Crunch Death Spiral: 1929 (No Response) vs 2008 (Aggressive Response)\n'
             'Same negative feedback loop, different policy intervention',
             fontsize=14, fontweight='bold')

for idx, (metric, label) in enumerate([('gdp', 'GDP Index'), ('credit', 'Credit Index'),
                                        ('asset', 'Asset Price Index')]):
    ax = axes[idx]
    ax.plot([h['round'] for h in no_response], [h[metric] for h in no_response],
            'o-', color='#2C3E50', linewidth=2.5, markersize=5, label='1929: No response')
    ax.plot([h['round'] for h in with_response], [h[metric] for h in with_response],
            's-', color='#27AE60', linewidth=2.5, markersize=5, label='2008: Policy response')
    ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Pre-crisis level')
    ax.set_xlabel('Quarters After Crisis', fontsize=11)
    ax.set_ylabel(label, fontsize=11)
    ax.set_title(label, fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('03_credit_spiral.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 03_credit_spiral.png")


# ============================================================
# MODEL 4: Unemployment Cascade
# ============================================================
print("\n" + "=" * 65)
print("MODEL 4: Unemployment Cascade -- 25 Years vs 5 Years")
print("=" * 65)

years_after = [0, 0.5, 1, 2, 3, 4, 5, 10]
unemp_1929 = [3.2, 5.0, 8.7, 15.9, 23.6, 24.9, 21.7, 14.6]
unemp_2008 = [5.0, 7.2, 9.3, 9.6, 8.9, 8.1, 7.2, 4.4]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Unemployment Cascade: 1929 (25% peak) vs 2008 (10% peak)\n'
             'Safety nets + policy response = 25 years of suffering compressed to 5',
             fontsize=14, fontweight='bold')

# Panel 1: Unemployment trajectories
ax = axes[0]
ax.plot(years_after, unemp_1929, 'o-', color='#2C3E50', linewidth=2.5, markersize=8,
        label='1929 Great Depression')
ax.fill_between(years_after, unemp_1929, alpha=0.15, color='#2C3E50')
ax.plot(years_after, unemp_2008, 's-', color='#E74C3C', linewidth=2.5, markersize=8,
        label='2008 Financial Crisis')
ax.fill_between(years_after, unemp_2008, alpha=0.15, color='#E74C3C')
ax.set_xlabel('Years After Crisis', fontsize=11)
ax.set_ylabel('Unemployment Rate (%)', fontsize=11)
ax.set_title('Unemployment Trajectories', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

# Panel 2: Gap between crises
ax = axes[1]
gap = [u1 - u2 for u1, u2 in zip(unemp_1929, unemp_2008)]
colors_gap = ['#E74C3C' if g > 0 else '#27AE60' for g in gap]
ax.bar(range(len(gap)), gap, color=colors_gap, edgecolor='black', linewidth=1)
ax.set_xticks(range(len(years_after)))
ax.set_xticklabels([f'+{y:.0f}yr' if y == int(y) else f'+{y}yr' for y in years_after],
                   fontsize=9)
ax.set_ylabel('Unemployment Gap (pp)', fontsize=11)
ax.set_title('1929 Excess Unemployment vs 2008', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
ax.axhline(y=0, color='black', linewidth=1)

# Panel 3: Policy differences
ax = axes[2]
policies = ['Deposit\nInsurance', 'Central Bank\nResponse', 'Fiscal\nStimulus',
            'Safety\nNets', 'Global\nCoordination']
score_1929 = [0, 10, 5, 5, 0]
score_2008 = [90, 85, 75, 70, 60]
x = np.arange(len(policies))
ax.barh(x - 0.18, score_1929, 0.35, color='#2C3E50', alpha=0.8, label='1929',
        edgecolor='black', linewidth=1)
ax.barh(x + 0.18, score_2008, 0.35, color='#27AE60', alpha=0.8, label='2008',
        edgecolor='black', linewidth=1)
ax.set_yticks(x)
ax.set_yticklabels(policies, fontsize=9)
ax.set_xlabel('Policy Effectiveness (0-100)', fontsize=11)
ax.set_title('Policy Response Comparison', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('04_unemployment_cascade.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 04_unemployment_cascade.png")


# ============================================================
# MODEL 5: Wealth Gini Changes
# ============================================================
print("\n" + "=" * 65)
print("MODEL 5: Wealth Gini -- Crisis Impact on Inequality")
print("=" * 65)

years_gini = [1928, 1932, 1945, 1979, 2007, 2010, 2024]
gini_vals = [0.82, 0.78, 0.68, 0.65, 0.83, 0.85, 0.87]
top1_share = [23.9, 18.4, 11.5, 8.0, 23.5, 24.1, 26.3]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Wealth Inequality Through Crises: Gini Coefficient & Top 1% Share\n'
             '1929 crisis led to New Deal compression | 2008 rescue made inequality worse',
             fontsize=14, fontweight='bold')

ax = axes[0]
ax.plot(years_gini, gini_vals, 'o-', color='#E74C3C', linewidth=2.5, markersize=8)
ax.fill_between(years_gini, gini_vals, alpha=0.15, color='#E74C3C')
ax.axvspan(1929, 1945, alpha=0.1, color='blue', label='New Deal era')
ax.axvspan(2008, 2024, alpha=0.1, color='red', label='Post-2008 QE era')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Gini Coefficient', fontsize=11)
ax.set_title('Gini Coefficient Over Time', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(years_gini, top1_share, 's-', color='#8E44AD', linewidth=2.5, markersize=8)
ax.fill_between(years_gini, top1_share, alpha=0.15, color='#8E44AD')
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Top 1% Wealth Share (%)', fontsize=11)
ax.set_title('Top 1% Wealth Concentration', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)
for y, g in zip(years_gini, top1_share):
    ax.annotate(f'{g}%', (y, g), textcoords="offset points", xytext=(0, 10),
                ha='center', fontsize=9, fontweight='bold')

# Panel 3: Paradox
ax = axes[2]
labels_p = ['1929 Crisis\n(No Rescue)', '2008 Crisis\n(Massive Rescue)']
gini_change = [0.82 - 0.65, 0.85 - 0.83]
inequality_direction = ['Decreased\n(New Deal)', 'Increased\n(QE benefited\nasset holders)']
colors_ineq = ['#27AE60', '#E74C3C']
bars = ax.bar(labels_p, [abs(gc)*100 for gc in gini_change], color=colors_ineq,
              edgecolor='black', linewidth=1.5)
ax.set_ylabel('Gini Change (x100)', fontsize=11)
ax.set_title('Crisis Paradox:\nRescue Can Worsen Inequality', fontsize=12, fontweight='bold')
for bar, direction in zip(bars, inequality_direction):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            direction, ha='center', fontsize=9, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('05_wealth_gini.png', dpi=300, bbox_inches='tight')
plt.close()
print("=> Saved: 05_wealth_gini.png")


# ============================================================
# MODEL 6: Recovery Time Comparison
# ============================================================
print("\n" + "=" * 65)
print("MODEL 6: Recovery Time -- 25 Years vs 5 Years")
print("=" * 65)

metrics = ['Stock Market\nto Pre-high', 'GDP to\nPre-high', 'Unemployment\nBelow 5%',
           'Banking System\nStable']
recovery_1929 = [25, 7, 13, 4]
recovery_2008 = [5, 3, 8, 2]
ratio_r = [r1/r2 for r1, r2 in zip(recovery_1929, recovery_2008)]

fig, axes = plt.subplots(1, 3, figsize=(22, 6))
fig.suptitle('Recovery Time: 1929 Great Depression vs 2008 Financial Crisis\n'
             'Institutional learning + policy response = dramatically faster recovery',
             fontsize=14, fontweight='bold')

ax = axes[0]
x = np.arange(len(metrics))
w = 0.35
ax.barh(x - w/2, recovery_1929, w, color='#2C3E50', alpha=0.8, label='1929',
        edgecolor='black', linewidth=1)
ax.barh(x + w/2, recovery_2008, w, color='#27AE60', alpha=0.8, label='2008',
        edgecolor='black', linewidth=1)
ax.set_yticks(x)
ax.set_yticklabels(metrics, fontsize=9)
ax.set_xlabel('Years to Recover', fontsize=11)
ax.set_title('Recovery Duration (Years)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3)

ax = axes[1]
bars = ax.bar(range(len(metrics)), ratio_r, color='#E67E22', edgecolor='black', linewidth=1)
ax.set_xticks(range(len(metrics)))
ax.set_xticklabels(metrics, fontsize=8)
ax.set_ylabel('Recovery Speed Ratio (1929/2008)', fontsize=11)
ax.set_title('How Much Slower Was 1929?', fontsize=12, fontweight='bold')
for bar, v in zip(bars, ratio_r):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{v:.1f}x', ha='center', fontweight='bold', fontsize=11)
ax.grid(axis='y', alpha=0.3)

# Panel 3: Key institutional differences
ax = axes[2]
institutions = ['FDIC\n(Deposit Insurance)', 'Fed as\nLender of Last Resort',
                'Automatic\nStabilizers', 'Global\nCoordination']
existed_1929 = [0, 0, 0, 0]
existed_2008 = [1, 1, 1, 1]
x3 = np.arange(len(institutions))
ax.barh(x3, existed_2008, 0.5, color='#27AE60', alpha=0.8, label='2008: Existed',
        edgecolor='black', linewidth=1)
ax.barh(x3, existed_1929, 0.5, color='#E74C3C', alpha=0.3, label='1929: Did NOT exist')
ax.set_yticks(x3)
ax.set_yticklabels(institutions, fontsize=9)
ax.set_xlabel('Available (0=No, 1=Yes)', fontsize=11)
ax.set_title('Key Institutional Safeguards', fontsize=12, fontweight='bold')
for i, (v29, v08) in enumerate(zip(existed_1929, existed_2008)):
    ax.text(0.5, i, 'YES' if v08 else 'NO', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
ax.legend(fontsize=9)
ax.set_xlim(0, 1.2)

plt.tight_layout(rect=[0, 0, 1, 0.92], w_pad=3)
plt.savefig('06_recovery_time.png', dpi=300, bbox_inches='tight')
plt.close()

for m, r1, r2, r in zip(metrics, recovery_1929, recovery_2008, ratio_r):
    print(f"  {m.replace(chr(10), ' '):<25}: 1929={r1:>2}yr, 2008={r2:>2}yr ({r:.1f}x slower)")
print("\n=> Saved: 06_recovery_time.png")


# ============================================================
print("\n" + "=" * 65)
print("ALL 6 MODELS COMPLETE")
print("Output files: 01-06_*.png")
print("=" * 65)
