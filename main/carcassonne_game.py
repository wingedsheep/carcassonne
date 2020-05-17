from main.carcassonne_game_state import CarcassonneGameState
from main.carcassonne_visualiser import CarcassonneVisualiser
from main.objects.actions.action import Action
from main.tile_sets.tile_sets import TileSet
from main.utils.action_util import ActionUtil
from main.utils.state_updater import StateUpdater


class CarcassonneGame:

    def __init__(self,
                 players: object = 2,
                 tile_sets: object = (TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS)) -> object:
        self.players = players
        self.tile_sets = tile_sets
        self.state: CarcassonneGameState = CarcassonneGameState(tile_sets=tile_sets)
        self.visualiser = CarcassonneVisualiser()
        self.action_util = ActionUtil()

    def reset(self):
        self.state = CarcassonneGameState(tile_sets=self.tile_sets)

    def step(self, player: int, action: Action):
        self.state = StateUpdater.apply_action(game_state=self.state, action=action)

    def render(self):
        self.visualiser.draw_game_state(self.state)

    def is_finished(self) -> bool:
        return self.state.is_terminated()

    def get_current_player(self) -> int:
        return self.state.current_player

    def get_possible_actions(self) -> [Action]:
        return ActionUtil.get_possible_actions(self.state)
