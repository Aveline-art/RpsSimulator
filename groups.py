import pygame
from pieces import Rock_Piece, Paper_Piece, Scissors_Piece


class Group():
    def __init__(self) -> None:
        self.group = pygame.sprite.Group()
