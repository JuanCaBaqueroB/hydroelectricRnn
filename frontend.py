import backend as bck
from tkinter import *
from tkinter import ttk
from math import sqrt
from numpy import concatenate
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

raiz=Tk()
raiz.title('Red neuronal')

#Icono del programa
#raiz.iconbitmap("nombreImagen.ico")
#Dimensiones de la ventana
raiz.geometry('500x500')
raiz.resizable(width=1,height=1)
raiz.config(bg="green")

#Variables de entrada de texto
fechaI=StringVar()
fechaF=StringVar()

#Variable de entrada de radio buttons
var = IntVar()

#Creación de leyenda Periodo
legend=LabelFrame(raiz,text="Periodo",padx=40,pady=30)
legend.pack(expand="yes",fill="both")
legend.place(x=30,y=30)

#Creación de un frame - Módulo periodo
miFrame=Frame(legend)
miFrame.pack()
miFrame.config(width=50)
#miFrame.config(bg="blue")

#Creación de leyenda de resultados
legendR=LabelFrame(raiz,text="Resultados",padx=45, pady=20)
legendR.pack(expand="no",fill="y")
legendR.place(x=30,y=270)
legendR.config(width="320", height="80")

#Módulo de resultados
resultadoP=StringVar()
res=Label(legendR,textvariable=resultadoP)
res.grid(row="1",column="0")
res.config(width=50,justify="left")

#Texto y selector de inicio
fechaInicio=Label(miFrame,text="Fecha de inicio:")
fechaInicio.grid(row=1,column=0,pady=10)
entFechaInicio=Entry(miFrame,textvariable=fechaI)
entFechaInicio.grid(row=1,column=1,pady=10) 
entFechaInicio.config(justify="center")

#Texto y selector de finalización
fechaFinal=Label(miFrame,text="Fecha final:")
fechaFinal.grid(row=2,column=0,pady=10)
entFechaFinal=Entry(miFrame,textvariable=fechaF)
entFechaFinal.grid(row=2,column=1,pady=10)
entFechaFinal.config(justify="center")

def hab():
    btnEjecutar.config(state='normal')
    entFechaInicio.config(state='normal')
    entFechaFinal.config(state='normal')
    btnEjecutar.config(state='normal')

#Selecciona todas las observaciones disponibles e Inhabilita el módulo periodo  
def dis():
    entFechaInicio.delete(0,END)
    entFechaFinal.delete(0,END)
    entFechaInicio.config(state='disabled')
    entFechaFinal.config(state='disabled')
    btnEjecutar.config(state='normal')

def ejecutarIntervalo():
    casoUso=int(var.get()) 
    if casoUso==2: 
        r=bck.ejecucion(fechaI.get(),fechaF.get())
        resultadoP.set(r)
        a=fechaF.get()

    if casoUso==1:
        d=read_csv('dias.csv', header=0, index_col=0)
        r=bck.ejecucion(d.iloc[0].name,d.iloc[len(d)-1].name)
        a=d.iloc[len(d)-1].name    
    resultadoP.set("Periodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}\nPeriodo {} predicción {:.2f}" .format(a+"+1",r[0],a+"+2",r[1],a+"+3",r[2],a+"+4",r[3],a+"+5",r[4],a+"+6",r[5],a+"+7",r[6]))

#Boton que ejecuta la red neronal con los datos seleccionados por el usuario
btnEjecutar=ttk.Button(miFrame, text='Realizar predicción', command=lambda: ejecutarIntervalo())
btnEjecutar.grid(row=3,column=1,pady="4")
btnEjecutar.config(state='disabled')

#Botón que cierra el programa
btnSalir=ttk.Button(raiz, text='Salir', command=quit )
btnSalir.place(x=400,y=400)
              
#Botones de selección
R1 = Radiobutton(miFrame, text="Todas las observaciones", variable=var, value=1,command=dis)
R1.grid(row=0,column=1)
R2 = Radiobutton(miFrame, text="Periodo escogido", variable=var, value=2,command=hab)
R2.grid(row=0,column=2)

#Main
raiz.mainloop()