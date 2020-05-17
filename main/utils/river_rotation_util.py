from typing import Optional, Set

from main.objects.rotation import Rotation
from main.objects.side import Side
from main.objects.tile import Tile
from main.utils.side_modification import opposite, turn_side


def get_connecting_side(previous_river_sides: [Side], river_sides: [Side]) -> Optional[Side]:
    for side in river_sides:
        if opposite(side) in previous_river_sides:
            return side
    return None


def get_river_rotation_tile(previous_tile: Tile, new_tile: Tile):
    previous_river_ends: Set[Side] = set(previous_tile.get_river_ends())
    river_ends: Set[Side] = set(new_tile.get_river_ends())
    return get_river_rotation_ends(previous_river_ends=previous_river_ends, river_ends=river_ends)


def get_river_rotation_ends(previous_river_ends: Set[Side], river_ends: Set[Side]):
    connecting_side: Side = get_connecting_side(previous_river_ends, river_ends)
    non_connecting_side: Side = river_ends.difference([connecting_side]).pop()

    if turn_side(non_connecting_side, 1) == connecting_side:
        return Rotation.CLOCKWISE
    elif turn_side(non_connecting_side, 3) == connecting_side:
        return Rotation.COUNTER_CLOCKWISE
    else:
        return Rotation.NONE
