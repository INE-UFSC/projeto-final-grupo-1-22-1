"""
    TODO: Seria interessante se o State pudesse visualizar 
    o método transition_to sem precisar ser passado como parâmetro: 
    através de uma ligação direta com o controlador.
"""
class State():
    def __init__(self, transition_to):
        self.__transition_to = transition_to

    def transicionar(self, next_state):
        self.__transition_to(next_state)
