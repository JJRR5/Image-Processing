import tkinter as tk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

ventana=tk.Tk()
ventana.title("Histograma y ecualización")

miframe=tk.Frame(ventana)
miframe.pack()
miframe.config(bg="light sky blue",cursor='hand2')

mensaje=tk.Label(miframe,text="Elige una de las 3 imagenes:",font=('Arial',25))
'''mensaje.place()
mensaje.pack()'''
mensaje.grid(row=0,column=1,padx=10,pady=10)

img1=Image.open('paisaje.jpg')
img1=img1.resize((250, 250),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img1)
img2=Image.open('rayosx.jpg')
img2=img2.resize((250, 250),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(img2)
img3=Image.open('Chito.png')
img3=img3.resize((250, 250),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img3)

boton1=tk.Button(miframe,image=img1)
boton1.grid(row=1,column=0,padx=5,pady=10)

boton2=tk.Button(miframe,image=img2)
boton2.grid(row=1,column=1,padx=5,pady=10)

boton3=tk.Button(miframe,image=img3)
boton3.grid(row=1,column=2,padx=5,pady=10)

ventana.mainloop()