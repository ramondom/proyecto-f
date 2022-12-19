import tkinter as tk
import tkinter.font as tkFont
from frmusers import Users
from frmsala import Sala

class Cliente(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Principal")        
        width=480
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
        GLabel_996["text"] = "Clientes:"
        GLabel_996.place(x=130,y=10,width=200,height=30)
        
        resv=tk.Button(self)
        resv["bg"] = "#90b8f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        resv["font"] = ft
        resv["fg"] = "#000000"
        resv["justify"] = "center"
        resv["text"] = "Reservas"
        resv["relief"] = "ridge"
        resv.place(x=30,y=60,width=135,height=45)
        resv["command"] = self.abrir_reservas

    def abrir_reservas(self):
        print('reservas')