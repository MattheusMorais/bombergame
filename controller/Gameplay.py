from model.Map import Map

class Gameplay:

    def __init__(self):
        pass

    def run(self):
        game_map = Map()
        createdMap = game_map.createMap()
        game_map.printMap(createdMap)