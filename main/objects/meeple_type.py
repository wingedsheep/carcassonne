from enum import Enum


class MeepleType(Enum):
    NORMAL = "normal"
    ABBOT = "abbot"
    FARMER = "farmer"
    BIG = "big"
    BIG_FARMER = "big_farmer"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
