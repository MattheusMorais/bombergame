import json

class GameState:

    def __init__(self, config_path = "config/gameConfig.json"):
        self.config_path = config_path
        self.config = {}

        # default values case JSON fail
        self.rounds_played = 1
        self.survived_turns = 1
        self.bombs_utilized =  0
        self.game_over_cause = "None"
        self.game_over_turn = 0
        self.maximum_turn = 11
        self.bomb_range = 2
        self.bomb_timer = 2
        self.enemy_start = 2
        self.enemy_quantity = 2
        self.enemy_spawn_frequency = 0
        self.obstacle_destruction_rate = 0.90

    def get_rounds_played(self):
        return self.rounds_played
    
    def set_rounds_played(self, value):
        self.rounds_played = value

    def get_survived_turns(self):
        return self.survived_turns
    
    def set_survived_turns(self,value):
        self.survived_turns = value

    def get_bombs_utilized(self):
        return self.bombs_utilized
    
    def set_bombs_utilized(self, value):
        self.bombs_utilized = value

    def get_game_over_cause(self):
        return self.game_over_cause
    
    def set_game_over_cause(self, value):
        self.game_over_cause = value

    def get_game_over_turn(self):
        return self.game_over_turn
    
    def set_game_over_turn(self, value):
        self.game_over_turn = value

    def get_maximum_turn(self):
        return self.maximum_turn
    
    def set_maximum_turn(self, value):
        self.maximum_turn = value

    def get_bomb_range(self):
        return self.bomb_range
    
    def set_bomb_range(self, value):
        self.bomb_range = value

    def get_bomb_timer(self):
        return self.bomb_timer
    
    def set_bomb_timer(self, value):
        self.bomb_timer = value

    def get_enemy_start(self):
        return self.enemy_start
    
    def set_enemy_start(self, value):
        self.enemy_start = value

    def get_enemy_quantity(self):
        return self.enemy_quantity
    
    def set_enemy_quantity(self, value):
        self.enemy_quantity = value

    def get_enemy_spawn_frequency(self):
        return self.enemy_spawn_frequency
    
    def set_enemy_spawn_frequency(self, value):
        self.enemy_spawn_frequency = value

    def get_obstacle_destruction_rate(self):
        return self.obstacle_destruction_rate
    
    def set_obstacle_destruction_rate(self, value):
        self.obstacle_destruction_rate = value

    def open(self):
        try:
            with open(self.config_path, "r") as configFile:
                self.config = json.load(configFile)

            self.rounds_played = self.config.get("roundsPlayed", self.rounds_played)
            self.survived_turns = self.config.get("survivedTurns", self.survived_turns)
            self.bombs_utilized = self.config.get("bombsUtilized", self.bombs_utilized)
            self.game_over_cause = self.config.get("gameOverCause", self.game_over_cause)
            self.game_over_turn = self.config.get("gameOverTurn", self.game_over_turn)
            self.maximum_turn = self.config.get("maximumTurn", self.maximum_turn)
            self.bomb_range = self.config.get("bombRange", self.bomb_range)
            self.bomb_timer = self.config.get("bombTimer", self.bomb_timer)
            self.enemy_start = self.config.get("enemyStart", self.enemy_start)
            self.enemy_quantity = self.config.get("enemyQuantity", self.enemy_quantity)
            self.enemy_spawn_frequency = self.config.get("enemySpawnFrequency", self.enemy_spawn_frequency)
            self.obstacle_destruction_rate = self.config.get("obstacleDestructionRate", self.obstacle_destruction_rate)

        except FileNotFoundError:
            print("Erro ao abrir arquivo! Arquivo não existe.")
        
        print(self.config) # debug
