import tkinter as tk
from tkinter import ttk
import database

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Mapas")
        
        frame = ttk.LabelFrame(root, text="Agregar nuevo mapa")
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(frame, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(frame, text="Año:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(frame, text="Ubicación:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(frame, text="Notas:").grid(row=4, column=0, padx=5, pady=5)

        self.nombre = ttk.Entry(frame)
        self.tipo = ttk.Entry(frame)
        self.año = ttk.Entry(frame)
        self.ubicación = ttk.Entry(frame)
        self.notas = ttk.Entry(frame)

        self.nombre.grid(row=0, column=1)
        self.tipo.grid(row=1, column=1)
        self.año.grid(row=2, column=1)
        self.ubicación.grid(row=3, column=1)
        self.notas.grid(row=4, column=1)

        ttk.Button(frame, text="Agregar", command=self.agregar_mapa).grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_mapa(self):
        nombre = self.nombre.get()
        tipo = self.tipo.get()
        año = self.año.get()
        ubicación = self.ubicación.get()
        notas = self.notas.get()

        database.agregar_mapa(nombre, tipo, año, ubicación, notas)
        self.cargar_tabla()
        self.nombre.delete(0, tk.END)
        self.tipo.delete(0, tk.END)
        self.año.delete(0, tk.END)
        self.ubicación.delete(0, tk.END)
        self.notas.delete(0, tk.END)

