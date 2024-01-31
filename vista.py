#vista
from tkinter import *
from tkinter import ttk
from modelo import Operaciones

"""Vista: componentes que se muestran en pantalla (ejemplo botones, inputs, selectores, etc)"""

#ventana
class CreacionVentana():

    def __init__(self, master):
        
        self.master = master
        
        self.ObjetoOp = Operaciones()
        self.master.title("carga de datos de empleados")
        master.resizable(False, False)

        self.titulo = Label(master, text="Ingrese sus datos", bg="green", fg="thistle1", height=2, width=80)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="we")

        self.nombre_campo = Label(master, text="Nombre")
        self.nombre_campo.grid(row=1, column=0, sticky= "w")
        self.edad_campo = Label(master, text="Edad")
        self.edad_campo.grid(row=2, column=0, sticky= "w")
        self.area_campo = Label(master, text="Area")
        self.area_campo.grid(row=3, column=0, sticky= "w")
        self.horas_diarias_campo = Label(master, text="Horas diarias")
        self.horas_diarias_campo.grid(row=4, column=0, sticky= "w")
        self.pago_hr_campo = Label(master, text="Pago por hora")
        self.pago_hr_campo.grid(row=5, column=0, sticky= "w")
        self.dias_trabajados_campo = Label(master, text="Dias trabajados en el mes")
        self.dias_trabajados_campo.grid(row= 6, column=0, sticky= "w")

        self.a_val, self.b_val, self.c_val, self.d_val, self.e_val, self.f_val, self.g_val = StringVar(), IntVar(), StringVar(), IntVar(), IntVar(), IntVar(), IntVar()
        self.ancho = 25

        self.entry_nombre = Entry(master, textvariable= self.a_val, width= self.ancho)
        self.entry_nombre.grid(row= 1, column= 1)
        self.entry_edad = Entry(master, textvariable= self.b_val, width= self.ancho)
        self.entry_edad.grid(row= 2, column= 1)
        self.entry_area = Entry(master, textvariable= self.c_val, width= self.ancho)
        self.entry_area.grid(row=3, column=1)
        self.entry_hsdiarias = Entry(master, textvariable= self.d_val, width= self.ancho)
        self.entry_hsdiarias.grid(row=4, column=1)
        self.entry_pagohr = Entry(master, textvariable= self.e_val, width= self.ancho)
        self.entry_pagohr.grid(row=5, column=1)
        self.entry_diastra = Entry(master, textvariable= self.f_val, width= self.ancho)
        self.entry_diastra.grid(row=6, column=1)


        self.planilla = ttk.Treeview(master)

        self.planilla["columns"] =("col1", "col2", "col3", "col4", "col5", "col6")

        self.planilla.column("#0", width = 100, minwidth = 80)
        self.planilla.column("col1", width= 200, minwidth= 80)
        self.planilla.column("col2", width= 200, minwidth= 80)
        self.planilla.column("col3", width= 200, minwidth= 80)
        self.planilla.column("col4", width= 200, minwidth= 80)
        self.planilla.column("col5", width= 200, minwidth= 80)
        self.planilla.column("col6", width= 200, minwidth= 80)

        self.planilla.heading("#0", text="ID")
        self.planilla.heading("col1", text="Nombre")
        self.planilla.heading("col2", text="Edad")
        self.planilla.heading("col3", text="Area")
        self.planilla.heading("col4", text="Horas diarias")
        self.planilla.heading("col5", text="Pago por hora")
        self.planilla.heading("col6", text="Dias trabajados")

        self.planilla.grid(row=13, column=0, columnspan=4)

        boton_alta = Button(master, text="Alta", width= self.ancho, fg= "green", command=lambda: self.ObjetoOp.alta(self.a_val, self.b_val, self.c_val, self.d_val, self.e_val, self.f_val, self.g_val, self.planilla))
        boton_alta.grid(row=8, column=1)

        boton_baja = Button(master, text="Baja", width= self.ancho, fg= "red", command=lambda: self.ObjetoOp.baja(self.planilla))
        boton_baja.grid(row=9, column=1)

        boton_modificar = Button(master, text="Modificar", width= self.ancho, fg="purple", command=lambda: self.ObjetoOp.modificar(self.a_val.get(), self.b_val.get(), self.c_val.get(), self.d_val.get(), self.e_val.get(), self.f_val.get(), self.g_val.get(), self.planilla))
        boton_modificar.grid(row=11, column=1)

if __name__ == "__main__":

    master=Tk()
    aplicacion=CreacionVentana(master)
    master.mainloop()