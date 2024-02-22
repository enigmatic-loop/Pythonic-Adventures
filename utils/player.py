import pygame
from main import load_sprite_sheets

class Player(pygame.sprite.Sprite):
  COLOR = (255, 0, 0)
  GRAVITY = 1
  SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)
  
  def __init__(self, x, y, width, height):
    self.rect = pygame.Rect(x, y, width, height)
    self.x_velocity = 0
    self.y_velocity = 0
    self.mask = None
    self.direction = "left"
    self.animation_count = 0
    self.fall_count = 0

  def move(self, dx, dy):
    self.rect.x += dx
    self.rect.y += dy

  def move_left(self, vel):
    self.x_velocity = -vel
    if self.direction != "left":
      self.direction = "left"
      self.animation_count = 0

  def move_right(self, vel):
    self.x_velocity = vel
    if self.direction != "right":
      self.direction = "right"
      self.animation_count = 0

  def loop(self, fps):
    # self.y_velocity += min(1, (self.fall_count / fps) * self.GRAVITY)
    self.move(self.x_velocity, self.y_velocity)

    self.fall_count += 1

  def draw(self, window):
    self.sprite = self.SPRITES["idle_" + self.direction][0]
    window.blit(self.sprite, (self.rect.x, self.rect.y))

