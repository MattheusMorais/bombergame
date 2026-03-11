import random

class Obstacles:
    """
    Representa os obstáculos do jogo, que podem ser destrutíveis ou indestrutíveis.

    Attributes:
        DESTR (str): Símbolo usado para definir obstáculos destrutíveis.
        INDESTR (str): Símbolo usado para definir obstáculos indestrutíveis.
        game_state: Objeto que mantém o estado atual do jogo, incluindo taxa de destruição.
        destructable_rate (float): Probabilidade de um obstáculo ser destrutível.
    """

    DESTR = "+"
    INDESTR = "#"

    def __init__(self, game_state):
        self.game_state = game_state
        self.destructable_rate = self.game_state.get_obstacle_destruction_rate()

    def is_destructable(self):
        random_rate = random.random()
        return True if random_rate < self.destructable_rate else False
            