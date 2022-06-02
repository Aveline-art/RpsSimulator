import pygame
from hands import Hand, Rock, Paper, Scissors


class RPS():

    def __init__(self) -> None:
        self.rock = Rock()
        self.paper = Paper()
        self.scissors = Scissors()

        def create_collide(opposing_hand: Hand):
            lambda kill=False: \
                pygame.sprite.groupcollide(
                    self.group, opposing_hand.group, kill, False)

        self.rock.collide = create_collide(self.paper)
        self.paper.collide = create_collide(self.scissors)
        self.scissors.collide = create_collide(self.rock)

    @property
    def all_sprites(self):
        sprites = self.rock.group.sprites() + self.paper.group.sprites() + \
            self.scissors.group.sprites()
        return sprites

    def create(self, num: int = 1):
        for i in range(num):
            self.rock.group.add(self.rock.create())
            self.paper.group.add(self.paper.create())
            self.scissors.group.add(self.scissors.create())
