"""
Department
"""
from Faculty import Faculty

class Department:
    
    # Constructor
    def __init__(self, deptname, university, numofmembers, firstname, lastname, academiclevel):
        self.deptname = deptname
        self.university = university
        self.numofmembers = numofmembers
        self.currentfaculty = Faculty(firstname, lastname, academiclevel)

    # Getters
    def getdeptname(self):
        return self.deptname
    def getuniversity(self):
        return self.university
    def getnumofmembers(self):
        return self.numofmembers
    def getfaculty(self):
        return self.currentfaculty

    # Setters
    def setdeptname(self, a):
        self.deptname = str(a)
    def setnumofmembers(self, a):
        self.numofmembers = int(a)
    def setuniversity(self, a):
        self.university = str(a)
    def setfaculty(self, firstname, lastname, academiclevel):
        self.currentfaculty.setfirstname(str(firstname))
        self.currentfaculty.setlastname(str(lastname))
        self.currentfaculty.setacademiclevel(str(academiclevel))

    def __repr__(self):
        return ("\nDept. Name:\t\t" + self.deptname +
                "\n" + "University:\t\t" + self.university +
                "\n" + "# of Members:\t" + str(self.numofmembers) +
                "\n" + "Faculty:\t\t" + str(self.currentfaculty) +
                "\n")
        
