import json
import sys
from typing import Set
import numpy as np

from wingedsheep.carcassonne.objects.connection import Connection
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection
from wingedsheep.carcassonne.objects.side import Side
from wingedsheep.carcassonne.objects.terrain_type import TerrainType
from wingedsheep.carcassonne.utils.side_modification_util import SideModificationUtil

np.set_printoptions(suppress=True, linewidth=np.nan, threshold=sys.maxsize)


class Tile:
    def __init__(self,
                 description: str = "",
                 turns: int = 0,
                 road: [Connection] = (),
                 river: [Connection] = (),
                 city: [[Side]] = (),
                 grass: [Side] = (),
                 farms: [FarmerConnection] = (),
                 shield: bool = False,
                 chapel: bool = False,
                 flowers: bool = False,
                 inn: [Side] = (),
                 cathedral: bool = False,
                 unplayable_sides: [Side] = (),
                 image: str = "Empty.png"):
        self.description = description
        self.turns = turns
        self.road = road
        self.river = river
        self.city = city
        self.grass = grass
        self.farms: [FarmerConnection] = farms
        self.shield = shield
        self.chapel = chapel
        self.flowers = flowers
        self.inn = inn
        self.cathedral = cathedral
        self.unplayable_sides = unplayable_sides
        self.image = image

    def get_road_ends(self) -> Set[Side]:
        sides: Set[Side] = set([])
        for road in self.road:
            sides.add(road.a)
            sides.add(road.b)
        return set(sides)

    def get_river_ends(self) -> Set[Side]:
        sides: Set[Side] = set([])
        for road in self.river:
            sides.add(road.a)
            sides.add(road.b)
        return set(sides)

    def get_city_sides(self) -> Set[Side]:
        sides: Set[Side] = set([])
        for side_list in self.city:
            for side in side_list:
                sides.add(side)
        return set(sides)

    def has_river(self) -> bool:
        return len(self.river) > 0

    def get_type(self, side: Side):
        if self.unplayable_sides.__contains__(side):
            return TerrainType.UNPLAYABLE

        if side == Side.CENTER and self.chapel:
            return TerrainType.CHAPEL

        if side == Side.CENTER and self.flowers:
            return TerrainType.FLOWERS

        if self.get_river_ends().__contains__(side):
            return TerrainType.UNPLAYABLE

        if self.get_road_ends().__contains__(side):
            return TerrainType.ROAD

        if self.get_city_sides().__contains__(side):
            return TerrainType.CITY

        if self.grass.__contains__(side):
            return TerrainType.GRASS

    def to_json(self):
        return {
            "description": self.description,
            "river": list(map(lambda x: x.to_json(), self.river)),
            "road": list(map(lambda x: x.to_json(), self.road)),
            "city": list(map(lambda x: x.to_json(), self.city)),
            "grass": list(map(lambda x: x.to_json(), self.grass)),
            "farms": list(map(lambda x: x.to_json(), self.farms)),
            "shield": self.shield,
            "chapel": self.chapel,
            "flowers": self.flowers,
            "inn": list(map(lambda x: x.to_json(), self.inn)),
            "unplayable_sides": list(map(lambda x: x.to_json(), self.unplayable_sides))
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)

    def turn(self, times: int):
        return Tile(
            description=self.description,
            turns=times,
            road=list(map(lambda x: SideModificationUtil.turn_connection(x, times), self.road)),
            river=list(map(lambda x: SideModificationUtil.turn_connection(x, times), self.river)),
            city=list(map(lambda x: SideModificationUtil.turn_sides(x, times), self.city)),
            grass=list(map(lambda x: SideModificationUtil.turn_side(x, times), self.grass)),
            farms=list(map(lambda x: SideModificationUtil.turn_farmer_connection(x, times), self.farms)),
            shield=self.shield,
            chapel=self.chapel,
            flowers=self.flowers,
            inn=list(map(lambda x: SideModificationUtil.turn_side(x, times), self.inn)),
            unplayable_sides=list(map(lambda x: SideModificationUtil.turn_side(x, times), self.unplayable_sides)),
            image=self.image
        )
