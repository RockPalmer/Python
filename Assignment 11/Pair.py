"""
Pair

// Assignment #: 8
// Name: Rock Palmer
// StudentID: 1214784662
// Lecture: T Th 1:30-2:45
// Section: CSE 205
// Description: The pair class pairs a row number and a column number.
"""
class Pair:
    # Initializes the pair object using two parameters 
    def __init__(self, row, column):
        self.row = row
        self.column = column
    # Accessor method for the row number
    def getrow(self):
        return self.row
    # Accessor method for the column number
    def getcolumn(self):
        return self.column
