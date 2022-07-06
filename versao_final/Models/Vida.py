from pygame import font
from Models.Configuracoes import Configuracoes

configuracoes = Configuracoes()

fonte = configuracoes.fonte

class Vida():
  def __init__(self):
    self.__vida_text = None

  def atualizar_vida(self, qtd_vida, superficie):
    self.__vida_text = fonte.render(
      f'Vida: {qtd_vida}',
      True,
      (255,255,255)
    )
    
    superficie.blit(self.__vida_text, (10,3))