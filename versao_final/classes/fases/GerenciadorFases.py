from classes.mapa.GerenciadorMapas import GerenciadorMapas
from classes.fases.Fase import Fase
import time
import pygame as pg
from pygame import Color

class GerenciadorFases:
  def __init__(self, window_surface, configuracoes, maps_path):
    self.__window = window_surface
    self.__configuracoes = configuracoes
    self.__gerenciador_mapas = GerenciadorMapas(window_surface, configuracoes, maps_path)
    self.__quantidade_fases = self.__gerenciador_mapas.quantidade_mapas
    self.__numero_fase = 0
    self.__fase = None
    self.__game_over_bg_img = pg.transform.scale(
            pg.image.load("recursos/imagens/Mapa.png"), (self.__configuracoes.largura_tela, self.__configuracoes.altura_tela))

  @property
  def gerenciador_mapas(self):
    return self.__gerenciador_mapas

  @property
  def quantidade_fases(self):
    return self.__quantidade_fases

  @property
  def numero_fase(self):
    return self.__numero_fase

  def add_contador(self):
    self.__contador += 1

  def gerar_fase(self):
    mapa = self.__gerenciador_mapas.gerar_mapa(self.__numero_fase)
    fase = Fase(mapa, self.__configuracoes.gerar_dados())
    self.__fase = fase
    self.__numero_fase += 1
    return self.__fase
      

  def mostrar_tela_fase(self):
    text_surf = self.__configuracoes.fonte_titulo.render(f'Nível {self.__numero_fase}', True, 'White')
    text_rect = text_surf.get_rect(center = (self.__configuracoes.largura_tela / 2, self.__configuracoes.altura_tela / 2))

    self.__window.blit(self.__game_over_bg_img, (0,0))
    self.__window.blit(text_surf, text_rect)
    
    pg.display.flip()
