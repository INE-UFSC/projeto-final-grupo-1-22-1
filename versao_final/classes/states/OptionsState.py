import pygame as pg
from classes.states.State import State
from classes.componentes.Button import Button
from classes.configuracoes.Configuracoes import Configuracoes
from classes.componentes.Musica import Musica


class OptionsState(State):
    def __init__(self, window, transition_to) -> None:  
        super().__init__(window, transition_to)
        self.__largura_tela = self.configuracoes.largura_tela
        self.__altura_tela = self.configuracoes.altura_tela
        self.__surface = self.window.surface
        self.__credits_bg_img = pg.transform.scale(
            pg.image.load("recursos/imagens/OptionsBG.png"), (self.__largura_tela, self.__altura_tela))
        self.__music_off_img = pg.image.load("recursos/imagens/MusicIconOff.png").convert_alpha()
        self.__music_on_img = pg.image.load("recursos/imagens/MusicIconOn.png").convert_alpha()
        self.__sound_off_img = pg.image.load("recursos/imagens/SoundIconOff.png").convert_alpha()
        self.__sound_on_img = pg.image.load("recursos/imagens/SoundIconOn.png").convert_alpha()
        self.__difficulty_off_img = pg.image.load("recursos/imagens/DifficultyOff.png").convert_alpha()
        self.__difficulty_on_img = pg.image.load("recursos/imagens/DifficultyOn.png").convert_alpha()
        self.__volume = self.configuracoes.vol_control
        self.__musica = self.configuracoes.music_control
        self.__dificuldade = self.configuracoes.dificuldade
        back_off_img = pg.image.load("recursos/imagens/BackOff.png").convert_alpha()
        back_on_img = pg.image.load("recursos/imagens/BackOn.png").convert_alpha()
        self.vol = [pg.image.load("recursos/imagens/Volume (1).png"),pg.image.load("recursos/imagens/Volume (2).png"),pg.image.load("recursos/imagens/Volume (3).png")]
        self.dificulty_img = [pg.image.load("recursos/imagens/Difficulty1.png"), pg.image.load("recursos/imagens/Difficulty2.png"), pg.image.load("recursos/imagens/Difficulty3.png")]
        self.music_img = [pg.image.load("recursos/imagens/MusicOn.png"), pg.image.load("recursos/imagens/MusicOff.png")]
        BUTTONS_SCALE = 1
        SPACE_BEFORE = 20
        SPACE_LEFT = self.__largura_tela * 0.75
        self.__back_button = Button(SPACE_LEFT, SPACE_BEFORE, back_off_img, back_on_img, BUTTONS_SCALE)
        self.__sound_button = Button(100, 230, self.__sound_off_img, self.__sound_on_img, BUTTONS_SCALE)
        self.__music_button = Button(100, 150, self.__music_off_img, self.__music_on_img, BUTTONS_SCALE)
        self.__difficult_button = Button(100, 310, self.__difficulty_off_img, self.__difficulty_on_img, BUTTONS_SCALE)

    def renderizar(self) -> None:
        self.checar_eventos()
        self.__surface.blit(self.__credits_bg_img, (0, 0))
        self.__surface.blit(self.vol[self.__volume],(260, 240))
        self.__surface.blit(self.dificulty_img[self.__dificuldade],(260, 310))
        self.__surface.blit(self.music_img[self.__musica], (260, 150))
        self.__back_button.draw(self.__surface)
        self.__sound_button.draw(self.__surface)
        self.__music_button.draw(self.__surface)
        self.__difficult_button.draw(self.__surface)
    
    def checar_eventos(self) -> None:
        self.__back_button.read_events()
        self.__sound_button.read_events()
        self.__music_button.read_events()
        self.__difficult_button.read_events()

        if self.__back_button.clicked:
            self.transicionar("MenuState")

        if self.__sound_button.clicked:
            self.__volume += 1
            if self.__volume > 2:
                self.__volume = 0
            self.configuracoes.vol_control = self.__volume
            if self.__volume == 0:
                Musica.alterar_volume(0.1)
            elif self.__volume == 1:
                Musica.alterar_volume(0.5)
            elif self.__volume == 2:
                Musica.alterar_volume(1)

        if self.__music_button.clicked:
            self.__musica += 1
            if self.__musica > 1:
                self.__musica = 0
            self.configuracoes.music_control = self.__musica
            Musica.parar_musica(self.configuracoes.music_control)

        if self.__difficult_button.clicked:
            self.__dificuldade += 1
            if self.__dificuldade > 2:
                self.__dificuldade = 0
            self.configuracoes.dificuldade = self.__dificuldade
