from main.carcassonne_game_state import CarcassonneGameState
from main.objects.actions.tile_action import TileAction
from main.objects.coordinate import Coordinate
from main.objects.coordinate_with_side import CoordinateWithSide
from main.objects.actions.meeple_action import MeepleAction
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.objects.side import Side
from main.objects.terrain_type import TerrainType
from main.objects.tile import Tile
from main.utils.city_util import CityUtil
from main.utils.road_util import RoadUtil

city_util: CityUtil = CityUtil()
road_util: RoadUtil = RoadUtil()


class PossibleMoveFinder:

    @staticmethod
    def possible_meeple_actions(game_state: CarcassonneGameState) -> [MeepleAction]:
        current_player = game_state.current_player
        last_tile_action: TileAction = game_state.last_tile_action
        last_played_tile: Tile = last_tile_action.tile
        last_played_position: Coordinate = last_tile_action.coordinate

        possible_actions: [MeepleAction] = []

        meeple_positions = PossibleMoveFinder.__possible_meeple_positions(game_state=game_state)

        if game_state.meeples[current_player] > 0:
            possible_actions.extend(list(
                map(lambda x: MeepleAction(meeple_type=MeepleType.NORMAL, coordinate_with_side=x), meeple_positions)))

        if game_state.big_meeples[current_player] > 0:
            possible_actions.extend(
                list(map(lambda x: MeepleAction(meeple_type=MeepleType.BIG, coordinate_with_side=x), meeple_positions)))

        if game_state.abbots[current_player] > 0:
            if last_played_tile.chapel_or_flowers:
                possible_actions.append(MeepleAction(meeple_type=MeepleType.ABBOT,
                                                     coordinate_with_side=CoordinateWithSide(
                                                         coordinate=last_played_position, side=Side.CENTER)))

        placed_meeple: MeeplePosition
        for placed_meeple in game_state.placed_meeples[current_player]:
            if placed_meeple.meeple_type == MeepleType.ABBOT:
                possible_actions.append(
                    MeepleAction(meeple_type=MeepleType.ABBOT, coordinate_with_side=placed_meeple.coordinate_with_side,
                                 remove=True))

        return possible_actions

    @staticmethod
    def __possible_meeple_positions(game_state: CarcassonneGameState) -> [CoordinateWithSide]:
        playing_positions: [CoordinateWithSide] = []
        last_tile_action: TileAction = game_state.last_tile_action
        last_played_tile: Tile = last_tile_action.tile
        last_played_position: Coordinate = last_tile_action.coordinate

        if last_played_tile.chapel_or_flowers:
            playing_positions.append(CoordinateWithSide(coordinate=last_played_position, side=Side.CENTER))

        for side in [Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]:
            if last_played_tile.get_type(side) == TerrainType.CITY:
                connected_cities = city_util.find_city(
                    game_state,
                    CoordinateWithSide(coordinate=last_played_position, side=side)
                )
                if city_util.city_contains_meeples(game_state, connected_cities):
                    continue
                else:
                    playing_positions.append(CoordinateWithSide(coordinate=last_played_position, side=side))

            if last_played_tile.get_type(side) == TerrainType.ROAD:
                connected_roads = road_util.find_road(
                    game_state,
                    CoordinateWithSide(coordinate=last_played_position, side=side)
                )
                if road_util.road_contains_meeples(game_state, connected_roads):
                    continue
                else:
                    playing_positions.append(CoordinateWithSide(coordinate=last_played_position, side=side))

        return playing_positions
