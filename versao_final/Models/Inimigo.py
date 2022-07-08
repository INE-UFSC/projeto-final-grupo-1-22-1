import pygame as pg
from Models.Personagem import Personagem
from random import randint

class Inimigo(Personagem):
  def __init__(self, velocidade: int = 1):
    super().__init__('Images/Lanterninha.png', velocidade, 640, randint(20,580))
    self.angulo = 0
  
  def ir_para(self, coordenada: tuple):
    x_atual = self.rect.centerx
    y_atual = self.rect.centery
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
  
