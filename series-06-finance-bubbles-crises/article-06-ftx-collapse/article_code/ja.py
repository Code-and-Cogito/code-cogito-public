# Code & Cogito: FTX崩壊と信頼の破産（完結編）
# Article: https://code-cogito.com/ja/?p=2632
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
    FTX-Alameda レバレッジの塔モデル

    FTTを担保とした循環依存：
    FTT価格下落 → アラメダの担保不足 → FTT売却を強制 →
    FTT価格さらに下落 → さらに担保不足 → 死のスパイラル
    """
    alameda_ftt = total_ftt_supply * alameda_ftt_holdings

    print(f"=== FTX-Alameda レバレッジの塔 崩壊モデル ===\n")
    print(f"FTT 初期価格：${initial_ftt_price}")
    print(f"FTT 総供給量：{total_ftt_supply:,.0f}")
    print(f"Alameda FTT保有量：{alameda_ftt:,.0f}（{alameda_ftt_holdings:.0%}）")
    print(f"担保率：{collateral_ratio:.0%}（借入/担保価値）")
    print(f"カバー率100%割れで追証、{margin_call_threshold:.0%}割れで強制清算\n")

    initial_value = alameda_ftt * initial_ftt_price
    borrowed = initial_value * collateral_ratio

    print(f"初期担保価値：${initial_value / 1e9:.2f}B")
    print(f"借入資金：${borrowed / 1e9:.2f}B\n")

    print(f"{'FTT価格':>10} {'下落率':>8} {'担保価値':>14} {'借入額':>12} "
          f"{'カバー率':>8} {'差額':>14} {'状態':>16}")
    print("-" * 100)

    for drop in price_drops:
        price = initial_ftt_price * (1 + drop)
        collateral_value = alameda_ftt * price
        coverage = collateral_value / borrowed if borrowed > 0 else 0
        gap = collateral_value - borrowed

        if coverage >= 1.0:
            status = "安全"
        elif coverage >= margin_call_threshold:
            status = "追証"
        elif coverage > 0:
            status = "強制清算"
        else:
            status = "完全崩壊"

        if gap < 0:
            gap_str = f"-${abs(gap)/1e9:.2f}B"
        else:
            gap_str = f"+${gap/1e9:.2f}B"

        print(f"${price:>9.2f} {drop:>+7.0%} ${collateral_value/1e9:>10.2f}B "
              f"${borrowed/1e9:>10.2f}B {coverage:>7.0%} {gap_str:>14} {status:>16}")

    print(f"\n--- 死のスパイラル メカニズム ---")
    print(f"1. FTT価格下落 → アラメダの担保不足")
    print(f"2. 追証通知を受領 → FTTの売却を強制される")
    print(f"3. 大量のFTTが投げ売り → FTT価格がさらに下落")
    print(f"4. さらなる担保不足 → さらなる強制売却")
    print(f"5. FTT価格がゼロに → アラメダ破産 → FTX破産")
    print(f"\n核心的洞察：FTTの価値はFTXに依存し、FTXの支払い能力は")
    print(f"アラメダに依存し、アラメダの資産の大半はFTTである。閉じた環だ。")
    print(f"環のどこか一点を壊せば、構造全体が崩壊する。")

leverage_tower_collapse()

# | === FTX-Alameda レバレッジの塔 崩壊モデル ===
# | 
# | FTT 初期価格：$25.0
# | FTT 総供給量：350,000,000
# | Alameda FTT保有量：140,000,000（40%）
# | 担保率：80%（借入/担保価値）
# | カバー率100%割れで追証、50%割れで強制清算
# | 
# | 初期担保価値：$3.50B
# | 借入資金：$2.80B
# | 
# |    FTT価格   下落率       担保価値       借入額 カバー率           差額             状態
# | ----------------------------------------------------------------------------------------------------
# |     $25.00     +0%      $3.50B      $2.80B   125%       +$0.70B             安全
# |     $22.50    -10%      $3.15B      $2.80B   112%       +$0.35B             安全
# |     $20.00    -20%      $2.80B      $2.80B   100%       +$0.00B             安全
# |     $17.50    -30%      $2.45B      $2.80B    88%       -$0.35B             追証
# |     $15.00    -40%      $2.10B      $2.80B    75%       -$0.70B             追証
# |     $12.50    -50%      $1.75B      $2.80B    62%       -$1.05B             追証
# |      $7.50    -70%      $1.05B      $2.80B    38%       -$1.75B         強制清算
# |      $2.50    -90%      $0.35B      $2.80B    12%       -$2.45B         強制清算
# | 
# | --- 死のスパイラル メカニズム ---
# | 1. FTT価格下落 → アラメダの担保不足
# | 2. 追証通知を受領 → FTTの売却を強制される
# | 3. 大量のFTTが投げ売り → FTT価格がさらに下落
# | 4. さらなる担保不足 → さらなる強制売却
# | 5. FTT価格がゼロに → アラメダ破産 → FTX破産
# | 
# | 核心的洞察：FTTの価値はFTXに依存し、FTXの支払い能力は
# | アラメダに依存し、アラメダの資産の大半はFTTである。閉じた環だ。
# | 環のどこか一点を壊せば、構造全体が崩壊する。
