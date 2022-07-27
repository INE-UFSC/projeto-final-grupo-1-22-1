import pygame as pg
import time
from pygame.sprite import GroupSingle
from Models.States.State import State
from Models.Configuracoes import Configuracoes
from Models.Mapa.Mapa import Mapa
from Models.Mapa.Inimigo import Inimigo
from Models.ControladorJogo import ControladorJogo
from Models.Pause import Pause
from Models.LeitorPause import LeitorPause


class JogoState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__configuracoes = Configuracoes()
        self.__window = window
        self.__window_surface = self.__window.surface
        self.__timer = pg.time.Clock()
        self.__controlador_jogo = ControladorJogo(self.__window_surface)
        self.pause_state = False
        self.__pause = Pause(self.__window)
        self.__leitor_pause = LeitorPause()
        

    def renderizar(self):
        controlador_jogo = self.__controlador_jogo
        while True:
            self.__timer.tick(60)
            # self.pause_state = self.__leitor_pause.paused(self.pause_state)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        print('loopin get')
                        self.pause_state = not self.pause_state
            
            # self.pause_state = self.__leitor_pause.paused()

            # while self.pause_state:
            #     self.__pause.renderizar()
            #     self.pause_state = self.__leitor_pause.paused(self.pause_state)
            #     pg.display.update()
            #     pg.display.flip()
                

            if not self.pause_state:
                self.__window_surface.fill((54, 107, 95))

                controlador_jogo.iniciar()

                if controlador_jogo.game_over():
                    self.transicionar("GameOverState")
                    break
            else:
                self.__pause.renderizar()

            pg.display.update()
            pg.display.flip()
