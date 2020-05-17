import random
from enum import Enum
from typing import Optional

from main.objects.actions.tile_action import TileAction
from main.tile_sets.base_deck import base_tile_counts, base_tiles
from main.tile_sets.inns_and_cathedrals_deck import inns_and_cathedrals_tile_counts, inns_and_cathedrals_tiles
from main.tile_sets.the_river_deck import the_river_tiles, the_river_tile_counts
from main.objects.playing_position import PlayingPosition
from main.objects.rotation import Rotation
from main.objects.tile import Tile
from main.tile_sets.tile_sets import TileSet


class GamePhase(Enum):
    TILES = "tiles"
    MEEPLES = "meeples"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value


class CarcassonneGameState:

    def __init__(self, tile_sets: [TileSet]):
        self.deck = self.initialize_deck(tile_sets=tile_sets)
        self.board: [[Tile]] = [[None for i in range(41)] for i in range(41)]
        self.next_tile = self.deck.pop(0)
        self.players = 2
        self.meeples = [7, 7]
        self.abbots = [1, 1]
        self.big_meeples = [1, 1]
        self.placed_meeples = [[], []]
        self.scores: [int] = [0, 0]
        self.current_player = 0
        self.phase = GamePhase.TILES
        self.last_tile_action: Optional[TileAction] = None
        self.last_river_rotation: Rotation = Rotation.NONE

    def get_tile(self, row: int, column: int):
        if row < 0 or column < 0:
            return None
        elif row >= len(self.board) or column >= len(self.board[0]):
            return None
        else:
            return self.board[row][column]

    def empty_board(self):
        for row in self.board:
            for column in row:
                if column is not None:
                    return False
        return True

    def is_terminated(self) -> bool:
        return False

    def initialize_deck(self, tile_sets: [TileSet]):
        deck: [Tile] = []

        # The river
        if TileSet.THE_RIVER in tile_sets:
            deck.append(the_river_tiles["river_start"])

            new_tiles = []
            for card_name, count in the_river_tile_counts.items():
                if card_name == "river_start":
                    continue
                if card_name == "river_end":
                    continue

                for i in range(count):
                    new_tiles.append(the_river_tiles[card_name])

            random.shuffle(new_tiles)
            for tile in new_tiles:
                deck.append(tile)

            deck.append(the_river_tiles["river_end"])

        new_tiles = []

        if TileSet.BASE in tile_sets:
            for card_name, count in base_tile_counts.items():
                for i in range(count):
                    new_tiles.append(base_tiles[card_name])

        if TileSet.INNS_AND_CATHEDRALS in tile_sets:
            for card_name, count in inns_and_cathedrals_tile_counts.items():
                for i in range(count):
                    new_tiles.append(inns_and_cathedrals_tiles[card_name])

        random.shuffle(new_tiles)
        for tile in new_tiles:
            deck.append(tile)

        return deck
