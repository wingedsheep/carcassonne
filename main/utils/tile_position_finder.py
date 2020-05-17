from main.carcassonne_game_state import CarcassonneGameState
from main.objects.coordinate import Coordinate
from main.objects.playing_position import PlayingPosition
from main.objects.tile import Tile
from main.utils.tile_fitter import fits


class TilePositionFinder:

    @staticmethod
    def possible_playing_positions(game_state: CarcassonneGameState, tile_to_play: Tile) -> [PlayingPosition]:
        if game_state.empty_board():
            return [PlayingPosition(coordinate=Coordinate(row=5, column=14), turns=0)]

        playing_positions = []

        for row_index, board_row in enumerate(game_state.board):
            for column_index, column_tile in enumerate(board_row):
                if column_tile is not None:
                    continue

                for tile_turns in range(0, 4):
                    if row_index == 0:
                        top = None
                    else:
                        top = game_state.board[row_index - 1][column_index]

                    if row_index == len(game_state.board) - 1:
                        bottom = None
                    else:
                        bottom = game_state.board[row_index + 1][column_index]

                    if column_index == 0:
                        left = None
                    else:
                        left = game_state.board[row_index][column_index - 1]

                    if column_index == len(board_row) - 1:
                        right = None
                    else:
                        right = game_state.board[row_index][column_index + 1]

                    if fits(tile_to_play.turn(tile_turns), top=top, bottom=bottom, left=left, right=right, game_state=game_state):
                        playing_positions.append(PlayingPosition(coordinate=Coordinate(row=row_index, column=column_index), turns=tile_turns))

        return playing_positions
