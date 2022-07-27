import pygame as pg
import sys
from sys import exit
from pygame.sprite import Group, GroupSingle
from Models.LeitorEventos import LeitorEventos
from Models.Mapa.GerenciadorColisao import GerenciadorColisao
from Models.LeitorPause import LeitorPause


class ControladorMovimentos:
    def __init__(self, mapa, adicionar_baus_no_placar, incrementar_mortes_inimigo_no_placar) -> None: 
        self.__mapa = mapa
        self.__adicionar_baus_no_placar = adicionar_baus_no_placar
        self.__incrementar_mortes_inimigo_no_placar = incrementar_mortes_inimigo_no_placar
        self.__leitor_eventos = LeitorEventos()
        self.__gerenciador_colisao = GerenciadorColisao(mapa.grupo_jogador, mapa.grupo_inimigo, mapa.tiles, mapa.grupo_armaduras, mapa.grupo_baus, mapa.grupo_portais)
        self.__grupo_jogador = mapa.grupo_jogador
        self.__grupo_inimigos = mapa.grupo_inimigo
        # self.__grupo_obstaculos = grupo_obstaculos
        # self.__configuracoes = Configuracoes()
        # self.__grupo_armaduras = grupo_armaduras
        # self.__grupo_armaduras = grupo_armaduras

    def mover_jogador(self):
        '''checa a colisão com obstáculos e 
        move o jogador de acordo com o evento'''
        evento = self.__leitor_eventos.ler_evento()
        jogador = self.__grupo_jogador.sprite
        direcao_jogador = jogador.get_dir()
        self.__gerenciador_colisao.checar_colisao_inimigo(self.__incrementar_mortes_inimigo_no_placar)
        portal_colidido = self.__gerenciador_colisao.checar_colisao_portal()
        if portal_colidido and jogador.baus > 0:
            self.__adicionar_baus_no_placar(jogador.baus)
            jogador.baus = 0
            # TODO: Atualizar a imagem
        bau_colidido = self.__gerenciador_colisao.checar_colisao_bau()
        if bau_colidido:
            jogador.baus += 1
            # TODO: Atualizar a imagem
            bau_colidido.kill()
        armadura_colidida = self.__gerenciador_colisao.checar_colisao_armadura()
        if armadura_colidida:
            jogador.armadura = True
            jogador.atualizar_imagem()
            armadura_colidida.kill()
        obstaculo_colidido = self.__gerenciador_colisao.checar_colisao_obstaculo(self.__grupo_jogador)
        if obstaculo_colidido:
            if direcao_jogador.x == -1:
                jogador.set_rect_left(obstaculo_colidido.get_rect_right()) 
            elif direcao_jogador.x == 1:
                jogador.set_rect_right(obstaculo_colidido.get_rect_left())
            elif direcao_jogador.y == -1:
                jogador.set_rect_top(obstaculo_colidido.get_rect_bottom())
            elif direcao_jogador.y == 1:
                jogador.set_rect_bottom(obstaculo_colidido.get_rect_top())
        else:
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
            elif evento == 'Paused':
                print('olha nois aqui no leitor')
                LeitorPause.detect()
            else:
                jogador.parar()
            

    def mover_inimigo(self, janela):
        jogador = self.__grupo_jogador.sprite
        x_jogador = jogador.get_centerx()
        y_jogador = jogador.get_centery()

        for inimigo in self.__grupo_inimigos.sprites():
            print(inimigo.get_coordenadas())
            dif_x = x_jogador - inimigo.get_centerx()
            dif_y = y_jogador - inimigo.get_centery() 
            distancia = (dif_x**2 + dif_y**2)**(1/2)
            if distancia <= 150:
                inimigo.seguir_jogador(jogador.get_coordenadas(), janela)
            else:
                inimigo.pegar_tesouro((128,128))

