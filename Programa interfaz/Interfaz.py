import tkinter as tk
from tkinter import filedialog, messagebox
#from PIL import Image, ImageTk  # Necesitas instalar pillow: pip install pillow

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi Interfaz con Botones")
ventana.geometry("500x500")  # tamaño de la ventana

# Función para mostrar un saludo
def saludo():
    messagebox.showinfo("Saludo", "¡Hola! Bienvenido a la interfaz.")

# Función para abrir y mostrar imagen
def seleccionar_imagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if ruta:
        messagebox.showinfo("Archivo seleccionado", f"Seleccionaste: {ruta}")
        # Abrir y redimensionar la imagen
       # imagen = Image.open(ruta)
        imagen = imagen.resize((300, 300))
        #imagen_tk = ImageTk.PhotoImage(imagen)
       # etiqueta_imagen.config(image=imagen_tk)
       # etiqueta_imagen.image = imagen_tk  # guardar referencia para que no se borre

# Botón para saludo
btn_saludo = tk.Button(ventana, text="Saludar", command=saludo, width=20, height=2)
btn_saludo.pack(pady=10)

# Botón para seleccionar imagen
btn_imagen = tk.Button(ventana, text="Seleccionar Imagen", command=seleccionar_imagen, width=20, height=2)
btn_imagen.pack(pady=10)

# Etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
etiqueta_imagen.config(image=imagen_tk)
etiqueta_imagen.image = imagen_tk

