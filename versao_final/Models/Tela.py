from abc import ABC, abstractmethod
from pygame import font

from Models.LeitorEventos import LeitorEventos
from Models.Window import Window

font.init()
fonte = font.SysFont('comicsans', 50)

class Tela(ABC):
  def __init__(self, leitor_eventos: LeitorEventos, window: Window, fonte = fonte) -> None:
    self.__leitor_eventos = leitor_eventos
    self.__window = window
    self.__fonte = fonte
  
  @property
  def leitor_eventos(self):
    return self.__leitor_eventos
    
  @property
  def window(self):
    return self.__window
  
  @property
  def fonte(self):
    return self.__fonte
  
  @abstractmethod
  def renderizar_tela():
    pass

  def renderizar_texto(self, text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)