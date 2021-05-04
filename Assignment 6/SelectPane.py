"""
SelectPane
"""
from tkinter import *

class SelectPane(Frame):
    def handle(self, event, index):
        if self.checkvars[index] == 0:
            self.numselectedfaculties = self.numselectedfaculties + self.numfacs[index]
            self.checkvars[index] = 1
        else:
            self.numselectedfaculties = self.numselectedfaculties - self.numfacs[index]
            self.checkvars[index] = 0
        self.selectedfaculty.config(text = "The total number of faculty for the selected department(s): " + str(self.numselectedfaculties))
    def __init__(self, newlist, master):

        # Place current frame
        super().__init__(master)
        super().pack(expand = 1, fill = BOTH)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 100)
        self.rowconfigure(2, weight = 1)

        # Place top label
        self.deptselect = Label(self, text = "Select Department(s)")
        self.deptselect.grid(row = 0, column = 0, sticky = W)

        # Place scroll pane
        self.gridpane = Frame(self)
        self.gridpane.grid(row = 1, column = 0, sticky = W+E)
        
        # Place scroll bar
        self.scrollbar = Scrollbar(self.gridpane)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        
        # Place content pane
        self.contentpane = Frame(self.gridpane)
        self.contentpane.pack(expand = 1, fill = BOTH)

        # Place bottom label
        self.selectedfaculty = Label(self, text = "The total number of faculty for the selected department(s): 0")
        self.selectedfaculty.grid(row = 2, column = 0, sticky = W)

        # Initialize other instance variables
        self.departlist = newlist
        self.checkboxes = list()
        self.checkvars = list()
        self.numfacs = list()
        self.numselectedfaculties = 0
        
    def updatedepartlist(self, newdep):
        self.checkvars.append(0)
        self.departlist.append(newdep)
        self.numfacs.append(newdep.getnumberofmembers())
        self.checkboxes.append(Checkbutton(self.contentpane))
        label = Label(self.contentpane, text = (str(newdep)))
        rownum = int(len(self.checkboxes) - 1)
        label.grid(row = rownum, column = 1)
        
        # Set event handler to checkbutton
        self.checkboxes[len(self.checkboxes) - 1].bind("<Button>", lambda event, arg=(len(self.checkboxes) - 1):self.handle(event,arg))

        # Add Checkbutton to gridpane
        self.checkboxes[len(self.checkboxes) - 1].grid(row = (len(self.checkboxes) - 1), column = 0)


                                                       
        
