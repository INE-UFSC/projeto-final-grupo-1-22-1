from cgitb import text
import pygame as pg
from Models.States.State import State
from Models.Button import Button
from Models.Configuracoes import Configuracoes
from Models.Persistencia.JogoDAO import JogoDAO


class RankingState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__window = window
        self.__configuracoes = Configuracoes()
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__surface = self.__window.surface
        self.__credits_bg_img = pg.transform.scale(
            pg.image.load("Images/RankingBG.png"), (self.__largura_tela, self.__altura_tela))
        self.__pg_font = pg.font.SysFont('arial',  30)
        
        back_off_img = pg.image.load("Images/BackRankingOff.png").convert_alpha()
        back_on_img = pg.image.load("Images/BackRankingOn.png").convert_alpha()

        BUTTONS_SCALE = 1
        SPACE_BEFORE = 20
        SPACE_LEFT = self.__largura_tela * 0.75
        self.__back_button = Button(
            SPACE_LEFT, SPACE_BEFORE, back_off_img, back_on_img, BUTTONS_SCALE)

        self.__jogo_dao = JogoDAO()

    def checar_eventos(self):
        self.__back_button.read_events()

        if self.__back_button.clicked:
            self.transicionar("MenuState")

    def renderizar(self):
        self.__surface.blit(self.__credits_bg_img, (0, 0))
        texto_pricipal = self.__pg_font.render(f'Pontos      Inimigos Mortos       Data', False, (255, 255, 255))

        self.__surface.blit(texto_pricipal, (60, 15))
        arq_pickle = self.__jogo_dao.get_all()
        tam = 50
        lista = []
        for i in arq_pickle:
            lista.append([i.baus, i.mortes, i.data])
        
        lista.sort()
        lista.reverse()
        for i in lista[:10]:
            linha = self.__pg_font.render(f'{i[0]}                {i[1]}        {i[2]}', False, (255, 255, 255))
            self.__surface.blit(linha, (90, tam))
            linha = self.__pg_font.render("---------------------------------------------------------------", False, (255, 255, 255))
            self.__surface.blit(linha, (30, tam+20))
            tam += 50

        self.checar_eventos()
        self.__back_button.draw(self.__surface)