import pygame as pg
from Models.States.State import State
from Models.Configuracoes import Configuracoes

class Pause():
    def __init__(self, window) -> None:
        self.__window = window
        self.__configuracoes = Configuracoes()
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__surface = self.__window.surface
        self.__pause_bg_img = pg.transform.scale(
            pg.image.load("Images/Pause.png"), (self.__largura_tela, self.__altura_tela))

    def pausar(self, signal: bool) -> bool:
        return not signal


    def renderizar(self):
        self.__surface.blit(self.__pause_bg_img, (0, 0))