"""
Assignment 8
"""
from DeptManagement import DeptManagement
import pickle

# The method printMenu displays the menu to a user
def printmenu():
    print("Choice\t\tAction\n"
    + "------\t\t------\n"
    + "A\t\tAdd a department\n"
    + "C\t\tCreate a DeptManagement\n"
    + "D\t\tSearch a department\n"
    + "E\t\tSearch a faculty\n"
    + "L\t\tList departments\n"
    + "N\t\tSort by department names\n"
    + "O\t\tSort by department faculty numbers\n"
    + "P\t\tSort by current faculty name\n"
    + "Q\t\tQuit\n"
    + "R\t\tRemove a department\n"
    + "T\t\tClose DeptManagement\n"
    + "U\t\tWrite strings to a text file\n"
    + "V\t\tRead strings from a text file\n"
    + "W\t\tSerialize DeptManagement to a data file\n"
    + "X\t\tDeserialize DeptManagement from a data file\n"
    + "?\t\tDisplay Help\n")

# create a DeptManagement object. This is used throughout this class.
deptmanage1 = DeptManagement()
try:

    # print out the menu
    printmenu()

    # read a line
    line = input("\nWhat action would you like to perform?\n").strip()
    input1 = line[0].upper()
    quitop = False
    
    while not quitop or len(line) == 1:

        # check if a user entered only one character
        if len(line) == 1:
            if input1 == "A":

                # Add Department

                # Store user input in variables
                print("Please enter the department information:\n")
                deptname = input("Enter department name:\n").strip()
                numoffaculty = int(input("Enter number of faculty:\n").strip())
                nameofuniversity = input("Enter university name:\n").strip()
                firstname = input("Enter faculty first name:\n").strip()
                lastname = input("Enter faculty last name:\n").strip()
                academiclevel = input("Enter faculty academic level:\n").strip()

                # Use user input to specify the department to add
                operation = deptmanage1.adddepartment(deptname, nameofuniversity, numoffaculty, firstname, lastname, academiclevel)
                if operation:
                    print("Department added")
                else:
                    print("Department NOT added")
            elif input1 == "C":

                # Create a new department management
                deptmanage1 = DeptManagement()
            elif input1 == "D":

                # Search by department's name and the university

                # Store user input in variables
                deptname = input("Please enter the department name to search:\n").strip()
                university = input("Please enter the university name to search:\n").strip()

                # Use user input to check if the specified department exists
                operation = deptmanage1.deptexists(deptname, university)
                if operation != -1:
                    print(deptname + " at " + university + " is found")
                else:
                    print(deptname + " at " + university + " is NOT found")
            elif input1 == "E":

                # Search faculty

                # Store user input in variables
                firstname = input("Please enter the faculty first name to search:\n").strip()
                lastname = input("Please enter the faculty last name to search:\n").strip()
                academiclevel = input("Please enter the faculty academic level to search:\n").strip()

                # Use user input to check if the specified faculty exists
                operation = deptmanage1.facultyexists(firstname, lastname, academiclevel)
                if operation != -1:
                    print("Faculty: " + firstname + " " + lastname + ", " + academiclevel + " is found")
                else:
                    print("Faculty: " + firstname + " " + lastname + ", " + academiclevel + " is NOT found")
            elif input1 == "L":
                # List departments
                print(deptmanage1.listdepartments())
            elif input1 == "N":
                deptmanage1.sortbydepartmentname()
                print("sorted by department names\n")
            elif input1 == "O":
                deptmanage1.sortbyfacultynumbers()
                print("sorted by faculty numbers\n")
            elif input1 == "P":
                deptmanage1.sortbydeptfaculty()
                print("sorted by current faculty name\n")
            elif input1 == "R":

                # Remove a department

                # Store user input in variables
                deptname = input("Please enter the department name to remove:\n").strip()
                university = input("Please enter the university name to remove:\n").strip()

                # Use user input to remove the specified department
                operation = deptmanage1.removedepartment(deptname, university)
                if operation:
                    print(deptname + " at " + university + " is removed\n")
                else:
                    print(deptname + " at " + university + " is NOT removed\n")
            elif input1 == "T":
                # Close DeptManagement
                deptmanage1.closedeptmanagement()
                print("Department management system closed\n")
            elif input1 == "U":
                # Write Text to a File
                filename = input("Please enter a file name that we will write to:\n").strip()
                try:

                    # Initialize objects to write in file
                    file = open(filename, "w")

                    # Print text
                    word = input("Please enter a string to write inside the file:")
                    file.write(word)
                    file.close()
                    print(filename + " is written")
                except IOError:
                    print("Error encountered when writing string into file\n")
            elif input1 == "V":
                # Read Text from a File
                try:
                    # Read file
                    filename = input("Please enter a file name which we will read from:\n").strip()
                    file = open(filename, "r")
                    word = file.read()
                    file.close()
                    print(filename + " was read")
                    print("The first line of the file is:\n" + word)
                except FileNotFoundError:
                    print(filename + " was not found")
                except IOError:
                    print("Read string from the file error")
            elif input1 == "W":
                # Serialize DeptManagement to a File
                filename = input("Please enter a file name which we will write to:\n").strip()
                try:
                    # Serialize object
                    file = open(filename, "wb")
                    pickle.dump(deptmanage1, file)
                    file.close()
                except pickle.PicklingError:
                    print("Not serializable exception\n")
                except IOError:
                    print("Data file written exception\n")
            elif input1 == "X":
                # Deserialize DeptManagement from a File
                filename = input("Please enter a file name which we will read from:\n").strip()
                try:
                    # Deserialize the object
                    file = open(filename, "rb")
                    deptmanage1 = pickle.load(file)
                    file.close()
                except pickle.AttributeError:
                    print("Class not found exception\n")
                except pickle.UnpicklingError:
                    print("Not serializable exception\n")
                except IOError:
                    print("Data file read exception\n")
            elif input1 == "?":
                # Display Menu
                printmenu()
            elif input1 == "Q":
                # Quit
                quitop = True
            else:
                print("Unknown action\n")
        else:
            print("Unkown action\n")
        if not quitop:
            line = input("\nWhat action would you like to perform?\n").strip()
            input1 = line[0].upper()
except IOError:
    print("IO Exception\n")
