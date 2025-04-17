# El orden es derecha, izquierda, arriba, abajo
"""
Se puede implementar considerando que siempre se va a expandir el nodo más profundo, cada vez
que una rama muere (se queda sin solución) salta a otra rama y expande el nodo de la misma,...Evitando ciclos
"""
from collections import deque

class Nodo:
    def __init__(self, matriz, x, y, cantPaquetes, padre=None, visitados=None):
        self.posicionX = x
        self.posicionY = y
        self.matriz = matriz
        self.faltan = cantPaquetes
        self.padre = padre
        self.paquetes = set()  # Conjunto para almacenar las coordenadas de los paquetes recogidos
        self.visitados = visitados if visitados else set()
        
    def expandir(self):
        movimientos = [
            (-1, 0),  # Arriba
            (0, -1),  # Izquierda
            (1, 0),   # Abajo
            (0, 1)    # Derecha
        ]
        
        vecinos = []
        for dx, dy in movimientos:
            nuevoX = self.posicionX + dx
            nuevoY = self.posicionY + dy

            if (0 <= nuevoX < len(self.matriz) and 
                0 <= nuevoY < len(self.matriz[0]) and 
                self.matriz[nuevoX][nuevoY] != 1 and
                (nuevoX, nuevoY) not in self.visitados):
                
                nuevos_visitados = self.visitados.copy()
                nuevos_visitados.add((nuevoX, nuevoY))
                
                nuevo_nodo = Nodo(
                    self.matriz,
                    nuevoX,
                    nuevoY,
                    self.faltan - (1 if self.matriz[nuevoX][nuevoY] == 4 and (nuevoX, nuevoY) not in self.paquetes else 0),
                    self,
                    nuevos_visitados
                )
                
                nuevo_nodo.paquetes = self.paquetes.copy()
                if self.matriz[nuevoX][nuevoY] == 4:
                    nuevo_nodo.paquetes.add((nuevoX, nuevoY))
                    
                vecinos.append(nuevo_nodo)
                
        return vecinos

def crearPila(matriz):
    inicio_x, inicio_y, cant_paquetes = encontrar_inicio_y_paquetes(matriz)
    nodoRaiz = Nodo(matriz, inicio_x, inicio_y, cant_paquetes)
    pila = deque([nodoRaiz])
    visitados = set()
    expandidos = []
    profundidad_actual = 0
    
    while pila:
        nodoActual = pila.pop()
        nueva_profundidad = len(reconstruir_camino(nodoActual)) - 1
        
        # Detectar cambio de rama
        if nueva_profundidad < profundidad_actual:
            print(f"Rama muerta en ({nodoActual.posicionX}, nodoActual.posicionY)")
            print(f"Retrocediendo a profundidad {nueva_profundidad}")
        
        profundidad_actual = nueva_profundidad
        
        if nodoActual.faltan == 0:
            print(f"\nSe encontró solución")
            print(f"Nodos expandidos: {len(expandidos)}")
            camino = reconstruir_camino(nodoActual)
            print(f"Profundidad de la solución: {len(camino)}")
            return camino
            
        if (nodoActual.posicionX, nodoActual.posicionY) not in visitados:
            visitados.add((nodoActual.posicionX, nodoActual.posicionY))
            expandidos.append(nodoActual)
            
            vecinos = nodoActual.expandir()
            if not vecinos:
                print(f"Rama sin salida en ({nodoActual.posicionX}, {nodoActual.posicionY})")
            
            # Agregamos los vecinos al inicio de la pila (DFS)
            pila.extend(reversed(vecinos))
            
    print("No se encontró solución")
    return None

def encontrar_inicio_y_paquetes(matriz):
    inicio_x = inicio_y = -1
    cant_paquetes = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                inicio_x, inicio_y = i, j
            elif matriz[i][j] == 4:
                cant_paquetes += 1
                
    return inicio_x, inicio_y, cant_paquetes

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append((nodo.posicionX, nodo.posicionY))
        nodo = nodo.padre
    return camino[::-1]

# Matriz de prueba
matriz = [
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 2, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [3, 3, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 4, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

camino = crearPila(matriz)
if camino:
    print("Camino encontrado:", camino)