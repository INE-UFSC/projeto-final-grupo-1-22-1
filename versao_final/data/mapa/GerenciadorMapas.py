from data.mapa.Mapa import Mapa
from pygame import Surface
from data.Configuracoes import Configuracoes
from csv import reader
import os

class GerenciadorMapas:
  def __init__(self, window_surface: Surface, configuracoes: Configuracoes, diretorio_mapas: str) -> None:
    self.__window_surface = window_surface
    self.__configuracoes = configuracoes
    #TODO : pegar lista de mapas de uma pasta e alimentar a lista de layouts a partir disso
    #os.listdir()
    self.__layouts_mapa = self.__pegar_arquivos_mapa(diretorio_mapas)

  def __pegar_arquivos_mapa(self, path):
    lista_mapas = os.listdir(path)
    lista_paths = []
    for nome_mapa in lista_mapas:
      complete_path = f'{path}/{nome_mapa}'
      lista_paths.append(complete_path)
    return lista_paths

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

