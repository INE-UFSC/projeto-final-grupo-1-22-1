import pygame as pg
import sys
from Models.LeitorEventos import LeitorEventos
from Models.Mapa.GerenciadorColisao import GerenciadorColisao


class ControladorMovimentos:
    #adicionar_baus_no_placar, incrementar_mortes_inimigo_no_placar
    def __init__(self, mapa) -> None: 
        # self.__adicionar_baus_no_placar = adicionar_baus_no_placar
        # self.__incrementar_mortes_inimigo_no_placar = incrementar_mortes_inimigo_no_placar
        self.__leitor_eventos = LeitorEventos()
        self.__gerenciador_colisao = GerenciadorColisao(mapa.grupo_jogador, mapa.grupo_inimigo, mapa.grupo_obstaculos, mapa.grupo_armaduras, mapa.grupo_baus, mapa.grupo_portais)
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
        obstaculo_colidido = self.__gerenciador_colisao.checar_colisao_obstaculo(jogador)
        inimigos_colididos = self.__gerenciador_colisao.checar_colisao_inimigo()
        portal_colidido = self.__gerenciador_colisao.checar_colisao_portal()
        if inimigos_colididos:
            if jogador.armadura:
                jogador.armadura = None
                # incrementar_mortes_inimigo_no_placar()
                inimigos_colididos[0].kill()
                jogador.atualizar_imagem()
            else:
                jogador.baus = 0
                jogador.renascer(jogador.posicao_inicial)
                jogador.diminuir_vida()
                return True
        if portal_colidido and jogador.baus > 0:
            print('colidiu com o portal')
            # self.__adicionar_baus_no_placar(jogador.baus)
            jogador.baus = 0
            # TODO: Atualizar a imagem
        bau_colidido = self.__gerenciador_colisao.checar_colisao_bau()
        if bau_colidido:
            print('colidiu com o bau')
            jogador.baus += 1
            # TODO: Atualizar a imagem
            bau_colidido.kill()
        armadura_colidida = self.__gerenciador_colisao.checar_colisao_armadura()
        if armadura_colidida:
            jogador.armadura = True
            jogador.atualizar_imagem()
            armadura_colidida.kill()
        obstaculo_colidido = self.__gerenciador_colisao.checar_colisao_obstaculo(self.__grupo_jogador.sprite)
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
            else:
                jogador.parar()

    def mover_inimigo(self):
        inimigos = self.__grupo_inimigos.sprites()

        for inimigo in inimigos:
            
            obstaculo_colidido = self.__gerenciador_colisao.checar_colisao_obstaculo(inimigo)
            if obstaculo_colidido:
                if inimigo.sentido == 'baixo':
                    inimigo.mover_inim(-1)
                    inimigo.sentido = 'cima'
                else:
                    inimigo.mover_inim(1)
                    inimigo.sentido = 'baixo'
            else:
                if inimigo.sentido == 'baixo':
                    inimigo.mover_inim(1)
                else:
                    inimigo.mover_inim(-1)
