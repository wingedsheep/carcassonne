from enum import Enum


class GamePhase(Enum):
    TILES = "tiles"
    MEEPLES = "meeples"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
