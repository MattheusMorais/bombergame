import random
import os

from model.Enemy import Enemy
from model.Map import Map
from model.Obstacles import Obstacles
from model.Player import Player
from service.GameState import GameState
from view.StartMenu import StartMenu

class Gameplay:

    def __init__(self):
        pass

    def run(self):
        # Creating GameState

        gameState = GameState()
        gameState.open()

        # Start Menu
        # start_menu = StartMenu(gameState)

        # Creating start Map
        start_game_map = Map(gameState)

        # Getting free positions on map
        free_positions = start_game_map.getFreePositions()  # return list of (row, col)

        # Creating player
        player1 = Player()

        # Creating enemies and putting on map
        enemies = []
        initial_number_of_enemies = gameState.config["enemyStart"]

        for enemy in range(initial_number_of_enemies):
            free_position = random.choice(free_positions)
            free_positions.remove(free_position)
            enemy = Enemy(free_position)
            enemies.append(enemy)
            row, col = free_position
            start_game_map.updateCell(row, col, enemy.SYMBOL)

        # Print map
        start_game_map.printMap()

        # Creating Obstacle
        obstacle = Obstacles(gameState)

