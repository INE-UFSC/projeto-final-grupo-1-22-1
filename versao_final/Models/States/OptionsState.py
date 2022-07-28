import pygame as pg
from Models.States.State import State
from Models.Button import Button
from Models.Configuracoes import Configuracoes


class OptionsState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(transition_to)
        self.__window = window
        self.__configuracoes = Configuracoes()
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__surface = self.__window.surface
        self.__credits_bg_img = pg.transform.scale(
            pg.image.load("Images/OptionsBG.png"), (self.__largura_tela, self.__altura_tela))
        self.__music_off_img = pg.image.load("Images/MusicIconOff.png").convert_alpha()
        self.__music_on_img = pg.image.load("Images/MusicIconOn.png").convert_alpha()
        self.__sound_off_img = pg.image.load("Images/SoundIconOff.png").convert_alpha()
        self.__sound_on_img = pg.image.load("Images/SoundIconOn.png").convert_alpha()
        self.__difficulty_off_img = pg.image.load("Images/DifficultyOff.png").convert_alpha()
        self.__difficulty_on_img = pg.image.load("Images/DifficultyOn.png").convert_alpha()
        
        back_off_img = pg.image.load("Images/BackOff.png").convert_alpha()
        back_on_img = pg.image.load("Images/BackOn.png").convert_alpha()
        self.vol = [pg.image.load("Images/Volume.png"),pg.image.load("Images/Volume (1).png"),pg.image.load("Images/Volume (2).png"),pg.image.load("Images/Volume (3).png")]
        self.dificulty_img = [pg.image.load("Images/Difficulty1.png"), pg.image.load("Images/Difficulty2.png"), pg.image.load("Images/Difficulty3.png")]
        self.music_img = [pg.image.load("Images/MusicOff.png"), pg.image.load("Images/MusicOn.png")]
        self.vol_control = 0
        self.dif_control = 0
        self.music_control = 0

        BUTTONS_SCALE = 1
        SPACE_BEFORE = 20
        SPACE_LEFT = self.__largura_tela * 0.75
        self.__back_button = Button(SPACE_LEFT, SPACE_BEFORE, back_off_img, back_on_img, BUTTONS_SCALE)
        self.__sound_button = Button(100, 230, self.__sound_off_img, self.__sound_on_img, BUTTONS_SCALE)
        self.__music_button = Button(100, 150, self.__music_off_img, self.__music_on_img, BUTTONS_SCALE)
        self.__difficult_button = Button(100, 310, self.__difficulty_off_img, self.__difficulty_on_img, BUTTONS_SCALE)

    def checar_eventos(self):
        self.__back_button.read_events()
        self.__sound_button.read_events()
        self.__music_button.read_events()
        self.__difficult_button.read_events()

        if self.__back_button.clicked:
            self.transicionar("MenuState")

        if self.__sound_button.clicked:
            self.vol_control += 1
            print(self.vol_control)
            if self.vol_control == 1:
                self.vol_control = 0
                print('ta dando bom')

        

    def renderizar(self):
        self.__surface.blit(self.__credits_bg_img, (0, 0))
        self.__surface.blit(self.vol[self.vol_control],(260, 240))
        self.__surface.blit(self.dificulty_img[self.dif_control],(260, 310))
        self.__surface.blit(self.music_img[self.music_control], (260, 150))

        self.checar_eventos()
        self.__back_button.draw(self.__surface)
        self.__sound_button.draw(self.__surface)
        self.__music_button.draw(self.__surface)
        self.__difficult_button.draw(self.__surface)