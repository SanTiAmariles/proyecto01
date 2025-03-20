import heapq
import time

matriz = []

class Nodo:
  def __init__(self,x, y,paquetes,costo,visitados,padre,recogidos):
    self.x = x
    self.y = y
    self.faltan = paquetes
    self.costoAcum = costo
    self.visitados = visitados
    self.nombre = f"({self.x},{self.y})"
    self.padre = padre
    self.recogidos = recogidos
  
  def getFaltantes(self):
    return self.faltan
  
  def getPadre(self):
    return self.padre
  
  #Define la comparación entre nodos
  def __lt__(self, otro):
    return self.costoAcum < otro.costoAcum
  
  def __repr__(self):
    return self.nombre
  
  def expandirNodo(self):
    #Me añado a visitados y expando
    lista =[]
    
    #Verifico si es meta y si he terminado
    ogFaltan = self.faltan
    if matriz[self.y][self.x] == 4 and self.nombre not in self.recogidos:
      self.faltan-=1
      self.recogidos.append(self.nombre)
      
    
    self.visitados.append([self.nombre,self.faltan])
    if self.faltan == 0:
      print (f"Terminé, soy {self.nombre} y me faltan {self.faltan} paquetes\nLa ruta que seguí es {self.visitados}")
      return [self]
    
    #El orden es derecha, izquierda, arriba, abajo
    operador = [(1,0),(-1,0),(0,-1),(0,1)]
    for i in range (0,len(operador)):
      nuevoX = self.x+operador[i][0]
      nuevoY = self.y+operador[i][1]
      if 0<=nuevoX<=9  and 0<=nuevoY<=9:
        nuevoValor = matriz[nuevoY][nuevoX]
        nuevoNombre = f"({nuevoX},{nuevoY})"
        costoMover = 1 if nuevoValor in (0, 2, 4) else 8 if nuevoValor == 3 else 0
        if nuevoValor!=1 and [nuevoNombre,self.faltan] not in self.visitados:
          lista.append(Nodo(nuevoX,nuevoY,self.faltan,self.costoAcum+costoMover,self.visitados,self,self.recogidos))
          #print(f"({self.nombre},{ogFaltan}) -> ({nuevoNombre},{self.faltan}). Costo:{self.costoAcum+costoMover}")
          
      '''if len(lista)==0:
        print(f"El nodo {self} no tiene hijos")
        print(f"->=({self.x+1},{self.y}) = {matriz[self.y][self.x+1]}")
        print(f"<-=({self.x-1},{self.y}) = {matriz[self.y][self.x-1]}")
        print(f"Up=({self.x},{self.y-1}) = {matriz[self.y-1][self.x]}")
        print(f"Down=({self.x},{self.y+1}) = {matriz[self.y+1][self.x]}")
        print(f"Visitados: {self.visitados}")'''
    
    return lista
        
      

def buscarSolucion(matrix, x, y, cantPaquetes):
  tiempoInicial = time.time()
  global matriz
  matriz = matrix
  
  raiz = Nodo(x,y,cantPaquetes,0,[],None,[])
  arbol=[]
  cola=[raiz]  
  faltantes = raiz.getFaltantes()
  
  while faltantes>0 and len(cola)>0:
    cabeza = heapq.heappop(cola)
    print(f"Saco el nodo {cabeza} de la cola y me faltan {cabeza.getFaltantes()} paquetes")
    print(f"Mi cola tiene {len(cola)} elementos")
    arbol.append(cabeza)
    faltantes = cabeza.getFaltantes()
    nodos = cabeza.expandirNodo()
    for i in range(0,len(nodos)):
      #print(f"Añado el nodo {nodos[i]} a la cola")
      heapq.heappush(cola,nodos[i])
  
  padre = cabeza.getPadre()
  print(f"Soy {cabeza} y mi padre es {padre}")
  while (padre!=None):
    hijo = padre
    padre = hijo.getPadre()
    print(f"Soy {hijo} y mi padre es {padre}")
  
  
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

buscarSolucion(matrix,1,2,3)