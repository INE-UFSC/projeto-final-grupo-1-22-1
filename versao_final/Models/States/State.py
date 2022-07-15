from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, transition_to):
        self.__transition_to = transition_to

    def transicionar(self, next_state):
        self.__transition_to(next_state)

    @abstractmethod
    def renderizar(self):
        pass
