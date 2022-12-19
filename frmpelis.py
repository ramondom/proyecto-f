from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
from frmpeli import Pelicula
import bll.pelis as pelic

class Peliculas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Películas")        
        width=940
        height=400
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
        GLabel_464["text"] = "Peliculas:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("tit", "desc", "gen", "act", "durac"), name="tvPelis")
        tv.column("#0", width=20)
        tv.column("tit", width=200, anchor=CENTER)
        tv.column("desc", width=300, anchor=CENTER)
        tv.column("gen", width=100, anchor=CENTER)
        tv.column("act", width=150, anchor=CENTER)
        tv.column("durac", width=100, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("tit", text="Título", anchor=CENTER)
        tv.heading("desc", text="Descripcion", anchor=CENTER)
        tv.heading("gen", text="Género", anchor=CENTER)
        tv.heading("act", text="Actores", anchor=CENTER)
        tv.heading("durac", text="Duracion", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=30,width=920,height=310)    

        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=300,y=355,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=380,y=355,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=460,y=355,width=70,height=25)
        btn_eliminar["command"] = self.eliminar      
        
    def obtener_fila(self, event):
        tvPelis = self.nametowidget("tvPelis")
        current_item = tvPelis.focus()
        if current_item:
            data = tvPelis.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Pelicula(self)

    def editar(self):
        if self.select_id != -1: 
            Pelicula(self, self.select_id)
        else:
            tkMsgBox.showinfo(self.master.title(), "Error de seleccion de registro!!!!")

    def eliminar(self):
        if self.select_id != -1:
            answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
            if answer:
                pelic.eliminar(self.select_id)
                self.refrescar()
        else:
            tkMsgBox.showinfo(self.master.title(), "Error de seleccion de registro!!!!")

    def refrescar(self):        
        tvPelis = self.nametowidget("tvPelis")
        for record in tvPelis.get_children():
            tvPelis.delete(record)
        pelis = pelic.listar()
        print(pelis)
        for peli in pelis:
            tvPelis.insert("", END, text=peli[0], values=(peli[1], peli[2], peli[3], peli[4], peli[5])) 