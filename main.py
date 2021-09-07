import pygame
import os
from tkinter import *
from tkinter.ttk import *
import time
import random

WIN = Tk()
#WIN.title('Space Shooter')
#WIN.geometry('1920x1080')
WIN.resizable(True, True)
WIDTH, HEIGHT = 1920, 1080
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
BG = pygame.image.load(os.path.join("assets", "background.png"))

def main():
  run = True
  FPS = 160
  clock = pygame.time.Clock()
  
  while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False