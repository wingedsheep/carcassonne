from wingedsheep.carcassonne.objects.coordinate import Coordinate
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection


class FarmerConnectionWithCoordinate:
    def __init__(self, farmer_connection: FarmerConnection, coordinate: Coordinate = ()):
        self.farmer_connection: FarmerConnection = farmer_connection
        self.coordinate: Coordinate = coordinate

    def __eq__(self, other):
        return self.farmer_connection == other.farmer_connection \
               and self.coordinate == other.coordinate

    def __hash__(self):
        return hash((self.farmer_connection, self.coordinate))
