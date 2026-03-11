from model.Helper import clear_screen

class GameOver:
    """ 
    Exibe a tela de Game Over do jogo, mostrando a causa da morte ou sucesso e o turno em que ocorreu.

    Attributes:
        cause_EXPLOSION (str): Representa morte por explosão.
        cause_ENEMY (str): Representa morte por inimigo.
        cause_SUCCESS (str): Representa sucesso em sobreviver.
        game_over_cause (str): Causa do fim do jogo.
        game_over_turn (int): Turno em que o jogador foi eliminado ou sobreviveu.
    """

    cause_EXPLOSION = "Explosão"
    cause_ENEMY = "Inimigo"
    cause_SUCCESS = "Sobreviveu!"

    def __init__(self, game_over_cause, game_over_turn):
        self.game_over_cause = game_over_cause
        self.game_over_turn = game_over_turn
        self.show_game_over_screen()

    def show_game_over_screen(self):
        clear_screen()

        if self.game_over_cause == self.cause_SUCCESS:
            print("  🎉  VOCÊ SOBREVIVEU!  🎉")
        else:
            print(f"  💀  GAME OVER  💀")
            print(f"  Eliminado por: {self.game_over_cause} no turno {self.game_over_turn}")
        