from main.objects.side import Side


def opposite(side: Side) -> Side:
    return turn_side(side, 2)


def turn_side(side: Side, times: int) -> Side:
    result: Side

    if times == 0:
        return side

    if side == Side.TOP:
        result = Side.RIGHT
    if side == Side.RIGHT:
        result = Side.BOTTOM
    if side == Side.BOTTOM:
        result = Side.LEFT
    if side == Side.LEFT:
        result = Side.TOP
    if side == Side.CENTER:
        result = Side.CENTER

    if times > 1:
        return turn_side(result, times - 1)

    return result


def turn_sides(sides: [Side], times):
    return list(map(lambda side: turn_side(side, times), sides))
