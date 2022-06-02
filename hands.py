import pygame
from pieces import Piece, Rock_Piece, Paper_Piece, Scissors_Piece


class Hand():
    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def collide(self):
        raise NotImplementedError

    def create(self) -> Piece:
        piece = self.piece.create()
        self.group.add(piece)
        return piece


class Rock(Hand):
    piece = Rock_Piece

    def __init__(self) -> None:
        super().__init__()


class Paper(Hand):
    piece = Paper_Piece

    def __init__(self) -> None:
        super().__init__()


class Scissors(Hand):
    piece = Scissors_Piece

    def __init__(self) -> None:
        super().__init__()
