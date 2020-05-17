from typing import Optional

from main.carcassonne_game_state import CarcassonneGameState
from main.objects.coordinate_with_side import CoordinateWithSide


class MeepleUtil:
    
    def position_contains_meeple(self, game_state: CarcassonneGameState, coordinate_with_side: CoordinateWithSide) -> Optional[int]:
        for player in range(game_state.players):
            if coordinate_with_side in list(map(lambda x: x.coordinate_with_side, game_state.placed_meeples[player])):
                return player
        return None
