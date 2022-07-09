from http.client import CONFLICT
from pathlib import WindowsPath
import pygame as pg
from States.State import Context
from States.MenuPrincipal import MenuPrincipal
import button

class Controlador():
  def __init__(self):
    pg.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    self.__window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Copper Temple - Menus")


    self.__game_paused = True
    self.__menu_state = "main"

    self.__font = pg.font.SysFont("arialblack", 40)

    self.__TEXT_COLLOR = (255, 255, 255)


    icon_img = pg.image.load("images/Icon.png")




    pg.display.set_icon(icon_img)

  def draw_text(self, text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      self.__window.blit(img, (x, y))

  def run(self):
    run = True

    while run:
        tela = Context(MenuPrincipal(self.__window))
       # if self.__game_paused == True:

        # if self.__menu_state == "ranking":
        #     self.__window.fill((52, 78, 91))
        #     self.draw_text("Ranking menu", self.__font, self.__TEXT_COLLOR, 160, 250)

        # if self.__menu_state == "options":
        #     self.__window.fill((52, 78, 91))
        #     self.draw_text("Options menu", self.__font, self.__TEXT_COLLOR, 160, 250)

        # if self.__menu_state == "credits":
        #     self.__window.fill((52, 78, 91))
        #     self.draw_text("Credits menu", self.__font, self.__TEXT_COLLOR, 160, 250)

        #else:
         #   self.draw_text("Press SPACE to pause", self.__font, self.__TEXT_COLLOR, 160, 250)

        for event in pg.event.get():
            if event.type ==pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.__game_paused = True
                if event.key == pg.K_ESCAPE:
                    self.__menu_state = "main"
            if event.type == pg.QUIT:
                run = False
        
        pg.display.update()

    pg.quit()
