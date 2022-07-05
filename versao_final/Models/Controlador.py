from Models.Jogador import Jogador
from Models.Inimigo import Inimigo
from Models.LeitorColisao import LeitorColisao
import pygame as pg
import sys

class Controlador():
  def __init__(self, jogador: Jogador, inimigo: Inimigo, grupo_jogador, grupo_obstaculos, grupo_inimigos):
    self.__jogador = jogador
    self.__inimigo = inimigo
    self.__leitor_colisao = LeitorColisao(grupo_jogador, grupo_obstaculos, grupo_inimigos)
    self.__coordenada_inimigo = (0,0)

  def checar_limites_mapa(self):
    if self.__jogador.sprite.rect.x == 580:
      return('lim-dir')
    elif self.__jogador.sprite.rect.x == 30:
      return('lim-esq')
    elif self.__jogador.sprite.rect.y == 30:
      return('lim-cima')
    elif self.__jogador.sprite.rect.y == 430:
      print('lim-y')
      return('lim-baixo')
      

  def mover_personagem(self, evento, personagem):
    if not self.__leitor_colisao.checar_colisao_obstaculo(self.__jogador.sprite):
      limite = self.checar_limites_mapa()
      if evento == 'FECHAR':
        pg.quit()
        sys.exit()
      elif evento == 'DIREITA' and not limite == 'lim-dir':
        personagem.mover_direita()
        self.__ultimo_movimento = 'DIREITA'
      elif evento == 'ESQUERDA' and not limite == 'lim-esq':
        self.__ultimo_movimento = 'ESQUERDA'
        personagem.mover_esquerda()
      elif evento == 'CIMA' and not limite == 'lim-cima':
        personagem.mover_cima()
        self.__ultimo_movimento = 'CIMA'
      elif evento == 'BAIXO' and not limite == 'lim-baixo':
        personagem.mover_baixo()
        self.__ultimo_movimento = 'BAIXO'
    else:
      if evento == 'DIREITA' and self.__ultimo_movimento != 'DIREITA':
        personagem.mover_direita()
        self.__ultimo_movimento = 'DIREITA' 
      elif evento == 'ESQUERDA' and self.__ultimo_movimento != 'ESQUERDA':
        self.__ultimo_movimento = 'ESQUERDA' 
        personagem.mover_esquerda()
      elif evento == 'CIMA' and self.__ultimo_movimento != 'CIMA':
        personagem.mover_cima()
        self.__ultimo_movimento = 'CIMA'
      elif evento == 'BAIXO' and self.__ultimo_movimento != 'BAIXO':
        personagem.mover_baixo()
        self.__ultimo_movimento = 'BAIXO'

  def gerar_coordenada(self):
    self.__coordenada_inimigo = (self.__jogador.sprite.rect.x, self.__jogador.sprite.rect.y)

  def mover_inimigo(self):
    x_atual = self.__inimigo.sprite.rect.x
    y_atual = self.__inimigo.sprite.rect.y
    x_jogador = self.__coordenada_inimigo[0]
    y_jogador = self.__coordenada_inimigo[1]

    if x_atual != x_jogador:
      if x_atual < x_jogador:
        self.__inimigo.sprite.rect.x += 1
      elif x_atual > x_jogador:
        self.__inimigo.sprite.rect.x -= 1
    if y_atual != y_jogador:
        if y_atual < y_jogador:
          self.__inimigo.sprite.rect.y += 1
        elif y_atual > y_jogador:
          self.__inimigo.sprite.rect.y -= 1

  def morte_jogador(self):
    if (self.__leitor_colisao.checar_colisao_inimigo(self.__jogador.sprite)):
      self.__jogador.sprite.rect.x = 200
      self.__jogador.sprite.rect.y = 200
      self.__jogador.diminuir_vida()
    
    if (self.__jogador.vida == 0):
      pg.quit()
      sys.exit()
