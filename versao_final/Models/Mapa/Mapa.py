from typing import List
from pygame.sprite import Sprite, Group, GroupSingle, spritecollide, collide_rect
import pygame
from pygame import Rect
from Models.Mapa.Tile import Tile
from Models.Jogador import Jogador
from Models.Configuracoes import Configuracoes
from Models.GerenciadorColisao import GerenciadorColisao
from Models.Mapa.ControladorMovimentos import ControladorMovimentos
from Models.Inimigo import Inimigo

class Mapa:
    def __init__(self, layout_mapa: list, surface, largura_mapa, altura_mapa, tamanho_tile) -> None:
        self.__surface_janela = surface
        self.__configuracoes = Configuracoes()
        self.__largura_mapa = largura_mapa
        self.__altura_mapa = altura_mapa
        self.__tamanho_tile = tamanho_tile
        self.preparar_mapa(layout_mapa)
        self.__deslocamento_x = 0
        self.__deslocado_x = 0
        self.__deslocamento_y = 0
        self.__deslocado_y = 0
    
    def preparar_mapa(self, layout_mapa: list) -> None:
        self.__tiles = Group()
        self.__grupo_jogador = GroupSingle()
        self.__grupo_inimigo = Group()
        for indice_linha,linha in enumerate(layout_mapa):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * self.__tamanho_tile
                y = indice_linha * self.__tamanho_tile
                if coluna == 'X':
                    tile = Tile((x,y), self.__tamanho_tile)
                    self.__tiles.add(tile)
                elif coluna == 'P':
                    self.__jogador = Jogador(self.__configuracoes.velocidade_jogador, (x,y))
                    self.__grupo_jogador.add(self.__jogador)
                    # self.__tiles.add(self.__jogador)
                elif coluna == 'I':
                    self.__inimigo = Inimigo(self.__configuracoes.velocidade_inimigo, (x, y))
                    self.__grupo_inimigo.add(self.__inimigo)
    
        self.__controlador_movimentos = ControladorMovimentos(self.__grupo_jogador, self.__grupo_inimigo, self.__tiles, self.__configuracoes)

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
        direcao_y = jogador.get_diry()
        largura_tela = self.__configuracoes.largura_tela
        y_jogador = jogador.get_centery()
        altura_tela = self.__configuracoes.altura_tela
        
        # if direcao_x != 0:
        ####print('andando em x')
        if x_jogador < (largura_tela / 4) and direcao_x < 0 and self.__deslocado_x < 0:
            self.__deslocamento_x = 3
            self.__deslocado_x += 3
            jogador.velocidade = 0
        elif x_jogador > largura_tela - (largura_tela / 4) and direcao_x > 0 and - (self.__deslocado_x) < self.__largura_mapa - largura_tela:
            self.__deslocamento_x = -(3)
            self.__deslocado_x -= 3
            jogador.velocidade = 0
        else:
            self.__deslocamento_x = 0
            jogador.velocidade = self.__configuracoes.velocidade_jogador
        # elif direcao_y != 0:
        #     print('andando em y')
        #     if y_jogador < (altura_tela / 4) and direcao_y < 0 and self.__deslocado_y < 0:
        #         self.__deslocamento_y += 3
        #         self.__deslocado_y += 3
        #         jogador.velocidade = 0
        #     elif y_jogador > altura_tela - (altura_tela / 4) and direcao_y > 0 and -(self.__deslocado_y) < self.__configuracoes.altura_mapa - altura_tela:
        #         self.__deslocamento_y = -(3)
        #         self.__deslocado_y -= 3
        #         jogador.velocidade = 0
        #     else:
        #         self.__deslocamento_y = 0
        #         jogador.velocidade = self.__configuracoes.velocidade_jogador

        ####print('deslocado', self.__deslocado_x)
    
    # def scroll_y(self):
    #     jogador = self.__jogador
        
        
    #     print('deslocado-y', self.__deslocado_y)


    def run(self) -> None:
        #Mapa
        self.__tiles.update(self.__deslocamento_x, self.__deslocamento_y)
        self.__tiles.draw(self.__surface_janela)
        self.scroll_x()


        #Jogador
        self.__controlador_movimentos.mover_jogador()
        self.__controlador_movimentos.atualizar_vida_jogador()
        self.__grupo_jogador.draw(self.__surface_janela)
        self.__grupo_jogador.update(self.__deslocamento_x, self.__deslocamento_y)
        # self.horizontal_mov_col()
        
        #Inimigo
        self.__controlador_movimentos.mover_inimigo()
        self.__grupo_inimigo.draw(self.__surface_janela)
        self.__grupo_inimigo.update(self.__deslocamento_x, self.__deslocamento_y)

        # for inimigo in self.__grupo_inimigo.sprites():
        #     inimigo.draw(self.__surface_janela)
        #  self.__surface_janela.blit(inimigo.get_imagem(), (inimigo.get_coordenadas()[0] - int(inimigo.get_imagem().get_width()) / 2, inimigo.get_coordenadas()[1] - int(inimigo.get_imagem().get_height()) / 2))
        #self.__window_surface.blit(inimigo.get_imagem(), (inimigo.get_coordenadas()[0] - int(inimigo.get_imagem().get_width()) / 2, inimigo.get_coordenadas()[1] - int(inimigo.get_imagem().get_height()) / 2))

