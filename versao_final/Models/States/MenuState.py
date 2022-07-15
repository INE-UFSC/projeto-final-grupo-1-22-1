from Models.States.State import State
import pygame as pg
from Models.button import Button


class MenuState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__window = window
        self.__surface = self.__window.surface
        self.__menu_bg_img = pg.image.load("Images/MainMenu.png")
        self.__title = pg.image.load("Images/Titulo.png")
        play_off_img = pg.image.load("Images/PlayOff.png").convert_alpha()
        play_on_img = pg.image.load("Images/PlayOn.png").convert_alpha()
        ranking_off_img = pg.image.load(
            "Images/RankingOff.png").convert_alpha()
        ranking_on_img = pg.image.load("Images/RankingOn.png").convert_alpha()
        options_off_img = pg.image.load(
            "Images/OptionsOff.png").convert_alpha()
        options_on_img = pg.image.load("Images/OptionsOn.png").convert_alpha()
        credits_off_img = pg.image.load(
            "Images/CreditsOff.png").convert_alpha()
        credits_on_img = pg.image.load("Images/CreditsOn.png").convert_alpha()

        self.__play_button = Button(
            40, 20, play_off_img, play_on_img, 1)
        self.__ranking_button = Button(
            40, 140, ranking_off_img, ranking_on_img, 1)
        self.__options_button = Button(
            40, 255, options_off_img, options_on_img, 1)
        self.__credits_button = Button(
            40, 370, credits_off_img, credits_on_img, 1)

    def checar_cliques(self):
        if self.__play_button.clique(self.__surface):
            self.transicionar("JogoState")
        if self.__ranking_button.clique(self.__surface):
            self.transicionar("RankingState")
        if self.__options_button.clique(self.__surface):
            self.transicionar("OptionsState")
        if self.__credits_button.clique(self.__surface):
            self.transicionar("CreditosState")

    def renderizar(self):
        self.__surface.blit(self.__menu_bg_img, (0, 0))

        self.__surface.blit(self.__title, (280, 235))

        self.__play_button.draw(self.__surface)
        self.__ranking_button.draw(self.__surface)
        self.__options_button.draw(self.__surface)
        self.__credits_button.draw(self.__surface)
        self.checar_cliques()
