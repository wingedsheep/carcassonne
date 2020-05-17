from main.objects.connection import Connection
from main.objects.side import Side
from main.objects.tile import Tile

inns_and_cathedrals_tiles = {
    "ic_1": Tile(
        description="ic_1",
        grass=[Side.TOP],
        city=[[Side.LEFT, Side.BOTTOM], [Side.RIGHT]],
        image="inns_cathedrals_1.png",
        shield=True
    ),
    "ic_2": Tile(
        description="ic_2",
        grass=[Side.TOP, Side.RIGHT],
        road=[Connection(Side.BOTTOM, Side.LEFT)],
        image="inns_cathedrals_2.png"
    ),
    "ic_3": Tile(
        description="ic_3",
        road=[Connection(Side.BOTTOM, Side.RIGHT), Connection(Side.TOP, Side.LEFT)],
        image="inns_cathedrals_3.png"
    ),
    "ic_4": Tile(
        description="ic_4",
        city=[[Side.LEFT, Side.RIGHT]],
        road=[Connection(Side.TOP, Side.CENTER), Connection(Side.BOTTOM, Side.CENTER)],
        image="inns_cathedrals_4.png"
    ),
    "ic_5": Tile(
        description="ic_5",
        city=[[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]],
        cathedral=True,
        image="inns_cathedrals_5.png"
    ),
    "ic_6": Tile(
        description="ic_6",
        city=[[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]],
        cathedral=True,
        image="inns_cathedrals_6.png"
    ),
    "ic_7": Tile(
        description="ic_7",
        city=[[Side.TOP], [Side.RIGHT], [Side.LEFT]],
        grass=[Side.BOTTOM],
        image="inns_cathedrals_7.png"
    ),
    "ic_8": Tile(
        description="ic_8",
        city=[[Side.TOP], [Side.RIGHT], [Side.LEFT], [Side.BOTTOM]],
        chapel_or_flowers=True,
        image="inns_cathedrals_8.png"
    ),
    "ic_9": Tile(
        description="ic_9",
        grass=[Side.TOP, Side.BOTTOM],
        road=[Connection(Side.LEFT, Side.RIGHT)],
        chapel_or_flowers=True,
        image="inns_cathedrals_9.png"
    ),
    "ic_10": Tile(
        description="ic_10",
        city=[[Side.LEFT]],
        grass=[Side.TOP],
        road=[Connection(Side.BOTTOM, Side.RIGHT)],
        image="inns_cathedrals_10.png"
    ),
    "ic_11": Tile(
        description="ic_11",
        city=[[Side.LEFT, Side.TOP]],
        grass=[Side.BOTTOM],
        road=[Connection(Side.CENTER, Side.RIGHT)],
        image="inns_cathedrals_11.png"
    ),
    "ic_12": Tile(
        description="ic_12",
        city=[[Side.RIGHT, Side.TOP]],
        grass=[Side.BOTTOM],
        road=[Connection(Side.CENTER, Side.LEFT)],
        image="inns_cathedrals_12.png"
    ),
    "ic_13": Tile(
        description="ic_13",
        city=[[Side.BOTTOM]],
        grass=[Side.LEFT, Side.RIGHT, Side.TOP],
        image="inns_cathedrals_13.png"
    ),
    "ic_14": Tile(
        description="ic_14",
        city=[[Side.BOTTOM, Side.RIGHT]],
        road=[Connection(Side.TOP, Side.LEFT)],
        shield=True,
        image="inns_cathedrals_14.png"
    ),
    "ic_15": Tile(
        description="ic_15",
        city=[[Side.BOTTOM]],
        road=[Connection(Side.TOP, Side.CENTER)],
        grass=[Side.LEFT, Side.RIGHT],
        image="inns_cathedrals_15.png"
    ),
    "ic_16": Tile(
        description="ic_16",
        city=[[Side.LEFT], [Side.RIGHT]],
        road=[Connection(Side.TOP, Side.CENTER), Connection(Side.BOTTOM, Side.CENTER)],
        image="inns_cathedrals_16.png"
    ),
    "ic_17": Tile(
        description="ic_17",
        road=[Connection(Side.LEFT, Side.CENTER), Connection(Side.RIGHT, Side.CENTER)],
        grass=[Side.TOP, Side.BOTTOM],
        chapel_or_flowers=True,
        image="inns_cathedrals_17.png"
    ),
    "ic_18": Tile(
        description="ic_18",
        road=[
            Connection(Side.LEFT, Side.CENTER),
            Connection(Side.RIGHT, Side.CENTER),
            Connection(Side.BOTTOM, Side.CENTER)
        ],
        grass=[Side.TOP],
        image="inns_cathedrals_18.png"
    )
}

inns_and_cathedrals_tile_counts = {
    "ic_1": 1,
    "ic_2": 1,
    "ic_3": 1,
    "ic_4": 1,
    "ic_5": 1,
    "ic_6": 1,
    "ic_7": 1,
    "ic_8": 1,
    "ic_9": 1,
    "ic_10": 1,
    "ic_11": 1,
    "ic_12": 1,
    "ic_13": 1,
    "ic_14": 1,
    "ic_15": 1,
    "ic_16": 1,
    "ic_17": 1,
    "ic_18": 1
}