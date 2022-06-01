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
'''
piece_image = {
    'RO': pygame.image.load('assets/rock.png'),
    'PA': pygame.image.load('assets/paper.png'),
    'SC': pygame.image.load('assets/scissors.png'),
}'''


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
        self._symbol = symbol
        self.image = font.render(symbol.value, True, preset.color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center or (random.randint(0, preset.SCREEN_WIDTH), random.randint(0, preset.SCREEN_HEIGHT))
    
    @property
    def symbol(self):
        return self._symbol
    
    @symbol.setter
    def symbol(self, new_symbol: str):
        self._symbol = new_symbol
    
    def update_image(self):
        self.image = font.render(self.symbol.value, True, preset.color.BLACK)

    def move(self):
        val = random.randint(1, 8)
        self.rect.move_ip(self.direction[val])