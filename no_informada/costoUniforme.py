#El orden es derecha, izquierda, arriba, abajo
"""
Se puede implementar considerando la lista de nodos a expandir como una cola 
de prioridad, donde la prioridad es el costo y se selecciona aquel con mejor prioridad
"""
class Nodo:
  def __init__(self, x, y, cantPaquetes, padre, visitados, costo, profundidad):
    self.posX = x
    self.posY = y
    self.faltan = cantPaquetes
    self.padre = padre
    self.visitados = visitados
    self.costoAcum = costo
    self.profundidad = profundidad
    self.valor = self.matriz[self.posX][self.posY]
    self.costo = 1 if self.valor in (0, 2, 4) else (8 if self.valor == 3 else 0)
    
  def expandir (self):
    operadores = [
      (1, 0),  # Derecha
      (-1, 0),  # Izquierda
      (0, 1),  # Arriba
      (0, -1)  # Abajo
    ]
    
    if self.faltan == 0:
      return ["Fin"]
    elif self.faltan >= 0:
      print("Prueba")
  
  def ciclos(self):
    if (self.posX,self.posY) in self.visitados:
      return True
    else:
      return False
      
    
    
def buscarSolucion(matriz, x, y, cantPaquetes):
  raiz = Nodo(x, y, cantPaquetes, [], [], 0, 0)