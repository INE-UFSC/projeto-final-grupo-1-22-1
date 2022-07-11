from States.State import State
import pygame as pg
from States.Creditos import Creditos
from button import Button


class MenuPrincipal(State):
    def __init__(self, window, controlador):
        self.__window = window
        self.__controlador = controlador
        self.__menu_bg_img = pg.image.load("images/MainMenu.png")
        self.__title = pg.image.load("images/Titulo.png")
        play_off_img = pg.image.load("images/PlayOff.png").convert_alpha()
        play_on_img = pg.image.load("images/PlayOn.png").convert_alpha()
        ranking_off_img = pg.image.load(
            "images/RankingOff.png").convert_alpha()
        ranking_on_img = pg.image.load("images/RankingOn.png").convert_alpha()
        options_off_img = pg.image.load(
            "images/OptionsOff.png").convert_alpha()
        options_on_img = pg.image.load("images/OptionsOn.png").convert_alpha()
        credits_off_img = pg.image.load(
            "images/CreditsOff.png").convert_alpha()
        credits_on_img = pg.image.load("images/CreditsOn.png").convert_alpha()

        self.__play_button = Button(
            40, 20, play_off_img, play_on_img, 1)
        self.__ranking_button = Button(
            40, 140, ranking_off_img, ranking_on_img, 1)
        self.__options_button = Button(
            40, 255, options_off_img, options_on_img, 1)
        self.__credits_button = Button(
            40, 370, credits_off_img, credits_on_img, 1)

        self.__window.blit(self.__menu_bg_img, (0, 0))

        self.__window.blit(self.__title, (280, 235))
        if self.__play_button.draw(self.__window):
            self.__controlador.state = "jogo"
        if self.__ranking_button.draw(self.__window):
            self.__controlador.state = "ranking"
        if self.__options_button.draw(self.__window):
            self.__controlador.state = "options"
        if self.__credits_button.draw(self.__window):
            self.__controlador.state = "credits"

    def renderizar(self, next_state):
        self.context.transition_to(next_state(
            self.__window, self.__controlador))
