import pygame as pg
from pygame import Surface
from pygame.sprite import Sprite

class Tile(Sprite):
  def __init__(self, position, size):
    super().__init__()
    # self.__image = Surface((size, size))
    # self.__image.fill('grey')
    self.__image = pg.transform.scale(
            pg.image.load("Images/Tijolo.png"), (size, size))
    self.__rect = self.__image.get_rect(topleft = position)

  @property
  def rect(self):
    return self.__rect

  @property
  def image(self):
    return self.__image
  
  def get_rect_left(self):
    return self.rect.left

  def get_rect_right(self):
    return self.rect.right

  def get_rect_top(self):
    return self.rect.top

  def get_rect_bottom(self):
    return self.rect.bottom

  def update(self, deslocamento_x, deslocamento_y):
    self.__rect.x += deslocamento_x
    self.__rect.y += deslocamento_y

