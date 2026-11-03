# Code & Cogito: 鬱金香狂熱 vs 比特幣泡沫
# Article: https://code-cogito.com/finance-01/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt

# === 示意用鬱金香價格走勢（手動設定的形狀，非歷史逐月資料） ===
tulip_months = np.arange(0, 36)  # 36個時間步
tulip_prices_raw = np.array([
    40, 42, 45, 50, 55, 60, 68, 75, 85, 100,
    120, 150, 180, 220, 280, 350, 450, 580, 750,
    900, 1100, 1400, 1800, 2200, 2800, 3000,
    2500, 1200, 400, 150, 80, 50, 40, 35, 32, 30
])

# === 比特幣近似走勢（美元，手動輸入；月收盤與月內高低點混用，約2019年12月至2023年年中） ===
btc_months = np.arange(0, 36)
btc_prices_raw = np.array([
    7200, 8800, 9200, 9500, 11300, 13800, 19000,
    33000, 45000, 58000, 57000, 64000, 35000, 40000,
    47000, 43000, 48000, 57000, 61000, 67000, 69000,
    46000, 38000, 29000, 20000, 19000, 16500, 17000,
    21000, 23000, 27000, 28000, 26000, 27500, 29000, 30000
])

# min-max 正規化到 0-100 區間
def normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min()) * 100

tulip_norm = normalize(tulip_prices_raw.astype(float))
btc_norm = normalize(btc_prices_raw.astype(float))

# === DTW 動態時間規整 ===
n, m = len(tulip_norm), len(btc_norm)
dtw_matrix = np.full((n + 1, m + 1), np.inf)
dtw_matrix[0, 0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = abs(tulip_norm[i-1] - btc_norm[j-1])
        dtw_matrix[i, j] = cost + min(
            dtw_matrix[i-1, j],
            dtw_matrix[i, j-1],
            dtw_matrix[i-1, j-1]
        )

dtw_distance = dtw_matrix[n, m]
max_possible = 100 * max(n, m)
similarity = (1 - dtw_distance / max_possible) * 100

print(f"DTW Distance: {dtw_distance:.1f}")
print(f"Similarity:   {similarity:.1f}%")
print(f"\nTulip peak:   step {np.argmax(tulip_norm)} "
      f"(normalized: {tulip_norm.max():.0f})")
print(f"BTC peak:     step {np.argmax(btc_norm)} "
      f"(normalized: {btc_norm.max():.0f})")
# 跌幅 = 從高點跌到高點之後的最低值
print(f"Tulip crash:  -{(1 - tulip_prices_raw[np.argmax(tulip_prices_raw):].min()/tulip_prices_raw.max())*100:.0f}%")
print(f"BTC crash:    -{(1 - btc_prices_raw[np.argmax(btc_prices_raw):].min()/btc_prices_raw.max())*100:.0f}%")

# | DTW Distance: 454.4
# | Similarity:   87.4%
# | 
# | Tulip peak:   step 25 (normalized: 100)
# | BTC peak:     step 20 (normalized: 100)
# | Tulip crash:  -99%
# | BTC crash:    -76%
