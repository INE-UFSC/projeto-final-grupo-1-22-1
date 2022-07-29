
from classes.desenhaveis.Desenhavel import Desenhavel


class Armadura(Desenhavel):
    def __init__(self, position):
        super().__init__("recursos/imagens/ArmaduraOff.png", position)
        
