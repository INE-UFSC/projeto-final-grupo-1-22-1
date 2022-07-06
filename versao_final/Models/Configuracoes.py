from pygame import font

from Models.Singleton import Singleton


class Configuracoes(Singleton):
    def init(self):
        font.init()

        self.__fonte = font.SysFont('comicsans', 50)

    @property
    def fonte(self):
        return self.__fonte
