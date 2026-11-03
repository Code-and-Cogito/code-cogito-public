# Code & Cogito: 1929年大恐慌 vs 2008年リーマン・ショック
# Article: https://code-cogito.com/ja/finance-03-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import matplotlib.pyplot as plt

# ====== 銀行取り付け騒ぎ Agent-Based シミュレーション ======
# 預金者が近隣者の行動に基づいて引き出しを決定するモデル

class BankRunSimulation:
    def __init__(self, n_depositors=200, reserve_ratio=0.1,
                 panic_threshold=0.3, neighbor_influence=0.6):
        self.n = n_depositors
        self.reserve = reserve_ratio * n_depositors  # 銀行の現金準備
        self.total_deposits = n_depositors            # 各人が1単位を預金
        self.panic_threshold = panic_threshold  # パニック発動の閾値
        self.neighbor_influence = neighbor_influence
        # 0 = 保有中, 1 = 引き出し済み
        self.states = [0] * n_depositors
        # 各人にランダムに5人の「近隣者」を割り当てる（ランダムな結びつきで、現実の社会ネットワークではない）
        self.neighbors = [random.sample(range(n_depositors), 5)
                          for _ in range(n_depositors)]

    def step(self):
        new_states = self.states[:]
        for i in range(self.n):
            if self.states[i] == 1:  # 既に引き出し済み、スキップ
                continue
            # 近隣者のうち引き出し済みの割合を計算
            neighbor_panic = sum(self.states[j] for j in self.neighbors[i])
            panic_ratio = neighbor_panic / len(self.neighbors[i])
            # 近隣者のパニックが閾値を超えたら、引き出す確率
            if panic_ratio >= self.panic_threshold:
                if random.random() < self.neighbor_influence:
                    new_states[i] = 1
                    self.reserve -= 1
            # パニックがなくても微小な自発的引き出し確率
            elif random.random() < 0.02:
                new_states[i] = 1
                self.reserve -= 1
        self.states = new_states
        bank_alive = self.reserve > 0
        return sum(self.states), bank_alive

# 乱数シードを固定して、結果を再現できるようにする
random.seed(42)

# 50ラウンド実行
sim = BankRunSimulation(n_depositors=200, reserve_ratio=0.1)
results = []
for t in range(50):
    withdrawn, alive = sim.step()
    results.append({'step': t, 'withdrawn': withdrawn,
                    'pct': withdrawn/200*100, 'alive': alive})
    if not alive:
        print(f"[銀行破綻] 第{t}ラウンド: {withdrawn}人が引き出し "
              f"({withdrawn/200*100:.0f}%)")
        break

# 重要な転換点を表示
for r in results:
    if r['pct'] in [0] or r['step'] % 5 == 0 or not r['alive']:
        status = "営業中" if r['alive'] else "破綻"
        print(f"  第{r['step']:2d}ラウンド: 引き出し {r['withdrawn']:3d}人 "
              f"({r['pct']:5.1f}%) | 銀行: {status}")

# | [銀行破綻] 第6ラウンド: 21人が引き出し (10%)
# |   第 0ラウンド: 引き出し   5人 (  2.5%) | 銀行: 営業中
# |   第 5ラウンド: 引き出し  15人 (  7.5%) | 銀行: 営業中
# |   第 6ラウンド: 引き出し  21人 ( 10.5%) | 銀行: 破綻

# | 資産価格下落 → 担保価値の縮小 → 銀行が融資を引き締め → 企業が資金を借りられない
# |     ↑                                                           ↓
# |     ←←←←←← 企業がリストラ/倒産 → 消費減少 → 需要縮小 ←←←←←←←←←
