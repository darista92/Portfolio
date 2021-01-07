# -*- coding: utf-8 -*-
"""
El script permite calcular el coste mensual aproximado (en €) de la gasolina utilizada durante un mes. Mediante una interfaz es posible introducir manualmente 
los kilómetros recorridos al día y el consumo del coche marcado por el fabricante para realizar el cálculo


"""


# --------------paquetes--------------

from tkinter import *
from tkinter import messagebox

#--------------core-----------------
root= Tk()

#----------fórmula original---------
'''def gasolina_mes(km_dia_laboral, consumo, precio_gas=1.151):
    Devuelve el coste de gasolina de un coche al mes
    km_mes = (km_dia_laboral*2) * 5.5 * 4.35 # dialaboral(*ida y vuelta); 5,5 dias a la semana * 4,3 semanas (30.3 dias)
    eur_1_km = (consumo/100)*precio_gas
    return round ((km_mes*eur_1_km),2)'''

#tkinter

#------propiedades generales----------
fuente_text =("Verdana", 20)
fuente_num = ("Verdana", 20, "bold")

#-----------etiquetas----------------
km_dia_etiq = Label(root, text="kilómetros diarios (ida)", font=fuente_text)
km_dia_etiq.grid(row=0, column=0)

consumo_etiq = Label(root, text="consumo del coche (l por 100km)", font=fuente_text)
consumo_etiq.grid(row=1, column=0)

#----------entrada de datos---------

# Entrada del valor numérico

km_al_dia = IntVar()
consumo_coche = IntVar()

#configuración de los campos

entrada_km_dia = Entry(root, textvariable = km_al_dia, width=40, 
                       bd=6, font=(fuente_num))
entrada_km_dia.grid(row=0, column=1)

entrada_consumo = Entry(root, textvariable= consumo_coche, width=40,
                        bd=6, font=(fuente_num))
entrada_consumo.grid(row=1, column=1)


#--------cálculo----------------

def gasolina_tkinter(precio_gas =1.151):
    km_dia_laboral = km_al_dia.get()
    consumo = consumo_coche.get()
    km_mes = (km_dia_laboral*2) * 5.5 * 4.35
    eur_1_km = (consumo/100)*precio_gas
    eur_mes = round((km_mes*eur_1_km),2)
    messagebox.showinfo("Resultado", f"El gasto mensual en gasolina para este coche es de: {eur_mes}"+"€")

#botón
calcular = Button(root, text="Calcular", font=fuente_num, width=15, bd=6
                  , command = gasolina_tkinter)
calcular.grid(row=2, columnspan=3)

#--------------ventana--------------

root.title("Calculadora gasto gasolina mensual")
root.resizable(False, False) #prohibe el cambio de dimensiones de la ventana
root.mainloop()
