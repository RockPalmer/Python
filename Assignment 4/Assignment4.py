"""
Assignment4
"""
from Department import Department
from Faculty import Faculty
def printMenu():
    print("Choice\t\tAction\n" + "------\t\t------\n" + "A\t\tAdd Department\n" + "D\t\tDisplay Department\n" + "Q\t\tQuit\n" + "?\t\tDisplay Help\n\n")
printMenu()
dept = Department()
userIn = input("What action would you like to perform?\n")
while len(userIn) == 1:
    userIn = userIn.upper()
    if userIn == "A":
        print("Please enter the department information:\n")
        deptName = input("Enter its name:\n")
        dept.setDeptName(deptName)
        numMembers = input("Enter its number of members:\n")
        dept.setNumberOfMembers(int(numMembers))
        univ = input("Enter its university:\n")
        dept.setUniversity(univ)
        fName = input("Enter its faculty's first name:\n")
        lName = input("Enter its faculty's last name:\n")
        aLevel = input("Enter its faculty's academic level:\n")
        dept.setCurrentFaculty(fName,lName,aLevel)
    elif userIn == "D":
        print(str(dept))
    elif userIn == "Q":
        break
    elif userIn == "?":
        printMenu()
    else:
        print("Unknown action\n")
    userIn = input("What action would you like to perform?\n")
    
