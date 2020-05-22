from enum import Enum


class TerrainType(Enum):
    CITY = "city"
    GRASS = "grass"
    ROAD = "road"
    CHAPEL = "chapel"
    FLOWERS = "flowers"
    UNPLAYABLE = "unplayable"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
