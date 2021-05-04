"""
Faculty
"""
class Faculty:
    def __init__(self, firstname, lastname, academiclevel):
        self.firstname = firstname
        self.lastname = lastname
        self.academiclevel = academiclevel
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def getacademiclevel(self):
        return self.academiclevel
    def setfirstname(self, firstname):
        self.firstname = firstname
    def setlastname(self, lastname):
        self.lastname = lastname
    def setacademiclevel(self, academiclevel):
        self.academiclevel = academiclevel
    def __repr__(self):
        return (self.firstname + " " + self.lastname + ", " + self.academiclevel)
