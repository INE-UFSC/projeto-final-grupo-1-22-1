from pygame import font

class Vida():
  def __init__(self):
    self.__fonte = font.SysFont('comicsans', 50)
    self.__vida_text = None

  def atualizar_vida(self, qtd_vida, superficie):
    self.__vida_text = self.__fonte.render(
      f'Vida: {qtd_vida}',
      True,
      (255,255,255)
    )
    
    superficie.blit(self.__vida_text, (10,3))