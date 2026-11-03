# Code & Cogito: 銀行擠兌：從北岩銀行到矽谷銀行
# Article: https://code-cogito.com/?p=2624
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
    銀行擠兌的自我實現預言模型（協調賽局的簡化示意；只列出報酬，不求解均衡）

    核心洞察：每個存戶的「理性」提款決策，
    加總後創造了所有人都試圖避免的銀行倒閉。
    """
    total_deposits = n_depositors * deposit_each
    cash_reserve = total_deposits * reserve_ratio
    loans = total_deposits * (1 - reserve_ratio)

    print(f"=== 銀行擠兌：自我實現的預言 ===\n")
    print(f"存戶數量：{n_depositors}")
    print(f"每人存款：${deposit_each:,.0f}")
    print(f"銀行總存款：${total_deposits:,.0f}")
    print(f"現金準備金（{reserve_ratio:.0%}）：${cash_reserve:,.0f}")
    print(f"已借出貸款：${loans:,.0f}\n")

    print(f"{'提款比例':>10} {'提款人數':>8} {'需求金額':>14} "
          f"{'可用資金':>14} {'每人拿回':>10} {'損失率':>8} {'結果':>12}")
    print("-" * 90)

    for panic in panic_levels:
        withdrawers = int(n_depositors * panic)
        demand = withdrawers * deposit_each

        if demand <= cash_reserve:
            available = demand
            recovery = deposit_each
            loss = 0.0
            status = "銀行存活"
        else:
            shortfall = demand - cash_reserve
            liquidated = min(shortfall / (1 - fire_sale_penalty), loans)
            recovered = liquidated * (1 - fire_sale_penalty)
            available = cash_reserve + recovered
            recovery = available / withdrawers if withdrawers > 0 else 0
            loss = 1 - (recovery / deposit_each)
            remaining_assets = loans - liquidated
            status = "被迫拋售" if remaining_assets > 0 else "銀行倒閉"

        print(f"{panic:>9.0%} {withdrawers:>8} ${demand:>13,.0f} "
              f"${available:>13,.0f} ${recovery:>9,.0f} "
              f"{loss:>7.1%} {status:>12}")

    print(f"\n--- 協調賽局分析 ---")
    print(f"如果你相信別人不會提款 → 你不提款 → 銀行安全（最佳結果）")
    print(f"如果你相信別人會提款   → 你必須提款 → 銀行倒閉（最差結果）")
    print(f"結論：理性的個人選擇 → 集體的災難性結果")

bank_run_simulation()

# | === 銀行擠兌：自我實現的預言 ===
# | 
# | 存戶數量：1000
# | 每人存款：$10,000
# | 銀行總存款：$10,000,000
# | 現金準備金（10%）：$1,000,000
# | 已借出貸款：$9,000,000
# | 
# |       提款比例     提款人數           需求金額           可用資金       每人拿回      損失率           結果
# | ------------------------------------------------------------------------------------------
# |        5%       50 $      500,000 $      500,000 $   10,000    0.0%         銀行存活
# |       10%      100 $    1,000,000 $    1,000,000 $   10,000    0.0%         銀行存活
# |       15%      150 $    1,500,000 $    1,500,000 $   10,000    0.0%         被迫拋售
# |       25%      250 $    2,500,000 $    2,500,000 $   10,000    0.0%         被迫拋售
# |       50%      500 $    5,000,000 $    5,000,000 $   10,000    0.0%         被迫拋售
# |       75%      750 $    7,500,000 $    7,300,000 $    9,733    2.7%         銀行倒閉
# |      100%     1000 $   10,000,000 $    7,300,000 $    7,300   27.0%         銀行倒閉
# | 
# | --- 協調賽局分析 ---
# | 如果你相信別人不會提款 → 你不提款 → 銀行安全（最佳結果）
# | 如果你相信別人會提款   → 你必須提款 → 銀行倒閉（最差結果）
# | 結論：理性的個人選擇 → 集體的災難性結果
