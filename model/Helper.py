import os

PLAYER_SYMBOL = "P"
ENEMY_SYMBOL = "E"
BOMB_SYMBOL = "B"
OBSTACLE_DESTR = "+"
OBSTACLE_INDESTR = "#"
MAP_EMPTY = " "

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
    """
    Limpa a tela do terminal.

    Usa 'cls' no Windows e 'clear' em sistemas Unix-like.
    """
