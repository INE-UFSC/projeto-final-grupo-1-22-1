from abc import ABC, abstractmethod
from classes.configuracoes.Configuracoes import Configuracoes
from classes.componentes.Window import Window

class State(ABC):
    def __init__(self, window: Window, transition_to) -> None:
        self.configuracoes = Configuracoes()
        self.__transition_to = transition_to
        self.window = window

    def transicionar(self, next_state: str) -> None:
        self.__transition_to(next_state)

    @abstractmethod
    def renderizar(self) -> None:
        pass
