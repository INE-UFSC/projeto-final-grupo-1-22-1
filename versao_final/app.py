
import pygame as pg
from pygame.locals import *
from sys import exit
from pygame import font

from pygame.sprite import Group, GroupSingle

from Models.Desenhavel import Desenhavel
from Models.LeitorEventos import LeitorEventos
from Models.Controlador import Controlador
from Models.Obstaculo import Obstaculo
from Models.Inimigo import Inimigo
from Models.SpriteObstaculo import SpriteObstaculo
from Models.Vida import Vida

from Models.Window import Window
from Models.TelaCreditos import TelaCreditos
from Models.TelaMenu import TelaMenu

from Models.Configuracoes import Configuracoes
from Models.Mapa.Mapa import Mapa
configuracoes = Configuracoes()
fonte = configuracoes.fonte
width = configuracoes.largura_tela
height = configuracoes.altura_tela
window = Window((width, height), "Cooper Temple - Alfa")
window_surface = window.surface
wall_size = 30

timer = pg.time.Clock()



pg.init()



inimigo = Inimigo()



grupo_obstaculos = Group(SpriteObstaculo(width/4, height/4),
                         SpriteObstaculo(width*3/4, height/4),
                         SpriteObstaculo(width/4, height*3/4),
                         SpriteObstaculo(width*3/4, height*3/4))

grupo_inimigos = GroupSingle(inimigo)



leitor_eventos = LeitorEventos()
mapa = Mapa(configuracoes.mapa, window_surface, leitor_eventos)
controlador = Controlador(mapa, inimigo, grupo_obstaculos, grupo_inimigos)


#Na entrega final, essa lógica estará implementada usando OO

def draw_luz():
    points = [(width*7/15, height*10/12), (width*8/15, height*10/12), (width*5/8,30), (width*3/8,30)]
    pg.draw.polygon(window_surface, (174, 207, 136), points)

def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

menu_principal = TelaMenu(leitor_eventos, window, fonte)

def main_menu():
    while True:
        escolha = menu_principal.renderizar_tela()
        # window_surface.fill((54,107,95))
        # draw_text('main menu', fonte, (255, 255, 255), window_surface, (width/2)-100, 20)
 
        # mx, my = pg.mouse.get_pos()
 
        # button_1 = pg.Rect((width/2)-100, 100, 200, 50)
        # button_2 = pg.Rect((width/2)-100, 200, 200, 50)
        # if button_1.collidepoint((mx, my)):
        #     if click:
        #         #Chamada do jogo
        #         game()
        # if button_2.collidepoint((mx, my)):
        #     if click:
        #         #chamada da segunda tela
        #         tela_creditos = TelaCreditos(leitor_eventos, window, fonte)
        #         tela_creditos.renderizar_tela()
        # pg.draw.rect(window_surface, (137, 199, 185), button_1)
        # pg.draw.rect(window_surface, (137, 199, 185), button_2)

        if escolha == 'OPCAO1':
            game()
        elif escolha == 'OPCAO2':
            tela_creditos = TelaCreditos(leitor_eventos, window, fonte)
            tela_creditos.renderizar_tela()
        
        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                window.fechar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window.fechar()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pg.display.update()
        timer.tick(60)
    

def draw_cenario(size, width, height):
        door = 40
        #Desenho de retangulos, que recebe "window" = tela em que vai ser desenhado, (45,84,60) = Cor em RGB, [] = coordenadas dos pontos da diagonal principal, 0 = Tamanho da borda do retangulo
        pg.draw.rect(window_surface, (45, 84, 60),[0, 0, width-size, size], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[width-size, 0, width, height/5], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[width-size, (height/5)+door , width, (height*(4/5))-(door+size)], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[size, height-size, width, height], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[0, size, size, height-size], 0)

def game():

    while True:
        timer.tick(60)

        controlador.mover_inimigo()
        controlador.morte_jogador()

        # for event in pg.event.get():
        #     if event.type == QUIT:
        #         pg.quit()
        #         exit()

    #Chamada dos desenhos
        #Define a cor da tela no padrão RGB
        window_surface.fill((54,107,95))
        mapa.run()

        luz = draw_luz()

        #Desenhando os grupos a cada ciclo de clock
        grupo_obstaculos.draw(window_surface)
        grupo_inimigos.draw(window_surface)


        controlador.mover_jogador()

        grupo_obstaculos.update()

        draw_cenario(30,width, height)

        controlador.atualizar_vida(window_surface)

        pg.display.flip() #Precisa estar no final do algoritmo

main_menu()