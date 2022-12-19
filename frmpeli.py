from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.pelis as peli

class Pelicula(Toplevel):
    def __init__(self, master=None, peli_id = None):        
        super().__init__(master)
        self.master = master
        self.peli_id = peli_id       
        self.title("Pelicula")
        #setting window size
        width=383
        height=431
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_572=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_572["font"] = ft
        GLabel_572["fg"] = "#999999"
        GLabel_572["justify"] = "center"
        GLabel_572["text"] = "Titulo"
        GLabel_572.place(x=15,y=35,width=94,height=30)

        Gtit=Entry(self, name="txtTitulo")
        Gtit["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Gtit["font"] = ft
        Gtit["fg"] = "#333333"
        Gtit["justify"] = "left"
        Gtit["text"] = ""
        Gtit.place(x=40,y=60,width=250,height=30)

        GLabel_102=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_102["font"] = ft
        GLabel_102["fg"] = "#999999"
        GLabel_102["justify"] = "center"
        GLabel_102["text"] = "Descripcion"
        GLabel_102.place(x=35,y=105,width=92,height=30)

        Gdesc= Entry(self, name="txtDescripcion")
        Gdesc["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Gdesc["font"] = ft
        Gdesc["fg"] = "#333333"
        Gdesc["justify"] = "left"
        Gdesc["text"] = ""
        Gdesc.place(x=40,y=130,width=301,height=30)

        GLabel_464= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#999999"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Genero"
        GLabel_464.place(x=35,y=165,width=70,height=25)

        Ggen= Entry(self, name="txtGenero")
        Ggen["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Ggen["font"] = ft
        Ggen["fg"] = "#333333"
        Ggen["justify"] = "left"
        Ggen["text"] = ""
        Ggen.place(x=40,y=190,width=172,height=30)

        GLabel_14= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_14["font"] = ft
        GLabel_14["fg"] = "#999999"
        GLabel_14["justify"] = "center"
        GLabel_14["text"] = "Actores"
        GLabel_14.place(x=35,y=220,width=70,height=20)

        Gact= Entry(self, name="txtActores")
        Gact["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Gact["font"] = ft
        Gact["fg"] = "#333333"
        Gact["justify"] = "left"
        Gact["text"] = ""
        Gact.place(x=40,y=240,width=232,height=30)

        GLabel_656= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#999999"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "Duracion"
        GLabel_656.place(x=35,y=275,width=70,height=25)

        Gdurac= Entry(self, name="txtDuracion")
        Gdurac["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Gdurac["font"] = ft
        Gdurac["fg"] = "#333333"
        Gdurac["justify"] = "left"
        Gdurac["text"] = ""
        Gdurac.place(x=40,y=300,width=139,height=30)

        GButton_924= Button(self)
        GButton_924["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_924["font"] = ft
        GButton_924["fg"] = "#000000"
        GButton_924["justify"] = "center"
        GButton_924["text"] = "Aceptar"
        GButton_924.place(x=140,y=360,width=70,height=25)
        GButton_924["command"] = self.aceptar

        GButton_220= Button(self)
        GButton_220["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_220["font"] = ft
        GButton_220["fg"] = "#000000"
        GButton_220["justify"] = "center"
        GButton_220["text"] = "Cancelar"
        GButton_220.place(x=240,y=360,width=70,height=25)
        GButton_220["command"] = self.cancelar

        #si peli_id se pasa como parametro 
        if peli_id is not None:
            pelicula = peli.obtener_id(peli_id)
            
            if pelicula is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                Gtit.insert(0, pelicula[0])
                Gdesc.insert(0, pelicula[1])
                Ggen.insert(0, pelicula[2])
                Gact.insert(0, pelicula[3])
                Gdurac.insert(0, pelicula[4])           

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def cancelar(self):
        self.destroy()

    def aceptar(self):
        try:            
            titulo = self.get_value("txtTitulo")
            descripcion = self.get_value("txtDescripcion")            
            genero = self.get_value("txtGenero")            
            actores = self.get_value("txtActores")
            duracion = self.get_value("txtDuracion")            
    
            # TODO validar los datos antes de ingresar
            if titulo == "" or descripcion == "" or genero == "" or actores == "" or duracion == "":
                tkMsgBox.showerror(self.master.title(), "todos los campos deben estar completos.")
                return

            if self.peli_id is None:
                print("Alta de pelicula")
                if not peli.existe(titulo):
                    peli.agregar(titulo, descripcion, genero, actores, duracion)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Pelicula existente en nuestros registros")
            else:
                print("Actualizacion de pelicula")
                peli.actualizar(self.peli_id, titulo, descripcion, genero, actores, duracion)
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))