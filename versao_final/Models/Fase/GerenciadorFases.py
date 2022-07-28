from Models.Mapa.GerenciadorMapas import GerenciadorMapas
from Models.Fase.Fase import Fase

class GerenciadorFases:
  def __init__(self, window_surface, configuracoes, maps_path):
    self.__gerenciador_mapas = GerenciadorMapas(window_surface, configuracoes, maps_path)
    self.__numero_fases = self.__gerenciador_mapas.quantidade_mapas
    self.__fase = None

  def gerar_fase(self, numero_fase):
    mapa = self.__gerenciador_mapas.gerar_mapa(numero_fase)
    fase = Fase(mapa)
    self.__fase = fase
    return self.__fase
