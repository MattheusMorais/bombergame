from model.Helper import clear_screen

class GameOver:

    cause_EXPLOSION = "Explosão"
    cause_ENEMY = "Inimigo"
    cause_SUCESS = "Sobreviveu!"

    def __init__(self, game_over_cause, game_over_turn):
        self.game_over_cause = game_over_cause
        self.game_over_turn = game_over_turn
        self.show_game_over_screen()

    def show_game_over_screen(self):
        clear_screen()

        if self.game_over_cause == GameOver.cause_SUCESS:
            print("  🎉  VOCÊ SOBREVIVEU!  🎉")
        else:
            print(f"  💀  GAME OVER  💀")
            print(f"  Eliminado por: {self.game_over_cause} no turno {self.game_over_turn}")
        