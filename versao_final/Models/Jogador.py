from Models.Personagem import Personagem
import pygame as pg

class Jogador(Personagem):
  def __init__(self, velocidade : int, position: tuple = (0,0) ) -> None:
    super().__init__('Images/Sombra.png', velocidade, position)
    self.__posicao_inicial = position
    self.__vida = 3
    self.__coordenada_tile = self.rect.center
    self.__armadura = None

  @property
  def coordenada_tile(self):
    return self.__coordenada_tile

    
  @property
  def vida(self):
    return self.__vida

  @property
  def posicao_inicial(self):
    return self.__posicao_inicial

  @property
  def armadura(self):
    return self.__armadura
  
  def update(self, deslocamento_x, deslocamento_y):
    self.__coordenada_tile = (self.__coordenada_tile[0] + deslocamento_x, self.__coordenada_tile[1] + deslocamento_y)

  @armadura.setter
  def armadura(self, nova_armadura):
    self.__armadura = nova_armadura

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1

  def renascer(self, position):
    self.rect.center = position
