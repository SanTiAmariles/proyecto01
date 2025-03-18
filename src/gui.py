import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk  # Para manejar imágenes

def cargar_matriz(archivo):
    with open(archivo, "r") as f:
        return [list(map(int, line.split())) for line in f]

class GridCuadricula:
    def __init__(self, root, matrix, cell_size=50):
        self.root = root
        self.matrix = matrix
        self.cell_size = cell_size
        self.grid_size = len(matrix)

        # imágenes
        self.images = {
            2: self.load_image(r"C:\Users\Asus\Downloads\proyecto01\assets\dron3.png"),
            3: self.load_image(r"C:\Users\Asus\Downloads\proyecto01\assets\peligro.png"),
            4: self.load_image(r"C:\Users\Asus\Downloads\proyecto01\assets\paquete.png"),
        }

    def load_image(self, path):
        """Carga y redimensiona una imagen."""
        image = Image.open(path)
        new_size = int(self.cell_size * 0.7)
        image = image.resize((new_size, new_size), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    def dibujar_cuadricula(self, canvas):
        for row in range(self.grid_size):
          for col in range(self.grid_size):
            x1, y1 = col * self.cell_size, row * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size

            cell_value = self.matrix[row][col]

            # Dibujar siempre el borde negro de la celda
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")

            if cell_value in self.images:
                canvas.create_image((x1 + x2) // 2, (y1 + y2) // 2, anchor=tk.CENTER, image=self.images[cell_value])
            else:
                fill_color = "white" if cell_value == 0 else "grey"
                canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")

def gui():
    ruta = os.path.join("src", "matriz.txt")
    matriz = cargar_matriz(ruta)

    root = tk.Tk()
    root.title("Proyecto 1 Inteligencia Artificial")

    # Crear marco principal
    marcoPrincipal = ttk.Frame(root)
    marcoPrincipal.pack(padx=20, pady=20)

    # Crear el botón de Importar
    bImportar = ttk.Button(marcoPrincipal, text="Importar archivo", command=lambda: funcionesGUI.selectFile(bImportar))
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
    grid = GridCuadricula(marcoPrincipal, matriz, cell_size)
    grid.dibujar_cuadricula(canvas)

    root.mainloop()

if __name__ == "__main__":
    gui()