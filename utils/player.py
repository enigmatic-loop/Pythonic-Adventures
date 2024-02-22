import pygame

class Player(pygame.sprite.Sprite):
  COLOR = (255, 0, 0)
  
  def __init__(self, x, y, width, height):
    self.rect = pygame.Rect(x, y, width, height)
    self.x_velocity = 0
    self.y_velocity = 0
    self.mask = None
    self.direction = "left"
    self.animation_count = 0

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
    self.move(self.x_velocity, self.y_velocity)

  def draw(self, window):
    pygame.draw.rect(window, self.COLOR, self.rect)