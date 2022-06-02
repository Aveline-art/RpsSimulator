import pygame
from pieces import Rock_Piece, Paper_Piece, Scissors_Piece


class Hand():
    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def collide(self):
        raise NotImplementedError


class Rock(Hand):
    piece = Rock_Piece
    create = Rock_Piece.create

    def __init__(self) -> None:
        pass


class Paper(Hand):
    piece = Paper_Piece
    create = Paper_Piece.create

    def __init__(self) -> None:
        pass


class Scissors(Hand):
    piece = Scissors_Piece
    create = Scissors_Piece.create

    def __init__(self) -> None:
        pass
