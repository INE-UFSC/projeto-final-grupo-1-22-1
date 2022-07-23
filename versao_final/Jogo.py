import pygame as pg
from pygame.locals import *

from Models.Window import Window
from Models.Configuracoes import Configuracoes
from Models.States.JogoState import JogoState
from Models.States.MenuState import MenuState
from Models.States.CreditosState import CreditosState
from Models.States.OptionsState import OptionsState
from Models.States.RankingState import RankingState
from Models.States.GameOverState import GameOverState
from Models.States.StateMachine import StateMachine


class Jogo():
    def __init__(self):
        self.__configuracoes = Configuracoes()
        self.__window = Window((self.__configuracoes.largura_tela,
                               self.__configuracoes.altura_tela), "Copper Temple - Alfa")
        pg.init()
        STATES_DICT = {
            "MenuState": MenuState,
            "JogoState": JogoState,
            "CreditosState": CreditosState,
            "OptionsState": OptionsState,
            "RankingState": RankingState,
            "GameOverState": GameOverState
        }
        INITIAL_STATE = "MenuState"
        self.__state_machine = StateMachine(STATES_DICT, INITIAL_STATE)

    def run(self):
        run = True

        while run:
            tela = self.__state_machine.render_state(self.__window)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        tela.transicionar(self.__state_machine.initial_state)
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()
            pg.display.flip()

        pg.quit()
