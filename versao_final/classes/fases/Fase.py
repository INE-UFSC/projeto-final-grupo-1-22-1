from classes.mapa.ControladorMovimentos import ControladorMovimentos
from classes.mapa.Mapa import Mapa


class Fase:
  def __init__(self, mapa: Mapa, dificuldade) -> None:
    self.__mapa = mapa
    self.__controlador_movimentos = ControladorMovimentos(self.__mapa)
    self.__concluida = False
    self.__dificuldade = dificuldade
  
  @property
  def mapa(self):
    return self.__mapa

  @property
  def controlador_movimentos(self):
    return self.__controlador_movimentos
    
  @property
  def concluida(self):
    return self.__concluida
  
  @property
  def dificuldade(self):
    return self.__dificuldade

  def checar_vitoria(self, baus_totais, placar):
    if self.__mapa.jogador.baus == 0 and len(self.__mapa.grupo_baus) == 0:
      self.__concluida = True
      return True

  def rodar(self):
    self.__mapa.run(self.__controlador_movimentos)

  def checar_derrota(self):
    jogador = self.__mapa.grupo_jogador.sprite
    if jogador.vida == 0:
      self.__concluida = False
      return True

  def aumentar_dificuldade(self, relogio):
    inimigos = self.mapa.grupo_inimigo.sprites()
    for inimigo in inimigos:
      inimigo.velocidade = (relogio.execucao_do_jogo // self.__dificuldade["acres_velo"]) + self.__dificuldade["velocidade"]
