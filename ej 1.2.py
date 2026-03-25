from tkinter import * 
import tkinter as tk

class Alineacion:
    def __init__(self,root):
        self.root = root
        self.root.title("Alineación")
        self.root.geometry("600x770")
        self.root.resizable(False, False)

        self.imgs = []

        self.canvas = tk.Canvas(root, width=600, height=770, highlightthickness=0)
        self.canvas.pack()
        
        self.cargar_cancha()
        self.cargar_iconos()
        self.ubicar_iconos()
        
    def cargar_cancha(self):
        self.cancha = tk.PhotoImage(file="a/cancha-.png")
        self.canvas.create_image(300, 385, image=self.cancha)
        
    def cargar_iconos(self):
        
        for e in range (1,12):
            img = tk.PhotoImage(file=f"a/icon{e}.png")
            self.imgs.append(img)
    
    def ubicar_iconos(self):
        self.canvas.create_image(300, 750, image=self.imgs[0])


        self.canvas.create_image(100, 640, image=self.imgs[1])
        self.canvas.create_image(200, 640, image=self.imgs[2])
        self.canvas.create_image(400, 640, image=self.imgs[3])
        self.canvas.create_image(500, 640, image=self.imgs[4])

        self.canvas.create_image(150, 400, image=self.imgs[5])
        self.canvas.create_image(300, 450, image=self.imgs[6])
        self.canvas.create_image(450, 400, image=self.imgs[7])


        self.canvas.create_image(100, 200, image=self.imgs[8])
        self.canvas.create_image(300, 200, image=self.imgs[9])
        self.canvas.create_image(500, 200, image=self.imgs[10])
        
root = tk.Tk()
a = Alineacion(root)
root.mainloop()