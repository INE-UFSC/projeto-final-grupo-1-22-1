from abc import ABC, abstractmethod
import pygame as pg
from pygame.sprite import Sprite
from pygame.image import load

class Desenhavel(Sprite, ABC):
  @abstractmethod
  def __init__(self, image_path: str, x_position: int = 0, y_position: int = 0):
    super().__init__()
    self.__image = load(image_path)
    self.__rect = self.__image.get_rect(center=(x_position, y_position))
    self.__mask = pg.mask.from_surface(self.image)

  @property
  def image(self):
    return self.__image

  @property
  def mask(self):
    return self.__mask

  @property
  def rect(self):
    return self.__rect 
  
  @image.setter
  def image(self, image):
    self.__image = image