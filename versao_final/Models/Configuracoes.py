from pygame import font

from Models.Singleton import Singleton


class Configuracoes(Singleton):
    def init(self):
        font.init()
        self.__fonte = font.SysFont('comicsans', 20)
        self.__largura_tela = 720
        self.__altura_tela = 540
        self.__velocidade_jogador = 3
        self.__velocidade_inimigo = 1
        self.__vol_control = 1
        self.__dif_control = 0
        self.__music_control = 0

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
    def velocidade_jogador(self):
        return self.__velocidade_jogador

    @property
    def velocidade_inimigo(self):
        return self.__velocidade_inimigo

    @property
    def vol_control(self):
        return self.__vol_control

    @property
    def music_control(self):
        return self.__music_control

    @property
    def dif_control(self):
        return self.__dif_control

    @vol_control.setter
    def vol_control(self, new_volum):
        self.__vol_control = new_volum

    @music_control.setter
    def music_control(self, new_music):
        self.__music_control = new_music

    @dif_control.setter
    def dif_control(self, new_dif):
        self.__dif_control = new_dif