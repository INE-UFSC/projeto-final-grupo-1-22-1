import pygame as pg
from pygame.locals import *
from classes.states.VitoriaState import VitoriaState
from classes.componentes.Window import Window
from classes.configuracoes.Configuracoes import Configuracoes
from classes.states.JogoState import JogoState
from classes.states.MenuState import MenuState
from classes.states.CreditosState import CreditosState
from classes.states.OptionsState import OptionsState
from classes.states.RankingState import RankingState
from classes.states.GameOverState import GameOverState
from classes.states.StateMachine import StateMachine
from classes.componentes.Musica import Musica


class Jogo():
    def __init__(self) -> None:
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
            "GameOverState": GameOverState,
            "VitoriaState": VitoriaState
        }
        INITIAL_STATE = "MenuState"
        self.__state_machine = StateMachine(STATES_DICT, INITIAL_STATE)

    def run(self) -> None:
        Musica.musica_jogo()
        Musica.tocar_musica()
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
