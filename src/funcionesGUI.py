import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import gui
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from no_informada import amplitud, profundidad, costoUniforme
from informada import aEstrella, avara


archivo = False
tipoBusqueda = ""
matriz = []
x=0
y=0
paquetes=0

def selectFile(boton,marcoPrincipal, cell_size,canvas, marco):
  global archivo
  global matriz
  filetypes = [('text files', '*.txt')]

  global filename
  filename = fd.askopenfilename(
    title='Seleccione el archivo a importar',
    filetypes=filetypes)

  if filename:
    archivo = True
    showinfo(
      title='Archivo seleccionado',
      message="Ha seleccionado el archivo " + filename
    )    
  else:
    showinfo(
      title='Error',
      message="No ha seleccionado ningún archivo"
    )
    return
    
  if archivo:
    with open(filename, "r") as entrada:
      for linea in entrada:
        try:
          valores = list(map(int, linea.strip().split()))
          matriz.append(valores)
        except:
          showinfo(
            title='Error',
            message="El archivo seleccionado no es válido"
          )
          return
  
  if len(matriz)!=10:
    showinfo(
      title='Error',
      message="El ambiente represetado no tiene el tamaño correcto"
    )
    return
  else:
    for i in range (10):
      if len(matriz[i])!=10:
        showinfo(
          title='Error',
          message="El ambiente represetado no tiene el tamaño correcto"
        )
        return
  showinfo(
    title='Operación exitosa',
    message="Archivo procesado correctamente"
  )
  boton.config(state=tk.DISABLED)  
  print(matriz)  
  grid = gui.GridCuadricula(marcoPrincipal, matriz, cell_size)
  grid.dibujar_cuadricula(canvas)
  marco.grid()
  procesarMatriz()
  
def noInformada(rb1, rb2, rb3, rb4, rb5, b):
  global tipoBusqueda
  rb1.config(state=tk.NORMAL)
  rb2.config(state=tk.NORMAL)
  rb3.config(state=tk.NORMAL)
  rb4.config(state=tk.DISABLED)
  rb5.config(state=tk.DISABLED)
  b.config(state=tk.NORMAL)
  tipoBusqueda = "noInformada"
  
def informada(rb1, rb2, rb3, rb4, rb5, b):
  global tipoBusqueda
  rb1.config(state=tk.DISABLED)
  rb2.config(state=tk.DISABLED)
  rb3.config(state=tk.DISABLED)
  rb4.config(state=tk.NORMAL)
  rb5.config(state=tk.NORMAL)
  b.config(state=tk.NORMAL)
  tipoBusqueda = "informada"

def buscar(op1, op2, boton):
  global tipoBusqueda
  if tipoBusqueda=="noInformada":
    if op1.get() == "amplitud":
      #amplitud.crearCola(matriz,x,y,paquetes)
      showinfo(
        title='Resultados',
        message="RESULTADOS DE LA BÚSQUEDA\n\n\nCantidad de nodos expandidos:\n\nProfundidad del árbol:\n\nTiempo de cómputo:"
      )
      exit()
    elif op1.get() == "uniforme":
      print("Costo Uniforme")
      expandidos,profundidad,tiempo,costo = costoUniforme.buscarSolucion(matriz,x,y,paquetes)
      showinfo(
        title='Resultados',
        message=f"RESULTADOS DE LA BÚSQUEDA\n\nCantidad de nodos expandidos: {expandidos}\nProfundidad del árbol: {profundidad}\nTiempo de cómputo: {tiempo} milisegundos\nCosto de la solución: {costo}"
      )
      exit()
    elif op1.get() == "profundidad":
      print("Profundidad")
      showinfo(
        title='Resultados',
        message="RESULTADOS DE LA BÚSQUEDA\n\n\nCantidad de nodos expandidos:\n\nProfundidad del árbol:\n\nTiempo de cómputo:"
      )
      exit()
    else:
      showinfo(
        title='Error',
        message="Error en la búsqueda"
      )
      return
    boton.config(state=tk.DISABLED)
  elif tipoBusqueda=="informada":
    if op2.get() == "avara":
      print("Avara")
      showinfo(
        title='Resultados',
        message="RESULTADOS DE LA BÚSQUEDA\n\n\nCantidad de nodos expandidos:\n\nProfundidad del árbol:\n\nTiempo de cómputo:"
      )
      exit()
    elif op2.get() == "aEstrella":
      print("A*")
      showinfo(
        title='Resultados',
        message="RESULTADOS DE LA BÚSQUEDA\n\n\nCantidad de nodos expandidos:\n\nProfundidad del árbol:\n\nTiempo de cómputo:\n\nCosto de la solución:"
      )
      exit()
    else:
      showinfo(
        title='Error',
        message="Error en la búsqueda"
      )
      return
    boton.config(state=tk.DISABLED)
  else:
    showinfo(
      title='Error',
      message="Error en la búsqueda"
    )
    return
  
def procesarMatriz():
  global matriz, x, y, paquetes
  contInicio=0
  for i in range (0,9):
    for j in range (0,9):
      if matriz[i][j]==2:
        contInicio+=1
        y=i
        x=j
      elif matriz[i][j]==4:
        paquetes+=1        
  
  if contInicio!=1 or paquetes<1:
    showinfo(title='Error',message="El laberinto seleccionado no es válido")
    exit()
    
    
