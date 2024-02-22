import pygame 
from os import listdir 
from os.path import isfile, join 
from utils.player import Player
from utils.configs import *
from utils.utils import *

pygame.init()
pygame.display.set_caption("Pythonic Adventures")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
  clock = pygame.time.Clock()
  background, bg_image = get_background("Gray.png")

  player = Player(100, 100, 50, 50)

  run = True
  # regulates framerate across different devices
  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break

    player.loop(FPS)
    handle_move(player)
    draw(window, background, bg_image, player)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main(window)