from Faculty import Faculty
class Department:
    ''
    name = ""
    numberOfMembers = -1
    university = ""
    currentFaculty = Faculty()
    def __init__(self):
        self.name = "?"
        self.numberOfMembers = 0
        self.university = "?"
    def getDeptName(self):
        return self.name
    def getNumberOfMembers(self):
        return self.numberOfMembers
    def getUniversity(self):
        return self.university
    def getCurrentFaculty(self):
        return self.currentFaculty
    def setDeptName(self, d_name):
        self.name = d_name
    def setNumberOfMembers(self, n_members):
        self.numberOfMembers = n_members
    def setUniversity(self, univ):
        self.university = univ
    def setCurrentFaculty(self, firstName, lastName, academicLevel):
        self.currentFaculty = Faculty()
        self.currentFaculty.setFirstName(firstName)
        self.currentFaculty.setLastName(lastName)
        self.currentFaculty.setAcademicLevel(academicLevel)
    def __repr__(self):
        return "\nDepartment Name:\t\t" + self.name + "\nNumber of Members:\t" + str(self.numberOfMembers) + "\nUniversity:\t\t" + self.university + "\nFaculty:\t\t" + str(self.currentFaculty) + "\n\n"
