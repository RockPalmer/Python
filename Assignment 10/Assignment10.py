"""
Assignment 10
"""
from LinkedList import LinkedList
def printmenu():
    print("Choice\t\tAction\n" +                        
    "------\t\t------\n" +
    "A\t\tAdd String\n" +                        
    "B\t\tCount Occurrences\n" +                        
    "C\t\tSearch\n" +                       
    "D\t\tRemove\n" +                        
    "E\t\tSize\n" +                        
    "L\t\tList Strings\n" +                        
    "F\t\tRemove String\n" +                        
    "Q\t\tQuit\n" +                        
    "?\t\tDisplay Help\n\n")
list1 = LinkedList()
try:
    input1 = ""
    line = " "
    isDone = False
    printmenu()
    while not isDone and len(line) == 1:
        line = input("What action would you like to perform?\n").strip()
        if len(line) == 1:
            input1 = line[0].upper()
            # Add a string
            if input1 == "A":
                string = input("Please enter a string to add:\n").strip()
                list1.add(string)
            # Count the number of occurrences of a string
            elif input1 == "B":
                string = input("Please enter a string to count:\n").strip()
                print("string occurs " + str(list1.count(string)) + " time(s)\n")
            # Search the index of a string
            elif input1 == "C":
                string = input("Please enter a string to search:\n").strip()
                index = list1.search(string)
                if index == -1:
                    print("string not found\n")
                else:
                    print("string found at " + str(index) + "\n")
            # Remove the string at an index
            elif input1 == "D":
                index = int(input("Please enter an index of a string to remove:\n").strip())
                obj = list1.remove(index)
                if obj == None:
                    print("The index is out of bounds")
                else:
                    print("The string " + obj + " was removed\n")
            # Print current list size
            elif input1 == "E":
                print(str(list1.size()))
            # List elements of the list
            elif input1 == "L":
                print(str(list1))
            # Remove the last few elements from the end of the list
            elif input1 == "F":
                num = int(input("Please enter a number of elements to remove from the end:\n").strip())
                list1.removelastfew(num)
            elif input1 == "Q":
                isDone = True
            elif input1 == "?":
                printmenu()
            else:
                print("Unknown action\n")
        else:
            print("Unknown action\n")
except IOError:
    print("IO error\n")
