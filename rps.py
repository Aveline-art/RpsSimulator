from typing import Optional, Tuple
import pygame
from hands import Rock, Paper, Scissors
from pieces import Piece


class RPS():

    def __init__(self) -> None:
        self.rock = Rock()
        self.paper = Paper()
        self.scissors = Scissors()

        def create_collide(hand, opposing_hand):
            return lambda kill=False: pygame.sprite.groupcollide(
                hand.group, opposing_hand.group, kill, False)

        self.rock.collide = create_collide(self.rock, self.paper)
        self.paper.collide = create_collide(self.paper, self.scissors)
        self.scissors.collide = create_collide(self.scissors, self.rock)

    @property
    def all_sprites(self) -> list[pygame.sprite.Group]:
        sprites = self.rock.group.sprites() + self.paper.group.sprites() + \
            self.scissors.group.sprites()
        return sprites

    def create(self, num: int = 1) -> None:
        if num < 1:
            raise ValueError('num cannot be less than 1')
        for i in range(num):
            self.rock.group.add(self.rock.create())
            self.paper.group.add(self.paper.create())
            self.scissors.group.add(self.scissors.create())

    def create_loses_to(self,
                        sprite: Piece,
                        center: Optional[Tuple[int, int]] = None) -> Piece:
        if sprite.symbol == self.rock.piece.symbol:
            return self.paper.create(center)
        elif sprite.symbol == self.paper.piece.symbol:
            return self.scissors.create(center)
        else:
            return self.rock.create(center)
