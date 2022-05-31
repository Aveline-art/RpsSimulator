#Imports
import pygame, sys
from pygame.locals import *
from pieces import Rock_Piece, Paper_Piece, Scissor_Piece
import preset

#Initialzing 
pygame.init()

#Setting up FPS 
FramePerSec = pygame.time.Clock()
 
#Setting up Fonts
font = pygame.font.SysFont(preset.FONT, 60)
font_small = pygame.font.SysFont(preset.FONT, 20)
game_over = font.render("Game Over", True, preset.color.BLACK)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((preset.SCREEN_WIDTH, preset.SCREEN_WIDTH))
DISPLAYSURF.fill(Color.WHITE.value)
pygame.display.set_caption("Game")

#Creating Sprites Groups
all_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
paper_sprites = pygame.sprite.Group()
scissors_sprites = pygame.sprite.Group()
for i in range(30):
    rock_piece = Rock_Piece()
    paper_piece = Paper_Piece()
    scissors_piece = Scissor_Piece()
    all_sprites.add(rock_piece, paper_piece, scissors_piece)
    rock_sprites.add(rock_piece)
    paper_sprites.add(paper_piece)
    scissors_sprites.add(scissors_piece)
 
#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
         
    pygame.display.update()
    FramePerSec.tick(preset.FPS)