import random

class Obstacles:

    DESTR = "+"
    INDESTR = "#"

    def __init__(self, game_state):
        self.game_state = game_state

    def is_destructable(self):
        destructable_rate = self.game_state.config["obstacleDestructionRate"]
        random_rate = random.random()
        if random_rate < destructable_rate:
            return True
        else:
            return False
            