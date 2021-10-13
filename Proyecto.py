import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

ventana=tk.Tk()
ventana.title("Proyecto PDI")

miframe=tk.Frame(ventana)
miframe.pack()
miframe.config(bg="light sky blue",cursor='hand2')
#//////////////////////////FUNCIONES///////////////////////////////////////////////
def select():
    if opcion.get()==1:
        ventana1=tk.Tk()
        ventana1.title("Filtros espaciales")
        ventana1.mainloop()
    elif opcion.get()==2:
        ventana2=tk.Tk()
        ventana2.title("Morfología")
        ventana2.mainloop()
    elif opcion.get()==3:
        ventana3=tk.Tk()
        ventana3.title("Umbralización y segmentación")
        ventana3.mainloop()
    elif opcion.get()==4:
        ventana4=tk.Tk()
        ventana4.title("Transformación de intensidad")
        ventana4.mainloop()
    else:
        messagebox.showerror(message="Debes seleccionar un comando antes de seleccionar la imagen",title="Error")
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

boton1=tk.Button(miframe,image=img1,command=select)
boton1.grid(row=1,column=0,padx=5,pady=5)
boton2=tk.Button(miframe,image=img2,command=select)
boton2.grid(row=1,column=1,padx=5,pady=5)
boton3=tk.Button(miframe,image=img3,command=select)
boton3.grid(row=1,column=2,padx=5,pady=5)

#Botones radiales
opcion = tk.IntVar()
b1 = tk.Radiobutton(miframe,text="1) Filtros Espaciales",variable=opcion,value=1,activebackground='green',font="Arial 15",bg='light sky blue')
b1.grid(row=2,column=1,padx=5,pady=5)
b2 = tk.Radiobutton(miframe,text="2) Morfología",variable=opcion,value=2,activebackground='green',font="Arial 15",bg='light sky blue')
b2.grid(row=3,column=1,padx=5,pady=5)
b3 = tk.Radiobutton(miframe,text="3) Umbralización y Segmentación",variable=opcion,value=3,activebackground='green',font="Arial 15",bg='light sky blue')
b3.grid(row=4,column=1,padx=5,pady=5)
b4 = tk.Radiobutton(miframe,text="4) Transformación de intensidad",variable=opcion,value=4,activebackground='green',font="Arial 15",bg='light sky blue')
b4.grid(row=5,column=1,padx=5,pady=5)

#Boton principal de salida
Salir=tk.Button(miframe,text="SALIR",width=10,command=salir,activebackground="red",font="Arial 18")
Salir.grid(row=5,column=2,padx=10,pady=10)

ventana.mainloop()