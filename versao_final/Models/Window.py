import pygame as pg
import sys


#Classe que usa as funcionalidades do pygame
class Window:
  def __init__(self, size: tuple, caption: str, flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0):
    self.__surface = pg.display.set_mode(size=size,
                                         flags=0,
                                         depth=0,
                                         display=0,
                                         #tira sincronização do tipo raster
                                         vsync=0)
    self.__size = size
    self.__caption = caption
    pg.display.set_caption(caption)

  @property
  def size(self):
    return self.__size

  @property
  def surface(self):
    return self.__surface
  
  @property
  def window(self):
    return self.__window

  def set_caption(self, caption):
    pg.display.set_caption(caption)

  def fechar(self):
    pg.quit()
    sys.exit()

  def update(self):
    pg.display.update()

  