from pygame import font

from Models.Singleton import Singleton


class Configuracoes(Singleton):
    def init(self):
        font.init()
        self.__mapa = ['                            ',
                       '                            ',
                       '                            ',
                       ' XX    XXX            X     ',
                       ' XX                         ',
                       ' XXXX    P    XX         XX ',
                       ' XXXX       XX              ',
                       ' XX    X  XXXX    XX  XX    ',
                       '       X  XXXX    XX  XXX   ',
                       '    XXXX  XXXXXX  XX  XXXX  ',
                       'XXXXXXXX  XXXXXX  XX  XXXX  ']
        self.__tamanho_tile = 64
        self.__largura_tela = 1200
        self.__altura_tela = len(self.__mapa) * self.__tamanho_tile
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
