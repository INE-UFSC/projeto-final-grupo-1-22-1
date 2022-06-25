from Models.Desenhavel import Desenhavel

class Jogador(Desenhavel):
  def __init__(self):
    super().__init__('Images/Sombra.png', 400, 100)
    self.__velocidade = 2

  def mover_dir(self):
    self.sprite.rect.x += self.__velocidade

  def mover_esq(self):
    self.sprite.rect.x -= self.__velocidade

  def mover_cim(self):
    self.sprite.rect.y -= self.__velocidade
  
  def mover_bai(self):
    self.sprite.rect.y += self.__velocidade