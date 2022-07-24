from data.mapa.Mapa import Mapa
from data.Placar import Placar
from data.mapa.GerenciadorMapas import GerenciadorMapas
from data.mapa.ControladorMovimentos import ControladorMovimentos
from pygame import Surface
from data.Configuracoes import Configuracoes
from data.persistencia.Pontuacao import Pontuacao
from data.persistencia.JogoDAO import JogoDAO
from data.Relogio import Relogio


class ControladorJogo:
  def __init__(self, window_surface: Surface) -> None:
    self.__configuracoes = Configuracoes()
    self.__gerenciador_mapas = GerenciadorMapas(window_surface, self.__configuracoes, 'resources/csv')
    self.__mapa = self.__gerenciador_mapas.gerar_mapa(0)
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 
    self.__jogo_dao = JogoDAO()
    self.__controlador_movimentos = ControladorMovimentos(self.__mapa, self.adicionar_baus_no_placar, self.incrementar_mortes_inimigo_no_placar)
    self.__relogio = Relogio()


  def iniciar(self):
    self.__relogio.atualizar_tempo_execucao_jogo()
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
      self.__jogo_dao.add(Pontuacao(self.__placar.baus_coletados, self.__relogio.execucao_do_jogo))
      return True
