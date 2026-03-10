from model.Helper import clear_screen
from controller.Gameplay import Gameplay

def main():
    while True:
        game_play = Gameplay()
        close_game = game_play.game_loop()

        if close_game:
            return

if __name__ == "__main__":
    clear_screen()
    main()
    