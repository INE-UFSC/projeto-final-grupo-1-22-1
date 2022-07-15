import pygame as pg
from States.MenuPrincipal import MenuPrincipal
from States.Jogo import Jogo
from States.Creditos import Creditos
from States.Options import Options
from States.Ranking import Ranking

STATES = {
    "MenuPrincipal": MenuPrincipal,
    "Jogo": Jogo,
    "Creditos": Creditos,
    "Options": Options,
    "Ranking": Ranking
}


class Controlador():
    def __init__(self):
        pg.init()

        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480

        self.__window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Copper Temple - Menus")

        self.__state = "MenuPrincipal"

        icon_img = pg.image.load("images/Icon.png")

        pg.display.set_icon(icon_img)

    def transition_to(self, new_state):
        if self.__state != new_state:
            print(f"Context: Transition to {new_state}")
            self.__state = new_state

    def run(self):
        run = True

        while run:
            if self.__state in STATES:
                tela = STATES[self.__state](self.__window, self.transition_to)
            else:
                tela = MenuPrincipal(self.__window, self.transition_to)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        tela.transicionar("MenuPrincipal")
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()

        pg.quit()
