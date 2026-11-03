# Code & Cogito: 達文西的解剖學革命
# Article: https://code-cogito.com/da-vinci-anatomy-revolution/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np

# 設定中文字體

print("=" * 60)
print("維特魯威人體比例分析")
print("=" * 60)

# ===== 程式一：計算人體比例 =====

# 黃金比例
PHI = (1 + np.sqrt(5)) / 2  # ≈ 1.618

# 人體基準單位（以頭長為1單位）
HEAD = 1.0

# 維特魯威的人體比例（以頭長為基準）
BODY_PROPORTIONS = {
    '頭長': HEAD,
    '臉長': HEAD * 10/8,          # 臉長 = 頭長的 1.25 倍
    '身高': HEAD * 8,              # 身高 = 8個頭長
    '雙臂張開': HEAD * 8,          # 張開雙臂 = 身高
    '肚臍到頭頂': HEAD * 8 - (HEAD * 8 / PHI),
    '肚臍到腳底': HEAD * 8 / PHI,  # 假設：肚臍在黃金分割點（設定值，非測量）
    '肩寬': HEAD * 2,
    '手掌長': HEAD * 10/8,         # 手掌長 = 臉長
    '腳長': HEAD * 8/7
}

print("\n[人體比例一覽表]")
print(f"{'部位':<15} {'比例(頭長)':<12} {'數值':<10}")
print("-" * 45)

for part, value in BODY_PROPORTIONS.items():
    ratio = value / HEAD
    print(f"{part:<15} {ratio:<12.3f} {value:<10.3f}")

# 檢查黃金比例：肚臍位置是用 φ 設定的，結果必然等於 φ（不是獨立驗證）
navel_ratio = BODY_PROPORTIONS['肚臍到腳底'] / BODY_PROPORTIONS['肚臍到頭頂']

print(f"\n【黃金比例檢查】")
print(f"肚臍分割比例: {navel_ratio:.3f}")
print(f"黃金比例 φ: {PHI:.3f}")
print(f"誤差: {abs(navel_ratio - PHI):.4f}")

if abs(navel_ratio - PHI) < 0.01:
    print("✓ 與設定一致（肚臍位置本來就是依 φ 放的）")
else:
    print("✗ 與黃金比例有偏差")

print(f"\n【關鍵發現】")
print(f"• 人體不是隨機的，遵循數學規律")
print(f"• 肚臍位置：本模型依黃金分割設定（假設，非測量）")
print(f"• 身高 = 8個頭長（繪畫的經典比例）")
print(f"• 雙臂張開 = 身高（形成正方形）")
print(f"\n→ 人體即宇宙，數學即美學")

# ===== 程式二：繪製維特魯威人 =====

height = BODY_PROPORTIONS['身高']
arm_span = BODY_PROPORTIONS['雙臂張開']
navel_y = BODY_PROPORTIONS['肚臍到腳底']

# === 左圖：圓形內的人體（雙臂雙腿張開） ===

# 繪製圓形（以肚臍為圓心）
circle_radius = arm_span / 2
circle = Circle((0, navel_y), circle_radius,
               fill=False, edgecolor='#4169E1', linewidth=2, linestyle='--')

# 繪製人體簡化版
head_radius = HEAD / 2
head = Circle((0, height - head_radius), head_radius,
             fill=False, edgecolor='black', linewidth=2)

# 軀幹
torso_width = BODY_PROPORTIONS['肩寬']

# 雙臂（張開）
arm_length = arm_span / 2

# 雙腿（張開，觸碰圓周）
leg_angle = np.pi / 6  # 30度
leg_length = navel_y
left_leg_x = -leg_length * np.sin(leg_angle)
left_leg_y = navel_y - leg_length * np.cos(leg_angle)

right_leg_x = leg_length * np.sin(leg_angle)
right_leg_y = navel_y - leg_length * np.cos(leg_angle)

# 標註

# === 右圖：正方形內的人體（雙腿併攏，雙臂平舉） ===

# 繪製正方形
square_side = height
square = Rectangle((-square_side/2, 0), square_side, square_side,
                  fill=False, edgecolor='#C41E3A', linewidth=2, linestyle='--')

# 頭部
head2 = Circle((0, height - head_radius), head_radius,
              fill=False, edgecolor='black', linewidth=2)

# 軀幹

# 雙臂（平舉）

# 雙腿（併攏）

# 標註黃金比例分割

print("\n✓ 視覺化完成：vitruvian_man.png")
print("✓ 達文西的維特魯威人：數學與藝術的完美結合")
