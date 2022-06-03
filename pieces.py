import pygame
import random
from typing import Optional
import preset
from rpstypes import Location


class Piece(pygame.sprite.Sprite):
    name: str
    symbol: str
    directions = {
        'SO': (0, 5),
        'SE': (5, 5),
        'EA': (5, 0),
        'NE': (5, -5),
        'NO': (0, -5),
        'NW': (-5, -5),
        'WE': (-5, 0),
        'SW': (-5, 5),
        'CE': (0, 0),
    }

    def __init__(self, image_path: str,
                 center: Optional[Location] = None) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = center or (random.randint(
            0, preset.SCREEN_WIDTH), random.randint(0, preset.SCREEN_HEIGHT))

    def move(self, *args, **kwargs) -> None:
        direction = self._move(self, *args, **kwargs) or random.choice(
            list(self.directions.values()))
        self.rect.move_ip(direction)

    @classmethod
    def create(cls, center: Optional[Location] = None) -> 'Piece':
        return cls(center)

    def _move(self, *args, **kwargs) -> None:
        return None


class Rock_Piece(Piece):
    name = 'Rock'
    symbol = "RO"

    def __init__(self, center: Optional[Location] = None) -> None:
        super().__init__('assets/rock.png', center)

    @staticmethod
    def wins_against() -> 'Scissors_Piece':
        return Scissors_Piece

    @staticmethod
    def loses_to() -> 'Paper_Piece':
        return Paper_Piece


class Paper_Piece(Piece):
    name = 'Paper'
    symbol = "PA"

    def __init__(self, center: Optional[Location] = None) -> None:
        super().__init__('assets/paper.png', center)

    @staticmethod
    def wins_against() -> Rock_Piece:
        return Rock_Piece

    @staticmethod
    def loses_to() -> 'Scissors_Piece':
        return Scissors_Piece


class Scissors_Piece(Piece):
    name = 'Scissors'
    symbol = "SC"

    def __init__(self, center: Optional[Location] = None) -> None:
        super().__init__('assets/scissors.png', center)

    @staticmethod
    def wins_against() -> Paper_Piece:
        return Paper_Piece

    @staticmethod
    def loses_to() -> Rock_Piece:
        return Rock_Piece
