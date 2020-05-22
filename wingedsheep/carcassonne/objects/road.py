from wingedsheep.carcassonne.objects.coordinate_with_side import CoordinateWithSide


class Road:
    def __init__(self, road_positions: [CoordinateWithSide], finished: bool):
        self.road_positions = road_positions
        self.finished = finished
