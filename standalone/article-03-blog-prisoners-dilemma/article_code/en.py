# Code & Cogito: Simulating the Prisoner's Dilemma in Python: From Marine Ecology to Game Theory Philosophy
# Article: https://code-cogito.com/en/blog-prisoners-dilemma-en/
# All the code blocks of the article, in order. Program output is kept as comments.

import random
import numpy as np

class PrisonersDilemma:
    """Prisoner's dilemma game engine"""

    def __init__(self):
        # Payoff matrix: (player1 payoff, player2 payoff)
        # 0 = cooperate, 1 = defect
        self.payoff_matrix = {
            (0, 0): (3, 3),  # Both cooperate: mutual benefit
            (0, 1): (0, 5),  # I cooperate, opponent defects: I get exploited
            (1, 0): (5, 0),  # I defect, opponent cooperates: I take advantage
            (1, 1): (1, 1),  # Both defect: mutual loss
        }

    def play_round(self, action1, action2):
        return self.payoff_matrix[(action1, action2)]

class MarineCreature:
    """Marine creature: each strategy represents a survival philosophy"""

    def __init__(self, name, strategy_type):
        self.name = name
        self.strategy_type = strategy_type
        self.total_payoff = 0
        self.reputation = 0.5  # Reputation score (recorded only; no strategy reads it)

    def choose_strategy(self, opponent_history, current_round):
        """Choose action based on strategy type"""

        if self.strategy_type == "always_cooperate":
            # Gentle Coral: always cooperate
            # Philosophy: idealism, believing goodwill pays off eventually
            return 0

        elif self.strategy_type == "always_defect":
            # Selfish Anemone: always defect
            # Philosophy: Hobbesian realism, self-preservation first
            return 1

        elif self.strategy_type == "tit_for_tat":
            # Clever Cleaner Fish: tit for tat
            # Cooperate first, then mirror opponent's last move
            # Philosophy: reciprocity -- treat others as they treat you
            if current_round == 0 or not opponent_history:
                return 0
            return opponent_history[-1]

        elif self.strategy_type == "tit_for_two_tats":
            # Cautious Clownfish: tit for two tats
            # Only retaliate after two consecutive defections
            # Philosophy: forgiving but not weak
            if len(opponent_history) < 2:
                return 0
            if opponent_history[-1] == 1 and opponent_history[-2] == 1:
                return 1
            return 0

        elif self.strategy_type == "generous_tit_for_tat":
            # Forgiving Turtle: generous tit for tat
            # 10% chance of forgiving a defection
            # Philosophy: the Confucian principle of shu -- give others
            # a chance to change
            if current_round == 0 or not opponent_history:
                return 0
            if opponent_history[-1] == 1:
                return 1 if random.random() > 0.1 else 0
            return 0

        else:  # random
            # Random Jellyfish: random action
            # Philosophy: unpredictability, survival through chaos
            return random.choice([0, 1])

    def update_reputation(self, own_action, opponent_action):
        if own_action == 0:
            self.reputation = min(1.0, self.reputation + 0.01)
        else:
            self.reputation = max(0.0, self.reputation - 0.02)

class MarineEcosystemSimulation:
    """Marine ecosystem simulation -- a round-robin tournament for game theory (six fixed strategies, each pair plays once, no reproduction or selection)"""

    def __init__(self):
        self.game = PrisonersDilemma()
        self.creatures = []
        self.history = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def simulate_interaction(self, c1, c2, rounds=200):
        """Simulate a multi-round interaction between two creatures"""
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
    """Every pair of creatures competes"""
    # Reset
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

    # Rankings
    ranked = sorted(ecosystem.creatures,
                    key=lambda x: x.total_payoff, reverse=True)
    return ranked, results

def analyze_winning_traits(strategy):
    """Analyze whether a strategy has the four winning traits (sketch, not runnable: the four predicates are not defined)"""
    traits = {
        "Nice": not strategy.strikes_first(),
        "Retaliatory": strategy.punishes_defection(),
        "Forgiving": strategy.forgives_after_cooperation(),
        "Clear": strategy.is_predictable(),
    }
    return traits
    # Tit for tat: all four satisfied
    # Always cooperate: nice, forgiving, clear, but not retaliatory
    # Always defect: clear only (not nice, not forgiving; it never responds to the opponent, so it is not retaliatory in the reciprocal sense)

# | # Retaliation spiral (hand-written illustration, not program output)
# | round_1: A cooperates, B cooperates        -> (3,3)
# | round_2: A cooperates, B accidentally defects -> (0,5) # B meant to cooperate, signal error
# | round_3: A retaliates, B cooperates        -> (5,0)
# | round_4: A cooperates, B retaliates        -> (0,5)
# | # Trapped in a retaliation loop forever...
# | 
# | # Forgiveness breaks the cycle (also hand-written; at a 10% rate it takes about 10 defections on average before one is forgiven)
# | round_1: A cooperates, B cooperates        -> (3,3)
# | round_2: A cooperates, B accidentally defects -> (0,5)
# | round_3: A forgives (10%), B cooperates    -> (3,3) # Back on track
