# Code & Cogito: 実践 ── 瞑想と量子状態
# Article: https://code-cogito.com/ja/meditation-quantum-states-practice-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Set Japanese font
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class BrainwaveSimulator:
    """
    Brainwave simulator
    Demonstrates brainwave characteristics of different meditation states
    """

    def __init__(self):
        self.sampling_rate = 256  # Hz
        self.duration = 10  # seconds
        self.t = np.linspace(0, self.duration, self.duration * self.sampling_rate)

    def generate_brainwave(self, wave_type, amplitude=1.0):
        """
        Generate different types of brainwaves
        """
        if wave_type == 'delta':
            freq = 2  # 0.5-4 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'theta':
            freq = 6  # 4-8 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'alpha':
            freq = 10  # 8-12 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'beta':
            freq = 20  # 13-30 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        elif wave_type == 'gamma':
            freq = 40  # 25-100 Hz
            wave = amplitude * np.sin(2 * np.pi * freq * self.t)
        else:
            wave = np.zeros_like(self.t)

        # Add random noise
        noise = np.random.normal(0, 0.1, len(self.t))
        return wave + noise

    def visualize_meditation_states(self):
        """
        Visualize brainwaves of different meditation states
        """
        fig, axes = plt.subplots(3, 2, figsize=(18, 14))

        # === Normal waking state ===
        ax = axes[0, 0]
        beta = self.generate_brainwave('beta', 1.0)
        alpha = self.generate_brainwave('alpha', 0.3)
        signal_normal = beta + alpha

        ax.plot(self.t[:512], signal_normal[:512], 'b-', linewidth=1)
        ax.set_xlabel('時間（秒）', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('通常覚醒状態\nベータ波主導（思考が多い）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Beginner meditation ===
        ax = axes[0, 1]
        alpha_med = self.generate_brainwave('alpha', 1.5)
        beta_low = self.generate_brainwave('beta', 0.5)
        signal_beginner = alpha_med + beta_low

        ax.plot(self.t[:512], signal_beginner[:512], 'g-', linewidth=1)
        ax.set_xlabel('時間（秒）', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('初心者の瞑想\nアルファ波増強（リラクゼーション）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Deep meditation (Theta) ===
        ax = axes[1, 0]
        theta = self.generate_brainwave('theta', 2.0)
        alpha_deep = self.generate_brainwave('alpha', 0.5)
        signal_deep = theta + alpha_deep

        ax.plot(self.t[:512], signal_deep[:512], 'purple', linewidth=1)
        ax.set_xlabel('時間（秒）', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('深い瞑想\nシータ波（深いリラクゼーション）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Advanced meditator (Gamma) ===
        ax = axes[1, 1]
        gamma = self.generate_brainwave('gamma', 3.0)
        alpha_adv = self.generate_brainwave('alpha', 1.0)
        signal_advanced = gamma + alpha_adv

        ax.plot(self.t[:512], signal_advanced[:512], 'r-', linewidth=1)
        ax.set_xlabel('時間（秒）', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('熟練瞑想者\nガンマ波（高度な集中）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === Power spectral analysis comparison ===
        ax = axes[2, 0]

        # Compute power spectral density
        freqs_normal, psd_normal = signal.welch(signal_normal, self.sampling_rate)
        freqs_beginner, psd_beginner = signal.welch(signal_beginner, self.sampling_rate)
        freqs_advanced, psd_advanced = signal.welch(signal_advanced, self.sampling_rate)

        ax.semilogy(freqs_normal, psd_normal, 'b-', label='通常', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_beginner, psd_beginner, 'g-', label='初心者', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_advanced, psd_advanced, 'r-', label='熟練者', alpha=0.7, linewidth=2)

        ax.set_xlabel('周波数（Hz）', fontsize=11)
        ax.set_ylabel('パワースペクトル密度', fontsize=11)
        ax.set_title('スペクトル解析\n各状態の脳波周波数分布',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 50)

        # Label frequency bands
        ax.axvspan(0.5, 4, alpha=0.1, color='purple', label='Delta')
        ax.axvspan(4, 8, alpha=0.1, color='blue', label='Theta')
        ax.axvspan(8, 12, alpha=0.1, color='green', label='Alpha')
        ax.axvspan(13, 30, alpha=0.1, color='orange', label='Beta')
        ax.axvspan(30, 50, alpha=0.1, color='red', label='Gamma')

        # === Summary panel ===
        ax = axes[2, 1]
        ax.axis('off')

        text = '''
        【脳波と瞑想状態】

        脳波の種類（周波数）：
        • Delta (0.5-4 Hz)：深い睡眠
        • Theta (4-8 Hz)：浅い睡眠、深い瞑想
        • Alpha (8-12 Hz)：リラックス、軽い瞑想
        • Beta (13-30 Hz)：通常覚醒、思考
        • Gamma (25-100 Hz)：高度な集中、意識統合

        瞑想による脳波の変化：
        1. 初心者：
           → Beta↓（思考の減少）
           → Alpha↑（リラクゼーション増加）

        2. 中級者：
           → Thetaの増加（深いリラクゼーション）
           → 「禅定」状態に入る可能性

        3. 熟練者（10,000時間以上）：
           → Gammaの著しい増強（増加幅は対照群の30倍超！）
           → 異なる脳領域の高度な同期
           → 意識統合度が極めて高い

        Orch OR理論の予測：
        • Gamma波40Hz ≈ 量子収縮頻度
        • 熟練瞑想者のGamma波増強は
          微小管の量子過程を反映？

        主要な発見（Lutz, Davidsonら 2004）：
        • 瞑想中にガンマ活動が大きく増加
        • 瞑想前の安静時からすでに対照群より高い
        • 著者らは長短期の神経変化の可能性を示唆
        '''

        ax.text(0.05, 0.5, text, fontsize=10, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='lightyellow',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('brainwave_meditation_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【脳波と瞑想：神経科学の証拠】")
        print("="*70)

        print("\n脳波の5種類：")
        print("  1. Delta (0.5-4 Hz)：深い睡眠")
        print("  2. Theta (4-8 Hz)：浅い睡眠、深い瞑想、創造性")
        print("  3. Alpha (8-12 Hz)：リラックスだが覚醒、軽い瞑想")
        print("  4. Beta (13-30 Hz)：通常覚醒、思考、集中")
        print("  5. Gamma (25-100 Hz)：高度な集中、意識統合")

        print("\n瞑想による脳波の変化：")
        print("  初心者（数週間の経験）：")
        print("    • ベータ波の低下 → 思考の減少")
        print("    • アルファ波の増強 → リラクゼーション増加")

        print("\n  中級者（数ヶ月〜数年）：")
        print("    • シータ波の増加 → 深いリラクゼーション")
        print("    • 「禅定」状態に入る可能性")

        print("\n  熟練者（10,000時間以上）：")
        print("    • ガンマ波の著しい増強（増加幅は対照群の30倍超！）")
        print("    • 異なる脳領域の高度な同期")
        print("    • 意識統合度が極めて高い")

        print("\nDavidson実験（2004）：")
        print("  • 8名のチベット仏教高僧")
        print("  • 累計瞑想時間：10,000〜50,000時間")
        print("  • 結果：瞑想中のガンマ活動の増加幅が対照群の30倍超")

        print("\nOrch OR理論の予測：")
        print("  • 量子収縮頻度 ≈ 40 Hz")
        print("  • ガンマ波周波数 ≈ 40 Hz")
        print("  • 関連性はあるのか？")

        print("\n考えうる説明：")
        print("  • ガンマ波が微小管の量子収縮を反映")
        print("  • 瞑想が微小管間の同期を増強")
        print("  • より強く、より同期したガンマ波を生成")

        print("\n注意：")
        print("  • これはあくまで推測！")
        print("  • 瞑想中の微小管に量子過程が起きている直接的証拠はない")
        print("  • しかし相関関係は驚くべきものがある")
        print("="*70)

# Run
brainwave_sim = BrainwaveSimulator()
brainwave_sim.visualize_meditation_states()

class NeuroplasticitySimulator:
    """
    Neuroplasticity simulator
    Demonstrates how long-term meditation changes brain structure
    """

    def __init__(self):
        pass

    def visualize_brain_changes(self):
        """
        Visualize meditation-induced brain changes
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        # === Gray matter density changes ===
        ax = axes[0, 0]

        brain_regions = ['海馬\n（記憶）', '前頭前皮質\n（集中）', '島皮質\n（共感）',
                        '扁桃体\n（恐怖）']
        control_group = [100, 100, 100, 100]
        meditators = [115, 120, 118, 85]  # Relative values

        x = np.arange(len(brain_regions))
        width = 0.35

        bars1 = ax.bar(x - width/2, control_group, width, label='対照群',
                      color='lightblue', edgecolor='black', linewidth=1.5)
        bars2 = ax.bar(x + width/2, meditators, width, label='瞑想者',
                      color='lightgreen', edgecolor='black', linewidth=1.5)

        ax.set_ylabel('相対灰白質密度（%）', fontsize=11)
        ax.set_title('灰白質密度の変化\n長期瞑想者 vs 対照群',
                    fontsize=13, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(brain_regions, fontsize=10)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # Label changes
        for i, (c, m) in enumerate(zip(control_group, meditators)):
            change = m - c
            color = 'green' if change > 0 else 'red'
            ax.text(i, max(c, m) + 3, f'{change:+d}%', ha='center',
                   fontsize=10, fontweight='bold', color=color)

        # === Meditation hours vs gray matter density ===
        ax = axes[0, 1]

        hours = np.array([0, 1000, 5000, 10000, 20000, 40000])
        hippocampus = 100 + 20 * (1 - np.exp(-hours/15000))
        prefrontal = 100 + 25 * (1 - np.exp(-hours/12000))

        ax.plot(hours/1000, hippocampus, 'o-', linewidth=3, markersize=8,
               label='海馬', color='blue')
        ax.plot(hours/1000, prefrontal, 's-', linewidth=3, markersize=8,
               label='前頭前皮質', color='green')

        ax.set_xlabel('瞑想時間（千時間）', fontsize=11)
        ax.set_ylabel('相対灰白質密度（%）', fontsize=11)
        ax.set_title('用量-反応関係\n瞑想時間が長いほど効果が顕著',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # === Default Mode Network (DMN) activity ===
        ax = axes[0, 2]

        states = ['安静時\n（通常）', '安静時\n（瞑想者）', '課題中\n（通常）', '課題中\n（瞑想者）']
        dmn_activity = [100, 70, 40, 30]
        colors = ['lightcoral', 'lightgreen', 'lightblue', 'lightgreen']

        bars = ax.bar(states, dmn_activity, color=colors, edgecolor='black',
                     linewidth=1.5)
        ax.set_ylabel('DMN活動（%）', fontsize=11)
        ax.set_title('デフォルトモードネットワーク（DMN）\n瞑想者の自己中心的思考の減少',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # Labels
        for bar, activity in zip(bars, dmn_activity):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 3,
                   f'{activity}%', ha='center', fontsize=10, fontweight='bold')

        # === Brain structural changes schematic ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Simplified brain outline
        from matplotlib.patches import Ellipse, FancyBboxPatch

        # Brain outline
        brain = Ellipse((0.5, 0.5), 0.6, 0.7, angle=0,
                       facecolor='lightgray', alpha=0.3,
                       edgecolor='black', linewidth=2)
        ax.add_patch(brain)

        # Label regions with increase (green)
        regions_increase = [
            (0.35, 0.7, '前頭前皮質\n+20%', 'lightgreen'),
            (0.5, 0.3, '海馬\n+15%', 'lightgreen'),
            (0.65, 0.5, '島皮質\n+18%', 'lightgreen'),
        ]

        for x, y, label, color in regions_increase:
            circle = plt.Circle((x, y), 0.08, color=color, alpha=0.7,
                               edgecolor='darkgreen', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y-0.12, label, ha='center', fontsize=9,
                   fontweight='bold')

        # Label regions with decrease (red)
        circle_amygdala = plt.Circle((0.5, 0.6), 0.06, color='lightcoral',
                                    alpha=0.7, edgecolor='darkred', linewidth=2)
        ax.add_patch(circle_amygdala)
        ax.text(0.5, 0.52, '扁桃体\n-15%', ha='center', fontsize=9,
               fontweight='bold')

        ax.set_title('脳構造変化の概略\n長期瞑想の神経可塑性',
                    fontsize=13, fontweight='bold')

        # === White matter connectivity ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Left: control group (sparse connections)
        ax.text(0.25, 0.95, '対照群', ha='center', fontsize=12,
               fontweight='bold')

        n_nodes = 6
        angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
        nodes_x = 0.25 + 0.15 * np.cos(angles)
        nodes_y = 0.5 + 0.15 * np.sin(angles)

        # Sparse connections
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.3:  # 30% connectivity
                    ax.plot([nodes_x[i], nodes_x[j]], [nodes_y[i], nodes_y[j]],
                           'gray', alpha=0.3, linewidth=1)

        # Nodes
        ax.scatter(nodes_x, nodes_y, s=200, c='lightblue',
                  edgecolors='blue', linewidths=2, zorder=5)

        # Right: meditators (dense connections)
        ax.text(0.75, 0.95, '瞑想者', ha='center', fontsize=12,
               fontweight='bold')

        nodes_x2 = 0.75 + 0.15 * np.cos(angles)
        nodes_y2 = 0.5 + 0.15 * np.sin(angles)

        # Dense connections
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.8:  # 80% connectivity
                    ax.plot([nodes_x2[i], nodes_x2[j]], [nodes_y2[i], nodes_y2[j]],
                           'green', alpha=0.5, linewidth=2)

        # Nodes
        ax.scatter(nodes_x2, nodes_y2, s=200, c='lightgreen',
                  edgecolors='darkgreen', linewidths=2, zorder=5)

        ax.set_title('白質結合\n瞑想者の脳領域間結合はより緊密',
                    fontsize=13, fontweight='bold')

        # === Summary panel ===
        ax = axes[1, 2]
        ax.axis('off')

        text_summary = '''
        【神経可塑性：瞑想が脳を変える】

        灰白質密度の変化：
        + 海馬：+15%（記憶、学習）
        + 前頭前皮質：+20%（意思決定、集中）
        + 島皮質：+18%（共感）
        - 扁桃体：-15%（恐怖、ストレス）

        白質結合：
        • 異なる脳領域間の結合が増強
        • 情報伝達がより効率的に
        • 脳ネットワークの統合性が向上

        デフォルトモードネットワーク（DMN）：
        • 自己中心的思考の減少
        • マインドワンダリングの減少
        • 「今ここ」への気づきの増強

        時間効果：
        • 効果は瞑想時間に比例して増加
        • 10,000時間以上：顕著な変化
        • ただし初心者（数週間）でも効果あり

        主要な知見：
        「修行」は心理的テクニックにとどまらず
        生物学的基盤を持つ
        脳の物理的構造の変化である

        これは測定可能かつ再現可能な
        神経可塑性の証拠である
        '''

        ax.text(0.05, 0.5, text_summary, fontsize=9, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('neuroplasticity_meditation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【神経可塑性：瞑想はいかに脳を変えるか】")
        print("="*70)

        print("\n灰白質密度の変化（長期瞑想者 vs 対照群）：")
        print("  増加した領域：")
        print("    • 海馬：+15%（記憶、学習）")
        print("    • 前頭前皮質：+20%（意思決定、集中、自己制御）")
        print("    • 島皮質：+18%（内受容感覚、共感）")
        print("  減少した領域：")
        print("    • 扁桃体：-15%（恐怖、ストレス反応）")

        print("\n白質結合：")
        print("  • 異なる脳領域間の結合が増強")
        print("  • 情報伝達がより効率的に")
        print("  • 脳ネットワークの統合性が向上")

        print("\nデフォルトモードネットワーク（DMN）：")
        print("  • DMN：脳が「何もしていない」ときの活動")
        print("  • 自己意識、マインドワンダリングと関連")
        print("  • 瞑想者のDMN活動は30%減少")
        print("  → 自己中心的思考の減少")
        print("  → 「今ここ」への気づきの増加")

        print("\n時間効果（用量-反応）：")
        print("  • 効果は瞑想時間に比例して増加")
        print("  • 10,000時間：顕著な変化")
        print("  • ただし初心者（8週間）でも測定可能な効果あり")

        print("\n重要な研究：")
        print("  • Davidson et al. (2004)：熟練瞑想者")
        print("  • Lazar et al. (2005)：皮質の厚さ")
        print("  • Holzel et al. (2011)：8週間のマインドフルネスプログラム")

        print("\n神経可塑性（Neuroplasticity）：")
        print("  • 脳は経験に基づいて構造を変化させることができる")
        print("  • 機能だけでなく、物理的構造が変わる")
        print("  • 「修行」には生物学的基盤がある")

        print("\n哲学的意義：")
        print("  • 東洋の修行伝統は「修行は心を変える」と説く")
        print("  • 現代の神経科学は確認する：")
        print("    修行は確かに脳を変える（心の物質的基盤を）")
        print("  • 理論と実践の統一")
        print("="*70)

# Run
neuro_sim = NeuroplasticitySimulator()
neuro_sim.visualize_brain_changes()

def visualize_vipassana_measurement():
    """
    Visualize the analogy between Vipassana meditation and quantum measurement
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === Quantum: Before measurement (superposition) ===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Multiple possibilities
    possibilities = ['|0>', '|1>', '|2>', '|3>']
    positions = [(0.3, 0.7), (0.7, 0.7), (0.3, 0.3), (0.7, 0.3)]

    for poss, pos in zip(possibilities, positions):
        circle = plt.Circle(pos, 0.08, color='purple', alpha=0.3,
                           edgecolor='purple', linewidth=2)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], poss, ha='center', va='center',
               fontsize=11, fontweight='bold')

    # Lines (entanglement)
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]],
                   'purple', alpha=0.2, linewidth=1.5)

    ax.text(0.5, 0.9, '測定前：重ね合わせ状態', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, '|ψ⟩ = Σ(αᵢ|i⟩)\nすべての可能性が同時に存在',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

    # === Quantum: Measurement (collapse) ===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Measurement
    ax.text(0.5, 0.80, '[ 測定 ]', ha='center', fontsize=16, fontweight='bold')

    # Arrow
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))

    # Result
    circle = plt.Circle((0.5, 0.3), 0.12, color='green', alpha=0.7,
                       edgecolor='darkgreen', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, '|2⟩', ha='center', va='center',
           fontsize=14, fontweight='bold', color='white')

    ax.text(0.5, 0.1, '測定後：確定状態\n波動関数の収縮',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === Vipassana: Before observation (chaotic thoughts) ===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Chaotic thoughts
    thoughts = ['怒', '喜', '悲', '懼', '愛', '憎', '欲', '貪']
    np.random.seed(42)
    for thought in thoughts:
        x, y = np.random.random(2) * 0.6 + 0.2
        ax.text(x, y, thought, fontsize=12, alpha=0.4,
               color=np.random.choice(['red', 'blue', 'green', 'purple']))

    # Center: unclear mind
    circle = plt.Circle((0.5, 0.5), 0.12, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n混沌', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.9, '観察前：念頭の混沌', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, '念頭が飛び交う\n不明瞭、不確定',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === Vipassana: Awareness (observation) ===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Awareness
    ax.text(0.5, 0.80, '[ 気づき ]', ha='center', fontsize=16, fontweight='bold',
           color='goldenrod')

    # Arrow
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='gold'))

    # Illuminated thought
    circle = plt.Circle((0.5, 0.3), 0.12, color='yellow', alpha=0.7,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, '怒', ha='center', va='center',
           fontsize=16, fontweight='bold')

    # Disappear
    ax.text(0.7, 0.3, '→ 消滅', ha='left', fontsize=10,
           color='gray', style='italic')

    ax.text(0.5, 0.1, '気づきの瞬間：念頭が照見される\n力を失い、消滅する',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Main title
    fig.text(0.5, 0.98, '内観瞑想 vs 量子測定',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('vipassana_measurement_analogy.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【内観瞑想と量子測定の深いアナロジー】")
    print("="*70)

    print("\n量子測定：")
    print("  測定前：系は重ね合わせ状態にある")
    print("    → |ψ⟩ = Σ(αᵢ|i⟩)")
    print("    → すべての可能性が同時に存在")

    print("\n  測定時：観察者が介入")
    print("    → 波動関数の収縮")

    print("\n  測定後：系は確定状態になる")
    print("    → |ψ⟩ → |i⟩")
    print("    → 一つの結果に確定")

    print("\n内観瞑想（ヴィパッサナー）：")
    print("  観察前：念頭は混沌")
    print("    → 怒、喜、悲、懼...が飛び交う")
    print("    → 不明瞭、不確定")

    print("\n  観察時：気づきが生じる")
    print("    → 念頭を「見つめる」")
    print("    → 追わず、抑えず")

    print("\n  観察後：念頭が照見される")
    print("    → 念頭は力を失う")
    print("    → 自然に消滅する")

    print("\n共通の構造：")
    print("  1. 「観察」が核心的な行為である")
    print("  2. 観察前：不確定、混沌")
    print("  3. 観察時：介入、照見")
    print("  4. 観察後：確定または消滅")

    print("\n対応関係：")
    print("  重ね合わせ状態 ～ 念頭の混沌")
    print("  測定 ～ 気づき")
    print("  収縮 ～ 念頭の顕現／消滅")
    print("  観察者 ～ 気づきそのもの")

    print("\n核心的洞察：")
    print("  • 「観察」が「被観察者」を変える")
    print("  • 量子力学ではこれは物理法則")
    print("  • 内観ではこれは心理的体験")
    print("  • 構造は驚くほど相似している")

    print("\nただし注意：")
    print("  • これはアナロジーであり、同一性ではない")
    print("  • 心理過程 ≠ 量子過程")
    print("  • しかし構造的対応は深い省察に値する")
    print("="*70)

# Run
visualize_vipassana_measurement()

def visualize_no_mind_superposition():
    """
    Visualize the correspondence between no-mind state and superposition
    """

    fig = plt.figure(figsize=(18, 10))

    # === Top left: Having-mind (definite state) ===
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # One thought (attachment)
    circle = plt.Circle((0.5, 0.5), 0.2, color='red', alpha=0.7,
                       edgecolor='darkred', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.5, '愛', ha='center', va='center',
            fontsize=24, fontweight='bold', color='white')

    # Arrows pointing inward (attachment)
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax1.annotate('', xy=(0.5, 0.5), xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red'))

    ax1.set_title('有念：一つの念頭に執着\n「愛」→「憎」の対立を生む',
                 fontsize=13, fontweight='bold')

    # === Top right: No-mind (superposition) ===
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # Multiple thoughts present but no attachment
    emotions = ['喜', '怒', '哀', '楽', '愛', '憎']
    angles = np.linspace(0, 2*np.pi, len(emotions), endpoint=False)

    for emotion, angle in zip(emotions, angles):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        circle = plt.Circle((x, y), 0.08, color='lightblue', alpha=0.5,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, emotion, ha='center', va='center',
                fontsize=11)

    # Center: emptiness
    circle_center = plt.Circle((0.5, 0.5), 0.12, color='gold', alpha=0.7,
                              edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.5, '無念', ha='center', va='center',
            fontsize=12, fontweight='bold')

    ax2.set_title('無念：念頭に住さず\n対立を超え、開放性を保つ',
                 fontsize=13, fontweight='bold')

    # === Bottom left: Quantum definite state (|0>) ===
    ax3 = fig.add_subplot(2, 2, 3)

    states = ['|0⟩', '|1⟩']
    probs = [1.0, 0.0]

    bars = ax3.bar(states, probs, color=['blue', 'lightgray'],
                  edgecolor='black', linewidth=2, alpha=0.7)
    ax3.set_ylabel('確率', fontsize=11)
    ax3.set_title('量子確定状態\n|0⟩：完全に確定',
                 fontsize=13, fontweight='bold')
    ax3.set_ylim(0, 1.2)
    ax3.grid(True, alpha=0.3, axis='y')

    # === Bottom right: Quantum superposition ===
    ax4 = fig.add_subplot(2, 2, 4)

    n_states = 4
    states2 = [f'|{i}⟩' for i in range(n_states)]
    probs2 = [0.5, 0.3, 0.15, 0.05]

    bars2 = ax4.bar(states2, probs2, color='purple',
                   edgecolor='black', linewidth=2, alpha=0.6)
    ax4.set_ylabel('振幅の二乗（確率）', fontsize=11)
    ax4.set_title('量子重ね合わせ状態\n|ψ⟩ = Σ(αᵢ|i⟩)：多様な可能性',
                 fontsize=13, fontweight='bold')
    ax4.set_ylim(0, 0.6)
    ax4.grid(True, alpha=0.3, axis='y')

    # Main title
    fig.text(0.5, 0.98, '無念 vs 重ね合わせ状態：開放性と潜在性',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('no_mind_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【無念と重ね合わせ状態：開放性と潜在性】")
    print("="*70)

    print("\n有念（確定状態）：")
    print("  • 一つの念頭に執着する")
    print("  • 例：「愛」に執着する")
    print("  • すると「愛／憎」の対立が生まれる")
    print("  • 開放性を失う")
    print("  • 量子確定状態|0⟩に似ている")

    print("\n無念（重ね合わせ状態）：")
    print("  • 念頭は来ては去り、住さない")
    print("  • いかなる念頭にも執着しない")
    print("  • 対立を超越する")
    print("  • 開放性を保つ")
    print("  • 量子重ね合わせ状態Σ(αᵢ|i⟩)に似ている")

    print("\n六祖慧能の教え：")
    print("  「何ぞ期せん自性の本より自ら清浄なることを」")
    print("  → 本来の面目は「無念」（清浄）である")

    print("\n  「念念住せず」")
    print("  → いかなる念頭にも執着しない")
    print("  → 「無念」の状態を保つ")

    print("\n量子コンピューティングの課題：")
    print("  • 重ね合わせ状態を収縮させずに保つ")
    print("  • デコヒーレンスを回避する")
    print("  • コヒーレンス時間を延長する")

    print("\n禅修行の課題：")
    print("  • 無念を保ち、起念を避ける")
    print("  • 執着を回避する")
    print("  • 「清明」の時間を延長する")

    print("\n対応関係：")
    print("  重ね合わせ状態 ～ 無念")
    print("  確定状態 ～ 有念（執着）")
    print("  測定／環境 ～ 起念／境界")
    print("  デコヒーレンス ～ 失念")

    print("\n共通の洞察：")
    print("  • 「無念／重ね合わせ状態」は「空虚」ではない")
    print("  • むしろ、より根源的でより豊かな状態")
    print("  • 無限の潜在性を持つ")
    print("  • 固定された二元対立を超越する")

    print("\n最終的な洞察：")
    print("  「無念」も「重ね合わせ状態」も指し示すのは：")
    print("  固定を超え、潜在性に満ちた")
    print("  開放的な状態である")
    print("="*70)

# Run
visualize_no_mind_superposition()
