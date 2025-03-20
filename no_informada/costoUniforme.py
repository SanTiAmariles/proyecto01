import heapq

class Nodo:
    def __init__(self, x, y, cantPaquetes, padre, visitados, costo, profundidad, matriz):
        self.posX = x
        self.posY = y
        self.faltan = cantPaquetes
        self.padre = padre
        self.visitados = set(visitados)  # Usamos un conjunto para mejor eficiencia
        self.costoAcum = costo
        self.profundidad = profundidad
        self.matriz = matriz  # Se añade la matriz como atributo

        self.valor = self.matriz[self.posX][self.posY]
        self.costo = 1 if self.valor in (0, 2, 4) else (8 if self.valor == 3 else float('inf'))

    def expandir(self):
        """ Genera nuevos nodos vecinos en las direcciones permitidas. """
        operadores = [
            (0, 1),  # Derecha
            (0, -1),  # Izquierda
            (-1, 0),  # Arriba
            (1, 0)   # Abajo
        ]

        hijos = []
        for dx, dy in operadores:
            nuevo_x, nuevo_y = self.posX + dx, self.posY + dy
            if 0 <= nuevo_x < len(self.matriz) and 0 <= nuevo_y < len(self.matriz[0]):
                if self.matriz[nuevo_x][nuevo_y] != 1:  # No podemos ir a obstáculos
                    nuevo_faltan = self.faltan - 1 if self.matriz[nuevo_x][nuevo_y] == 4 else self.faltan
                    nuevo_nodo = Nodo(nuevo_x, nuevo_y, nuevo_faltan, self, self.visitados, self.costoAcum + self.costo, self.profundidad + 1, self.matriz)
                    hijos.append(nuevo_nodo)
        return hijos

    def ciclos(self):
        """ Evita visitar nodos repetidos. """
        return (self.posX, self.posY) in self.visitados


def reconstruir_camino(nodo):
    """ Devuelve el camino desde la raíz hasta el nodo final. """
    camino = []
    while nodo:
        camino.append((nodo.posX, nodo.posY))
        nodo = nodo.padre
    return camino[::-1]


def buscarSolucion(matriz, x, y, cantPaquetes):
    """ Algoritmo de búsqueda con prioridad basada en costo acumulado. """
    raiz = Nodo(x, y, cantPaquetes, None, set(), 0, 0, matriz)
    frontera = []
    heapq.heappush(frontera, (raiz.costoAcum, raiz))
    visitados = set()

    while frontera:
        _, nodo_actual = heapq.heappop(frontera)

        # Debugging
        print(f"🔍 Visitando: ({nodo_actual.posX}, {nodo_actual.posY}) - Faltan: {nodo_actual.faltan}, Costo: {nodo_actual.costoAcum}")

        if (nodo_actual.posX, nodo_actual.posY) in visitados:
            continue
        visitados.add((nodo_actual.posX, nodo_actual.posY))

        if nodo_actual.faltan == 0:
            print("¡Todos los paquetes recolectados!")
            return reconstruir_camino(nodo_actual)

        for hijo in nodo_actual.expandir():
            if (hijo.posX, hijo.posY) not in visitados:
                heapq.heappush(frontera, (hijo.costoAcum, hijo))

    print(" No se encontró un camino.")
    return None

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

inicio_x, inicio_y = 2, 2
paquetes = 3 

camino = buscarSolucion(matriz, inicio_x, inicio_y, paquetes)
print("🚀 Camino encontrado:", camino)
