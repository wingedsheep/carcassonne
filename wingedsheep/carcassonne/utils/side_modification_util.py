from wingedsheep.carcassonne.objects.connection import Connection
from wingedsheep.carcassonne.objects.farmer_connection import FarmerConnection
from wingedsheep.carcassonne.objects.farmer_side import FarmerSide
from wingedsheep.carcassonne.objects.side import Side

class SideModificationUtil:

    @classmethod
    def turn_side(cls, side: Side, times: int) -> Side:
        result: Side

        if times == 0:
            return side

        if side == Side.TOP:
            result = Side.RIGHT
        elif side == Side.RIGHT:
            result = Side.BOTTOM
        elif side == Side.BOTTOM:
            result = Side.LEFT
        elif side == Side.LEFT:
            result = Side.TOP
        elif side == Side.CENTER:
            result = Side.CENTER
        elif side == Side.TOP_LEFT:
            result = Side.TOP_RIGHT
        elif side == Side.TOP_RIGHT:
            result = Side.BOTTOM_RIGHT
        elif side == Side.BOTTOM_RIGHT:
            result = Side.BOTTOM_LEFT
        else:  # side == Side.BOTTOM_LEFT
            result = Side.TOP_LEFT

        if times > 1:
            return cls.turn_side(result, times - 1)

        return result

    @classmethod
    def opposite_side(cls, side: Side):
        return cls.turn_side(side, 2)

    @classmethod
    def turn_sides(cls, sides: [Side], times: int):
        return list(map(lambda side: cls.turn_side(side, times), sides))

    @classmethod
    def turn_farmer_side(cls, farmer_side: FarmerSide, times: int) -> FarmerSide:
        result: FarmerSide

        if times == 0:
            return farmer_side

        if farmer_side == FarmerSide.TLL:
            result = FarmerSide.TRT
        elif farmer_side == FarmerSide.TLT:
            result = FarmerSide.TRR
        elif farmer_side == FarmerSide.TRT:
            result = FarmerSide.BRR
        elif farmer_side == FarmerSide.TRR:
            result = FarmerSide.BRB
        elif farmer_side == FarmerSide.BRR:
            result = FarmerSide.BLB
        elif farmer_side == FarmerSide.BRB:
            result = FarmerSide.BLL
        elif farmer_side == FarmerSide.BLB:
            result = FarmerSide.TLL
        else:  # farmer_side == FarmerSide.BLL:
            result = FarmerSide.TLT

        if times > 1:
            return cls.turn_farmer_side(result, times - 1)

        return result

    @classmethod
    def turn_farmer_sides(cls, farmer_sides: [FarmerSide], times: int) -> [FarmerSide]:
        return list(map(lambda farmer_side: cls.turn_farmer_side(farmer_side, times), farmer_sides))

    @classmethod
    def opposite_farmer_side(cls, farmer_side: FarmerSide) -> FarmerSide:
        if farmer_side == FarmerSide.TLL:
            return FarmerSide.TRR
        elif farmer_side == FarmerSide.TLT:
            return FarmerSide.BLB
        elif farmer_side == FarmerSide.TRT:
            return FarmerSide.BRR
        elif farmer_side == FarmerSide.TRR:
            return FarmerSide.TLL
        elif farmer_side == FarmerSide.BRR:
            return FarmerSide.BLL
        elif farmer_side == FarmerSide.BRB:
            return FarmerSide.TRT
        elif farmer_side == FarmerSide.BLB:
            return FarmerSide.TLT
        else:  # farmer_side == FarmerSide.BLL:
            return FarmerSide.BRR

    @classmethod
    def turn_farmer_connection(cls, farmer_connection: FarmerConnection, times: int):
        return FarmerConnection(
            farmer_positions=cls.turn_sides(farmer_connection.farmer_positions, times),
            tile_connections=cls.turn_farmer_sides(farmer_connection.tile_connections, times),
            city_sides=cls.turn_sides(farmer_connection.city_sides, times)
        )

    @classmethod
    def turn_connection(cls, connection: Connection, times: int) -> Connection:
        return Connection(cls.turn_side(connection.a, times), cls.turn_side(connection.b, times))
