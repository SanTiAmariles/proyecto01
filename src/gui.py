import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
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
        self.image_refs = []
        self.labels = {}

        # Colores
        self.colors = {
            0: "white",  # Casilla libre
            1: "grey",  # Obstáculo
        }
        # Imágenes
        assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets')
        self.images = {
            0: self.load_image(os.path.join(assets_path, "libre.png")),  
            1: self.load_image(os.path.join(assets_path, "muro2.png")),  
            2: self.load_image(os.path.join(assets_path, "dron2.png")),
            3: self.load_image(os.path.join(assets_path, "peligro3.png")),
            4: self.load_image(os.path.join(assets_path, "paquete.png")),
            5: self.load_image(os.path.join(assets_path, "fin.png"))
        }

    def load_image(self, path):
        try:
            image = Image.open(path)
            new_size = int(self.cell_size * 0.7)
            image = image.resize((new_size, new_size), Image.Resampling.LANCZOS)
            print(f"Imagen cargada correctamente: {path}")
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error al cargar la imagen {path}: {e}")
            return None
    
    def dibujar_cuadricula(self, canvas):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                cell_value = self.matrix[row][col]

                fill_color = self.colors.get(cell_value, "white")
                canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")

                if cell_value in self.images and self.images[cell_value]:
                    img = self.images[cell_value]
                    label = tk.Label(canvas, image=img)
                else:
                    label = tk.Label(canvas, bg=fill_color) 

                label.place(x=(x1 + x2) // 2, y=(y1 + y2) // 2, anchor=tk.CENTER)
                self.labels[(row, col)] = label 
                      
    
def gui():
    matrizInicial = [[0] * 10 for _ in range(10)]

    root = tk.Tk()
    root.title("Proyecto 1 Inteligencia Artificial")
    root.geometry("+100+0")

    marcoPrincipal = ttk.Frame(root)
    marcoPrincipal.grid(padx=20, pady=2)
 
    cell_size = 50
    grid_size = len(matrizInicial)
    canvas = tk.Canvas(marcoPrincipal, width=grid_size * cell_size, height=grid_size * cell_size)
    canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=2)
 
    grid = GridCuadricula(marcoPrincipal, matrizInicial, cell_size)
    grid.dibujar_cuadricula(canvas)
 
    bImportar = ttk.Button(marcoPrincipal, text="Importar archivo", command=lambda: funcionesGUI.selectFile(bImportar, marcoPrincipal, cell_size, canvas, marcoBotones, grid))
    bImportar.grid(row=0, column=0, columnspan=2, padx=10, pady=2)
 
    marcoBotones = ttk.Frame(marcoPrincipal)
    marcoBotones.grid(row=2, column=0, columnspan=2, padx=10, pady=2)
 
    bNoInformada = ttk.Button(marcoBotones, text="No Informada", command=lambda: funcionesGUI.noInformada(rbAmplitud, rbCostoUniforme, rbProfundidad, rbAvara, rbAEstrella, bBuscar))
    bNoInformada.grid(row=0, column=0, padx=10, pady=10)
    bInformada = ttk.Button(marcoBotones, text="Informada", command=lambda: funcionesGUI.informada(rbAmplitud, rbCostoUniforme, rbProfundidad, rbAvara, rbAEstrella, bBuscar))
    bInformada.grid(row=0, column=1, padx=10, pady=10)
 
    opcionNoInformada = tk.StringVar(value="amplitud")
    rbAmplitud = tk.Radiobutton(marcoBotones, text="Amplitud", variable=opcionNoInformada, value="amplitud", state="disabled")
    rbCostoUniforme = tk.Radiobutton(marcoBotones, text="Costo Uniforme", variable=opcionNoInformada, value="costo", state="disabled")
    rbProfundidad = tk.Radiobutton(marcoBotones, text="Profundidad evitando ciclos", variable=opcionNoInformada, value="profundidad", state="disabled")
    rbAmplitud.grid(row=1, column=0, sticky="w", padx=10, pady=2)
    rbCostoUniforme.grid(row=2, column=0, sticky="w", padx=10, pady=2)
    rbProfundidad.grid(row=3, column=0, sticky="w", padx=10, pady=2)
 
    opcionInformada = tk.StringVar(value="avara")
    rbAvara = tk.Radiobutton(marcoBotones, text="Avara", variable=opcionInformada, value="avara", state="disabled")
    rbAEstrella = tk.Radiobutton(marcoBotones, text="A*", variable=opcionInformada, value="aEstrella", state="disabled")
    rbAvara.grid(row=1, column=1, sticky="w", padx=10, pady=2)
    rbAEstrella.grid(row=2, column=1, sticky="w", padx=10, pady=2)
 
    bBuscar = ttk.Button(marcoBotones, text="Buscar Solución", command=lambda: funcionesGUI.buscar(opcionNoInformada, opcionInformada, bBuscar, canvas, cell_size, grid), state="disabled")
    bBuscar.grid(row=4, column=0, columnspan=2, padx=10, pady=2)

    marcoBotones.grid_remove()

    root.mainloop()

if __name__ == "__main__":
    gui()