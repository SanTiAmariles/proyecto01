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
    
	ruta = os.path.join("src", "matriz.txt")
	matriz = cargar_matriz(ruta)

	root = tk.Tk()
	root.title("Proyecto 1 Inteligencia Artificial")

	#Crear marco principal
	marcoPrincipal = ttk.Frame(root)
	marcoPrincipal.pack(padx=20, pady=20)
 
	#Crear el botón de Importar
	bImportar = ttk.Button(marcoPrincipal, text="Importar archivo", command=lambda: funcionesGUI.selectFile(bImportar,marcoPrincipal, cell_size, canvas))
	bImportar.pack(padx=10, pady=10)
 
	# Crear un Frame para contener el canvas
	frame = ttk.Frame(marcoPrincipal)
	frame.pack(padx=10, pady=10) 	
 
	# Crear el canvas dentro del Frame
	cell_size = 50
	grid_size = len(matriz)
	canvas = tk.Canvas(frame, width=grid_size * cell_size, height=grid_size * cell_size)
	canvas.pack()
 
	# Dibujar la cuadrícula
	matrizInicial = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	grid = GridCuadricula(marcoPrincipal, matrizInicial, cell_size)
	grid.dibujar_cuadricula(canvas)
 
	#Crear Botones Tipo de Búsqueda
	bNoInformada = ttk.Button(marcoPrincipal, text="No Informada", command=lambda: funcionesGUI.noInformada())
	bNoInformada.pack(padx=10, pady=10)
	bInformada = ttk.Button(marcoPrincipal, text="No Informada", command=lambda: funcionesGUI.noInformada())
	
 
	#Crear Radio Buttons No Informada
	opcionNoInformada = tk.StringVar(value="amplitud")
	rbAmplitud = tk.Radiobutton(marcoPrincipal, text="Amplitud", variable=opcionNoInformada, value="amplitud")
	rbCostoUniforme = tk.Radiobutton(marcoPrincipal, text="Costo Uniforme", variable=opcionNoInformada, value="uniforme")
	rbProfundidad = tk.Radiobutton(marcoPrincipal, text="Profundidad evitando ciclos", variable=opcionNoInformada, value="profundidad")
	rbAmplitud.pack(padx=10, pady=10)
	rbCostoUniforme.pack(padx=10, pady=10)
	rbProfundidad.pack(padx=10, pady=10)
 
	#Crear Radio Buttons Informada
	bInformada.pack(padx=10, pady=10)
	opcionInformada = tk.StringVar(value="avara")
	rbAvara = tk.Radiobutton(marcoPrincipal, text="Avara", variable=opcionInformada, value="avara")
	rbAEstrella = tk.Radiobutton(marcoPrincipal, text="A*", variable=opcionInformada, value="aEstrella")
	rbAvara.pack(padx=10, pady=10)
	rbAEstrella.pack(padx=10, pady=10)
 
	#Crear botón búsqueda
	bBuscar = ttk.Button(marcoPrincipal, text="Buscar Solución", command=lambda: funcionesGUI.buscar())
	bBuscar.pack(padx=10, pady=10)

	root.mainloop()


if __name__ == "__main__":
	gui()
