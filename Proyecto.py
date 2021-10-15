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

#//////////////////////////FUNCIONES//////////////////////////////////////////////////////////////////////////////////
def select():
    global imagen
    #BACK FUNCION PARA VOLVER AL MENÚ PRINCIPAL
    def back1():
        ventana1.destroy()
    def back2():
        ventana2.destroy()
    def back3():
        ventana3.destroy()
    def back4():
        ventana4.destroy()
#/////////////////PASA BAJAS/////////////////////////////////////////////////////////////////
    def PasaBajas():
        def validar():
            num1 = entry1.get()
            num2 = entry2.get()
            num3 = entry3.get()
            num4 = entry4.get()
            num5 = entry5.get()
            num6 = entry6.get()
            num7 = entry7.get()
            num8 = entry8.get()
            num9 = entry9.get()
            if num1.isnumeric()==True and num2.isnumeric()==True and num3.isnumeric()==True and num4.isnumeric()==True and num5.isnumeric()==True and num6.isnumeric()==True and num7.isnumeric()==True and num8.isnumeric()==True and  num9.isnumeric()==True:
                numa = int(num1)
                numb = int(num2)
                numc = int(num3)
                numd = int(num4)
                nume = int(num5)
                numf = int(num6)
                numg = int(num7)
                numh = int(num8)
                numi = int(num9)
                kernel=np.array([[numa,numb,numc],[numd,nume,numf],[numg,numh,numi]])
                kernel = 1/9 * kernel
                im=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
                Promedio=cv2.filter2D(im,-1,kernel)
                cv2.imshow("PASA BAJAS",Promedio)
                cv2.waitKey()
            else:
                messagebox.showerror(message="Los datos que ingresaste no son númericos o hay un espacio en blanco",title="Error")
        def limpiar():
            entry1.delete(0,tk.END)
            entry2.delete(0,tk.END)
            entry3.delete(0,tk.END)
            entry4.delete(0,tk.END)
            entry5.delete(0,tk.END)
            entry6.delete(0,tk.END)
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
        def backespacial():
            ventanapb.destroy()
        ventanapb=tk.Tk()
        ventanapb.title("Valores de la matriz 3x3")
        miframepb=tk.Frame(ventanapb)
        miframepb.pack()
        miframepb.config(bg="salmon",cursor='hand2')
        #etiquetas que indica donde se tienen que poner los valores
        mensaje1=tk.Label(miframepb,text="Valores 1-3:",font=('Arial 15'),bg='salmon')
        mensaje1.grid(row=0,column=0,padx=5,pady=5)
        mensaje2=tk.Label(miframepb,text="Valores 4-6:",font=('Arial 15'),bg='salmon')
        mensaje2.grid(row=1,column=0,padx=5,pady=5)
        mensaje3=tk.Label(miframepb,text="Valores 7-9:",font=('Arial 15'),bg='salmon')
        mensaje3.grid(row=2,column=0,padx=5,pady=5)
        #entrys para los valores del kernel
        entry1 = tk.Entry(miframepb,font="Arial 15")
        entry1.grid(row=0,column=1,padx=5,pady=5)
        entry1.config(justify="center") 
        entry2 = tk.Entry(miframepb,font="Arial 15")
        entry2.grid(row=0,column=2,padx=5,pady=5)
        entry2.config(justify="center")
        entry3 = tk.Entry(miframepb,font="Arial 15")
        entry3.grid(row=0,column=3,padx=5,pady=5)
        entry3.config(justify="center")
        entry4 = tk.Entry(miframepb,font="Arial 15")
        entry4.grid(row=1,column=1,padx=5,pady=5)
        entry4.config(justify="center")
        entry5 = tk.Entry(miframepb,font="Arial 15")
        entry5.grid(row=1,column=2,padx=5,pady=5)
        entry5.config(justify="center")
        entry6 = tk.Entry(miframepb,font="Arial 15")
        entry6.grid(row=1,column=3,padx=5,pady=5)
        entry6.config(justify="center")
        entry7 = tk.Entry(miframepb,font="Arial 15")
        entry7.grid(row=2,column=1,padx=5,pady=5)
        entry7.config(justify="center")
        entry8 = tk.Entry(miframepb,font="Arial 15")
        entry8.grid(row=2,column=2,padx=5,pady=5)
        entry8.config(justify="center")
        entry9 = tk.Entry(miframepb,font="Arial 15")
        entry9.grid(row=2,column=3,padx=5,pady=5)
        entry9.config(justify="center")
        
        #botón regresar,filtrar y limpiar
        Menuespacial=tk.Button(miframepb,text="Back",width=10,command=backespacial,font="Arial 18",activebackground="red")
        Menuespacial.grid(row=4,column=0,padx=10,pady=10)
        filtrar = tk.Button(miframepb,text="Filtrar",width=10,command=validar,font="Arial 18",activebackground="green")
        filtrar.grid(row=4,column=3,padx=10,pady=10)
        limpiar1=tk.Button(miframepb,text="Borrar",width=10,command=limpiar,font="Arial 18",activebackground="red")
        limpiar1.grid(row=4,column=2,padx=10,pady=10)
        ventanapb.mainloop()
#/////////////////PASA ALTAS///////////////////////////////////////////////////////////////////
    def PasaAltas():
        def validar():
            num1 = entry1.get()
            num2 = entry2.get()
            num3 = entry3.get()
            num4 = entry4.get()
            num5 = entry5.get()
            num6 = entry6.get()
            num7 = entry7.get()
            num8 = entry8.get()
            num9 = entry9.get()
            if num1.isnumeric()==True and num2.isnumeric()==True and num3.isnumeric()==True and num4.isnumeric()==True and num5.isnumeric()==True and num6.isnumeric()==True and num7.isnumeric()==True and num8.isnumeric()==True and  num9.isnumeric()==True:
                numa = int(num1)*-1
                numb = int(num2)*-1
                numc = int(num3)*-1
                numd = int(num4)*-1
                nume = int(num5)
                numf = int(num6)*-1
                numg = int(num7)*-1
                numh = int(num8)*-1
                numi = int(num9)*-1
                kernel=np.array([[numa,numb,numc],[numd,nume,numf],[numg,numh,numi]])
                kernel = 1/2 * kernel
                bordes=cv2.filter2D(imagen,-1,kernel)
                cv2.imshow("PASA ALTAS",bordes)
                cv2.waitKey()
            else:
                messagebox.showerror(message="Los datos que ingresaste no son númericos o hay un espacio en blanco",title="Error")
        def limpiar():
            entry1.delete(0,tk.END)
            entry2.delete(0,tk.END)
            entry3.delete(0,tk.END)
            entry4.delete(0,tk.END)
            entry5.delete(0,tk.END)
            entry6.delete(0,tk.END)
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
        def backespacial():
            ventanapb.destroy()
        ventanapb=tk.Tk()
        ventanapb.title("Valores de la matriz 3x3")
        miframepb=tk.Frame(ventanapb)
        miframepb.pack()
        miframepb.config(bg="salmon",cursor='hand2')
        #etiquetas que indica donde se tienen que poner los valores
        mensaje1=tk.Label(miframepb,text="Valores 1-3:",font=('Arial 15'),bg='salmon')
        mensaje1.grid(row=0,column=0,padx=5,pady=5)
        mensaje2=tk.Label(miframepb,text="Valores 4-6:",font=('Arial 15'),bg='salmon')
        mensaje2.grid(row=1,column=0,padx=5,pady=5)
        mensaje3=tk.Label(miframepb,text="Valores 7-9:",font=('Arial 15'),bg='salmon')
        mensaje3.grid(row=2,column=0,padx=5,pady=5)
        #entrys para los valores del kernel
        entry1 = tk.Entry(miframepb,font="Arial 15")
        entry1.grid(row=0,column=1,padx=5,pady=5)
        entry1.config(justify="center") 
        entry2 = tk.Entry(miframepb,font="Arial 15")
        entry2.grid(row=0,column=2,padx=5,pady=5)
        entry2.config(justify="center")
        entry3 = tk.Entry(miframepb,font="Arial 15")
        entry3.grid(row=0,column=3,padx=5,pady=5)
        entry3.config(justify="center")
        entry4 = tk.Entry(miframepb,font="Arial 15")
        entry4.grid(row=1,column=1,padx=5,pady=5)
        entry4.config(justify="center")
        entry5 = tk.Entry(miframepb,font="Arial 15")
        entry5.grid(row=1,column=2,padx=5,pady=5)
        entry5.config(justify="center")
        entry6 = tk.Entry(miframepb,font="Arial 15")
        entry6.grid(row=1,column=3,padx=5,pady=5)
        entry6.config(justify="center")
        entry7 = tk.Entry(miframepb,font="Arial 15")
        entry7.grid(row=2,column=1,padx=5,pady=5)
        entry7.config(justify="center")
        entry8 = tk.Entry(miframepb,font="Arial 15")
        entry8.grid(row=2,column=2,padx=5,pady=5)
        entry8.config(justify="center")
        entry9 = tk.Entry(miframepb,font="Arial 15")
        entry9.grid(row=2,column=3,padx=5,pady=5)
        entry9.config(justify="center")
        
        #botón regresar,filtrar y limpiar
        Menuespacial=tk.Button(miframepb,text="Back",width=10,command=backespacial,font="Arial 18",activebackground="red")
        Menuespacial.grid(row=4,column=0,padx=10,pady=10)
        filtrar = tk.Button(miframepb,text="Filtrar",width=10,command=validar,font="Arial 18",activebackground="green")
        filtrar.grid(row=4,column=3,padx=10,pady=10)
        limpiar1=tk.Button(miframepb,text="Borrar",width=10,command=limpiar,font="Arial 18",activebackground="red")
        limpiar1.grid(row=4,column=2,padx=10,pady=10)
        ventanapb.mainloop()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def Dilatación():
        print
    def Erosión():
        print
#///////////////////////////////////////////////////////////////////LÓGICA DEL MENU PRINCIPAL/////////////////////////////////////////////////////////////////
    if menu.current()==0:
        ventana1=tk.Tk()
        ventana1.title("Filtros Espaciales")
        miframe1=tk.Frame(ventana1)
        miframe1.pack()
        miframe1.config(bg="salmon",cursor='hand2')
        botonpb=tk.Button(miframe1,text="Filtro pasa bajas",font="Arial 15",activebackground="green",command=PasaBajas)
        botonpb.grid(row=1,column=0,padx=5,pady=5)
        botonpa=tk.Button(miframe1,text="Filtro pasa altas",font="Arial 15",activebackground="green",command=PasaAltas)
        botonpa.grid(row=1,column=2,padx=5,pady=5)
        Menu=tk.Button(miframe1,text="BACK",width=10,command=back1,font="Arial 18",activebackground="red")
        Menu.grid(row=6,column=1,padx=10,pady=10)
        ventana1.mainloop()
    elif menu.current()==1:
        ventana2=tk.Tk()
        ventana2.title("Morfología")
        miframe2=tk.Frame(ventana2)
        miframe2.pack()
        miframe2.config(bg="gold",cursor='hand2')
        botondi=tk.Button(miframe2,text="Dilatación",font="Arial 15",activebackground="green")
        botondi.grid(row=1,column=0,padx=5,pady=5)
        botoner=tk.Button(miframe2,text="Erosión",font="Arial 15",activebackground="green")
        botoner.grid(row=1,column=2,padx=5,pady=5)
        Menu=tk.Button(miframe2,text="BACK",width=10,command=back2,font="Arial 18",activebackground="gold")
        Menu.grid(row=2,column=1,padx=10,pady=10)
        ventana2.mainloop()
    elif menu.current()==2:
        ventana3=tk.Tk()
        ventana3.title("Umbralización y Segmentación")
        miframe3=tk.Frame(ventana3)
        miframe3.pack()
        miframe3.config(bg="gold",cursor='hand2')
        botoneg=tk.Button(miframe3,text="Escala de grises")
        botoneg.grid(row=1,column=0,padx=5,pady=5)
        botonbn=tk.Button(miframe3,text="Blanco y negro")
        botonbn.grid(row=1,column=1,padx=5,pady=5)
        ventana3.mainloop()
    elif menu.current()==3:
        ventana4=tk.Tk()
        ventana4.title("Transformación de Intensidad")
        miframe4=tk.Frame(ventana4)
        miframe4.pack()
        miframe4.config(bg="gold",cursor='hand2')
        b=tk.Scale(miframe4, from_=0, to=100, orient=tk.HORIZONTAL)
        b.grid(row=1,column=1,padx=5,pady=5)
        botonsel=tk.Button(miframe4,text="Seleccionar")
        botonsel.grid(row=2,column=1,padx=5,pady=5)
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
    cv2.destroyAllWindows()
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
menu=ttk.Combobox(miframe,font="Arial 15",justify=tk.CENTER,width=30,state="readonly")
menu.grid(row=1,column=1,padx=15,pady=15)
opciones1=["Filtros Espaciales","Morfología","Umbralización y Segmentación","Transformación de Intensidad"]
menu["values"]=opciones1

#Boton principal de salida
Salir=tk.Button(miframe,text="SALIR",width=10,command=salir,activebackground="red",font="Arial 18")
Salir.grid(row=5,column=2,padx=10,pady=10)

ventana.mainloop()