import pygame as pg
from classes.componentes.Placar import Placar
from pygame import Surface
from classes.configuracoes.Configuracoes import Configuracoes
from classes.persistencia.Pontuacao import Pontuacao
from classes.persistencia.JogoDAO import JogoDAO
from classes.componentes.Relogio import Relogio
from classes.fases.GerenciadorFases import GerenciadorFases


class ControladorJogo:
  def __init__(self, window_surface: Surface) -> None:
    self.__window = window_surface
    self.__configuracoes = Configuracoes()
    self.__gerenciador_fases = GerenciadorFases(window_surface, self.__configuracoes, 'recursos/csv')
    self.__fase = self.__gerenciador_fases.gerar_fase()
    self.__placar = Placar(window_surface, self.__configuracoes.fonte) 
    self.__jogo_dao = JogoDAO()
    self.__relogio = Relogio()
    self.__timer = pg.time.Clock()
    self.__tempo_total = 0
    self.__baus_totais = 0
    self.__mortes_total = 0
    self.__vidas_total = self.__fase.mapa.grupo_jogador.sprite.vida
    self.__finalizou_mapas = False

  def iniciar(self):
    self.__fase.mapa.grupo_jogador.sprite.vida = self.__vidas_total
    self.__gerenciador_fases.mostrar_tela_fase()
    pg.time.wait(2000)

    while not self.__fase.checar_vitoria(self.__baus_totais, self.__placar):
      self.__timer.tick(60)

      self.__window.fill(self.__configuracoes.cor_fundo)

      self.__fase.rodar()
      self.__relogio.atualizar_tempo_execucao_jogo()
      self.__placar.atualizar_vida(self.__fase.mapa.grupo_jogador)
      self.__placar.adicionar_baus(self.__fase.controlador_movimentos.adicionar_baus_no_placar)
      self.__placar.atualizar_baus(self.__baus_totais)
      self.__placar.incrementar_mortes_inimigo(self.__fase.controlador_movimentos.incrementar_mortes_inimigo_no_placar)
      self.__placar.atualizar_mortes_inimigo()
      self.__placar.atualizar_tempo(self.__tempo_total + self.__relogio.execucao_do_jogo - 2)
      self.__fase.aumentar_dificuldade(self.__relogio)

      if self.__fase.checar_derrota():
        self.__salvar_infos_fase()
        self.__salvar_pontuacao()
        break
      
      pg.display.update()
      pg.display.flip()

    if self.__fase.concluida:
      self.__passar_de_fase()
  
  def __checar_baus_necessario(self):
    if self.__fase.dificuldade["baus_nesc"] > self.__baus_totais:
      self.__fase.mapa.grupo_jogador.sprite.vida = 0
      return True

  def checar_vitoria_jogo(self):
    if self.__finalizou_mapas:
      self.__salvar_pontuacao()
      if self.__checar_baus_necessario():
        return False
      else:
        return True
    else:
      return False

  def checar_derrota_jogo(self):
    return self.__fase.checar_derrota()

  def adicionar_baus_no_placar(self, novos_baus): 
    self.__placar.adicionar_baus(novos_baus)
    
  def incrementar_mortes_inimigo_no_placar(self):
    self.__placar.incrementar_mortes_inimigo()

  def __salvar_pontuacao(self):
    print('baus',self.__baus_totais)
    self.__jogo_dao.add(Pontuacao(self.__baus_totais, self.__mortes_total))

  def __passar_de_fase(self):
    self.__salvar_infos_fase()

    self.__placar.baus_coletados = 0
    self.__relogio.settar_comeco_jogo()

    try:
      self.__fase = self.__gerenciador_fases.gerar_fase()
      self.iniciar()
    except IndexError:
      self.__finalizou_mapas = True

  def __salvar_infos_fase(self):
    self.__mortes_total += self.__placar.mortes_inimigo
    self.__tempo_total += self.__relogio.execucao_do_jogo
    self.__baus_totais += self.__placar.baus_coletados
    self.__vidas_total = self.__fase.mapa.grupo_jogador.sprite.vida
