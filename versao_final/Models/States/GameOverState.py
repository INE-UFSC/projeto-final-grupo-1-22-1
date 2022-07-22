import pygame as pg
from Models.States.State import State
from Models.Configuracoes import Configuracoes


class GameOverState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(transition_to)
        self.__window = window
        self.__configuracoes = Configuracoes()
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__surface = self.__window.surface
        self.__game_over_bg_img = pg.transform.scale(
            pg.image.load("Images/GameOver.png"), (self.__largura_tela, self.__altura_tela))

    def renderizar(self):
        self.__surface.blit(self.__game_over_bg_img, (0, 0))