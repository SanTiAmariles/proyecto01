import heapq
import time
from tkinter.messagebox import showinfo

matriz = []
paquetesTotales = 0
posPaquetesFaltan = []

class Nodo:
  #Constructor de la clase
  def __init__(self,row, col,paquetes,visitados,recogidos,paquetesRestantes):
    self.row = row
    self.col = col
    self.faltan = paquetes
    self.paquetesRestantes = paquetesRestantes
    self.costoEstimado = heuristica(paquetes, row, col, paquetesRestantes)
    self.visitados = visitados
    self.recogidos = recogidos
    self.nombre = f"({self.row},{self.col})"
  
  #Retorna el altributo faltan
  def getFaltantes(self):
    return self.faltan
  
  #Retorna el altributo visitados
  def getVisitados(self):
    return self.visitados
  
  #Define la comparación entre nodos
  def __lt__(self, otro):
    return self.costoEstimado < otro.costoEstimado
  
  #Expande el nodo
  def expandirNodo(self):
    lista = []   
    
    # Verifico si el nodo actual es un paquete que no ha sido recogido
    if matriz[self.row][self.col] == 4 and self.nombre not in self.recogidos:
      nuevoFaltan = self.faltan - 1
      nuevoRecogidos = self.recogidos + [self.nombre]
    else:
      nuevoRecogidos = self.recogidos.copy()
      nuevoFaltan = self.faltan
    
    nuevoVisitados = self.visitados + [[self.nombre, nuevoFaltan]]
    
    # Condición de parada
    if nuevoFaltan == 0:
      self.visitados.append([self.nombre, nuevoFaltan])
      return None
    
    # El orden es derecha, izquierda, arriba, abajo
    operador = [(0,1),(0,-1),(-1,0),(1,0)]

    for dx, dy in operador:
      nuevoRow = self.row + dx
      nuevoCol = self.col + dy
      
      # Verificar si el nuevo índice está dentro de la matriz
      if 0 <= nuevoRow < len(matriz) and 0 <= nuevoCol < len(matriz[0]):
        nuevoValor = matriz[nuevoRow][nuevoCol]
        nuevoNombre = f"({nuevoRow},{nuevoCol})"
        
        # Verificar que la nueva casilla no sea un muro y no haya sido visitada
        if nuevoValor != 1 and [nuevoNombre, nuevoFaltan] not in nuevoVisitados:
          paquetesRestantes = [p for p in posPaquetesFaltan if p not in nuevoRecogidos]
          nuevoNodo = Nodo(
            nuevoRow, nuevoCol, nuevoFaltan,
            nuevoVisitados,
            nuevoRecogidos,
            paquetesRestantes
          )
          lista.append(nuevoNodo)
    
    return lista
        
#Funcion para calcular la distancia de manhattan
def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

#Función heuristica 
def heuristica(paquetesFaltantes, x, y, faltan):
  distanciaMinima = 21
  if (paquetesFaltantes == 0):
    return 0
  else:
    for i in faltan:
      posPaquete = tuple(map(int, i.strip("()").split(",")))
      distanciaManhattan = manhattan(x, y, posPaquete[0], posPaquete[1])

      if (distanciaManhattan <= distanciaMinima):
        distanciaMinima = distanciaManhattan
    return distanciaMinima

#Función que permite indicar en que posición estan los paquetes
def conocerPaquetes():
  for i in range(0, 10):
    for j in range(0, 10):
      if matriz[i][j] == 4:
        posPaquetesFaltan.append(f"({i},{j})")

#Función que busca la solución del laberinto
def buscarSolucion(matrix, row, col, cantPaquetes):
  #Inicializar variables
  tiempoInicial = time.time()
  global matriz, paquetesTotales
  paquetesTotales = cantPaquetes
  matriz = matrix  
  conocerPaquetes()
  cantExpandidos=0
  
  #Crear nodo raíz y añadirlo a la cola prioritaria
  raiz = Nodo(row,col,cantPaquetes,[],[],posPaquetesFaltan)
  cola=[raiz]  
  faltantes = raiz.getFaltantes()
  
  #Condición de búsqueda
  while faltantes>0 and len(cola)!=0:
    #Sacar la cabeza de la cola, que es el elemento de menor costo estimado, y expandirlo
    cabeza = heapq.heappop(cola)
    cantExpandidos+=1
    faltantes = cabeza.getFaltantes()
    nodos = cabeza.expandirNodo()
    
    #Condición de parada
    if nodos is None:
      break
    
    #Añadir los nodos expandidos a la cola
    for i in range(0,len(nodos)):
      heapq.heappush(cola,nodos[i])
      
  #Condición de no solución
  if (faltantes>0 and len(cola)==0):
    showinfo(
      title='Error',
      message="El laberinto no se pudo resolver usando este método."
    )
    exit()
  
  tiempoFinal = time.time()
  tiempo = (tiempoFinal-tiempoInicial)*1000
  return(cantExpandidos,len(cabeza.getVisitados())-1,round(tiempo,3),cabeza.getVisitados())