import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import gui
from no_informada import amplitud


archivo = False

def selectFile(boton,marcoPrincipal, cell_size,canvas):
  global archivo
  matriz = []
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
  
def noInformada():
  print("No informada")
  
def informada():
  print("Informada")

def buscar():
  print("Buscar")
  
    
