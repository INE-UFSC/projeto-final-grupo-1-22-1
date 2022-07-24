from pygame.sprite import Group

class Placar:
  def __init__(self, window_surface, fonte) -> None:
    self.__fonte = fonte
    self.__window = window_surface
    self.__texto_vida = ''
    self.__mortes_inimigo = 0
    self.__baus_coletados = 0

  def atualizar_vida(self, grupo_jogador: Group) -> None:
    jogador = grupo_jogador.sprite
    self.__texto_vida = self.__fonte.render(
      f'Vida: {jogador.vida}',
      True,
      (255,255,255)
    )
    
    self.__window.blit(self.__texto_vida, (10,3))
    
  def adicionar_baus(self, novos_baus):
    self.__baus_coletados += novos_baus
        
  def atualizar_baus(self) -> None:
    self.__texto_baus = self.__fonte.render(
      f'Baus coletados: {self.__baus_coletados}',
      True,
      (255,255,255)
    )
    
    self.__window.blit(self.__texto_baus, (10,18))
    
  def incrementar_mortes_inimigo(self):
    self.__mortes_inimigo += 1
        
  def atualizar_mortes_inimigo(self) -> None:
    self.__texto_mortes_inimigo = self.__fonte.render(
      f'Mortes de Inimigo: {self.__mortes_inimigo}',
      True,
      (255,255,255)
    )
    
    self.__window.blit(self.__texto_mortes_inimigo, (10,33))

  def atualizar_tempo(self, tempo) -> None:
    self.__texto_tempo = self.__fonte.render(
      f'Tempo: {tempo}s',
      True,
      (255,255,255)
    )
    
    self.__window.blit(self.__texto_tempo, (10,48))

  @property
  def baus_coletados(self):
    return self.__baus_coletados
