# Code & Cogito: 量子革命前夜——ニュートンの宇宙が崩壊し始めたとき
# Article: https://code-cogito.com/ja/quantum-revolution-newton-universe-collapse-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

# | ∇·E = ρ/ε₀        （ガウスの法則）
# | ∇·B = 0            （磁場の発散なし）
# | ∇×E = -∂B/∂t       （ファラデーの法則）
# | ∇×B = μ₀J + μ₀ε₀∂E/∂t  （アンペール-マクスウェルの法則）

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# Japanese font configuration
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def planck_law(wavelength, T):
    """Planck's law (quantum theory)"""
    return (8 * np.pi * h * c / wavelength**5) / (np.exp(h * c / (wavelength * k * T)) - 1)

def rayleigh_jeans_law(wavelength, T):
    """Rayleigh-Jeans law (classical theory)"""
    return 8 * np.pi * k * T / wavelength**4

def visualize_blackbody_radiation():
    """Visualize blackbody radiation: classical vs quantum"""

    wavelength_nm = np.linspace(100, 3000, 1000)
    wavelength_m = wavelength_nm * 1e-9
    T = 5000  # Approximate solar surface temperature

    planck_intensity = planck_law(wavelength_m, T)
    rayleigh_intensity = rayleigh_jeans_law(wavelength_m, T)

    fig, ax = plt.subplots(figsize=(12, 8))

    # Quantum theory (blue solid line)
    ax.plot(wavelength_nm, planck_intensity * 1e-13,
            'b-', linewidth=2.5, label='プランク公式（量子理論）')

    # Classical theory (red dashed line) - only plot long wavelengths; short wavelengths explode
    mask = wavelength_nm > 500
    ax.plot(wavelength_nm[mask], rayleigh_intensity[mask] * 1e-13,
            'r--', linewidth=2, label='レイリー-ジーンズ公式（古典理論）')

    # Mark UV catastrophe region and visible light region
    uv_region = wavelength_nm < 400
    ax.fill_between(wavelength_nm[uv_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.2, color='purple',
                     label='紫外破綻領域（古典理論は無限大を予測）')

    visible_region = (wavelength_nm >= 380) & (wavelength_nm <= 750)
    ax.fill_between(wavelength_nm[visible_region], 0,
                     np.max(planck_intensity * 1e-13) * 1.2,
                     alpha=0.1, color='yellow', label='可視光領域')

    ax.set_xlabel('波長（nm）', fontsize=14)
    ax.set_ylabel('放射強度（任意単位）', fontsize=14)
    ax.set_title(f'黒体放射：古典理論の「紫外破綻」vs 量子理論の救済\n温度 T = {T} K',
                 fontsize=16, fontweight='bold')
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(100, 2000)
    ax.set_ylim(0, np.max(planck_intensity * 1e-13) * 1.1)

    ax.text(200, np.max(planck_intensity * 1e-13) * 0.9,
            '古典理論はこの領域で\n放射強度が無限大に！\n→「紫外破綻」',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

    ax.text(800, np.max(planck_intensity * 1e-13) * 0.6,
            'プランク公式は実験と完全一致\n→ エネルギーは量子化される！',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='blue', alpha=0.3))

    plt.tight_layout()
    plt.savefig('blackbody_radiation.png', dpi=300, bbox_inches='tight')
    plt.show()

    peak_wavelength = 2.898e-3 / T
    print(f"\n【ウィーンの変位則】")
    print(f"温度 T = {T} K")
    print(f"ピーク波長 λ_max = {peak_wavelength*1e9:.1f} nm")

    stefan_boltzmann = 5.67e-8
    total_power = stefan_boltzmann * T**4
    print(f"\n【シュテファン-ボルツマンの法則】")
    print(f"全放射パワー ∝ T⁴ = {total_power:.2e} W/m²")

# Execute
visualize_blackbody_radiation()

def photoelectric_effect_simulation():
    """Photoelectric effect simulation"""

    metals = {
        'ナトリウム (Na)': 2.28,
        'アルミニウム (Al)': 4.08,
        '銅 (Cu)': 4.70,
        '亜鉛 (Zn)': 4.31,
        '銀 (Ag)': 4.73
    }

    wavelengths = np.linspace(200, 600, 100)
    frequencies = c / (wavelengths * 1e-9)
    photon_energies = h * frequencies / 1.6e-19  # Convert to eV

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Left panel: cutoff frequencies of different metals
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    for (metal, work_function), color in zip(metals.items(), colors):
        kinetic_energy = photon_energies - work_function
        kinetic_energy[kinetic_energy < 0] = 0

        ax1.plot(wavelengths, kinetic_energy,
                linewidth=2, label=f'{metal} (W₀={work_function} eV)', color=color)

        cutoff_wavelength = h * c / (work_function * 1.6e-19) * 1e9
        ax1.axvline(cutoff_wavelength, color=color, linestyle='--', alpha=0.5)
        ax1.text(cutoff_wavelength, 5, f'{cutoff_wavelength:.0f}nm',
                rotation=90, va='bottom', fontsize=9, color=color)

    ax1.set_xlabel('光の波長（nm）', fontsize=13)
    ax1.set_ylabel('光電子の運動エネルギー（eV）', fontsize=13)
    ax1.set_title('光電効果：周波数が電子エネルギーを決定\nKE = hν - W₀',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(200, 600)
    ax1.set_ylim(0, 6)
    ax1.axvspan(380, 750, alpha=0.1, color='yellow', label='可視光')

    # Right panel: light intensity vs electron count (not energy)
    intensities = np.array([1, 2, 5, 10])
    wavelength_fixed = 300  # nm
    photon_energy_fixed = h * c / (wavelength_fixed * 1e-9) / 1.6e-19

    work_function_Na = metals['ナトリウム (Na)']

    if photon_energy_fixed > work_function_Na:
        electron_counts = intensities * 100
        electron_energy = photon_energy_fixed - work_function_Na

        bars = ax2.bar(intensities, electron_counts, width=0.8,
                      color='skyblue', edgecolor='navy', linewidth=2)

        for bar, count in zip(bars, electron_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                    f'{int(count)}個の電子\n各エネルギー{electron_energy:.2f}eV',
                    ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    ax2.set_xlabel('光の強度（相対値）', fontsize=13)
    ax2.set_ylabel('放出された電子数', fontsize=13)
    ax2.set_title(f'光電効果：強度は電子の数を決定（エネルギーではない）\n金属：ナトリウム、光の波長：{wavelength_fixed}nm',
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    ax2.text(6, 800,
            '重要な洞察：\n'
            '光の強度上昇 → 電子数が増加\n'
            'しかし各電子のエネルギーは同じ！\n'
            '電子のエネルギーは光の周波数のみで決定\n\n'
            '古典的波動理論では説明不可能！\n'
            '→ 光は粒子（光量子）でなければならない',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig('photoelectric_effect.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*60)
    print("【光電効果 仮想実験室】")
    print("="*60)

    chosen_metal = '亜鉛 (Zn)'
    work_function = metals[chosen_metal]
    print(f"\n選択：{chosen_metal}")
    print(f"仕事関数 W₀ = {work_function} eV")
    print(f"遮断波長 λ₀ = {h * c / (work_function * 1.6e-19) * 1e9:.1f} nm")

    test_wavelengths = [200, 300, 400, 500]
    print("\n実験結果：")
    print("-" * 60)
    print(f"{'波長(nm)':<10} {'光子エネルギー(eV)':<20} {'電子の運動エネルギー(eV)':<25} {'結果'}")
    print("-" * 60)

    for wl in test_wavelengths:
        photon_e = h * c / (wl * 1e-9) / 1.6e-19
        ke = photon_e - work_function
        if ke > 0:
            result = f"電子放出！"
        else:
            result = f"放出不可"
        print(f"{wl:<10} {photon_e:<20.2f} {max(0, ke):<25.2f} {result}")

# Execute
photoelectric_effect_simulation()

# | 選択：亜鉛 (Zn)
# | 仕事関数 W₀ = 4.31 eV
# | 遮断波長 λ₀ = 287.7 nm
# | 
# | 波長(nm)   光子エネルギー(eV)   電子の運動エネルギー(eV)  結果
# | ------------------------------------------------------------
# | 200        6.20                 1.89                      電子放出！
# | 300        4.14                 0.00                      放出不可
# | 400        3.10                 0.00                      放出不可
# | 500        2.48                 0.00                      放出不可

def determinism_timeline():
    """Visualize the transformation of physics worldview"""

    fig, ax = plt.subplots(figsize=(14, 10))

    events = [
        (1687, "ニュートン\n『プリンキピア』", "決定論的宇宙\nF=ma", 'blue', 1.0),
        (1814, "ラプラスの\n悪魔", "初期条件を与えよ\nすべてが分かる", 'blue', 1.0),
        (1865, "マクスウェル\n電磁理論", "電磁光の統一\n宇宙は知りうる", 'blue', 0.9),
        (1900, "プランク\n量子仮説", "エネルギー量子化\nE=nhν", 'orange', 0.5),
        (1905, "アインシュタイン\n光量子", "光は粒子\nE=hν", 'orange', 0.4),
        (1913, "ボーア\n原子模型", "電子軌道の量子化\nn=1,2,3...", 'orange', 0.3),
        (1923, "ド・ブロイ\n物質波", "粒子も波である\nλ=h/p", 'red', 0.2),
        (1925, "ハイゼンベルク\n行列力学", "可視化との訣別\n万物は行列", 'red', 0.1),
        (1926, "シュレーディンガー\n波動力学", "波動関数 ψ\n確率解釈", 'red', 0.1),
        (1927, "ハイゼンベルク\n不確定性原理", "Δx·Δp ≥ ℏ/2\n確定性の死", 'red', 0.0)
    ]

    years = [e[0] for e in events]
    certainties = [e[4] for e in events]

    # Background gradient: blue -> orange -> red
    for i in range(len(events)-1):
        ax.fill_between([events[i][0], events[i+1][0]], 0, 1,
                        alpha=0.3, color=events[i][3])

    # Certainty curve
    ax.plot(years, certainties, 'k-', linewidth=3, label='「確定性」指数')
    ax.scatter(years, certainties, c=[e[3] for e in events],
              s=300, edgecolor='black', linewidth=2, zorder=5)

    # Annotate events
    for year, person, description, color, certainty in events:
        ax.text(year, certainty + 0.1, person,
               ha='center', fontsize=10, fontweight='bold')
        ax.text(year, certainty - 0.15, description,
               ha='center', fontsize=8, style='italic',
               bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

    # Three eras
    ax.text(1750, 0.95, '古典時代\n「宇宙は時計仕掛け」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(1910, 0.45, '量子の萌芽\n「エネルギーは離散的」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    ax.text(1926, 0.05, '量子革命\n「不確定性こそ本質」',
           fontsize=14, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

    ax.set_xlim(1680, 1935)
    ax.set_ylim(-0.2, 1.15)
    ax.set_xlabel('年', fontsize=14)
    ax.set_ylabel('世界の「確定性」', fontsize=14)
    ax.set_title('確定から不確定へ：物理学の世界観の240年の変遷',
                fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12, loc='upper right')
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_yticklabels(['完全に不確定\n（量子の世界）', '半確定\n（過渡期）', '完全に確定\n（古典の世界）'])

    plt.tight_layout()
    plt.savefig('determinism_timeline.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【物理学の三つの世界観】")
    print("="*70)

    worldviews = [
        {'時代': '古典時代（1687-1900）', '代表人物': 'ニュートン、ラプラス',
         '核心的信念': '決定論', '宇宙の比喩': '精密な時計仕掛け',
         '因果': '過去が未来を決定', '自由意志': '幻想（すべては決定済み）',
         '神の役割': '第一原因（最初の一押し）'},
        {'時代': '量子の萌芽（1900-1925）', '代表人物': 'プランク、アインシュタイン',
         '核心的信念': 'エネルギーは不連続', '宇宙の比喩': '故障した時計',
         '因果': '因果は残るが限界あり', '自由意志': '不明',
         '神の役割': '「サイコロを振らない」（アインシュタインの確信）'},
        {'時代': '量子革命（1925-現在）', '代表人物': 'ハイゼンベルク、シュレーディンガー、ボーア',
         '核心的信念': '根源的不確定性', '宇宙の比喩': '確率の雲',
         '因果': '確率のみ、必然なし', '自由意志': '存在しうる（余地がある）',
         '神の役割': '「確かにサイコロを振る」（ボーア）'}
    ]

    for wv in worldviews:
        print(f"\n【{wv['時代']}】")
        for key, value in wv.items():
            if key != '時代':
                print(f"  {key:<12}: {value}")

# Execute
determinism_timeline()
