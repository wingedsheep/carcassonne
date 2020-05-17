import random

from main.carcassonne_game_state import CarcassonneGameState, GamePhase
from main.objects.actions.meeple_action import MeepleAction
from main.utils.game_state_updater import draw_tile, play_tile, play_meeple, next_player, \
    remove_meeples_and_update_score
from main.utils.possible_move_finder import possible_meeple_actions
from main.utils.tile_position_finder import PlayingPosition, possible_playing_positions


class RandomCarcassonneAgent:

    def act(self, game_state: CarcassonneGameState):
        if game_state.phase == GamePhase.TILES:
            return self.play_random_tile(game_state)
        elif game_state.phase == GamePhase.MEEPLES:
            new_game_state = self.play_random_meeple(game_state)
            return remove_meeples_and_update_score(new_game_state)

    def play_random_tile(self, game_state: CarcassonneGameState):
        playing_positions = possible_playing_positions(game_state, game_state.next_tile)
        print("Tile: " + game_state.next_tile.description + ", Deck: " + str(
            len(game_state.deck)) + ", Playing positions: " + str(len(playing_positions)))

        if len(playing_positions) == 0:
            game_state = draw_tile(game_state)
            if game_state.next_tile is None:
                return game_state
            else:
                return self.play_random_tile(game_state)

        random_playing_position: PlayingPosition = random.choice(playing_positions)
        return play_tile(game_state, game_state.next_tile, random_playing_position)

    def play_random_meeple(self, game_state) -> CarcassonneGameState:
        new_game_state = game_state
        meeple_actions: [MeepleAction] = possible_meeple_actions(game_state=game_state)
        if len(meeple_actions) > 0:
            random_meeple_action: MeepleAction = random.choice(meeple_actions)
            new_game_state = play_meeple(game_state, random_meeple_action)

        return next_player(new_game_state)
