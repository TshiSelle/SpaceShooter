import pygame
import os
import time
import random

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#importing enemy ships assets
ENEMEY_SHIP_ONE = pygame.image.load(os.path.join("assets", ""))
LASER_SHIP_ONE = pygame.image.load(os.path.join("assets", ""))

ENEMY_SHIP_TWO = pygame.image.load(os.path.join("assets", ""))
LASER_SHIP_TWO = pygame.image.load(os.path.join("assets", ""))

ENEMY_SHIP_THREE = pygame.image.load(os.path.join("assets", ""))
LASER_SHIP_THREE = pygame.image.load(os.path.join("assets", ""))

#importing player ship asset
PLAYER_SHIP = pygame.image.load(os.path.join("assets", ""))
LASER_PLAYER = pygame.image.load(os.path.join("assets", ""))

#importing background
BG = pygame.image.load(os.path.join("assets", "background.png"))