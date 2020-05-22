import os

from wingedsheep.carcassonne.objects.connection import Connection
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection
from wingedsheep.carcassonne.objects.farmer_side import FarmerSide
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.objects.tile import Tile

the_river_tiles = {
    "river_start": Tile(
        description="river_start",
        river=[
            Connection(Side.CENTER, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT, Side.TOP],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT,
                    Side.TOP_RIGHT,
                    Side.BOTTOM_LEFT,
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRT, FarmerSide.TRR,
                    FarmerSide.BRR, FarmerSide.BRB,
                    FarmerSide.BLB, FarmerSide.BLL
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_A.png")
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
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLB, FarmerSide.BLL
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRB, FarmerSide.BRR
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL
                ],
                city_sides=[
                    Side.TOP
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR
                ],
                city_sides=[
                    Side.TOP
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_B.png")
    ),
    "river_double_city": Tile(
        description="river_double_city",
        river=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        city=[[Side.TOP], [Side.BOTTOM]],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLL,
                    FarmerSide.BRR
                ],
                city_sides=[
                    Side.BOTTOM
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL,
                    FarmerSide.TRR
                ],
                city_sides=[
                    Side.TOP
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_C.png")
    ),
    "river_straight": Tile(
        description="river_straight",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.BLL, FarmerSide.BLB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_D.png")
    ),
    "river_diagonal_city": Tile(
        description="river_diagonal_city",
        river=[
            Connection(Side.LEFT, Side.BOTTOM),
        ],
        city=[[Side.TOP, Side.RIGHT]],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL,
                    FarmerSide.BLB
                ],
                city_sides=[
                    Side.TOP,
                    Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_E.png")
    ),
    "river_straight_2": Tile(
        description="river_straight_2",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.RIGHT],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.BLL, FarmerSide.BLB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_F.png")
    ),
    "river_bend": Tile(
        description="river_bend",
        river=[
            Connection(Side.TOP, Side.LEFT),
        ],
        grass=[Side.RIGHT, Side.BOTTOM],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT, Side.BOTTOM_RIGHT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR, FarmerSide.BRB,
                    FarmerSide.BLL, FarmerSide.BLB
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_G.png")
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
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            )
        ],
        chapel=True,
        image=os.path.join("the_river", "River_III_C2_Tile_H.png")
    ),
    "river_bend_with_road": Tile(
        description="river_bend_with_road",
        river=[
            Connection(Side.RIGHT, Side.BOTTOM),
        ],
        road=[
            Connection(Side.LEFT, Side.TOP),
        ],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB,
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_I.png")
    ),
    "river_flowery_bend": Tile(
        description="river_flowery_bend",
        river=[
            Connection(Side.RIGHT, Side.BOTTOM),
        ],
        grass=[Side.LEFT, Side.TOP],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.BOTTOM_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB,
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.TLL, FarmerSide.TLT
                ]
            )
        ],
        flowers=True,
        image=os.path.join("the_river", "River_III_C2_Tile_J.png")
    ),
    "river_crossing": Tile(
        description="river_crossing",
        river=[
            Connection(Side.TOP, Side.BOTTOM),
        ],
        road=[
            Connection(Side.LEFT, Side.RIGHT),
        ],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLB, FarmerSide.BLL
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRB, FarmerSide.BRR
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            )
        ],
        image=os.path.join("the_river", "River_III_C2_Tile_K.png")
    ),
    "river_end": Tile(
        description="river_end",
        river=[
            Connection(Side.TOP, Side.CENTER),
        ],
        grass=[Side.LEFT, Side.RIGHT, Side.BOTTOM],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT,
                    Side.TOP_RIGHT,
                    Side.BOTTOM_LEFT,
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRT, FarmerSide.TRR,
                    FarmerSide.BRR, FarmerSide.BRB,
                    FarmerSide.BLB, FarmerSide.BLL
                ]
            )
        ],
        image=os.path.join("the_river", "River_I_C2_Tile_L.png")
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