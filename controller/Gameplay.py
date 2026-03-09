import random

from model.Enemy import Enemy
from model.Map import Map
from model.Obstacles import Obstacles
from model.Player import Player
from service.GameState import GameState
from view.StartMenu import StartMenu

class Gameplay:

    def __init__(self):
        self.game_state = GameState()
        self.game_state.open()
        self.survivedTurns = self.game_state.config["survivedTurns"]
        self.roundsPlayed = self.game_state.config["roundsPlayed"]
        self.bombsUtilized = self.game_state.config["bombsUtilized"]
        self.initial_number_of_enemies = self.game_state.config["enemyStart"]
        self.enemies = []

    def run(self):
        
        # Start Menu
        start_menu = StartMenu(self.game_state)

        # Creating start Map
        start_game_map = Map(self.game_state)

        # Getting free positions on map
        free_positions = start_game_map.get_free_positions()  # return list of (row, col)

        # Creating player
        player_1 = Player(self.game_state)

        # Creating enemies and putting on map
        
        for enemy in range(self.initial_number_of_enemies):
            free_position = random.choice(free_positions)
            free_positions.remove(free_position)
            enemy = Enemy(free_position)
            self.enemies.append(enemy)
            row, col = free_position
            start_game_map.update_cell(row, col, enemy.SYMBOL)

        # Print map
        start_game_map.print_map()

        # Creating Obstacle
        obstacle = Obstacles(self.game_state)

        # Player move
        player_1.move("d", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("s", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.put_bomb("f", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("d", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("s", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("a", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("a", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()

        player_1.move("a", start_game_map)
        for bomb in player_1.active_bombs[:]:
            if bomb.tick():
                start_game_map.chain_explosion(bomb, player_1, self.enemies)
                player_1.active_bombs.remove(bomb)
        for enemy in self.enemies:
            enemy.move(start_game_map)
        start_game_map.print_map()



