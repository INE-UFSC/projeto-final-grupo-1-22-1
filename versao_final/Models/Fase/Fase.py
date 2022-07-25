from Models.Mapa.ControladorMovimentos import ControladorMovimentos
from Models.Mapa.Mapa import Mapa


class Fase:
  def __init__(self, mapa: Mapa) -> None:
    self.__mapa = mapa
    self.__controlador_movimentos = ControladorMovimentos(self.__mapa)
  
  @property
  def mapa(self):
    return self.__mapa

  def aumentar_dificuldade(self):
    pass

  def __checar_vitoria(self):
    jogador = self.__mapa.grupo_jogador.sprite
    numero_baus = len(self.__mapa.grupo_baus)
    numero_armaduras = len(self.__mapa.grupo_armaduras)
    if  numero_baus == 0 and numero_armaduras == 0 and jogador.baus == 0:
        return True

  def iniciar(self):
    self.__mapa.run(self.__controlador_movimentos)
    if self.__checar_vitoria():
      print('ganhou')

  def game_over(self):
    jogador = self.__mapa.grupo_jogador.sprite
    if jogador.vida == 0:
      return True
