# Code & Cogito: ダ・ヴィンチの解剖学革命
# Article: https://code-cogito.com/ja/da-vinci-anatomy-revolution-ja/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np

# 日本語フォント設定

print("=" * 60)
print("ウィトルウィウス的人体図 比例分析")
print("=" * 60)

# ===== パート1：人体比例の計算 =====

# 黄金比
PHI = (1 + np.sqrt(5)) / 2  # ≈ 1.618

# 基準単位：頭部の長さ = 1
HEAD = 1.0

# ウィトルウィウスの人体比例（頭部の長さを基準）
BODY_PROPORTIONS = {
    '頭部': HEAD,
    '顔': HEAD * 8/10,                # 顔 = 身長の1/10 = 頭部の0.8倍
    '身長': HEAD * 8,                  # 身長 = 頭部 × 8
    '両腕幅': HEAD * 8,               # 両腕を広げた幅 = 身長
    '臍から頭頂': HEAD * 8 - (HEAD * 8 / PHI),
    '臍から足底': HEAD * 8 / PHI,     # 仮定：臍を黄金分割点に置く（設定値であり計測値ではない）
    '肩幅': HEAD * 2,
    '手のひら': HEAD * 8/10,          # 手のひら = 顔
    '足の長さ': HEAD * 8/7
}

print("\n[人体比例一覧表]")
print(f"{'部位':<15} {'比率(頭部)':<12} {'数値':<10}")
print("-" * 45)

for part, value in BODY_PROPORTIONS.items():
    ratio = value / HEAD
    print(f"{part:<15} {ratio:<12.3f} {value:<10.3f}")

# 黄金比の確認：臍の位置をφで決めているので、結果は必ずφになる（独立した検証ではない）
navel_ratio = BODY_PROPORTIONS['臍から足底'] / BODY_PROPORTIONS['臍から頭頂']

print(f"\n【黄金比の確認】")
print(f"臍の分割比率: {navel_ratio:.3f}")
print(f"黄金比 φ: {PHI:.3f}")
print(f"誤差: {abs(navel_ratio - PHI):.4f}")

if abs(navel_ratio - PHI) < 0.01:
    print("=> 設定どおり：臍の位置はφを使って置いたもの")
else:
    print("=> 黄金比との偏差が検出された")

print(f"\n【主要な発見】")
print(f"・人体は無作為ではない。数学的法則に従っている")
print(f"・臍の位置：このモデルでは黄金分割に置いている（仮定であり、計測値ではない）")
print(f"・身長 = 頭部 × 8（絵画の古典的比率）")
print(f"・両腕を広げた幅 = 身長（正方形を形成）")
print(f"\n=> 人体即ち宇宙、数学即ち美学")

# ===== パート2：ウィトルウィウス的人体図の可視化 =====

height = BODY_PROPORTIONS['身長']
arm_span = BODY_PROPORTIONS['両腕幅']
navel_y = BODY_PROPORTIONS['臍から足底']

# === 左図：円内の人体（両腕・両脚を広げた姿勢） ===

# 円を描画（臍を中心とする）
circle_radius = arm_span / 2
circle = Circle((0, navel_y), circle_radius,
               fill=False, edgecolor='#4169E1', linewidth=2, linestyle='--')

# 人体の簡略図
head_radius = HEAD / 2
head = Circle((0, height - head_radius), head_radius,
             fill=False, edgecolor='black', linewidth=2)

# 胴体
torso_width = BODY_PROPORTIONS['肩幅']

# 両腕（広げた状態）
arm_length = arm_span / 2

# 両脚（広げた状態、円周に接する）
leg_angle = np.pi / 6  # 30度
leg_length = navel_y
left_leg_x = -leg_length * np.sin(leg_angle)
left_leg_y = navel_y - leg_length * np.cos(leg_angle)

right_leg_x = leg_length * np.sin(leg_angle)
right_leg_y = navel_y - leg_length * np.cos(leg_angle)

# 注釈

# === 右図：正方形内の人体（両脚を揃え、両腕を水平に） ===

# 正方形を描画
square_side = height
square = Rectangle((-square_side/2, 0), square_side, square_side,
                  fill=False, edgecolor='#C41E3A', linewidth=2, linestyle='--')

# 頭部
head2 = Circle((0, height - head_radius), head_radius,
              fill=False, edgecolor='black', linewidth=2)

# 胴体

# 両腕（水平）

# 両脚（揃えた状態）

# 黄金比分割の注釈

print("\n=> 可視化完了：vitruvian_man.png")
print("=> ダ・ヴィンチのウィトルウィウス的人体図：数学と芸術の完璧な融合")
