# El orden es derecha, izquierda, arriba, abajo
"""
Se puede implementar considerando que siempre se va a expandir el nodo más profundo, cada vez
que una rama muere (se queda sin solución) salta a otra rama y expande el nodo de la misma,...Evitando ciclos
"""
from collections import deque

class Nodo:
    def __init__(self, matriz, x, y, cantPaquetes, padre=None, costo=0, profundidad=0):
        self.posicionX = x
        self.posicionY = y
        self.matriz = matriz
        self.faltan = cantPaquetes
        self.padre = padre
        self.costo = costo
        self.profundidad = profundidad
        
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

                    if self.matriz[nuevoX][nuevoY] == 4:  
                        nuevaFaltan -= 1

                    if self.matriz[nuevoX][nuevoY] != 1:  
                        nuevaCelda = Nodo(self.matriz, nuevoX, nuevoY, nuevaFaltan, self, self.costo + 1, self.profundidad + 1)
                        vecinos.append(nuevaCelda)

            return vecinos

def encontrar_inicio_y_paquetes(matriz):
    inicio_x = inicio_y = -1
    cant_paquetes = 0
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 2:
                inicio_x, inicio_y = i, j
            elif valor == 4:
                cant_paquetes += 1
    return inicio_x, inicio_y, cant_paquetes

def crearPila(matriz):
    inicio_x, inicio_y, cant_paquetes = encontrar_inicio_y_paquetes(matriz)
    nodoRaiz = Nodo(matriz, inicio_x, inicio_y, cant_paquetes)
    pila = deque()
    pila.append(nodoRaiz)
    visitados = set()

    while pila:
        nodoActual = pila.pop()
        if nodoActual.faltan == 0:
            print("Se recogieron todos los paquetes con éxito")
            return reconstruir_camino(nodoActual)

        if (nodoActual.posicionX, nodoActual.posicionY) in visitados:
            continue  # Evitar volver a visitar nodos

        visitados.add((nodoActual.posicionX, nodoActual.posicionY))

        print(nodoActual.posicionX, ",", nodoActual.posicionY)
        vecinos = nodoActual.expandir()
        pila.extend(vecinos)

    print("No se encontraron todos los paquetes")
    return None

#Camino nuevo si una rama muere
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append((nodo.posicionX, nodo.posicionY))
        nodo = nodo.padre
    return camino[::-1]

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

camino = crearPila(matriz)
print("Camino encontrado:", camino)