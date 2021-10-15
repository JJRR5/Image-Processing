import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

ventana=tk.Tk()
ventana.title("Proyecto PDI")

miframe=tk.Frame(ventana)
miframe.pack()
miframe.config(bg="light sky blue",cursor='hand2')

imagen=cv2.imread('Chito.jpg')

#//////////////////////////FUNCIONES///////////////////////////////////////////////
def select():
    global imagen
    if menu.current()==0:
        ventana1=tk.Tk()
        ventana1.title("Filtros Espaciales")
        miframe1=tk.Frame(ventana1)
        miframe1.pack()
        miframe1.config(bg="gold",cursor='hand2')
        botonpb=tk.Button(miframe1,text="Filtro pasa bajas")
        botonpb.grid(row=1,column=0,padx=5,pady=5)
        botonpa=tk.Button(miframe1,text="Filtro pasa altas")
        botonpa.grid(row=1,column=2,padx=5,pady=5)
        ventana1.mainloop()
    elif menu.current()==1:
        ventana2=tk.Tk()
        ventana2.title("Morfología")
        miframe2=tk.Frame(ventana2)
        miframe2.pack()
        miframe2.config(bg="gold",cursor='hand2')
        botondi=tk.Button(miframe2,text="Dilatación")
        botondi.grid(row=1,column=0,padx=5,pady=5)
        botoner=tk.Button(miframe2,text="Erosión")
        botoner.grid(row=1,column=1,padx=5,pady=5)
        ventana2.mainloop()
    elif menu.current()==2:
        ventana3=tk.Tk()
        ventana3.title("Umbralización y Segmentación")
        miframe3=tk.Frame(ventana3)
        miframe3.pack()
        miframe3.config(bg="gold",cursor='hand2')
        botoneg=tk.Button(miframe3,text="Escala de grises",command=select)
        botoneg.grid(row=1,column=0,padx=5,pady=5)
        botonbn=tk.Button(miframe3,text="Blanco y negro",command=select)
        botonbn.grid(row=1,column=1,padx=5,pady=5)
        ventana3.mainloop()
    elif menu.current()==3:
        ventana4=tk.Tk()
        ventana4.title("Transformación de Intensidad")
        ventana4.mainloop()
    else:
        messagebox.showerror(message="Debes seleccionar un comando antes de seleccionar la imagen",title="Error")

def select1():
    global imagen
    imagen=cv2.imread('paisaje.jpg')
    select()

def select2():
    global imagen
    imagen=cv2.imread('rayosx.jpg')
    select()

def select3():
    global imagen
    imagen=cv2.imread('Chito.png')
    select()

def salir():
    ventana.destroy()
    
#//////////////////////////////////////////////////////////////////////////////
mensaje=tk.Label(miframe,text="Elige una de las 3 imagenes y el comando a utilizar",font=('Arial 20'),bg='light sky blue')
mensaje.grid(row=0,column=1,padx=10,pady=10)

img1=Image.open('paisaje.jpg')
img1=img1.resize((200, 220),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img1)
img2=Image.open('rayosx.jpg')
img2=img2.resize((200, 220),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(img2)
img3=Image.open('Chito.png')
img3=img3.resize((200, 220),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img3)

boton1=tk.Button(miframe,image=img1,command=select1)
boton1.grid(row=2,column=0,padx=5,pady=5)
boton2=tk.Button(miframe,image=img2,command=select2)
boton2.grid(row=2,column=1,padx=5,pady=5)
boton3=tk.Button(miframe,image=img3,command=select3)
boton3.grid(row=2,column=2,padx=5,pady=5)

#Menu
menu=ttk.Combobox(miframe,font="Arial 15",justify=tk.CENTER,width=30)
menu.grid(row=1,column=1,padx=15,pady=15)
opciones1=["Filtros Espaciales","Morfología","Umbralización y Segmentación","Transformación de Intensidad"]
menu["values"]=opciones1

#Boton principal de salida
Salir=tk.Button(miframe,text="SALIR",width=10,command=salir,activebackground="red",font="Arial 18")
Salir.grid(row=5,column=2,padx=10,pady=10)

ventana.mainloop()