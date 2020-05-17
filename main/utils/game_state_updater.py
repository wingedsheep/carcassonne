import copy
from main.carcassonne_game_state import CarcassonneGameState, GamePhase
from main.objects.meeple_action import MeepleAction
from main.objects.meeple_position import MeeplePosition
from main.objects.meeple_type import MeepleType
from main.objects.rotation import Rotation
from main.objects.tile import Tile
from main.utils.city_util import CityUtil
from main.utils.meeple_util import MeepleUtil
from main.utils.points_collector import PointsCollector
from main.utils.river_rotation_util import get_river_rotation_tile
from main.utils.road_util import RoadUtil
from main.utils.tile_positions import PlayingPosition

points_collector: PointsCollector = PointsCollector(city_util=CityUtil(), road_util=RoadUtil(), meeple_util=MeepleUtil())


def play_tile(game_state: CarcassonneGameState, tile: Tile, playing_position: PlayingPosition) -> CarcassonneGameState:
    new_game_state = copy.deepcopy(game_state)
    turned_tile: Tile = tile.turn(playing_position.turns)
    new_game_state.board[playing_position.coordinate.row][playing_position.coordinate.column] = turned_tile
    new_game_state.phase = GamePhase.MEEPLES
    update_last_played_river_rotation(game_state, new_game_state, turned_tile)
    new_game_state.last_played_tile = (turned_tile, playing_position)
    return new_game_state


def update_last_played_river_rotation(game_state, new_game_state, turned_tile):
    if turned_tile.has_river() and game_state.last_played_tile is not None:
        river_rotation: Rotation = get_river_rotation_tile(previous_tile=game_state.last_played_tile[0],
                                                           new_tile=turned_tile)
        if river_rotation != Rotation.NONE:
            new_game_state.last_river_rotation = river_rotation


def play_meeple(game_state: CarcassonneGameState, meeple_action: MeepleAction) -> CarcassonneGameState:
    new_game_state = copy.deepcopy(game_state)

    if not meeple_action.remove:
        new_game_state.placed_meeples[game_state.current_player].append(MeeplePosition(meeple_type=meeple_action.meeple_type, coordinate_with_side=meeple_action.coordinate_with_side))
    else:
        new_game_state.placed_meeples[game_state.current_player].remove(MeeplePosition(meeple_type=meeple_action.meeple_type, coordinate_with_side=meeple_action.coordinate_with_side))

    if meeple_action.meeple_type == MeepleType.NORMAL or meeple_action.meeple_type == MeepleType.FARMER:
        new_game_state.meeples[game_state.current_player] += 1 if meeple_action.remove else -1
    elif meeple_action.meeple_type == MeepleType.ABBOT:
        new_game_state.abbots[game_state.current_player] += 1 if meeple_action.remove else -1
    elif meeple_action.meeple_type == MeepleType.BIG or meeple_action.meeple_type == MeepleType.BIG_FARMER:
        new_game_state.big_meeples[game_state.current_player] += 1 if meeple_action.remove else -1

    if new_game_state.last_played_tile is not None and new_game_state.last_played_tile[1] is not None:
        points_collector.remove_meeples_and_collect_points(game_state=new_game_state, coordinate=new_game_state.last_played_tile[1].coordinate)

    return new_game_state


def next_player(game_state: CarcassonneGameState):
    new_game_state: CarcassonneGameState = copy.deepcopy(game_state)
    new_game_state = draw_tile(new_game_state)
    new_game_state.phase = GamePhase.TILES
    new_game_state.current_player = game_state.current_player + 1
    if new_game_state.current_player >= game_state.players:
        new_game_state.current_player = 0
    return new_game_state
    

def draw_tile(game_state: CarcassonneGameState) -> CarcassonneGameState:
    if len(game_state.deck) == 0:
        game_state.next_tile = None
    else:
        game_state.next_tile = game_state.deck.pop(0)
    return game_state
