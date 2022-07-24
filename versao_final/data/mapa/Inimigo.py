import pygame as pg
from data.Personagem import Personagem

class Inimigo(Personagem):
  def __init__(self, velocidade, posicao):
    super().__init__('resources/images/Cientista.png', velocidade, posicao)
    self.__rotacao = 0
    self.__sentido = 'baixo'
    self.imagem = pg.transform.rotate(self.image, self.__rotacao%360) 
    
  @property
  def sentido(self):
    return self.__sentido

  @sentido.setter
  def sentido(self, sentido):
    self.__sentido = sentido

  def draw(self, window):
    window.blit(self.imagem, self.get_coordenadas())

  def update(self, deslocamento_x, deslocamento_y):
    self.rect.x += deslocamento_x
    self.rect.y += deslocamento_y

  def mover_inim(self, sentido):
    self.rect.y += sentido