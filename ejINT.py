import tkinter as tk
from tkinter import ttk

class SistemaGestion:
    def __init__(self,root):
        self.root = root
        self.title = "Sistema de Gestion de Inventario"
        self.root.state('zoomed')

        panelIzq = ttk.LabelFrame(self.root, text="Panel de Operaciones", padding=(20))
        panelIzq.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

        #panelIzq = ttk.LabelFrame(self.root, text="Panel de Operaciones")
        #panelIzq.pack(padx=0, pady=10)
        
        # ID LABEL - ENTRY

        self.id_label = tk.Label(panelIzq, text="Name:")
        self.id_label.grid(row =0, column=0, padx= 5, pady=5, sticky= "e")

        self.id_entry= tk.Entry(panelIzq)
        self.id_entry.grid(row =0, column=2, padx= 5, pady=5, sticky= "w")

        # DESC LABEL -ENTRY

        self.desc_label = tk.Label(panelIzq, text= "Descripción:")
        self.desc_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

        self.desc_entry = tk.Entry(panelIzq)
        self.desc_entry.grid(row = 1, column= 2, padx= 5, pady= 5, sticky= "w")

        #STOCK LABEL-ENTRY

        self.stock_label = tk.Label(panelIzq, text= "Stock:")
        self.stock_label.grid(row= 3, column=0, padx= 5, pady=5, sticky="e")

        self.stock_entry = tk.Entry(panelIzq)
        self.stock_entry.grid(row=3, column=2, padx= 5, pady= 5, sticky="w")
        
        #Treeview

        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        panelIzq.columnconfigure(1, weight=1)


    def guardar(self):
        pass

    def modificar(self):
        pass

    def borrar_registro(self):
        pass



root = tk.Tk()
r = SistemaGestion(root)
root.mainloop()


columnas = ('ID', 'Nombre', 'Edad')
tree = ttk.Treeview(root, columns=columnas, show='headings')

tree.heading('ID', text='ID')
tree.heading('Nombre', text='Nombre')
tree.heading('Edad', text='Edad')

tree.insert('', tk.END, values=('1', 'Ana', '25'))
tree.insert('', tk.END, values=('2', 'Luis', '30'))
tree.insert('', tk.END, values=('3', 'Pedro', '22'))

tree.pack(expand=True, fill='both')

root.mainloop()