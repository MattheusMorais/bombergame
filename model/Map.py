import random
from model.Enemy import Enemy
from model.Obstacles import Obstacles
from model.Player import Player

class Map:

    EMPTY = " "

    def __init__(self, game_state):
        self.game_state = game_state
        self.matrix = None
        self.size = 12
        self.player_row, self.player_col = Player.spawn_position
        self.enemy_start = game_state.config["enemyStart"]
        self.enemy_quantity = game_state.config["enemyQuantity"]
        self.create_map()

    def create_map(self):
        self.matrix = [[self.EMPTY for _ in range(self.size)] for _ in range(self.size)]

        # Create external walls to delimit player Map
        for i in range(self.size):
            for j in range(self.size):
                if i==0 or i== self.size-1 or j == 0 or j == self.size-1:
                    self.matrix[i][j] = Obstacles.INDESTR
    
        # Create obstacles in Map
        obstacles = []
        num_obstacles = 3
        min_distance_from_border = 3

        while len(obstacles) < num_obstacles:
            row = random.randint(1, self.size - 2)  
            col = random.randint(1, self.size - 2)

            if self.matrix[row][col] == self.EMPTY:
                if abs(row - self.player_row) + abs(col - self.player_col) >= min_distance_from_border:

                    obstacle = Obstacles(self.game_state)

                    if obstacle.is_destructable():
                        self.matrix[row][col] = Obstacles.DESTR
                    else:
                        self.matrix[row][col] = Obstacles.INDESTR

                    obstacles.append((obstacle, row, col))

        # Put Player in Map
        row, col = Player.spawn_position
        self.matrix[row][col] = Player.SYMBOL

        return self.matrix
    
    def get_free_positions(self):
        free_positions = []
        min_distance_from_player = 3

        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell == self.EMPTY:  
                    if abs(i - self.player_row) + abs(j - self.player_col) >= min_distance_from_player:
                        free_positions.append((i, j))
        return free_positions
    
    def update_cell(self, row, col, symbol):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.matrix[row][col] = symbol
        else:
            print(f"Tentativa de atualizar célula inválida: ({row},{col})")
            
    def chain_explosion(self, bomb, player_1, enemies):
        explosion_tiles = bomb.get_explosion_tiles()

        for row, col in explosion_tiles:
            cell = self.matrix[row][col]

            if cell == Obstacles.INDESTR:
                continue
        
            self.update_cell(row, col, "*")

            if cell == Obstacles.DESTR:
                self.update_cell(row, col, " ")

            if cell == Enemy.SYMBOL:
                self.update_cell(row, col, " ")

            # for enemy in self.enemies:
            #     if enemy.current_position == (row, col):
            #         enemy.die()

            # if player_1.current_position == (row, col):
            #     player_1.die()
  
    def print_map(self):
        for row in self.matrix:
            print(self.EMPTY.join(row))
        