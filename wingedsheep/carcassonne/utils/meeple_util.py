from typing import Optional

from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
from wingedsheep.carcassonne.objects.coordinate_with_side import CoordinateWithSide
from wingedsheep.carcassonne.objects.meeple_position import MeeplePosition
from wingedsheep.carcassonne.objects.meeple_type import MeepleType


class MeepleUtil:

    @staticmethod
    def position_contains_meeple(game_state: CarcassonneGameState, coordinate_with_side: CoordinateWithSide) -> Optional[int]:
        for player in range(game_state.players):
            if coordinate_with_side in list(map(lambda x: x.coordinate_with_side, game_state.placed_meeples[player])):
                return player
        return None

    @staticmethod
    def remove_meeples(game_state: CarcassonneGameState, meeples: [[MeeplePosition]]):
        for player, meeple_positions in enumerate(meeples):
            meeple_position: MeeplePosition
            for meeple_position in meeple_positions:
                MeepleUtil.remove_meeple(game_state, meeple_position, player)

    @staticmethod
    def remove_meeple(game_state: CarcassonneGameState, meeple_position: MeeplePosition, player: int):
        game_state.placed_meeples[player].remove(meeple_position)
        if meeple_position.meeple_type == MeepleType.NORMAL or meeple_position.meeple_type == MeepleType.FARMER:
            game_state.meeples[player] += 1
        elif meeple_position.meeple_type == MeepleType.ABBOT:
            game_state.abbots[player] += 1
        elif meeple_position.meeple_type == MeepleType.BIG or meeple_position.meeple_type == MeepleType.BIG_FARMER:
            game_state.big_meeples[player] += 1
