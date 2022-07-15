import pygame as pg
import sys
from sys import exit
from pygame.sprite import Group, GroupSingle
from Models.LeitorEventos import LeitorEventos
from Models.Mapa.GerenciadorColisao import GerenciadorColisao


class ControladorMovimentos:
    #TODO: INSERIR grupo_inimigos: Group
    # self.__grupo_inimigos = grupo_inimigos
    def __init__(self, grupo_jogador: GroupSingle, grupo_obstaculos: Group) -> None: 
        self.__leitor_eventos = LeitorEventos()
        self.__gerenciador_colisao = GerenciadorColisao(grupo_jogador, grupo_obstaculos)
        self.__grupo_jogador = grupo_jogador
        self.__grupo_obstaculos = grupo_obstaculos

    def mover_jogador(self):
        '''checa a colisão com obstáculos e 
        move o jogador de acordo com o evento'''
        jogador = self.__grupo_jogador.sprite
        direcao_jogador = jogador.get_dir()
        obstaculo_colidido = self.__gerenciador_colisao.checar_colisao_obstaculo(self.__grupo_jogador)
        if obstaculo_colidido:
            if direcao_jogador.x == -1:
                jogador.set_rect_left(obstaculo_colidido.get_rect_right()) 
                # jogador.parar()
            elif direcao_jogador.x == 1:
                jogador.set_rect_right(obstaculo_colidido.get_rect_left())
            elif direcao_jogador.y == -1:
                jogador.set_rect_top(obstaculo_colidido.get_rect_bottom())
            elif direcao_jogador.y == 1:
                jogador.set_rect_bottom(obstaculo_colidido.get_rect_top())
        else:
            evento = self.__leitor_eventos.ler_evento()
            if evento == 'FECHAR':
                pg.quit()
                sys.exit()
            elif evento == 'DIREITA':
                jogador.mover_direita()
            elif evento == 'ESQUERDA':
                jogador.mover_esquerda()
            elif evento == 'CIMA':
                jogador.mover_cima()
            elif evento == 'BAIXO':
                jogador.mover_baixo()
            else:
                jogador.parar()

    def mover_inimigo(self):
        pass

    