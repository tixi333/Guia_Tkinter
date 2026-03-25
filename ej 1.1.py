from tkinter import *
import tkinter as tk

class Calculadora:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x700")
        self.root.title("Calculadora")
        self.root.resizable(False,False)
        self.root.configure(bg="pink")
   
        self.screen = Entry(
                root,
                width=20,
                font=("Arial", 24),
                justify="right",
                bg="white",
                fg="pink",
                bd=15,
                )
        
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=15)

        self.expresion = ""
        buttons = [
            ("Ce",1,0), ("AC",1,1), ("√",1,2), ("^",1,3),
            ("7",2,0), ("8",2,1), ("9",2,2), ("/",2,3),
            ("4",3,0), ("5",3,1), ("6",3,2), ("*",3,3),
            ("1",4,0), ("2",4,1), ("3",4,2), ("-",4,3),
            ("0",5,0), (".",5,1), ("=",5,2), ("+",5,3)
        ]
        
        for text, row, col in buttons:
            
            if text == "Ce":
                Ce= tk.Button(root,
                          text= text,
                          command= self.delete,
                          bg = "pink",
                          activebackground= "pink1",
                          activeforeground="white")
                Ce.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
                
            elif text == "=":
                Equal = tk.Button(root,text= text, command= self.calculate, bg = "pink", activebackground= "pink1",activeforeground="white")
                Equal.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
                
            elif text == "AC":
                AC = tk.Button(root,
                               text= text,
                               command= self.delete_all, 
                               bg = "pink",
                               activebackground= "pink1",
                               activeforeground="white")
                AC.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
            
            elif text == "√":
                sqrt = tk.Button(root,
                                 text= text,
                                 command=lambda: self.add("**0.5"), 
                                 bg = "pink",
                                 activebackground= "pink1",
                                 activeforeground="white")
                sqrt.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
            
            elif text == "^":
                pow_ = tk.Button(root,
                                 text= text,
                                 command=lambda: self.add("**"), 
                                 bg = "pink",
                                 activebackground= "pink1",
                                 activeforeground="white")
                
                pow_.grid(row=row,column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew" )
                
            else:
                keys= tk.Button(root,
                          text= text,
                          command=lambda t=text: self.add(t),
                          bg = "pink", 
                          activebackground= "pink1",
                          activeforeground="white")
                keys.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
        
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        
        root.bind("<Return>", lambda event: self.calculate())
        root.bind("<BackSpace>", lambda event: self.delete())
        
        for key in "0123456789+-*/.":
            root.bind(f"<Key-{key}>", lambda event, t=key: self.add(t))
            
    def add(self,value):
        op = "+-*/.^"
        try:
            for char in value:
                if char not in "0123456789+-*/.^()":
                    raise ValueError("Error")
                
            if self.expresion:
                if self.expresion[-1] in op and value in op:
                    return
                
            if not self.expresion and value in op:
                return
        except ValueError:
            self.screen.delete(0, END)
            self.screen.insert(END, "Error")
            self.expresion = ""
            return
        else:
            self.expresion += value
            self.screen.delete(0, END)
            self.screen.insert(END, self.expresion)
            
    
    def delete(self):
        self.expresion = self.expresion[:-1]
        self.screen.delete(0, END)
        self.screen.insert(END, self.expresion)
    
    def delete_all(self):
        self.expresion = ""
        self.screen.delete(0, END)
    
    def calculate(self):
        try:
            resultado = str(eval(self.expresion))
            self.screen.delete(0, END)
            self.screen.insert(END, resultado)
            self.expresion = resultado
        except:
            self.screen.delete(0,END)
            self.screen.insert(END, "Error")
            self.expresion = ""
        
        
root = tk.Tk()
a = Calculadora(root)
root.mainloop()