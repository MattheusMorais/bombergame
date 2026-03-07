class StartMenu:

    def __init__(self, gameState):
        self.gameState = gameState
        self.show_welcome()
         

    def show_welcome(self):
            print("=" * 40)
            print("       CAMPO MINADO - Jogo CLI")
            print("=" * 40)
            if self.gameState.config["roundsPlayed"] > 0:
                print(f"\n📂 Estado da última sessão carregado.")
                # print(self.state.get_difficulty_summary())
            else:
                print("\nPrimeira partida! Boa sorte.\n")
            input("  Pressione ENTER para começar...")