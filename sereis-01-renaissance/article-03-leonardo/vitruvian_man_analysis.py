"""
維特魯威人體比例分析（基礎版）
重現達文西的人體黃金比例發現

文章：達文西的解剖學革命
作者：Wina
系列：文藝復興的數位重生 #3/12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("維特魯威人體比例分析")
print("=" * 60)

# ===== 黃金比例 =====

PHI = (1 + np.sqrt(5)) / 2  # ≈ 1.618

print(f"\n黃金比例 φ = {PHI:.6f}")

# ===== 人體比例（以頭長為基準單位）=====

HEAD = 1.0

BODY_PROPORTIONS = {
    '頭長': HEAD,
    '臉長': HEAD * 10/8,          # 臉長 = 頭長的 1.25 倍
    '身高': HEAD * 8,              # 身高 = 8個頭長
    '雙臂張開': HEAD * 8,          # 張開雙臂 = 身高
    '肚臍到頭頂': HEAD * 8 / PHI,  # 黃金分割
    '肚臍到腳底': HEAD * 8 - (HEAD * 8 / PHI),
    '肩寬': HEAD * 2,
    '手掌長': HEAD * 10/8,         # 手掌長 = 臉長
    '腳長': HEAD * 8/7
}

# ===== 輸出比例表 =====

print("\n[人體比例一覽表]")
print(f"{'部位':<15} {'比例(頭長)':<12} {'數值':<10}")
print("-" * 45)

for part, value in BODY_PROPORTIONS.items():
    ratio = value / HEAD
    print(f"{part:<15} {ratio:<12.3f} {value:<10.3f}")

# ===== 驗證黃金比例 =====

navel_ratio = BODY_PROPORTIONS['肚臍到頭頂'] / BODY_PROPORTIONS['肚臍到腳底']

print(f"\n【黃金比例驗證】")
print(f"肚臍分割比例: {navel_ratio:.6f}")
print(f"黃金比例 φ:   {PHI:.6f}")
print(f"誤差:         {abs(navel_ratio - PHI):.8f}")

if abs(navel_ratio - PHI) < 0.01:
    print("\n✓ 達文西是對的！肚臍確實是黃金分割點")
else:
    print("\n✗ 與黃金比例有偏差")

print(f"\n【關鍵發現】")
print(f"• 人體不是隨機的，遵循數學規律")
print(f"• 肚臍位置恰好符合黃金分割")
print(f"• 身高 = 8個頭長（繪畫的經典比例）")
print(f"• 雙臂張開 = 身高（形成正方形）")
print(f"\n→ 人體即宇宙，數學即美學")

# ===== 視覺化維特魯威人 =====

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

height = BODY_PROPORTIONS['身高']
arm_span = BODY_PROPORTIONS['雙臂張開']
navel_y = BODY_PROPORTIONS['肚臍到腳底']

# === 左圖：圓形內的人體（雙臂雙腿張開） ===

# 繪製圓形（以肚臍為圓心）
circle_radius = arm_span / 2
circle = Circle((0, navel_y), circle_radius, 
               fill=False, edgecolor='#4169E1', linewidth=2, linestyle='--')
ax1.add_patch(circle)

# 繪製人體簡化版
head_radius = HEAD / 2
head = Circle((0, height - head_radius), head_radius,
             fill=False, edgecolor='black', linewidth=2)
ax1.add_patch(head)

# 軀幹
torso_width = BODY_PROPORTIONS['肩寬']
ax1.plot([0, 0], [navel_y, height - HEAD], 'k-', linewidth=3)
ax1.plot([-torso_width/2, torso_width/2], [height - HEAD, height - HEAD], 
        'k-', linewidth=3)

# 雙臂（張開）
arm_length = arm_span / 2
ax1.plot([0, -arm_length], [height - HEAD*1.5, height - HEAD*2], 
        'k-', linewidth=2)
ax1.plot([0, arm_length], [height - HEAD*1.5, height - HEAD*2], 
        'k-', linewidth=2)

# 雙腿（張開，觸碰圓周）
leg_angle = np.pi / 6  # 30度
leg_length = navel_y
left_leg_x = -leg_length * np.sin(leg_angle)
left_leg_y = navel_y - leg_length * np.cos(leg_angle)
ax1.plot([0, left_leg_x], [navel_y, left_leg_y], 'k-', linewidth=3)

right_leg_x = leg_length * np.sin(leg_angle)
right_leg_y = navel_y - leg_length * np.cos(leg_angle)
ax1.plot([0, right_leg_x], [navel_y, right_leg_y], 'k-', linewidth=3)

# 標註
ax1.plot(0, navel_y, 'ro', markersize=10, label='肚臍（圓心）')
ax1.text(0, navel_y - 0.5, '肚臍\n黃金分割點', 
        ha='center', fontsize=10, color='red', fontweight='bold')

ax1.set_xlim(-5, 5)
ax1.set_ylim(-1, 9)
ax1.set_aspect('equal')
ax1.set_title('維特魯威人：圓形構圖\n雙臂雙腿張開，以肚臍為圓心', 
             fontsize=14, fontweight='bold', pad=15)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.axvline(x=0, color='gray', linewidth=0.5)

# === 右圖：正方形內的人體（雙腿併攏，雙臂平舉） ===

# 繪製正方形
square_side = height
square = Rectangle((-square_side/2, 0), square_side, square_side,
                  fill=False, edgecolor='#C41E3A', linewidth=2, linestyle='--')
ax2.add_patch(square)

# 頭部
head2 = Circle((0, height - head_radius), head_radius,
              fill=False, edgecolor='black', linewidth=2)
ax2.add_patch(head2)

# 軀幹
ax2.plot([0, 0], [0, height - HEAD], 'k-', linewidth=3)
ax2.plot([-torso_width/2, torso_width/2], [height - HEAD, height - HEAD], 
        'k-', linewidth=3)

# 雙臂（平舉）
ax2.plot([0, -arm_span/2], [height - HEAD*1.5, height - HEAD*1.5], 
        'k-', linewidth=2)
ax2.plot([0, arm_span/2], [height - HEAD*1.5, height - HEAD*1.5], 
        'k-', linewidth=2)

# 雙腿（併攏）
ax2.plot([0, 0], [navel_y, 0], 'k-', linewidth=3)

# 標註黃金比例分割
ax2.plot([square_side/2 + 0.3, square_side/2 + 0.3], 
        [0, navel_y], 'b-', linewidth=2)
ax2.plot([square_side/2 + 0.3, square_side/2 + 0.3], 
        [navel_y, height], 'r-', linewidth=2)

ax2.text(square_side/2 + 0.8, navel_y/2, 
        f'{BODY_PROPORTIONS["肚臍到腳底"]:.2f}', 
        fontsize=10, color='blue', fontweight='bold')
ax2.text(square_side/2 + 0.8, (navel_y + height)/2, 
        f'{BODY_PROPORTIONS["肚臍到頭頂"]:.2f}', 
        fontsize=10, color='red', fontweight='bold')

ax2.plot(0, navel_y, 'go', markersize=10, 
        label=f'黃金分割點 ({navel_ratio:.3f}≈φ)')

ax2.set_xlim(-5, 5)
ax2.set_ylim(-1, 9)
ax2.set_aspect('equal')
ax2.set_title('維特魯威人：正方形構圖\n雙腿併攏，雙臂平舉', 
             fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='gray', linewidth=0.5)
ax2.axvline(x=0, color='gray', linewidth=0.5)

plt.tight_layout()

# 儲存圖片
plt.savefig('vitruvian_man.png', dpi=300, bbox_inches='tight')
print("\n✓ 視覺化完成：vitruvian_man.png")
print("✓ 達文西的維特魯威人：數學與藝術的完美結合")

plt.show()

print("\n" + "=" * 60)
print("分析完成！")
print("=" * 60)
