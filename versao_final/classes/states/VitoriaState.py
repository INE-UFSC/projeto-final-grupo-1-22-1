import pygame as pg
from classes.states.State import State
from classes.componentes.Button import Button
from classes.configuracoes.Configuracoes import Configuracoes

class VitoriaState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(window, transition_to)
        self.__largura_tela = self.configuracoes.largura_tela
        self.__altura_tela = self.configuracoes.altura_tela
        self.__surface = self.window.surface
        self.__game_over_bg_img = pg.transform.scale(
            pg.image.load("recursos/imagens/CreditsBG.png"), (self.__largura_tela, self.__altura_tela))
        self.__ganhou = pg.image.load("recursos/imagens/Victory.png")
        back_off_img = pg.image.load("recursos/imagens/BackOff.png").convert_alpha()
        back_on_img = pg.image.load("recursos/imagens/BackOn.png").convert_alpha()
        BUTTONS_SCALE = 1
        SPACE_BEFORE = 20
        SPACE_LEFT = self.__largura_tela * 0.75
        self.__back_button = Button(
            SPACE_LEFT, SPACE_BEFORE, back_off_img, back_on_img, BUTTONS_SCALE)
    
    def checar_eventos(self):
        self.__back_button.read_events()
        if self.__back_button.clicked:
            self.transicionar("MenuState")

    def renderizar(self):
        self.__surface.blit(self.__game_over_bg_img, (0, 0))
        self.__surface.blit(self.__ganhou, (int(self.__largura_tela/2)-200, int(self.__altura_tela/2)-70))
        self.checar_eventos()
        self.__back_button.draw(self.__surface)
