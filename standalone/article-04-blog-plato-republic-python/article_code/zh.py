# Code & Cogito: 用 Python 模擬柏拉圖的理想國：當古典哲學遇見現代程式設計
# Article: https://code-cogito.com/blog-plato-republic-python/
# All the code blocks of the article, in order. Program output is kept as comments.

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class Virtue(Enum):
    """四種美德——系統的核心指標"""
    WISDOM = "智慧"
    COURAGE = "勇氣"
    TEMPERANCE = "節制"
    JUSTICE = "正義"

class SoulPart(Enum):
    """靈魂三部分——人才的內在結構"""
    REASON = "理性"
    SPIRIT = "意氣"
    APPETITE = "慾望"

class SocialClass(Enum):
    """社會三階級——系統的角色定義"""
    PHILOSOPHER_KING = "哲學家王"
    AUXILIARY = "輔助者"
    PRODUCER = "生產者"

@dataclass
class CitizenAttributes:
    """公民屬性——每個人的靈魂組成"""
    wisdom: float      # 理性的強度 (0-1)
    courage: float     # 意氣的強度 (0-1)
    temperance: float  # 節制的強度 (0-1)
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
    """理想國公民——柏拉圖人才分類的實作"""

    def __init__(self, attributes: CitizenAttributes):
        self.attributes = attributes
        self.social_class = self._determine_class()
        self.soul_harmony = self._calculate_soul_harmony()

    def _determine_class(self) -> SocialClass:
        """根據靈魂結構決定社會角色"""
        attr = self.attributes
        if attr.wisdom > attr.courage and attr.wisdom > attr.temperance:
            return SocialClass.PHILOSOPHER_KING
        elif attr.courage > attr.temperance:
            return SocialClass.AUXILIARY
        else:
            return SocialClass.PRODUCER

    def _calculate_soul_harmony(self) -> float:
        """靈魂平衡度：三個數值是否接近（衡量均勻程度）"""
        total = (self.attributes.wisdom +
                 self.attributes.courage +
                 self.attributes.temperance)
        peak = max(self.attributes.wisdom,
                   self.attributes.courage,
                   self.attributes.temperance)
        balance = 1 - abs(peak - total / 3) / (total / 3)
        return max(0, min(1, balance))

    def contribute(self) -> Dict[str, float]:
        """對社會的貢獻——各司其職"""
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
    """柏拉圖的理想國——一個完整的社會模擬系統"""

    def __init__(self, name: str):
        self.name = name
        self.citizens: List[Citizen] = []
        self.social_harmony = 0.0
        self.justice_level = 0.0

    def add_citizen(self, citizen: Citizen):
        self.citizens.append(citizen)
        self._update_metrics()

    def _update_metrics(self):
        """更新國家指標——正義與和諧"""
        if not self.citizens:
            return

        # 社會和諧 = 個體靈魂和諧的平均值
        harmonies = [c.soul_harmony for c in self.citizens]
        self.social_harmony = np.mean(harmonies)

        # 正義 = 階級比例是否接近理想值
        dist = self._get_class_distribution()
        ideal = {
            SocialClass.PHILOSOPHER_KING: 0.05,  # 5%（假設值）
            SocialClass.AUXILIARY: 0.20,          # 20%（假設值）
            SocialClass.PRODUCER: 0.75            # 75%（假設值）
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
        """模擬教育系統——柏拉圖最重視的社會機制"""
        for year in range(1, years + 1):
            for citizen in self.citizens:
                # 年輕人更容易接受教育
                factor = max(0.1, 1 - (citizen.attributes.age - 20) / 100)
                improvement = random.uniform(0.01, 0.05) * factor

                # 兩次獨立抽籤：智慧 40%、勇氣 0.6×0.7 = 42%、節制 0.6×0.3 = 18%
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
