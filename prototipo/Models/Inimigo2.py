from Models.Desenhavel import Desenhavel
from random import randint
import pygame as pg

class Inimigo2(Desenhavel):
  def __init__(self):
    super().__init__('Images/Lanterninha.png', 640, randint(20,580))
    self.__mask = pg.mask.from_surface(self.sprite.image)

  @property
  def mask(self):
    return self.__mask
  
