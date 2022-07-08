from Models.Desenhavel import Desenhavel
from Models.SpriteImage import SpriteImage
import pygame as pg

class Jogador(Desenhavel):
  def __init__(self):
    super().__init__('Images/Sombra.png', 400, 100)
    self.__velocidade = 5
    self.__vida = 3
    self.__mask = pg.mask.from_surface(self.sprite.image)

  @property
  def vida(self):
    return self.__vida
  
  @property
  def mask(self):
    return self.__mask

  def mover_direita(self):
    self.sprite.rect.x += self.__velocidade
    
  def mover_esquerda(self):
    self.sprite.rect.x -= self.__velocidade

  def mover_cima(self):
    self.sprite.rect.y -= self.__velocidade
  
  def mover_baixo(self):
    self.sprite.rect.y += self.__velocidade

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1