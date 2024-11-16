# IMPORTACION DE LAS LIBRERIAS UTILIZADAS
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# CREACION DE LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Generico")
root.geometry("400x300")

# AGREGAR UN ICONO A LA APLICACION
icon_path = "assets/generico.png"
icon_img = ImageTk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_img)

# FRAME QUE CONTENDRA LAS HERRAMIENTAS
toolbar = ttk.Frame(root, relief="raised", padding=(10, 3))
toolbar.pack(side="top", fill="x")

# DEFINICION DE LA CARPETA DE ASSETS
icon_path = "assets"

# LISTA CON LOS ICONOS
icons = ["icon1.png", "icon2.png", "icon3.png"]

# SE AGREGAN LOS ICONOS EN LA BARRA
for icon in icons:
    img = Image.open(os.path.join(icon_path, icon))
    img = img.resize((20, 20), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    btn = ttk.Button(toolbar, image=img)
    btn.image = img
    btn.pack(side="left", padx=2, pady=2)

# EJECUTAR LA APLICACION
root.mainloop()