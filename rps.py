from pieces import *
import pygame
from pygame.sprite import Sprite

class RPS():
    def __init__(self) -> None:
        self.Rock = Piece_Organizer(Rock_Piece)
        self.Paper = Piece_Organizer(Paper_Piece)
        self.Scissors = Piece_Organizer(Scissors_Piece)
        self.Rock.add_loses(self.Paper)
        self.Paper.add_loses(self.Scissors)
        self.Scissors.add_loses(self.Rock)
    
    @property
    def all_sprites(self):
        return self.Rock.group.sprites() + self.Paper.group.sprites() + self.Scissors.group.sprites()
    
    def create(self, num: int = 1):
        self.Rock.create(num)
        self.Paper.create(num)
        self.Scissors.create(num)
    
    def wins(self, symbol: Symbol):
        if symbol == Symbol.ROCK:
            return self.Paper
        elif symbol == Symbol.PAPER:
            return self.Scissors
        else:
            return self.Rock

class Piece_Organizer():
    def __init__(self, piece_class: Piece) -> None:
        self.group = pygame.sprite.Group()
        self.piece_class = piece_class
    
    def create(self, num_create: int = 1, center: Optional[Tuple[int, int]] = None) -> None:
        added = []
        for i in range (num_create):
            piece = self.piece_class(center)
            added.append(piece)
            self.group.add(piece)
        
        if num_create == 1:
            return piece
        else:
            return added
    
    def add_loses(self, organizer):
        self.loses_to = organizer
    
    def collide(self, kill = False) -> dict[Sprite, list[Sprite]]:
        return pygame.sprite.groupcollide(self.group, self.loses_to.group, kill, False)