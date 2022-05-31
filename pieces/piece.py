import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, symbol: str) -> None:
        super().__init__() 
        self.symbol = symbol
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()
    
    def move(self):
        pass
