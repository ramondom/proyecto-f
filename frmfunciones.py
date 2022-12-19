from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
#import bll.usuarios as user
from frmfuncion import Funcion
import bll.funciones as func

class Funciones(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Funciones")        
        width=680
        height=350
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Funciones:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("fech", "hora", "sala", "peli"), name="tvFunciones")
        tv.column("#0", width=20)
        tv.column("fech", width=50, anchor=CENTER)
        tv.column("hora", width=50, anchor=CENTER)
        tv.column("sala", width=40, anchor=CENTER)
        tv.column("peli", width=250, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("fech", text="Fecha", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("sala", text="Sala", anchor=CENTER)
        tv.heading("peli", text="Pelicula", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=30,width=660,height=280)    

        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=250,y=320,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=330,y=320,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=410,y=320,width=70,height=25)
        btn_eliminar["command"] = self.eliminar      
        
    def obtener_fila(self, event):
        tvFunciones = self.nametowidget("tvFunciones")
        current_item = tvFunciones.focus()
        if current_item:
            data = tvFunciones.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Funcion(self)

    def editar(self): 
        if self.select_id != -1: 
            Funcion(self, self.select_id)
        else:
            tkMsgBox.showinfo(self.master.title(), "Error de seleccion de registro!!!!")

    def eliminar(self):
        if self.select_id != -1:
            answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
            if answer:
                func.eliminar(self.select_id)
                self.refrescar()
        else:
            tkMsgBox.showinfo(self.master.title(), "Error de seleccion de registro!!!!")
        

    def refrescar(self):        
        tvFunciones = self.nametowidget("tvFunciones")
        for record in tvFunciones.get_children():
            tvFunciones.delete(record)
        funciones = func.listar()
        print(funciones)
        for fun in funciones:
            tvFunciones.insert("", END, text=fun[0], values=(fun[1], fun[2], fun[3], fun[4])) 