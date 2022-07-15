from typing import List
from pygame.sprite import Sprite, Group, GroupSingle, spritecollide, collide_rect
import pygame
from pygame import Rect
from Models.Mapa.Tile import Tile
from Models.Jogador import Jogador
from Models.Configuracoes import Configuracoes
from Models.GerenciadorColisao import GerenciadorColisao
from Models.Mapa.ControladorMovimentos import ControladorMovimentos

class Mapa:
    def __init__(self, layout_mapa: list, surface) -> None:
        self.__surface_janela = surface
        self.__configuracoes = Configuracoes()
        self.preparar_mapa(layout_mapa)
        self.__deslocamento = 0
    
    def preparar_mapa(self, layout_mapa: list) -> None:
        self.__tiles = Group()
        self.__grupo_jogador = GroupSingle()
        for indice_linha,linha in enumerate(layout_mapa):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * self.__configuracoes.tamanho_tile
                y = indice_linha * self.__configuracoes.tamanho_tile
                if coluna == 'X':
                    tile = Tile((x,y), self.__configuracoes.tamanho_tile)
                    self.__tiles.add(tile)
                if coluna == 'P':
                    self.__jogador = Jogador((x,y))
                    self.__grupo_jogador.add(self.__jogador)
                    # self.__tiles.add(self.__jogador)
        self.__controlador_movimentos = ControladorMovimentos(self.__grupo_jogador, self.__tiles)
        print(len(self.__tiles))

    @property
    def tiles(self) -> list:
        return self.__tiles

    @property
    def grupo_jogador(self) -> GroupSingle:
        return self.__grupo_jogador

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    def scroll_x(self):
        jogador = self.__jogador
        x_jogador = jogador.get_centerx()
        direcao_x = jogador.get_dirx()
        largura_tela = self.__configuracoes.largura_tela
        
        if x_jogador < (largura_tela / 4) and direcao_x < 0:
            self.__deslocamento = 3
            jogador.velocidade = 0
        elif x_jogador > largura_tela - (largura_tela / 4) and direcao_x > 0:
            self.__deslocamento = -(3)
            jogador.velocidade = 0
        else:
            self.__deslocamento = 0
            jogador.velocidade = 3

    # def horizontal_mov_col(self):
        # jogador = self.__jogador
        # jogador.mover_x()
        
        #TODO: COLOCAR TESTE DE COLISÃO ABAIXO DENTRO DO GERENCIADOR DE COLISÃO

        # for tile_sprite in self.__tiles.sprites():
        #     if tile_sprite.rect.colliderect(jogador.rect):
        #         tile_sprite.image.fill('red')
                # if jogador.direcao.x > 0:
                #     print('oi')
                #     jogador.rect.right = tile_sprite.rect.left
         


    def run(self) -> None:
        #Mapa
        self.__tiles.update(self.__deslocamento)
        self.__tiles.draw(self.__surface_janela)
        self.scroll_x()

        #Jogador
        self.__controlador_movimentos.mover_jogador()
        self.__grupo_jogador.draw(self.__surface_janela)
        # self.horizontal_mov_col()
        
