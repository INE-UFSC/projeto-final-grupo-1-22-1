from turtle import right
from pygame.sprite import Sprite
from pygame import Surface

class Lanterna(Sprite):
  def __init__(self, position, size):
    super().__init__()
    self.__image = Surface((size, size))
    self.__image.fill('grey')
    #self.__rect = self.__image.get_rect(midleft = position)

  @property
  def image(self):
    return self.__image