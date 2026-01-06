"""
透視法的數學秘密 - 免費版程式碼
Renaissance Digital Rebirth Series #4 (Free Version)

作者：Wina Wu
日期：2025-12

本免費版包含：
✓ 基礎透視投影函數
✓ 簡單的3D立方體投影示範
✓ 一點透視法視覺化

完整版（付費訂閱）另包含：
• 兩點透視法視覺化
• 透視縮放驗證
• 多物體3D場景渲染
• 文藝復興傑作分析程式碼

需要的套件：
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 70)
print("透視法的數學秘密 - 免費版")
print("Renaissance Digital Rebirth Series #4")
print("=" * 70)
print()

# ============================================================================
# 核心函數：透視投影
# ============================================================================

def perspective_projection(point_3d, d=5.0):
    """
    透視投影：將3D點投影到2D平面
    
    數學原理：
        x' = (d × x) / z
        y' = (d × y) / z
    
    參數：
    - point_3d: (x, y, z) 3D座標
    - d: 畫面平面距離（預設5.0）
    
    返回：
    - (x', y') 2D投影座標
    """
    x, y, z = point_3d
    
    # 避免除以零
    if z == 0:
        z = 0.001
    
    # 透視投影公式
    x_proj = (d * x) / z
    y_proj = (d * y) / z
    
    return x_proj, y_proj


def create_cube(size=1, center=(0, 0, 5)):
    """創建立方體的頂點和邊"""
    cx, cy, cz = center
    s = size / 2
    
    # 8個頂點
    vertices = np.array([
        [cx - s, cy - s, cz - s],  # 0: 左下後
        [cx + s, cy - s, cz - s],  # 1: 右下後
        [cx + s, cy + s, cz - s],  # 2: 右上後
        [cx - s, cy + s, cz - s],  # 3: 左上後
        [cx - s, cy - s, cz + s],  # 4: 左下前
        [cx + s, cy - s, cz + s],  # 5: 右下前
        [cx + s, cy + s, cz + s],  # 6: 右上前
        [cx - s, cy + s, cz + s],  # 7: 左上前
    ])
    
    # 12條邊
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # 後面
        (4, 5), (5, 6), (6, 7), (7, 4),  # 前面
        (0, 4), (1, 5), (2, 6), (3, 7),  # 連接前後
    ]
    
    return vertices, edges


# ============================================================================
# 示範：基礎透視投影
# ============================================================================

print("示範：3D立方體的透視投影\n")

# 創建立方體
vertices_3d, edges = create_cube(size=2, center=(0, 0, 8))

# 投影到2D
vertices_2d = np.array([perspective_projection(v, d=5.0) for v in vertices_3d])

# 視覺化
fig = plt.figure(figsize=(14, 6))

# === 3D視圖 ===
ax1 = fig.add_subplot(121, projection='3d')

for edge in edges:
    points = vertices_3d[[edge[0], edge[1]]]
    ax1.plot3D(*points.T, 'b-', linewidth=2)

ax1.scatter(*vertices_3d.T, c='red', s=100)
ax1.scatter(0, 0, 0, c='black', s=200, marker='o', label='觀察者')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z(深度)')
ax1.set_title('3D視圖', fontsize=13, fontweight='bold')
ax1.legend()

# === 2D投影 ===
ax2 = fig.add_subplot(122)

for edge in edges:
    points = vertices_2d[[edge[0], edge[1]]]
    ax2.plot(*points.T, 'b-', linewidth=2)

ax2.scatter(*vertices_2d.T, c='red', s=100)

ax2.set_xlabel('X\'')
ax2.set_ylabel('Y\'')
ax2.set_title('2D透視投影', fontsize=13, fontweight='bold')
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('perspective_basic_free.png', dpi=300, bbox_inches='tight')
plt.show()

# 輸出數據
print("3D立方體頂點 → 2D投影：")
print(f"{'頂點':<6} {'3D座標':<25} {'2D投影':<15}")
print("-" * 50)
for i, (v3d, v2d) in enumerate(zip(vertices_3d, vertices_2d)):
    print(f"頂點{i}  ({v3d[0]:4.1f}, {v3d[1]:4.1f}, {v3d[2]:4.1f})  →  ({v2d[0]:5.2f}, {v2d[1]:5.2f})")

print("\n✓ 觀察：後面的頂點投影較小，前面的頂點投影較大")

# ============================================================================
# 總結
# ============================================================================

print("\n" + "=" * 70)
print("透視法核心公式：")
print("-" * 70)
print("x' = (d × x) / z")
print("y' = (d × y) / z")
print("-" * 70)
print("關鍵：除以深度 z → 距離越遠，投影越小")
print("=" * 70)

print("\n想要完整版程式碼？")
print("訂閱 Code & Cogito Newsletter")
print("獲得：兩點透視、3D場景渲染、文藝復興作品分析")
print("\n感謝使用！")
print("=" * 70)
