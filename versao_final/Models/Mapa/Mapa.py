from typing import List
from pygame.sprite import Sprite, Group, GroupSingle, spritecollide, collide_rect
import pygame
from pygame import Rect
from Models.Mapa.Tile import Tile
from Models.Jogador import Jogador
from Models.Configuracoes import Configuracoes
from Models.GerenciadorColisao import GerenciadorColisao

class Mapa:
    def __init__(self, layout_mapa, surface, leitor_eventos) -> None:
        self.__leitor_eventos = leitor_eventos
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
                    self.__tiles.add(self.__jogador)

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
        x_jogador = jogador.rect.centerx
        direcao_x = jogador.direcao.x
        largura_tela = self.__configuracoes.largura_tela
        evento = self.__leitor_eventos.ler_evento()
        
        if x_jogador < (largura_tela / 4) and direcao_x < 0 and evento == 'ESQUERDA':
            self.__deslocamento = 8
            jogador.velocidade = 0
        elif x_jogador > largura_tela - (largura_tela / 4) and direcao_x > 0 and evento == 'DIREITA':
            self.__deslocamento = -(8)
            jogador.velocidade = 0
        else:
            self.__deslocamento = 0
            jogador.velocidade = 8

    def horizontal_mov_col(self):
        jogador = self.__jogador
        jogador.rect.x += jogador.direcao.x * jogador.velocidade
        
        for tile_sprite in self.__tiles.sprites():
            if tile_sprite.rect.colliderect(jogador.rect) and tile_sprite != jogador:
                tile_sprite.image.fill('red')
            #     #     jogador.rect.left = tile_sprite.rect.right
            #     # elif jogador.direcao.x > 0:
            #     #     jogador.rect.right = tile_sprite.rect.left
            # else:
            #     print('tchau')
        #     if :
        #         print(jogador.get_coordenadas())
        #         # print('colisao', jogador.direcao.x)
        #         # print(jogador.direcao.x)


    def run(self) -> None:
        #Mapa
        self.__tiles.update(self.__deslocamento)
        self.__tiles.draw(self.__surface_janela)
        self.scroll_x()

        #Jogador
        self.__grupo_jogador.draw(self.__surface_janela)
        self.horizontal_mov_col()
        
