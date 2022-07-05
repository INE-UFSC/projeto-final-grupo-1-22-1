from DAO import DAO
#from Cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo_pontuacao: Pontuacao):
        if isinstance(cliente.codigo, int) and isinstance(cliente, Cliente):
            super().add(jogo_pontuacao)
        else:
            print('Não foi')