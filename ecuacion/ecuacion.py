#improto la libreria tkinter con el alias tk
from cgitb import text
from email import message
import tkinter as tk
from tkinter import IntVar, messagebox
import estilos 

#variables globales

#funciones operaciones
def calcular():
    messagebox.showinfo("programa 1" , "Se esta calculando los datos de la ecuacion")
    r = x.get() + y.get()
    at_resultados.insert(tk.INSERT,"suma: " + str(r) + "\n")

def borrar():
     messagebox.showinfo("programa 1" , "Se borraran los datos de las operaciones")
     x.set(0)
     y.set(0)
     at_resultados.delete("1.0","end")

def salir():
   messagebox.showinfo("programa 1" , "Ya usaste esta app")
   ventana_principal.destroy()

#creacion objeto tk,ventana_principal
ventana_principal = tk.Tk()

#titulo de la ventana principal
ventana_principal.title("Arnold aguancha")

#deshabilitar boton principal maximizar
ventana_principal.resizable(0,0)

#dimensiones ventana
#ventana_principal.geometry("500x500")

#color fondo ventan
ventana_principal.config(bg="white")

# icono de la ventana
#ventana_principal.iconbitmap("icono.ico")

#---------------------
#variables - globales
#---------------------
x= tk.IntVar()
y= tk.IntVar()

"""AGREGAMOS FRAMES A LA VENTANA PRINCIPAL"""

#FRAMDE DE ENTRADA DE DATOS

frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg=estilos.COLOR_FONDO_FRAMES1, width=480,height=200)
frame_entrada.pack(fill=tk.BOTH, padx=10, pady=10 )

#etiqueta de texto  (Label)
titulo = tk.Label(frame_entrada,text="nombre del programa")
titulo.config(bg="black", fg="white" , font=("arial", 12))
titulo.place(x=100,y=10)

logo_uis = tk.PhotoImage(file="uis.png")
label_logo = tk.Label(frame_entrada,image=logo_uis)
label_logo.place(x=10,y=40)

#etiqueta x

label_x=tk.Label(frame_entrada, text="X =")
label_x.config(fg="blue", font=("Arial", 14))
label_x.place(x=240,y=100)

#caja de texto x
entry_x = tk.Entry(frame_entrada,textvariable=x)
entry_x.config(font=("arial",12))
entry_x.focus_set
entry_x.place(x=280,y=100)

#etqueta y

label_x=tk.Label(frame_entrada, text="y =")
label_x.config(fg="blue", font=("Arial", 14))
label_x.place(x=240,y=140)

#caja de texto y
entry_y = tk.Entry(frame_entrada, textvariable=y)
entry_y.config(font=("arial",12))
entry_y.place(x=280,y=140)
#-------------------------
#FRAMDE DE operaciones
#-------------------------

frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg=estilos.COLOR_FONDO_FRAMES2, width=480,height=100)
frame_operaciones.pack(fill=tk.BOTH, padx=10, pady=10)
frame_operaciones.columnconfigure(0,weight=1)
frame_operaciones.columnconfigure(1,weight=1)
frame_operaciones.columnconfigure(2,weight=1)

#boton calcular
boton_calcular = tk.Button(frame_operaciones, text="calcular", command= calcular) 
boton_calcular.grid(row=0, column=0, padx=10,pady=10)

#boton borrar
boton_borrar = tk.Button(frame_operaciones, text="borrar", command=borrar)
boton_borrar.grid(row=0, column=1, padx=10,pady=10)

#boton salir
boton_salir = tk.Button(frame_operaciones, text="salir", command= salir)
boton_salir.grid(row=0, column=2, padx=10,pady=10)

#-------------------------
#FRAMDE para resultados 
#------------------------

frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg=estilos.COLOR_FONDO_FRAMES3, width=480,height=100)
frame_resultados.pack(fill=tk.BOTH, padx=10, pady=10 )

#area de resultados
at_resultados = tk.Text(frame_resultados,width=50,height=3)
at_resultados.grid(row=0, column=0)
sb_resultados = tk.Scrollbar(frame_resultados,command=at_resultados.yview)
sb_resultados.grid(row=0, column=1, sticky="nsew")

""""despegamos la ventana principal
en pantalla y queda a la espera de lo que el usuario haga"""
ventana_principal.mainloop()

