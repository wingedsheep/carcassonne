from enum import Enum

from wingedsheep.carcassonne.objects.side import Side


class FarmerSide(Enum):
    TLL = "tll"
    TLT = "tlt"
    TRT = "trt"
    TRR = "trr"
    BLL = "bll"
    BLB = "blb"
    BRB = "brb"
    BRR = "brr"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value

    def get_side(self) -> Side:
        if self.value[2] == "l":
            return Side.LEFT
        if self.value[2] == "r":
            return Side.RIGHT
        if self.value[2] == "b":
            return Side.BOTTOM
        if self.value[2] == "t":
            return Side.TOP
