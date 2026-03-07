from model.Bomb import Bomb

class Player:

    SYMBOL = "P"

    directions = {
        "w" : (-1,0),
        "a" : (0,-1),
        "s" : (1,0),
        "d" : (0,1)
    }

    spawn_position = (1,1)

    def __init__(self):
        pass

    def move(self, command, gamemap):
        pass

    def putBomb(self, gamemap):
        bomb = Bomb()
        pass

    def is_walkable(self, gamemap):
        pass
        
