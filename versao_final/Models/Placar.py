from pygame.sprite import Group

class Placar:
  def __init__(self, window_surface, fonte) -> None:
    self.__fonte = fonte
    self.__window = window_surface
    self.__texto_vida = ''
    self.__quantidade_mortes = 0

  def atualizar_vida(self, grupo_jogador: Group) -> None:
    jogador = grupo_jogador.sprite
    self.__texto_vida = self.__fonte.render(
      f'Vida: {jogador.vida}',
      True,
      (255,255,255)
    )
    
    self.__window.blit(self.__texto_vida, (10,3))
