import pygame 
from os import listdir
from os.path import join, isfile
from configs import *
from utils.utils import *
from utils.player import *

pygame.init()
pygame.display.set_caption("Pythonic Adventures")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def load_sprite_sheets(directory1, directory2, width, height, direction=False):
  path = join("assets", directory1, directory2)
  images = [file for file in listdir(path) if isfile(join(path, file))]

  all_sprites = {}

  for image in images:
    sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

    sprites = []
    for i in range(sprite_sheet.get_width() // width):
      surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
      rectangle = pygame.Rect(i * width, 0, width, height)
      surface.blit(sprite_sheet, (0,0), rectangle)
      sprites.append(pygame.transform.scale2x(surface))

    if direction:
      all_sprites[image.replace(".png", "") + "_right"] = sprites
      all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
    else:
      all_sprites[image.replace(".png", "")] = sprites

  return all_sprites

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