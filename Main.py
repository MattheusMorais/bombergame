from model.Helper import clear_screen
from controller.Gameplay import Gameplay

def main():
    game_play = Gameplay()
    game_play.game_loop()

if __name__ == "__main__":
    clear_screen()
    main()
    