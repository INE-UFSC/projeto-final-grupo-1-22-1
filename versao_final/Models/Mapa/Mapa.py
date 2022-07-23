from pygame.sprite import Group, GroupSingle, spritecollide, collide_rect
from Models.Mapa.Tile import Tile
from Models.Mapa.Portal import Portal
from Models.Mapa.Armadura import Armadura
from Models.Mapa.Bau import Bau
from Models.Jogador import Jogador
from Models.Configuracoes import Configuracoes
from Models.Mapa.Inimigo import Inimigo

class Mapa:
    def __init__(self, layout_mapa: list, surface, largura_mapa, altura_mapa, tamanho_tile) -> None:
        self.__surface_janela = surface
        self.__largura_mapa = largura_mapa
        self.__altura_mapa = altura_mapa
        self.__tamanho_tile = tamanho_tile
        self.__configuracoes = Configuracoes()
        self.preparar_mapa(layout_mapa)
        self.__deslocamento_x = 0
        self.__deslocado_x = 0
        self.__deslocamento_y = 0
        self.__deslocado_y = 0
    
    def preparar_mapa(self, layout_mapa: list) -> None:
        self.__tiles = Group()
        self.__grupo_armaduras = Group()
        self.__grupo_baus = Group()
        self.__grupo_portais = Group()
        self.__grupo_jogador = GroupSingle()
        self.__grupo_inimigo = Group()
        for indice_linha,linha in enumerate(layout_mapa):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * self.__tamanho_tile
                y = indice_linha * self.__tamanho_tile
                if coluna == 'parede' or coluna == 'obstaculo':
                    tile = Tile((x,y), self.__tamanho_tile)
                    self.__tiles.add(tile)
                elif coluna == 'jogador':
                    self.__jogador = Jogador(self.__configuracoes.velocidade_jogador, (x,y))
                    self.__grupo_jogador.add(self.__jogador)
                    # self.__tiles.add(self.__jogador)
                elif coluna == 'inimigo':
                    self.__inimigo = Inimigo(self.__configuracoes.velocidade_inimigo, (x, y))
                    self.__grupo_inimigo.add(self.__inimigo)
                elif coluna == 'armadura':
                    armadura = Armadura((x,y))
                    self.__grupo_armaduras.add(armadura)
                    # TODO: Ativar e desativar armaduras de tempos em tempos
                elif coluna == 'bau':
                    bau = Bau((x,y))
                    self.__grupo_baus.add(bau)
                elif coluna == 'portal':
                    portal = Portal((x,y), self.__tamanho_tile)
                    self.__grupo_portais.add(portal)

    @property
    def tiles(self) -> list:
        return self.__tiles

    @property
    def grupo_jogador(self) -> GroupSingle:
        return self.__grupo_jogador
    
    @property
    def grupo_armaduras(self) -> Group:
        return self.__grupo_armaduras    
    
    @property
    def grupo_baus(self) -> Group:
        return self.__grupo_baus

    @property
    def grupo_portais(self) -> Group:
        return self.__grupo_portais

    @property
    def grupo_inimigo(self) -> Group:
        return self.__grupo_inimigo

    @property
    def tiles(self) -> Group:
        return self.__tiles

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    def scroll_x(self):
        jogador = self.__jogador
        x_jogador = jogador.get_centerx()
        direcao_x = jogador.get_dirx()
        direcao_y = jogador.get_diry()
        largura_tela = self.__configuracoes.largura_tela
        y_jogador = jogador.get_centery()
        altura_tela = self.__configuracoes.altura_tela
        
        if x_jogador < (largura_tela / 4) and direcao_x < 0 and self.__deslocado_x < 0:
            self.__deslocamento_x = 3
            self.__deslocado_x += 3
            jogador.velocidade = 0
        elif x_jogador > largura_tela - (largura_tela / 4) and direcao_x > 0 and - (self.__deslocado_x) < self.__largura_mapa - largura_tela:
            self.__deslocamento_x = -(3)
            self.__deslocado_x -= 3
            jogador.velocidade = 0
        else:
            self.__deslocamento_x = 0
            jogador.velocidade = self.__configuracoes.velocidade_jogador


    def run(self, controlador_movimentos) -> None:
        #Mapa
        self.__tiles.update(self.__deslocamento_x, self.__deslocamento_y)
        self.__tiles.draw(self.__surface_janela)
        #Armadura
        self.__grupo_armaduras.update(self.__deslocamento_x, self.__deslocamento_y)
        self.__grupo_armaduras.draw(self.__surface_janela)
        #Bau
        self.__grupo_baus.update(self.__deslocamento_x, self.__deslocamento_y)
        self.__grupo_baus.draw(self.__surface_janela)
        #Portal
        self.__grupo_portais.update(self.__deslocamento_x, self.__deslocamento_y)
        self.__grupo_portais.draw(self.__surface_janela)
        self.scroll_x()
        

        #Jogador
        controlador_movimentos.mover_jogador()
        self.__grupo_jogador.draw(self.__surface_janela)
        self.__grupo_jogador.update(self.__deslocamento_x, self.__deslocamento_y)
        # self.horizontal_mov_col()
        
        #Inimigo
        controlador_movimentos.mover_inimigo()
        self.__grupo_inimigo.draw(self.__surface_janela)
        self.__grupo_inimigo.update(self.__deslocamento_x, self.__deslocamento_y)