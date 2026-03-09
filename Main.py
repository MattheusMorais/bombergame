import os
from controller.Gameplay import Gameplay

def main():
    game_play = Gameplay()
    game_play.run()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') 
    main()
    