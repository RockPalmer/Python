"""
Department
"""
class Department:
    name = ""
    numberoffaculty = -1
    university = ""
    def __init__(self):
        self.name = "?"
        self.numberoffaculty = 0
        self.university = "?"
    def getdeptname(self):
        return self.name
    def getnumberofmembers(self):
        return self.numberoffaculty
    def getuniversity(self):
        return self.university
    def setdeptname(self, name):
        self.name = name
    def setnumberofmembers(self, numfaculty):
        self.numberoffaculty = numfaculty
    def setuniversity(self, name):
        self.university = name
    def __repr__(self):
        return ("\nDepartment Name:\t\t" + self.name + "\nNumber Of Faculty:\t" + str(self.numberoffaculty) + "\nUniversity:\t\t" + self.university + "\n\n")
