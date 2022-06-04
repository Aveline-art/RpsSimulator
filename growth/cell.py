from typing import Union


class Cell():
    def __init__(self, type: Union[int, str], enemies: list[any]) -> None:
        self.type = type
        self.enemies = enemies

    def surrounded(self, neighbors: list[any], threshold=2) -> bool:
        neighboring_enemies = len(
            [neighbor for neighbor in neighbors if neighbor in self.enemies])
        if neighboring_enemies >= threshold:
            return True
        else:
            return False
