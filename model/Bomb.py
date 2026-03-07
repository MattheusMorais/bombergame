class Bomb:
    timer = 2
    bombRange = 3

    SYMBOL = "B"

    def __init__(self):
        pass

    def explosion(self):
        if player in rangeOfExplosion:
            print("Player got exploded. GameOver...")
        elif enemy in rangeOfExplosion:
            #enemy vanishes from map(matrix)
            pass
        elif "+" in rangeOfExplosion:
            # destroy object
            pass
        pass



