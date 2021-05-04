"""
Student
"""
class Student:
    firstName = ""
    lastName = ""
    studentID = ""
    numCredit = -1
    rate = -1.0
    tuition = -1.0
    def __init__(self,fName,lName,sID,nCredit,newRate):
        self.firstName = fName
        self.lastName = lName
        self.studentID = sID
        self.numCredit = nCredit
        self.rate = newRate
        self.tuition = 0.0
    def getNumCredit(self):
        return self.numCredit
    def computeTuition(self):
        pass
    def __repr__(self):
        return ("\nFirst name:\t\t" + self.firstName + "\nLast name:\t\t" +
                self.lastName + "\nStudent ID:\t\t" + self.studentID + "\nCredits:\t\t" +
                str(self.numCredit) + "\nRate:\t\t\t" + "$" + format(self.rate,".2f") + "\n")
