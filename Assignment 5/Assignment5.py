"""
Assignment5
"""
from Student import Student
from Graduate import Graduate
from UnderGrad import UnderGrad
from StuParser import StuParser
def printMenu():
    print("Choice\t\tAction\n------\t\t------\nA\t\tAdd Student\nC\t\tCompute Tuition\nD\t\tCount Certain Students\nL\t\tList Students\nQ\t\tQuit\n?\t\tDisplay Help\n\n")
printMenu()
userIn = input("What action would you like to perform?\n")
userIn = userIn.upper()
studentList = list()
while userIn != "Q":
    if len(userIn) == 1:
        if userIn == "A":
            studentStr = input("Please enter a student information to add:\n")
            newStudent = StuParser.parseStringToStudent(studentStr)
            studentList.append(newStudent)
        elif userIn == "C":
            count = 0
            while count < len(studentList):
                studentList[count].computeTuition()
                count = count + 1
            print("tuition computed\n")
        elif userIn == "D":
            numCredits = int(input("Please enter a number of credits:\n"))
            count1 = 0
            count2 = 0
            while count1 < len(studentList):
                if studentList[count1].getNumCredit() == numCredits:
                    count2 = count2 + 1
                count1 = count1 + 1
            print("The number of students who are taking " + str(numCredits) + " credits is: " + str(count2))
        elif userIn == "L":
            if len(studentList) == 0:
                print("no student\n")
            else:
                count = 0
                while count < len(studentList):
                    print(studentList[count])
                    count = count + 1
        elif userIn == "Q":
            break
        elif userIn == "?":
            printMenu()
        else:
            print("Unknown action\n")
    else:
        print("Unknown action\n")
    userIn = input("What action would you like to perform?\n")
