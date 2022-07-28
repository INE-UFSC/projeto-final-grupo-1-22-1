from Models.Mapa.Mapa import Mapa
from Models.Placar import Placar
from Models.Mapa.GerenciadorMapas import GerenciadorMapas
from Models.Mapa.ControladorMovimentos import ControladorMovimentos
from pygame import Surface
from Models.Configuracoes import Configuracoes
from Models.Persistencia.Pontuacao import Pontuacao
from Models.Persistencia.JogoDAO import JogoDAO
from Models.Relogio import Relogio
from Models.Fase.GerenciadorFases import GerenciadorFases


class ControladorJogo:
  def __init__(self, window_surface: Surface) -> None:
    self.__configuracoes = Configuracoes()
    self.__gerenciador_fases = GerenciadorFases(window_surface, self.__configuracoes, 'csv')
    self.__fase = self.__gerenciador_fases.gerar_fase(0)
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 
    self.__jogo_dao = JogoDAO()
    self.__relogio = Relogio()


  def iniciar(self):
    self.__fase.iniciar()
    self.__relogio.atualizar_tempo_execucao_jogo()
    self.__placar.atualizar_vida(self.__fase.mapa.grupo_jogador)
    self.__placar.adicionar_baus(self.__fase.controlador_movimentos.adicionar_baus_no_placar)
    self.__placar.atualizar_baus()
    self.__placar.incrementar_mortes_inimigo(self.__fase.controlador_movimentos.incrementar_mortes_inimigo_no_placar)
    self.__placar.atualizar_mortes_inimigo()
    self.__placar.atualizar_tempo(self.__relogio.execucao_do_jogo)
    
    inimigos = self.__fase.controlador_movimentos.grupo_inimigos.sprites()
    for inimigo in inimigos:
      inimigo.velocidade = (self.__relogio.execucao_do_jogo // 5) + 1

  def adicionar_baus_no_placar(self, novos_baus): 
    self.__placar.adicionar_baus(novos_baus)
    
  def incrementar_mortes_inimigo_no_placar(self):
    self.__placar.incrementar_mortes_inimigo()

  def proxima_fase(self):
    if self.__placar.baus_coletados == 10:
      pass

  def game_over(self):
    if self.__fase.game_over():
      self.__jogo_dao.add(Pontuacao(self.__placar.baus_coletados, self.__relogio.execucao_do_jogo))
      return True
