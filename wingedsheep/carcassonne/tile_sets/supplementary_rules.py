from enum import Enum


class SupplementaryRule(Enum):
    FARMERS = "farmers"
    ABBOTS = "abbots"
    NORMAL_MEEPLES_CAN_USE_FLOWERS = "normal_meeples_can_use_flowers"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
