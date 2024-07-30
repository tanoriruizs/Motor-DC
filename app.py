from tkinter import *
from PIL import Image, ImageTk
import serial
import time

# Configurar la conexión serial con el Arduino
arduino = serial.Serial('COM4', 9600)  # Cambia 'COM3' al puerto correspondiente en tu sistema
time.sleep(2)  # Esperar a que la conexión se establezca

def enviar_comando(comando):
    arduino.write(comando.encode())
    time.sleep(0.1)  # Pequeña pausa para asegurar la transmisión

def girarizquierda():
    boton1.config(state=DISABLED)
    boton2.config(state=NORMAL)
    boton3.config(state=NORMAL)
    mensaje.config(image=giroizquierda)
    mensaje_texto.config(text="Girando a la izquierda")
    enviar_comando('i')

def detenermotor():
    boton1.config(state=NORMAL)
    boton2.config(state=DISABLED)
    boton3.config(state=NORMAL)
    mensaje.config(image=motorparado)
    mensaje_texto.config(text="Motor detenido")
    enviar_comando('p')

def girarderecha():
    boton1.config(state=NORMAL)
    boton2.config(state=NORMAL)
    boton3.config(state=DISABLED)
    mensaje.config(image=giroderecha)
    mensaje_texto.config(text="Girando a la derecha")
    enviar_comando('d')

ventana = Tk()
ventana.title("Control del Motor de Corriente Directa")

# Configurar la ventana para que se ajuste al contenido
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Cargar imágenes
giroizquierda = ImageTk.PhotoImage(Image.open("giroalaizquierda.gif"))
motorparado = ImageTk.PhotoImage(Image.open("motorparado.jpg"))
giroderecha = ImageTk.PhotoImage(Image.open("giroaladerecha.gif"))
izquierda = ImageTk.PhotoImage(Image.open("flechaizquierda.png"))
detener = ImageTk.PhotoImage(Image.open("detener.jpg"))
derecha = ImageTk.PhotoImage(Image.open("flechaderecha.png"))

# Crear marco para los botones
frame_botones = Frame(ventana, bg="lightgrey")
frame_botones.grid(row=0, column=0, pady=20)

# Crear botones
boton1 = Button(frame_botones, image=izquierda, bg="green", command=girarizquierda, borderwidth=2)
boton2 = Button(frame_botones, image=detener, bg="red", state=DISABLED, command=detenermotor, borderwidth=2)
boton3 = Button(frame_botones, image=derecha, bg="blue", command=girarderecha, borderwidth=2)

# Posicionar botones
boton1.grid(row=0, column=0, padx=20, pady=10)
boton2.grid(row=0, column=1, padx=20, pady=10)
boton3.grid(row=0, column=2, padx=20, pady=10)

# Crear etiquetas descriptivas
label1 = Label(frame_botones, text="Girar Izquierda", bg="lightgrey")
label2 = Label(frame_botones, text="Detener Motor", bg="lightgrey")
label3 = Label(frame_botones, text="Girar Derecha", bg="lightgrey")

# Posicionar etiquetas
label1.grid(row=1, column=0, padx=20, pady=5)
label2.grid(row=1, column=1, padx=20, pady=5)
label3.grid(row=1, column=2, padx=20, pady=5)

# Crear y posicionar mensaje
mensaje = Label(ventana, image=motorparado, bg="lightgrey")
mensaje.grid(row=1, column=0, pady=20)

# Crear y posicionar mensaje de texto
mensaje_texto = Label(ventana, text="Motor detenido", font=("Helvetica", 16), bg="lightgrey")
mensaje_texto.grid(row=2, column=0, pady=10)

# Ajustar la ventana al contenido
ventana.update_idletasks()
ventana.geometry(f"{ventana.winfo_reqwidth()}x{ventana.winfo_reqheight()}+{ventana.winfo_x()}+{ventana.winfo_y()}")

# Iniciar el loop de la ventana
ventana.mainloop()

# Cerrar la conexión serial al cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", lambda: [arduino.close(), ventana.destroy()])
