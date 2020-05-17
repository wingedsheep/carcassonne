from main.objects.connection import Connection
from main.objects.side import Side
from main.objects.tile import Tile

base_tiles = {
    "chapel_with_road": Tile(
        description="chapel_with_road",
        road=[Connection(Side.BOTTOM, Side.CENTER)],
        grass=[Side.LEFT, Side.TOP, Side.RIGHT],
        chapel_or_flowers=True,
        image="Base_Game_C2_Tile_A.jpg"
    ),
    "chapel": Tile(
        description="chapel",
        grass=[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT],
        chapel_or_flowers=True,
        image="Base_Game_C2_Tile_B.jpg"
    ),
    "full_city_with_shield": Tile(
        description="full_city_with_shield",
        city=[[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]],
        shield=True,
        image="Base_Game_C2_Tile_C.jpg"
    ),
    "city_one_side_straight_road": Tile(
        description="city_with_straight_road",
        road=[Connection(Side.LEFT, Side.RIGHT)],
        city=[[Side.TOP]],
        grass=[Side.BOTTOM],
        image="Base_Game_C2_Tile_D.jpg"
    ),
    "city_one_side": Tile(
        description="city_top",
        city=[[Side.TOP]],
        grass=[Side.RIGHT, Side.BOTTOM, Side.LEFT],
        image="Base_Game_C2_Tile_E.jpg"
    ),
    "city_narrow_shield": Tile(
        description="city_narrow_shield",
        city=[[Side.LEFT, Side.RIGHT]],
        grass=[Side.TOP, Side.BOTTOM],
        shield=True,
        image="Base_Game_C2_Tile_F.jpg"
    ),
    "city_narrow": Tile(
        description="city_narrow",
        city=[[Side.LEFT, Side.RIGHT]],
        grass=[Side.TOP, Side.BOTTOM],
        image="Base_Game_C2_Tile_G.jpg"
    ),
    "city_left_right": Tile(
        description="city_left_right",
        city=[[Side.LEFT], [Side.RIGHT]],
        grass=[Side.TOP, Side.BOTTOM, Side.CENTER],
        image="Base_Game_C2_Tile_H.jpg"
    ),
    "city_top_right": Tile(
        description="city_top_right",
        city=[[Side.TOP], [Side.RIGHT]],
        grass=[Side.LEFT, Side.BOTTOM, Side.CENTER],
        image="Base_Game_C2_Tile_I.jpg"
    ),
    "city_top_road_bend_right": Tile(
        description="city_top_road_bend_right",
        city=[[Side.TOP]],
        road=[Connection(Side.BOTTOM, Side.RIGHT)],
        grass=[Side.LEFT],
        image="Base_Game_C2_Tile_J.jpg"
    ),
    "city_top_road_bend_left": Tile(
        description="city_top_road_bend_left",
        city=[[Side.TOP]],
        road=[Connection(Side.BOTTOM, Side.LEFT)],
        grass=[Side.RIGHT],
        image="Base_Game_C2_Tile_K.jpg"
    ),
    "city_top_crossroads": Tile(
        description="city_top_crossroads",
        city=[[Side.TOP]],
        road=[
            Connection(Side.BOTTOM, Side.CENTER),
            Connection(Side.LEFT, Side.CENTER),
            Connection(Side.RIGHT, Side.CENTER)
        ],
        image="Base_Game_C2_Tile_L.jpg"
    ),
    "city_diagonal_top_right_shield": Tile(
        description="city_diagonal_top_right_shields",
        city=[[Side.TOP, Side.RIGHT]],
        grass=[Side.LEFT, Side.BOTTOM],
        shield=True,
        image="Base_Game_C2_Tile_M.jpg"
    ),
    "city_diagonal_top_right": Tile(
        description="city_diagonal_top_right",
        city=[[Side.TOP, Side.RIGHT]],
        grass=[Side.LEFT, Side.BOTTOM],
        image="Base_Game_C2_Tile_N.jpg"
    ),
    "city_diagonal_top_left_shield_road": Tile(
        description="city_diagonal_top_left_shield_road",
        road=[Connection(Side.BOTTOM, Side.RIGHT)],
        city=[[Side.TOP, Side.LEFT]],
        shield=True,
        image="Base_Game_C2_Tile_O.jpg"
    ),
    "city_diagonal_top_left_road": Tile(
        description="city_diagonal_top_left_shield_road",
        road=[Connection(Side.BOTTOM, Side.RIGHT)],
        city=[[Side.TOP, Side.LEFT]],
        image="Base_Game_C2_Tile_P.jpg"
    ),
    "city_bottom_grass_shield": Tile(
        description="city_bottom_grass_shield",
        city=[[Side.TOP, Side.LEFT, Side.RIGHT]],
        grass=[Side.BOTTOM],
        shield=True,
        image="Base_Game_C2_Tile_Q.jpg"
    ),
    "city_bottom_grass": Tile(
        description="city_bottom_grass",
        city=[[Side.TOP, Side.LEFT, Side.RIGHT]],
        grass=[Side.BOTTOM],
        image="Base_Game_C2_Tile_R.jpg"
    ),
    "city_bottom_road_shield": Tile(
        description="city_bottom_road_shield",
        city=[[Side.TOP, Side.LEFT, Side.RIGHT]],
        road=[Connection(Side.BOTTOM, Side.CENTER)],
        shield=True,
        image="Base_Game_C2_Tile_S.jpg"
    ),
    "city_bottom_road": Tile(
        description="city_bottom_road",
        city=[[Side.TOP, Side.LEFT, Side.RIGHT]],
        road=[Connection(Side.BOTTOM, Side.CENTER)],
        image="Base_Game_C2_Tile_T.jpg"
    ),
    "straight_road": Tile(
        description="straight_road",
        road=[Connection(Side.BOTTOM, Side.TOP)],
        grass=[Side.LEFT, Side.RIGHT],
        image="Base_Game_C2_Tile_U.jpg"
    ),
    "bent_road": Tile(
        description="bent_road",
        road=[Connection(Side.LEFT, Side.BOTTOM)],
        grass=[Side.TOP, Side.RIGHT],
        image="Base_Game_C2_Tile_V.jpg"
    ),
    "three_split_road": Tile(
        description="three_split_road",
        road=[
            Connection(Side.BOTTOM, Side.CENTER),
            Connection(Side.LEFT, Side.CENTER),
            Connection(Side.RIGHT, Side.CENTER)
        ],
        grass=[Side.TOP],
        image="Base_Game_C2_Tile_W.jpg"
    ),
    "crossroads": Tile(
        description="crossroads",
        road=[
            Connection(Side.BOTTOM, Side.CENTER),
            Connection(Side.LEFT, Side.CENTER),
            Connection(Side.RIGHT, Side.CENTER),
            Connection(Side.TOP, Side.CENTER)
        ],
        image="Base_Game_C2_Tile_X.jpg"
    )
}

base_tile_counts = {
    "chapel_with_road": 2,
    "chapel": 4,
    "full_city_with_shield": 1,
    "city_one_side_straight_road": 4,
    "city_one_side": 5,
    "city_narrow_shield": 2,
    "city_narrow": 1,
    "city_left_right": 3,
    "city_top_right": 2,
    "city_top_road_bend_right": 3,
    "city_top_road_bend_left": 3,
    "city_top_crossroads": 3,
    "city_diagonal_top_right_shield": 2,
    "city_diagonal_top_right": 3,
    "city_diagonal_top_left_shield_road": 2,
    "city_diagonal_top_left_road": 3,
    "city_bottom_grass_shield": 1,
    "city_bottom_grass": 3,
    "city_bottom_road_shield": 2,
    "city_bottom_road": 1,
    "straight_road": 8,
    "bent_road": 9,
    "three_split_road": 4,
    "crossroads": 1
}