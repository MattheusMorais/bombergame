import random

from service.GameState import GameState


class Obstacles:

    DESTR = "+"
    INDESTR = "#"

    def __init__(self, gameState):
        self.gameState = gameState

    def isDestructable(self):
        destructableRate = self.gameState.config["obstacleDestructionRate"]
        randomRate = random.random()
        if randomRate < destructableRate:
            print("Objeto destrutivel gerado")
            return True
        else:
            print("Objeto indestrutivel gerado")
            return False
            
    