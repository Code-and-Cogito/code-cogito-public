# Code & Cogito: 南海泡沫 vs 網路泡沫
# Article: https://code-cogito.com/finance-02/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

# === 南海公司 P/E 示意路徑（手動設定的示意值，非歷史紀錄；1719-1721，季度） ===
ss_quarters = ['1719Q1','1719Q2','1719Q3','1719Q4',
               '1720Q1','1720Q2','1720Q3','1720Q4',
               '1721Q1','1721Q2']
ss_pe = np.array([12, 14, 15, 18, 35, 85, 160, 105, 15, 11])
ss_hist_avg = 14  # 假設的「歷史平均」P/E（示意值）

# === NASDAQ 科技股 P/E 示意路徑（手動設定的示意值，非市場資料；1998-2002，季度） ===
nq_quarters = ['1998Q1','1998Q2','1998Q3','1998Q4',
               '1999Q1','1999Q2','1999Q3','1999Q4',
               '2000Q1','2000Q2','2000Q3','2000Q4',
               '2001Q1','2001Q2','2001Q3','2001Q4',
               '2002Q1','2002Q2']
nq_pe = np.array([22, 25, 24, 30, 38, 50, 65, 95,
                  120, 150, 85, 55, 40, 35, 28, 22, 18, 16])
nq_hist_avg = 20  # 假設的「歷史平均」P/E（示意值）

# 計算「這次不一樣」指數：相對於歷史均值的偏離倍數
ss_deviation = ss_pe / ss_hist_avg
nq_deviation = nq_pe / nq_hist_avg

# 辨識「危險區域」（偏離 > 3倍歷史均值）
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

# 回歸均值的速度
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

# | 南海公司股價崩盤
# |   → 以南海股票為抵押的貸款違約
# |     → 金匠銀行（早期銀行）出現流動性危機
# |       → 銀行停止放貸
# |         → 其他公司無法獲得融資
# |           → 許多泡沫計畫倒閉（不少在崩盤前就已萎縮）
# |             → 一批銀行與金匠倒閉（1720年9月至12月）
# |               → 對實體經濟的衝擊有多大，史家仍有爭論

# | NASDAQ崩盤
# |   → 科技公司市值蒸發
# |     → 風投基金虧損，停止新投資
# |       → 創業公司無法獲得下一輪融資
# |         → 大規模裁員（聖塔克拉拉郡失業率從2000年12月的約2.4%升到2002年12月的約8.5%）
# |           → 科技業就業與所得萎縮
# |             → 廣告收入下降（科技公司主要收入來源）
# |               → 更多公司破產
# |                 → 911事件加劇恐慌
# |                   → 經濟衰退
