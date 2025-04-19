from collections import deque
import time
from tkinter.messagebox import showinfo

matriz = []

class Nodo:
    def __init__(self, matriz, x, y, cantPaquetes, camino=None):
        self.posicionX = x
        self.posicionY = y
        self.matriz = matriz
        self.faltan = cantPaquetes
        self.camino = camino if camino else [(x, y)]
        
    def expandir(self):
        operadores = [
            (1, 0),  # Derecha
            (-1, 0),  # Izquierda
            (0, 1),  # Abajo
            (0, -1)  # Arriba
        ]

        vecinos = []
        for dx, dy in operadores:
            nuevoX = self.posicionX + dx
            nuevoY = self.posicionY + dy

            if 0 <= nuevoX < len(self.matriz) and 0 <= nuevoY < len(self.matriz[0]):
                nuevaFaltan = self.faltan
                nuevaMatriz = [fila[:] for fila in self.matriz]

                if nuevaMatriz[nuevoX][nuevoY] == 4:
                    nuevaFaltan -= 1
                    nuevaMatriz[nuevoX][nuevoY] = 0

                if nuevaMatriz[nuevoX][nuevoY] != 1:
                    nuevoCamino = self.camino + [(nuevoX, nuevoY)]
                    nuevoNodo = Nodo(nuevaMatriz, nuevoX, nuevoY, nuevaFaltan, nuevoCamino)
                    vecinos.append(nuevoNodo)

        return vecinos

def crearCola(matriz, x, y, cantPaquetes):
    nodoRaiz = Nodo(matriz, x, y, cantPaquetes)
    cola = deque()
    cola.append(nodoRaiz)
    visitados = set()  

    while cola:
        nodoActual = cola.popleft()
        estado_actual = (nodoActual.posicionX, nodoActual.posicionY, nodoActual.faltan)

        # Verificar si el estado ya fue visitado
        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)
        
        # Verificar si se han recogido todos los paquetes
        if nodoActual.faltan == 0:
            return nodoActual.camino

        # Expandir los nodos vecinos
        vecinos = nodoActual.expandir()
        cola.extend(vecinos)

    showinfo(
      title='Error',
      message="El laberinto no se pudo resolver usando este método."
    )
    exit()

def buscarSolucion(matriz, x, y, cantPaquetes):
    inicio = time.time() 
    camino = crearCola(matriz, x, y, cantPaquetes)
    fin = time.time() 

    if camino:
        expandidos = len(camino)  
        profundidad = len(camino) - 1 
        tiempo = (fin - inicio) * 1000  
        return expandidos, profundidad, round(tiempo,3), camino
    else:
        return 0, 0, 0, []  # Si no hay solución, devuelve valor por defecto
