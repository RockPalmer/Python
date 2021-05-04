class Faculty:
    ''
    firstName = ""
    lastName = ""
    academicLevel = ""
    def __init__(self):
        self.firstName = "?"
        self.lastName = "?"
        self.academicLevel = "?"
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getAcademicLevel(self):
        return self.academicLevel
    def setFirstName(self, fName):
        self.firstName = fName
    def setLastName(self, lName):
        self.lastName = lName
    def setAcademicLevel(self, acLevel):
        self.academicLevel = acLevel
    def __repr__(self):
        return self.lastName + "," + self.firstName + "(" + self.academicLevel + ")"
