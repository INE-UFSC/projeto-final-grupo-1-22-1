from Models.Mapa.Mapa import Mapa
from Models.Placar import Placar
from Models.Mapa.GerenciadorMapas import GerenciadorMapas
from Models.Mapa.ControladorMovimentos import ControladorMovimentos
from pygame import Surface
from Models.Configuracoes import Configuracoes
import os
from Models.Relogio import Relogio


class ControladorJogo:
  def __init__(self, window_surface: Surface) -> None:
    self.__configuracoes = Configuracoes()
    self.__gerenciador_mapas = GerenciadorMapas(window_surface, self.__configuracoes, 'csv')
    self.__mapa = self.__gerenciador_mapas.gerar_mapa(0)
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 
    self.__controlador_movimentos = ControladorMovimentos(self.__mapa, self.adicionar_baus_no_placar, self.incrementar_mortes_inimigo_no_placar)
    self.__relogio = Relogio()


  def iniciar(self):
    self.__relogio.atualizar_tempo_execucao_jogo()
    print(self.__relogio.execucao_do_jogo)
    self.__mapa.run(self.__controlador_movimentos)
    self.__placar.atualizar_vida(self.__mapa.grupo_jogador)
    self.__placar.atualizar_baus()
    self.__placar.atualizar_mortes_inimigo()
    self.__placar.atualizar_tempo(self.__relogio.execucao_do_jogo)

  def adicionar_baus_no_placar(self, novos_baus):
    self.__placar.adicionar_baus(novos_baus)
    
  def incrementar_mortes_inimigo_no_placar(self):
    self.__placar.incrementar_mortes_inimigo()

  def game_over(self):
    jogador = self.__mapa.grupo_jogador.sprite
    if jogador.vida == 0:
      return True


  