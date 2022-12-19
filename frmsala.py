
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.salas as sala

class Sala(tk.Toplevel):
    def __init__(self, master = None, sala_id =  None):
        super().__init__(master)
        self.master = master
        self.sala_id = sala_id
        #setting title
        self.title("Sala")
        #setting window size
        width=250
        height=220
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_986=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_986["font"] = ft
        GLabel_986["fg"] = "#999999"
        GLabel_986["justify"] = "left"
        GLabel_986["text"] = "Nombre"
        GLabel_986.place(x=35,y=10,width=60,height=20)

        GLabel_949=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_949["font"] = ft
        GLabel_949["fg"] = "#999999"
        GLabel_949["justify"] = "left"
        GLabel_949["text"] = "Capacidad"
        GLabel_949.place(x=35,y=50,width=70,height=20)

        GLabel_205=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_205["font"] = ft
        GLabel_205["fg"] = "#999999"
        GLabel_205["justify"] = "left"
        GLabel_205["text"] = "Formato"
        GLabel_205.place(x=35,y=90,width=60,height=20)

        GLineEdit_119=tk.Entry(self, name = "txtNombre")
        GLineEdit_119["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_119["font"] = ft
        GLineEdit_119["fg"] = "#333333"
        GLineEdit_119["justify"] = "left"
        GLineEdit_119["text"] = ""
        GLineEdit_119.place(x=40,y=30,width=112,height=20)

        GLineEdit_522=tk.Entry(self, name = "txtCapacidad")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "left"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=40,y=70,width=111,height=20)

        GLineEdit_557=tk.Entry(self, name = "txtFormato")
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "left"
        GLineEdit_557["text"] = ""
        GLineEdit_557.place(x=40,y=110,width=111,height=20)

        GButton_215=tk.Button(self)
        GButton_215["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_215["font"] = ft
        GButton_215["fg"] = "#000000"
        GButton_215["justify"] = "center"
        GButton_215["text"] = "Aceptar"
        GButton_215.place(x=40,y=150,width=60,height=20)
        GButton_215["command"] = self.aceptar

        GButton_901=tk.Button(self)
        GButton_901["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "Cancelar"
        GButton_901.place(x=110,y=150,width=60,height=20)
        GButton_901["command"] = self.cancelar

        if sala_id is not None:
            salaa = sala.obtener_id(sala_id)
            
            if salaa is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la sala, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_119.insert(0, salaa[1])
                GLineEdit_522.insert(0, salaa[2])
                GLineEdit_557.insert(0, salaa[3])

    def aceptar(self):
        try:
            nom = self.get_value("txtNombre")
            cap = self.get_value("txtCapacidad")
            form = self.get_value("txtFormato")

            #validar datos
            if nom == "" or form == "" or cap == "":
                tkMsgBox.showerror(self.master.title(), "algun campo esta vacío.")
                return

            #si sala_id esta vacio entonces se agrega nuevo registro
            if self.sala_id is None:
                if not sala.existe(nom):
                    sala.agregar(nom, cap, form)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Sala existente en nuestros registros")
                print("alta nueva de sala")
                #guardar los datos en la bd
            else:
                print("edicion de sala")
                sala.actualizar(self.sala_id, nom, cap, form) 
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()
                #guardar los datos en la bd       
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cancelar(self):
        self.destroy()

    def get_value(self, name):
        return self.nametowidget(name).get()
