import pygame as pg
from Models.Personagem import Personagem
from random import randint

class Inimigo(Personagem):
  def __init__(self):
    super().__init__('Images/Lanterninha.png', 1, (640, randint(20,580)))

  def ir_para(self, coordenada: tuple):
    x_atual = self.rect.x
    y_atual = self.rect.y
    x_ref = coordenada[0]
    y_ref = coordenada[1]

    if x_atual != x_ref:
      if x_atual < x_ref:
        self.mover_direita()
      elif x_atual > x_ref:
        self.mover_esquerda()
    if y_atual != y_ref:
        if y_atual < y_ref:
          self.mover_baixo()
        elif y_atual > y_ref:
          self.mover_cima()
  
