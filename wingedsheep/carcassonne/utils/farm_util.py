from typing import Set, Optional

from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
from wingedsheep.carcassonne.objects.coordinate import Coordinate
from wingedsheep.carcassonne.objects.coordinate_with_farmer_side import CoordinateWithFarmerSide
from wingedsheep.carcassonne.objects.coordinate_with_side import CoordinateWithSide
from wingedsheep.carcassonne.objects.farm import Farm
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection
from wingedsheep.carcassonne.objects.farmer_connection_with_coordinate import FarmerConnectionWithCoordinate
from wingedsheep.carcassonne.objects.meeple_position import MeeplePosition
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.objects.tile import Tile
from wingedsheep.carcassonne.utils.side_modification_util import SideModificationUtil


class FarmUtil:

    @classmethod
    def find_farm_by_coordinate(cls, game_state: CarcassonneGameState, position: CoordinateWithSide):
        tile: Tile = game_state.get_tile(position.coordinate.row, position.coordinate.column)

        farmer_connection: FarmerConnection
        for farmer_connection in tile.farms:
            if position.side in farmer_connection.farmer_positions:
                return cls.find_farm(game_state, FarmerConnectionWithCoordinate(farmer_connection, position.coordinate))

    @classmethod
    def find_farm(cls, game_state: CarcassonneGameState, farmer_connection_with_coordinate: FarmerConnectionWithCoordinate) -> Farm:
        farmer_connections_with_coordinate: [FarmerConnectionWithCoordinate] = {farmer_connection_with_coordinate}
        open_sides: Set[CoordinateWithFarmerSide] = set(map(lambda x: CoordinateWithFarmerSide(farmer_connection_with_coordinate.coordinate, x), farmer_connection_with_coordinate.farmer_connection.tile_connections))
        to_explore: Set[CoordinateWithFarmerSide] = set(map(lambda farmer_side: cls.opposite_edge(farmer_side), open_sides))
        to_ignore: Set[CoordinateWithFarmerSide] = open_sides.union(to_explore)

        while len(to_explore) > 0:
            open_edge: CoordinateWithFarmerSide = to_explore.pop()
            to_ignore.add(open_edge)
            new_farmer_connection_with_coordinate: FarmerConnectionWithCoordinate = cls.farm_for_position(game_state, open_edge)
            if new_farmer_connection_with_coordinate is not None:
                farmer_connections_with_coordinate.add(new_farmer_connection_with_coordinate)
                new_open_sides: Set[CoordinateWithFarmerSide] = set(map(lambda x: CoordinateWithFarmerSide(new_farmer_connection_with_coordinate.coordinate, x), new_farmer_connection_with_coordinate.farmer_connection.tile_connections))
                new_to_explore: Set[CoordinateWithFarmerSide] = set(map(lambda farmer_side: cls.opposite_edge(farmer_side), new_open_sides))
                to_ignore = to_ignore.union(new_open_sides)
                new_edge_to_explore: CoordinateWithFarmerSide
                for new_edge_to_explore in new_to_explore:
                    if new_edge_to_explore not in to_ignore:
                        to_explore.add(new_edge_to_explore)
                        to_ignore.add(new_edge_to_explore)

        return Farm(farmer_connections_with_coordinate)

    @classmethod
    def opposite_edge(cls, coordinate_with_farmer_side: CoordinateWithFarmerSide) -> CoordinateWithFarmerSide:
        if coordinate_with_farmer_side.farmer_side.get_side() == Side.TOP:
            return CoordinateWithFarmerSide(
                Coordinate(coordinate_with_farmer_side.coordinate.row - 1,
                           coordinate_with_farmer_side.coordinate.column),
                SideModificationUtil.opposite_farmer_side(coordinate_with_farmer_side.farmer_side)
            )
        elif coordinate_with_farmer_side.farmer_side.get_side() == Side.RIGHT:
            return CoordinateWithFarmerSide(
                Coordinate(coordinate_with_farmer_side.coordinate.row,
                           coordinate_with_farmer_side.coordinate.column + 1),
                SideModificationUtil.opposite_farmer_side(coordinate_with_farmer_side.farmer_side)
            )
        elif coordinate_with_farmer_side.farmer_side.get_side() == Side.BOTTOM:
            return CoordinateWithFarmerSide(
                Coordinate(coordinate_with_farmer_side.coordinate.row + 1,
                           coordinate_with_farmer_side.coordinate.column),
                SideModificationUtil.opposite_farmer_side(coordinate_with_farmer_side.farmer_side)
            )
        elif coordinate_with_farmer_side.farmer_side.get_side() == Side.LEFT:
            return CoordinateWithFarmerSide(
                Coordinate(coordinate_with_farmer_side.coordinate.row,
                           coordinate_with_farmer_side.coordinate.column - 1),
                SideModificationUtil.opposite_farmer_side(coordinate_with_farmer_side.farmer_side)
            )

    @classmethod
    def farm_for_position(cls, game_state: CarcassonneGameState, coordinate_with_farmer_side: CoordinateWithFarmerSide) -> Optional[FarmerConnectionWithCoordinate]:
        tile: Tile = game_state.board[coordinate_with_farmer_side.coordinate.row][coordinate_with_farmer_side.coordinate.column]

        if tile is None:
            return None

        farmer_connection: FarmerConnection
        for farmer_connection in tile.farms:
            if coordinate_with_farmer_side.farmer_side in farmer_connection.tile_connections:
                return FarmerConnectionWithCoordinate(farmer_connection, coordinate_with_farmer_side.coordinate)

        return None

    @classmethod
    def has_meeples(cls, game_state: CarcassonneGameState, farm: Farm) -> bool:
        for meeples in cls.find_meeples(game_state, farm):
            if len(meeples) > 0:
                return True
        return False

    @classmethod
    def find_meeples(cls, game_state: CarcassonneGameState, farm: Farm) -> [[MeeplePosition]]:
        meeples: [[MeeplePosition]] = [[] for _ in range(game_state.players)]

        farmer_connection_with_coordinate: FarmerConnectionWithCoordinate
        for farmer_connection_with_coordinate in farm.farmer_connections_with_coordinate:
            farmer_position: CoordinateWithSide = CoordinateWithSide(farmer_connection_with_coordinate.coordinate, farmer_connection_with_coordinate.farmer_connection.farmer_positions[0])
            for player in range(game_state.players):
                meeple_position: MeeplePosition
                for meeple_position in game_state.placed_meeples[player]:
                    if farmer_position == meeple_position.coordinate_with_side:
                        meeples[player].append(meeple_position)

        return meeples
