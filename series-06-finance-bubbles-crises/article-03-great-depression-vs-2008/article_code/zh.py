# Code & Cogito: 1929大蕭條 vs 2008金融海嘯
# Article: https://code-cogito.com/finance-03/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import matplotlib.pyplot as plt

# ====== 銀行擠兌 Agent-Based 模擬 ======
# 模擬存款人如何根據鄰居行為決定是否提款

class BankRunSimulation:
    def __init__(self, n_depositors=200, reserve_ratio=0.1,
                 panic_threshold=0.3, neighbor_influence=0.6):
        self.n = n_depositors
        self.reserve = reserve_ratio * n_depositors  # 銀行現金儲備
        self.total_deposits = n_depositors            # 每人存款 1 單位
        self.panic_threshold = panic_threshold  # 多少鄰居提款就會恐慌
        self.neighbor_influence = neighbor_influence
        # 0 = 持有, 1 = 已提款
        self.states = [0] * n_depositors
        # 每人隨機抽 5 個「鄰居」（隨機連結，不是真實的社會網絡）
        self.neighbors = [random.sample(range(n_depositors), 5)
                          for _ in range(n_depositors)]

    def step(self):
        new_states = self.states[:]
        for i in range(self.n):
            if self.states[i] == 1:  # 已經提款，跳過
                continue
            # 計算鄰居中已提款的比例
            neighbor_panic = sum(self.states[j] for j in self.neighbors[i])
            panic_ratio = neighbor_panic / len(self.neighbors[i])
            # 如果鄰居恐慌超過門檻，有機率跟著提款
            if panic_ratio >= self.panic_threshold:
                if random.random() < self.neighbor_influence:
                    new_states[i] = 1
                    self.reserve -= 1
            # 即使鄰居不恐慌，也有微小機率自發提款
            elif random.random() < 0.02:
                new_states[i] = 1
                self.reserve -= 1
        self.states = new_states
        bank_alive = self.reserve > 0
        return sum(self.states), bank_alive

# 固定亂數種子，讓結果可以重現
random.seed(42)

# 跑 50 輪模擬
sim = BankRunSimulation(n_depositors=200, reserve_ratio=0.1)
results = []
for t in range(50):
    withdrawn, alive = sim.step()
    results.append({'step': t, 'withdrawn': withdrawn,
                    'pct': withdrawn/200*100, 'alive': alive})
    if not alive:
        print(f"[銀行倒閉] 第 {t} 輪，{withdrawn} 人已提款 "
              f"({withdrawn/200*100:.0f}%)")
        break

# 印出關鍵轉折點
for r in results:
    if r['pct'] in [0] or r['step'] % 5 == 0 or not r['alive']:
        status = "營運中" if r['alive'] else "已倒閉"
        print(f"  第{r['step']:2d}輪: 提款 {r['withdrawn']:3d}人 "
              f"({r['pct']:5.1f}%) | 銀行: {status}")

# | [銀行倒閉] 第 6 輪，21 人已提款 (10%)
# |   第 0輪: 提款   5人 (  2.5%) | 銀行: 營運中
# |   第 5輪: 提款  15人 (  7.5%) | 銀行: 營運中
# |   第 6輪: 提款  21人 ( 10.5%) | 銀行: 已倒閉

# | 資產價格下跌 → 抵押品價值縮水 → 銀行收緊貸款 → 企業無法借到錢
# |     ↑                                                    ↓
# |     ←←←←←← 企業裁員/倒閉 → 消費下降 → 需求萎縮 ←←←←←←←←←
