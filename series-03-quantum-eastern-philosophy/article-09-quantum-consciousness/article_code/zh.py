# Code & Cogito: 量子意識 vs 東方心學——心靈是量子過程嗎？
# Article: https://code-cogito.com/quantum-consciousness-eastern-philosophy/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class QuantumConsciousnessSimulator:
    """
    量子意識模擬器
    展示：測量/觀察如何影響量子系統
    """

    def __init__(self):
        pass

    def visualize_measurement_consciousness(self):
        """
        視覺化測量與意識的關係
        """
        fig = plt.figure(figsize=(18, 12))

        # === 圖1：測量前（疊加態）===
        ax1 = fig.add_subplot(2, 3, 1, projection='3d')

        # 生成疊加態的Bloch球表示
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax1.plot_surface(x, y, z, alpha=0.3, color='cyan')

        # 疊加態向量
        theta, phi = np.pi/4, np.pi/4
        sx = np.sin(theta) * np.cos(phi)
        sy = np.sin(theta) * np.sin(phi)
        sz = np.cos(theta)

        ax1.quiver(0, 0, 0, sx, sy, sz, color='purple',
                  arrow_length_ratio=0.1, linewidth=3)

        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('測量前：疊加態\n|ψ⟩ = α|0⟩ + β|1⟩',
                     fontsize=13, fontweight='bold')

        # === 圖2：測量時（觀察者介入）===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # 眼睛（觀察者）
        eye = plt.Circle((0.5, 0.7), 0.15, color='blue', alpha=0.6,
                        edgecolor='darkblue', linewidth=3)
        ax2.add_patch(eye)
        ax2.text(0.5, 0.7, '👁', ha='center', va='center', fontsize=40)

        # 箭頭向下
        ax2.annotate('', xy=(0.5, 0.4), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=5, color='red'))
        ax2.text(0.6, 0.475, '觀察\n測量', ha='left', fontsize=12,
                color='red', fontweight='bold')

        # 量子系統
        rect = plt.Rectangle((0.35, 0.25), 0.3, 0.15,
                            facecolor='purple', alpha=0.5,
                            edgecolor='purple', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(0.5, 0.325, '量子系統', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        ax2.set_title('測量時：觀察者介入\n波函數即將坍縮',
                     fontsize=13, fontweight='bold')

        # === 圖3：測量後（坍縮）===
        ax3 = fig.add_subplot(2, 3, 3, projection='3d')

        # Bloch球
        ax3.plot_surface(x, y, z, alpha=0.3, color='lightblue')

        # 坍縮到|0⟩（北極）
        ax3.quiver(0, 0, 0, 0, 0, 1, color='red',
                  arrow_length_ratio=0.1, linewidth=3)

        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('Z')
        ax3.set_title('測量後：坍縮\n|ψ⟩ → |0⟩',
                     fontsize=13, fontweight='bold')

# |         # === 圖4：經典觀點 ===
# |         ax4 = fig.add_subplot(2, 3, 4)
# |         ax4.axis('off')
# | 
# |         text_classical = '''
# |         經典觀點（唯物論）：
# | 
# |         • 物質獨立於觀察者
# |         • 觀察只是「發現」
# |         • 意識是副產品
# |         • 大腦是經典計算機
# | 
# |         問題：
# |         → 無法解釋測量問題
# |         → 無法解釋意識的統一性
# |         '''
# | 
# |         ax4.text(0.1, 0.5, text_classical, fontsize=10, va='center',
# |                 bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
# | 
# |         # === 圖5：量子意識觀點 ===
# |         ax5 = fig.add_subplot(2, 3, 5)
# |         ax5.axis('off')
# | 
# |         text_quantum = '''
# |         量子意識（Orch OR）：
# | 
# |         • 意識是量子過程
# |         • 發生在微管中
# |         • 意識導致波函數坍縮
# |         • 每次坍縮 = 意識瞬間
# | 
# |         優點：
# |         → 解釋意識的統一性
# |         → 解釋意識的非計算性
# |         → 連結量子力學與意識
# |         '''
# | 
# |         ax5.text(0.1, 0.5, text_quantum, fontsize=10, va='center',
# |                 bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.8))
# | 
# |         # === 圖6：東方心學觀點 ===
# |         ax6 = fig.add_subplot(2, 3, 6)
# |         ax6.axis('off')
# | 
# |         text_eastern = '''
# |         東方心學/禪宗：
# | 
# |         • 心是萬法根源
# |         • 離開心，無法談物
# |         • 心不是大腦
# |         • 心是本體
# | 
# |         王陽明：
# |         「心外無物，心外無理」
# | 
# |         禪宗：
# |         「直指人心，見性成佛」
# | 
# |         共同點：
# |         → 心/意識有本體地位
# |         → 觀察創造實在
# |         '''
# | 
# |         ax6.text(0.1, 0.5, text_eastern, fontsize=10, va='center',
# |                 bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
# | 
# |         # 總標題
# |         fig.text(0.5, 0.98, '量子測量與意識：三種觀點',
# |                 ha='center', fontsize=16, fontweight='bold')
# | 
# |         plt.tight_layout()
# |         plt.subplots_adjust(top=0.93)
# |         plt.savefig('quantum_measurement_consciousness.png',
# |                    dpi=300, bbox_inches='tight')
# |         plt.show()

        print("\n" + "="*70)
        print("【量子測量與意識】")
        print("="*70)

        print("\n測量問題：")
        print("  • 測量前：系統處於疊加態")
        print("  • 測量時：波函數坍縮")
        print("  • 測量後：系統處於確定態")
        print("  • 問題：什麼導致坍縮？")

        print("\n三種回答：")
        print("\n1. 哥本哈根詮釋（標準）：")
        print("   → 測量儀器導致坍縮")
        print("   → 但測量儀器也是量子系統")
        print("   → 無限後退問題")

        print("\n2. 多世界詮釋：")
        print("   → 沒有坍縮，宇宙分裂")
        print("   → 意識不特殊")

        print("\n3. 馮·諾伊曼/Orch OR：")
        print("   → 意識導致坍縮")
        print("   → 意識有特殊地位")

        print("\n東方哲學的相關觀點：")
        print("  王陽明：「心外無物」")
        print("  → 離開心，無法定義物")

        print("\n  禪宗：「明心見性」")
        print("  → 直接體悟心的本質")

        print("\n共同點：")
        print("  • 觀察者/心有核心角色")
        print("  • 「客觀實在」依賴主體")
        print("  • 心/意識不是副產品")

        print("\n關鍵問題：")
        print("  • 意識真的導致坍縮嗎？")
        print("  • 如果是，機制是什麼？")
        print("  • Orch OR理論是對的嗎？")
        print("  • 還是需要新的物理學？")
        print("="*70)

# 執行
simulator = QuantumConsciousnessSimulator()
simulator.visualize_measurement_consciousness()

# | class OrchORSimulator:
# |     """
# |     Orch OR理論模擬
# |     展示：微管如何可能產生意識
# |     """
# | 
# |     def __init__(self):
# |         self.hbar = 1.054571817e-34  # 約化普朗克常數 (J·s)
# |         self.c = 299792458  # 光速 (m/s)
# | 
# |     def calculate_collapse_time(self, delta_mass):
# |         """
# |         計算客觀坍縮時間
# |         τ = ℏ / (ΔM · c²)
# |         """
# |         delta_energy = delta_mass * self.c**2
# |         tau = self.hbar / delta_energy
# |         return tau
# | 
# |     def visualize_orch_or(self):
# |         """
# |         視覺化Orch OR理論
# |         """
# |         fig = plt.figure(figsize=(18, 10))

        # === 圖1：微管結構 ===
        ax1 = fig.add_subplot(2, 3, 1)
        ax1.axis('off')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        # 微管（圓柱形）
        from matplotlib.patches import Rectangle, Circle

        # 繪製簡化的微管
        for i in range(5):
            y = 0.2 + i * 0.15
            # 微管蛋白
            circle1 = Circle((0.3, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle2 = Circle((0.5, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            circle3 = Circle((0.7, y), 0.04, color='lightblue',
                           edgecolor='blue', linewidth=1.5)
            ax1.add_patch(circle1)
            ax1.add_patch(circle2)
            ax1.add_patch(circle3)

        # 連線
        for i in range(4):
            y = 0.2 + i * 0.15
            ax1.plot([0.3, 0.3], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.5, 0.5], [y+0.04, y+0.11], 'b-', alpha=0.5)
            ax1.plot([0.7, 0.7], [y+0.04, y+0.11], 'b-', alpha=0.5)

        ax1.set_title('微管結構\n微管蛋白排列', fontsize=13, fontweight='bold')

        ax1.text(0.5, 0.05, '直徑：~25 nm\n長度：數微米',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))

        # === 圖2：量子疊加 ===
        ax2 = fig.add_subplot(2, 3, 2)
        ax2.axis('off')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # 微管蛋白的兩個狀態
        circle_left = Circle((0.3, 0.5), 0.1, color='red', alpha=0.5,
                            edgecolor='darkred', linewidth=2)
        circle_right = Circle((0.7, 0.5), 0.1, color='blue', alpha=0.5,
                             edgecolor='darkblue', linewidth=2)
        ax2.add_patch(circle_left)
        ax2.add_patch(circle_right)

        ax2.text(0.3, 0.5, '狀態|0⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')
        ax2.text(0.7, 0.5, '狀態|1⟩', ha='center', va='center',
                fontsize=10, fontweight='bold')

        # 雙向箭頭
        ax2.annotate('', xy=(0.68, 0.5), xytext=(0.32, 0.5),
                    arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
        ax2.text(0.5, 0.55, '+', ha='center', fontsize=16, fontweight='bold')

        ax2.text(0.5, 0.7, '疊加態：α|0⟩ + β|1⟩', ha='center',
                fontsize=11, fontweight='bold', color='purple')

        ax2.set_title('微管蛋白的量子疊加', fontsize=13, fontweight='bold')

        # === 圖3：客觀坍縮 ===
        ax3 = fig.add_subplot(2, 3, 3)

        # 時間軸
        t = np.linspace(0, 0.03, 100)

        # 疊加態的「大小」（能量/質量差）
        mass_diff = 1e-8 * (1 - np.exp(-t/0.01))  # kg

        ax3.plot(t * 1000, mass_diff * 1e8, 'b-', linewidth=3)
        ax3.axhline(1e-8 * 1e8, color='red', linestyle='--', linewidth=2,
                   label='坍縮閾值')

        # 標註坍縮點
        collapse_idx = np.where(mass_diff >= 1e-8 * 0.99)[0][0]
        ax3.scatter([t[collapse_idx] * 1000], [mass_diff[collapse_idx] * 1e8],
                   c='red', s=200, zorder=5, edgecolors='black', linewidth=2)
        ax3.text(t[collapse_idx] * 1000, mass_diff[collapse_idx] * 1e8 + 0.05,
                '坍縮！', ha='center', fontsize=11, fontweight='bold',
                color='red')

        ax3.set_xlabel('時間 (毫秒)', fontsize=12)
        ax3.set_ylabel('質量差 (×10⁻⁸ kg)', fontsize=12)
        ax3.set_title('客觀坍縮過程\n疊加態累積到閾值',
                     fontsize=13, fontweight='bold')
        ax3.legend(fontsize=10)
        ax3.grid(True, alpha=0.3)

        # === 圖4：坍縮時間計算 ===
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.axis('off')

        # 計算不同質量差的坍縮時間
        masses = np.logspace(-12, -6, 100)  # kg
        times = [self.calculate_collapse_time(m) * 1000 for m in masses]  # ms

        ax4_plot = fig.add_axes([0.1, 0.1, 0.25, 0.35])
        ax4_plot.loglog(masses, times, 'g-', linewidth=3)
        ax4_plot.set_xlabel('質量差 (kg)', fontsize=11)
        ax4_plot.set_ylabel('坍縮時間 (ms)', fontsize=11)
        ax4_plot.set_title('彭羅斯公式：τ = ℏ/(ΔM·c²)',
                          fontsize=12, fontweight='bold')
        ax4_plot.grid(True, alpha=0.3)

        # 標註大腦的參數
        brain_mass = 1e-8
        brain_time = self.calculate_collapse_time(brain_mass) * 1000
        ax4_plot.scatter([brain_mass], [brain_time], c='red', s=100,
                        zorder=5, edgecolors='black', linewidth=2)
        ax4_plot.text(brain_mass * 3, brain_time,
                     f'大腦\n~{brain_time:.1f} ms',
                     fontsize=9, color='red', fontweight='bold')

        # === 圖5：意識的時間線 ===
        ax5 = fig.add_subplot(2, 3, 5)

        # 模擬意識「更新」
        n_updates = 10
        update_times = np.linspace(0, 0.25, n_updates)

        for i, t_update in enumerate(update_times):
            ax5.scatter([t_update * 1000], [1], c='purple', s=300,
                       alpha=0.7, edgecolors='black', linewidth=2)
            ax5.text(t_update * 1000, 1.1, f'{i+1}', ha='center',
                    fontsize=9, fontweight='bold')

        ax5.plot([0, 250], [1, 1], 'gray', linestyle='--', alpha=0.3)
        ax5.set_xlabel('時間 (毫秒)', fontsize=12)
        ax5.set_title('意識的「量子更新」\n每次坍縮 = 一個意識瞬間',
                     fontsize=13, fontweight='bold')
        ax5.set_ylim(0.5, 1.5)
        ax5.set_yticks([])
        ax5.grid(True, alpha=0.3, axis='x')

        # 標註頻率
        ax5.text(125, 0.7, f'頻率：~40 Hz\n(與腦波一致)',
                ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # === 圖6：Orch OR總結 ===
        ax6 = fig.add_subplot(2, 3, 6)
        ax6.axis('off')

        text_summary = '''
        Orch OR理論總結：

        1. 微管蛋白處於量子疊加態
           |ψ⟩ = α|0⟩ + β|1⟩

        2. 疊加態持續時間：
           τ = ℏ / (ΔM · c²)

        3. 當ΔM足夠大：
           時空曲率顯著
           → 自發坍縮（客觀約化）

        4. 每次坍縮 = 意識瞬間
           坍縮頻率 ~40 Hz

        5. 大腦編排這些坍縮
           → 統一的意識體驗

        關鍵預測：
        • 麻醉藥影響微管量子態
        • 意識依賴量子相干性
        • 意識是非算法的

        爭議：
        • 大腦溫度太高？
        • 退相干太快？
        • 客觀坍縮存在？
        '''

        ax6.text(0.1, 0.5, text_summary, fontsize=9, va='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                         edgecolor='black', linewidth=2))

        plt.tight_layout()
        plt.savefig('orch_or_simulation.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*70)
        print("【Orch OR理論：量子意識假說】")
        print("="*70)

        print("\n彭羅斯-哈梅羅夫（1996）：")
        print("  • Orchestrated Objective Reduction")
        print("  • 編排的客觀約化")

        print("\n核心機制：")
        print("  1. 微管蛋白處於量子疊加態")
        print("  2. 疊加態持續一段時間")
        print("  3. 當質量差ΔM足夠大時")
        print("  4. 時空曲率變得顯著")
        print("  5. 自發坍縮（客觀約化）")
        print("  6. 這個坍縮 = 一個意識瞬間")

        print("\n彭羅斯公式：")
        print(f"  τ = ℏ / (ΔM · c²)")
        print(f"  ℏ = {self.hbar:.3e} J·s")
        print(f"  c = {self.c:.0f} m/s")

        print("\n大腦的參數（估計）：")
        brain_mass = 1e-8  # kg
        brain_tau = self.calculate_collapse_time(brain_mass)
        print(f"  ΔM ≈ {brain_mass:.0e} kg")
        print(f"  τ ≈ {brain_tau * 1000:.1f} ms")
        print(f"  頻率 ≈ {1/brain_tau:.0f} Hz")

        print("\n實驗證據（2014）：")
        print("  • 微管在生理溫度下有量子振動")
        print("  • 但這不能完全證明Orch OR")

        print("\n爭議：")
        print("  支持者：解釋意識的統一性和非計算性")
        print("  反對者：大腦太熱，退相干太快")

        print("\n彭羅斯（2020諾貝爾獎演講）：")
        print("  「我不知道意識是否是量子的。")
        print("   但如果要理解意識，我們需要新的物理學。」")
        print("="*70)

# 執行
orch_sim = OrchORSimulator()
orch_sim.visualize_orch_or()

def visualize_zen_enlightenment_collapse():
    """
    視覺化禪宗開悟與波函數坍縮的類比
    """

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # === 圖1：迷（測量前）===
    ax = axes[0, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '迷（測量前）', ha='center',
           fontsize=14, fontweight='bold')

    # 混亂的心（疊加態）
    np.random.seed(42)
    for _ in range(30):
        x, y = np.random.random(2)
        ax.text(x, y, '妄', fontsize=12, alpha=0.6,
               color=np.random.choice(['gray', 'darkgray']))

    # 中心：模糊的心
    circle = plt.Circle((0.5, 0.5), 0.15, color='gray', alpha=0.5,
                       edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n不明', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    ax.text(0.5, 0.15, '妄念紛飛\n如同疊加態', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # === 圖2：悟（測量時）===
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '悟（測量時）', ha='center',
           fontsize=14, fontweight='bold')

    # 閃光（頓悟）
    for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        ax.plot([0.5, x], [0.5, y], 'yellow', linewidth=3, alpha=0.8)

    # 中心：明亮的心
    circle = plt.Circle((0.5, 0.5), 0.15, color='gold', alpha=0.9,
                       edgecolor='orange', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '心\n見性', ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(0.5, 0.15, '瞬間開悟\n如同坍縮', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # === 圖3：悟後（測量後）===
    ax = axes[1, 0]
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.9, '悟後（測量後）', ha='center',
           fontsize=14, fontweight='bold')

    # 清明的心（確定態）
    circle = plt.Circle((0.5, 0.5), 0.2, color='lightblue', alpha=0.7,
                       edgecolor='blue', linewidth=3)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '本心\n清明', ha='center', va='center',
           fontsize=12, fontweight='bold', color='darkblue')

    # 周圍：清淨
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax.text(x, y, '淨', fontsize=10, alpha=0.6, color='blue')

    ax.text(0.5, 0.15, '心明性見\n如同確定態', ha='center',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === 圖4：對應總結 ===
    ax = axes[1, 1]
    ax.axis('off')

    comparison = '''
    【禪宗開悟 vs 波函數坍縮】

    禪宗：
    • 迷：妄念紛飛，心不明
    • 悟：瞬間頓悟，明心見性
    • 悟後：本心清明

    量子：
    • 測量前：疊加態，不確定
    • 測量時：波函數坍縮
    • 測量後：確定態

    相似點：
    ✓ 都是非連續的變化
    ✓ 都是瞬間的（量子跳躍）
    ✓ 都涉及「觀察」的角色
    ✓ 都從不確定→確定

    禪宗的「頓悟」：
    • 不是漸進的
    • 是突然的
    • 無法預測
    • 不可逆的

    波函數坍縮：
    • 不是連續的
    • 是瞬間的
    • 隨機的（機率）
    • 不可逆的

    深刻類比：
    「明心見性」= 意識導致坍縮？
    '''

    ax.text(0.1, 0.5, comparison, fontsize=10, va='center',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9,
                    edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig('zen_enlightenment_collapse.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【禪宗開悟與波函數坍縮的類比】")
    print("="*70)

    print("\n禪宗的「明心見性」：")
    print("  • 明心：明了自己的心")
    print("  • 見性：見到自己的本性（佛性）")
    print("  • 方法：坐禪、公案、棒喝")
    print("  • 結果：突然頓悟")

    print("\n六祖慧能的頓悟：")
    print("  聽到「應無所住而生其心」")
    print("  → 瞬間開悟")

    print("\n  偈語：")
    print("  「菩提本無樹，明鏡亦非台。")
    print("   本來無一物，何處惹塵埃？」")

    print("\n禪宗的「頓悟」特性：")
    print("  • 非連續：不是漸進的")
    print("  • 瞬間性：突然發生")
    print("  • 不可預測：不知何時發生")
    print("  • 不可逆：一旦開悟，不會退轉")

    print("\n波函數坍縮的特性：")
    print("  • 非連續：量子跳躍")
    print("  • 瞬間性：沒有過渡過程")
    print("  • 隨機性：只能預測機率")
    print("  • 不可逆：坍縮後無法恢復")

    print("\n類比的深度：")
    print("  迷（妄念） ≈ 疊加態（不確定）")
    print("  悟（頓悟） ≈ 坍縮（測量）")
    print("  悟後（清明） ≈ 確定態（結果）")

    print("\n問題：")
    print("  • 「明心見性」是意識導致坍縮嗎？")
    print("  • 「觀察自心」是一種「測量」嗎？")
    print("  • 禪宗的「心」是量子過程嗎？")

    print("\n可能的答案：")
    print("  • 禪宗和量子力學都指向：")
    print("    觀察/心的角色是核心的")
    print("  • 「頓悟」和「坍縮」都是")
    print("    從不確定到確定的瞬間轉變")
    print("  • 但禪宗的「心」可能超越")
    print("    物理學的「意識」")
    print("="*70)

# 執行
visualize_zen_enlightenment_collapse()

def visualize_mind_principle_observer():
    """
    視覺化王陽明「心即理」與觀察者效應
    """

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # === 圖1：經典觀點（心外有物）===
    ax1.axis('off')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    ax1.text(0.5, 0.95, '經典觀點：心外有物', ha='center',
            fontsize=14, fontweight='bold', transform=ax1.transAxes)

    # 物在外
    rect_matter = plt.Rectangle((0.6, 0.4), 0.25, 0.3,
                                facecolor='blue', alpha=0.6,
                                edgecolor='black', linewidth=2)
    ax1.add_patch(rect_matter)
    ax1.text(0.725, 0.55, '物\n(客觀)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # 心在內
    circle_mind = plt.Circle((0.25, 0.55), 0.1, color='red', alpha=0.6,
                            edgecolor='black', linewidth=2)
    ax1.add_patch(circle_mind)
    ax1.text(0.25, 0.55, '心\n(主觀)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # 箭頭：物→心（被動接受）
    ax1.annotate('', xy=(0.35, 0.55), xytext=(0.6, 0.55),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax1.text(0.475, 0.6, '感知', ha='center', fontsize=10)

    ax1.text(0.5, 0.15, '物獨立於心\n心被動接受', ha='center',
            fontsize=10, transform=ax1.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # === 圖2：王陽明「心即理」===
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    ax2.text(0.5, 0.95, '王陽明：心即理', ha='center',
            fontsize=14, fontweight='bold', transform=ax2.transAxes)

    # 心在中心
    circle_mind = plt.Circle((0.5, 0.55), 0.15, color='gold', alpha=0.7,
                            edgecolor='orange', linewidth=3)
    ax2.add_patch(circle_mind)
    ax2.text(0.5, 0.55, '心\n(本體)', ha='center', va='center',
            fontsize=12, fontweight='bold')

    # 物從心生
    manifestations = [
        (0.25, 0.75, '物1'),
        (0.75, 0.75, '物2'),
        (0.25, 0.35, '物3'),
        (0.75, 0.35, '物4'),
    ]

    for x, y, label in manifestations:
        circle = plt.Circle((x, y), 0.07, color='lightblue', alpha=0.6,
                           edgecolor='blue', linewidth=1.5)
        ax2.add_patch(circle)
        ax2.text(x, y, label, ha='center', va='center', fontsize=9)

        # 箭頭：心→物
        ax2.annotate('', xy=(x, y), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', lw=2, color='orange',
                                  alpha=0.6))

    ax2.text(0.5, 0.15, '心外無物\n物依心而顯', ha='center',
            fontsize=10, transform=ax2.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # === 圖3：量子觀察者效應 ===
    ax3.axis('off')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    ax3.text(0.5, 0.95, '量子力學：觀察者效應', ha='center',
            fontsize=14, fontweight='bold', transform=ax3.transAxes)

    # 觀察者
    circle_observer = plt.Circle((0.5, 0.75), 0.1, color='purple', alpha=0.7,
                                edgecolor='darkpurple', linewidth=2)
    ax3.add_patch(circle_observer)
    ax3.text(0.5, 0.75, '觀察者', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # 箭頭向下（觀察）
    ax3.annotate('', xy=(0.5, 0.45), xytext=(0.5, 0.65),
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax3.text(0.6, 0.55, '觀察\n測量', ha='left', fontsize=10,
            color='red', fontweight='bold')

    # 量子系統（疊加→確定）
    # 疊加態
    circle_left = plt.Circle((0.35, 0.35), 0.06, color='red', alpha=0.3,
                            edgecolor='red', linewidth=1.5)
    circle_right = plt.Circle((0.65, 0.35), 0.06, color='blue', alpha=0.3,
                             edgecolor='blue', linewidth=1.5)
    ax3.add_patch(circle_left)
    ax3.add_patch(circle_right)

    # 箭頭（疊加→確定）
    ax3.plot([0.35, 0.65], [0.35, 0.35], 'gray', linestyle=':', alpha=0.5)
    ax3.text(0.5, 0.3, '疊加態', ha='center', fontsize=9, color='gray')

    # 坍縮後
    circle_result = plt.Circle((0.5, 0.15), 0.08, color='green', alpha=0.7,
                              edgecolor='darkgreen', linewidth=2)
    ax3.add_patch(circle_result)
    ax3.text(0.5, 0.15, '確定態', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    ax3.annotate('', xy=(0.5, 0.23), xytext=(0.5, 0.29),
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))

    ax3.text(0.5, 0.05, '觀察創造實在\n屬性依測量而定', ha='center',
            fontsize=10, transform=ax3.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # 總標題
    fig.text(0.5, 0.98, '「心」的角色：三種觀點',
            ha='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig('mind_principle_observer.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n" + "="*70)
    print("【王陽明「心即理」與觀察者效應】")
    print("="*70)

    print("\n王陽明的心學：")
    print("  核心：「心即理」")
    print("  → 心外無物，心外無理")
    print("  → 離開心，無法談論物的存在和意義")

    print("\n龍場悟道（1508）：")
    print("  「聖人之道，吾性自足，")
    print("   向之求理於事物者誤也！」")
    print("  → 過去向外求理，錯了")
    print("  → 理在心中")

    print("\n「知行合一」：")
    print("  • 真知必然帶來真行")
    print("  • 知和行不可分離")
    print("  • 例：知道火熱→不會摸火")

    print("\n量子力學的觀察者效應：")
    print("  • 測量前：粒子處於疊加態")
    print("  • 測量時：波函數坍縮")
    print("  • 測量後：粒子處於確定態")
    print("  → 觀察者參與創造實在")

    print("\n對應：")
    print("  王陽明：心外無物")
    print("  量子：觀察外無確定屬性")

    print("\n  王陽明：物依心而顯")
    print("  量子：屬性依測量而定")

    print("\n差異：")
    print("  • 王陽明的「心」：")
    print("    不只是個人意識")
    print("    而是本體、宇宙心")
    print("  • 量子的「觀察者」：")
    print("    可以是測量儀器")
    print("    不一定需要意識")

    print("\n共同洞見：")
    print("  • 「客觀實在」依賴主體")
    print("  • 主體和客體不可分離")
    print("  • 「物自體」不可知")

    print("\n深刻問題：")
    print("  • 王陽明的「心」= 量子的「觀察者」？")
    print("  • 「心即理」= 「觀察創造實在」？")
    print("  • 還是兩者指向不同層次的真理？")
    print("="*70)

# 執行
visualize_mind_principle_observer()
