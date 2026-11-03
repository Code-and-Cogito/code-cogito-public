# Code & Cogito: The South Sea Bubble vs the Dot-Com Bubble
# Article: https://code-cogito.com/en/finance-02-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

# === South Sea Company illustrative P/E path (hand-set values, not historical records; 1719-1721, quarterly) ===
ss_quarters = ['1719Q1','1719Q2','1719Q3','1719Q4',
               '1720Q1','1720Q2','1720Q3','1720Q4',
               '1721Q1','1721Q2']
ss_pe = np.array([12, 14, 15, 18, 35, 85, 160, 105, 15, 11])
ss_hist_avg = 14  # Assumed "historical average" P/E (illustrative)

# === NASDAQ tech stock illustrative P/E path (hand-set values, not market data; 1998-2002, quarterly) ===
nq_quarters = ['1998Q1','1998Q2','1998Q3','1998Q4',
               '1999Q1','1999Q2','1999Q3','1999Q4',
               '2000Q1','2000Q2','2000Q3','2000Q4',
               '2001Q1','2001Q2','2001Q3','2001Q4',
               '2002Q1','2002Q2']
nq_pe = np.array([22, 25, 24, 30, 38, 50, 65, 95,
                  120, 150, 85, 55, 40, 35, 28, 22, 18, 16])
nq_hist_avg = 20  # Assumed "historical average" P/E (illustrative)

# Calculate "This Time Is Different" Index: deviation multiple from historical mean
ss_deviation = ss_pe / ss_hist_avg
nq_deviation = nq_pe / nq_hist_avg

# Identify "danger zones" (deviation > 3x historical mean)
ss_danger = [(q, d) for q, d in zip(ss_quarters, ss_deviation) if d > 3]
nq_danger = [(q, d) for q, d in zip(nq_quarters, nq_deviation) if d > 3]

print("=" * 60)
print("'THIS TIME IS DIFFERENT' INDEX")
print("(P/E deviation from historical average)")
print("=" * 60)

print(f"\n--- South Sea Company (hist avg P/E: {ss_hist_avg}) ---")
for q, pe, dev in zip(ss_quarters, ss_pe, ss_deviation):
    flag = " *** DANGER" if dev > 3 else ""
    print(f"  {q}: P/E={pe:>5}, deviation={dev:.1f}x{flag}")

print(f"\n--- NASDAQ Tech (hist avg P/E: {nq_hist_avg}) ---")
for q, pe, dev in zip(nq_quarters, nq_pe, nq_deviation):
    flag = " *** DANGER" if dev > 3 else ""
    print(f"  {q}: P/E={pe:>5}, deviation={dev:.1f}x{flag}")

print(f"\n{'='*60}")
print(f"SOUTH SEA peak deviation: {ss_deviation.max():.1f}x "
      f"(at {ss_quarters[np.argmax(ss_deviation)]})")
print(f"NASDAQ peak deviation:    {nq_deviation.max():.1f}x "
      f"(at {nq_quarters[np.argmax(nq_deviation)]})")
print(f"\nCorrelation of deviation curves: "
      f"{np.corrcoef(ss_deviation[:10], nq_deviation[4:14])[0,1]:.2f}")

# Speed of mean reversion
ss_peak_idx = np.argmax(ss_deviation)
ss_quarters_to_normal = len([d for d in ss_deviation[ss_peak_idx:]
                             if d > 1.5])
nq_peak_idx = np.argmax(nq_deviation)
nq_quarters_to_normal = len([d for d in nq_deviation[nq_peak_idx:]
                             if d > 1.5])
print(f"\nQuarters to revert (dev < 1.5x):")
print(f"  South Sea: {ss_quarters_to_normal} quarters")
print(f"  NASDAQ:    {nq_quarters_to_normal} quarters")

# | ============================================================
# | 'THIS TIME IS DIFFERENT' INDEX
# | (P/E deviation from historical average)
# | ============================================================
# | 
# | --- South Sea Company (hist avg P/E: 14) ---
# |   1719Q1: P/E=   12, deviation=0.9x
# |   1719Q2: P/E=   14, deviation=1.0x
# |   1719Q3: P/E=   15, deviation=1.1x
# |   1719Q4: P/E=   18, deviation=1.3x
# |   1720Q1: P/E=   35, deviation=2.5x
# |   1720Q2: P/E=   85, deviation=6.1x *** DANGER
# |   1720Q3: P/E=  160, deviation=11.4x *** DANGER
# |   1720Q4: P/E=  105, deviation=7.5x *** DANGER
# |   1721Q1: P/E=   15, deviation=1.1x
# |   1721Q2: P/E=   11, deviation=0.8x
# | 
# | --- NASDAQ Tech (hist avg P/E: 20) ---
# |   1998Q1: P/E=   22, deviation=1.1x
# |   1998Q2: P/E=   25, deviation=1.2x
# |   1998Q3: P/E=   24, deviation=1.2x
# |   1998Q4: P/E=   30, deviation=1.5x
# |   1999Q1: P/E=   38, deviation=1.9x
# |   1999Q2: P/E=   50, deviation=2.5x
# |   1999Q3: P/E=   65, deviation=3.2x *** DANGER
# |   1999Q4: P/E=   95, deviation=4.8x *** DANGER
# |   2000Q1: P/E=  120, deviation=6.0x *** DANGER
# |   2000Q2: P/E=  150, deviation=7.5x *** DANGER
# |   2000Q3: P/E=   85, deviation=4.2x *** DANGER
# |   2000Q4: P/E=   55, deviation=2.8x
# |   2001Q1: P/E=   40, deviation=2.0x
# |   2001Q2: P/E=   35, deviation=1.8x
# |   2001Q3: P/E=   28, deviation=1.4x
# |   2001Q4: P/E=   22, deviation=1.1x
# |   2002Q1: P/E=   18, deviation=0.9x
# |   2002Q2: P/E=   16, deviation=0.8x
# | 
# | ============================================================
# | SOUTH SEA peak deviation: 11.4x (at 1720Q3)
# | NASDAQ peak deviation:    7.5x (at 2000Q2)
# | 
# | Correlation of deviation curves: 0.37
# | 
# | Quarters to revert (dev < 1.5x):
# |   South Sea: 2 quarters
# |   NASDAQ:    5 quarters

# | South Sea share price crashes
# |   → Loans collateralized by South Sea stock default
# |     → Goldsmith banks (proto-banks) face liquidity crisis
# |       → Banks stop lending
# |         → Other companies can't get financing
# |           → Many bubble schemes fail (quite a few had already withered before the crash)
# |             → A number of banks and goldsmiths fail (September–December 1720)
# |               → How much damage reached the real economy is still debated by historians

# | NASDAQ crashes
# |   → Tech company market caps evaporate
# |     → Venture capital funds take losses, halt new investments
# |       → Startups can't raise their next round
# |         → Mass layoffs (Santa Clara County unemployment rose from about 2.4% in December 2000 to about 8.5% in December 2002)
# |           → Tech-sector jobs and incomes shrink
# |             → Advertising revenue falls (tech companies' main income)
# |               → More companies go under
# |                 → 9/11 amplifies the panic
# |                   → Recession
