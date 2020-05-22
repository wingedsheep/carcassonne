import json

from wingedsheep.carcassonne.objects.coordinate import Coordinate


class PlayingPosition:
    def __init__(self, coordinate: Coordinate, turns: int):
        self.coordinate = coordinate
        self.turns = turns

    def to_json(self):
        return {
            "coordinate": self.coordinate,
            "turns": self.turns
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)
