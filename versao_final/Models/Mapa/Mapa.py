from pygame.sprite import Sprite, Group, GroupSingle
from Models.Mapa.Tile import Tile
from Models.Jogador import Jogador
from Models.Configuracoes import Configuracoes


class Mapa:
    def __init__(self, layout_mapa, surface) -> None:
        self.__surface_janela = surface
        self.__configuracoes = Configuracoes()
        self.preparar_mapa(layout_mapa)
        self.__deslocamento = 0
    
    def preparar_mapa(self, layout_mapa: list) -> None:
        self.__tiles = Group()
        self.__grupo_jogador = GroupSingle()
        #FAZER A INSTÂNCIA DO JOGADOR AQUI
        for indice_linha,linha in enumerate(layout_mapa):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * self.__configuracoes.tamanho_tile
                y = indice_linha * self.__configuracoes.tamanho_tile
                if coluna == 'X':
                    tile = Tile((x,y), self.__configuracoes.tamanho_tile)
                    self.__tiles.add(tile)
                if coluna == 'P':
                    self.__jogador = Jogador((x,y))
                    self.__tiles.add(self.__jogador)

    @property
    def grupo_jogador(self) -> GroupSingle:
        return self.__grupo_jogador

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    def run(self) -> None:
        self.__tiles.update(self.__deslocamento)
        self.__tiles.draw(self.__surface_janela)
        self.__grupo_jogador.draw(self.__surface_janela)