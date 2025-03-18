#El orden es derecha, izquierda, arriba, abajo
"""
Se puede implementar considerando la lista de nodos a expandir como una cola 
de prioridad, donde la prioridad es el costo y se selecciona aquel con mejor prioridad
"""
import heapq

arbol = []
cola = []
resultado=[]

class Nodo:
  def __init__(self, matriz,x, y, cantPaquetes, padre, costo, profundidad, expandidos):
    self.matriz = matriz
    self.posX = x
    self.posY = y
    self.faltan = cantPaquetes
    self.padre = padre
    self.costoAcum = costo
    self.profundidad = profundidad
    self.expandidos = expandidos
    
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
    return self.matriz[self.posY][self.posX]
  
  #Define la comparación entre nodos
  def __lt__(self, otro):
    return self.costoAcum < otro.costoAcum
  
  #Define que se muestra al imprimir un nodo
  def __repr__(self):
    return "("+str(self.posX)+","+str(self.posY)+")"
  
  #Crea una lista con los nodos que se pueden expandir a partir del nodo actual
  def nodosExpandir(self):
    lista=[]
    
    #Derecha
    if self.posX+1 <=9 and getValor(self.matriz, self.posX+1,self.posY)!=1:
      lista.append((self.posX+1,self.posY))
      self.expandidos+=1
    
    #Izquierda
    if self.posX-1 >=0 and getValor(self.matriz, self.posX-1,self.posY)!=1:
      lista.append((self.posX-1,self.posY))
      self.expandidos+=1
    
    #Arriba
    if self.posY-1 >=0 and getValor(self.matriz, self.posX,self.posY-1)!=1:
      lista.append((self.posX,self.posY-1))
      self.expandidos+=1
      
    #Abajo
    if self.posY+1 <=9 and getValor(self.matriz, self.posX,self.posY+1)!=1:
      lista.append((self.posX,self.posY+1))
      self.expandidos+=1  
    
    return lista

def buscarSolucion(matriz, x, y, cantPaquetes):
  global arbol, cola, faltantes
  faltantes = cantPaquetes
  
  #Crear y expandir la raiz
  raiz = Nodo(matriz,x, y, cantPaquetes, None, 0, 0, 0)
  arbol.append(raiz)
  nodos=raiz.nodosExpandir()
  for i in range(0, len(nodos)):
    nuevoX = nodos[i][0]
    nuevoY = nodos[i][1]
    valor = getValor(matriz,nuevoX,nuevoY)
    heapq.heappush(cola,Nodo(matriz,nuevoX,nuevoY,faltantes,raiz,getCosto(valor),1,0))
  
  #Tomo cabeza, la añado a resultado, miro si es paquete, miro que nodos se pueden expandir
  #Y los creo en la cola
  while faltantes>0:
    cabeza = heapq.heappop(cola)
    arbol.append(cabeza)
    
    if cabeza.getValor()==4:
      faltantes-=1
      print(f"Se recogió el paquete {cabeza}")
      matriz[cabeza.getY()][cabeza.getX()]=0
      
    nodos=cabeza.nodosExpandir()
    for i in range(0, len(nodos)):
      nuevoX = nodos[i][0]
      nuevoY = nodos[i][1]
      nuevoValor = getValor(matriz,nuevoX,nuevoY)
      nuevoCosto = cabeza.getCosto()+getCosto(nuevoValor)
      nuevaProfundidad = cabeza.getProfundidad()+1
      nuevoExpandidos = cabeza.getExpandidos()
      #(matriz,x, y, cantPaquetes, padre, costo, profundidad, expandidos)
      heapq.heappush(cola,Nodo(matriz,nuevoX,nuevoY,faltantes,cabeza,nuevoCosto,nuevaProfundidad,nuevoExpandidos))
  
  #print (cola)
  
  #if faltantes==0:
  #Tomo el último elemento de la lista, lo añado al resultado
  #Busco su padre, lo añado a la lista, y busco a ese padre hasta que sea None
  final = arbol[-1]
  
  print(f"Cantidad de nodos expandidos: {len(arbol)}")
  print(f"Profundidad del árbol: {final.getProfundidad()}")
  print(f"Costo de la solución: {final.getCosto()}")
  
  resultado.append(final)
  padre = final.getPadre()
  print(f"Soy {final} y mi padre es {padre}")
  while (padre!=None):
    resultado.append(padre)
    hijo = padre
    padre = hijo.getPadre()
    print(f"Soy {hijo} y mi padre es {padre}")
    
  print("Terminé")
  #print(resultado)
    #return resultado


def getValor(matriz,x,y):
  return matriz[y][x]

def getCosto(valor):
  if valor in (0, 2, 4):
    return 1
  elif valor== 3:
    return 8
  else:
    return 0

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

buscarSolucion(matriz,1,2,3)