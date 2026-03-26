from tkinter import * 
import tkinter as tk

class SistemaGestion:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistema de Gestion de Inventario")
        self.root.geometry("600x500")
        root.configure(bg='snow')

        for e in range(2):
            self.root.columnconfigure({e}, weight= 1)
        self.root.rowconfigure(0, weight=1)

        self.panelIzq = tk.LabelFrame(self.root, text="Panel de Operaciones",bg= "misty rose")
        self.panelIzq.grid(row=0, column= 0, padx=20, pady=20, sticky="nsew")

        self.panelentry = tk.LabelFrame()

        panelDer = tk.LabelFrame(self.root, text="Inventario", bg = "misty rose")
        panelDer.grid(row=0, column=1, padx=20, pady=20, sticky="nsew" )

        for e in range(5):
            self.panelIzq.rowconfigure({e},weight=1)

        for e in range(5):
            self.panelIzq.columnconfigure({e},weight=1)
        

        id_label = tk.Label(self.panelIzq,text= "Nombre:", bg= "misty rose")
        id_label.grid(row = 0, column=0,padx=1,pady=1, sticky="ew")

        id_entry = tk.Entry(self.panelIzq, justify="left")
        id_entry.grid(row=0, column=2)
        


    def guardar(self):
        pass

    def modificar(self):
        pass

    def borrar_registro(self):
        pass



root = tk.Tk()
r = SistemaGestion(root)
root.mainloop()