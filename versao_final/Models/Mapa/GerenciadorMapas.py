from Models.Mapa.Mapa import Mapa
from pygame import Surface
from Models.Configuracoes import Configuracoes

class GerenciadorMapas:
  def __init__(self, window_surface: Surface, configuracoes: Configuracoes) -> None:
    self.__window_surface = window_surface
    #TODO: criar propriedade com a lista de file_paths de cada mapa
    self.__layout_mapa = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                          'X                          X',
                          'X   P           I       I   ',
                          'X X    XXX            X    X',
                          'X X         I              X',
                          'X XXX         XX         XXX',
                          'X XXX       XX             X',
                          'X X    X  XXXX    XX  XX   X',
                          'X      X  XXXX    XX  XXX  X',
                          'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
    self.__tamanho_tile = configuracoes.altura_tela/len(self.__layout_mapa)
    self.__largura_mapa = len(self.__layout_mapa[0]) * self.__tamanho_tile
    self.__altura_mapa = len(self.__layout_mapa) * self.__tamanho_tile
    self.__mapas = [Mapa(self.__layout_mapa, self.__window_surface, self.__largura_mapa, self.__altura_mapa, self.__tamanho_tile)]

  
  def get_mapa(self, mapa_index):
    mapa = self.__mapas[mapa_index]
    return mapa
  
  def gerar_mapas(self):
    #TODO: iterar a lista de flie_paths e gerar os mapas, inserindo-os na lista de mapas
    pass
