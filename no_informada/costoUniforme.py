import heapq

class Nodo:
    def __init__(self, x, y, cantPaquetes, padre, visitados, costo, profundidad, matriz):
        self.posX = x
        self.posY = y
        self.faltan = cantPaquetes
        self.padre = padre
        self.visitados = set(visitados)  
        self.costoAcum = costo
        self.profundidad = profun

        self.valor = self.matriz[self.posX][self.posY]
        self.costo = 1 if self.valor in (0, 2, 4) else (8 if self.valor == 3 else float('inf'))

  




matriz = [
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 2, 0, 3, 4, 4, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [3, 3, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 4, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

