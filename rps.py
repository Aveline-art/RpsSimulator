import pygame
from pieces import Rock, Paper, Scissors


class RPS():
    rock = Rock
    paper = Paper
    scissors = Scissors

    def __init__(self) -> None:
        self.rock.group = pygame.sprite.Group()
        self.paper.group = pygame.sprite.Group()
        self.scissors.group = pygame.sprite.Group()

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
