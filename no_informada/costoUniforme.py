#El orden es derecha, izquierda, arriba, abajo
"""
Se puede implementar considerando la lista de nodos a expandir como una cola 
de prioridad, donde la prioridad es el costo y se selecciona aquel con mejor prioridad
"""
import heapq
import time

arbol = []
cola = []
resultado=[]
recogidos=[]
matriz = []

class Nodo:
  def __init__(self,x, y, cantPaquetes, padre, costo, profundidad, expandidos):
    self.posX = x
    self.posY = y
    self.faltan = cantPaquetes
    self.padre = padre
    self.costoAcum = costo
    self.profundidad = profundidad
    self.expandidos = expandidos
    self.nombre = "("+str(self.posX)+","+str(self.posY)+")"
    
  #Métodos Get
  def getX(self):
    return self.posX
  
  def getY(self):
    return self.posY
  
  def getFaltan(self):
    return self.faltan
  
  def getPadre(self):
    return self.padre
  
  def getCosto(self):
    return self.costoAcum
  
  def getProfundidad(self):
    return self.profundidad
  
  def getExpandidos(self):
    return self.expandidos
  
  def getValor(self):
    return matriz[self.posY][self.posX]
  
  def getNombre(self):
    return self.nombre
  
  #Define la comparación entre nodos
  def __lt__(self, otro):
    return self.costoAcum < otro.costoAcum
  
  #Define que se muestra al imprimir un nodo
  def __repr__(self):
    return self.nombre
  
  #Crea una lista con los nodos que se pueden expandir a partir del nodo actual
  def nodosExpandir(self):
    lista=[]
    
    #Derecha
    if self.posX+1 <=9 and getValor(self.posX+1,self.posY)!=1:
      lista.append((self.posX+1,self.posY))
      self.expandidos+=1
    
    #Izquierda
    if self.posX-1 >=0 and getValor(self.posX-1,self.posY)!=1:
      lista.append((self.posX-1,self.posY))
      self.expandidos+=1
    
    #Arriba
    if self.posY-1 >=0 and getValor(self.posX,self.posY-1)!=1:
      lista.append((self.posX,self.posY-1))
      self.expandidos+=1
      
    #Abajo
    if self.posY+1 <=9 and getValor(self.posX,self.posY+1)!=1:
      lista.append((self.posX,self.posY+1))
      self.expandidos+=1  
    
    return lista
  
#Obtiene el valor de la matriz en la posición especificada
def getValor(x,y):
  global matriz
  return matriz[y][x]

#Obtiene el costo del movimiento
def getCosto(valor):
  if valor in (0, 2, 4):
    return 1
  elif valor== 3:
    return 8
  else:
    return 0

#Busca al camino que debe seguir el dron para recoger todos los paquetes
def buscarSolucion(matrix, x, y, cantPaquetes):
  tiempoInicial = time.time()
  global arbol, cola, faltantes, recogidos, matriz
  matriz = matrix
  faltantes = cantPaquetes
  
  #Crear y expandir la raiz
  raiz = Nodo(x, y, cantPaquetes, None, 0, 0, 0)
  print("Creo la raiz")
  arbol.append(raiz)
  nodos=raiz.nodosExpandir()
  for i in range(0, len(nodos)):
    nuevoX = nodos[i][0]
    nuevoY = nodos[i][1]
    valor = getValor(nuevoX,nuevoY)
    heapq.heappush(cola,Nodo(nuevoX,nuevoY,cantPaquetes,raiz,getCosto(valor),1,0))
  print("Expando la raiz")
  #Tomo cabeza, la añado a resultado, miro si es paquete, miro que nodos se pueden expandir
  #Y los creo en la cola
  while faltantes>0:
    cabeza = heapq.heappop(cola)
    print(f"Soy {cabeza} y me faltan {faltantes} paquetes")
    arbol.append(cabeza)
    '''
    if cabeza.getValor()==4 and cabeza.getNombre() not in recogidos:
      recogidos.append(cabeza.getNombre())
      faltantes-=1
      print(f"Se recogió el paquete {cabeza}")
    '''  
    #(self,x, y, cantPaquetes, padre, costo, profundidad, expandidos)
    nodos=cabeza.nodosExpandir()
    for i in range(0, len(nodos)):
      nuevoX = nodos[i][0]
      nuevoY = nodos[i][1]
      nuevoValor = getValor(nuevoX,nuevoY)
      nuevoCosto = cabeza.getCosto()+getCosto(nuevoValor)
      nuevaProfundidad = cabeza.getProfundidad()+1
      nuevoExpandidos = cabeza.getExpandidos()
      
      if cabeza.getValor()==4:
        nuevoFaltantes = cabeza.getFaltan()-1
        faltantes = nuevoFaltantes
      else:
        nuevoFaltantes = cabeza.getFaltan()
      
      nuevoNodo = Nodo(nuevoX,nuevoY,nuevoFaltantes,cabeza,nuevoCosto,nuevaProfundidad,nuevoExpandidos)
      
      if cabeza.getPadre().getNombre()!=nuevoNodo.getNombre() and cabeza.getPadre().getFaltan()!=nuevoNodo.getFaltan():
        heapq.heappush(cola,nuevoNodo)
      
      #si padre de cabeza es igual a mi, no lo añado
      #Si valor de cabeza es 4, mi nuevo faltasntes es cabeza-1
      #Si no, nuevo faltantes es igual a cabeza 
      
  #print (arbol)
  
  #Tomo el último elemento de la lista, lo añado al resultado
  #Busco su padre, lo añado a la lista, y busco a ese padre hasta que sea None
  tiempoFinal = time.time()
  tiempo = tiempoFinal-tiempoInicial
  
  final = arbol[-1]
  
  print(f"Los paquetes recogidos fueron {recogidos}")
  print(f"Cantidad de nodos expandidos: {len(arbol)}")
  print(f"Cantidad de nodos expandidos V2: {final.getExpandidos()}")
  print(f"Profundidad del árbol: {final.getProfundidad()}")
  print(f"Tiempo de ejecución: {round(tiempo,2)} segundos")
  print(f"Costo de la solución: {final.getCosto()}")
  
  resultado.append(final)
  padre = final.getPadre()
  print(f"Soy {final} y mi padre es {padre}")
  while (padre!=None):
    resultado.append(padre)
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