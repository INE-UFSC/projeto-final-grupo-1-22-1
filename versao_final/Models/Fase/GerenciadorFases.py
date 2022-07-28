from Models.Mapa.GerenciadorMapas import GerenciadorMapas
from Models.Fase.Fase import Fase
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
    self.text_surf = self.__configuracoes.fonte.render('Nível 1', True, 'White')
    self.text_rect = self.text_surf.get_rect(center = (1280 / 2, 720 / 2))

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
    fase = Fase(mapa)
    self.__fase = fase
    print(f'Fase -> {self.__numero_fase} - Quantidade -> {self.__quantidade_fases}')
    self.__numero_fase += 1
    return self.__fase

  def mostrar_tela_fase(self):
    self.__window.fill((54, 107, 95))
    self.__window.blit(self.text_surf, self.text_rect)
    
    pg.display.flip()
