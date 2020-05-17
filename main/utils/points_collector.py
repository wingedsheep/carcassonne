import json
from typing import Set

import numpy as np

from main.carcassonne_game_state import CarcassonneGameState
from main.objects.city import City
from main.objects.coordinate import Coordinate
from main.objects.coordinate_with_side import CoordinateWithSide
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.objects.road import Road
from main.objects.side import Side
from main.objects.terrain_type import TerrainType
from main.objects.tile import Tile
from main.utils.city_util import CityUtil
from main.utils.meeple_util import MeepleUtil
from main.utils.road_util import RoadUtil


class PointsCollector:

    def __init__(self, city_util: CityUtil, road_util: RoadUtil, meeple_util: MeepleUtil):
        self.city_util = city_util
        self.road_util = road_util
        self.meeple_util = meeple_util

    def remove_meeples_and_collect_points(self, game_state: CarcassonneGameState, last_played_coordinate: Coordinate):

        # Points for finished cities
        cities: [City] = self.city_util.find_cities(game_state=game_state, coordinate=last_played_coordinate)
        for city in cities:
            if city.finished:
                meeples: [[MeeplePosition]] = self.city_util.find_meeples(game_state=game_state, city=city)
                meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                print("City finished. Meeples:", json.dumps(meeple_counts_per_player))
                winning_player = self.get_winning_player(meeple_counts_per_player)
                if winning_player is not None:
                    game_state.scores[winning_player] += self.count_city_points(game_state=game_state, city=city)
                self.remove_meeples(game_state=game_state, meeples=meeples)

        # Points for finished roads
        roads: [Road] = self.road_util.find_roads(game_state=game_state, coordinate=last_played_coordinate)
        for road in roads:
            if road.finished:
                meeples: [[MeeplePosition]] = self.road_util.find_meeples(game_state=game_state, road=road)
                meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                print("Road finished. Meeples:", json.dumps(meeple_counts_per_player))
                winning_player = self.get_winning_player(meeple_counts_per_player)
                if winning_player is not None:
                    game_state.scores[winning_player] += self.count_road_points(game_state=game_state, road=road)
                self.remove_meeples(game_state=game_state, meeples=meeples)

        # Points for finished chapels
        for row in range(last_played_coordinate.row - 1, last_played_coordinate.row + 2):
            for column in range(last_played_coordinate.column - 1, last_played_coordinate.column + 2):
                tile: Tile = game_state.board[row][column]

                if tile is None:
                    continue

                coordinate = Coordinate(row=row, column=column)
                coordinate_with_side = CoordinateWithSide(coordinate=coordinate, side=Side.CENTER)
                meeple_of_player = self.meeple_util.position_contains_meeple(game_state=game_state,
                                                                             coordinate_with_side=coordinate_with_side)
                if tile.chapel_or_flowers and meeple_of_player is not None:
                    points = self.chapel_or_flowers_points(game_state=game_state, coordinate=coordinate)
                    if points == 9:
                        print("Chapel or flowers finished for player", str(meeple_of_player))
                        game_state.scores[meeple_of_player] += points

                        meeples_per_player = []
                        for _ in range(game_state.players):
                            meeples_per_player.append([])
                        meeples_per_player[meeple_of_player].append(coordinate_with_side)

                        self.remove_meeples(game_state=game_state, meeples=meeples_per_player)

    def get_winning_player(self, meeple_counts_per_player: [int]):
        winners = np.argwhere(meeple_counts_per_player == np.amax(meeple_counts_per_player))
        if len(winners) == 1:
            return int(winners[0])
        else:
            return None

    def count_city_points(self, game_state: CarcassonneGameState, city: City):
        points = 0
        cathedral_points = 0
        has_cathedral = False

        coordinates: Set[Coordinate] = set()
        position: CoordinateWithSide
        for position in city.city_positions:
            coordinate: Coordinate = position.coordinate
            coordinates.add(coordinate)

        tiles: [Tile] = list(map(lambda x: game_state.board[x.row][x.column], coordinates))

        tile: Tile
        for tile in tiles:
            if tile.shield:
                points += 4
                cathedral_points += 2
            else:
                points += 2
                cathedral_points += 2
            if tile.cathedral:
                has_cathedral = True

        if has_cathedral:
            return points + cathedral_points
        else:
            return points

    def count_road_points(self, game_state: CarcassonneGameState, road: Road):
        points = 0
        has_inn = False

        coordinates: Set[Coordinate] = set()
        position: CoordinateWithSide
        for position in road.road_positions:
            coordinate: Coordinate = position.coordinate
            tile: Tile = game_state.board[coordinate.row][coordinate.column]
            if tile.inn:
                has_inn = True
            coordinates.add(coordinate)

        tiles: [Tile] = list(map(lambda x: game_state.board[x.row][x.column], coordinates))

        tile: Tile
        for _ in tiles:
            points += 1
            if has_inn:
                points += 1

        return points

    def remove_meeples(self, game_state: CarcassonneGameState, meeples: [[MeeplePosition]]):
        for player, meeple_positions in enumerate(meeples):
            meeple_position: MeeplePosition
            for meeple_position in meeple_positions:
                game_state.placed_meeples[player].remove(meeple_position)
                if meeple_position.meeple_type == MeepleType.NORMAL or meeple_position.meeple_type == MeepleType.FARMER:
                    game_state.meeples[player] += 1
                elif meeple_position.meeple_type == MeepleType.ABBOT:
                    game_state.abbots[player] += 1
                elif meeple_position.meeple_type == MeepleType.BIG or meeple_position.meeple_type == MeepleType.BIG_FARMER:
                    game_state.big_meeples[player] += 1

    def chapel_or_flowers_points(self, game_state: CarcassonneGameState, coordinate: Coordinate):
        points = 0
        for row in range(coordinate.row - 1, coordinate.row + 2):
            for column in range(coordinate.column - 1, coordinate.column + 2):
                tile: Tile = game_state.board[row][column]
                if tile is not None:
                    points += 1
        return points

    def count_final_scores(self, game_state: CarcassonneGameState):
        for player, placed_meeples in enumerate(game_state.placed_meeples):
            meeple_position: MeeplePosition
            for meeple_position in placed_meeples:
                tile: Tile = game_state.board[meeple_position.coordinate_with_side.coordinate.row][
                    meeple_position.coordinate_with_side.coordinate.column]
                type: TerrainType = tile.get_type(meeple_position.coordinate_with_side.side)

                if type == TerrainType.CITY:
                    city: City = self.city_util.find_city(game_state=game_state,
                                                          city_position=meeple_position.coordinate_with_side)
                    meeples: [CoordinateWithSide] = self.city_util.find_meeples(game_state=game_state, city=city)
                    meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                    print("Collecting points for unfinished city. Meeples:", json.dumps(meeple_counts_per_player))
                    winning_player = self.get_winning_player(meeple_counts_per_player)
                    if winning_player is not None:
                        game_state.scores[winning_player] += self.count_city_points(game_state=game_state, city=city)
                    self.remove_meeples(game_state=game_state, meeples=meeples)
                    continue

                if type == TerrainType.ROAD:
                    road: [Road] = self.road_util.find_road(game_state=game_state,
                                                            road_position=meeple_position.coordinate_with_side)
                    meeples: [CoordinateWithSide] = self.road_util.find_meeples(game_state=game_state, road=road)
                    meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                    print("Collecting points for unfinished road. Meeples:", json.dumps(meeple_counts_per_player))
                    winning_player = self.get_winning_player(meeple_counts_per_player)
                    if winning_player is not None:
                        game_state.scores[winning_player] += self.count_road_points(game_state=game_state, road=road)
                    self.remove_meeples(game_state=game_state, meeples=meeples)
                    continue

                if type == TerrainType.CHAPEL_OR_FLOWERS:
                    points = self.chapel_or_flowers_points(game_state=game_state,
                                                           coordinate=meeple_position.coordinate_with_side.coordinate)
                    print("Collecting points for unfinished chapel or flowers for player", str(player))
                    game_state.scores[player] += points

                    meeples_per_player = []
                    for _ in range(game_state.players):
                        meeples_per_player.append([])
                    meeples_per_player[player].append(meeple_position)

                    self.remove_meeples(game_state=game_state, meeples=meeples_per_player)
                    continue

                print("Collecting points for unknown type", type)

    def get_meeple_counts_per_player(self, meeples):
        meeple_counts_per_player = list(
            map(
                lambda x:
                sum(list(map(
                    lambda y: 2 if y.meeple_type == MeepleType.BIG or y.meeple_type == MeepleType.BIG_FARMER else 1, x
                ))),
                meeples
            )
        )
        return meeple_counts_per_player
