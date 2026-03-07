import random

class Enemy:

    SYMBOL = "E"

    directions = {
        "w" : (-1,0),
        "a" : (0,-1),
        "s" : (1,0),
        "d" : (0,1)
        }

    def __init__(self, position):
        self.position = position

    def isBlocked(self):
        row, col = self.position
        if self.gameMap[row][col] == "+" or self.gameMap[row][col] == "#":
            return True
        else:
            return False

    def move(self):
        pairs = list(self.directions.values())
        row, col = random.choice(pairs)

        if self.isBlocked(self.position):
            print("Can't move, position is blocked")
        
        if (self.position == "P"):
            print("Enemy killed Played. Game Over...")
        else:
            pass
        

    