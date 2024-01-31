#modelo
from tkinter import messagebox
import sqlite3
import re

"""Modelo: componentes que llevan la tarea de hacer funcionar la app (ejemplo “agregar cosas al carrito”, “hacer la suma del total”, etc)"""

#creacion de la db y tabla

class OperacionCON():
    def ConectarBase():
        conectar = sqlite3.connect("mybs.db")
        return conectar
    
class OperacionCREA():  
    def CrearTabla():
        con = OperacionCON.ConectarBase()
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
    OperacionCON.ConectarBase()
    OperacionCREA.CrearTabla()
except:
    print("La tabla se ha creado con anterioridad")  


#funciones 

class OperacionL():
    def limpiar(self, nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados):
        nombre.set("")
        edad.set("")
        area.set("")
        horas_diarias.set("")
        pago_por_hora.set("")
        dias_trabajados.set("")
    
# Alta
class Operaciones():
    
    def alta(self, nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men, planilla):
        regx = nombre.get()
        patron = "^[A-Za-záéíóú]*$" 
        if(re.match(patron, regx)):
            con = OperacionCON.ConectarBase()
            cursor = con.cursor()
            if horas_diarias.get() and pago_por_hora.get() and dias_trabajados.get():
                sueldo_men = (horas_diarias.get() * pago_por_hora.get()) * (dias_trabajados.get())
                data = (nombre.get(), edad.get(), area.get(), horas_diarias.get(), pago_por_hora.get(), dias_trabajados.get(), sueldo_men)         
                sql ="INSERT INTO empleados(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_mensual) VALUES(?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(sql, data)
                con.commit()
                print("Todo se encuentra correcto")
                ActualizarTreeview(planilla)
                messagebox.showinfo("Exito", "Empleado agregado.")
                OperacionL.limpiar(self, nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados)
            else:
                messagebox.showerror("Error", "Horas diarias, pago por hora, y dias trabajados deben ser valores enteros.")
                
# Baja

    def baja(self, planilla):
        valor = planilla.selection()
        print(valor)
        item = planilla.item(valor)
        print(item)    
        print(item['text'])
        mi_id = item['text']

        con=OperacionCON.ConectarBase()
        cursor=con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM empleados WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        planilla.delete(valor)

        messagebox.showinfo("Éxito", "Empleado dado de baja.")

#modificar

    def modificar(self, nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men, planilla):
        valor = planilla.selection()
        print(valor)
        item = planilla.item(valor)
        print(item)    
        print(item['text'])
        mi_id = item['text']
        
        try:
            con=OperacionCON.ConectarBase()
            cursor=con.cursor()
            sql = f"UPDATE empleados SET nombre='{nombre}', edad='{edad}', area='{area}', horas_diarias='{horas_diarias}', pago_por_hora='{pago_por_hora}', dias_trabajados='{dias_trabajados}', sueldo_mensual='{sueldo_men}' WHERE id={mi_id}"
            cursor.execute(sql)
            con.commit()
            messagebox.showinfo("Éxito", "Empleado actualizado con éxito")
            ActualizarTreeview(planilla)
        except:
            messagebox.showwarning("ADVERTENCIA", "Ocurrio un error en la actualización del registro")
    
#actualizar treeview

def ActualizarTreeview(mytreeview):
    records = mytreeview.get_children()
    for element in records:
        mytreeview.delete(element)

    sql = "SELECT * FROM empleados ORDER BY id ASC"
    con=OperacionCON.ConectarBase()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mytreeview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
