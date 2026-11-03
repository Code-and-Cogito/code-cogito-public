# Code & Cogito: 印刷術革命 vs 社交媒體爆炸
# Article: https://code-cogito.com/thought-revolution-02/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt

def sir_model(population, beta, gamma, days, initial_infected=10):
    """SIR模型：模擬資訊（或假新聞）在網絡中的傳播"""
    S, I, R = [population - initial_infected], [initial_infected], [0]
    for _ in range(days):
        s, i, r = S[-1], I[-1], R[-1]
        new_infected = beta * s * i / population
        new_recovered = gamma * i
        S.append(s - new_infected)
        I.append(i + new_infected - new_recovered)
        R.append(r + new_recovered)
    return np.array(S), np.array(I), np.array(R)

# 場景一：路德《九十五條論綱》透過印刷術傳播（1517年）
# beta=0.3: 中等傳播率（印刷速度限制）, gamma=0.01: 極低恢復率（缺乏事實查核）
S1, I1, R1 = sir_model(100000, beta=0.3, gamma=0.01, days=90)

# 場景二：現代真實新聞透過社交媒體傳播
# beta=0.5: 較高傳播率, gamma=0.1: 中等恢復率（有事實查核）
S2, I2, R2 = sir_model(1000000, beta=0.5, gamma=0.1, days=30)

# 場景三：現代假新聞透過社交媒體傳播
# beta=0.9: 極高傳播率（手動設定的示意值，並非由MIT研究的6倍推得）, gamma=0.02: 極低恢復率（同為假設）
S3, I3, R3 = sir_model(1000000, beta=0.9, gamma=0.02, days=30)

# 計算關鍵指標
peak_luther = np.max(I1)
peak_real = np.max(I2)
peak_fake = np.max(I3)
day_peak_luther = np.argmax(I1)
day_peak_real = np.argmax(I2)
day_peak_fake = np.argmax(I3)
total_reached_luther = R1[-1] + I1[-1]
total_reached_real = R2[-1] + I2[-1]
total_reached_fake = R3[-1] + I3[-1]

print("=== 資訊傳播SIR模型：三個場景對比 ===\n")
print(f"{'指標':<20} {'路德論綱(1517)':<20} {'現代真新聞':<20} {'現代假新聞':<20}")
print("-" * 80)
print(f"{'人口規模':<20} {'100,000':<20} {'1,000,000':<20} {'1,000,000':<20}")
print(f"{'傳播率(β)':<20} {'0.30':<20} {'0.50':<20} {'0.90':<20}")
print(f"{'恢復率(γ)':<20} {'0.01':<20} {'0.10':<20} {'0.02':<20}")
print(f"{'感染峰值':<20} {peak_luther:<20.0f} {peak_real:<20.0f} {peak_fake:<20.0f}")
print(f"{'達峰天數':<20} {day_peak_luther:<20} {day_peak_real:<20} {day_peak_fake:<20}")
print(f"{'總觸及人數':<20} {total_reached_luther:<20.0f} {total_reached_real:<20.0f} {total_reached_fake:<20.0f}")
print(f"{'觸及率':<20} {total_reached_luther/100000*100:<19.1f}% {total_reached_real/1000000*100:<19.1f}% {total_reached_fake/1000000*100:<19.1f}%")

# | === 資訊傳播SIR模型：三個場景對比 ===
# | 
# | 指標                 路德論綱(1517)       現代真新聞            現代假新聞
# | --------------------------------------------------------------------------------
# | 人口規模             100,000              1,000,000            1,000,000
# | 傳播率(β)            0.30                 0.50                 0.90
# | 恢復率(γ)            0.01                 0.10                 0.02
# | 感染峰值             86,506               188,322              925,671
# | 達峰天數             47                   30                   21
# | 總觸及人數            100,000              242,729              1,000,000
# | 觸及率               100.0%               24.3%                100.0%
