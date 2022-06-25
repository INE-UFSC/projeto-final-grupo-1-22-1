from Models.Desenhavel import Desenhavel

class Jogador(Desenhavel):
  def __init__(self):
    super().__init__('Images/Sombra.png', 400, 100)
    self.__velocidade = 5
    self.__vida = 3

  @property
  def vida(self):
    return self.__vida

  def mover_dir(self):
    self.sprite.rect.x += self.__velocidade

  def mover_esq(self):
    self.sprite.rect.x -= self.__velocidade

  def mover_cim(self):
    self.sprite.rect.y -= self.__velocidade
  
  def mover_bai(self):
    self.sprite.rect.y += self.__velocidade

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1