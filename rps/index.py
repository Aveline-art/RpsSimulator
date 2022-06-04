# Imports
from typing import Optional
import pygame
import sys
from pygame.locals import QUIT
import rps.preset as preset
from rps.rps import RPS
from rps.rpstypes import Direction

# Initialzing
pygame.init()

# Setting up FPS
FramePerSec = pygame.time.Clock()

# Setting up Fonts
font = pygame.font.SysFont(preset.FONT, 60)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode(
    (preset.SCREEN_WIDTH, preset.SCREEN_WIDTH))

# Creating Sprites Groups
rps = RPS()
rps.create(30)
all_sprites = pygame.sprite.Group()
all_sprites.add(rps.all_sprites)

# Prototype Move


def move(self) -> Optional[Direction]:
    '''CREATE A MOVE FUNCTION HERE
    A move function controls how a sprite moves when its move() function
    is called. Its first argument is always the sprite object itself. This
    means that it has access to all of its own functions and properties. In
    addition, the move function can take any number of positional and keyword
    arguments, but must return a Direction object, which is
    Tuple[Literal[-5, 0, 5], Literal[-5, 0, 5]], or None. If a Direction is
    returned, then the sprites will move in accordance with that direction. If
    None is returned, then the sprites will move at random when the sprite's
    move() function is called.

    To easily call a direction, you can also use the RPS class's directions
    attribute, which is a dictionary with cardinal directions as keys (NO, SO,
    EA, WE, NE, SE, NW, SW, CE) that returns a Direction object.
    '''
    return None


rps.prototype_move(move)


# Game Loop
while True:
    DISPLAYSURF.fill(preset.color.WHITE)
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Moves and Re-draws all Sprites
    for sprite in all_sprites:
        DISPLAYSURF.blit(sprite.image, sprite.rect)
        sprite.move()

    for sprite in rps.collide(True).keys():
        new_piece = rps.create_loses_to(sprite, sprite.rect.center)
        all_sprites.add(new_piece)

    pygame.display.update()
    FramePerSec.tick(preset.FPS)
