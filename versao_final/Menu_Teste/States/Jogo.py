import pygame as pg


class Jogo:
    def __init__(self, window, controlador) -> None:
        self.__window = window
        self.__controlador = controlador
        self.__window.fill((52, 78, 91))

        self.draw_text("Jogo menu", pg.font.SysFont("arialblack", 40),
                       (255, 255, 255), 160, 250)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.__window.blit(img, (x, y))

    def renderizar(self, next_state):
        self.context.transition_to(next_state(
            self.__window, self.__controlador))
