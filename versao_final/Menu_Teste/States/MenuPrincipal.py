from States.State import State
import pygame as pg
from button import Button


class MenuPrincipal(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__window = window
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
            self.transicionar("Jogo")
        if self.__ranking_button.draw(self.__window):
            self.transicionar("Ranking")
        if self.__options_button.draw(self.__window):
            self.transicionar("Options")
        if self.__credits_button.draw(self.__window):
            self.transicionar("Creditos")
