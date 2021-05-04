"""
UnderGrad
"""
from Student import Student
class UnderGrad(Student):
    inState = False
    creditUpperBound = -1
    programFee = -1.0
    def __init__(self,fName,lName,ID,nCredits,rate,inState,programFee):
        super().__init__(fName,lName,ID,nCredits,rate)
        self.inState = inState
        self.programFee = programFee
        if inState:
            self.creditUpperBound = 7
        else:
            self.creditUpperBound = 12
    def computeTuition(self):
        if self.numCredit >= self.creditUpperBound:
            self.tuition = float(self.rate) * float(self.creditUpperBound) + float(self.programFee)
        else:
            self.tuition = float(self.rate) * float(self.numCredit) + float(self.programFee)
    def __repr__(self):
        result = "\nUnderGrad:\n"
        if self.inState:
            result = result + "In"
        else:
            result = results + "Out-Of"
        result = result + "-State" + super().__repr__() + "Student Program Fee:\t" + "$" + format(self.programFee,".2f")
        return result
