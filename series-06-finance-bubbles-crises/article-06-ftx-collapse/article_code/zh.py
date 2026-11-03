# Code & Cogito: FTX崩潰與信任的破產（完結篇）
# Article: https://code-cogito.com/finance-06/
# All the code blocks of the article, in order. Program output is kept as comments.

def leverage_tower_collapse(
    initial_ftt_price=25.0,
    total_ftt_supply=350_000_000,
    alameda_ftt_holdings=0.40,
    collateral_ratio=0.80,
    margin_call_threshold=0.50,
    price_drops=[0.0, -0.10, -0.20, -0.30, -0.40, -0.50, -0.70, -0.90]
):
    """
    FTX-Alameda 槓桿之塔模型

    FTT作為抵押品的循環依賴：
    當FTT價格下跌 → Alameda的抵押品不足 → 被迫賣FTT →
    FTT價格進一步下跌 → 更多抵押品不足 → 死亡螺旋
    """
    alameda_ftt = total_ftt_supply * alameda_ftt_holdings

    print(f"=== FTX-Alameda 槓桿之塔崩潰模型 ===\n")
    print(f"FTT 初始價格：${initial_ftt_price}")
    print(f"FTT 總供應量：{total_ftt_supply:,.0f}")
    print(f"Alameda 持有 FTT：{alameda_ftt:,.0f}（{alameda_ftt_holdings:.0%}）")
    print(f"抵押率：{collateral_ratio:.0%}（借款/抵押品價值）")
    print(f"覆蓋率低於 100% 進入追繳保證金，低於 {margin_call_threshold:.0%} 進入強制清算\n")

    initial_value = alameda_ftt * initial_ftt_price
    borrowed = initial_value * collateral_ratio

    print(f"初始抵押品價值：${initial_value / 1e9:.2f}B")
    print(f"借入資金：${borrowed / 1e9:.2f}B\n")

    print(f"{'FTT價格':>10} {'跌幅':>8} {'抵押品價值':>14} {'借款':>12} "
          f"{'覆蓋率':>8} {'缺口':>14} {'狀態':>16}")
    print("-" * 100)

    for drop in price_drops:
        price = initial_ftt_price * (1 + drop)
        collateral_value = alameda_ftt * price
        coverage = collateral_value / borrowed if borrowed > 0 else 0
        gap = collateral_value - borrowed

        if coverage >= 1.0:
            status = "安全"
        elif coverage >= margin_call_threshold:
            status = "追繳保證金"
        elif coverage > 0:
            status = "強制清算"
        else:
            status = "完全崩潰"

        if gap < 0:
            gap_str = f"-${abs(gap)/1e9:.2f}B"
        else:
            gap_str = f"+${gap/1e9:.2f}B"

        print(f"${price:>9.2f} {drop:>+7.0%} ${collateral_value/1e9:>10.2f}B "
              f"${borrowed/1e9:>10.2f}B {coverage:>7.0%} {gap_str:>14} {status:>16}")

    print(f"\n--- 死亡螺旋機制 ---")
    print(f"1. FTT價格下跌 → Alameda抵押品不足")
    print(f"2. 收到追繳保證金通知 → 被迫賣出FTT")
    print(f"3. 大量FTT被拋售 → FTT價格進一步下跌")
    print(f"4. 更多抵押品不足 → 更多強制賣出")
    print(f"5. FTT價格歸零 → Alameda破產 → FTX破產")
    print(f"\n關鍵洞察：FTT的價值取決於FTX，FTX的償付能力取決於")
    print(f"Alameda，而Alameda的資產大部分是FTT。這是一個閉環。")
    print(f"打破環中任何一點，整個結構崩潰。")

leverage_tower_collapse()

# | === FTX-Alameda 槓桿之塔崩潰模型 ===
# | 
# | FTT 初始價格：$25.0
# | FTT 總供應量：350,000,000
# | Alameda 持有 FTT：140,000,000（40%）
# | 抵押率：80%（借款/抵押品價值）
# | 覆蓋率低於 100% 進入追繳保證金，低於 50% 進入強制清算
# | 
# | 初始抵押品價值：$3.50B
# | 借入資金：$2.80B
# | 
# |    FTT價格     跌幅       抵押品價值         借款   覆蓋率           缺口             狀態
# | ----------------------------------------------------------------------------------------------------
# |     $25.00     +0%      $3.50B      $2.80B   125%       +$0.70B             安全
# |     $22.50    -10%      $3.15B      $2.80B   112%       +$0.35B             安全
# |     $20.00    -20%      $2.80B      $2.80B   100%       +$0.00B             安全
# |     $17.50    -30%      $2.45B      $2.80B    88%       -$0.35B         追繳保證金
# |     $15.00    -40%      $2.10B      $2.80B    75%       -$0.70B         追繳保證金
# |     $12.50    -50%      $1.75B      $2.80B    62%       -$1.05B         追繳保證金
# |      $7.50    -70%      $1.05B      $2.80B    38%       -$1.75B         強制清算
# |      $2.50    -90%      $0.35B      $2.80B    12%       -$2.45B         強制清算
# | 
# | --- 死亡螺旋機制 ---
# | 1. FTT價格下跌 → Alameda抵押品不足
# | 2. 收到追繳保證金通知 → 被迫賣出FTT
# | 3. 大量FTT被拋售 → FTT價格進一步下跌
# | 4. 更多抵押品不足 → 更多強制賣出
# | 5. FTT價格歸零 → Alameda破產 → FTX破產
# | 
# | 關鍵洞察：FTT的價值取決於FTX，FTX的償付能力取決於
# | Alameda，而Alameda的資產大部分是FTT。這是一個閉環。
# | 打破環中任何一點，整個結構崩潰。
