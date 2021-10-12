import tkinter as tk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

ventana=tk.Tk()
ventana.title("Histograma y ecualización")

miframe=tk.Frame(ventana)
miframe.pack()

mensaje=tk.Label(miframe,text="Elige una de las 3 imagenes:",font=('Arial',25))
mensaje.place()
mensaje.pack()

img1=Image.open('R1.jpg')
img1=img1.resize((250, 250),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img1)
img2=Image.open('R2.jpg')
img2=img2.resize((250, 250),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(img2)
img3=Image.open('R3.jpg')
img3=img3.resize((250, 250),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img3)
boton1=tk.Button(miframe,image=img1)
boton1.place()
boton1.pack()
boton2=tk.Button(miframe,image=img2)
boton2.place()
boton2.pack()
boton3=tk.Button(miframe,image=img3)
boton3.place()
boton3.pack()

ventana.mainloop()