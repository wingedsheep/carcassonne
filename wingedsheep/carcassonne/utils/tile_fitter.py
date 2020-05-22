from typing import Set

from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
from wingedsheep.carcassonne.objects.rotation import Rotation
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.objects.tile import Tile
from wingedsheep.carcassonne.utils.river_rotation_util import RiverRotationUtil


class TileFitter:

    @classmethod
    def grass_fits(cls, center: Tile, top: Tile = None, right: Tile = None, bottom: Tile = None,
                   left: Tile = None) -> bool:
        for side in center.grass:
            if side == Side.LEFT and left is not None and not left.grass.__contains__(Side.RIGHT):
                return False
            if side == Side.RIGHT and right is not None and not right.grass.__contains__(Side.LEFT):
                return False
            if side == Side.TOP and top is not None and not top.grass.__contains__(Side.BOTTOM):
                return False
            if side == Side.BOTTOM and bottom is not None and not bottom.grass.__contains__(Side.TOP):
                return False
        return True

    @classmethod
    def cities_fit(cls, center: Tile, top: Tile = None, right: Tile = None, bottom: Tile = None, left: Tile = None) -> bool:
        for side in center.get_city_sides():
            if side == Side.LEFT and left is not None and not left.get_city_sides().__contains__(Side.RIGHT):
                return False
            if side == Side.RIGHT and right is not None and not right.get_city_sides().__contains__(Side.LEFT):
                return False
            if side == Side.TOP and top is not None and not top.get_city_sides().__contains__(Side.BOTTOM):
                return False
            if side == Side.BOTTOM and bottom is not None and not bottom.get_city_sides().__contains__(Side.TOP):
                return False
        return True

    @classmethod
    def roads_fit(cls, center: Tile, top: Tile = None, right: Tile = None, bottom: Tile = None, left: Tile = None) -> bool:
        for side in center.get_road_ends():
            if side == Side.LEFT and left is not None and not left.get_road_ends().__contains__(Side.RIGHT):
                return False
            if side == Side.RIGHT and right is not None and not right.get_road_ends().__contains__(Side.LEFT):
                return False
            if side == Side.TOP and top is not None and not top.get_road_ends().__contains__(Side.BOTTOM):
                return False
            if side == Side.BOTTOM and bottom is not None and not bottom.get_road_ends().__contains__(Side.TOP):
                return False
        return True

    @classmethod
    def rivers_fit(cls, center: Tile, top: Tile = None, right: Tile = None, bottom: Tile = None, left: Tile = None,
                   game_state: CarcassonneGameState = None) -> bool:
        if len(center.get_river_ends()) == 0:
            return True

        connected_side = None
        unconnected_side = None

        for side in center.get_river_ends():
            if side == Side.LEFT and left is not None and left.get_river_ends().__contains__(Side.RIGHT):
                connected_side = Side.LEFT
            if side == Side.RIGHT and right is not None and right.get_river_ends().__contains__(Side.LEFT):
                connected_side = Side.RIGHT
            if side == Side.TOP and top is not None and top.get_river_ends().__contains__(Side.BOTTOM):
                connected_side = Side.TOP
            if side == Side.BOTTOM and bottom is not None and bottom.get_river_ends().__contains__(Side.TOP):
                connected_side = Side.BOTTOM

            if side == Side.LEFT and left is None:
                unconnected_side = Side.LEFT
            if side == Side.RIGHT and right is None:
                unconnected_side = Side.RIGHT
            if side == Side.TOP and top is None:
                unconnected_side = Side.TOP
            if side == Side.BOTTOM and bottom is None:
                unconnected_side = Side.BOTTOM

            if side == Side.LEFT and left is not None and not left.get_river_ends().__contains__(Side.RIGHT):
                return False
            if side == Side.RIGHT and right is not None and not right.get_river_ends().__contains__(Side.LEFT):
                return False
            if side == Side.TOP and top is not None and not top.get_river_ends().__contains__(Side.BOTTOM):
                return False
            if side == Side.BOTTOM and bottom is not None and not bottom.get_river_ends().__contains__(Side.TOP):
                return False

        if connected_side is None:
            return False

        if unconnected_side is not None and game_state.last_river_rotation is not Rotation.NONE and game_state.last_tile_action is not None:
            last_played_tile: Tile = game_state.last_tile_action.tile
            last_played_river_ends: Set[Side] = last_played_tile.get_river_ends()
            river_ends: Set[Side] = {connected_side, unconnected_side}

            rotation: Rotation = RiverRotationUtil.get_river_rotation_ends(previous_river_ends=last_played_river_ends,
                                                                           river_ends=river_ends)
            if rotation == game_state.last_river_rotation:
                return False

        return True

    @classmethod
    def fits(cls, center: Tile, top: Tile = None, right: Tile = None, bottom: Tile = None, left: Tile = None,
             game_state: CarcassonneGameState = None) -> bool:
        if top is None and right is None and bottom is None and left is None:
            return False

        return cls.grass_fits(center, top, right, bottom, left) \
               and cls.cities_fit(center, top, right, bottom, left) \
               and cls.roads_fit(center, top, right, bottom, left) \
               and cls.rivers_fit(center, top, right, bottom, left, game_state)
