import os
import tkinter as tk
from tkinter import messagebox

def formatear_usb():
    # Aquí puedes agregar la lógica para formatear el USB
    messagebox.showinfo("Formatear", "USB formateado")

def copiar_archivos():
    # Aquí puedes agregar la lógica para copiar archivos al USB
    messagebox.showinfo("Copiar", "Archivos copiados al USB")

def verificar_espacio():
    # Aquí puedes agregar la lógica para verificar el espacio disponible en el USB
    messagebox.showinfo("Espacio", "Espacio disponible verificado")

root = tk.Tk()
root.title("Utilidades USB")

label = tk.Label(root, text="Utilidades USB")
label.pack(pady=10)

boton_formatear = tk.Button(root, text="Formatear USB", command=formatear_usb)
boton_formatear.pack(pady=10)

boton_copiar = tk.Button(root, text="Copiar Archivos", command=copiar_archivos)
boton_copiar.pack(pady=10)

boton_verificar = tk.Button(root, text="Verificar Espacio", command=verificar_espacio)
boton_verificar.pack(pady=10)

def formatear_usb():
    # Ejemplo de comando para formatear (esto puede variar según el sistema operativo)
    os.system('mkfs -t vfat /dev/sdX1')
    messagebox.showinfo("Formatear", "USB formateado")

def copiar_archivos():
    origen = '/ruta/al/archivo'
    destino = '/ruta/al/usb'
    try:
        shutil.copy(origen, destino)
        messagebox.showinfo("Copiar", "Archivos copiados al USB")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo copiar el archivo: {e}")
def verificar_espacio():
    statvfs = os.statvfs('E:')
    espacio_disponible = statvfs.f_frsize * statvfs.f_bavail
    messagebox.showinfo("Espacio", f"Espacio disponible: {espacio_disponible / (1024 * 1024)} MB")


root.mainloop()
