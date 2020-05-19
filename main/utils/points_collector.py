import json
from typing import Set

import numpy as np

from main.carcassonne_game_state import CarcassonneGameState
from main.objects.city import City
from main.objects.coordinate import Coordinate
from main.objects.coordinate_with_side import CoordinateWithSide
from main.objects.farm import Farm
from main.objects.farmer_connection_with_coordinate import FarmerConnectionWithCoordinate
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.objects.road import Road
from main.objects.side import Side
from main.objects.terrain_type import TerrainType
from main.objects.tile import Tile
from main.utils.city_util import CityUtil
from main.utils.farm_util import FarmUtil
from main.utils.meeple_util import MeepleUtil
from main.utils.road_util import RoadUtil


class PointsCollector:

    def __init__(self, city_util: CityUtil, road_util: RoadUtil, meeple_util: MeepleUtil):
        self.city_util = city_util
        self.road_util = road_util
        self.meeple_util = meeple_util

    def remove_meeples_and_collect_points(self, game_state: CarcassonneGameState, coordinate: Coordinate):

        # Points for finished cities
        cities: [City] = self.city_util.find_cities(game_state=game_state, coordinate=coordinate)
        for city in cities:
            if city.finished:
                meeples: [[MeeplePosition]] = self.city_util.find_meeples(game_state=game_state, city=city)
                meeple_counts_per_player = PointsCollector.get_meeple_counts_per_player(meeples)
                print("City finished. Meeples:", json.dumps(meeple_counts_per_player))
                if sum(meeple_counts_per_player) == 0:
                    continue
                winning_player = PointsCollector.get_winning_player(meeple_counts_per_player)
                if winning_player is not None:
                    points = PointsCollector.count_city_points(game_state=game_state, city=city)
                    print(points, "points for player", winning_player)
                    game_state.scores[winning_player] += points
                self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples)

        # Points for finished roads
        roads: [Road] = self.road_util.find_roads(game_state=game_state, coordinate=coordinate)
        for road in roads:
            if road.finished:
                meeples: [[MeeplePosition]] = self.road_util.find_meeples(game_state=game_state, road=road)
                meeple_counts_per_player = PointsCollector.get_meeple_counts_per_player(meeples)
                print("Road finished. Meeples:", json.dumps(meeple_counts_per_player))
                if sum(meeple_counts_per_player) == 0:
                    continue
                winning_player = PointsCollector.get_winning_player(meeple_counts_per_player)
                if winning_player is not None:
                    points = PointsCollector.count_road_points(game_state=game_state, road=road)
                    print(points, "points for player", winning_player)
                    game_state.scores[winning_player] += points
                self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples)

        # Points for finished chapels
        for row in range(coordinate.row - 1, coordinate.row + 2):
            for column in range(coordinate.column - 1, coordinate.column + 2):
                tile: Tile = game_state.get_tile(row, column)

                if tile is None:
                    continue

                coordinate = Coordinate(row=row, column=column)
                coordinate_with_side = CoordinateWithSide(coordinate=coordinate, side=Side.CENTER)
                meeple_of_player = self.meeple_util.position_contains_meeple(game_state=game_state,
                                                                             coordinate_with_side=coordinate_with_side)
                if tile.chapel_or_flowers and meeple_of_player is not None:
                    points = PointsCollector.chapel_or_flowers_points(game_state=game_state, coordinate=coordinate)
                    if points == 9:
                        print("Chapel or flowers finished for player", str(meeple_of_player))
                        print(points, "points for player", meeple_of_player)
                        game_state.scores[meeple_of_player] += points

                        meeples_per_player = []
                        for _ in range(game_state.players):
                            meeples_per_player.append([])
                        meeples_per_player[meeple_of_player].append(coordinate_with_side)

                        self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples_per_player)

    @staticmethod
    def get_winning_player(meeple_counts_per_player: [int]):
        winners = np.argwhere(meeple_counts_per_player == np.amax(meeple_counts_per_player))
        if len(winners) == 1:
            return int(winners[0])
        else:
            return None

    @staticmethod
    def count_city_points(game_state: CarcassonneGameState, city: City):
        points = 0
        has_cathedral = False

        coordinates: Set[Coordinate] = set()
        position: CoordinateWithSide
        for position in city.city_positions:
            coordinate: Coordinate = position.coordinate
            tile: Tile = game_state.board[coordinate.row][coordinate.column]
            if tile.inn:
                has_cathedral = True
            coordinates.add(coordinate)

        tiles: [Tile] = list(map(lambda x: game_state.board[x.row][x.column], coordinates))

        if not city.finished and has_cathedral:
            return 0

        tile: Tile
        for tile in tiles:
            if tile.shield:
                if has_cathedral:
                    points += 6
                else:
                    points += 4 if city.finished else 2
            else:
                if has_cathedral:
                    points += 3
                else:
                    points += 2 if city.finished else 1

        return points

    @staticmethod
    def count_road_points(game_state: CarcassonneGameState, road: Road):
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

        if not road.finished and has_inn:
            return 0

        tile: Tile
        for _ in tiles:
            if has_inn:
                points += 2
            else:
                points += 1

        return points

    @staticmethod
    def chapel_or_flowers_points(game_state: CarcassonneGameState, coordinate: Coordinate):
        points = 0
        for row in range(coordinate.row - 1, coordinate.row + 2):
            for column in range(coordinate.column - 1, coordinate.column + 2):
                tile: Tile = game_state.board[row][column]
                if tile is not None:
                    points += 1
        return points

    def count_final_scores(self, game_state: CarcassonneGameState):
        for player, placed_meeples in enumerate(game_state.placed_meeples):

            # TODO also remove meeples from meeples_to_remove, when there are multiple

            meeples_to_remove: Set[MeeplePosition] = set(placed_meeples)
            while len(meeples_to_remove) > 0:
                meeple_position: MeeplePosition = meeples_to_remove.pop()

                tile: Tile = game_state.board[meeple_position.coordinate_with_side.coordinate.row][
                    meeple_position.coordinate_with_side.coordinate.column]

                terrrain_type: TerrainType = tile.get_type(meeple_position.coordinate_with_side.side)

                if terrrain_type == TerrainType.CITY:
                    city: City = self.city_util.find_city(game_state=game_state,
                                                          city_position=meeple_position.coordinate_with_side)
                    meeples: [CoordinateWithSide] = self.city_util.find_meeples(game_state=game_state, city=city)
                    meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                    print("Collecting points for unfinished city. Meeples:", json.dumps(meeple_counts_per_player))
                    winning_player = self.get_winning_player(meeple_counts_per_player)
                    if winning_player is not None:
                        points = self.count_city_points(game_state=game_state, city=city)
                        print(points, "points for player", player)
                        game_state.scores[winning_player] += points

                    self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples)
                    continue

                if terrrain_type == TerrainType.ROAD:
                    road: [Road] = self.road_util.find_road(game_state=game_state,
                                                            road_position=meeple_position.coordinate_with_side)
                    meeples: [CoordinateWithSide] = self.road_util.find_meeples(game_state=game_state, road=road)
                    meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                    print("Collecting points for unfinished road. Meeples:", json.dumps(meeple_counts_per_player))
                    winning_player = self.get_winning_player(meeple_counts_per_player)
                    if winning_player is not None:
                        points = self.count_road_points(game_state=game_state, road=road)
                        print(points, "points for player", player)
                        game_state.scores[winning_player] += points
                    self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples)
                    continue

                if terrrain_type == TerrainType.CHAPEL_OR_FLOWERS:
                    points = self.chapel_or_flowers_points(game_state=game_state,
                                                           coordinate=meeple_position.coordinate_with_side.coordinate)
                    print("Collecting points for unfinished chapel or flowers for player", str(player))
                    print(points, "points for player", player)
                    game_state.scores[player] += points

                    meeples_per_player = []
                    for _ in range(game_state.players):
                        meeples_per_player.append([])
                    meeples_per_player[player].append(meeple_position)

                    self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples_per_player)
                    continue

                if meeple_position.meeple_type == MeepleType.FARMER or meeple_position.meeple_type == MeepleType.BIG_FARMER:
                    farm: Farm = FarmUtil.find_farm_by_coordinate(game_state=game_state, position=meeple_position.coordinate_with_side)
                    meeples: [[MeeplePosition]] = FarmUtil.find_meeples(game_state=game_state, farm=farm)
                    meeple_counts_per_player = self.get_meeple_counts_per_player(meeples)
                    print("Collecting points for farm. Meeples:", json.dumps(meeple_counts_per_player))
                    winning_player = self.get_winning_player(meeple_counts_per_player)
                    if winning_player is not None:
                        points = self.count_farm_points(game_state=game_state, farm=farm)
                        print(points, "points for player", winning_player)
                        game_state.scores[winning_player] += points
                    self.meeple_util.remove_meeples(game_state=game_state, meeples=meeples)
                    continue

                print("Collecting points for unknown type", terrrain_type)

    @staticmethod
    def get_meeple_counts_per_player(meeples: [[MeeplePosition]]):
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

    @classmethod
    def count_farm_points(cls, game_state: CarcassonneGameState, farm: Farm):
        cities: Set[City] = set()

        points = 0

        farmer_connection_with_coordinate: FarmerConnectionWithCoordinate
        for farmer_connection_with_coordinate in farm.farmer_connections_with_coordinate:
            cities = cities.union(CityUtil.find_cities(game_state=game_state, coordinate=farmer_connection_with_coordinate.coordinate, sides=farmer_connection_with_coordinate.farmer_connection.city_sides))

        city: City
        for city in cities:
            if city.finished:
                points += 3

        return points
