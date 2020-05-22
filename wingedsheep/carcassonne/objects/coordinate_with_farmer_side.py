from wingedsheep.carcassonne.objects.coordinate import Coordinate
from wingedsheep.carcassonne.objects.farmer_side import FarmerSide


class CoordinateWithFarmerSide:

    def __init__(self, coordinate: Coordinate, farmer_side: FarmerSide):
        self.coordinate = coordinate
        self.farmer_side = farmer_side

    def __eq__(self, other):
        return self.coordinate == other.coordinate and self.farmer_side == other.farmer_side

    def __hash__(self):
        return hash((self.coordinate, self.farmer_side))
