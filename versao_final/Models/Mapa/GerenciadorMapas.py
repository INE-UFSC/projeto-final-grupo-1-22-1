from Models.Mapa.Mapa import Mapa
from pygame import Surface
from Models.Configuracoes import Configuracoes
from csv import reader

class GerenciadorMapas:
  def __init__(self, window_surface: Surface, configuracoes: Configuracoes) -> None:
    self.__window_surface = window_surface
    self.__configuracoes =configuracoes
    self.__layouts_mapa = ['csv/mapa01.csv']

  def get_mapa(self, mapa_index):
    mapa = self.__mapas[mapa_index]
    return mapa

  def __importar_csv(self, layout_index):
    with open(self.__layouts_mapa[layout_index]) as mapa_csv:
      layout_mapa = reader(mapa_csv, delimiter=',')
      layout_list = list(layout_mapa)
      self.__tamanho_tile = self.__configuracoes.altura_tela/len(layout_list)
      self.__largura_mapa = len(layout_list[0]) * self.__tamanho_tile
      self.__altura_mapa = len(layout_list) * self.__tamanho_tile
    return layout_list
  
  def gerar_mapa(self, layout_index):
    layout_mapa = self.__importar_csv(layout_index)
    mapa = Mapa(layout_mapa, self.__window_surface, self.__largura_mapa, self.__altura_mapa, self.__tamanho_tile)
    return mapa

