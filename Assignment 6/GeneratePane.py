"""
GeneratePane
"""
from SelectPane import SelectPane
from Department import Department
from tkinter import *
        
class GeneratePane(Frame):
    def handle(self, event):
        dettitle = ""
        faculties = 0
        nameuniv = ""
        isemptyfields = False
        alreadyexists = False
        if self.titleentry.get() == "" or self.numentry.get() == "" or self.nameentry.get() == "":
            isemptyfields = True
        if isemptyfields:
            self.errlabel.config(text = "Please fill all fields")
        else:
            try:
                newdepart = Department()
                depttitle = self.titleentry.get()
                faculties = int(self.numentry.get())
                nameuniv = self.nameentry.get()

                # If data was valid, no exceptions would have occured by this point

                # Check for any duplicate departments
                count = 0
                while count < len(self.departlist) and alreadyexists == False:
                    depttocheck = self.departlist[count]
                    if depttocheck.getdeptname() == depttitle and depttocheck.getnumberofmembers() == faculties and depttocheck.getuniversity() == nameuniv:
                        alreadyexists = True
                        raise Exception
                    count = count + 1
                
                # If there are no duplicate Departments, add the user's Department to the list
                if alreadyexists == False:
                    
                    # Set attributes of new Department object
                    newdepart.setdeptname(depttitle)
                    newdepart.setnumberofmembers(faculties)
                    newdepart.setuniversity(nameuniv)

                    # Add the new Department to the list
                    self.departlist.append(newdepart)

                    #  Clear the user-entry boxes
                    self.titleentry.delete(0,END)
                    self.numentry.delete(0,END)
                    self.nameentry.delete(0,END)

                    # Reset the text in 'departments'
                    if self.departments.get(1.0, 1.13) == "No department":
                        self.departments.delete(1.0, END)
                    currtext = self.departments.get(1.0, END)
                    self.departments.delete(1.0,END)
                    self.departments.insert(1.0, (currtext + str(newdepart)))

                    # Use the 'errLabel' Label to tell the user that their Department was added
                    self.errlabel.config(text = "Department added")

                    # Update the info in the other tab of the GUI
                    self.selectpane.updatedepartlist(newdepart)
            except (ValueError):
                self.errlabel.config(text = "Please enter an integer for the number of faculty")
            except (Exception):
                if alreadyexists == True:
                    self.errlabel.config(text = "Department not added - already exist")
    def __init__(self, newlist, sepane, master):
        super().__init__(master)
        super().pack(fill = BOTH)

        # All Frame objects
        gridpane = Frame(self)
        gridpane.pack(expand = 1, fill = BOTH)
        leftpane = Frame(gridpane)
        entrypane = Frame(leftpane)
        buttonpane = Frame(leftpane)

        # All instance variables
        self.departlist = newlist
        self.selectpane = sepane
        self.titleentry = Entry(entrypane)
        self.numentry = Entry(entrypane)
        self.nameentry = Entry(entrypane)
        self.errlabel = Label(leftpane)
        self.departments = Text(gridpane)

        # All other GUI components needed
        depttitle = Label(entrypane)
        numfaculty = Label(entrypane)
        univname = Label(entrypane)
        adddept = Button(buttonpane, text = "Add a Department")
        
        # Build layout
        gridpane.columnconfigure(0, weight = 1)
        gridpane.columnconfigure(1, weight = 1)

        # Set layout of nodes on gridpane
        self.departments.grid(row = 0, column = 1, sticky = E)
        self.departments.config(width = 55)
        if len(self.departlist) == 0:
            self.departments.insert('1.0', "No department")
        else:
            count = 0
            while count < len(self.departlist):
                currtext = self.departments.get('1.0', END)
                self.departments.delete('1.0', END)
                currtext = currtext + str(self.departlist[count])
                self.departments.insert('1.0', currtext)
                count = count + 1

        # Set layout of left side of pane
        leftpane.grid(row = 0, column = 0)

        # Set attributes of error message
        self.errlabel.configure(fg = 'red')
        self.errlabel.grid(row = 0, column = 0, sticky = N)

        # Set layout of user input area
        entrypane.grid(row = 1, column = 0)
        entrypane.columnconfigure(0, weight = 2)
        entrypane.columnconfigure(1, weight = 2)

        # Add the 3 labels to the 'entrypane' object
        depttitle.config(text = "Department Title")
        depttitle.grid(row = 0, column = 0)
        numfaculty.config(text = "Number of Faculty")
        numfaculty.grid(row = 1, column = 0)
        univname.config(text = "Name of University")
        univname.grid(row = 2, column = 0)

        # Add the 3 user-entry boxes to the 'entrypane' object
        self.titleentry.grid(row = 0, column = 1)
        self.numentry.grid(row = 1, column = 1)
        self.nameentry.grid(row = 2, column = 1)

        # Add the 'buttonpane' object
        buttonpane.grid(row = 2, column = 0)

        # Add the 'adddept' button to buttonpane
        adddept.pack(side = TOP)

        # Set event handler to adddept
        adddept.bind("<Button>", self.handle)
