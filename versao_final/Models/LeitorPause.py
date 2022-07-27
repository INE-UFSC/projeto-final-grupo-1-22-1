from abc import ABC, abstractmethod
from abc import abstractclassmethod
from Models.LeitorEventos import LeitorEventos

# evento = LeitorEventos()
# game_paused = False

class LeitorPause():
    def __init__(self):
        self.evento = LeitorEventos()
        self.game_paused = False

    # @abstractclassmethod
    def paused(self) -> bool:
        # print('Classe pause')
        return self.game_paused
        # if evento.ler_evento() == 'Paused':
        #     print('Pausado')
        #     return not pause_state
        # else:
        #     print('Velho')
        #     return pause_state

    # @abstractclassmethod
    def detect(self) -> bool:
        self.game_paused = not self.game_paused