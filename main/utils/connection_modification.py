from main.objects.connection import Connection
from main.utils.side_modification import turn_side


def turn_connection(connection: Connection, times: int) -> Connection:
    return Connection(turn_side(connection.a, times), turn_side(connection.b, times))
