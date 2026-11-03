# Code & Cogito: 取り付け騒ぎ：ノーザン・ロックからシリコンバレー銀行まで
# Article: https://code-cogito.com/ja/?p=2626
# All the code blocks of the article, in order. Program output is kept as comments.

import numpy as np

def bank_run_simulation(
    n_depositors=1000,
    deposit_each=10000,
    reserve_ratio=0.10,
    fire_sale_penalty=0.30,
    panic_levels=[0.05, 0.10, 0.15, 0.25, 0.50, 0.75, 1.00]
):
    """
    取り付け騒ぎの自己実現的予言モデル（協調ゲームの簡略な例示。利得を並べるだけで、均衡は解いていない）

    核心的洞察：各預金者の「合理的」な引き出し判断が、
    集計されると全員が避けようとした銀行破綻を引き起こす。
    """
    total_deposits = n_depositors * deposit_each
    cash_reserve = total_deposits * reserve_ratio
    loans = total_deposits * (1 - reserve_ratio)

    print(f"=== 取り付け騒ぎ：自己実現的予言 ===\n")
    print(f"預金者数：{n_depositors}")
    print(f"一人当たり預金：${deposit_each:,.0f}")
    print(f"総預金：${total_deposits:,.0f}")
    print(f"現金準備金（{reserve_ratio:.0%}）：${cash_reserve:,.0f}")
    print(f"貸出済み：${loans:,.0f}\n")

    print(f"{'引出比率':>10} {'引出人数':>8} {'需要額':>14} "
          f"{'利用可能額':>14} {'一人当たり':>10} {'損失率':>8} {'結果':>12}")
    print("-" * 90)

    for panic in panic_levels:
        withdrawers = int(n_depositors * panic)
        demand = withdrawers * deposit_each

        if demand <= cash_reserve:
            available = demand
            recovery = deposit_each
            loss = 0.0
            status = "銀行存続"
        else:
            shortfall = demand - cash_reserve
            liquidated = min(shortfall / (1 - fire_sale_penalty), loans)
            recovered = liquidated * (1 - fire_sale_penalty)
            available = cash_reserve + recovered
            recovery = available / withdrawers if withdrawers > 0 else 0
            loss = 1 - (recovery / deposit_each)
            remaining_assets = loans - liquidated
            status = "投げ売り" if remaining_assets > 0 else "銀行倒産"

        print(f"{panic:>9.0%} {withdrawers:>8} ${demand:>13,.0f} "
              f"${available:>13,.0f} ${recovery:>9,.0f} "
              f"{loss:>7.1%} {status:>12}")

    print(f"\n--- 協調ゲーム分析 ---")
    print(f"他の人が引き出さないと信じる → 自分も引き出さない → 銀行は安全（最良の結果）")
    print(f"他の人が引き出すと信じる   → 自分も引き出す必要あり → 銀行倒産（最悪の結果）")
    print(f"結論：個人の合理的選択 → 集団の壊滅的結果")

bank_run_simulation()

# | === 取り付け騒ぎ：自己実現的予言 ===
# | 
# | 預金者数：1000
# | 一人当たり預金：$10,000
# | 総預金：$10,000,000
# | 現金準備金（10%）：$1,000,000
# | 貸出済み：$9,000,000
# | 
# |       引出比率     引出人数            需要額          利用可能額      一人当たり      損失率           結果
# | ------------------------------------------------------------------------------------------
# |        5%       50 $      500,000 $      500,000 $   10,000    0.0%         銀行存続
# |       10%      100 $    1,000,000 $    1,000,000 $   10,000    0.0%         銀行存続
# |       15%      150 $    1,500,000 $    1,500,000 $   10,000    0.0%         投げ売り
# |       25%      250 $    2,500,000 $    2,500,000 $   10,000    0.0%         投げ売り
# |       50%      500 $    5,000,000 $    5,000,000 $   10,000    0.0%         投げ売り
# |       75%      750 $    7,500,000 $    7,300,000 $    9,733    2.7%         銀行倒産
# |      100%     1000 $   10,000,000 $    7,300,000 $    7,300   27.0%         銀行倒産
# | 
# | --- 協調ゲーム分析 ---
# | 他の人が引き出さないと信じる → 自分も引き出さない → 銀行は安全（最良の結果）
# | 他の人が引き出すと信じる   → 自分も引き出す必要あり → 銀行倒産（最悪の結果）
# | 結論：個人の合理的選択 → 集団の壊滅的結果
