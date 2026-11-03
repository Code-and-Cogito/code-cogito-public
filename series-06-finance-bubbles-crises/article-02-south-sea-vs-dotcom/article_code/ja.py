# Code & Cogito: 南海バブル vs ドットコムバブル
# Article: https://code-cogito.com/ja/finance-02-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

# === 南海会社 PERの推移（説明用に手で設定した値。歴史的記録ではない。1719-1721、四半期） ===
ss_quarters = ['1719Q1','1719Q2','1719Q3','1719Q4',
               '1720Q1','1720Q2','1720Q3','1720Q4',
               '1721Q1','1721Q2']
ss_pe = np.array([12, 14, 15, 18, 35, 85, 160, 105, 15, 11])
ss_hist_avg = 14  # 想定した「歴史的平均」PER（説明用の値）

# === NASDAQテック株 PERの推移（説明用に手で設定した値。市場データではない。1998-2002、四半期） ===
nq_quarters = ['1998Q1','1998Q2','1998Q3','1998Q4',
               '1999Q1','1999Q2','1999Q3','1999Q4',
               '2000Q1','2000Q2','2000Q3','2000Q4',
               '2001Q1','2001Q2','2001Q3','2001Q4',
               '2002Q1','2002Q2']
nq_pe = np.array([22, 25, 24, 30, 38, 50, 65, 95,
                  120, 150, 85, 55, 40, 35, 28, 22, 18, 16])
nq_hist_avg = 20  # 想定した「歴史的平均」PER（説明用の値）

# 「今回は違う」指数の算出：歴史的平均からの乖離倍率
ss_deviation = ss_pe / ss_hist_avg
nq_deviation = nq_pe / nq_hist_avg

# 「危険ゾーン」の特定（乖離率 > 3倍）
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

# 平均回帰の速度
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

# | 南海会社の株価崩壊
# |   → 南海株を担保にした融資が不履行
# |     → ゴールドスミス銀行（初期の銀行）が流動性危機に陥る
# |       → 銀行が融資を停止
# |         → 他の企業が資金調達できなくなる
# |           → 多くのバブル計画が破綻（崩壊前にすでにしぼんでいたものも多い）
# |             → 一部の銀行や金細工商が破綻（1720年9〜12月）
# |               → 実体経済への打撃の大きさについては歴史家の間でも議論がある

# | NASDAQが崩壊
# |   → テック企業の時価総額が蒸発
# |     → VCファンドが損失を被り、新規投資を停止
# |       → スタートアップが次のラウンドの資金を調達できなくなる
# |         → 大量解雇（サンタクララ郡の失業率は、2000年12月の約2.4%から2002年12月の約8.5%へ上昇）
# |           → テック業界の雇用と所得が縮小
# |             → 広告収入が減少（テック企業の主要収入源）
# |               → さらに多くの企業が倒産
# |                 → 9.11テロが恐慌を増幅
# |                   → 景気後退
