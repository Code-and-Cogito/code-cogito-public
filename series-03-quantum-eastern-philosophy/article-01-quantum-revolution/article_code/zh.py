# Code & Cogito: 量子革命前夜——當牛頓的宇宙開始崩解
# Article: https://code-cogito.com/quantum-revolution-newton-universe-collapse/
# All the code blocks of the article, in order. Program output is kept as comments.

# | nabla·E = rho/epsilon_0        （高斯定律）
# | nabla·B = 0                    （磁場無源）
# | nabla x E = -dB/dt             （法拉第定律）
# | nabla x B = mu_0 J + mu_0 epsilon_0 dE/dt  （安培-馬克士威定律）

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def planck_law(wavelength, T):
    """普朗克公式（量子理論）"""
    return (8 * np.pi * h * c / wavelength**5) / (np.exp(h * c / (wavelength * k * T)) - 1)

def rayleigh_jeans_law(wavelength, T):
    """瑞利-金斯公式（經典理論）"""
    return 8 * np.pi * k * T / wavelength**4

def visualize_blackbody_radiation():
    """視覺化黑體輻射：經典 vs 量子"""

    wavelength_nm = np.linspace(100, 3000, 1000)
    wavelength_m = wavelength_nm * 1e-9
    T = 5000  # 類似太陽表面溫度

    planck_intensity = planck_law(wavelength_m, T)
    rayleigh_intensity = rayleigh_jeans_law(wavelength_m, T)

    fig, ax = plt.subplots(figsize=(12, 8))

    # 量子理論（藍色實線）
    ax.plot(wavelength_nm, planck_intensity * 1e-13,
            'b-', linewidth=2.5, label='普朗克公式（量子理論）')

    # 經典理論（紅色虛線）——只畫長波長，短波長會爆炸
    mask = wavelength_nm > 500
    ax.plot(wavelength_nm[mask], rayleigh_intensity[mask] * 1e-13,
            'r--', linewidth=2, label='瑞利-金斯公式（經典理論）')

    # 標記紫外災難區與可見光區
    uv_region = wavelength_nm < 400
    ax.fill_between(wavelength_nm[uv_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.2, color='purple',
                     label='紫外災難區（經典理論預測無限大）')

    visible_region = (wavelength_nm >= 380) & (wavelength_nm <= 750)
    ax.fill_between(wavelength_nm[visible_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.1, color='yellow', label='可見光區')

    ax.set_xlabel('波長（nm）', fontsize=14)
    ax.set_ylabel('輻射強度（任意單位）', fontsize=14)
    ax.set_title(f'黑體輻射：經典理論的「紫外災難」 vs 量子理論的拯救\n溫度 T = {T} K',
                 fontsize=16, fontweight='bold')
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(100, 2000)
    ax.set_ylim(0, np.max(planck_intensity * 1e-13) * 1.1)

    ax.text(200, np.max(planck_intensity * 1e-13) * 0.9,
            '經典理論在此區域預測\n輻射強度趨於無限大！\n→ 「紫外災難」',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

    ax.text(800, np.max(planck_intensity * 1e-13) * 0.6,
            '普朗克公式完美符合實驗\n→ 能量必須是量子化的！',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='blue', alpha=0.3))

    plt.tight_layout()
    plt.savefig('blackbody_radiation.png', dpi=300, bbox_inches='tight')
    plt.show()

    peak_wavelength = 2.898e-3 / T
    print(f"\n【維恩位移定律】")
    print(f"溫度 T = {T} K")
    print(f"峰值波長 lambda_max = {peak_wavelength*1e9:.1f} nm")

    stefan_boltzmann = 5.67e-8
    total_power = stefan_boltzmann * T**4
    print(f"\n【斯特藩-玻爾茲曼定律】")
    print(f"總輻射功率 proportional to T^4 = {total_power:.2e} W/m2")

# 執行
visualize_blackbody_radiation()

def photoelectric_effect_simulation():
    """光電效應互動模擬"""

    metals = {
        '鈉 (Na)': 2.28,
        '鋁 (Al)': 4.08,
        '銅 (Cu)': 4.70,
        '鋅 (Zn)': 4.31,
        '銀 (Ag)': 4.73
    }

    wavelengths = np.linspace(200, 600, 100)
    frequencies = c / (wavelengths * 1e-9)
    photon_energies = h * frequencies / 1.6e-19  # 轉換為eV

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 左圖：不同金屬的截止頻率
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    for (metal, work_function), color in zip(metals.items(), colors):
        kinetic_energy = photon_energies - work_function
        kinetic_energy[kinetic_energy < 0] = 0

        ax1.plot(wavelengths, kinetic_energy,
                linewidth=2, label=f'{metal} (W0={work_function} eV)', color=color)

        cutoff_wavelength = h * c / (work_function * 1.6e-19) * 1e9
        ax1.axvline(cutoff_wavelength, color=color, linestyle='--', alpha=0.5)
        ax1.text(cutoff_wavelength, 5, f'{cutoff_wavelength:.0f}nm',
                rotation=90, va='bottom', fontsize=9, color=color)

    ax1.set_xlabel('光的波長（nm）', fontsize=13)
    ax1.set_ylabel('光電子動能（eV）', fontsize=13)
    ax1.set_title('光電效應：頻率決定電子能量\nKE = hv - W0',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(200, 600)
    ax1.set_ylim(0, 6)
    ax1.axvspan(380, 750, alpha=0.1, color='yellow', label='可見光')

    # 右圖：光強度 vs 電子數（非能量）
    intensities = np.array([1, 2, 5, 10])
    wavelength_fixed = 300  # nm
    photon_energy_fixed = h * c / (wavelength_fixed * 1e-9) / 1.6e-19

    work_function_Na = metals['鈉 (Na)']

    if photon_energy_fixed > work_function_Na:
        electron_counts = intensities * 100
        electron_energy = photon_energy_fixed - work_function_Na

        bars = ax2.bar(intensities, electron_counts, width=0.8,
                      color='skyblue', edgecolor='navy', linewidth=2)

        for bar, count in zip(bars, electron_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                    f'{int(count)}個電子\n每個能量{electron_energy:.2f}eV',
                    ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    ax2.set_xlabel('光強度（相對值）', fontsize=13)
    ax2.set_ylabel('射出的電子數', fontsize=13)
    ax2.set_title(f'光電效應：強度決定電子數量（非能量）\n金屬：鈉，光波長：{wavelength_fixed}nm',
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    ax2.text(6, 800,
            '關鍵洞見：\n'
            '光強度上升 → 電子數量上升\n'
            '但每個電子的能量相同！\n'
            '電子能量只由光頻率決定\n\n'
            '經典波動理論無法解釋！\n'
            '→ 光必須是粒子（光量子）',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('photoelectric_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*60)
    print("【光電效應虛擬實驗室】")
    print("="*60)

    chosen_metal = '鋅 (Zn)'
    work_function = metals[chosen_metal]
    print(f"\n選擇：{chosen_metal}")
    print(f"功函數 W0 = {work_function} eV")
    print(f"截止波長 lambda_0 = {h * c / (work_function * 1.6e-19) * 1e9:.1f} nm")

    test_wavelengths = [200, 300, 400, 500]
    print("\n實驗結果：")
    print("-" * 60)
    print(f"{'波長(nm)':<10} {'光子能量(eV)':<15} {'電子動能(eV)':<15} {'結果'}")
    print("-" * 60)

    for wl in test_wavelengths:
        photon_e = h * c / (wl * 1e-9) / 1.6e-19
        ke = photon_e - work_function
        if ke > 0:
            result = f"射出電子！"
        else:
            result = f"無法射出"
        print(f"{wl:<10} {photon_e:<15.2f} {max(0, ke):<15.2f} {result}")

# 執行
photoelectric_effect_simulation()

# | 選擇：鋅 (Zn)
# | 功函數 W0 = 4.31 eV
# | 截止波長 lambda_0 = 287.7 nm
# | 
# | 波長(nm)   光子能量(eV)    電子動能(eV)    結果
# | ------------------------------------------------------------
# | 200        6.20            1.89            射出電子！
# | 300        4.14            0.00            無法射出
# | 400        3.10            0.00            無法射出
# | 500        2.48            0.00            無法射出

def determinism_timeline():
    """視覺化物理學世界觀的轉變"""

    fig, ax = plt.subplots(figsize=(14, 10))

    events = [
        (1687, "牛頓\n《原理》", "確定論宇宙\nF=ma", 'blue', 1.0),
        (1814, "拉普拉斯\n妖精", "給我初始條件\n我知道一切", 'blue', 1.0),
        (1865, "馬克士威\n電磁理論", "統一電磁光\n宇宙是可知的", 'blue', 0.9),
        (1900, "普朗克\n量子假說", "能量量子化\nE=nhv", 'orange', 0.5),
        (1905, "愛因斯坦\n光量子", "光是粒子\nE=hv", 'orange', 0.4),
        (1913, "波耳\n原子模型", "電子軌道量子化\nn=1,2,3...", 'orange', 0.3),
        (1923, "德布羅意\n物質波", "粒子也是波\nlambda=h/p", 'red', 0.2),
        (1925, "海森堡\n矩陣力學", "告別可視化\n萬物皆矩陣", 'red', 0.1),
        (1926, "薛丁格\n波動力學", "波函數 psi\n機率詮釋", 'red', 0.1),
        (1927, "海森堡\n不確定性原理", "Dx·Dp >= h-bar/2\n確定性死亡", 'red', 0.0)
    ]

    years = [e[0] for e in events]
    certainties = [e[4] for e in events]

    # 背景漸變：藍→橘→紅
    for i in range(len(events)-1):
        ax.fill_between([events[i][0], events[i+1][0]], 0, 1,
                        alpha=0.3, color=events[i][3])

    # 確定性曲線
    ax.plot(years, certainties, 'k-', linewidth=3, label='「確定性」指數')
    ax.scatter(years, certainties, c=[e[3] for e in events],
              s=300, edgecolor='black', linewidth=2, zorder=5)

    # 標註事件
    for year, person, description, color, certainty in events:
        ax.text(year, certainty + 0.1, person,
               ha='center', fontsize=10, fontweight='bold')
        ax.text(year, certainty - 0.15, description,
               ha='center', fontsize=8, style='italic',
               bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

    # 三個時代
    ax.text(1750, 0.95, '經典時代\n「宇宙是時鐘」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(1910, 0.45, '量子萌芽\n「能量是分立的」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    ax.text(1926, 0.05, '量子革命\n「不確定性是本質」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

    ax.set_xlim(1680, 1935)
    ax.set_ylim(-0.2, 1.15)
    ax.set_xlabel('年份', fontsize=14)
    ax.set_ylabel('世界的「確定性」', fontsize=14)
    ax.set_title('從確定到不確定：物理學世界觀的240年演變',
                fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12, loc='upper right')
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_yticklabels(['完全不確定\n(量子世界)', '半確定\n(過渡期)', '完全確定\n(經典世界)'])

    plt.tight_layout()
    plt.savefig('determinism_timeline.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【物理學的三個世界觀】")
    print("="*70)

    worldviews = [
        {'時代': '經典時代（1687-1900）', '代表人物': '牛頓、拉普拉斯',
         '核心信念': '確定論', '宇宙比喻': '精密時鐘',
         '因果': '過去決定未來', '自由意志': '幻覺（一切已註定）',
         '上帝角色': '第一推動者'},
        {'時代': '量子萌芽（1900-1925）', '代表人物': '普朗克、愛因斯坦',
         '核心信念': '能量不連續', '宇宙比喻': '故障的時鐘',
         '因果': '仍有因果，但有限制', '自由意志': '不確定',
         '上帝角色': '「不擲骰子」（愛因斯坦堅信）'},
        {'時代': '量子革命（1925-至今）', '代表人物': '海森堡、薛丁格、波耳',
         '核心信念': '根本不確定性', '宇宙比喻': '機率雲',
         '因果': '只有機率，無必然', '自由意志': '可能存在（有空間）',
         '上帝角色': '「確實擲骰子」（波耳）'}
    ]

    for wv in worldviews:
        print(f"\n【{wv['時代']}】")
        for key, value in wv.items():
            if key != '時代':
                print(f"  {key:<10}: {value}")

# 執行
determinism_timeline()
