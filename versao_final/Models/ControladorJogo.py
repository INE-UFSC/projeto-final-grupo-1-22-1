from Models.Mapa.Mapa import Mapa
from Models.Placar import Placar
from Models.Mapa.GerenciadorMapas import GerenciadorMapas
from pygame import Surface
from Models.Configuracoes import Configuracoes

class ControladorJogo:
  #TODO: inserir um controlador de mapa (cria um mapa a partir de um csv)
  def __init__(self, window_surface: Surface) -> None:
    self.__configuracoes = Configuracoes()
    self.__gerenciador_mapas = GerenciadorMapas(window_surface, self.__configuracoes)
    self.__mapa = self.__gerenciador_mapas.get_mapa(0)
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 

  def iniciar(self):
    self.__mapa.run()
    self.__placar.atualizar_vida(self.__mapa.grupo_jogador)

  def game_over(self):
    jogador = self.__mapa.grupo_jogador.sprite
    if jogador.vida == 0:
      return True


  