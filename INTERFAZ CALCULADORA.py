import tkinter as tk
import math
import random

def FuncionSumatoriaAnterior(numero1,numero2,numero3):
    return numero1+numero2+numero3

def FuncionSumatoria():
    ecuacion=int(entrada1.get())+int(entrada2.get())+int(entrada3.get())
    resultado["text"]=ecuacion

def FuncionMultiplicar():
    ecuacion=int(entrada1.get())*int(entrada2.get())*int(entrada3.get())
    resultado["text"]=ecuacion

def FuncionDividir():
    ecuacion=int(entrada1.get())/int(entrada2.get())/int(entrada3.get())
    resultado["text"]=ecuacion

def FuncionMayor():
    if int(entrada1.get())>int(entrada2.get()):
        if int(entrada1.get())>int(entrada3.get()):
            resultado["text"]=entrada1.get()
        else:
            resultado["text"]=entrada3.get()
    else:
        if int(entrada2.get())>int(entrada3.get()):
            resultado["text"]=entrada2.get()
        else:
            resultado["text"]=entrada3.get()

def Aleatorio():
    numero = random.randint(1, 2)
    if numero == 1:
        ecuacion=int(entrada1.get()) + int(entrada2.get()) + int(entrada3.get())
    else:
        ecuacion= int(entrada1.get()) * int(entrada2.get()) * int(entrada3.get())
    return ecuacion

def RaizCuadrada():
    ecuacion=math.sqrt(Aleatorio())
    resultado["text"]=ecuacion

ventana=tk.Tk()
ventana.geometry("700x700")

entrada1=tk.Entry(ventana)
entrada1.grid(row=0, column=0)

entrada2=tk.Entry(ventana)
entrada2.grid(row=0, column=1)

entrada3=tk.Entry(ventana)
entrada3.grid(row=0, column=2)

entrada4=tk.Entry(ventana)
entrada4.grid(row=0, column=3)

entrada5=tk.Entry(ventana)
entrada5.grid(row=0, column=4)

boton1=tk.Button(ventana,text="Sumatoria",width=10,height=4,command=FuncionSumatoria)
boton1.grid(row=1,column=0)

boton2=tk.Button(ventana,text="Multiplicar",width=10,height=4,command=FuncionMultiplicar)
boton2.grid(row=1,column=2)

boton3=tk.Button(ventana,text="Dividir",width=15,height=4,command=FuncionDividir)
boton3.grid(row=1,column=3)

boton4=tk.Button(ventana,text="Mayor",width=15,height=4,command=FuncionMayor)
boton4.grid(row=1,column=1)

boton5=tk.Button(ventana,text="RaizCuadrada",width=15,height=4,command=RaizCuadrada)
boton5.grid(row=1,column=4)

resultado=tk.Label(ventana)
resultado.grid(row=2,column=1)

ventana.mainloop()