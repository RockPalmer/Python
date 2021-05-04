"""
Graduate
"""
from Student import Student
class Graduate(Student):
    gradFee = -1.0
    def __init__(self,fName,lName,ID,nCredits,rate,gradFee):
        self.gradFee = gradFee
        super().__init__(fName,lName,ID,nCredits,rate)
    def computeTuition(self):
        self.tuition = float(self.rate) * float(self.numCredit) + float(self.gradFee)
    def __repr__(self):
        return "\nGraduate Student:" + super().__repr__() + "\nGrad Fee:\t\t" + "$" + format(self.gradFee,".2f") + "\n"
