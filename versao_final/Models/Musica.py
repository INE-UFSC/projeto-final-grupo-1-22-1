import pygame
from pygame.locals import *
from pygame import mixer
from Models.Configuracoes import Configuracoes

class Musica:

    def musica_creditos():
        mixer.music.load('Musics/The Oldest Mage(MP3_320K).mp3')

    
    def musica_jogo():
        mixer.music.load('Musics/Skeletoni(MP3_320K).mp3')

    
    def musica_menu():
        mixer.music.load('Musics/An Ugly Heart But It does Beats(MP3_320K).mp3')

    
    def musica_pause():
        mixer.music.load('Musics/A Lonely Cherry Tree --(MP3_320K).mp3')

    def tocar_musica():
        mixer.music.play()

    def alterar_volume(volume: float):
        mixer.music.set_volume(volume)

    def parar_musica(music_state: int):
        if music_state == 1:
            mixer.music.pause()
        else:
            mixer.music.unpause()
