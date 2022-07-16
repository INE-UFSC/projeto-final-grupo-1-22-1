import pygame as pg
from pygame.locals import *

from Models.Window import Window
from Models.Configuracoes import Configuracoes
from Models.States.JogoState import JogoState
from Models.States.MenuState import MenuState
from Models.States.CreditosState import CreditosState
from Models.States.OptionsState import OptionsState
from Models.States.RankingState import RankingState

STATES = {
    "MenuState": MenuState,
    "JogoState": JogoState,
    "CreditosState": CreditosState,
    "OptionsState": OptionsState,
    "RankingState": RankingState
}
class Jogo():
    def __init__(self):
        self.__configuracoes = Configuracoes()
        self.__window = Window((self.__configuracoes.largura_tela,
                               self.__configuracoes.altura_tela), "Cooper Temple - Alfa")
        pg.init()
        self.__state = "MenuState"

    def transition_to(self, new_state):
        if self.__state != new_state:
            print(f"Context: Transition to {new_state}")
            self.__state = new_state

    def run(self):
        run = True

        while run:

            if self.__state in STATES:
                tela = STATES[self.__state](self.__window, self.transition_to)
                tela.renderizar()
            else:
                tela.transicionar("MenuState")
                tela = MenuState(self.__window, self.transition_to)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        tela.transicionar("MenuState")
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()
            pg.display.flip()

        pg.quit()
