import pygame as pg
from Models.States.State import State
from Models.button import Button
from Models.Configuracoes import Configuracoes


class OptionsState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(transition_to)
        self.__window = window
        self.__configuracoes = Configuracoes()
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__surface = self.__window.surface
        self.__credits_bg_img = pg.transform.scale(
            pg.image.load("Images/OptionsBG.png"), (self.__largura_tela, self.__altura_tela))
        
        back_off_img = pg.image.load("Images/BackOff.png").convert_alpha()
        back_on_img = pg.image.load("Images/BackOn.png").convert_alpha()

        BUTTONS_SCALE = 1
        SPACE_BEFORE = 20
        SPACE_LEFT = self.__largura_tela / 50
        self.__back_button = Button(
            SPACE_LEFT, SPACE_BEFORE, back_off_img, back_on_img, BUTTONS_SCALE)

    def checar_eventos(self):
        self.__back_button.read_events()

        if self.__back_button.clicked:
            self.transicionar("MenuState")

    def renderizar(self):
        self.__surface.blit(self.__credits_bg_img, (0, 0))

        self.checar_eventos()
        self.__back_button.draw(self.__surface)
