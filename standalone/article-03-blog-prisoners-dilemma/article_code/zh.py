# Code & Cogito: 用 Python 模擬囚徒困境：從海洋生態合作到遊戲理論哲學
# Article: https://code-cogito.com/blog-prisoners-dilemma/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import numpy as np

class PrisonersDilemma:
    """囚徒困境遊戲引擎"""

    def __init__(self):
        # 收益矩陣：(玩家1收益, 玩家2收益)
        # 0 = 合作, 1 = 背叛
        self.payoff_matrix = {
            (0, 0): (3, 3),  # 雙方合作：互利共贏
            (0, 1): (0, 5),  # 我合作對方背叛：我被利用
            (1, 0): (5, 0),  # 我背叛對方合作：我佔便宜
            (1, 1): (1, 1),  # 雙方背叛：兩敗俱傷
        }

    def play_round(self, action1, action2):
        return self.payoff_matrix[(action1, action2)]

class MarineCreature:
    """海洋生物：每種策略代表一種生存哲學"""

    def __init__(self, name, strategy_type):
        self.name = name
        self.strategy_type = strategy_type
        self.total_payoff = 0
        self.reputation = 0.5  # 信譽值（僅作記錄，沒有任何策略讀取它）

    def choose_strategy(self, opponent_history, current_round):
        """根據策略類型選擇行動"""

        if self.strategy_type == "always_cooperate":
            # 善良珊瑚：永遠合作
            # 哲學：理想主義，相信善意終將回報
            return 0

        elif self.strategy_type == "always_defect":
            # 自私海葵：永遠背叛
            # 哲學：霍布斯式現實主義，自保優先
            return 1

        elif self.strategy_type == "tit_for_tat":
            # 聰明清潔魚：以牙還牙
            # 第一輪合作，之後模仿對手上一輪行為
            # 哲學：對等互惠，你怎麼待我我怎麼待你
            if current_round == 0 or not opponent_history:
                return 0
            return opponent_history[-1]

        elif self.strategy_type == "tit_for_two_tats":
            # 謹慎小丑魚：雙重以牙還牙
            # 對手連續背叛兩次才報復
            # 哲學：寬容但不軟弱
            if len(opponent_history) < 2:
                return 0
            if opponent_history[-1] == 1 and opponent_history[-2] == 1:
                return 1
            return 0

        elif self.strategy_type == "generous_tit_for_tat":
            # 寬容海龜：寬容的以牙還牙
            # 有 10% 機率原諒對手的背叛
            # 哲學：儒家恕道，給人改過的機會
            if current_round == 0 or not opponent_history:
                return 0
            if opponent_history[-1] == 1:
                return 1 if random.random() > 0.1 else 0
            return 0

        else:  # random
            # 隨機水母：隨機行動
            # 哲學：不可預測性，混沌中的生存
            return random.choice([0, 1])

    def update_reputation(self, own_action, opponent_action):
        if own_action == 0:
            self.reputation = min(1.0, self.reputation + 0.01)
        else:
            self.reputation = max(0.0, self.reputation - 0.02)

class MarineEcosystemSimulation:
    """海洋生態系統模擬——博弈論的循環賽實驗場（六種固定策略兩兩對戰一次，沒有繁殖或淘汰）"""

    def __init__(self):
        self.game = PrisonersDilemma()
        self.creatures = []
        self.history = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def simulate_interaction(self, c1, c2, rounds=200):
        """模擬兩個生物之間的多輪互動"""
        h1, h2 = [], []
        pay1, pay2 = [], []

        for r in range(rounds):
            a1 = c1.choose_strategy(h2, r)
            a2 = c2.choose_strategy(h1, r)
            p1, p2 = self.game.play_round(a1, a2)

            h1.append(a1)
            h2.append(a2)
            pay1.append(p1)
            pay2.append(p2)

            c1.total_payoff += p1
            c2.total_payoff += p2
            c1.update_reputation(a1, a2)
            c2.update_reputation(a2, a1)

        return {
            'creature1': c1.name, 'creature2': c2.name,
            'cooperation_rate1': h1.count(0) / len(h1),
            'cooperation_rate2': h2.count(0) / len(h2),
            'total_payoff1': sum(pay1),
            'total_payoff2': sum(pay2),
        }

def run_tournament(ecosystem, rounds_per_match=200):
    """每對生物都進行對戰"""
    # 重置
    for c in ecosystem.creatures:
        c.total_payoff = 0
        c.reputation = 0.5

    results = []
    for i in range(len(ecosystem.creatures)):
        for j in range(i + 1, len(ecosystem.creatures)):
            result = ecosystem.simulate_interaction(
                ecosystem.creatures[i],
                ecosystem.creatures[j],
                rounds_per_match
            )
            results.append(result)

    # 排名
    ranked = sorted(ecosystem.creatures,
                    key=lambda x: x.total_payoff, reverse=True)
    return ranked, results

def analyze_winning_traits(strategy):
    """分析策略是否具備四個成功特徵（示意用偽代碼，非可執行：四個判斷函式並未定義）"""
    traits = {
        "善良": not strategy.strikes_first(),
        "可報復": strategy.punishes_defection(),
        "寬容": strategy.forgives_after_cooperation(),
        "清晰": strategy.is_predictable(),
    }
    return traits
    # 以牙還牙：四個全滿
    # 永遠合作：善良、寬容、清晰，但不可報復
    # 永遠背叛：只有清晰（不善良、不寬容；它對誰都背叛，並不是在回應對方，所以也談不上可報復）

# | # 報復循環（示意用的手寫軌跡，不是程式輸出）
# | round_1: A合作, B合作         -> (3,3)
# | round_2: A合作, B意外背叛     -> (0,5) # B其實想合作，但訊號出錯
# | round_3: A報復, B合作         -> (5,0)
# | round_4: A合作, B報復         -> (0,5)
# | # 永遠在報復中循環...
# | 
# | # 寬容打破循環（同樣是手寫示意；10% 的原諒機率下，平均要遇到約 10 次背叛才會原諒一次）
# | round_1: A合作, B合作         -> (3,3)
# | round_2: A合作, B意外背叛     -> (0,5)
# | round_3: A原諒(10%), B合作   -> (3,3) # 回到正軌
