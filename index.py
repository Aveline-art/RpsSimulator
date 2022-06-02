# Imports
import pygame
import sys
from pygame.locals import QUIT
import preset
from rps import RPS

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

    rock_on_paper = rps.rock.collide(True)
    paper_on_scissors = rps.paper.collide(True)
    scissors_on_rock = rps.scissors.collide(True)

    for sprite in (rock_on_paper |
                   paper_on_scissors |
                   scissors_on_rock).keys():
        new_piece = rps.create_loses_to(sprite, sprite.rect.center)
        all_sprites.add(new_piece)

    pygame.display.update()
    FramePerSec.tick(preset.FPS)
