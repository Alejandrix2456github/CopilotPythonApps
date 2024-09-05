import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def iniciar_sesion():
    global remitente, contrasena
    remitente = simpledialog.askstring("Inicio de Sesión", "Ingrese su correo electrónico:")
    contrasena = simpledialog.askstring("Inicio de Sesión", "Ingrese su contraseña:", show='*')
    if remitente and contrasena:
        login_window.destroy()
        root.deiconify()
    else:
        messagebox.showerror("Error", "Debe ingresar su correo y contraseña")

def enviar_correo():
    destinatario = simpledialog.askstring("Destinatario", "Ingrese el correo del destinatario:")
    asunto = simpledialog.askstring("Asunto", "Ingrese el asunto del correo:")
    mensaje = simpledialog.askstring("Mensaje", "Ingrese el mensaje del correo:")

    if destinatario and asunto and mensaje:
        try:
            msg = MIMEMultipart()
            msg['From'] = remitente
            msg['To'] = destinatario
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(remitente, contrasena)
            text = msg.as_string()
            server.sendmail(remitente, destinatario, text)
            server.quit()

            messagebox.showinfo("Éxito", "Correo enviado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")

def cambiar_tema():
    tema = simpledialog.askstring("Tema", "Ingrese el nombre del tema (claro/oscuro):")
    if tema == "oscuro":
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white")
    elif tema == "claro":
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")
    else:
        messagebox.showwarning("Advertencia", "Tema no reconocido")

root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal hasta que se inicie sesión

login_window = tk.Toplevel()
login_window.title("Inicio de Sesión")
login_label = tk.Label(login_window, text="Inicie sesión para continuar")
login_label.pack(pady=10)
login_button = tk.Button(login_window, text="Iniciar Sesión", command=iniciar_sesion)
login_button.pack(pady=10)

root.deiconify()  # Mostrar la ventana principal después de iniciar sesión
root.title("Cliente de Correo Electrónico")

# Crear la barra de navegación
nav_frame = tk.Frame(root, bg="lightgray")
nav_frame.pack(side="left", fill="y")

inbox_button = tk.Button(nav_frame, text="Bandeja de Entrada", command=lambda: messagebox.showinfo("Bandeja de Entrada", "Mostrando bandeja de entrada"))
inbox_button.pack(fill="x")

sent_button = tk.Button(nav_frame, text="Enviados", command=lambda: messagebox.showinfo("Enviados", "Mostrando correos enviados"))
sent_button.pack(fill="x")

drafts_button = tk.Button(nav_frame, text="Borradores", command=lambda: messagebox.showinfo("Borradores", "Mostrando borradores"))
drafts_button.pack(fill="x")

# Crear la lista de correos
email_list_frame = tk.Frame(root)
email_list_frame.pack(side="left", fill="both", expand=True)

email_list = tk.Listbox(email_list_frame)
email_list.pack(fill="both", expand=True)

# Crear los botones de acción
action_frame = tk.Frame(root)
action_frame.pack(side="bottom", fill="x")

boton_enviar = tk.Button(action_frame, text="Enviar Correo", command=enviar_correo)
boton_enviar.pack(side="left", padx=5, pady=5)

boton_tema = tk.Button(action_frame, text="Cambiar Tema", command=cambiar_tema)
boton_tema.pack(side="left", padx=5, pady=5)

root.mainloop()
