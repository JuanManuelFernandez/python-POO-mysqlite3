#prueba_app_2

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3
import re


#creacion de la db y tabla

def conectar_base():
    conectar = sqlite3.connect("mybs.db")
    return conectar

def crear_tabla():
    con = conectar_base()
    cursor = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS empleados
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre varchar NOT NULL, 
            edad real, 
            area, 
            horas_diarias real, 
            pago_por_hora real, 
            dias_trabajados real, 
            sueldo_mensual real
            )
    """
    #NOT NULL es para que el valor no pueda ser nulo
    cursor.execute(sql)
    con.commit()

try:
    conectar_base()
    crear_tabla()
except:
    print("La tabla se ha creado con anterioridad")  


db = {}


#funciones 

#alta

def alta(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men, planilla):
    global db
    db[nombre]= {"edad ": edad,
                       "area": area, 
                       "horas diarias": horas_diarias, 
                       "pago por hora": pago_por_hora, 
                       "dias trabajados en el mes": dias_trabajados, 
                       "sueldo mensual": sueldo_men}
    regx = nombre
    patron = "^[A-Za-záéíóú]*$" 
    if(re.match(patron, regx)):
        con = conectar_base()
        cursor = con.cursor()
        sueldo_men = (horas_diarias * pago_por_hora) * dias_trabajados
        data = (nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men)
        sql ="INSERT INTO empleados(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_mensual) VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Todo se encuentra correcto")
        actualizar_treeview(planilla)
    else:
        print("error en campo")

    messagebox.showinfo("Éxito", "Empleado agregado con éxito.")
    limpiar_campos()

#baja

def baja(planilla):
    valor = planilla.selection()
    print(valor)
    item = planilla.item(valor)
    print(item)    
    print(item['text'])
    mi_id = item['text']

    con=conectar_base()
    cursor=con.cursor()
    data = (mi_id,)
    sql = "DELETE FROM empleados WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    planilla.delete(valor)

    messagebox.showinfo("Éxito", "Empleado dado de baja con éxito.")

#consulta

def consulta():
    global db
    messagebox.showwarning("Datos", db)

#modificar

def modificar(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men, planilla):
    valor = planilla.selection()
    print(valor)
    item = planilla.item(valor)
    print(item)    
    print(item['text'])
    mi_id = item['text']
    
    try:
        con=conectar_base()
        cursor=con.cursor()
        sql = f"UPDATE empleados SET nombre='{nombre}', edad='{edad}', area='{area}', horas_diarias='{horas_diarias}', pago_por_hora='{pago_por_hora}', dias_trabajados='{dias_trabajados}', sueldo_mensual='{sueldo_men}' WHERE id={mi_id}"
        cursor.execute(sql)
        con.commit()
        messagebox.showinfo("Éxito", "Empleado actualizado con éxito")
        actualizar_treeview(planilla)
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error en la actualización del registro")

    limpiar_campos()
    

#actualizar treeview

def actualizar_treeview(mytreeview):
    records = mytreeview.get_children()
    for element in records:
        mytreeview.delete(element)

    sql = "SELECT * FROM empleados ORDER BY id ASC"
    con=conectar_base()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mytreeview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

#limpiar campos

def limpiar_campos():
    entry_nombre.delete(0 ,END)
    entry_edad.delete(0, END)
    entry_area.delete(0, END)
    entry_hsdiarias.delete(0, END)
    entry_pagohr.delete(0, END)
    entry_diastra.delete(0, END)


#darkmode

var_tema = 0

col_claro = "#F0F0F0"
col_oscuro = "#272727"

def cambiar_color():
    global var_tema
    if var_tema == 0:
        master.config(bg=col_oscuro)
        var_tema = 1
    
    else:
        master.config(bg=col_claro)
        var_tema = 0

#funcion doble click para cargar los datos automaticamente en los campos entry a la hora de querer modificar

def on_double_click(event):
    item = planilla.selection()[0]
    try:
        a_val.set(planilla.item(item, "values")[0])
        b_val.set(planilla.item(item, "values")[1])
        c_val.set(planilla.item(item, "values")[2])
        d_val.set(planilla.item(item, "values")[3])
        e_val.set(planilla.item(item, "values")[4])
        f_val.set(planilla.item(item, "values")[5])
        g_val.set(planilla.item(item, "values")[6])
    except IndexError:
        pass


#ventana

master = Tk()
master.title("carga de datos de empleados")
master.resizable(False, False)


titulo = Label(master, text="Ingrese sus datos", bg="green", fg="thistle1", height=2, width=80)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

nombre_campo = Label(master, text="Nombre")
nombre_campo.grid(row=1, column=0, sticky= W)
edad_campo = Label(master, text="Edad")
edad_campo.grid(row=2, column=0, sticky= W)
area_campo = Label(master, text="Area")
area_campo.grid(row=3, column=0, sticky= W)
horas_diarias_campo = Label(master, text="Horas diarias")
horas_diarias_campo.grid(row=4, column=0, sticky= W)
pago_hr_campo = Label(master, text="Pago por hora")
pago_hr_campo.grid(row=5, column=0, sticky= W)
dias_trabajados_campo = Label(master, text="Dias trabajados en el mes")
dias_trabajados_campo.grid(row= 6, column=0, sticky= W)



a_val, b_val, c_val, d_val, e_val, f_val, g_val = StringVar(), IntVar(), StringVar(), IntVar(), IntVar(), IntVar(), IntVar()
ancho = 25


entry_nombre = Entry(master, textvariable= a_val, width= ancho)
entry_nombre.grid(row= 1, column= 1)
entry_edad = Entry(master, textvariable= b_val, width= ancho)
entry_edad.grid(row= 2, column= 1)
entry_area = Entry(master, textvariable= c_val, width= ancho)
entry_area.grid(row=3, column=1)
entry_hsdiarias = Entry(master, textvariable= d_val, width= ancho)
entry_hsdiarias.grid(row=4, column=1)
entry_pagohr = Entry(master, textvariable= e_val, width= ancho)
entry_pagohr.grid(row=5, column=1)
entry_diastra = Entry(master, textvariable= f_val, width= ancho)
entry_diastra.grid(row=6, column=1)


#Tree

planilla = ttk.Treeview(master)


planilla["columns"] =("col1", "col2", "col3", "col4", "col5", "col6")

planilla.column("#0", width = 100, minwidth = 80)
planilla.column("col1", width= 200, minwidth= 80)
planilla.column("col2", width= 200, minwidth= 80)
planilla.column("col3", width= 200, minwidth= 80)
planilla.column("col4", width= 200, minwidth= 80)
planilla.column("col5", width= 200, minwidth= 80)
planilla.column("col6", width= 200, minwidth= 80)


planilla.heading("#0", text="ID")
planilla.heading("col1", text="Nombre")
planilla.heading("col2", text="Edad")
planilla.heading("col3", text="Area")
planilla.heading("col4", text="Horas diarias")
planilla.heading("col5", text="Pago por hora")
planilla.heading("col6", text="Dias trabajados")

planilla.grid(row=13, column=0, columnspan=4)


boton_alta = Button(master, text="Alta", width= ancho, fg= "green", command=lambda: alta(a_val.get(), b_val.get(), c_val.get(), d_val.get(), e_val.get(), f_val.get(), g_val.get(), planilla))
boton_alta.grid(row=8, column=1)

boton_baja = Button(master, text="Baja", width= ancho, fg= "red", command=lambda: baja(planilla))
boton_baja.grid(row=9, column=1)

boton_dark = Button(master, text="Modo oscuro", command=lambda: cambiar_color())
boton_dark.grid(row=9, column=0, sticky= W)

boton_limpiar = Button(master, text="Limpiar campos", fg= "blue", command=lambda:limpiar_campos())
boton_limpiar.grid(row=10, column=0, sticky= W)

boton_consulta = Button(master, text="Consultar", width= ancho, fg="blue",  command=lambda:consulta())
boton_consulta.grid(row=10, column=1)


boton_modificar = Button(master, text="Modificar", width= ancho, fg="purple", command=lambda: modificar(a_val.get(), b_val.get(), c_val.get(), d_val.get(), e_val.get(), f_val.get(), g_val.get(),planilla))
boton_modificar.grid(row=11, column=1)


planilla.bind("<Double-1>", on_double_click)


master.mainloop()