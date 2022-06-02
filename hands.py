from typing import Optional, Tuple
import pygame
from pieces import Piece, Rock_Piece, Paper_Piece, Scissors_Piece


class Hand():
    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def collide(self, kill: bool = False) -> \
            dict[pygame.sprite.Group, list[pygame.sprite.Group]]:
        raise NotImplementedError

    def create(self, center: Optional[Tuple[int, int]] = None) -> Piece:
        piece = self.piece.create(center)
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
