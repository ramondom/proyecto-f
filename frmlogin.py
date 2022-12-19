import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from frmuser import User
from frmadmin import Dashboard
from frmclientes import Cliente
import bll.usuarios as user

class Login(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Login")        
        width=305
        height=250
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLineEdit_223=tk.Entry(self, name="txtUsuario")
        GLineEdit_223["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_223["font"] = ft
        GLineEdit_223["fg"] = "#333333"
        GLineEdit_223["justify"] = "left"
        GLineEdit_223["text"] = ""
        GLineEdit_223.place(x=50,y=35,width=200,height=30)

        GLineEdit_666=tk.Entry(self, name ="txtContrasenia", show="*")
        GLineEdit_666["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_666["font"] = ft
        GLineEdit_666["fg"] = "#333333"
        GLineEdit_666["justify"] = "left"
        GLineEdit_666["text"] = ""
        GLineEdit_666.place(x=50,y=100,width=200,height=30)

        GLabel_521=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_521["font"] = ft
        GLabel_521["fg"] = "#333333"
        GLabel_521["justify"] = "right"
        GLabel_521["text"] = "Usuario"
        GLabel_521.place(x=50,y=15,width=50,height=20)

        GLabel_214=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_214["font"] = ft
        GLabel_214["fg"] = "#333333"
        GLabel_214["justify"] = "right"
        GLabel_214["text"] = "Contraseña"        
        GLabel_214.place(x=50,y=80,width=65,height=20)

        GButton_793=tk.Button(self)
        GButton_793["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_793["font"] = ft
        GButton_793["fg"] = "#000000"
        GButton_793["justify"] = "center"
        GButton_793["text"] = "Aceptar"
        GButton_793.place(x=90,y=145,width=70,height=25)
        GButton_793["command"] = self.iniciar_sesion

        GButton_100=tk.Button(self)
        GButton_100["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_100["font"] = ft
        GButton_100["fg"] = "#000000"
        GButton_100["justify"] = "center"
        GButton_100["text"] = "Cancelar"
        GButton_100.place(x=170,y=145,width=70,height=25)
        GButton_100["command"] = self.cancelar

        GButton_946=tk.Button(self)
        GButton_946["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10, underline=True, weight='bold',slant='italic')
        GButton_946["font"] = ft
        GButton_946["fg"] = "#1f93ff"
        GButton_946["justify"] = "center"
        GButton_946["text"] = "Crear cuenta"
        GButton_946.place(x=115,y=190,width=101,height=25)
        GButton_946["command"] = self.abrir_user
        GButton_946["border"] = 0        

    def iniciar_sesion(self):
        try:
            usuario = self.nametowidget("txtUsuario").get()            
            contrasenia = self.nametowidget("txtContrasenia").get()

            if usuario != "":
                if user.validar(usuario, contrasenia):                    
                    usuario = user.obtener_nombre_usuario(usuario)
                    
                    if usuario is not None:
                        if usuario[8] == "Administrador":
                            Dashboard(self.master)
                            self.destroy()
                        elif usuario[8] == "Cliente":
                            # TODO chequear el rol del usuario para abrir el menu/ventana correspondiente
                            Cliente(self.master)
                            self.destroy()
                    else:
                        tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cancelar(self):
        self.destroy()

    def abrir_user(self):
        User(self.master, True)