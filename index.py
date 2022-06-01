#Imports
import pygame, sys
from pygame.locals import *
from pieces import Piece, Symbol
import preset

#Initialzing 
pygame.init()

#Setting up FPS 
FramePerSec = pygame.time.Clock()

#Setting up Fonts
font = pygame.font.SysFont(preset.FONT, 60)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((preset.SCREEN_WIDTH, preset.SCREEN_WIDTH))

#Creating Sprites Groups
all_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
paper_sprites = pygame.sprite.Group()
scissors_sprites = pygame.sprite.Group()
for i in range(30):
    rock_piece = Piece(Symbol.ROCK)
    paper_piece = Piece(Symbol.PAPER)
    scissors_piece = Piece(Symbol.SCISSORS)
    all_sprites.add(rock_piece, paper_piece, scissors_piece)
    rock_sprites.add(rock_piece)
    paper_sprites.add(paper_piece)
    scissors_sprites.add(scissors_piece)
 
#Game Loop
while True:
    
    DISPLAYSURF.fill(preset.color.WHITE)
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Moves and Re-draws all Sprites
    for piece in all_sprites:
        DISPLAYSURF.blit(piece.image, piece.rect)
        piece.move()
    
    rock_on_paper = pygame.sprite.groupcollide(rock_sprites, paper_sprites, True, False)
    paper_on_scissors = pygame.sprite.groupcollide(paper_sprites, scissors_sprites, True, False)
    scissors_on_rock = pygame.sprite.groupcollide(scissors_sprites, rock_sprites, True, False)

    for piece in rock_on_paper.keys():
        piece = Piece(Symbol.PAPER, piece.rect.center)
        paper_sprites.add(piece)
        all_sprites.add(piece)
    
    for piece in paper_on_scissors.keys():
        piece = Piece(Symbol.SCISSORS, piece.rect.center)
        scissors_sprites.add(piece)
        all_sprites.add(piece)

    for piece in scissors_on_rock.keys():
        piece = Piece(Symbol.ROCK, piece.rect.center)
        rock_sprites.add(piece)
        all_sprites.add(piece)
         
    pygame.display.update()
    FramePerSec.tick(preset.FPS)