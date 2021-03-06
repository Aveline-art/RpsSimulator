from typing import Optional
import pygame
from rps.pieces import Piece, Rock_Piece, Paper_Piece, Scissors_Piece
from rps.rpstypes import Location


class Hand():
    piece: Piece

    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def collide(self, kill: bool = False) -> \
            dict[pygame.sprite.Group, list[pygame.sprite.Group]]:
        raise NotImplementedError

    def create(self,
               center: Optional[Location] = None,
               num: int = 1
               ) -> list[Piece]:
        if num < 1:
            raise ValueError('num cannot be less than 1')
        elif not isinstance(num, int):
            raise TypeError('num must be an int')
        pieces = []
        for i in range(num):
            piece = self.piece.create(center)
            self.group.add(piece)
            pieces.append(piece)
        return pieces


class Rock(Hand):
    piece = Rock_Piece


class Paper(Hand):
    piece = Paper_Piece


class Scissors(Hand):
    piece = Scissors_Piece
