import pygame
from pieces import Rock_Piece, Paper_Piece, Scissors_Piece


class Hand():
    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def collide(self):
        raise NotImplementedError

    def add_opposing_group(self, hand):
        self._generate_collide(hand.group)

    def _generate_collide(self, opposing_group):
        self.collide = lambda kill=False: \
            pygame.sprite.groupcollide(self.group, opposing_group, kill, False)


class Rock():
    piece = Rock_Piece
    create = Rock_Piece.create

    def __init__(self) -> None:
        pass


class Paper():
    piece = Paper_Piece
    create = Paper_Piece.create

    def __init__(self) -> None:
        pass


class Scissors():
    piece = Scissors_Piece
    create = Scissors_Piece.create

    def __init__(self) -> None:
        pass
