import tkinter as tk

def cargar_matriz(archivo):
    with open(archivo, "r") as f:
        return [list(map(int, line.split())) for line in f]

class GridCuadricula:
    def __init__(self, root, matrix, cell_size=50):
        self.root = root
        self.matrix = matrix
        self.cell_size = cell_size
        self.grid_size = len(matrix)  

        #cuadrícula
        self.canvas = tk.Canvas(root, width=self.grid_size * cell_size, height=self.grid_size * cell_size)
        self.canvas.pack()

        # colores
        self.colors = {
            0: "white",   # Casilla libre
            1: "grey",    # Obstáculo
            2: "blue",    # Inicio del dron
            3: "orange",  # Campo electromagnético
            4: "green"    # Paquete
        }

        self.dibujar_cuadricula()
        

    def dibujar_cuadricula(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                
                fill_color = self.colors.get(self.matrix[row][col], "white")
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")

if __name__ == "__main__":
    matriz = cargar_matriz(r"C:\Users\sheil\OneDrive\Escritorio\proyecto01\src\matriz.txt")

    root = tk.Tk()
    app = GridCuadricula(root, matriz)
    root.mainloop()




