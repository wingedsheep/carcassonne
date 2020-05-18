from main.objects.coordinate import Coordinate
from main.objects.farmer_side import FarmerSide
from main.objects.side import Side


class CoordinateWithFarmerSide:

    def __init__(self, coordinate: Coordinate, farmer_side: FarmerSide):
        self.coordinate = coordinate
        self.farmer_side = farmer_side

    def __eq__(self, other):
        return self.coordinate == other.coordinate and self.farmer_side == other.farmer_side

    def __hash__(self):
        return hash((self.coordinate, self.farmer_side))
