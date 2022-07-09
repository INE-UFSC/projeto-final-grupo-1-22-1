from States.State import State
import pygame as pg
from States.Creditos import Creditos
import button

class MenuPrincipal(State):
    def __init__(self, window):
        self.__window = window
        self.__menu_bg_img = pg.image.load("images/MainMenu.png")
        self.__title = pg.image.load("images/Titulo.png")
        play_off_img = pg.image.load("images/PlayOff.png").convert_alpha()
        play_on_img = pg.image.load("images/PlayOn.png").convert_alpha()
        ranking_off_img = pg.image.load("images/RankingOff.png").convert_alpha()
        ranking_on_img = pg.image.load("images/RankingOn.png").convert_alpha()
        options_off_img = pg.image.load("images/OptionsOff.png").convert_alpha()
        options_on_img = pg.image.load("images/OptionsOn.png").convert_alpha()
        credits_off_img = pg.image.load("images/CreditsOff.png").convert_alpha()
        credits_on_img = pg.image.load("images/CreditsOn.png").convert_alpha()
        self.__play_button = button.Button(40, 20, play_off_img, play_on_img, 1)
        self.__ranking_button = button.Button(40, 140, ranking_off_img, ranking_on_img, 1)
        self.__options_button = button.Button(40, 255, options_off_img, options_on_img, 1)
        self.__credits_button = button.Button(40, 370, credits_off_img,credits_on_img, 1)

        self.__window.blit(self.__menu_bg_img, (0,0))

        if self.__menu_state == "main":
                self.__window.blit(self.__title, (280,235))
                if self.__play_button.draw(self.__window):
                    self.__game_paused = False
                if self.__ranking_button.draw(self.__window):
                    self.__menu_state = "ranking"
                if self.__options_button.draw(self.__window):
                    self.__menu_state = "options"
                if self.__credits_button.draw(self.__window):
                    self.__menu_state = "credits"

    def clique_em_creditos(self):
        self.context.transition_to(Creditos())
        print("Muda de estado para a tela de Creditos.")

    def transicionar(self) -> None:
         return super().transicionar()

    def renderizar(self) -> None:
         return super().renderizar()


# if __name__ == "__main__":
#     # The client code.

#     context = Context(ConcreteStateA())
#     context.request1()
#     context.request2()
