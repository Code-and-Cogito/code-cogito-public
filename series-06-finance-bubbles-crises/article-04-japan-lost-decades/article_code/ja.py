# Code & Cogito: 日本の失われた30年 vs 台湾の住宅危機
# Article: https://code-cogito.com/ja/finance-04-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

# ====== 住宅価格対年収比：東京 vs 台北 ======
# 例示用の数値：東京圏の新築マンションと台湾内政部（台北市）の住宅価格対年収比の公表水準に合わせて手作業で設定。公的な年次統計ではない

japan_years  = [1980, 1983, 1985, 1987, 1989, 1991, 1993,
                1995, 1998, 2000, 2003, 2005, 2008, 2010,
                2013, 2015, 2018, 2020]
japan_ratios = [8.2,  9.1, 10.5, 14.8, 18.4, 16.2, 12.1,
                10.3,  8.5,  7.8,  7.2,  7.5,  8.1,  7.9,
                 8.3,  9.0, 10.2, 10.8]

tw_years  = [2002, 2004, 2006, 2008, 2010, 2012, 2014,
             2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
tw_ratios = [6.1,  6.8,  8.2,  8.9, 10.1, 12.6, 14.1,
             14.8, 13.5, 14.1, 15.2, 16.2, 16.1, 15.8, 16.0]

jp_peak = max(japan_ratios)
jp_peak_yr = japan_years[japan_ratios.index(jp_peak)]
jp_trough = min(japan_ratios[japan_ratios.index(jp_peak):])
jp_decline = (jp_peak - jp_trough) / jp_peak * 100

tw_peak = max(tw_ratios)
tw_peak_yr = tw_years[tw_ratios.index(tw_peak)]

print("=" * 55)
print("   住宅価格対年収比：東京 vs 台北")
print("=" * 55)

stages = [
    ("上昇前",     8.2, 1980, 6.1, 2002),
    ("緩やかな上昇", 10.5, 1985, 8.2, 2006),
    ("加速膨張",   14.8, 1987, 12.6, 2012),
    ("頂点/高原",  18.4, 1989, 16.2, 2021),
    ("ピーク後",   16.2, 1991, 16.0, 2024),
]

print(f"\n{'段階':<12} {'東京':>8}  {'年':>5}  "
      f"{'台北':>8}  {'年':>5}")
print("-" * 55)
for stage, jp, jp_y, tw, tw_y in stages:
    print(f"{stage:<12} {jp:>8.1f}x  {jp_y:>5}  "
          f"{tw:>8.1f}x  {tw_y:>5}")

print(f"\n[日本] ピーク: {jp_peak:.1f}x ({jp_peak_yr}) → "
      f"底値: {jp_trough:.1f}x | 下落幅: {jp_decline:.0f}%")
print(f"[台湾] ピーク: {tw_peak:.1f}x ({tw_peak_yr}) → "
      f"現在: {tw_ratios[-1]:.1f}x | 横ばい")
print(f"\n目安（公的基準ではない）: 3-6x | 警戒線: 10x | 危険域: 15x+")
