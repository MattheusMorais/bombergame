import json
import os

class GameState:

    

    def __init__(self, config_path = "config/gameConfig.json"):
        self.config_path = config_path
        self.config = {}
    

    def open(self):
        try:
            with open(self.config_path, "r") as configFile:
                self.config = json.load(configFile)
        except FileNotFoundError:
            print("Erro ao abrir arquivo! Arquivo não existe.")
        
        print(self.config)

    def updateGameConfig(self):
        pass
        