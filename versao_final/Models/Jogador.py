from Models.Personagem import Personagem
import pygame as pg

class Jogador(Personagem):
  def __init__(self, velocidade : int, position: tuple = (0,0) ) -> None:
    super().__init__('Images/Sombra.png', velocidade, position)
    self.__vida = 3
    self.__coordenada_tile = self.rect.center

  @property
  def coordenada_tile(self):
    return self.__coordenada_tile

  @property
  def vida(self):
    return self.__vida

  def update(self, deslocamento_x, deslocamento_y):
    self.__coordenada_tile = (self.__coordenada_tile[0] + deslocamento_x, self.__coordenada_tile[1] + deslocamento_y)

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1
