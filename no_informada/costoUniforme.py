import heapq
import time

matriz = []

class Nodo:
  #Constructor de la clase
  def __init__(self,row, col,paquetes,costo,visitados,recogidos):
    self.row = row
    self.col = col
    self.faltan = paquetes
    self.costoAcum = costo
    self.visitados = visitados
    self.recogidos = recogidos
    self.nombre = f"({self.row},{self.col})"
  
  #Retorna el altributo faltan
  def getFaltantes(self):
    return self.faltan
  
  #Retorna el altributo visitados
  def getVisitados(self):
    return self.visitados
  
  #Retorna el altributo costoAcum
  def getCostoAcum(self):
    return self.costoAcum  
  
  #Define la comparación entre nodos
  def __lt__(self, otro):
    return self.costoAcum < otro.costoAcum
  
  def expandirNodo(self):
    lista =[]   
    
    #Verifico si el nodo actual es un paquete que no ha sido recogido
    if matriz[self.row][self.col] == 4 and self.nombre not in self.recogidos:
      nuevoFaltan=self.faltan-1
      nuevoRecogidos = self.recogidos + [self.nombre]
    else:
      nuevoRecogidos = self.recogidos.copy()
      nuevoFaltan=self.faltan
    
    nuevoVisitados = self.visitados +[[self.nombre,nuevoFaltan]]
    
    #Condición de parada
    if nuevoFaltan == 0:
      self.visitados.append([self.nombre,nuevoFaltan])
      return None
    
    #El orden es derecha, izquierda, arriba, abajo
    operador = [(0,1),(0,-1),(-1,0),(1,0)]
    for i in range (0,len(operador)):
      nuevoRow = self.row+operador[i][0]
      nuevoCol = self.col+operador[i][1]
      #Verificar si nuevo índice está dentro de la matriz
      if 0<=nuevoRow<=9  and 0<=nuevoCol<=9:
        nuevoValor = matriz[nuevoRow][nuevoCol]
        nuevoNombre = f"({nuevoRow},{nuevoCol})"
        costoMover = 1 if nuevoValor in (0, 2, 4) else 8 if nuevoValor == 3 else 0
        #Verificar que la nueva casilla no sea un muro y haya sido visitada por la rama
        if nuevoValor!=1 and [nuevoNombre,nuevoFaltan] not in nuevoVisitados:
          lista.append(Nodo(nuevoRow,nuevoCol,nuevoFaltan,self.costoAcum+costoMover,nuevoVisitados,nuevoRecogidos))
      
    return lista
        
      
#Función que busca la solución del laberinto
def buscarSolucion(matrix, row, col, cantPaquetes):
  #Inicializar variables
  tiempoInicial = time.time()
  global matriz
  matriz = matrix  
  cantExpandidos=0
  
  #Crear nodo raíz y añadirlo a la cola prioritaria
  raiz = Nodo(row,col,cantPaquetes,0,[],[])
  cola=[raiz]  
  faltantes = raiz.getFaltantes()
  
  #Condición de búsqueda
  while faltantes>0:
    #Sacar la cabeza de la cola, que es el elemento de menor costo, y expandirlo
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
  
  tiempoFinal = time.time()
  tiempo = (tiempoFinal-tiempoInicial)*1000
  return(cantExpandidos,len(cabeza.getVisitados())-1,round(tiempo,3),cabeza.getCostoAcum(),cabeza.getVisitados())