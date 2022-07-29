from classes.desenhaveis.Personagem import Personagem
import pygame as pg
from pygame.image import load

class Jogador(Personagem):
  def __init__(self, velocidade : int, vidas: int, position: tuple = (0,0)) -> None:
    super().__init__('recursos/imagens/Sombra.png', velocidade, position)
    self.__posicao_inicial = position
    self.__vida = vidas
    self.__armadura = None
    self.__baus = 0

  @property
  def vida(self):
    return self.__vida

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1

  @property
  def posicao_inicial(self):
    return self.__posicao_inicial

  @property
  def armadura(self):
    return self.__armadura
  
  @property
  def baus(self):
    return self.__baus

  @armadura.setter
  def armadura(self, novo_estado):
    self.__armadura = novo_estado
    
  @baus.setter
  def baus(self, novo_estado):
    self.__baus = novo_estado

  @vida.setter
  def vida(self, vida):
    self.__vida = vida

  def atualizar_imagem(self):
    imagem = "Sombra"
    if self.__baus > 0:
      if self.__armadura:
        imagem = "ArmaduraTesouro"
      else:
        imagem = "SombraTesouro"
    else:
      if self.__armadura:
        imagem = "ArmaduraOn"
      else:
        imagem = "Sombra"
    super().girar_imagem('cima')
    self.image = load(f'recursos/imagens/{imagem}.png')

  def diminuir_vida(self):
    if self.__vida > 0:
      self.__vida -= 1

  def renascer(self, position):
    self.rect.center = position
