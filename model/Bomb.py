class Bomb:
    """
    Representa uma bomba no mapa do jogo.

    Attributes:
        SYMBOL (str): Símbolo que representa a bomba no mapa.
        row (int): Linha onde a bomba está posicionada.
        col (int): Coluna onde a bomba está posicionada.
        timer (int): Contador de turnos até a explosão.
        range (int): Alcance da explosão da bomba.
    """
   
    SYMBOL = "B"

    def __init__(self, row, col, game_state):
        self.row = row
        self.col = col
        self.timer = game_state.get_bomb_timer()
        self.range = game_state.get_bomb_range()

    def tick(self):
        self.timer -= 1
        return self.timer == 0
            
    def get_explosion_tiles(self):
        tiles = [(self.row, self.col)]

        for i in range(1, self.range + 1):
            tiles.append((self.row + i, self.col))
            tiles.append((self.row - i, self.col))
            tiles.append((self.row, self.col + i))
            tiles.append((self.row, self.col - i))
        
        return tiles
    