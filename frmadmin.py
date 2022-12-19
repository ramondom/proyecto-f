import tkinter as tk
import tkinter.font as tkFont
from frmusers import Users
from frmsalas import Salas
from frmpelis import Peliculas
from frmfunciones import Funciones

class Dashboard(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Principal")        
        width=548
        height=307
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_996=tk.Label(self)
        ft = tkFont.Font(family='Times',size=15, weight='bold')
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#333333"
        GLabel_996["justify"] = "left"
        GLabel_996["text"] = "Administración:"
        GLabel_996.place(x=150,y=10,width=200,height=30)
        
        GButton_245=tk.Button(self)
        GButton_245["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "Usuarios"
        GButton_245["relief"] = "ridge"
        GButton_245.place(x=30,y=60,width=135,height=45)
        GButton_245["command"] = self.abrir_usuarios

        GButton_196=tk.Button(self)
        GButton_196["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        GButton_196["font"] = ft
        GButton_196["fg"] = "#000000"
        GButton_196["justify"] = "center"
        GButton_196["text"] = "Salas"
        GButton_196["relief"] = "ridge"
        GButton_196.place(x=190,y=60,width=135,height=45)
        GButton_196["command"] = self.abrir_salas

        GButton_430=tk.Button(self)
        GButton_430["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Descuentos"
        GButton_430["relief"] = "ridge"
        GButton_430.place(x=350,y=60,width=135,height=45)
        GButton_430["command"] = self.abrir_descuentos

        usuarios=tk.Button(self)
        usuarios["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        usuarios["font"] = ft
        usuarios["fg"] = "#000000"
        usuarios["justify"] = "center"
        usuarios["text"] = "Reservas"
        usuarios["relief"] = "ridge"
        usuarios.place(x=30,y=120,width=135,height=45)
        usuarios["command"] = self.abrir_reservas

        funciones=tk.Button(self)
        funciones["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        funciones["font"] = ft
        funciones["fg"] = "#000000"
        funciones["justify"] = "center"
        funciones["text"] = "Funciones"
        funciones["relief"] = "ridge"
        funciones.place(x=190,y=120,width=135,height=45)
        funciones["command"] = self.abrir_funciones

        pel=tk.Button(self)
        pel["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        pel["font"] = ft
        pel["fg"] = "#000000"
        pel["justify"] = "center"
        pel["text"] = "Peliculas"
        pel["relief"] = "ridge"
        pel.place(x=350,y=120,width=135,height=45)
        pel["command"] = self.abrir_peliculas

    def abrir_usuarios(self):
        Users(self)

    def abrir_salas(self):
        Salas(self)

    def abrir_descuentos(self):
        print("descuentos")

    def abrir_reservas(self):
        print("reservas")

    def abrir_funciones(self):
        Funciones(self)

    def abrir_peliculas(self):
        Peliculas(self)