import pygame
import random
from typing import Optional
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
    def __init__(self, symbol: Symbol, image: Optional[str] = None) -> None:
        super().__init__() 
        self.symbol = symbol.value
        self.image = pygame.image.load(image) if image else font.render(symbol.value, True, preset.color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 600), random.randint(0, 600))  
    
    def move(self):
        pass

class Rock_Piece(Piece):
    def __init__(self) -> None:
        super().__init__(Symbol.ROCK)

class Paper_Piece(Piece):
    def __init__(self) -> None:
        super().__init__(Symbol.PAPER)

class Scissor_Piece(Piece):
    def __init__(self) -> None:
        super().__init__(Symbol.SCISSORS)
