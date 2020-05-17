from main.objects.actions.action import Action
from main.objects.coordinate import Coordinate
from main.objects.tile import Tile


class TileAction(Action):
    def __init__(self, tile: Tile, coordinate: Coordinate):
        self.tile = tile
        self.coordinate = coordinate
