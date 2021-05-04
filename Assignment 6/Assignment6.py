"""
Assignment6
"""
from GeneratePane import *
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("900x400")
departlist = list()
tabpane = ttk.Notebook(root)
tab2 = ttk.Frame(tabpane)
tabpane.add(tab2, text = "Select Department")
selectpane = SelectPane(departlist, tab2)
tab1 = ttk.Frame(tabpane)
tabpane.add(tab1, text = "Add Department")
createpane = GeneratePane(departlist, selectpane, tab1)
tabpane.pack(expand = 1, fill = BOTH)
root.mainloop()
