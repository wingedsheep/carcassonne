from enum import Enum


class TileSet(Enum):
    BASE = "base"
    THE_RIVER = "the_river"
    INNS_AND_CATHEDRALS = "inns_and_cathedrals"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
