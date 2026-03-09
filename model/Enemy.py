import random
from model.Obstacles import Obstacles
from model.Bomb import Bomb

class Enemy:

    SYMBOL = "E"
    directions = {
        "w" : (-1,0),
        "a" : (0,-1),
        "s" : (1,0),
        "d" : (0,1)
        }

    def __init__(self, current_position):
        self.current_position = current_position

    def is_blocked(self, new_row, new_col, game_map):
        cell = game_map.matrix[new_row][new_col]
        if cell == Obstacles.DESTR or cell == Obstacles.INDESTR or cell == Bomb.SYMBOL or cell == Enemy.SYMBOL:
            return True
            
        return False

    def move(self, game_map):
        from model.Map import Map

        old_row, old_col = self.current_position

        row, col = random.choice(list(self.directions.values()))

        new_row = old_row + row
        new_col = old_col + col

        if self.is_blocked(new_row, new_col, game_map):
            print("Can't move ENEMY, position is blocked")
            return

        if (game_map.matrix[new_row][new_col] == "P"):
            print("Enemy killed Played. Game Over...")
            return
        
        if game_map.matrix[old_row][old_col] == Enemy.SYMBOL:
            game_map.update_cell(old_row, old_col, Map.EMPTY)

        game_map.update_cell(new_row, new_col, Enemy.SYMBOL)

        self.current_position = (new_row, new_col)

    