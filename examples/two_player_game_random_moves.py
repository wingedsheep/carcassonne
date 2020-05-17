import random
from typing import Optional

from main.carcassonne_game import CarcassonneGame
from main.carcassonne_game_state import CarcassonneGameState
from main.objects.actions.action import Action
from main.tile_sets.tile_sets import TileSet


def print_state(carcassonne_game_state: CarcassonneGameState):
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


game = CarcassonneGame(
    players=2,
    tile_sets=[TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS]
)

while not game.is_finished():
    player: int = game.state.current_player
    valid_actions: [Action] = game.get_possible_actions()
    action: Optional[Action] = random.choice(valid_actions)
    if action is not None:
        game.step(player, action)
    game.render()

print_state(carcassonne_game_state=game.state)
