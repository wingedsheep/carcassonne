from enum import Enum


class Side(Enum):
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"
    CENTER = "center"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
