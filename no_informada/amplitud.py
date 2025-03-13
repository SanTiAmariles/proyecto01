from collections import deque

class Nodo:
    def __init__(self, matriz, x, y, cantPaquetes, visitados=None):
        # Posición inicial del dron
        self.posicionX = x
        self.posicionY = y
        self.matriz = matriz
        self.faltan = cantPaquetes
        
        # para registr las celdas visitadas en cada ruta
        self.visitados_camino = visitados.copy() if visitados else set()
        self.visitados_camino.add((x, y))  # Toma la celda como visitada

    def expandir(self):
        operadores = [
            (1, 0),  # Derecha
            (-1, 0),  # Izquierda
            (0, 1),  # Abajo
            (0, -1)  # Arriba
        ]

        if self.faltan == 0:
            return ["Fin"]
        elif self.faltan >= 0:
            vecinos = []
            for dx, dy in operadores:
                nuevoX = self.posicionX + dx
                nuevoY = self.posicionY + dy

                if 0 <= nuevoX < len(self.matriz) and 0 <= nuevoY < len(self.matriz[0]):
                    nuevaFaltan = self.faltan  

                    if (nuevoX, nuevoY) in self.visitados_camino:
                        continue 

                    nuevaFaltan = self.faltan 

                    if self.matriz[nuevoX][nuevoY] == 4:  
                        nuevaFaltan -= 1

                    if self.matriz[nuevoX][nuevoY] == 4: 
                        self.faltan -= 1

                    if self.matriz[nuevoX][nuevoY] != 1:  
                        nuevo_visitados_camino = self.visitados_camino.copy() # copia el historial de celdas visitadas del nodp actual.
                        nuevo_visitados_camino.add((nuevoX, nuevoY)) # agrega la nueva posición para el nodo hijo.

                        nuevaCelda = Nodo(self.matriz, nuevoX, nuevoY, self.faltan, nuevo_visitados_camino)
                        vecinos.append(nuevaCelda)

            return vecinos

        
def crearCola(matriz, x, y, cantPaquetes):
    nodoRaiz = Nodo(matriz, x, y, cantPaquetes)
    cola = deque()
    cola.append(nodoRaiz)

    while cola:
        nodoActual = cola.popleft()
        if nodoActual == "Fin":
            print("Se recogieron todos los paquetes con éxito")
            return 1
        print(nodoActual.posicionX, ",", nodoActual.posicionY)
        vecinos = nodoActual.expandir()
        cola.extend(vecinos)

    
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

crearCola(matriz, 2, 1, 3)
