from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

class SpriteObstaculo(Sprite):
  def __init__(self, x_position: float = 0.1, y_position: float = 0.1):
    super().__init__()
    self.__image = load('Images/dod0f.png')
    self.__image = scale(self.__image, (80, 80))   
    self.__radius = 40  
    self.__rect = self.__image.get_rect(
      center=(x_position, y_position)
    )

  @property
  def image(self):
    return self.__image

  @property
  def rect(self):
    return self.__rect

  @property
  def radius(self):
    return self.__radius
