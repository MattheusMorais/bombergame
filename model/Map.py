import random

from model.Obstacles import Obstacles
from model.Player import Player


class Map:

    def __init__(self, gameState):
        self.gameState = gameState
        self.matrix = None
        self.size = 12
        self.player_row, self.player_col = Player.spawn_position
        self.createMap()

    def createMap(self):
        self.matrix = [[" " for _ in range(self.size)] for _ in range(self.size)]

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

            if self.matrix[row][col] == " ":
                if abs(row - self.player_row) + abs(col - self.player_col) >= min_distance_from_border:

                    obstacle = Obstacles(self.gameState)

                    if obstacle.isDestructable():
                        self.matrix[row][col] = "+"
                    else:
                        self.matrix[row][col] = "#"

                    obstacles.append((obstacle, row, col))

        # Put Player in Map
        row, col = Player.spawn_position
        self.matrix[row][col] = "P"

            
        return self.matrix
    
    def getFreePositions(self):
        free_positions = []
        min_distance_from_player = 3

        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell == " ":  
                    if abs(i - self.player_row) + abs(j - self.player_col) >= min_distance_from_player:
                        free_positions.append((i, j))
        return free_positions
    
    def updateCell(self, row, col, symbol):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.matrix[row][col] = symbol
        else:
            print(f"Tentativa de atualizar célula inválida: ({row},{col})")
            

    def printMap(self):
        for linha in self.matrix:
            print(" ".join(linha))
        


        
        


