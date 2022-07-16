from re import X
import pygame as pg
from Models.Personagem import Personagem
from random import randint
import math

class Inimigo(Personagem):
  def __init__(self):
    super().__init__('Images/Cientista.png', 1, (400, 250))
    self.imagem = pg.transform.rotate(self.image, self.angulo%360) 

  def ir_para(self, coordenada: tuple):
    x_atual = self.rect.x
    y_atual = self.rect.y
    x_player = coordenada[0]
    y_player = coordenada[1]
    #print(f'Player - {x_player, y_player}, Inimigo - {x_atual, y_atual}')
    
    if y_player < y_atual:
      if x_player < x_atual:                                      #-1, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -1, -1)
      elif x_player > x_atual:                                    #1, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 1, -1)
      else:                                                       #0, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 0, -1)
    elif y_player > y_atual:
      if x_player > x_atual:                                      #1, 1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 1, 1)
      elif x_player < x_atual:                                    #1, 1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -1, 1)
      else:                                                       #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 1, 0)
    else:
      if x_player > x_atual:                                      #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 1, 0)
      else:                                                       #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -1, 0)
  
