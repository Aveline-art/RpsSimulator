import pygame
import random
from typing import Optional, Tuple
from enum import Enum, unique
import preset

pygame.init()

font = pygame.font.SysFont("Verdana", 12)

@unique
class Symbol(Enum):
    ROCK = "RO"
    PAPER = "PA"
    SCISSORS = "SC"


class Piece(pygame.sprite.Sprite):
    direction = {
        1: (0, 5),
        2: (5, 5),
        3: (5, 0),
        4: (5, -5),
        5: (0, -5),
        6: (-5, -5),
        7: (-5, 0),
        8: (-5, 5),
    }

    def __init__(self, symbol: Symbol, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__() 
        self.symbol = symbol
        self.image = font.render(symbol.value, True, preset.color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center or (random.randint(0, preset.SCREEN_WIDTH), random.randint(0, preset.SCREEN_HEIGHT))

    def move(self):
        val = random.randint(1, 8)
        self.rect.move_ip(self.direction[val])

class Rock_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Symbol.ROCK, center)
        self.image = pygame.image.load('assets/rock.png')

class Paper_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Symbol.PAPER, center)
        self.image = pygame.image.load('assets/paper.png')

class Scissors_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Symbol.SCISSORS, center)
        self.image = pygame.image.load('assets/scissors.png')