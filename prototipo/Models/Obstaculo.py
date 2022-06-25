from Models.Desenhavel import Desenhavel
from Models.SpriteImage import SpriteImage
from pygame.transform import scale

class Obstaculo(Desenhavel):
  def __init__(self, x_position, y_position):
    super().__init__('Images/circle-sprite.png', x_position, y_position)
    self.__image_scaled = scale(self.sprite.image, (10, 10)) 
    self.__rect = self.__image_scaled.get_rect()

  @property
  def rect(self):
    return self.__rect