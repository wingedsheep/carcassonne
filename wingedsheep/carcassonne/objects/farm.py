from wingedsheep.carcassonne.objects.farmer_connection_with_coordinate import FarmerConnectionWithCoordinate


class Farm:
    def __init__(self, farmer_connections_with_coordinate: [FarmerConnectionWithCoordinate]):
        self.farmer_connections_with_coordinate: [FarmerConnectionWithCoordinate] = farmer_connections_with_coordinate
