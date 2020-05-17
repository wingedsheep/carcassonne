from main.objects.connection import Connection
from main.objects.side import Side
from main.objects.tile import Tile

the_river_tiles = {
    "river_start": Tile(
        description="river_start",
        river=[
            Connection(Side.CENTER, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT, Side.TOP],
        image="River_III_C2_Tile_A.png"
    ),
    "river_city_with_road": Tile(
        description="river_city_with_road",
        river=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        road=[
            Connection(Side.CENTER, Side.BOTTOM),
        ],
        city=[[Side.TOP]],
        image="River_III_C2_Tile_B.png"
    ),
    "river_double_city": Tile(
        description="river_double_city",
        river=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        city=[[Side.TOP], [Side.BOTTOM]],
        image="River_III_C2_Tile_C.png"
    ),
    "river_straight": Tile(
        description="river_straight",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT],
        image="River_III_C2_Tile_D.png"
    ),
    "river_diagonal_city": Tile(
        description="river_diagonal_city",
        river=[
            Connection(Side.LEFT, Side.BOTTOM),
        ],
        city=[[Side.TOP, Side.RIGHT]],
        image="River_III_C2_Tile_E.png"
    ),
    "river_straight_2": Tile(
        description="river_straight_2",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT],
        image="River_III_C2_Tile_F.png"
    ),
    "river_bend": Tile(
        description="river_bend",
        river=[
            Connection(Side.TOP, Side.LEFT),
        ],
        grass=[Side.RIGHT, Side.BOTTOM],
        image="River_III_C2_Tile_G.png"
    ),
    "river_chapel": Tile(
        description="river_chapel",
        river=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        road=[
            Connection(Side.CENTER, Side.BOTTOM)
        ],
        grass=[Side.TOP],
        chapel_or_flowers=True,
        image="River_III_C2_Tile_H.png"
    ),
    "river_bend_with_road": Tile(
        description="river_bend_with_road",
        river=[
            Connection(Side.RIGHT, Side.BOTTOM),
        ],
        road=[
            Connection(Side.LEFT, Side.TOP),
        ],
        image="River_III_C2_Tile_I.png"
    ),
    "river_flowery_bend": Tile(
        description="river_flowery_bend",
        river=[
            Connection(Side.RIGHT, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.TOP],
        chapel_or_flowers=True,
        image="River_III_C2_Tile_J.png"
    ),
    "river_crossing": Tile(
        description="river_crossing",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        road=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        image="River_III_C2_Tile_K.png"
    ),
    "river_end": Tile(
        description="river_end",
        river=[
            Connection(Side.TOP, Side.CENTER),
        ],
        grass=[Side.LEFT, Side.RIGHT, Side.BOTTOM],
        image="River_I_C2_Tile_L.jpg"
    )
}

the_river_tile_counts = {
    "river_start": 1,
    "river_straight": 2,
    "river_flowery_bend": 1,
    "river_chapel": 1,
    "river_crossing": 1,
    "river_bend": 1,
    "river_double_city": 1,
    "river_bend_with_road": 1,
    "river_city_with_road": 1,
    "river_end": 1
}