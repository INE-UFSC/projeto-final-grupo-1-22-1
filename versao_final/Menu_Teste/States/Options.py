import pygame as pg
from States.State import State


class Options(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(transition_to)
        self.__window = window
        self.__window.fill((52, 78, 91))

        self.draw_text("Options menu", pg.font.SysFont("arialblack", 40),
                       (255, 255, 255), 160, 250)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.__window.blit(img, (x, y))
