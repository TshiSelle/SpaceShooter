import pygame
import os

import time
import random


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Space Shooter")

#importing enemy ships assets
#ENEMEY_SHIP_ONE = pygame.image.load(os.path.join("assets", ""))
#LASER_SHIP_ONE = pygame.image.load(os.path.join("assets", ""))

#ENEMY_SHIP_TWO = pygame.image.load(os.path.join("assets", ""))
#LASER_SHIP_TWO = pygame.image.load(os.path.join("assets", ""))

#ENEMY_SHIP_THREE = pygame.image.load(os.path.join("assets", ""))
#LASER_SHIP_THREE = pygame.image.load(os.path.join("assets", ""))

#importing player ship asset
#PLAYER_SHIP = pygame.image.load(os.path.join("assets", ""))
#LASER_PLAYER = pygame.image.load(os.path.join("assets", ""))

#importing background
BG = pygame.image.load(os.path.join("assets", "background.png"))

def main():
  run = True
  FPS = 160
  level = 1
  lives = 5
  clock = pygame.time.Clock()
  
  def refactor_window():
    WIN.blit(BG, (0, 0))
    pygame.display.update()
  while run:
    clock.tick(FPS)
    refactor_window()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
main()