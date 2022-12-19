from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol
from datetime import date

class User(Toplevel):
    def __init__(self, master=None, isAdmin = False, user_id = None):        
        super().__init__(master)
        self.master = master
        self.user_id = user_id       
        self.title("Registro de cuenta")        
        width=380
        height=440
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_243 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#999999"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Apellido"
        GLabel_243.place(x=50,y=10,width=50,height=20)

        GLineEdit_871 = Entry(self, name="txtApellido")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=50,y=30,width=284,height=20)

        GLabel_599 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#999999"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Nombre"
        GLabel_599.place(x=50,y=50,width=50,height=20)

        GLineEdit_911 = Entry(self, name="txtNombre")
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=50,y=70,width=285,height=20)        

        GLabel_600 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#999999"
        GLabel_600["anchor"] = "e"
        GLabel_600["text"] = "Fecha de nacimiento"
        GLabel_600.place(x=45,y=90,width=120,height=20)

        Getiq=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Getiq["font"] = ft
        Getiq["fg"] = "#333333"
        Getiq["justify"] = "center"
        Getiq["text"] = "dd/mm/aaaa"
        Getiq.place(x=160,y=110,width=70,height=20)

        GLineEdit_208 = Entry(self, name="txtFechaNac")
        GLineEdit_208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_208["font"] = ft
        GLineEdit_208["fg"] = "#333333"
        GLineEdit_208["justify"] = "left"
        GLineEdit_208["text"] = ""
        GLineEdit_208.place(x=50,y=110,width=94,height=20)

        GLabel_737 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#999999"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "DNI"
        GLabel_737.place(x=50,y=130,width=30,height=20)

        GLineEdit_234 = Entry(self, name="txtDni")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=50,y=150,width=133,height=20)

        GLabel_454 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_454["font"] = ft
        GLabel_454["fg"] = "#999999"
        GLabel_454["anchor"] = "e"
        GLabel_454["text"] = "Correo electrónico"
        GLabel_454.place(x=40,y=170,width=115,height=20)

        GLineEdit_384 = Entry(self, name="txtEmail")
        GLineEdit_384["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_384["font"] = ft
        GLineEdit_384["fg"] = "#333333"
        GLineEdit_384["justify"] = "left"
        GLineEdit_384["text"] = ""
        GLineEdit_384.place(x=50,y=190,width=285,height=20)

        GLabel_616 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#999999"
        GLabel_616["anchor"] = "e"
        GLabel_616["text"] = "Usuario"
        GLabel_616.place(x=50,y=210,width=50,height=20)

        GLineEdit_481 = Entry(self, name="txtUsuario")
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "left"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=50,y=230,width=286,height=20)

        GLabel_61 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#999999"
        GLabel_61["anchor"] = "e"
        GLabel_61["text"] = "Contraseña"
        GLabel_61.place(x=50,y=250,width=70,height=20)

        GLineEdit_366 = Entry(self, show="*", name="txtContrasenia")
        GLineEdit_366["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_366["font"] = ft
        GLineEdit_366["fg"] = "#333333"
        GLineEdit_366["justify"] = "left"
        GLineEdit_366["text"] = ""
        GLineEdit_366.place(x=50,y=270,width=286,height=20)        

        GLabel_524 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#999999"
        GLabel_524["anchor"] = "e"
        GLabel_524["text"] = "Confirme contraseña"
        GLabel_524.place(x=50,y=290,width=120,height=20)

        GLineEdit_126 = Entry(self, show="*", name="txtConfirmacion")
        GLineEdit_126["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_126["font"] = ft
        GLineEdit_126["fg"] = "#333333"
        GLineEdit_126["justify"] = "left"
        GLineEdit_126["text"] = ""
        GLineEdit_126.place(x=50,y=310,width=285,height=20)        

        GLabel_975 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#000000"
        GLabel_975["anchor"] = "e"
        GLabel_975["text"] = "Rol"
        GLabel_975.place(x=50,y=330,width=30,height=20)
        
        roles = dict(rol.listar())
        print(rol.listar())
        print(roles)
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[2])
        cb_roles.place(x=50,y=350,width=150,height=20)

        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=50,y=385,width=70,height=25)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=140,y=385,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command

        if user_id is not None:
            usuario = user.obtener_id(user_id)
            
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_871.insert(0, usuario[1])
                GLineEdit_911.insert(0, usuario[2])
                fecha_nac = date(int(usuario[3][:4]), int(usuario[3][5:7]), int(usuario[3][8:]))
                GLineEdit_208.insert(0, fecha_nac.strftime(r"%d/%m/%Y"))
                GLineEdit_234.insert(0, usuario[4])
                GLineEdit_384.insert(0, usuario[5])
                GLineEdit_481.insert(0, usuario[6])
                GLineEdit_481["state"] = "disabled"           
                cb_roles.set(usuario[8])

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try:            
            apellido = self.get_value("txtApellido")
            nombre = self.get_value("txtNombre")            
            fecha_nac = self.get_value("txtFechaNac")            
            dni = self.get_value("txtDni")
            email = self.get_value("txtEmail")            
            usuario = self.get_value("txtUsuario")

            contrasenia = self.get_value("txtContrasenia")            
            confirmacion = self.get_value("txtConfirmacion")
            rol_id = self.get_index("cbRoles")

            # TODO validar los datos antes de ingresar
            if apellido == "":
                tkMsgBox.showerror(self.master.title(), "Apellido es un valor requerido.")
                return
            
            if nombre == "":
                tkMsgBox.showerror(self.master.title(), "Nombre es un valor requerido.")
                return
            
            if contrasenia != confirmacion:
                tkMsgBox.showerror(self.master.title(), "La contraseña con su confirmacion no tienen el mismo valor.")
                return  

            if self.user_id is None:
                print("Alta de usuario")
                if not user.existe(usuario):
                    user.agregar(apellido, nombre, fecha_nac, dni, email, usuario, contrasenia, rol_id)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id, apellido, nombre, fecha_nac, dni, email, contrasenia, rol_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))