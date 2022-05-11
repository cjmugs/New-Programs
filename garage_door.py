from tkinter import *
from tkinter import ttk

def new_gui():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Basic GUI").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Denotate", command=root.destroy).grid(column=2, row=0)
    root.mainloop()
    
new_gui()