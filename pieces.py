import pygame
import random
from typing import Optional, Tuple
import preset
from hands import Hand, Rock_Hand, Paper_Hand, Scissors_Hand

pygame.init()


class Piece(pygame.sprite.Sprite):
    direction = {
        1: (0, 5),
        2: (5, 5),
        3: (5, 0),
        4: (5, -5),
        5: (0, -5),
        6: (-5, -5),
        7: (-5, 0),
        8: (-5, 5),
    }

    def __init__(self, hand: Hand, image_path: str,
                 center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__()
        self.hand = hand
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = center or (random.randint(
            0, preset.SCREEN_WIDTH), random.randint(0, preset.SCREEN_HEIGHT))

    def move(self):
        val = random.randint(1, 8)
        self.rect.move_ip(self.direction[val])

    @classmethod
    def create(cls, center: Optional[Tuple[int, int]] = None):
        return cls(center)


class Rock_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Rock_Hand, 'assets/rock.png', center)


class Paper_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Paper_Hand, 'assets/paper.png', center)


class Scissors_Piece(Piece):
    def __init__(self, center: Optional[Tuple[int, int]] = None) -> None:
        super().__init__(Scissors_Hand, 'assets/paper.png', center)
