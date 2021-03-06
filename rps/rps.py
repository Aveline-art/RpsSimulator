from typing import Any, Callable, Optional
import pygame
from rps.hands import Rock, Paper, Scissors
from rps.pieces import Piece
from rps.rpstypes import Direction, Location


class RPS():
    directions = Piece.directions

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
        elif not isinstance(num, int):
            raise TypeError('num must be an int')
        self.rock.group.add(self.rock.create(num=num))
        self.paper.group.add(self.paper.create(num=num))
        self.scissors.group.add(self.scissors.create(num=num))

    def create_loses_to(self,
                        sprite: Piece,
                        center: Optional[Location] = None) -> Piece:
        if sprite.symbol == self.rock.piece.symbol:
            return self.paper.create(center)
        elif sprite.symbol == self.paper.piece.symbol:
            return self.scissors.create(center)
        else:
            return self.rock.create(center)

    def collide(self, kill: bool = False) -> \
            dict[pygame.sprite.Group, list[pygame.sprite.Group]]:
        rock_on_paper = self.rock.collide(True)
        paper_on_scissors = self.paper.collide(True)
        scissors_on_rock = self.scissors.collide(True)
        return rock_on_paper | paper_on_scissors | scissors_on_rock

    def prototype_move(self, func: Callable[[Any], Direction]) -> None:
        wrapped = self._move_wrapper(func)
        self.rock.piece._move = wrapped
        self.paper.piece._move = wrapped
        self.scissors.piece._move = wrapped

    def _move_wrapper(self, func):
        def new_func(self, *args, **kwargs):
            # TODO insert some useful self variables (maybe as keywords)
            # as arguments into func
            return func(*args, **kwargs)
        return new_func
