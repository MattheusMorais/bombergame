class Bomb:
   
    SYMBOL = "B"

    def __init__(self, row, col, game_state):
        self.row = row
        self.col = col
        self.timer = game_state.get_bomb_timer()
        self.range = game_state.get_bomb_range()

    def tick(self):
        self.timer -= 1
        if self.timer == 0:
            return True
        
    def get_explosion_tiles(self):
        tiles = [(self.row, self.col)]

        for i in range(1, self.range + 1):
            tiles.append((self.row + i, self.col))
            tiles.append((self.row - i, self.col))
            tiles.append((self.row, self.col + i))
            tiles.append((self.row, self.col - i))
        
        return tiles
    