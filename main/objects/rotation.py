from enum import Enum


class Rotation(Enum):
    CLOCKWISE = "clockwise"
    COUNTER_CLOCKWISE = "counter_clockwise"
    NONE = "none"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value
