from ursina import *
import pygame
from pygame.locals import *
import random

pygame.init()



screen = pygame.display.set_mode((800, 600))
screen.fill((255, 120, 160))


block = pygame.image.load("game.png").convert()
block_x = 100
block_y = 100

screen.blit(block, (block_x, block_y))

def game():
  
    x = 2


pygame.display.flip()

run = True
while run:
    game()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
        elif event.type == QUIT:
            run = False

