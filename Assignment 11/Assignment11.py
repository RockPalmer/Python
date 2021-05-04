"""
Assignment 11

// Assignment #: 8
// Name: Rock Palmer
// StudentID: 1214784662
// Lecture Time: T Th 1:30-2:45
// Section: CSE 205
// Description: Assignment 10 class displays a menu of choices to a user
//      and performs the chosen task. It will keep asking a user to
//      enter the next choice until the choice of 'Q' (Quit) is entered.
"""
from NQueenSolver import NQueenSolver

# The method printMenu displays the menu to a user
def printmenu():
    print("Choice\t\tAction\n" +                        
    "------\t\t------\n" +                        
    "E\t\tEnter Problem Parameter\n" +                        
    "Q\t\tQuit\n" +                        
    "?\t\tDisplay Help\n\n")
input1 = ""
line = ""
printmenu()

# will ask for user input
while input1 != "Q" or len(line) != 1:
    line = input("What action would you like to perform?\n").strip()
    input1 = line[0].upper()
    if len(line) == 1:
        # matches one of the conditional statements
        if input1 == "E":
            # Enter Problem parameter
            queennum = int(input("Please enter a number of queens\n").strip())
            # Create a solver for this problem.
            solver = NQueenSolver(queennum)
            if (solver.findsolution()):
                print("solution found!")
                print(solver.returnanswer())
            else:
                print("solution not found")
        elif input1 == "Q": # Quit
            pass
        elif input1 == "?": # Display Menu
            printmenu()
        else:
            print("Unknown Action")
    else:
        print("Unknown Action")
    
