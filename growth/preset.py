from dataclasses import dataclass

FPS = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FONT = "Verdana"


@dataclass
class color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


DISTRIBUTION = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
}
