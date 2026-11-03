# Code & Cogito: Pythonでプラトンの理想国をシミュレーションする：古典哲学と現代プログラミングの邂逅
# Article: https://code-cogito.com/ja/blog-plato-republic-python-ja/
# All the code blocks of the article, in order. Program output is kept as comments.

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class Virtue(Enum):
    """四つの美徳——システムのコアメトリクス"""
    WISDOM = "知恵"
    COURAGE = "勇気"
    TEMPERANCE = "節制"
    JUSTICE = "正義"

class SoulPart(Enum):
    """魂の三部分——人材の内的構造"""
    REASON = "理性"
    SPIRIT = "気概"
    APPETITE = "欲望"

class SocialClass(Enum):
    """社会の三階級——システムのロール定義"""
    PHILOSOPHER_KING = "哲人王"
    AUXILIARY = "補助者"
    PRODUCER = "生産者"

@dataclass
class CitizenAttributes:
    """市民の属性——各人の魂の構成"""
    wisdom: float      # 理性の強度 (0-1)
    courage: float     # 気概の強度 (0-1)
    temperance: float  # 節制の強度 (0-1)
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
    """理想国の市民——プラトンの人材分類の実装"""

    def __init__(self, attributes: CitizenAttributes):
        self.attributes = attributes
        self.social_class = self._determine_class()
        self.soul_harmony = self._calculate_soul_harmony()

    def _determine_class(self) -> SocialClass:
        """魂の構造に基づいて社会的役割を決定する"""
        attr = self.attributes
        if attr.wisdom > attr.courage and attr.wisdom > attr.temperance:
            return SocialClass.PHILOSOPHER_KING
        elif attr.courage > attr.temperance:
            return SocialClass.AUXILIARY
        else:
            return SocialClass.PRODUCER

    def _calculate_soul_harmony(self) -> float:
        """魂のバランス度：三つの値がどれだけ近いか（均等さの指標）"""
        total = (self.attributes.wisdom +
                 self.attributes.courage +
                 self.attributes.temperance)
        peak = max(self.attributes.wisdom,
                   self.attributes.courage,
                   self.attributes.temperance)
        balance = 1 - abs(peak - total / 3) / (total / 3)
        return max(0, min(1, balance))

    def contribute(self) -> Dict[str, float]:
        """社会への貢献——各自の職務を全うする"""
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
    """プラトンの理想国——完全な社会シミュレーションシステム"""

    def __init__(self, name: str):
        self.name = name
        self.citizens: List[Citizen] = []
        self.social_harmony = 0.0
        self.justice_level = 0.0

    def add_citizen(self, citizen: Citizen):
        self.citizens.append(citizen)
        self._update_metrics()

    def _update_metrics(self):
        """国家のメトリクスを更新する——正義と調和"""
        if not self.citizens:
            return

        # 社会的調和 = 個人の魂の調和の平均値
        harmonies = [c.soul_harmony for c in self.citizens]
        self.social_harmony = np.mean(harmonies)

        # 正義 = 階級比率が理想値に近いか
        dist = self._get_class_distribution()
        ideal = {
            SocialClass.PHILOSOPHER_KING: 0.05,  # 5%（仮定値）
            SocialClass.AUXILIARY: 0.20,          # 20%（仮定値）
            SocialClass.PRODUCER: 0.75            # 75%（仮定値）
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
        """教育システムのシミュレーション——プラトンが最も重視した社会メカニズム"""
        for year in range(1, years + 1):
            for citizen in self.citizens:
                # 若者ほど教育の影響を受けやすい
                factor = max(0.1, 1 - (citizen.attributes.age - 20) / 100)
                improvement = random.uniform(0.01, 0.05) * factor

                # 二回の独立した抽選：知恵40%、勇気 0.6×0.7 = 42%、節制 0.6×0.3 = 18%
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
