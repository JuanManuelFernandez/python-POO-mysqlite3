#controlador
from tkinter import ttk
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Button
from tkinter import messagebox

from modelo import Operaciones
from modelo import OperacionCREA
from modelo import ActualizarTreeview
obj = Operaciones

if __name__ == "__main__":
    #primer prueba realizada para la modificación de la def alta, actualmente definida dentro de una clase
    def alta(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_men, planilla):
        if horas_diarias.get() and pago_por_hora.get() and dias_trabajados.get():
            sueldo_men = (horas_diarias.get() * pago_por_hora.get()) * (dias_trabajados.get())
            data = (nombre.get(), edad.get(), area.get(), horas_diarias.get(), pago_por_hora.get(), dias_trabajados.get(), sueldo_men)         
            sql ="INSERT INTO empleados(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados, sueldo_mensual) VALUES(?, ?, ?, ?, ?, ?, ?)"         
            OperacionCREA.cursor.execute(sql, data)
            OperacionCREA.con.commit()
            print("Todo se encuentra correcto")
            ActualizarTreeview(planilla)
            messagebox.showinfo("Exito", "Empleado agregado.")
            limpiar(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados)
        else:
            messagebox.showerror("Error", "Horas diarias, pago por hora, y dias trabajados deben ser valores enteros.")
    
    def limpiar(nombre, edad, area, horas_diarias, pago_por_hora, dias_trabajados):
        nombre.set("")
        edad.set("")
        area.set("")
        horas_diarias.set("")
        pago_por_hora.set("")
        dias_trabajados.set("")

    #ventana

master = Tk()
master.title("carga de datos de empleados")
master.resizable(False, False)


titulo = Label(master, text="Ingrese sus datos", bg="green", fg="thistle1", height=2, width=80)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="we")

nombre_campo = Label(master, text="Nombre")
nombre_campo.grid(row=1, column=0, sticky= "w")
edad_campo = Label(master, text="Edad")
edad_campo.grid(row=2, column=0, sticky= "w")
area_campo = Label(master, text="Area")
area_campo.grid(row=3, column=0, sticky= "w")
horas_diarias_campo = Label(master, text="Horas diarias")
horas_diarias_campo.grid(row=4, column=0, sticky= "w")
pago_hr_campo = Label(master, text="Pago por hora")
pago_hr_campo.grid(row=5, column=0, sticky= "w")
dias_trabajados_campo = Label(master, text="Dias trabajados en el mes")
dias_trabajados_campo.grid(row= 6, column=0, sticky= "w")



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

boton_alta = Button(master, text="Alta", width= ancho, fg= "green", command=lambda: obj.alta(a_val, b_val, c_val, d_val, e_val, f_val, g_val, planilla))
boton_alta.grid(row=8, column=1)

boton_baja = Button(master, text="Baja", width= ancho, fg= "red", command=lambda: obj.baja(planilla))
boton_baja.grid(row=9, column=1)

boton_modificar = Button(master, text="Modificar", width= ancho, fg="purple", command=lambda: obj.modificar(a_val.get(), b_val.get(), c_val.get(), d_val.get(), e_val.get(), f_val.get(), g_val.get(),planilla))
boton_modificar.grid(row=11, column=1)


master.mainloop()