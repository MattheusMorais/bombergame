import random
from model.Helper import ENEMY_SYMBOL
from model.Obstacles import Obstacles
from model.Player import Player
from model.Bomb import Bomb

class Map:

    EMPTY = " "

    def __init__(self, game_state):
        self.game_state = game_state
        self.matrix = None
        self.size = 12
        self.player_row, self.player_col = Player.spawn_position
        self.initial_number_of_enemies = game_state.get_enemy_start()
        self.enemy_quantity = game_state.get_enemy_quantity()
        self.obstacles = []
        self.num_obstacles = 3
        self.min_distance_from_border = 3
        self.create_map()

    def create_map(self):
        self.matrix = [[self.EMPTY for _ in range(self.size)] for _ in range(self.size)]

        # Create external walls to delimit player Map
        for i in range(self.size):
            for j in range(self.size):
                if i==0 or i== self.size-1 or j == 0 or j == self.size-1:
                    self.matrix[i][j] = Obstacles.INDESTR
    
        # Create obstacles in Map
        while len(self.obstacles) < self.num_obstacles:
            row = random.randint(1, self.size - 2)  
            col = random.randint(1, self.size - 2)

            if self.matrix[row][col] == self.EMPTY:
                if abs(row - self.player_row) + abs(col - self.player_col) >= self.min_distance_from_border:

                    obstacle = Obstacles(self.game_state)

                    if obstacle.is_destructable():
                        self.matrix[row][col] = Obstacles.DESTR
                    else:
                        self.matrix[row][col] = Obstacles.INDESTR

                    self.obstacles.append((obstacle, row, col))

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
    
    def is_index_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
            
    def update_cell(self, row, col, symbol):
        if self.is_index_valid(row, col):
            self.matrix[row][col] = symbol
        else:
            print(f"Tentativa de atualizar célula inválida: ({row},{col})")
            
    def chain_explosion(self, bomb, player_1, enemies):
        explosion_tiles = bomb.get_explosion_tiles()
        original_cells = {}

        for row, col in explosion_tiles:
            if not self.is_index_valid(row, col):
                continue

            cell = self.matrix[row][col]

            if cell == Obstacles.INDESTR:
                continue
                
            original_cells[(row, col)] = cell
            self.update_cell(row, col, "*")

        self.print_map()

        hit_enemies = []
        player_hit = False
        for (row, col), original_cell in original_cells.items():
            if original_cell == Obstacles.DESTR:
                self.update_cell(row, col, self.EMPTY)
            elif original_cell == ENEMY_SYMBOL or original_cell == Player.SYMBOL:
                self.update_cell(row, col, self.EMPTY)
            elif original_cell == Bomb.SYMBOL:
                self.update_cell(row, col, self.EMPTY)
            else:
                self.update_cell(row, col, original_cell)
        
            for enemy in enemies:
                if enemy.current_position == (row, col):
                    hit_enemies.append(enemy)

            if player_1.current_position == (row, col):
                player_hit = True

        return hit_enemies, player_hit
    
    def print_map(self):
        for row in self.matrix:
            print(self.EMPTY.join(row))
        