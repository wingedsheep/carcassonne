import os

from wingedsheep.carcassonne.objects.connection import Connection
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection
from wingedsheep.carcassonne.objects.farmer_side import FarmerSide
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.objects.tile import Tile

inns_and_cathedrals_tiles = {
    "ic_1": Tile(
        description="ic_1",
        grass=[Side.TOP],
        city=[[Side.LEFT, Side.BOTTOM], [Side.RIGHT]],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLT, FarmerSide.TRT
                ],
                city_sides=[
                    Side.LEFT,
                    Side.RIGHT,
                    Side.BOTTOM
                ]
            )
        ],
        shield=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_1.png")
    ),
    "ic_2": Tile(
        description="ic_2",
        grass=[Side.TOP, Side.RIGHT],
        road=[Connection(Side.BOTTOM, Side.LEFT)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR, FarmerSide.BRB
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
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_2.png")
    ),
    "ic_3": Tile(
        description="ic_3",
        road=[Connection(Side.BOTTOM, Side.RIGHT), Connection(Side.TOP, Side.LEFT)],
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
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_3.png")
    ),
    "ic_4": Tile(
        description="ic_4",
        city=[[Side.LEFT, Side.RIGHT]],
        road=[Connection(Side.TOP, Side.CENTER), Connection(Side.BOTTOM, Side.CENTER)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLT
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRT
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLB
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRB
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_4.png")
    ),
    "ic_5": Tile(
        description="ic_5",
        city=[[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]],
        cathedral=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_5.png")
    ),
    "ic_6": Tile(
        description="ic_6",
        city=[[Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT]],
        cathedral=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_6.png")
    ),
    "ic_7": Tile(
        description="ic_7",
        city=[[Side.TOP], [Side.RIGHT], [Side.LEFT]],
        grass=[Side.BOTTOM],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLB, FarmerSide.BRB
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT, Side.TOP
                ]
            ),
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_7.png")
    ),
    "ic_8": Tile(
        description="ic_8",
        city=[[Side.TOP], [Side.RIGHT], [Side.LEFT], [Side.BOTTOM]],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.CENTER
                ],
                city_sides=[
                    Side.LEFT, Side.RIGHT, Side.TOP, Side.BOTTOM
                ]
            ),
        ],
        flowers=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_8.png")
    ),
    "ic_9": Tile(
        description="ic_9",
        grass=[Side.TOP, Side.BOTTOM],
        road=[Connection(Side.LEFT, Side.RIGHT)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB,
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            )
        ],
        flowers=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_9.png")
    ),
    "ic_10": Tile(
        description="ic_10",
        city=[[Side.LEFT]],
        grass=[Side.TOP],
        road=[Connection(Side.BOTTOM, Side.RIGHT)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BLB
                ],
                city_sides=[
                    Side.LEFT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_10.png")
    ),
    "ic_11": Tile(
        description="ic_11",
        city=[[Side.LEFT, Side.TOP]],
        grass=[Side.BOTTOM],
        road=[Connection(Side.CENTER, Side.RIGHT)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR
                ],
                city_sides=[
                    Side.TOP, Side.LEFT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BRR, FarmerSide.BRB,
                    FarmerSide.BLB
                ],
                city_sides=[
                    Side.TOP, Side.LEFT
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_11.png")
    ),
    "ic_12": Tile(
        description="ic_12",
        city=[[Side.RIGHT, Side.TOP]],
        grass=[Side.BOTTOM],
        road=[Connection(Side.CENTER, Side.LEFT)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL
                ],
                city_sides=[
                    Side.TOP, Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BRB,
                    FarmerSide.BLL, FarmerSide.BLB
                ],
                city_sides=[
                    Side.TOP, Side.RIGHT
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_12.png")
    ),
    "ic_13": Tile(
        description="ic_13",
        city=[[Side.BOTTOM]],
        grass=[Side.LEFT, Side.RIGHT, Side.TOP],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.TLL
                ],
                city_sides=[
                    Side.BOTTOM
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR
                ],
                city_sides=[
                    Side.BOTTOM
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_13.png")
    ),
    "ic_14": Tile(
        description="ic_14",
        city=[[Side.BOTTOM, Side.RIGHT]],
        road=[Connection(Side.TOP, Side.LEFT)],
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
                    Side.TOP_RIGHT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TRT,
                    FarmerSide.BLL
                ],
                city_sides=[
                    Side.BOTTOM, Side.RIGHT
                ]
            )
        ],
        shield=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_14.png")
    ),
    "ic_15": Tile(
        description="ic_15",
        city=[[Side.BOTTOM]],
        road=[Connection(Side.TOP, Side.CENTER)],
        grass=[Side.LEFT, Side.RIGHT],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.BLL
                ],
                city_sides=[
                    Side.BOTTOM
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRR, FarmerSide.TRT,
                    FarmerSide.BRR
                ],
                city_sides=[
                    Side.BOTTOM
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_15.png")
    ),
    "ic_16": Tile(
        description="ic_16",
        city=[[Side.LEFT], [Side.RIGHT]],
        road=[Connection(Side.TOP, Side.CENTER), Connection(Side.BOTTOM, Side.CENTER)],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT
                ],
                tile_connections=[
                    FarmerSide.TLT
                ],
                city_sides=[
                    Side.LEFT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TRT
                ],
                city_sides=[
                    Side.RIGHT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT
                ],
                tile_connections=[
                    FarmerSide.BLB
                ],
                city_sides=[
                    Side.LEFT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BRB
                ],
                city_sides=[
                    Side.RIGHT
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_16.png")
    ),
    "ic_17": Tile(
        description="ic_17",
        road=[Connection(Side.LEFT, Side.CENTER), Connection(Side.RIGHT, Side.CENTER)],
        grass=[Side.TOP, Side.BOTTOM],
        farms=[
            FarmerConnection(
                farmer_positions=[
                    Side.TOP_LEFT, Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            ),
            FarmerConnection(
                farmer_positions=[
                    Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT
                ],
                tile_connections=[
                    FarmerSide.BLL, FarmerSide.BLB,
                    FarmerSide.BRR, FarmerSide.BRB
                ]
            )
        ],
        chapel=True,
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_17.png")
    ),
    "ic_18": Tile(
        description="ic_18",
        road=[
            Connection(Side.LEFT, Side.CENTER),
            Connection(Side.RIGHT, Side.CENTER),
            Connection(Side.BOTTOM, Side.CENTER)
        ],
        grass=[Side.TOP],
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
                    Side.TOP_LEFT,
                    Side.TOP_RIGHT
                ],
                tile_connections=[
                    FarmerSide.TLL, FarmerSide.TLT,
                    FarmerSide.TRR, FarmerSide.TRT
                ]
            )
        ],
        image=os.path.join("inns_and_cathedrals", "inns_cathedrals_18.png")
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