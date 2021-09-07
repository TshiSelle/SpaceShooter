import pygame
import os
import time
import random
import math
pygame.font.init()

WIDTH, HEIGHT = 750 ,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

def main():
  run = True
  FPS = 160
  level = 1
  lives = 5
  main_font = pygame.font.SysFont("comicsans", 45)
  clock = pygame.time.Clock()
  
  def refactor_window():
    WIN.blit(BG, (0, 0))
    lives_label = main_font.render(f"lives: {lives}", 1, (224, 230, 227))
    level_label = main_font.render(f"level: {level}", 1, (224, 230, 227))
    
   
    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10 , 10))
    
    
    pygame.display.update()
  while run:
    clock.tick(FPS)
    refactor_window()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
main()