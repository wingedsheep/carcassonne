from wingedsheep.carcassonne.objects.actions.action import Action
from wingedsheep.carcassonne.objects.coordinate import Coordinate
from wingedsheep.carcassonne.objects.tile import Tile


class TileAction(Action):
    def __init__(self, tile: Tile, coordinate: Coordinate):
        self.tile = tile
        self.coordinate = coordinate
