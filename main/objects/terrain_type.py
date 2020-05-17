from enum import Enum


class TerrainType(Enum):
    CITY = "city"
    GRASS = "grass"
    ROAD = "road"
    CHAPEL_OR_FLOWERS = "chapel_or_flowers"
    UNPLAYABLE = "unplayable"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
