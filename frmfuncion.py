from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.funciones as func

class Funcion(Toplevel):
    def __init__(self, master=None, func_id = None):        
        super().__init__(master)
        self.master = master
        self.func_id = func_id       
        self.title("Funcion")
        #setting window size
        width=383
        height=350
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
        GLabel_572["text"] = "Fecha"
        GLabel_572.place(x=15,y=35,width=94,height=30)

        Getiq=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Getiq["font"] = ft
        Getiq["fg"] = "#333333"
        Getiq["justify"] = "center"
        Getiq["text"] = "dd/mm/aaaa"
        Getiq.place(x=220,y=60,width=70,height=30)

        Gfech=Entry(self, name="txtFecha")
        Gfech["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Gfech["font"] = ft
        Gfech["fg"] = "#333333"
        Gfech["justify"] = "left"
        Gfech["text"] = ""
        Gfech.place(x=40,y=60,width=150,height=30)

        GLabel_102=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_102["font"] = ft
        GLabel_102["fg"] = "#999999"
        GLabel_102["justify"] = "center"
        GLabel_102["text"] = "Hora"
        GLabel_102.place(x=35,y=105,width=50,height=30)

        Geti=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Geti["font"] = ft
        Geti["fg"] = "#333333"
        Geti["justify"] = "center"
        Geti["text"] = "hh:mm"
        Geti.place(x=215,y=130,width=60,height=30)

        Ghora= Entry(self, name="txtHora")
        Ghora["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Ghora["font"] = ft
        Ghora["fg"] = "#333333"
        Ghora["justify"] = "left"
        Ghora["text"] = ""
        Ghora.place(x=40,y=130,width=150,height=30)

        GLabel_464= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#999999"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Pelicula"
        GLabel_464.place(x=35,y=165,width=68,height=25)

        
        pel = dict(func.listarP())
        print(pel)
        cb_pelis = ttk.Combobox(self, state="readonly", values=list(pel.values()), name="cbPeli")
        cb_pelis.place(x=40,y=190,width=320,height=30)

        GLabel_14= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_14["font"] = ft
        GLabel_14["fg"] = "#999999"
        GLabel_14["justify"] = "center"
        GLabel_14["text"] = "Sala"
        GLabel_14.place(x=35,y=220,width=50,height=20)

        
        sala = dict(func.listarS())
        print(sala)
        cb_salas = ttk.Combobox(self, state="readonly", values=list(sala.values()), name="cbSala")
        cb_salas.place(x=40,y=240,width=80,height=30)

        GButton_924= Button(self)
        GButton_924["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_924["font"] = ft
        GButton_924["fg"] = "#000000"
        GButton_924["justify"] = "center"
        GButton_924["text"] = "Aceptar"
        GButton_924.place(x=140,y=290,width=70,height=25)
        GButton_924["command"] = self.aceptar

        GButton_220= Button(self)
        GButton_220["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_220["font"] = ft
        GButton_220["fg"] = "#000000"
        GButton_220["justify"] = "center"
        GButton_220["text"] = "Cancelar"
        GButton_220.place(x=240,y=290,width=70,height=25)
        GButton_220["command"] = self.cancelar

        #si peli_id se pasa como parametro 
        if func_id is not None:
            funcion = func.obtener_id(func_id)
            print(funcion)
            if funcion is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la Pelicula, reintente nuevamente")
               self.destroy()
            else:
                Gfech.insert(0, funcion[1])
                Ghora.insert(0, funcion[2])
                cb_pelis.set(funcion[3])
                cb_salas.set(funcion[4])        

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def cancelar(self):
        self.destroy()

    def aceptar(self):
        try:            
            fecha = self.get_value("txtFecha")
            hora = self.get_value("txtHora")            
            pelId = self.get_index("cbPeli")
            salaId = self.get_index("cbSala")         
            print(pelId)
            print(salaId)
            # TODO validar los datos antes de ingresar
            if fecha == "" or hora == "" or pelId == "" or salaId == "":
                tkMsgBox.showerror(self.master.title(), "todos los campos deben estar completos.")
                return

            if self.func_id is None:
                print("Alta de funcion")
                if not func.existe(fecha, hora, pelId, salaId): #####ver existe()
                    func.agregar(fecha, hora, pelId, salaId)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Funcion existente en nuestros registros")
            else:
                print("Actualizacion de Funcion")
                func.actualizar(self.peli_id, fecha, hora, pel, sala)
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))