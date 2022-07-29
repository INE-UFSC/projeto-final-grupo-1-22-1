from pygame.sprite import Group, GroupSingle, spritecollide, collide_rect
from classes.desenhaveis.Obstaculo import Obstaculo
from classes.desenhaveis.Portal import Portal
from classes.desenhaveis.Armadura import Armadura
from classes.desenhaveis.Bau import Bau
from classes.desenhaveis.Jogador import Jogador
from classes.configuracoes.Configuracoes import Configuracoes
from classes.desenhaveis.Inimigo import Inimigo
from classes.mapa.ControladorMovimentos import ControladorMovimentos

class Mapa:
    def __init__(self, layout_mapa: list, surface, largura_mapa, altura_mapa, tamanho_tile) -> None:
        self.__surface_janela = surface
        self.__largura_mapa = largura_mapa
        self.__altura_mapa = altura_mapa
        self.__tamanho_tile = tamanho_tile
        self.__configuracoes = Configuracoes()
        self.__quantidade_baus = 0
        self.preparar_mapa(layout_mapa)
        self.__deslocamento_x = 0
        self.__deslocado_x = 0
        self.__deslocamento_y = 0
    
    def preparar_mapa(self, layout_mapa: list) -> None:
        configs = self.__configuracoes
        self.__grupo_obstaculos = Group()
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
                    obstaculo = Obstaculo((x,y), self.__tamanho_tile)
                    self.__grupo_obstaculos.add(obstaculo)
                elif coluna == 'jogador':
                    self.__jogador = Jogador(configs.vidas_jogador, configs.velocidade_jogador, (x,y), )
                    self.__grupo_jogador.add(self.__jogador)
                    # self.__tiles.add(self.__jogador)
                elif coluna == 'inimigo':
                    self.__inimigo = Inimigo(configs.velocidade_inimigo, (x, y))
                    self.__grupo_inimigo.add(self.__inimigo)
                elif coluna == 'armadura':
                    armadura = Armadura((x,y))
                    self.__grupo_armaduras.add(armadura)
                    # TODO: Ativar e desativar armaduras de tempos em tempos
                elif coluna == 'bau':
                    bau = Bau((x,y))
                    self.__grupo_baus.add(bau)
                    self.__quantidade_baus += 1
                elif coluna == 'portal':
                    portal = Portal((x,y), self.__tamanho_tile)
                    self.__grupo_portais.add(portal)

    @property
    def controlador_movimentos(self):
        return self.__controlador_movimentos

    @property
    def grupo_obstaculos(self) -> list:
        return self.__grupo_obstaculos

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
    def jogador(self) -> Jogador:
        return self.__jogador

    @property
    def quantidade_baus(self):
        return self.__quantidade_baus

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
        self.__grupo_obstaculos.update(self.__deslocamento_x)
        self.__grupo_obstaculos.draw(self.__surface_janela)
        #Armadura
        self.__grupo_armaduras.update(self.__deslocamento_x)
        self.__grupo_armaduras.draw(self.__surface_janela)
        #Bau
        self.__grupo_baus.update(self.__deslocamento_x)
        self.__grupo_baus.draw(self.__surface_janela)
        #Portal
        self.__grupo_portais.update(self.__deslocamento_x)
        self.__grupo_portais.draw(self.__surface_janela)
        self.scroll_x()
        #Jogador
        controlador_movimentos.mover_jogador()
        self.__grupo_jogador.draw(self.__surface_janela)
        # self.horizontal_mov_col()
        #Inimigo
        controlador_movimentos.mover_inimigo()
        self.__grupo_inimigo.draw(self.__surface_janela)
        self.__grupo_inimigo.update(self.__deslocamento_x)