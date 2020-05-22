from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
from wingedsheep.carcassonne.carcassonne_visualiser import CarcassonneVisualiser
from wingedsheep.carcassonne.objects.actions.action import Action
from wingedsheep.carcassonne.tile_sets.supplementary_rules import SupplementaryRule
from wingedsheep.carcassonne.tile_sets.tile_sets import TileSet
from wingedsheep.carcassonne.utils.action_util import ActionUtil
from wingedsheep.carcassonne.utils.state_updater import StateUpdater


class CarcassonneGame:

    def __init__(self,
                 players: int = 2,
                 tile_sets: [TileSet] = (TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS),
                 supplementary_rules: [SupplementaryRule] = (SupplementaryRule.FARMERS, SupplementaryRule.ABBOTS)):
        self.players = players
        self.tile_sets = tile_sets
        self.supplementary_rules = supplementary_rules
        self.state: CarcassonneGameState = CarcassonneGameState(
            tile_sets=tile_sets,
            players=players,
            supplementary_rules=supplementary_rules
        )
        self.visualiser = CarcassonneVisualiser()

    def reset(self):
        self.state = CarcassonneGameState(tile_sets=self.tile_sets, supplementary_rules=self.supplementary_rules)

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
