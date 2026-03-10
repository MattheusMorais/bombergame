import random

from model.Helper import clear_screen
from model.Enemy import Enemy
from model.Map import Map
from model.Obstacles import Obstacles
from model.Player import Player
from service.GameState import GameState
from view.GameOver import GameOver
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
        self.enemies_killed = 0

        # Start Menu
        self.start_menu = StartMenu(self.game_state)

        # Creating start Map
        self.start_game_map = Map(self.game_state)

        # Getting free positions on map
        self.free_positions = self.start_game_map.get_free_positions()  # return list of (row, col)

        # Creating player
        self.player_1 = Player(self.game_state)

        # Creating Obstacle
        obstacle = Obstacles(self.game_state)

    def game_loop(self):
        
        print("Warning!! Enemies spawning...")
        # Creating enemies and putting on map
        
        for _ in range(self.initial_number_of_enemies):
            free_position = random.choice(self.free_positions)
            self.free_positions.remove(free_position)
            enemy = Enemy(free_position)
            self.enemies.append(enemy)
            row, col = free_position
            self.start_game_map.update_cell(row, col, enemy.SYMBOL)

        # Print map
        self.start_game_map.print_map()

        while self.player_1.is_alive() and self.game_state.get_game_over_cause() == "None":

            print(f"move: w/a/s/d        "
                  f"put bomb: f        "
                  f"quit: q        "
                  f"bombs utilized: {self.game_state.get_bombs_utilized()}        "
                  f"enemies alive: {self.game_state.get_enemy_quantity()}        "
                  f"survived turns: {self.game_state.get_survived_turns()}        "
                  f"maximum turn: {self.game_state.get_maximum_turn()}        "
                  )
            
            command = input("").lower()

            if command not in ["w", "a", "s", "d", "f", "q"]:
                print("Digite um comando válido!")
                continue

            if command == "q":
                return

            if command in ["w", "a", "s", "d"]:
                self.player_1.move(command, self.start_game_map)
                
            if command == "f":
                self.player_1.put_bomb(command, self.start_game_map)
            
            clear_screen()
            self.update_bombs()
            self.update_enemies()

            if not self.player_1.is_alive():
                break

            if self.game_state.get_survived_turns() == self.game_state.get_maximum_turn():
                self.player_survived()

    def update_bombs(self):
        player_hit = False
        hit_enemies = []

        for bomb in self.player_1.active_bombs[:]:
            if bomb.tick():
                hit_enemies, player_hit = self.start_game_map.chain_explosion(bomb, self.player_1, self.enemies)
                self.player_1.active_bombs.remove(bomb)

        self.start_game_map.print_map()

        for enemy in hit_enemies:
            self.enemies.remove(enemy)
            self.update_enemies_quantity

        if player_hit: # GameOver
            self.player_dead_by_explosion()

    def update_enemies(self):
        
        for enemy in self.enemies:
            if enemy.move(self.start_game_map):
                self.player_killed_by_enemy()
                self.player_1.player_alive = False
        
        self.start_game_map.print_map()

    def player_survived(self):
        if self.game_state.get_survived_turns() == self.game_state.get_maximum_turn():
            self.game_state.set_game_over_cause(GameOver.cause_SUCESS)

            game_over_cause = self.game_state.get_game_over_cause()
            game_over_turn = self.game_state.get_survived_turns()

        GameOver(game_over_cause, game_over_turn)
    
    def player_killed_by_enemy(self):
        self.game_state.set_game_over_cause(GameOver.cause_ENEMY)
        self.game_state.set_game_over_turn(self.game_state.get_survived_turns())
        self.player_1.player_alive = False

        game_over_cause = self.game_state.get_game_over_cause()
        game_over_turn = self.game_state.get_game_over_turn()

        GameOver(game_over_cause, game_over_turn)
    
    def player_dead_by_explosion(self):
        self.game_state.set_game_over_cause(GameOver.cause_EXPLOSION)
        self.game_state.set_game_over_turn(self.game_state.get_survived_turns())
        self.player_1.player_alive = False

        game_over_cause = self.game_state.get_game_over_cause()
        game_over_turn = self.game_state.get_game_over_turn()

        GameOver(game_over_cause, game_over_turn)

    def update_enemies_quantity(self):
        enemies_quantity = self.game_state.get_enemy_quantity()

        for enemy in self.enemies:
            enemies_quantity -= 1
            self.enemies_killed += 1
        
        self.game_state.set_enemy_quantity(enemies_quantity)
    

