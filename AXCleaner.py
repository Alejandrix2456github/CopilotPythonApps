import os
import shutil
import tkinter as tk
from tkinter import messagebox

def limpiar_temp():
    temp_folder = os.getenv('TEMP')
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"No se pudo eliminar {file}: {e}")
    messagebox.showinfo("Limpieza", "Archivos temporales eliminados")

def limpiar_prefetch():
    prefetch_folder = os.path.join(os.getenv('SYSTEMROOT'), 'Prefetch')
    for root, dirs, files in os.walk(prefetch_folder):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"No se pudo eliminar {file}: {e}")
    messagebox.showinfo("Limpieza", "Archivos Prefetch eliminados")

def limpiar_recycle_bin():
    recycle_bin = os.path.join(os.getenv('SYSTEMDRIVE'), '$Recycle.Bin')
    for root, dirs, files in os.walk(recycle_bin):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"No se pudo eliminar {file}: {e}")
    messagebox.showinfo("Limpieza", "Papelera de reciclaje vaciada")

root = tk.Tk()
root.title("Limpiador de Disco")

label = tk.Label(root, text="Limpiador de Disco Duro")
label.pack(pady=10)

boton_temp = tk.Button(root, text="Limpiar Archivos Temporales", command=limpiar_temp)
boton_temp.pack(pady=10)

boton_prefetch = tk.Button(root, text="Limpiar Archivos Prefetch", command=limpiar_prefetch)
boton_prefetch.pack(pady=10)

boton_recycle_bin = tk.Button(root, text="Vaciar Papelera de Reciclaje", command=limpiar_recycle_bin)
boton_recycle_bin.pack(pady=10)

root.mainloop()
