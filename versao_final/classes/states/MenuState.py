from classes.states.State import State
import pygame as pg
from classes.componentes.Button import Button
from classes.configuracoes.Configuracoes import Configuracoes


class MenuState(State):
    def __init__(self, window, transition_to):
        super().__init__(window, transition_to)
        self.__largura_tela = self.configuracoes.largura_tela
        self.__altura_tela = self.configuracoes.altura_tela
        self.__surface = self.window.surface
        self.__menu_bg_img = pg.transform.scale(
            pg.image.load("recursos/imagens/MainMenu.png"), (self.__largura_tela, self.__altura_tela))
        self.__title = pg.transform.scale(pg.image.load(
            "recursos/imagens/Titulo.png"), (self.__largura_tela / 2, self.__altura_tela / 2))

        play_off_img = pg.image.load("recursos/imagens/PlayOff.png").convert_alpha()
        play_on_img = pg.image.load("recursos/imagens/PlayOn.png").convert_alpha()
        ranking_off_img = pg.image.load(
            "recursos/imagens/RankingOff.png").convert_alpha()
        ranking_on_img = pg.image.load("recursos/imagens/RankingOn.png").convert_alpha()
        options_off_img = pg.image.load(
            "recursos/imagens/OptionsOff.png").convert_alpha()
        options_on_img = pg.image.load("recursos/imagens/OptionsOn.png").convert_alpha()
        credits_off_img = pg.image.load(
            "recursos/imagens/CreditsOff.png").convert_alpha()
        credits_on_img = pg.image.load("recursos/imagens/CreditsOn.png").convert_alpha()

        BUTTONS_SCALE = 1.25
        SPACE_BEFORE = 35
        SPACE_LEFT = self.__largura_tela / 16
        row = (self.__altura_tela - SPACE_BEFORE * 2) / 4
        self.__play_button = Button(
            SPACE_LEFT, SPACE_BEFORE, play_off_img, play_on_img, BUTTONS_SCALE)
        self.__ranking_button = Button(
            SPACE_LEFT, row + SPACE_BEFORE, ranking_off_img, ranking_on_img, BUTTONS_SCALE)
        self.__options_button = Button(
            SPACE_LEFT, row * 2 + SPACE_BEFORE, options_off_img, options_on_img, BUTTONS_SCALE)
        self.__credits_button = Button(
            SPACE_LEFT, row * 3 + SPACE_BEFORE, credits_off_img, credits_on_img, BUTTONS_SCALE)

    def renderizar(self):
        self.__surface.blit(self.__menu_bg_img, (0, 0))

        self.__surface.blit(
            self.__title, (self.__largura_tela / 2 - self.__largura_tela / 32, self.__altura_tela / 2 - 40))

        self.checar_eventos()
        self.__play_button.draw(self.__surface)
        self.__ranking_button.draw(self.__surface)
        self.__options_button.draw(self.__surface)
        self.__credits_button.draw(self.__surface)

    def checar_eventos(self):
        self.__play_button.read_events()
        self.__ranking_button.read_events()
        self.__options_button.read_events()
        self.__credits_button.read_events()

        if self.__play_button.clicked:
            self.transicionar("JogoState")
        elif self.__ranking_button.clicked:
            self.transicionar("RankingState")
        elif self.__options_button.clicked:
            self.transicionar("OptionsState")
        elif self.__credits_button.clicked:
            self.transicionar("CreditosState")
