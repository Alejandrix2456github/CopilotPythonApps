import tkinter as tk
from tkinter import messagebox
import http.client
from bs4 import BeautifulSoup # type: ignore

def extraer_datos(url):
    try:
        if url.startswith("http://"):
            url = url[7:]
        elif url.startswith("https://"):
            url = url[8:]
        
        host, path = url.split("/", 1)
        path = "/" + path

        conn = http.client.HTTPConnection(host)
        conn.request("GET", path)
        response = conn.getresponse()

        if response.status == 200:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            titulos = soup.find_all('h2')

            resultado = "\n".join([titulo.text for titulo in titulos])
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showerror("Error", f"Error al obtener la página: {response.status} {response.reason}")

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def iniciar_scraping():
    url = entrada_url.get()
    if url:
        extraer_datos(url)
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Web Scraper")

# Crear y colocar los widgets
etiqueta_url = tk.Label(ventana, text="Introduce la URL de la página web:")
etiqueta_url.pack(pady=5)

entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(pady=5)

boton_scrapear = tk.Button(ventana, text="Iniciar Scraping", command=iniciar_scraping)
boton_scrapear.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
