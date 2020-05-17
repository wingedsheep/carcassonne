import json

from main.objects.side import Side


class Connection:
    def __init__(self, a: Side, b: Side):
        self.a = a
        self.b = b

    def to_json(self):
        return {
            "a": self.a.to_json(),
            "b": self.b.to_json()
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)
