from Models.Personagem import Personagem
import pygame as pg

class Jogador(Personagem):
  def __init__(self, position: tuple = (0,0)) -> None:
    super().__init__('Images/Sombra.png', 3, position)
    self.__vida = 3
    
  @property
  def vida(self):
    return self.__vida

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1
