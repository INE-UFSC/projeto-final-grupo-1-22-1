from abc import ABC, abstractmethod
import pygame as pg
from pygame.sprite import Sprite
from pygame.image import load

class Desenhavel(Sprite, ABC):
  @abstractmethod
  def __init__(self, image_path: str, position : tuple = (0,0)):
    super().__init__()
    self.__image = load(image_path)
    self.__rect = self.__image.get_rect(center=position)
    self.__mask = pg.mask.from_surface(self.image)
    self.__position = position

  @property
  def image(self):
    return self.__image

  @property
  def position(self):
    return self.__position

  @property
  def mask(self):
    return self.__mask

  @property
  def rect(self): return self.__rect 
  
  def set_rect_left(self, valor): self.__rect.left = valor
  
  def set_rect_right(self, valor): self.__rect.right = valor

  def set_rect_top(self, valor): self.__rect.top = valor

  def set_rect_bottom(self, valor): self.__rect.bottom = valor

  @image.setter
  def image(self, image):
    self.__image = image