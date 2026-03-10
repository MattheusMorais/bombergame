from model.Bomb import Bomb
from model.Helper import MAP_EMPTY, ENEMY_SYMBOL, OBSTACLE_DESTR, OBSTACLE_INDESTR

class Player:

    SYMBOL = "P"
    spawn_position = (1,1)
    directions = {
        "w" : (-1,0),
        "a" : (0,-1),
        "s" : (1,0),
        "d" : (0,1)
    }

    def __init__(self, game_state):
        self.active_bombs = []
        self.current_position = self.spawn_position
        self.game_state = game_state
        self.player_alive = True
        
    def move(self, command, game_map):

            if self.is_blocked(command, game_map):
                print("Caminho bloqueado")
                return
            
            if command in self.directions:
                old_row, old_col = self.current_position
                drow, dcol = self.directions[command]

                new_row = old_row + drow
                new_col = old_col + dcol

                if game_map.matrix[old_row][old_col] == Bomb.SYMBOL:
                    game_map.update_cell(old_row, old_col, Bomb.SYMBOL)
                else:
                    game_map.update_cell(old_row, old_col, MAP_EMPTY)

                if game_map.matrix[new_row][new_col] == Bomb.SYMBOL:
                    game_map.update_cell(new_row, new_col, Bomb.SYMBOL)
                else:
                    game_map.update_cell(new_row, new_col, Player.SYMBOL)

                self.current_position = (new_row, new_col)

                survived_turns = self.game_state.get_survived_turns()

                self.game_state.set_survived_turns(survived_turns+1)
                game_map.print_map()
            
    def put_bomb(self, command, gamemap):
        if command == 'f':
            row, col = self.current_position

            gamemap.update_cell(row, col, Bomb.SYMBOL)

            bomb = Bomb(row, col, self.game_state)
            self.active_bombs.append(bomb)

            bombs_utilized = self.game_state.get_bombs_utilized()
            self.game_state.set_bombs_utilized(bombs_utilized+1)
        
    def is_blocked(self, command, game_map):
        row, col = self.current_position

        if command in self.directions:
            drow, dcol = self.directions[command]

            new_row = row + drow
            new_col = col + dcol

            cell = game_map.matrix[new_row][new_col]

            if cell == OBSTACLE_DESTR or cell == OBSTACLE_INDESTR or cell == ENEMY_SYMBOL:
                print("Player cant move, blocked")
                return True
            
        return False
    
    def is_alive(self):
        if self.player_alive == True:
            return True
        return False
    