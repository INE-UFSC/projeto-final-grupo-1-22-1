from pygame.image import load
from pygame.sprite import Sprite

class Bau(Sprite):
  def __init__(self, position):
    super().__init__()
    self.__image = load("Images/Explorador.png")
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

