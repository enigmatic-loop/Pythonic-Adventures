import pygame
from os.path import join
from configs import *

def get_background(name):
  image = pygame.image.load(join("assets", "Background", name))
  _, _, width, height = image.get_rect()
  tiles = []

  for i in range(WIDTH // width + 1):
    for j in range(HEIGHT // height + 1):
      pos = (i * width, j * height)
      tiles.append(pos)

  return tiles, image

def draw(window, background, bg_image, player):
  for tile in background:
    window.blit(bg_image, tuple(tile))

  player.draw(window)
  pygame.display.update()

def handle_move(player):
  keys = pygame.key.get_pressed()
  player.x_velocity = 0

  if keys[pygame.K_LEFT]:
    player.move_left(PLAYER_VELOCITY)
  if keys[pygame.K_RIGHT]:
    player.move_right(PLAYER_VELOCITY)

def flip(sprites):
  return [pygame.transform.flip(sprite, True, False) for sprite in sprites]