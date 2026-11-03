# Code & Cogito: 活版印刷革命 vs ソーシャルメディア爆発
# Article: https://code-cogito.com/ja/thought-revolution-02-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt

def sir_model(population, beta, gamma, days, initial_infected=10):
    """SIR model: simulate information (or misinformation) spread in a network"""
    S, I, R = [population - initial_infected], [initial_infected], [0]
    for _ in range(days):
        s, i, r = S[-1], I[-1], R[-1]
        new_infected = beta * s * i / population
        new_recovered = gamma * i
        S.append(s - new_infected)
        I.append(i + new_infected - new_recovered)
        R.append(r + new_recovered)
    return np.array(S), np.array(I), np.array(R)

# Scenario 1: Luther's 95 Theses spreading via print (1517)
# beta=0.3: moderate transmission (print speed limits), gamma=0.01: very low recovery (no fact-checking)
S1, I1, R1 = sir_model(100000, beta=0.3, gamma=0.01, days=90)

# Scenario 2: Modern real news spreading via social media
# beta=0.5: higher transmission, gamma=0.1: moderate recovery (fact-checking exists)
S2, I2, R2 = sir_model(1000000, beta=0.5, gamma=0.1, days=30)

# Scenario 3: Modern fake news spreading via social media
# beta=0.9: very high transmission (illustrative value, not derived from the MIT study's 6x), gamma=0.02: very low recovery (assumed)
S3, I3, R3 = sir_model(1000000, beta=0.9, gamma=0.02, days=30)

# Calculate key metrics
peak_luther = np.max(I1)
peak_real = np.max(I2)
peak_fake = np.max(I3)
day_peak_luther = np.argmax(I1)
day_peak_real = np.argmax(I2)
day_peak_fake = np.argmax(I3)
total_reached_luther = R1[-1] + I1[-1]
total_reached_real = R2[-1] + I2[-1]
total_reached_fake = R3[-1] + I3[-1]

print("=== Information Spread SIR Model: Three Scenarios Compared ===\n")
print(f"{'Metric':<20} {'Luther Theses(1517)':<20} {'Modern Real News':<20} {'Modern Fake News':<20}")
print("-" * 80)
print(f"{'Population':<20} {'100,000':<20} {'1,000,000':<20} {'1,000,000':<20}")
print(f"{'Spread rate(β)':<20} {'0.30':<20} {'0.50':<20} {'0.90':<20}")
print(f"{'Recovery rate(γ)':<20} {'0.01':<20} {'0.10':<20} {'0.02':<20}")
print(f"{'Peak infected':<20} {peak_luther:<20.0f} {peak_real:<20.0f} {peak_fake:<20.0f}")
print(f"{'Days to peak':<20} {day_peak_luther:<20} {day_peak_real:<20} {day_peak_fake:<20}")
print(f"{'Total reached':<20} {total_reached_luther:<20.0f} {total_reached_real:<20.0f} {total_reached_fake:<20.0f}")
print(f"{'Reach rate':<20} {total_reached_luther/100000*100:<19.1f}% {total_reached_real/1000000*100:<19.1f}% {total_reached_fake/1000000*100:<19.1f}%")

# | === Information Spread SIR Model: Three Scenarios Compared ===
# | 
# | Metric               Luther Theses(1517) Modern Real News     Modern Fake News
# | --------------------------------------------------------------------------------
# | Population           100,000              1,000,000            1,000,000
# | Spread rate(β)       0.30                 0.50                 0.90
# | Recovery rate(γ)     0.01                 0.10                 0.02
# | Peak infected        86,506               188,322              925,671
# | Days to peak         47                   30                   21
# | Total reached        100,000              242,729              1,000,000
# | Reach rate           100.0%               24.3%                100.0%
