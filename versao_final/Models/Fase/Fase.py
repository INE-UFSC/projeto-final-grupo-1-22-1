from Models.Mapa.ControladorMovimentos import ControladorMovimentos
from Models.Mapa.Mapa import Mapa


class Fase:
  def __init__(self, mapa: Mapa) -> None:
    self.__mapa = mapa
    self.__controlador_movimentos = ControladorMovimentos(self.__mapa)
    self.__concluida = False
  
  @property
  def mapa(self):
    return self.__mapa

  @property
  def controlador_movimentos(self):
    return self.__controlador_movimentos
    
  @property
  def concluida(self):
    return self.__concluida

  def aumentar_dificuldade(self):
    pass

  def checar_vitoria(self, placar):
      if placar.baus_coletados == self.__mapa.quantidade_baus:
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
      inimigo.velocidade = (relogio.execucao_do_jogo // 5) + 1
  