import unittest

from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
from wingedsheep.carcassonne.objects.coordinate import Coordinate
from wingedsheep.carcassonne.objects.coordinate_with_side import CoordinateWithSide
from wingedsheep.carcassonne.objects.meeple_position import MeeplePosition
from wingedsheep.carcassonne.objects.meeple_type import MeepleType
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.tile_sets.base_deck import base_tiles
from wingedsheep.carcassonne.tile_sets.inns_and_cathedrals_deck import inns_and_cathedrals_tiles
from wingedsheep.carcassonne.utils.points_collector import PointsCollector


class TestPointsCollector(unittest.TestCase):

    def test_collect_points_small_city(self):
        """
        Find cities left and right
        """

        # Given
        game_state: CarcassonneGameState = CarcassonneGameState()

        city_one_side_straight_road = base_tiles["city_top_straight_road"].turn(3)
        city_with_road = inns_and_cathedrals_tiles["ic_15"].turn(3)

        game_state.board = [[None for column in range(2)] for row in range(1)]

        game_state.board[0][0] = city_with_road
        game_state.board[0][1] = city_one_side_straight_road

        game_state.players = 2

        game_state.placed_meeples = [[], []]
        game_state.placed_meeples[0].append(MeeplePosition(meeple_type=MeepleType.NORMAL, coordinate_with_side=CoordinateWithSide(Coordinate(0, 0), Side.RIGHT)))
        game_state.placed_meeples[1].append(MeeplePosition(meeple_type=MeepleType.NORMAL, coordinate_with_side=CoordinateWithSide(Coordinate(0, 1), Side.BOTTOM)))

        # When
        PointsCollector.remove_meeples_and_collect_points(game_state=game_state, coordinate=Coordinate(0, 0))

        # Then
        self.assertEqual(0, len(game_state.placed_meeples[0]))
        self.assertEqual(1, len(game_state.placed_meeples[1]))
        self.assertEqual(4, game_state.scores[0])
        self.assertEqual(0, game_state.scores[1])

    def test_collect_points_small_city_2(self):
        """
        Find cities left and right
        """

        # Given
        game_state: CarcassonneGameState = CarcassonneGameState()

        city_one_side_straight_road = base_tiles["city_top_straight_road"].turn(3)
        city_with_road = inns_and_cathedrals_tiles["ic_15"].turn(3)

        game_state.board = [[None for column in range(2)] for row in range(1)]

        game_state.board[0][0] = city_with_road
        game_state.board[0][1] = city_one_side_straight_road

        game_state.players = 2

        game_state.placed_meeples = [[], []]
        game_state.placed_meeples[0].append(MeeplePosition(meeple_type=MeepleType.NORMAL, coordinate_with_side=CoordinateWithSide(Coordinate(0, 0), Side.RIGHT)))
        game_state.placed_meeples[1].append(MeeplePosition(meeple_type=MeepleType.NORMAL, coordinate_with_side=CoordinateWithSide(Coordinate(0, 1), Side.BOTTOM)))

        # When
        PointsCollector.remove_meeples_and_collect_points(game_state=game_state, coordinate=Coordinate(0, 1))

        # Then
        self.assertEqual(0, len(game_state.placed_meeples[0]))
        self.assertEqual(1, len(game_state.placed_meeples[1]))
        self.assertEqual(4, game_state.scores[0])
        self.assertEqual(0, game_state.scores[1])
