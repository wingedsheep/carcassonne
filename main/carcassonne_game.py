from main.agent.random_agent import RandomCarcassonneAgent
from main.carcassonne_game_state import CarcassonneGameState
from main.carcassonne_visualiser import CarcassonneVisualiser
from main.utils.city_util import CityUtil
from main.utils.meeple_util import MeepleUtil
from main.utils.points_collector import PointsCollector
from main.utils.road_util import RoadUtil


class CarcassonneGame:

    def __init__(self, players: [RandomCarcassonneAgent],
                 visualiser: CarcassonneVisualiser):
        self.players = players
        self.visualiser = visualiser

    def play_game(self):
        carcassonne_game_state: CarcassonneGameState = CarcassonneGameState()
        while carcassonne_game_state.next_tile is not None:
            print("Player", carcassonne_game_state.current_player, carcassonne_game_state.phase)
            player = self.players[carcassonne_game_state.current_player]
            carcassonne_game_state = player.act(carcassonne_game_state)
            self.visualiser.draw_game_state(carcassonne_game_state)
            self.print_state(carcassonne_game_state)

        points_collector = PointsCollector(city_util=CityUtil(), road_util=RoadUtil(), meeple_util=MeepleUtil())
        points_collector.count_final_scores(game_state=carcassonne_game_state)
        self.print_state(carcassonne_game_state)

    def print_state(self, carcassonne_game_state):

        print_object = {
            "scores": {
                "player 1": carcassonne_game_state.scores[0],
                "player 2": carcassonne_game_state.scores[1]
            },
            "meeples": {
                "player 1": {
                    "normal": carcassonne_game_state.meeples[0],
                    "abbots": carcassonne_game_state.abbots[0],
                    "big": carcassonne_game_state.big_meeples[0]
                },
                "player 2": {
                    "normal": carcassonne_game_state.meeples[1],
                    "abbots": carcassonne_game_state.abbots[1],
                    "big": carcassonne_game_state.big_meeples[1]
                }
            }
        }

        print(print_object)
