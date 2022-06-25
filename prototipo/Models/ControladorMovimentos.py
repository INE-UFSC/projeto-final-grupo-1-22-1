from Models.Jogador import Jogador
from Models.LeitorColisao import LeitorColisao
import pygame as pg


class ControladorMovimentos():
  def __init__(self, jogador: Jogador, grupo_jogador, grupo_obstaculos):
    self.__jogador = jogador
    self.__leitor_colisao = LeitorColisao(grupo_jogador, grupo_obstaculos)
  
  def mover_personagem(self, evento, personagem):
    if not self.__leitor_colisao.checar_colisao(self.__jogador.sprite):
      if evento == "fechar":
        pg.quit()
      elif evento == "mover-dir":
        personagem.mover_dir()
      elif evento == "mover-esq":
        personagem.mover_esq()
      elif evento == "mover-up":
        personagem.mover_cim()
      elif evento == 'mover-down':
        personagem.mover_bai()
    else:
      print('porra')
      print(evento)
      
