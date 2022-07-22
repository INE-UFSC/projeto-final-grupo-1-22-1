from Models.Jogador import Jogador
from Models.Inimigo import Inimigo
from Models.GerenciadorColisao import GerenciadorColisao
from Models.Mapa.Mapa import Mapa
from Models.Persistencia.JogoDAO import JogoDAO
from Models.LeitorEventos import LeitorEventos
from Models.Persistencia.Pontuacao import Pontuacao
from Models.Vida import Vida

import pygame as pg
import sys



class Controlador():
  def __init__(self, jogador, grupo_obstaculos, inimigo: Inimigo, grupo_inimigos):
    self.__jogador = jogador
    self.__inimigo = inimigo
    self.__gerenciador_colisao = GerenciadorColisao(Mapa.tiles, Mapa.grupo_jogador, grupo_inimigos)
    self.__leitor_eventos = LeitorEventos()
    self.__vida = Vida()
    self.__coordenada_inimigo = (0,0)
    self.__jogo_dao = JogoDAO()

  def mover_inimigo(self):
    self.__inimigo.ir_para(self.__jogador.get_coordenadas())

  def morte_jogador(self):
    if (self.__gerenciador_colisao.checar_colisao_inimigo2(self.__jogador)):
      self.__jogador.rect.x = 200
      self.__jogador.rect.y = 200
      self.__jogador.diminuir_vida()
    
    if (self.__jogador.vida == 0):
      self.__jogo_dao.add(Pontuacao(self.__jogador.vida))
      pg.quit()
      sys.exit()

  def atualizar_vida(self, window_surface):
    self.__vida.atualizar_vida(self.__jogador.vida, window_surface)
    
