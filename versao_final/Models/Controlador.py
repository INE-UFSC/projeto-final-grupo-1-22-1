from Models.Jogador import Jogador
from Models.Inimigo import Inimigo
from Models.LeitorColisao import LeitorColisao
from Models.Mapa.Mapa import Mapa
from Models.Persistencia.JogoDAO import JogoDAO
from Models.LeitorEventos import LeitorEventos
from Models.Persistencia.Pontuacao import Pontuacao
from Models.Vida import Vida

import pygame as pg
import sys



class Controlador():
  def __init__(self, mapa: Mapa, inimigo: Inimigo, grupo_obstaculos, grupo_inimigos):
    self.__jogador = mapa.jogador
    self.__inimigo = inimigo
    self.__leitor_colisao = LeitorColisao(mapa.grupo_jogador, grupo_obstaculos, grupo_inimigos)
    self.__leitor_eventos = LeitorEventos()
    self.__vida = Vida()
    self.__coordenada_inimigo = (0,0)
    self.__jogo_dao = JogoDAO()

  def checar_limites_mapa(self):
    if self.__jogador.rect.x == 580:
      return('lim-dir')
    elif self.__jogador.rect.x == 30:
      return('lim-esq')
    elif self.__jogador.rect.y == 30:
      return('lim-cima')
    elif self.__jogador.rect.y == 430:
      print('lim-y')
      return('lim-baixo')
      

  def mover_jogador(self):
    evento = self.__leitor_eventos.ler_evento()
    if not self.__leitor_colisao.checar_colisao_obstaculo(self.__jogador):
      limite = self.checar_limites_mapa()
      if evento == 'FECHAR':
        pg.quit()
        sys.exit()
      elif evento == 'DIREITA' and not limite == 'lim-dir':
        self.__jogador.mover_direita()
        self.__ultimo_movimento = 'DIREITA'
      elif evento == 'ESQUERDA' and not limite == 'lim-esq':
        self.__ultimo_movimento = 'ESQUERDA'
        self.__jogador.mover_esquerda()
      elif evento == 'CIMA' and not limite == 'lim-cima':
        self.__jogador.mover_cima()
        self.__ultimo_movimento = 'CIMA'
      elif evento == 'BAIXO' and not limite == 'lim-baixo':
        self.__jogador.mover_baixo()
        self.__ultimo_movimento = 'BAIXO'
    else:
      if evento == 'DIREITA' and self.__ultimo_movimento != 'DIREITA':
        self.__jogador.mover_direita()
        self.__ultimo_movimento = 'DIREITA' 
      elif evento == 'ESQUERDA' and self.__ultimo_movimento != 'ESQUERDA':
        self.__ultimo_movimento = 'ESQUERDA' 
        self.__jogador.mover_esquerda()
      elif evento == 'CIMA' and self.__ultimo_movimento != 'CIMA':
        self.__jogador.mover_cima()
        self.__ultimo_movimento = 'CIMA'
      elif evento == 'BAIXO' and self.__ultimo_movimento != 'BAIXO':
        self.__jogador.mover_baixo()
        self.__ultimo_movimento = 'BAIXO'

  def mover_inimigo(self):
    self.__inimigo.ir_para(self.__jogador.get_coordenadas())

  def morte_jogador(self):
    if (self.__leitor_colisao.checar_colisao_inimigo2(self.__jogador)):
      self.__jogador.rect.x = 200
      self.__jogador.rect.y = 200
      self.__jogador.diminuir_vida()
    
    if (self.__jogador.vida == 0):
      self.__jogo_dao.add(Pontuacao(self.__jogador.vida, 10))
      pg.quit()
      sys.exit()

  def atualizar_vida(self, window_surface):
    self.__vida.atualizar_vida(self.__jogador.vida, window_surface)
    
