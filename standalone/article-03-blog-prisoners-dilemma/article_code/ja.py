# Code & Cogito: Pythonで囚人のジレンマをシミュレーションする：海洋生態の協力からゲーム理論哲学へ
# Article: https://code-cogito.com/ja/blog-prisoners-dilemma-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import numpy as np

class PrisonersDilemma:
    """囚人のジレンマ ゲームエンジン"""

    def __init__(self):
        # 報酬マトリクス：(プレイヤー1の報酬, プレイヤー2の報酬)
        # 0 = 協力, 1 = 裏切り
        self.payoff_matrix = {
            (0, 0): (3, 3),  # 双方協力：互恵的ウィンウィン
            (0, 1): (0, 5),  # 自分が協力、相手が裏切り：搾取される
            (1, 0): (5, 0),  # 自分が裏切り、相手が協力：搾取する
            (1, 1): (1, 1),  # 双方裏切り：共倒れ
        }

    def play_round(self, action1, action2):
        return self.payoff_matrix[(action1, action2)]

class MarineCreature:
    """海洋生物：各戦略が一つの生存哲学を代表する"""

    def __init__(self, name, strategy_type):
        self.name = name
        self.strategy_type = strategy_type
        self.total_payoff = 0
        self.reputation = 0.5  # 信用値（記録のみ。どの戦略もこの値を参照しない）

    def choose_strategy(self, opponent_history, current_round):
        """戦略タイプに基づいてアクションを選択する"""

        if self.strategy_type == "always_cooperate":
            # 善良なサンゴ：常に協力
            # 哲学：理想主義、善意は最終的に報われると信じる
            return 0

        elif self.strategy_type == "always_defect":
            # 利己的なイソギンチャク：常に裏切り
            # 哲学：ホッブズ的現実主義、自己防衛優先
            return 1

        elif self.strategy_type == "tit_for_tat":
            # 賢いクリーナーフィッシュ：しっぺ返し
            # 第一ラウンドは協力、以降は相手の前回の行動を模倣
            # 哲学：互恵の原則、あなたが私にするように私もあなたに
            if current_round == 0 or not opponent_history:
                return 0
            return opponent_history[-1]

        elif self.strategy_type == "tit_for_two_tats":
            # 慎重なクマノミ：ダブルしっぺ返し
            # 相手が二回連続裏切ってから初めて報復
            # 哲学：寛容だが弱くはない
            if len(opponent_history) < 2:
                return 0
            if opponent_history[-1] == 1 and opponent_history[-2] == 1:
                return 1
            return 0

        elif self.strategy_type == "generous_tit_for_tat":
            # 寛大なウミガメ：寛容なしっぺ返し
            # 10%の確率で相手の裏切りを許す
            # 哲学：儒教の恕の道、改過の機会を与える
            if current_round == 0 or not opponent_history:
                return 0
            if opponent_history[-1] == 1:
                return 1 if random.random() > 0.1 else 0
            return 0

        else:  # random
            # ランダムなクラゲ：ランダムに行動
            # 哲学：予測不可能性、混沌の中の生存
            return random.choice([0, 1])

    def update_reputation(self, own_action, opponent_action):
        if own_action == 0:
            self.reputation = min(1.0, self.reputation + 0.01)
        else:
            self.reputation = max(0.0, self.reputation - 0.02)

class MarineEcosystemSimulation:
    """海洋生態系シミュレーション——ゲーム理論の総当たり戦の実験場（六つの固定戦略が各ペア一度ずつ対戦、繁殖も淘汰もなし）"""

    def __init__(self):
        self.game = PrisonersDilemma()
        self.creatures = []
        self.history = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def simulate_interaction(self, c1, c2, rounds=200):
        """二つの生物間の複数ラウンドの相互作用をシミュレーションする"""
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
    """すべてのペアが対戦する"""
    # リセット
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

    # ランキング
    ranked = sorted(ecosystem.creatures,
                    key=lambda x: x.total_payoff, reverse=True)
    return ranked, results

def analyze_winning_traits(strategy):
    """戦略が四つの成功特徴を備えているか分析する（説明用の疑似コード。実行不可：四つの判定関数は未定義）"""
    traits = {
        "善良": not strategy.strikes_first(),
        "報復可能": strategy.punishes_defection(),
        "寛容": strategy.forgives_after_cooperation(),
        "明確": strategy.is_predictable(),
    }
    return traits
    # しっぺ返し：四つすべて満たす
    # 常に協力：善良、寛容、明確だが、報復不可能
    # 常に裏切り：明確なだけ（善良でも寛容でもない。誰に対しても裏切るので、相手への応答ではなく、報復とも言えない）

# | # 報復のサイクル（手書きの説明用トレース。プログラムの出力ではない）
# | round_1: A協力, B協力         -> (3,3)
# | round_2: A協力, B偶発的裏切り -> (0,5) # Bは本当は協力したかったが信号エラー
# | round_3: A報復, B協力         -> (5,0)
# | round_4: A協力, B報復         -> (0,5)
# | # 永遠に報復のサイクルが続く...
# | 
# | # 寛容がサイクルを断つ（これも手書きの説明。10%の確率では、平均して約10回の裏切りに一度しか許さない）
# | round_1: A協力, B協力         -> (3,3)
# | round_2: A協力, B偶発的裏切り -> (0,5)
# | round_3: A許す(10%), B協力   -> (3,3) # 正常な軌道に復帰
