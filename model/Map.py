class Map:

    def __init__(self):
        pass

    def createMap(self):
        n = 8

        mat = [[" " for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==0 or i== n-1 or j == 0 or j == n-1:
                    mat[i][j] = "#"

        return mat

    def printMap(self, mat):
        for linha in mat:
            print(" ".join(linha))
        


        
        


