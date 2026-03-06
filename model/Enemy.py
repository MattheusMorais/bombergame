import random

class Enemy:

    def __init__(self):
        pass

    def isBlocked(self, position):
        if (position == "+" or position == "#"):
            return True
        else:
            return False

    def move(self, position):
        if isBlocked(position):
            print("Can't move, position is blocked")
        
        if (position == "P"):
            print("Enemy killed Played. Game Over...")
        else:
            pass
        

    