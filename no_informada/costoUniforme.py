import heapq
import time

matriz = []

class Nodo:
  #Constructor de la clase
  def __init__(self,x, y,paquetes,costo,visitados,recogidos):
    self.x = x
    self.y = y
    self.faltan = paquetes
    self.costoAcum = costo
    self.visitados = visitados
    self.recogidos = recogidos
    self.nombre = f"({self.x},{self.y})"
  
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
    nuevoFaltan = self.faltan
    
    
    #Verifico si el nodo actual es un paquete que no ha sido recogido
    if matriz[self.y][self.x] == 4 and self.nombre not in self.recogidos:
      nuevoFaltan-=1
      nuevoRecogidos = self.recogidos + [self.nombre]
    else:
      nuevoRecogidos = self.recogidos.copy()
    
    #nuevoVisitados = self.visitados +[[self.nombre,nuevoFaltan]]
    nuevoVisitados = self.visitados +[[self.nombre,self.faltan]]
    
    #Condición de parada
    if nuevoFaltan == 0:
      self.visitados.append([self.nombre,nuevoFaltan])
      return None
    
    #El orden es derecha, izquierda, arriba, abajo
    #operador = [(1,0),(-1,0),(0,-1),(0,1)]
    operador = [(0,-1),(-1,0),(0,1),(1,0)]
    for i in range (0,len(operador)):
      nuevoX = self.x+operador[i][0]
      nuevoY = self.y+operador[i][1]
      if 0<=nuevoX<=9  and 0<=nuevoY<=9:
        nuevoValor = matriz[nuevoY][nuevoX]
        nuevoNombre = f"({nuevoX},{nuevoY})"
        costoMover = 1 if nuevoValor in (0, 2, 4) else 8 if nuevoValor == 3 else 0
        if nuevoValor!=1 and [nuevoNombre,nuevoFaltan] not in nuevoVisitados:
          lista.append(Nodo(nuevoX,nuevoY,nuevoFaltan,self.costoAcum+costoMover,nuevoVisitados,nuevoRecogidos))
      
    return lista
        
      

def buscarSolucion(matrix, x, y, cantPaquetes):
  tiempoInicial = time.time()
  global matriz
  matriz = matrix
  
  raiz = Nodo(x,y,cantPaquetes,0,[],[])
  cantExpandidos=0
  cola=[raiz]  
  faltantes = raiz.getFaltantes()
  
  while faltantes>0:

    cabeza = heapq.heappop(cola)
    print(f"Expando el nodo {cabeza.nombre}")
    cantExpandidos+=1
    faltantes = cabeza.getFaltantes()
    nodos = cabeza.expandirNodo()
    if nodos is None:
      break
    for i in range(0,len(nodos)):
      heapq.heappush(cola,nodos[i])
  
  tiempoFinal = time.time()
  tiempo = (tiempoFinal-tiempoInicial)*1000
  print(f"La ruta a seguir fue: {cabeza.getVisitados()}")
  return(cantExpandidos,len(cabeza.getVisitados())-1,round(tiempo,3),cabeza.getCostoAcum())

 
matrix = [
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

#buscarSolucion(matrix,1,2,3)