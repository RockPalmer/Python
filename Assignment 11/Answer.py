"""
Answer

// Assignment #: 8
// Name: Rock Palmer
// StudentID: 1214784662
// Lecture: T TH 1:30-2:45
// Section: CSE 205
// Description: This class contains a 2-dimensional list to
// display the content of the checker board.
"""
from Stack import Stack

class Answer:
    # Constructor to create a 2-dimensional list and initialize it.  
    def __init__(self, size):
        self.solution = list()
        for x in range(size):
            self.solution.append(list())
            for y in range(size):
                self.solution[x].append('_')
    # This method changes the element at row and col to have 'Q'  
    # to say that there is a queen placed at the location.  
    def setqueen(self, row, col):
        self.solution[row][col] = 'Q'
    # The copySolution method copies the location of queens from  
    # the parameter stack into the 2-dimensional list
    def copysolution(self, thissolution):
        while not thissolution.isempty():
            current = thissolution.pop()
            self.setqueen(current.getrow(), current.getcolumn())
    # The toString method returns a string to display the content of  
    # the n queen problem solution 
    def __repr__(self):
        result = ' |'
        for x in range(len(self.solution)):
            result = result + str(x) + "|"
        result = result + "\n"
        for x in range(len(self.solution)):
            result = result + str(x) + "|"
            for y in self.solution[x]:
                result = result + y + "|"
            result = result + "\n"
        return result
