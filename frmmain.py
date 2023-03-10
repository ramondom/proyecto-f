import tkinter as tk
import tkinter.font as tkFont
from frmlogin import Login
from dal.db import Db

class App:
    def __init__(self, root, title):
        self.root = root
        #setting title
        root.title(title)
        #setting window size
        width=335
        height=131
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_284=tk.Button(root)
        GButton_284["bg"] = "#90f090"
        ft = tkFont.Font(family='Times',size=10,weight='bold')
        GButton_284["font"] = ft
        GButton_284["fg"] = "#000000"
        GButton_284["justify"] = "center"
        GButton_284["text"] = "Abrir " + title
        GButton_284["relief"] = "groove"
        GButton_284.place(x=75,y=40,width=200,height=30)
        GButton_284["command"] = self.abrir_login

    def abrir_login(self):
        Login(self.root)

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    project = "cinemark"
    root = tk.Tk()
    root.iconbitmap(default=f"{project}.ico")
    app = App(root, project.capitalize())
    root.mainloop()
