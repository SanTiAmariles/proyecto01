import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import gui
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from no_informada import amplitud, costoUniforme, profundidad
from informada import aEstrella, avara


archivo = False
tipoBusqueda = ""
matriz = []

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
    with open(filename, "r", encoding="utf-8") as entrada:
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
      amplitud.crearCola(matriz,2,1,3)
      print("Amplitud")
    elif op1.get() == "uniforme":
      print("Uniforme")
    elif op1.get() == "profundidad":
      print("Profundidad")
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
    elif op2.get() == "aEstrella":
      print("A*")
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
  
    
