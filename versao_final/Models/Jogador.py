from Models.Personagem import Personagem
import pygame as pg

class Jogador(Personagem):
  def __init__(self, velocidade: int = 1):
    super().__init__('Images/Sombra.png', velocidade, 400, 100)
    self.__vida = 3
    
  @property
  def vida(self):
    return self.__vida

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1