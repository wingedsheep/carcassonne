import copy

from main.carcassonne_game_state import CarcassonneGameState, GamePhase
from main.objects.actions.action import Action
from main.objects.actions.meeple_action import MeepleAction
from main.objects.actions.pass_action import PassAction
from main.objects.actions.tile_action import TileAction
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.utils.points_collector import PointsCollector
from main.utils.river_rotation_util import RiverRotationUtil


class StateUpdater:

    @staticmethod
    def apply_action(game_state: CarcassonneGameState, action: Action) -> CarcassonneGameState:
        new_game_state: CarcassonneGameState = copy.deepcopy(game_state)

        if isinstance(action, TileAction):
            StateUpdater.play_tile(game_state=new_game_state, tile_action=action)
            new_game_state.phase = GamePhase.MEEPLES
        elif isinstance(action, MeepleAction):
            StateUpdater.play_meeple(game_state=new_game_state, meeple_action=action)
        elif isinstance(action, PassAction):
            if game_state.phase == GamePhase.TILES:
                StateUpdater.draw_tile(game_state=new_game_state)
                new_game_state.phase = GamePhase.MEEPLES
            elif game_state.phase == GamePhase.MEEPLES:
                pass

        if game_state.phase == GamePhase.MEEPLES:
            StateUpdater.remove_meeples_and_update_score(game_state=new_game_state)
            StateUpdater.draw_tile(game_state=new_game_state)
            StateUpdater.next_player(game_state=new_game_state)

        if new_game_state.is_terminated():
            PointsCollector.count_final_scores(game_state=new_game_state)

        return new_game_state

    @staticmethod
    def next_player(game_state: CarcassonneGameState) -> CarcassonneGameState:
        game_state.phase = GamePhase.TILES
        game_state.current_player = game_state.current_player + 1
        if game_state.current_player >= game_state.players:
            game_state.current_player = 0
        return game_state

    @staticmethod
    def play_tile(game_state: CarcassonneGameState, tile_action: TileAction) -> CarcassonneGameState:
        game_state.board[tile_action.coordinate.row][tile_action.coordinate.column] = tile_action.tile
        game_state.phase = GamePhase.MEEPLES
        game_state.last_river_rotation = RiverRotationUtil.get_river_rotation(game_state=game_state,
                                                                              tile=tile_action.tile)
        game_state.last_tile_action = tile_action
        return game_state

    @staticmethod
    def play_meeple(game_state: CarcassonneGameState, meeple_action: MeepleAction) -> CarcassonneGameState:
        if not meeple_action.remove:
            game_state.placed_meeples[game_state.current_player].append(
                MeeplePosition(meeple_type=meeple_action.meeple_type,
                               coordinate_with_side=meeple_action.coordinate_with_side))
        else:
            game_state.placed_meeples[game_state.current_player].remove(
                MeeplePosition(meeple_type=meeple_action.meeple_type,
                               coordinate_with_side=meeple_action.coordinate_with_side))

        if meeple_action.meeple_type == MeepleType.NORMAL or meeple_action.meeple_type == MeepleType.FARMER:
            game_state.meeples[game_state.current_player] += 1 if meeple_action.remove else -1
        elif meeple_action.meeple_type == MeepleType.ABBOT:
            if meeple_action.remove:
                points = PointsCollector.chapel_or_flowers_points(game_state=game_state,
                                                                  coordinate=meeple_action.coordinate_with_side.coordinate)
                game_state.scores[game_state.current_player] += points
            game_state.abbots[game_state.current_player] += 1 if meeple_action.remove else -1
        elif meeple_action.meeple_type == MeepleType.BIG or meeple_action.meeple_type == MeepleType.BIG_FARMER:
            game_state.big_meeples[game_state.current_player] += 1 if meeple_action.remove else -1

        return game_state

    @staticmethod
    def draw_tile(game_state: CarcassonneGameState) -> CarcassonneGameState:
        if len(game_state.deck) == 0:
            game_state.next_tile = None
        else:
            game_state.next_tile = game_state.deck.pop(0)
        return game_state

    @staticmethod
    def remove_meeples_and_update_score(game_state: CarcassonneGameState) -> CarcassonneGameState:
        if game_state.last_tile_action is not None and game_state.last_tile_action.tile is not None:
            PointsCollector.remove_meeples_and_collect_points(game_state=game_state,
                                                              coordinate=game_state.last_tile_action.coordinate)
        return game_state
