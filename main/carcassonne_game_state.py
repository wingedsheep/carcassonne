import random
from enum import Enum

from main.decks.base_deck import base_tile_counts, base_tiles
from main.decks.inns_and_cathedrals_deck import inns_and_cathedrals_tile_counts, inns_and_cathedrals_tiles
from main.decks.the_river_deck import the_river_tiles, the_river_tile_counts
from main.objects.playing_position import PlayingPosition
from main.objects.rotation import Rotation
from main.objects.tile import Tile


class GamePhase(Enum):
    TILES = "tiles"
    MEEPLES = "meeples"

    def to_json(self):
        return self.value

    def __str__(self):
        return self.value


class CarcassonneGameState:

    def __init__(self):
        self.deck = self.initialize_deck(add_river_tiles=True)
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
        self.last_played_tile: (Tile, PlayingPosition) = None
        self.last_river_rotation: Rotation = Rotation.NONE

    def empty_board(self):
        for row in self.board:
            for column in row:
                if column is not None:
                    return False
        return True

    def is_terminated(self) -> bool:
        return False

    def initialize_deck(self, add_river_tiles: bool):
        deck: [Tile] = []

        # The river
        if add_river_tiles:
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

        for card_name, count in base_tile_counts.items():
            for i in range(count):
                new_tiles.append(base_tiles[card_name])

        for card_name, count in inns_and_cathedrals_tile_counts.items():
            for i in range(count):
                new_tiles.append(inns_and_cathedrals_tiles[card_name])

        random.shuffle(new_tiles)
        for tile in new_tiles:
            deck.append(tile)

        return deck
