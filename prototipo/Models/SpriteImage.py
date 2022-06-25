from pygame.sprite import Sprite
from pygame.image import load

class SpriteImage(Sprite):
  def __init__(self, image_path: str = '', x_position: float = 0.1, y_position: float = 0.1):
    super().__init__()

    self.__image = load(image_path)
    self.__rect = self.__image.get_rect(
      center=(x_position, y_position)
    )
    self.__radius = 10

  @property
  def rect(self):
    return self.__rect

  @property
  def image(self):
    return self.__image

  @property
  def radius(self):
    return self.__radius
  
  def update(self, value: float = 0, comando: str = ""):
    # self.kill() #Destroi o sprite
    if comando == "cima":
      self.mover_cim(value)
    elif comando == "baixo":
      self.mover_bai(value)
    elif comando == "dir":
      self.mover_pos(value)
    elif comando == "esq":
      self.mover_neg(value)
    
    if self.__rect.x == 800:
      print('ola')
      self.kill()
  
  @property
  def image(self) -> str:
    return self.__image
  
  @property
  def rect(self) -> object:
    return self.__rect
  
  def mover_neg(self, value) -> None:
    self.__rect.x -= value
    if self.__rect.x == 0:
      self.kill()
  
  def mover_pos(self, value) -> None:
    self.__rect.x += value

  def mover_cim(self,value) -> None:
    self.__rect.y -= value
  
  def mover_bai(self, value) -> None:
    self.__rect.y += value