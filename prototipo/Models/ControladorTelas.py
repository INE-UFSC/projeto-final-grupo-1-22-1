from Models.Tela import Tela

class ControladorTelas:
    def __init__(self, tela_menu: Tela, tela_creditos: Tela): #tela_game_over, tela_pause
        self.tela_menu = tela_menu
        self.tela_creditos = tela_creditos