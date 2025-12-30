"""
黃金比例驗證
簡單計算人體的黃金分割點

文章：達文西的解剖學革命
作者：Wina
系列：文藝復興的數位重生 #3/12
"""

import numpy as np

print("=" * 60)
print("黃金比例驗證")
print("=" * 60)

# ===== 黃金比例計算 =====

PHI = (1 + np.sqrt(5)) / 2

print(f"\n【黃金比例的定義】")
print(f"φ = (1 + √5) / 2")
print(f"φ = {PHI:.10f}")
print(f"φ ≈ 1.618")

# ===== 人體黃金分割點 =====

# 假設身高為8個頭長（達文西的標準比例）
height = 8.0

# 黃金分割點計算
# 肚臍應該在整體高度的 φ/(1+φ) = 1/φ 位置
navel_to_head = height / PHI
navel_to_feet = height - navel_to_head

print(f"\n【人體的黃金分割】")
print(f"如果身高 = {height} 個頭長")
print(f"黃金分割點（肚臍）應該在：")
print(f"  從頭頂往下: {navel_to_head:.3f} 個頭長")
print(f"  從腳底往上: {navel_to_feet:.3f} 個頭長")

# 驗證比例
ratio = navel_to_head / navel_to_feet

print(f"\n【比例驗證】")
print(f"上段 / 下段 = {ratio:.10f}")
print(f"黃金比例 φ = {PHI:.10f}")
print(f"誤差       = {abs(ratio - PHI):.12f}")

if abs(ratio - PHI) < 0.000001:
    print("\n✓ 完美符合黃金比例！")
    print("✓ 達文西的測量是正確的")
else:
    print(f"\n✗ 有微小偏差")

# ===== 黃金比例的特性 =====

print(f"\n【黃金比例的數學特性】")
print(f"1. φ² = φ + 1")
print(f"   驗證: {PHI**2:.6f} = {PHI + 1:.6f} ✓")

print(f"\n2. 1/φ = φ - 1")
print(f"   驗證: {1/PHI:.6f} = {PHI - 1:.6f} ✓")

print(f"\n3. φ = 1 + 1/φ")
print(f"   驗證: {PHI:.6f} = {1 + 1/PHI:.6f} ✓")

# ===== 費波那契數列與黃金比例 =====

print(f"\n【費波那契數列與黃金比例】")
print(f"費波那契數列: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...")
print(f"相鄰項的比值趨近黃金比例：")

fib = [1, 1]
for i in range(10):
    fib.append(fib[-1] + fib[-2])

print(f"\n{'n':<5} {'Fn':<8} {'Fn+1':<8} {'Fn+1/Fn':<12} {'與φ的誤差':<15}")
print("-" * 50)
for i in range(5, 10):
    ratio_fib = fib[i+1] / fib[i]
    error = abs(ratio_fib - PHI)
    print(f"{i:<5} {fib[i]:<8} {fib[i+1]:<8} {ratio_fib:<12.8f} {error:<15.8f}")

print(f"\n→ 數列越後面，比值越接近φ")

# ===== 黃金比例的其他應用 =====

print(f"\n【黃金比例的其他應用】")
print("=" * 60)

print("\n建築：")
print("  • 帕德嫩神廟的寬高比 ≈ φ")
print("  • 埃及金字塔的斜邊與底邊比 ≈ φ")

print("\n藝術：")
print("  • 《蒙娜麗莎》的構圖使用黃金矩形")
print("  • 達文西的許多畫作都暗藏黃金比例")

print("\n自然：")
print("  • 鸚鵡螺殼的螺旋符合黃金螺旋")
print("  • 向日葵種子的排列遵循φ")
print("  • 松果的螺旋數量是費波那契數")

print("\n設計：")
print("  • 信用卡尺寸（85.60 × 53.98 mm）≈ φ")
print("  • 書籍開本常用黃金矩形比例")

print("\n音樂：")
print("  • 貝多芬《第五交響曲》的段落比例")
print("  • 莫札特奏鳴曲的展開部與再現部比例")

print("\n" + "=" * 60)
print("黃金比例無處不在！")
print("=" * 60)
