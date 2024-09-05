import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para abrir un directorio
def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        listbox.delete(0, tk.END)
        for file_name in os.listdir(directory):
            listbox.insert(tk.END, file_name)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Explorador de Archivos")
root.geometry('700x500')

# Crear el Listbox y Scrollbar
scroll_bar = tk.Scrollbar(root)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scroll_bar.set)
listbox.pack(fill=tk.BOTH, expand=True)

scroll_bar.config(command=listbox.yview)

# Crear el botón para abrir un directorio
button_open = tk.Button(root, text="Abrir Directorio", command=open_directory)
button_open.pack()

root.mainloop()
