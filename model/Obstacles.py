import random


class Obstacles:

    def __init__(self, tag):
        pass

    def isDestructable(self):
        return random.choice([True, False])

    