from abc import ABC, abstractmethod
from abc import abstractclassmethod
from Models.LeitorEventos import LeitorEventos

evento = LeitorEventos()

class LeitorPause():
    def __init__(self):
        pass

    @abstractclassmethod
    def paused(cls, pause_state: bool):
        #print('Classe pause')
        if evento.ler_evento() == 'Paused':
            print('Pausado')
            return not pause_state
        else:
            #print('Velho')
            return pause_state