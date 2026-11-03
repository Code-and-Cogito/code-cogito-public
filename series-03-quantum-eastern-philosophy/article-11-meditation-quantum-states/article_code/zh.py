# Code & Cogito: 實踐——冥想與量子態
# Article: https://code-cogito.com/meditation-quantum-states-practice/
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class BrainwaveSimulator:
    """
    腦波模擬器
    展示：不同冥想狀態的腦波特徵
    """

    def __init__(self):
        self.sampling_rate = 256  # Hz
        self.duration = 10  # seconds
        self.t = np.linspace(0, self.duration, self.duration * self.sampling_rate)

    def generate_brainwave(self, wave_type, amplitude=1.0):
        """
        生成不同類型的腦波
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

        # 加入隨機噪音
        noise = np.random.normal(0, 0.1, len(self.t))
        return wave + noise

    def visualize_meditation_states(self):
        """
        視覺化不同冥想狀態的腦波
        """
        fig, axes = plt.subplots(3, 2, figsize=(18, 14))

        # === 正常清醒狀態 ===
        ax = axes[0, 0]
        beta = self.generate_brainwave('beta', 1.0)
        alpha = self.generate_brainwave('alpha', 0.3)
        signal_normal = beta + alpha

        ax.plot(self.t[:512], signal_normal[:512], 'b-', linewidth=1)
        ax.set_xlabel('時間 (秒)', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('正常清醒狀態\nBeta波主導（思慮多）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === 初學者冥想 ===
        ax = axes[0, 1]
        alpha_med = self.generate_brainwave('alpha', 1.5)
        beta_low = self.generate_brainwave('beta', 0.5)
        signal_beginner = alpha_med + beta_low

        ax.plot(self.t[:512], signal_beginner[:512], 'g-', linewidth=1)
        ax.set_xlabel('時間 (秒)', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('初學者冥想\nAlpha波增強（放鬆）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === 深度冥想（Theta）===
        ax = axes[1, 0]
        theta = self.generate_brainwave('theta', 2.0)
        alpha_deep = self.generate_brainwave('alpha', 0.5)
        signal_deep = theta + alpha_deep

        ax.plot(self.t[:512], signal_deep[:512], 'purple', linewidth=1)
        ax.set_xlabel('時間 (秒)', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('深度冥想\nTheta波（深度放鬆）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === 資深冥想者（Gamma）===
        ax = axes[1, 1]
        gamma = self.generate_brainwave('gamma', 3.0)
        alpha_adv = self.generate_brainwave('alpha', 1.0)
        signal_advanced = gamma + alpha_adv

        ax.plot(self.t[:512], signal_advanced[:512], 'r-', linewidth=1)
        ax.set_xlabel('時間 (秒)', fontsize=11)
        ax.set_ylabel('振幅', fontsize=11)
        ax.set_title('資深冥想者\nGamma波（高度專注）',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 2)

        # === 頻譜分析對比 ===
        ax = axes[2, 0]

        # 計算功率譜
        freqs_normal, psd_normal = signal.welch(signal_normal, self.sampling_rate)
        freqs_beginner, psd_beginner = signal.welch(signal_beginner, self.sampling_rate)
        freqs_advanced, psd_advanced = signal.welch(signal_advanced, self.sampling_rate)

        ax.semilogy(freqs_normal, psd_normal, 'b-', label='正常', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_beginner, psd_beginner, 'g-', label='初學者', alpha=0.7, linewidth=2)
        ax.semilogy(freqs_advanced, psd_advanced, 'r-', label='資深', alpha=0.7, linewidth=2)

        ax.set_xlabel('頻率 (Hz)', fontsize=11)
        ax.set_ylabel('功率譜密度', fontsize=11)
        ax.set_title('頻譜分析\n不同狀態的腦波頻率分佈',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 50)

        # 標註頻段
        ax.axvspan(0.5, 4, alpha=0.1, color='purple', label='Delta')
        ax.axvspan(4, 8, alpha=0.1, color='blue', label='Theta')
        ax.axvspan(8, 12, alpha=0.1, color='green', label='Alpha')
        ax.axvspan(13, 30, alpha=0.1, color='orange', label='Beta')
        ax.axvspan(30, 50, alpha=0.1, color='red', label='Gamma')

        # === 說明 ===
        ax = axes[2, 1]
        ax.axis('off')

        text = '''
        【腦波與冥想狀態】

        腦波類型（頻率）：
        • Delta (0.5-4 Hz)：深度睡眠
        • Theta (4-8 Hz)：淺睡、深度冥想
        • Alpha (8-12 Hz)：放鬆、輕度冥想
        • Beta (13-30 Hz)：正常清醒、思考
        • Gamma (25-100 Hz)：高度專注、意識整合

        冥想的腦波變化：
        1. 初學者：
           → Beta↓（思慮減少）
           → Alpha↑（放鬆增加）

        2. 中級：
           → Theta增加（深度放鬆）
           → 可能進入「禪定」狀態

        3. 資深（10,000+小時）：
           → Gamma顯著增強（增幅超過對照組30倍！）
           → 不同腦區高度同步
           → 意識整合度極高

        Orch OR理論的預測：
        • Gamma波40Hz ≈ 量子坍縮頻率
        • 資深冥想者的Gamma波增強
          可能反映微管的量子過程

        關鍵發現（Lutz, Davidson 等人 2004）：
        • 冥想時 Gamma 活動大幅增加
        • 冥想前的靜息基線就高於對照組
        • 作者推測可能有長短期神經變化
        '''

        ax.text(0.05, 0.5, text, fontsize=10, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='lightyellow',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('brainwave_meditation_states.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【腦波與冥想：神經科學的證據】")
        print("="*70)

        print("\n腦波的五種類型：")
        print("  1. Delta (0.5-4 Hz)：深度睡眠")
        print("  2. Theta (4-8 Hz)：淺睡、深度冥想、創造力")
        print("  3. Alpha (8-12 Hz)：放鬆但清醒、輕度冥想")
        print("  4. Beta (13-30 Hz)：正常清醒、思考、專注")
        print("  5. Gamma (25-100 Hz)：高度專注、意識整合")

        print("\n冥想的腦波變化：")
        print("  初學者（幾週經驗）：")
        print("    • Beta波降低 → 思慮減少")
        print("    • Alpha波增強 → 放鬆增加")

        print("\n  中級（幾個月-幾年）：")
        print("    • Theta波增加 → 深度放鬆")
        print("    • 可能進入「禪定」狀態")

        print("\n  資深（10,000+小時）：")
        print("    • Gamma波顯著增強（增幅超過對照組30倍！）")
        print("    • 不同腦區高度同步")
        print("    • 意識整合度極高")

        print("\nDavidson實驗（2004）：")
        print("  • 8位藏傳佛教僧侶")
        print("  • 累積冥想經驗：10,000-50,000小時")
        print("  • 結果：冥想時 Gamma 活動增幅超過對照組 30 倍")

        print("\nOrch OR理論的預測：")
        print("  • 量子坍縮頻率 ≈ 40 Hz")
        print("  • Gamma波頻率 ≈ 40 Hz")
        print("  • 可能的聯繫？")

        print("\n可能的解釋：")
        print("  • Gamma波反映微管的量子坍縮")
        print("  • 冥想增強微管之間的同步")
        print("  • 產生更強、更同步的Gamma波")

        print("\n注意：")
        print("  • 這只是推測！")
        print("  • 沒有直接證據證明微管在冥想中有量子過程")
        print("  • 但相關性令人驚訝")
        print("="*70)

# 執行
brainwave_sim = BrainwaveSimulator()
brainwave_sim.visualize_meditation_states()

class NeuroplasticitySimulator:
    """
    神經可塑性模擬器
    展示：長期冥想如何改變大腦結構
    """

    def __init__(self):
        pass

    def visualize_brain_changes(self):
        """
        視覺化冥想導致的大腦變化
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        # === 灰質密度變化 ===
        ax = axes[0, 0]

        brain_regions = ['海馬迴\n(記憶)', '前額葉\n(專注)', '島葉\n(同理心)',
                        '杏仁核\n(恐懼)']
        control_group = [100, 100, 100, 100]
        meditators = [115, 120, 118, 85]  # 相對值

        x = np.arange(len(brain_regions))
        width = 0.35

        bars1 = ax.bar(x - width/2, control_group, width, label='對照組',
                      color='lightblue', edgecolor='black', linewidth=1.5)
        bars2 = ax.bar(x + width/2, meditators, width, label='冥想者',
                      color='lightgreen', edgecolor='black', linewidth=1.5)

        ax.set_ylabel('相對灰質密度 (%)', fontsize=11)
        ax.set_title('灰質密度變化\n長期冥想者 vs 對照組',
                    fontsize=13, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(brain_regions, fontsize=10)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # 標註變化
        for i, (c, m) in enumerate(zip(control_group, meditators)):
            change = m - c
            color = 'green' if change > 0 else 'red'
            ax.text(i, max(c, m) + 3, f'{change:+d}%', ha='center',
                   fontsize=10, fontweight='bold', color=color)

        # === 冥想時間與灰質密度關係 ===
        ax = axes[0, 1]

        hours = np.array([0, 1000, 5000, 10000, 20000, 40000])
        hippocampus = 100 + 20 * (1 - np.exp(-hours/15000))
        prefrontal = 100 + 25 * (1 - np.exp(-hours/12000))

        ax.plot(hours/1000, hippocampus, 'o-', linewidth=3, markersize=8,
               label='海馬迴', color='blue')
        ax.plot(hours/1000, prefrontal, 's-', linewidth=3, markersize=8,
               label='前額葉', color='green')

        ax.set_xlabel('冥想時數 (千小時)', fontsize=11)
        ax.set_ylabel('相對灰質密度 (%)', fontsize=11)
        ax.set_title('劑量-反應關係\n冥想時間越長，效果越明顯',
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # === 默認模式網絡（DMN）活動 ===
        ax = axes[0, 2]

        states = ['休息\n(正常)', '休息\n(冥想者)', '任務\n(正常)', '任務\n(冥想者)']
        dmn_activity = [100, 70, 40, 30]
        colors = ['lightcoral', 'lightgreen', 'lightblue', 'lightgreen']

        bars = ax.bar(states, dmn_activity, color=colors, edgecolor='black',
                     linewidth=1.5)
        ax.set_ylabel('DMN活動 (%)', fontsize=11)
        ax.set_title('默認模式網絡（DMN）\n冥想者的自我中心思維減少',
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # 標註
        for bar, activity in zip(bars, dmn_activity):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 3,
                   f'{activity}%', ha='center', fontsize=10, fontweight='bold')

        # === 大腦結構變化示意圖 ===
        ax = axes[1, 0]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # 簡化的大腦輪廓
        from matplotlib.patches import Ellipse, FancyBboxPatch

        # 大腦輪廓
        brain = Ellipse((0.5, 0.5), 0.6, 0.7, angle=0,
                       facecolor='lightgray', alpha=0.3,
                       edgecolor='black', linewidth=2)
        ax.add_patch(brain)

        # 標註增加的區域（綠色）
        regions_increase = [
            (0.35, 0.7, '前額葉\n+20%', 'lightgreen'),
            (0.5, 0.3, '海馬迴\n+15%', 'lightgreen'),
            (0.65, 0.5, '島葉\n+18%', 'lightgreen'),
        ]

        for x, y, label, color in regions_increase:
            circle = plt.Circle((x, y), 0.08, color=color, alpha=0.7,
                               edgecolor='darkgreen', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y-0.12, label, ha='center', fontsize=9,
                   fontweight='bold')

        # 標註減少的區域（紅色）
        circle_amygdala = plt.Circle((0.5, 0.6), 0.06, color='lightcoral',
                                    alpha=0.7, edgecolor='darkred', linewidth=2)
        ax.add_patch(circle_amygdala)
        ax.text(0.5, 0.52, '杏仁核\n-15%', ha='center', fontsize=9,
               fontweight='bold')

        ax.set_title('大腦結構變化示意\n長期冥想的神經可塑性',
                    fontsize=13, fontweight='bold')

        # === 白質連接增強 ===
        ax = axes[1, 1]
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # 左：對照組（連接少）
        ax.text(0.25, 0.95, '對照組', ha='center', fontsize=12,
               fontweight='bold')

        n_nodes = 6
        angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
        nodes_x = 0.25 + 0.15 * np.cos(angles)
        nodes_y = 0.5 + 0.15 * np.sin(angles)

        # 稀疏連接
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.3:  # 30% 連接
                    ax.plot([nodes_x[i], nodes_x[j]], [nodes_y[i], nodes_y[j]],
                           'gray', alpha=0.3, linewidth=1)

        # 節點
        ax.scatter(nodes_x, nodes_y, s=200, c='lightblue',
                  edgecolors='blue', linewidths=2, zorder=5)

        # 右：冥想者（連接多）
        ax.text(0.75, 0.95, '冥想者', ha='center', fontsize=12,
               fontweight='bold')

        nodes_x2 = 0.75 + 0.15 * np.cos(angles)
        nodes_y2 = 0.5 + 0.15 * np.sin(angles)

        # 密集連接
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if np.random.random() < 0.8:  # 80% 連接
                    ax.plot([nodes_x2[i], nodes_x2[j]], [nodes_y2[i], nodes_y2[j]],
                           'green', alpha=0.5, linewidth=2)

        # 節點
        ax.scatter(nodes_x2, nodes_y2, s=200, c='lightgreen',
                  edgecolors='darkgreen', linewidths=2, zorder=5)

        ax.set_title('白質連接\n冥想者的腦區連接更緊密',
                    fontsize=13, fontweight='bold')

        # === 總結說明 ===
        ax = axes[1, 2]
        ax.axis('off')

        text_summary = '''
        【神經可塑性：冥想改變大腦】

        灰質密度變化：
        + 海馬迴：+15%（記憶、學習）
        + 前額葉：+20%（決策、專注）
        + 島葉：+18%（同理心）
        - 杏仁核：-15%（恐懼、壓力）

        白質連接：
        • 不同腦區連接增強
        • 資訊傳遞更高效
        • 大腦網絡更整合

        默認模式網絡（DMN）：
        • 自我中心思維減少
        • 心遊走（mind-wandering）減少
        • 當下覺知增強

        時間效應：
        • 效果隨冥想時數增加
        • 10,000+小時：顯著改變
        • 但初學者（幾週）也有效果

        關鍵發現：
        「修行」不只是心理技巧
        而是有生物學基礎的
        大腦結構也可能有差異

        這是可以測量的
        神經可塑性線索
        '''

        ax.text(0.05, 0.5, text_summary, fontsize=9, va='center',
               family='monospace',
               bbox=dict(boxstyle='round', facecolor='white',
                        alpha=0.9, edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('neuroplasticity_meditation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【神經可塑性：冥想如何改變大腦】")
        print("="*70)

        print("\n灰質密度變化（長期冥想者 vs 對照組）：")
        print("  增加的區域：")
        print("    • 海馬迴：+15%（記憶、學習）")
        print("    • 前額葉皮層：+20%（決策、專注、自控）")
        print("    • 島葉：+18%（內感受、同理心）")
        print("  減少的區域：")
        print("    • 杏仁核：-15%（恐懼、壓力反應）")

        print("\n白質連接：")
        print("  • 不同腦區之間的連接增強")
        print("  • 資訊傳遞更高效")
        print("  • 大腦網絡更整合")

        print("\n默認模式網絡（DMN）：")
        print("  • DMN：大腦「不做事」時的活動")
        print("  • 與自我意識、心遊走相關")
        print("  • 冥想者的DMN活動減少30%")
        print("  → 更少的自我中心思維")
        print("  → 更多的當下覺知")

        print("\n時間效應（劑量-反應）：")
        print("  • 效果隨冥想時數增加")
        print("  • 10,000小時：顯著改變")
        print("  • 8週課程的結果不一：Kral 等人（2022）未發現結構變化")

        print("\n重要研究：")
        print("  • Davidson et al. (2004)：資深冥想者")
        print("  • Lazar et al. (2005)：皮質厚度")
        print("  • Holzel et al. (2011)：8週正念課程")

        print("\n神經可塑性（Neuroplasticity）：")
        print("  • 大腦可以根據經驗改變結構")
        print("  • 結構差異仍有爭議，因果尚無定論")
        print("  • 「修行」有生物學基礎")

        print("\n哲學意義：")
        print("  • 東方修行傳統說：「修行改變心性」")
        print("  • 現代神經科學正在研究：")
        print("    修行是否改變大腦（心的物質基礎）")
        print("  • 理論與實踐的統一")
        print("="*70)

# 執行
neuro_sim = NeuroplasticitySimulator()
neuro_sim.visualize_brain_changes()

def visualize_vipassana_measurement():
    """
    視覺化內觀冥想與量子測量的類比
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === 量子：測量前（疊加態）===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 多個可能性
    possibilities = ['|0>', '|1>', '|2>', '|3>']
    positions = [(0.3, 0.7), (0.7, 0.7), (0.3, 0.3), (0.7, 0.3)]

    for poss, pos in zip(possibilities, positions):
        circle = plt.Circle(pos, 0.08, color='purple', alpha=0.3,
                           edgecolor='purple', linewidth=2)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], poss, ha='center', va='center',
               fontsize=11, fontweight='bold')

    # 連線（糾纏）
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]],
                   'purple', alpha=0.2, linewidth=1.5)

    ax.text(0.5, 0.9, '測量前：疊加態', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, '|psi> = Sum(alpha_i|i>)\n所有可能同時存在',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

    # === 量子：測量（坍縮）===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 測量
    ax.text(0.5, 0.80, '[ 測量 ]', ha='center', fontsize=16, fontweight='bold')

    # 箭頭
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='red'))

    # 結果
    circle = plt.Circle((0.5, 0.3), 0.12, color='green', alpha=0.7,
                       edgecolor='darkgreen', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, '|2>', ha='center', va='center',
           fontsize=14, fontweight='bold', color='white')

    ax.text(0.5, 0.1, '測量後：確定態\n波函數坍縮',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # === 內觀：觀察前（念頭混沌）===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 混亂的念頭
    thoughts = ['怒', '喜', '悲', '懼', '愛', '恨', '欲', '貪']
    np.random.seed(42)
    for thought in thoughts:
        x, y = np.random.random(2) * 0.6 + 0.2
        ax.text(x, y, thought, fontsize=12, alpha=0.4,
               color=np.random.choice(['red', 'blue', 'green', 'purple']))

    # 中心：心不明
    circle = plt.Circle((0.5, 0.5), 0.12, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n混沌', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.9, '觀察前：念頭混沌', ha='center',
           fontsize=13, fontweight='bold')
    ax.text(0.5, 0.1, '念頭紛飛\n不清晰、不確定',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === 內觀：覺知（觀察）===
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 覺知
    ax.text(0.5, 0.80, '[ 覺知 ]', ha='center', fontsize=16, fontweight='bold',
           color='goldenrod')

    # 箭頭
    ax.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.65),
               arrowprops=dict(arrowstyle='->', lw=5, color='gold'))

    # 被照見的念頭
    circle = plt.Circle((0.5, 0.3), 0.12, color='yellow', alpha=0.7,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.3, '怒', ha='center', va='center',
           fontsize=16, fontweight='bold')

    # 消失
    ax.text(0.7, 0.3, '-> 消失', ha='left', fontsize=10,
           color='gray', style='italic')

    ax.text(0.5, 0.1, '覺知時：念頭被照見\n失去力量，消失',
           ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 總標題
    fig.text(0.5, 0.98, '內觀冥想 vs 量子測量',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('vipassana_measurement_analogy.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【內觀冥想與量子測量的深刻類比】")
    print("="*70)

    print("\n量子測量：")
    print("  測量前：系統處於疊加態")
    print("    -> |psi> = Sum(alpha_i|i>)")
    print("    -> 所有可能同時存在")

    print("\n  測量時：觀察者介入")
    print("    -> 波函數坍縮")

    print("\n  測量後：系統處於確定態")
    print("    -> |psi> -> |i>")
    print("    -> 確定一個結果")

    print("\n內觀冥想（Vipassana）：")
    print("  觀察前：念頭混沌")
    print("    -> 怒、喜、悲、懼...紛飛")
    print("    -> 不清晰、不確定")

    print("\n  觀察時：覺知生起")
    print("    -> 「看著」念頭")
    print("    -> 不追逐，不壓抑")

    print("\n  觀察後：念頭被照見")
    print("    -> 念頭失去力量")
    print("    -> 自然消失")

    print("\n共同結構：")
    print("  1. 「觀察」是核心動作")
    print("  2. 觀察前：不確定、混沌")
    print("  3. 觀察時：介入、照見")
    print("  4. 觀察後：確定或消失")

    print("\n對應：")
    print("  疊加態 ~ 念頭混沌")
    print("  測量 ~ 覺知")
    print("  坍縮 ~ 念頭顯現/消失")
    print("  觀察者 ~ 覺知本身")

    print("\n關鍵洞見：")
    print("  • 「觀察」改變「被觀察者」")
    print("  • 這在量子力學是物理定律")
    print("  • 這在內觀是心理經驗")
    print("  • 結構驚人相似")

    print("\n但要注意：")
    print("  • 這是類比，不是等同")
    print("  • 心理過程 != 量子過程")
    print("  • 但結構對應值得深思")
    print("="*70)

# 執行
visualize_vipassana_measurement()

def visualize_no_mind_superposition():
    """
    視覺化無念狀態與疊加態的對應
    """

    fig = plt.figure(figsize=(18, 10))

    # === 左上：有念（確定態）===
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # 一個念頭（執著）
    circle = plt.Circle((0.5, 0.5), 0.2, color='red', alpha=0.7,
                       edgecolor='darkred', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0.5, 0.5, '愛', ha='center', va='center',
            fontsize=24, fontweight='bold', color='white')

    # 箭頭指向（執著）
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax1.annotate('', xy=(0.5, 0.5), xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red'))

    ax1.set_title('有念：執著一個念頭\n「愛」-> 產生「恨」的對立',
                 fontsize=13, fontweight='bold')

    # === 右上：無念（疊加態）===
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # 多個念頭同時（但不執著）
    emotions = ['喜', '怒', '哀', '樂', '愛', '恨']
    angles = np.linspace(0, 2*np.pi, len(emotions), endpoint=False)

    for emotion, angle in zip(emotions, angles):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        circle = plt.Circle((x, y), 0.08, color='lightblue', alpha=0.5,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, emotion, ha='center', va='center',
                fontsize=11)

    # 中心：空
    circle_center = plt.Circle((0.5, 0.5), 0.12, color='gold', alpha=0.7,
                              edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_center)
    ax2.text(0.5, 0.5, '無念', ha='center', va='center',
            fontsize=12, fontweight='bold')

    ax2.set_title('無念：念頭不住\n超越對立，保持開放',
                 fontsize=13, fontweight='bold')

    # === 左下：量子確定態（|0>）===
    ax3 = fig.add_subplot(2, 2, 3)

    states = ['|0>', '|1>']
    probs = [1.0, 0.0]

    bars = ax3.bar(states, probs, color=['blue', 'lightgray'],
                  edgecolor='black', linewidth=2, alpha=0.7)
    ax3.set_ylabel('機率', fontsize=11)
    ax3.set_title('量子確定態\n|0>：完全確定',
                 fontsize=13, fontweight='bold')
    ax3.set_ylim(0, 1.2)
    ax3.grid(True, alpha=0.3, axis='y')

    # === 右下：量子疊加態 ===
    ax4 = fig.add_subplot(2, 2, 4)

    n_states = 4
    states2 = [f'|{i}>' for i in range(n_states)]
    probs2 = [0.5, 0.3, 0.15, 0.05]

    bars2 = ax4.bar(states2, probs2, color='purple',
                   edgecolor='black', linewidth=2, alpha=0.6)
    ax4.set_ylabel('振幅平方（機率）', fontsize=11)
    ax4.set_title('量子疊加態\n|psi> = Sum(alpha_i|i>)：多種可能',
                 fontsize=13, fontweight='bold')
    ax4.set_ylim(0, 0.6)
    ax4.grid(True, alpha=0.3, axis='y')

    # 總標題
    fig.text(0.5, 0.98, '無念 vs 疊加態：開放性與潛能',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.05)
    plt.savefig('no_mind_superposition.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【無念與疊加態：開放性與潛能】")
    print("="*70)

    print("\n有念（確定態）：")
    print("  • 執著於一個念頭")
    print("  • 例如：執著於「愛」")
    print("  • 就產生「愛/恨」的對立")
    print("  • 失去開放性")
    print("  • 像量子確定態|0>")

    print("\n無念（疊加態）：")
    print("  • 念頭來去不住")
    print("  • 不執著任何念頭")
    print("  • 超越對立")
    print("  • 保持開放性")
    print("  • 像量子疊加態Sum(alpha_i|i>)")

    print("\n六祖慧能的教導：")
    print("  「何期自性，本自清淨。」")
    print("  -> 本來面目是「無念」（清淨）")

    print("\n  「念念不住」")
    print("  -> 不執著於任何念頭")
    print("  -> 保持「無念」狀態")

    print("\n量子計算的挑戰：")
    print("  • 保持疊加態不坍縮")
    print("  • 避免退相干")
    print("  • 延長相干時間")

    print("\n禪修的挑戰：")
    print("  • 保持無念不起念")
    print("  • 避免執著")
    print("  • 延長「清明」時間")

    print("\n對應：")
    print("  疊加態 ~ 無念")
    print("  確定態 ~ 有念（執著）")
    print("  測量/環境 ~ 起念/境界")
    print("  退相干 ~ 失念")

    print("\n共同洞見：")
    print("  • 「無念/疊加態」不是「空無」")
    print("  • 而是更基礎、更豐富的狀態")
    print("  • 有無限潛能")
    print("  • 超越固定的二元對立")

    print("\n最終洞見：")
    print("  「無念」和「疊加態」都指向：")
    print("  一種超越固定、充滿潛能的")
    print("  開放狀態")
    print("="*70)

# 執行
visualize_no_mind_superposition()
