import os

from controller.Gameplay import Gameplay

def main():
    gamePlay = Gameplay()
    gamePlay.run()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') 
    main()
    