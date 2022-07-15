import pygame as pg
from States.State import Context
from States.MenuPrincipal import MenuPrincipal
from States.Jogo import Jogo
from States.Creditos import Creditos
from States.Options import Options
from States.Ranking import Ranking

STATES = {
    "main": MenuPrincipal,
    "jogo": Jogo,
    "credits": Creditos,
    "options": Options,
    "ranking": Ranking
}


class Controlador():
    def __init__(self):
        pg.init()

        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480

        self.__window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Copper Temple - Menus")

        # self.__game_paused = True
        self.__state = "main"

        icon_img = pg.image.load("images/Icon.png")

        pg.display.set_icon(icon_img)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state) -> None:
        self.__state = state

    def run(self):
        run = True

        tela = Context(MenuPrincipal(self.__window, self))

        while run:
            if self.__state in STATES:
                tela.renderizar(STATES[self.__state])

            # else:
            #   self.draw_text("Press SPACE to pause", self.__font, self.__TEXT_COLLOR, 160, 250)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_SPACE:
                    #     self.__game_paused = True
                    if event.key == pg.K_ESCAPE:
                        self.__state = "main"
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()

        pg.quit()
