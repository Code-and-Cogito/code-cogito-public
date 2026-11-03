# Code & Cogito: The Great Depression vs the 2008 Financial Crisis
# Article: https://code-cogito.com/en/finance-03-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import matplotlib.pyplot as plt

# ====== Bank Run Agent-Based Simulation ======
# Models how depositors decide to withdraw based on neighbor behavior

class BankRunSimulation:
    def __init__(self, n_depositors=200, reserve_ratio=0.1,
                 panic_threshold=0.3, neighbor_influence=0.6):
        self.n = n_depositors
        self.reserve = reserve_ratio * n_depositors  # Bank cash reserves
        self.total_deposits = n_depositors            # Each person deposits 1 unit
        self.panic_threshold = panic_threshold  # Fraction of panicking neighbors to trigger
        self.neighbor_influence = neighbor_influence
        # 0 = holding, 1 = withdrawn
        self.states = [0] * n_depositors
        # Each person gets 5 randomly drawn "neighbors" (random links, not a real social network)
        self.neighbors = [random.sample(range(n_depositors), 5)
                          for _ in range(n_depositors)]

    def step(self):
        new_states = self.states[:]
        for i in range(self.n):
            if self.states[i] == 1:  # Already withdrawn, skip
                continue
            # Calculate fraction of neighbors who have withdrawn
            neighbor_panic = sum(self.states[j] for j in self.neighbors[i])
            panic_ratio = neighbor_panic / len(self.neighbors[i])
            # If neighbor panic exceeds threshold, probability of withdrawing
            if panic_ratio >= self.panic_threshold:
                if random.random() < self.neighbor_influence:
                    new_states[i] = 1
                    self.reserve -= 1
            # Small spontaneous withdrawal probability even without panic
            elif random.random() < 0.02:
                new_states[i] = 1
                self.reserve -= 1
        self.states = new_states
        bank_alive = self.reserve > 0
        return sum(self.states), bank_alive

# Fix the random seed so the result is reproducible
random.seed(42)

# Run 50 rounds
sim = BankRunSimulation(n_depositors=200, reserve_ratio=0.1)
results = []
for t in range(50):
    withdrawn, alive = sim.step()
    results.append({'step': t, 'withdrawn': withdrawn,
                    'pct': withdrawn/200*100, 'alive': alive})
    if not alive:
        print(f"[BANK FAILURE] Round {t}: {withdrawn} depositors withdrawn "
              f"({withdrawn/200*100:.0f}%)")
        break

# Print key turning points
for r in results:
    if r['pct'] in [0] or r['step'] % 5 == 0 or not r['alive']:
        status = "Operating" if r['alive'] else "FAILED"
        print(f"  Round {r['step']:2d}: Withdrawn {r['withdrawn']:3d} "
              f"({r['pct']:5.1f}%) | Bank: {status}")

# | [BANK FAILURE] Round 6: 21 depositors withdrawn (10%)
# |   Round  0: Withdrawn   5 (  2.5%) | Bank: Operating
# |   Round  5: Withdrawn  15 (  7.5%) | Bank: Operating
# |   Round  6: Withdrawn  21 ( 10.5%) | Bank: FAILED

# | Asset prices fall -> Collateral values shrink -> Banks tighten lending -> Businesses can't borrow
# |     ^                                                                        |
# |     <-------- Businesses lay off / fail -> Spending drops -> Demand contracts <
