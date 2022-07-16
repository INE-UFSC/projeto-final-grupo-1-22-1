from pygame import font

from Models.Singleton import Singleton


class Configuracoes(Singleton):
    def init(self):
        font.init()
        self.__mapa = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                       'X                          X',
                       'X                           ',
                       'X X    XXX            X    X',
                       'X X                        X',
                       'X XXX    P    XX         XXX',
                       'X XXX       XX             X',
                       'X X    X  XXXX    XX  XX   X',
                       'X      X  XXXX    XX  XXX  X',
                       'X   XXXX  XXXXXX  XX  XXXX X',
                       'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
        self.__velocidade_jogador = 3
        self.__tamanho_tile = 64
        self.__largura_mapa = len(self.__mapa[0]) * self.tamanho_tile
        self.__altura_mapa = len(self.__mapa) * self.tamanho_tile
        self.__largura_tela = 640
        self.__altura_tela = 480
        self.__fonte = font.SysFont('comicsans', 50)

    @property
    def fonte(self):
        return self.__fonte 

    @property
    def largura_tela(self):
        return self.__largura_tela

    @property
    def altura_tela(self):
        return self.__altura_tela

    @property
    def mapa(self):
        return self.__mapa

    @property
    def tamanho_tile(self):
        return self.__tamanho_tile

    @property
    def largura_mapa(self):
        return self.__largura_mapa

    @property
    def altura_mapa(self):
        return self.__altura_mapa

    @property
    def velocidade_jogador(self):
        return self.__velocidade_jogador
