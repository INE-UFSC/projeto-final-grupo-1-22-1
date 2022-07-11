import pygame as pg
from pygame import Surface
from pygame.sprite import Sprite

class Tile(Sprite):
  def __init__(self, position, size):
    super().__init__()
    self.__image = Surface((size, size))
    self.__image.fill('grey')
    self.__rect = self.__image.get_rect(topleft = position)

  @property
  def rect(self):
    return self.__rect

  @property
  def image(self):
    return self.__image

  def update(self, deslocamento_x):
    self.__rect.x += deslocamento_x
