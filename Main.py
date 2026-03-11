from model.Helper import clear_screen
from controller.Gameplay import Gameplay

def main():
    """ 
    Inicializa e executa o loop principal do jogo.

    Observação: O loop while True garante que o jogador possa reiniciar o jogo sem que a execução anterior continue em segundo plano.

    """

    while True:
        game_play = Gameplay()
        close_game = game_play.game_loop()

        if close_game: 
            break

if __name__ == "__main__":
    clear_screen() 
    main()
    