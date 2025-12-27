"""
匯票利潤計算模擬
展示美第奇銀行如何用匯票繞過高利貸禁令

文章：美第奇家族的金融帝國
作者：Wina
系列：文藝復興的數位重生 #2/12
"""

print("=" * 60)
print("匯票利潤計算模擬")
print("=" * 60)

def calculate_bill_profit(principal, spot_rate, forward_rate, months):
    """
    計算匯票交易的利潤
    
    參數：
    principal: 本金（佛羅林）
    spot_rate: 即期匯率（佛羅林/英鎊）
    forward_rate: 遠期匯率
    months: 時間（月）
    
    返回：
    利潤、年化報酬率等資訊
    """
    # 客戶支付的英鎊
    gbp_paid = principal / forward_rate
    
    # 銀行實際成本
    gbp_cost = principal / spot_rate
    
    # 利潤（英鎊）
    profit_gbp = gbp_paid - gbp_cost
    
    # 換算回佛羅林
    profit_florin = profit_gbp * spot_rate
    
    # 年化報酬率
    annual_return = (profit_florin / principal) * (12 / months) * 100
    
    return {
        'profit_florin': profit_florin,
        'annual_return': annual_return,
        'gbp_paid': gbp_paid,
        'gbp_cost': gbp_cost,
        'profit_gbp': profit_gbp
    }

# ===== 範例計算 =====

print("\n【匯票交易範例】")
print("=" * 60)

# 情境：倫敦羊毛商欠佛羅倫斯布商100佛羅林
result = calculate_bill_profit(
    principal=100,      # 100佛羅林
    spot_rate=0.25,     # 1佛羅林 = 0.25英鎊（即期）
    forward_rate=0.24,  # 1佛羅林 = 0.24英鎊（3個月後）
    months=3
)

print(f"\n交易條件：")
print(f"  本金: 100 佛羅林")
print(f"  即期匯率: 1佛羅林 = 0.25英鎊")
print(f"  遠期匯率: 1佛羅林 = 0.24英鎊（3個月後）")
print(f"  時間: 3個月")

print(f"\n交易過程：")
print(f"  1. 羊毛商在倫敦美第奇分行購買匯票")
print(f"     支付: {result['gbp_paid']:.2f} 英鎊")
print(f"  2. 匯票寄給佛羅倫斯布商（紙張，不怕被搶）")
print(f"  3. 布商在佛羅倫斯美第奇總行兌現")
print(f"     領取: 100 佛羅林")

print(f"\n美第奇銀行的收益：")
print(f"  客戶支付: {result['gbp_paid']:.2f} 英鎊")
print(f"  銀行成本: {result['gbp_cost']:.2f} 英鎊")
print(f"  利潤（英鎊）: {result['profit_gbp']:.2f} 英鎊")
print(f"  利潤（佛羅林）: {result['profit_florin']:.2f} 佛羅林")
print(f"  年化報酬率: {result['annual_return']:.2f}%")

# ===== 關鍵洞察 =====

print(f"\n【關鍵洞察】")
print("=" * 60)
print(f"• 表面上：這只是貨幣兌換服務")
print(f"• 實際上：{result['profit_florin']:.2f}佛羅林就是利息")
print(f"• 技巧：利息偽裝成「匯率差」")
print(f"• 結果：規避了教會的高利貸禁令")
print(f"\n→ 這是金融工程的早期形式！")

# ===== 不同情境比較 =====

print(f"\n【不同時間的年化報酬率】")
print("=" * 60)
print(f"{'時間（月）':<12} {'年化報酬率':<15}")
print("-" * 30)

for months in [1, 3, 6, 12]:
    result_temp = calculate_bill_profit(100, 0.25, 0.24, months)
    print(f"{months:<12} {result_temp['annual_return']:<15.2f}%")

print(f"\n→ 時間越短，年化報酬率越高")
print(f"→ 美第奇銀行偏好短期匯票（3-6個月）")

# ===== 與現代金融產品對比 =====

print(f"\n【與現代金融產品對比】")
print("=" * 60)
print(f"美第奇銀行匯票（3個月）: {result['annual_return']:.2f}%")
print(f"現代信用卡利率: 15-20%")
print(f"現代企業債券: 3-6%")
print(f"現代銀行定存: 1-2%")
print(f"\n→ 美第奇的匯票報酬率相當於中等風險投資")

print("\n" + "=" * 60)
print("模擬完成！")
print("=" * 60)
