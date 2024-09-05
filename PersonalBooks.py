import tkinter as tk
from tkinter import messagebox, Menu, ttk
from ttkthemes import ThemedTk
import sqlite3
import http.client
import json
from PIL import Image, ImageTk
import io
import os

# Conexión a la base de datos
conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

# Crear tablas
c.execute('''CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                autor TEXT,
                isbn TEXT)''')

conn.commit()

# Función para agregar un libro
def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    isbn = entry_isbn.get()
    c.execute("INSERT INTO libros (titulo, autor, isbn) VALUES (?, ?, ?)", (titulo, autor, isbn))
    conn.commit()
    messagebox.showinfo("Éxito", "Libro agregado exitosamente")
    mostrar_libros()

# Función para mostrar libros
def mostrar_libros():
    for row in tree.get_children():
        tree.delete(row)
    c.execute("SELECT * FROM libros")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Función para buscar libros en Google Books usando http.client
def buscar_google_books():
    isbn = entry_isbn.get()
    if isbn:
        try:
            conn = http.client.HTTPSConnection("www.googleapis.com")
            conn.request("GET", f"/books/v1/volumes?q=isbn:{isbn}")
            response = conn.getresponse()
            if response.status == 200:
                data = json.loads(response.read().decode())
                if 'items' in data:
                    libro = data['items'][0]['volumeInfo']
                    titulo = libro.get('title', 'N/A')
                    autor = ', '.join(libro.get('authors', 'N/A'))
                    imagen_url = libro.get('imageLinks', {}).get('thumbnail', '')
                    mostrar_informacion_libro(titulo, autor, imagen_url)
                else:
                    messagebox.showinfo("Información del Libro", "No se encontró información para este ISBN.")
            else:
                messagebox.showerror("Error", f"Error en la solicitud: {response.status}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar a Google Books: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un ISBN.")

# Función para mostrar información del libro
def mostrar_informacion_libro(titulo, autor, imagen_url):
    info_text.set(f"Título: {titulo}\nAutor: {autor}")
    if imagen_url:
        try:
            conn = http.client.HTTPSConnection("books.google.com")
            conn.request("GET", imagen_url)
            response = conn.getresponse()
            if response.status == 200:
                image_data = response.read()
                image = Image.open(io.BytesIO(image_data))
                image.thumbnail((150, 200))
                photo = ImageTk.PhotoImage(image)
                label_imagen.config(image=photo)
                label_imagen.image = photo
            else:
                label_imagen.config(image='')
                label_imagen.image = None
        except Exception as e:
            label_imagen.config(image='')
            label_imagen.image = None
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Interfaz gráfica
root = ThemedTk(theme="equilux")
root.title("PersonalBooks")

# Cargar imagen de inicio
def cargar_imagen_inicio():
    try:
        ruta_imagen = os.path.abspath("C:/Usuarios/TuUsuario/Documentos/PersonalBooks.png")  # Ruta absoluta
        image = Image.open(ruta_imagen)
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label_imagen_inicio.config(image=photo)
        label_imagen_inicio.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen de inicio: {e}")

# Función para ocultar la imagen de inicio y mostrar el programa
def iniciar_programa():
    label_imagen_inicio.pack_forget()
    tab_control.pack(expand=1, fill='both')

# Menú
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Salir", command=root.quit)

libros_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Libros", menu=libros_menu)
libros_menu.add_command(label="Mostrar Libros", command=mostrar_libros)

# Pestañas
tab_control = ttk.Notebook(root)
tab_libros = ttk.Frame(tab_control)
tab_mi_biblioteca = ttk.Frame(tab_control)
tab_control.add(tab_libros, text='Libros')
tab_control.add(tab_mi_biblioteca, text='Mi Biblioteca Personal')

# Marco para la entrada de datos
frame_entrada = ttk.LabelFrame(tab_libros, text="Agregar/Buscar Libro")
frame_entrada.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(frame_entrada, text="Título").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(frame_entrada, text="Autor").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(frame_entrada, text="ISBN").grid(row=2, column=0, padx=5, pady=5)

entry_titulo = ttk.Entry(frame_entrada)
entry_autor = ttk.Entry(frame_entrada)
entry_isbn = ttk.Entry(frame_entrada)

entry_titulo.grid(row=0, column=1, padx=5, pady=5)
entry_autor.grid(row=1, column=1, padx=5, pady=5)
entry_isbn.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame_entrada, text="Agregar Libro", command=agregar_libro).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(frame_entrada, text="Buscar en Google Books", command=buscar_google_books).grid(row=3, column=1, padx=5, pady=5)

# Tabla de libros
frame_tabla = ttk.LabelFrame(tab_libros, text="Lista de Libros")
frame_tabla.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

tree = ttk.Treeview(frame_tabla, columns=("ID", "Título", "Autor", "ISBN"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Título", text="Título")
tree.heading("Autor", text="Autor")
tree.heading("ISBN", text="ISBN")
tree.pack(expand=True, fill='both')

# Información del libro
frame_info = ttk.LabelFrame(tab_libros, text="Información del Libro")
frame_info.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

info_text = tk.StringVar()
label_info = ttk.Label(frame_info, textvariable=info_text)
label_info.grid(row=0, column=0, padx=5, pady=5)

# Imagen del libro
label_imagen = ttk.Label(frame_info)
label_imagen.grid(row=1, column=0, padx=5, pady=5)

# Imagen de inicio
label_imagen_inicio = ttk.Label(root)
label_imagen_inicio.pack(pady=10)

# Cargar imagen de inicio al abrir el programa
cargar_imagen_inicio()

# Ocultar la imagen de inicio y mostrar el programa después de 3 segundos
root.after(3000, iniciar_programa)

# Pestaña de Mi Biblioteca Personal
ttk.Label(tab_mi_biblioteca, text="Aquí puedes gestionar tu biblioteca personal.").pack(padx=10, pady=10)

root.mainloop()
