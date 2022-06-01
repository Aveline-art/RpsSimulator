#Imports
import pygame, sys
from pygame.locals import *
import preset
from rps import RPS

#Initialzing 
pygame.init()

#Setting up FPS 
FramePerSec = pygame.time.Clock()

#Setting up Fonts
font = pygame.font.SysFont(preset.FONT, 60)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((preset.SCREEN_WIDTH, preset.SCREEN_WIDTH))

#Creating Sprites Groups
rps = RPS()
rps.create(30)
all_sprites = pygame.sprite.Group()
all_sprites.add(rps.all_sprites)
 
#Game Loop
while True:
    DISPLAYSURF.fill(preset.color.WHITE)
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Moves and Re-draws all Sprites
    for sprite in all_sprites:
        DISPLAYSURF.blit(sprite.image, sprite.rect)
        sprite.move()
    
    rock_on_paper = rps.Rock.collide(True)
    paper_on_scissors = rps.Paper.collide(True)
    scissors_on_rock = rps.Scissors.collide(True)

    for sprite in (rock_on_paper | paper_on_scissors | scissors_on_rock).keys():
        symbol = sprite.symbol
        piece = rps.wins(symbol).create(center=sprite.rect.center)
        all_sprites.add(piece)
         
    pygame.display.update()
    FramePerSec.tick(preset.FPS)