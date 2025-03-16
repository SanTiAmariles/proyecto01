import tkinter as tk
from tkinter import ttk
import os
import funcionesGUI


def cargar_matriz(archivo):
	with open(archivo, "r") as f:
		return [list(map(int, line.split())) for line in f]


class GridCuadricula:
	def __init__(self, root, matrix, cell_size=50):
		self.root = root
		self.matrix = matrix
		self.cell_size = cell_size
		self.grid_size = len(matrix)

		# colores
		self.colors = {
			0: "white",  # Casilla libre
			1: "grey",  # Obstáculo
			2: "blue",  # Inicio del dron
			3: "orange",  # Campo electromagnético
			4: "green",  # Paquete
		}

	def dibujar_cuadricula(self, canvas):
		for row in range(self.grid_size):
			for col in range(self.grid_size):
				x1, y1 = col * self.cell_size, row * self.cell_size
				x2, y2 = x1 + self.cell_size, y1 + self.cell_size

				fill_color = self.colors.get(self.matrix[row][col], "white")

				canvas.create_rectangle(
					x1, y1, x2, y2, fill=fill_color, outline="black"
				)
    
def gui():
    
	#ruta = os.path.join("src", "matriz.txt")
	#matriz = cargar_matriz(ruta)
	matrizInicial = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

	root = tk.Tk()
	root.title("Proyecto 1 Inteligencia Artificial")

	#Crear marco principal
	marcoPrincipal = ttk.Frame(root)
	marcoPrincipal.grid(padx=20, pady=2)
 
	#Crear el botón de Importar
	bImportar = ttk.Button(marcoPrincipal, text="Importar archivo", command=lambda: funcionesGUI.selectFile(bImportar,marcoPrincipal, cell_size, canvas, marcoBotones))
	bImportar.grid(row=0, column=0, columnspan=2, padx=10, pady=2)
 
	# Crear un Frame para contener el canvas
	frame = ttk.Frame(marcoPrincipal)
	frame.grid(row=1, column=0, columnspan=2, padx=10, pady=2)	
 
	# Crear el canvas dentro del Frame
	cell_size = 50
	grid_size = len(matrizInicial)
	canvas = tk.Canvas(frame, width=grid_size * cell_size, height=grid_size * cell_size)
	canvas.grid()
 
	# Dibujar la cuadrícula
	grid = GridCuadricula(marcoPrincipal, matrizInicial, cell_size)
	grid.dibujar_cuadricula(canvas)
 
	# Contenedor de botones en dos columnas
	marcoBotones = ttk.Frame(marcoPrincipal)
	marcoBotones.grid(row=2, column=0, columnspan=2, padx=10, pady=2)
 
	#Crear Botones Tipo de Búsqueda
	bNoInformada = ttk.Button(marcoBotones, text="No Informada", command=lambda: funcionesGUI.noInformada(rbAmplitud, rbCostoUniforme, rbProfundidad, rbAvara, rbAEstrella, bBuscar))
	bNoInformada.grid(row=0, column=0, padx=10, pady=10)
	bInformada = ttk.Button(marcoBotones, text="Informada", command=lambda: funcionesGUI.informada(rbAmplitud, rbCostoUniforme, rbProfundidad, rbAvara, rbAEstrella, bBuscar))
	bInformada.grid(row=0, column=1, padx=10, pady=10)
 
	#Crear Radio Buttons No Informada
	opcionNoInformada = tk.StringVar(value="amplitud")
	rbAmplitud = tk.Radiobutton(marcoBotones, text="Amplitud", variable=opcionNoInformada, value="amplitud", state="disabled")
	rbCostoUniforme = tk.Radiobutton(marcoBotones, text="Costo Uniforme", variable=opcionNoInformada, value="uniforme", state="disabled")
	rbProfundidad = tk.Radiobutton(marcoBotones, text="Profundidad evitando ciclos", variable=opcionNoInformada, value="profundidad", state="disabled")
	rbAmplitud.grid(row=1, column=0, sticky="w", padx=10, pady=2)
	rbCostoUniforme.grid(row=2, column=0, sticky="w", padx=10, pady=2)
	rbProfundidad.grid(row=3, column=0, sticky="w", padx=10, pady=2)
 
	#Crear Radio Buttons Informada
	opcionInformada = tk.StringVar(value="avara")
	rbAvara = tk.Radiobutton(marcoBotones, text="Avara", variable=opcionInformada, value="avara", state="disabled")
	rbAEstrella = tk.Radiobutton(marcoBotones, text="A*", variable=opcionInformada, value="aEstrella", state="disabled")
	rbAvara.grid(row=1, column=1, sticky="w", padx=10, pady=2)
	rbAEstrella.grid(row=2, column=1, sticky="w", padx=10, pady=2)
 
	#Crear botón búsqueda
	bBuscar = ttk.Button(marcoBotones, text="Buscar Solución", command=lambda: funcionesGUI.buscar(opcionNoInformada, opcionInformada, bBuscar), state="disabled")
	bBuscar.grid(row=4, column=0, columnspan=2, padx=10, pady=2)

	marcoBotones.grid_remove()

	root.mainloop()


if __name__ == "__main__":
	gui()
