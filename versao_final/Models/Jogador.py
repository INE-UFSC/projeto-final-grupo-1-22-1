from Models.Personagem import Personagem
import pygame as pg
from pygame.math import Vector2

class Jogador(Personagem):
  def __init__(self, position: tuple = (0,0)) -> None:
    super().__init__('Images/Sombra.png', 3, position)
    self.__vida = 3
    self.__direcao = Vector2(0,0)
    
  @property
  def vida(self):
    return self.__vida

  @property
  def direcao(self):
    return self.__direcao
  
  def mover_direita(self) -> None:
      self.__direcao.x = 1

  def mover_esquerda(self) -> None:
      self.__direcao.x = -1

  def zerar_direcao(self) -> None:
      self.__direcao.x = 0

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1
