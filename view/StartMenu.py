class StartMenu:

    def __init__(self, game_state):
        self.game_state = game_state
        self.show_welcome()
         
    def show_welcome(self):
            print("=" * 40)
            print("       CAMPO MINADO - Jogo CLI")
            print("=" * 40)
            if self.game_state.get_rounds_played() > 0:
                print(f"\n📂 Estatisticas da ultima sessão.")
                print(f"Partidas jogadas: {self.game_state.get_rounds_played()}")
                print(f"Causa da última morte: {self.game_state.get_game_over_cause()}")
                print(f"Inimigos eliminados: {self.game_state.get_killed_enemies()}")
            else:
                print("\nPrimeira partida! Boa sorte.\n")
            input("  Pressione ENTER para começar...")
             