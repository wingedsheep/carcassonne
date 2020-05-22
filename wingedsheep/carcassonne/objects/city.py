from wingedsheep.carcassonne.objects.coordinate_with_side import CoordinateWithSide


class City:
    def __init__(self, city_positions: [CoordinateWithSide], finished: bool):
        self.city_positions = city_positions
        self.finished = finished
