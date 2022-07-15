import pygame as pg
from Models.States.State import State


class OptionsState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(transition_to)
        self.__surface = window.surface

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.__surface.blit(img, (x, y))

    def renderizar(self):
        self.__surface.fill((52, 78, 91))

        self.draw_text("OptionsState menu", pg.font.SysFont("arialblack", 40),
                       (255, 255, 255), 160, 250)
