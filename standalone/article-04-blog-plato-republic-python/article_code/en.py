# Code & Cogito: Simulating Plato's Republic in Python: When Classical Philosophy Meets Modern Programming
# Article: https://code-cogito.com/en/blog-plato-republic-python-en/
# All the code blocks of the article, in order. Program output is kept as comments.

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class Virtue(Enum):
    """Four virtues -- the system's core metrics"""
    WISDOM = "Wisdom"
    COURAGE = "Courage"
    TEMPERANCE = "Temperance"
    JUSTICE = "Justice"

class SoulPart(Enum):
    """Three parts of the soul -- the internal structure of talent"""
    REASON = "Reason"
    SPIRIT = "Spirit"
    APPETITE = "Appetite"

class SocialClass(Enum):
    """Three social classes -- the system's role definitions"""
    PHILOSOPHER_KING = "Philosopher King"
    AUXILIARY = "Auxiliary"
    PRODUCER = "Producer"

@dataclass
class CitizenAttributes:
    """Citizen attributes -- each person's soul composition"""
    wisdom: float      # Strength of reason (0-1)
    courage: float     # Strength of spirit (0-1)
    temperance: float  # Strength of appetite control (0-1)
    name: str
    age: int

    def dominant_virtue(self) -> Virtue:
        virtues = {
            Virtue.WISDOM: self.wisdom,
            Virtue.COURAGE: self.courage,
            Virtue.TEMPERANCE: self.temperance
        }
        return max(virtues, key=virtues.get)

class Citizen:
    """Citizen of the Republic -- implementing Plato's talent classification"""

    def __init__(self, attributes: CitizenAttributes):
        self.attributes = attributes
        self.social_class = self._determine_class()
        self.soul_harmony = self._calculate_soul_harmony()

    def _determine_class(self) -> SocialClass:
        """Assign social role based on soul structure"""
        attr = self.attributes
        if attr.wisdom > attr.courage and attr.wisdom > attr.temperance:
            return SocialClass.PHILOSOPHER_KING
        elif attr.courage > attr.temperance:
            return SocialClass.AUXILIARY
        else:
            return SocialClass.PRODUCER

    def _calculate_soul_harmony(self) -> float:
        """Soul balance: how close are the three values to each other (evenness)?"""
        total = (self.attributes.wisdom +
                 self.attributes.courage +
                 self.attributes.temperance)
        peak = max(self.attributes.wisdom,
                   self.attributes.courage,
                   self.attributes.temperance)
        balance = 1 - abs(peak - total / 3) / (total / 3)
        return max(0, min(1, balance))

    def contribute(self) -> Dict[str, float]:
        """Contribution to society -- each doing their part"""
        contrib = {"governance": 0, "protection": 0, "production": 0}
        if self.social_class == SocialClass.PHILOSOPHER_KING:
            contrib["governance"] = self.attributes.wisdom * 0.8
        elif self.social_class == SocialClass.AUXILIARY:
            contrib["protection"] = self.attributes.courage * 0.8
        else:
            contrib["production"] = self.attributes.temperance * 0.8
        return contrib

import numpy as np
import random

class Republic:
    """Plato's Republic -- a complete social simulation system"""

    def __init__(self, name: str):
        self.name = name
        self.citizens: List[Citizen] = []
        self.social_harmony = 0.0
        self.justice_level = 0.0

    def add_citizen(self, citizen: Citizen):
        self.citizens.append(citizen)
        self._update_metrics()

    def _update_metrics(self):
        """Update national metrics -- justice and harmony"""
        if not self.citizens:
            return

        # Social harmony = average of individual soul harmonies
        harmonies = [c.soul_harmony for c in self.citizens]
        self.social_harmony = np.mean(harmonies)

        # Justice = how close the class distribution is to the ideal
        dist = self._get_class_distribution()
        ideal = {
            SocialClass.PHILOSOPHER_KING: 0.05,  # 5% (assumed)
            SocialClass.AUXILIARY: 0.20,          # 20% (assumed)
            SocialClass.PRODUCER: 0.75            # 75% (assumed)
        }
        score = 0
        for cls, target in ideal.items():
            actual = dist.get(cls, 0)
            score += max(0, 1 - abs(actual - target) * 2)
        self.justice_level = score / len(ideal)

    def _get_class_distribution(self) -> Dict[SocialClass, float]:
        if not self.citizens:
            return {}
        counts = {}
        for c in self.citizens:
            counts[c.social_class] = counts.get(c.social_class, 0) + 1
        total = len(self.citizens)
        return {k: v / total for k, v in counts.items()}

    def simulate_education(self, years: int = 10):
        """Simulate the education system -- Plato's most valued social mechanism"""
        for year in range(1, years + 1):
            for citizen in self.citizens:
                # Younger people are more receptive to education
                factor = max(0.1, 1 - (citizen.attributes.age - 20) / 100)
                improvement = random.uniform(0.01, 0.05) * factor

                # Two independent draws: wisdom 40%, courage 0.6 x 0.7 = 42%, temperance 0.6 x 0.3 = 18%
                if random.random() < 0.4:
                    citizen.attributes.wisdom = min(
                        1.0, citizen.attributes.wisdom + improvement)
                elif random.random() < 0.7:
                    citizen.attributes.courage = min(
                        1.0, citizen.attributes.courage + improvement)
                else:
                    citizen.attributes.temperance = min(
                        1.0, citizen.attributes.temperance + improvement)

                citizen.soul_harmony = citizen._calculate_soul_harmony()

            self._update_metrics()
