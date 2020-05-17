import unittest

from main.carcassonne_game_state import CarcassonneGameState
from main.decks.base_deck import base_tiles
from main.objects.city import City
from main.objects.coordinate import Coordinate
from main.objects.coordinate_with_side import CoordinateWithSide
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.objects.road import Road
from main.objects.side import Side
from main.utils.city_util import CityUtil
from main.utils.road_util import RoadUtil


class TestCityUtil(unittest.TestCase):

    def test_find_road(self):
        """
        Find the positions for a city with a top and a bottom
        """

        # Given
        road_util: RoadUtil = RoadUtil()
        game_state: CarcassonneGameState = CarcassonneGameState()

        crossroads = base_tiles["crossroads"]

        game_state.board = [[None for column in range(1)] for row in range(2)]

        game_state.board[0][0] = crossroads
        game_state.board[1][0] = crossroads

        # When
        road: Road = road_util.find_road(
            game_state=game_state,
            road_position=CoordinateWithSide(Coordinate(0, 0), Side.BOTTOM)
        )

        # Then
        self.assertTrue(road.finished)
        self.assertEqual(2, len(road.road_positions))
        self.assertIn(CoordinateWithSide(Coordinate(0, 0), Side.BOTTOM), road.road_positions)
        self.assertIn(CoordinateWithSide(Coordinate(1, 0), Side.TOP), road.road_positions)