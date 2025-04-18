import tkinter as tk
from tkinter import filedialog
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
x = 0
y = 0
paquetes = 0

def selectFile(button, frame, cell_size, canvas, marcoBotones, grid):
    global matriz
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        archivo = True
        showinfo(
            title='Archivo seleccionado',
            message="Ha seleccionado el archivo " + file_path
        )
        matriz = gui.cargar_matriz(file_path)
        print(matriz)  # para depurar
        grid.matrix = matriz 
        grid.dibujar_cuadricula(canvas)
        marcoBotones.grid()
        button.config(state="disabled")
        procesarMatriz(matriz)
    else:
        showinfo(
            title='Error',
            message="No ha seleccionado ningún archivo"
        )

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

def buscar(op1, op2, boton, canvas, cell_size, grid):
    global tipoBusqueda, matriz, x, y, paquetes
    if tipoBusqueda == "noInformada":
        if op1.get() == "uniforme":
            expandidos, profundidad, tiempo, costo, ruta = costoUniforme.buscarSolucion(matriz, x, y, paquetes)
            camino = []
            for nodo in ruta:
                nombre = nodo[0] 
                fila, columna = map(int, nombre.strip("()").split(","))
                camino.append((fila, columna))
            
            print(f"Camino calculado: {camino}")
            animar_dron(canvas, matriz, camino, cell_size, grid.images, grid.labels)
            
            showinfo(
                title='Resultados',
                message=f"RESULTADOS DE LA BÚSQUEDA\n\nCantidad de nodos expandidos: {expandidos}\nProfundidad del árbol: {profundidad}\nTiempo de cómputo: {tiempo} ms\nCosto de la solución: {costo}\nRuta de la solución: {camino}"
            )
        elif op1.get() == "amplitud":
            camino = amplitud.buscarSolucion(matriz, x, y, paquetes)  # Devuelve lista de nodos
            animar_dron(canvas, matriz, camino, cell_size, grid.images, grid.labels)
            print(f"Camino calculado: {camino}")
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
    elif tipoBusqueda == "informada":
        if op2.get() == "avara":
            print("Avara")
            expandidos, profundidad, tiempo, costo, ruta = avara.buscarSolucion(matriz, x, y, paquetes)
            camino = []
            for nodo in ruta:
                nombre = nodo[0] 
                fila, columna = map(int, nombre.strip("()").split(","))
                camino.append((fila, columna))
            
            print(f"Camino calculado: {camino}")
            animar_dron(canvas, matriz, camino, cell_size, grid.images, grid.labels)
            
            showinfo(
                title='Resultados',
                message=f"RESULTADOS DE LA BÚSQUEDA\n\nCantidad de nodos expandidos: {expandidos}\nProfundidad del árbol: {profundidad}\nTiempo de cómputo: {tiempo} ms\nCosto de la solución: {costo}\nRuta de la solución: {camino}"
            )
        elif op2.get() == "aEstrella":
            print("A*")
            expandidos, profundidad, tiempo, costo, ruta = aEstrella.buscarSolucion(matriz, x, y, paquetes)
            camino = []
            for nodo in ruta:
                nombre = nodo[0] 
                fila, columna = map(int, nombre.strip("()").split(","))
                camino.append((fila, columna))
            
            print(f"Camino calculado: {camino}")
            animar_dron(canvas, matriz, camino, cell_size, grid.images, grid.labels)
            
            showinfo(
                title='Resultados',
                message=f"RESULTADOS DE LA BÚSQUEDA\n\nCantidad de nodos expandidos: {expandidos}\nProfundidad del árbol: {profundidad}\nTiempo de cómputo: {tiempo} ms\nCosto de la solución: {costo}\nRuta de la solución: {camino}"
            )
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

def procesarMatriz(matriz):
    global x, y, paquetes
    contInicio = 0
    paquetes = 0  # Reset package counter
    for i in range(10):
        for j in range(10):
            if matriz[i][j] == 2:
                contInicio += 1
                x = i
                y = j
            elif matriz[i][j] == 4:
                paquetes += 1

    if contInicio != 1 or paquetes < 1:
        showinfo(title='Error', message="El laberinto seleccionado no es válido")
        exit()

def animar_dron(canvas, matriz, camino, cell_size, images, labels):
    pos = 0

    def mover():
        nonlocal pos
        if pos < len(camino):
            fila, columna = camino[pos]

            # Restaurar la casilla anterior
            if pos > 0:
                fila_ant, col_ant = camino[pos - 1]
                labels[(fila_ant, col_ant)].config(image="", bg="red")
                if matriz[fila_ant][col_ant] == 3: 
                    casilla_ant = images[3]
                else:
                    casilla_ant = images[0] 
                if casilla_ant:  
                    labels[(fila_ant, col_ant)].config(image=casilla_ant)

            # Actualizar la posición actual del dron
            if pos == len(camino) - 1:  
                labels[(fila, columna)].config(image=images[2])  # Imagen del dron sobre el paquete
            else:
                labels[(fila, columna)].config(image=images[2])  # Dron en movimiento

            pos += 1
            canvas.after(500, mover) 
    mover()