from game_definition import GameDefinition
from main.carcassonne_game_state import CarcassonneGameState


class CarcassonneGameDefinition(GameDefinition):

    def new_game(self) -> CarcassonneGameState:
        return CarcassonneGameState()
