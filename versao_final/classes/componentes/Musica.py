import pygame
from pygame.locals import *
from pygame import mixer
from classes.configuracoes.Configuracoes import Configuracoes

class Musica:

    def musica_jogo():
        mixer.music.load('recursos/musicas/An Ugly Heart But It does Beats(MP3_320K).mp3')

    def tocar_musica():
        mixer.music.play()

    def alterar_volume(volume: float):
        mixer.music.set_volume(volume)

    def parar_musica(music_state: int):
        if music_state == 1:
            mixer.music.pause()
        else:
            mixer.music.unpause()
