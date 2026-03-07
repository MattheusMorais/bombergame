class GameOver:

    cause_EXPLOSION = "Explosão"
    cause_ENEMY = "Inimigo"
    cause_SUCESS = "Sobreviveu!"

    @staticMethod
    def showGameOverScreen(self):

        if self.cause_SUCESS:
            print("  🎉  VOCÊ SOBREVIVEU!  🎉")
        else:
            print(f"  💀  GAME OVER  💀")
            print(f"  Eliminado por: {cause} no turno {turn}")


