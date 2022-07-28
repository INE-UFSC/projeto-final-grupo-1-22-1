import time
import pygame as pg
from cgi import print_arguments
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
    self.__window = window_surface
    self.__configuracoes = Configuracoes()
    self.__gerenciador_fases = GerenciadorFases(window_surface, self.__configuracoes, 'csv')
    self.__fase = self.__gerenciador_fases.gerar_fase()
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 
    self.__jogo_dao = JogoDAO()
    self.__relogio = Relogio()
    self.__timer = pg.time.Clock()
    self.__tempo_total = 0
    self.__baus_totais = 0

  def checar_derrota(self):
    return self.__fase.checar_derrota

  def iniciar(self):
    self.__gerenciador_fases.mostrar_tela_fase()
    pg.time.wait(2000)

    while not self.__fase.checar_vitoria(self.__placar):
      self.__timer.tick(60)

      self.__window.fill(self.__configuracoes.cor_fundo)

      self.__fase.rodar()
      self.__relogio.atualizar_tempo_execucao_jogo()
      self.__placar.atualizar_vida(self.__fase.mapa.grupo_jogador)
      self.__placar.adicionar_baus(self.__fase.controlador_movimentos.adicionar_baus_no_placar)
      self.__placar.atualizar_baus()
      self.__placar.incrementar_mortes_inimigo(self.__fase.controlador_movimentos.incrementar_mortes_inimigo_no_placar)
      self.__placar.atualizar_mortes_inimigo()
      self.__placar.atualizar_tempo(self.__relogio.execucao_do_jogo - 2)
      self.__fase.aumentar_dificuldade(self.__relogio)
      if self.__fase.checar_derrota():
        print('morreu')
        self.salvar_pontuacao()
        break
      
      pg.display.update()
      pg.display.flip()
    
    if self.__fase.concluida:
      self.__passar_de_fase()

  def adicionar_baus_no_placar(self, novos_baus): 
    self.__placar.adicionar_baus(novos_baus)
    
  def incrementar_mortes_inimigo_no_placar(self):
    self.__placar.incrementar_mortes_inimigo()

  def salvar_pontuacao(self):
    self.__jogo_dao.add(Pontuacao(self.__baus_totais, self.__tempo_total))

  def __passar_de_fase(self):
    self.__tempo_total += self.__relogio.execucao_do_jogo
    self.__baus_totais += self.__placar.baus_coletados

    self.__placar.baus_coletados = 0
    self.__relogio.settar_comeco_jogo()

    self.__fase = self.__gerenciador_fases.gerar_fase()
    
    self.iniciar()
