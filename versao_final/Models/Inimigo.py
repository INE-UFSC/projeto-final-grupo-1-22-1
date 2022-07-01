from Models.Desenhavel import Desenhavel
from random import randint

class Inimigo(Desenhavel):
  def __init__(self):
    super().__init__('Images/Cientista.png', 640, randint(20,580))
  
