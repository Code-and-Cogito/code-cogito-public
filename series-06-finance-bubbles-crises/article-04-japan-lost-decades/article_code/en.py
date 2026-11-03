# Code & Cogito: Japan's Lost Decades vs Taiwan's Housing Crisis
# Article: https://code-cogito.com/en/finance-04-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

# ====== Price-to-Income Ratio: Tokyo vs Taipei ======
# Illustrative, hand-set values scaled to published Tokyo-area new-condo and Taiwan MOI (Taipei) price-to-income figures; not an official year-by-year series

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
print("   Price-to-Income Ratio: Tokyo vs Taipei")
print("=" * 55)

stages = [
    ("Pre-rise",     8.2, 1980, 6.1, 2002),
    ("Slow climb",  10.5, 1985, 8.2, 2006),
    ("Acceleration", 14.8, 1987, 12.6, 2012),
    ("Peak/Plateau", 18.4, 1989, 16.2, 2021),
    ("Post-peak",    16.2, 1991, 16.0, 2024),
]

print(f"\n{'Stage':<15} {'Tokyo':>8}  {'Year':>5}  "
      f"{'Taipei':>8}  {'Year':>5}")
print("-" * 55)
for stage, jp, jp_y, tw, tw_y in stages:
    print(f"{stage:<15} {jp:>8.1f}x  {jp_y:>5}  "
          f"{tw:>8.1f}x  {tw_y:>5}")

print(f"\n[Japan] Peak: {jp_peak:.1f}x ({jp_peak_yr}) -> "
      f"Trough: {jp_trough:.1f}x | Decline: {jp_decline:.0f}%")
print(f"[Taiwan] Peak: {tw_peak:.1f}x ({tw_peak_yr}) -> "
      f"Current: {tw_ratios[-1]:.1f}x | Holding steady")
print(f"\nRule of thumb (not an official standard): 3-6x | Warning: 10x | Danger: 15x+")
