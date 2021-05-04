"""
StuParse
"""
from Student import Student
from Graduate import Graduate
from UnderGrad import UnderGrad
class StuParser:
    def parseStringToStudent(lineToParse):
        attributes = ["","","","","","","",""]
        count1 = 0
        count2 = 0
        while count1 < len(lineToParse):
            line = ""
            while count1 < len(lineToParse) and lineToParse[count1] != "/":
                line = line + lineToParse[count1]
                count1 = count1 + 1
            else:
                attributes[count2] = line
                line = ""
                count2 = count2 + 1
                count1 = count1 + 1
        if attributes[0] == "Graduate":
            grad = Graduate(attributes[1],attributes[2],attributes[3],int(attributes[4]),float(attributes[5]),float(attributes[6]))
            return grad
        else:
            isInState = False
            if attributes[6] == "InState" or attributes[6] == "inState":
                isInState = True
            else:
                isInState = False
            unGrad = UnderGrad(attributes[1],attributes[2],attributes[3],int(attributes[4]),float(attributes[5]),isInState,float(attributes[7]))
            return unGrad
