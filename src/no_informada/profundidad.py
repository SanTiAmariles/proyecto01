import time
from tkinter.messagebox import showinfo

matriz = []

class Nodo:
  #Constructor de la clase
  def __init__(self,row, col,paquetes,visitados,recogidos):
    self.row = row
    self.col = col
    self.faltan = paquetes
    self.visitados = visitados
    self.recogidos = recogidos
    self.nombre = f"({self.row},{self.col})"
  
  #Retorna el altributo faltan
  def getFaltantes(self):
    return self.faltan
  
  #Retorna el altributo visitados
  def getVisitados(self):
    return self.visitados
  
  #Expande el nodo
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
      print("Retorno None")
      return None
    
    #El orden es derecha, izquierda, arriba, abajo, así que lo escribo al reves
    operador = [(1,0),(-1,0),(0,-1),(0,1)]
    for i in range (0,len(operador)):
      nuevoRow = self.row+operador[i][0]
      nuevoCol = self.col+operador[i][1]
      
      #Verificar si nuevo índice está dentro de la matriz
      if 0<=nuevoRow<=9  and 0<=nuevoCol<=9:
        nuevoValor = matriz[nuevoRow][nuevoCol]
        nuevoNombre = f"({nuevoRow},{nuevoCol})"
        
        #Verificar que la nueva casilla no sea un muro ni haya sido visitada por la rama
        if nuevoValor!=1 and [nuevoNombre,nuevoFaltan] not in nuevoVisitados:
          lista.append(Nodo(nuevoRow,nuevoCol,nuevoFaltan,nuevoVisitados,nuevoRecogidos))
    
    return lista
        
      
#Función que busca la solución del laberinto
def buscarSolucion(matrix, row, col, cantPaquetes):
  #Inicializar variables
  tiempoInicial = time.time()
  global matriz
  matriz = matrix  
  cantExpandidos=0
  
  #Crear nodo raíz y añadirlo a la lista
  raiz = Nodo(row,col,cantPaquetes,[],[])
  pila=[raiz]  
  faltantes = raiz.getFaltantes()
  
  #Condición de búsqueda
  while faltantes>0 and len(pila)!=0:
    #Sacar el elemento último elemento de la pila, que es el de mayor profundidad, y expandirlo
    nodoExpandir = pila.pop()
    cantExpandidos+=1
    faltantes = nodoExpandir.getFaltantes()
    nodos = nodoExpandir.expandirNodo()
    
    #Condición de parada
    if nodos is None:
      print(f"Hago break, mi cabeza es: {nodoExpandir.nombre}")
      break
    
    #Añadir los nodos expandidos a la pila
    if len(nodos)!=0:
      pila.extend(nodos)
  
  #Condición de no solución
  if (faltantes>0 and len(pila)==0):
    showinfo(
      title='Error',
      message="El laberinto no se pudo resolver usando este método."
    )
    exit()
    
  tiempoFinal = time.time()
  tiempo = (tiempoFinal-tiempoInicial)*1000
  return(cantExpandidos,len(nodoExpandir.getVisitados())-1,round(tiempo,3),nodoExpandir.getVisitados())