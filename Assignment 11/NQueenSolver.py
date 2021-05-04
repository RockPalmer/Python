"""
NQueenSolver

// Assignment #: 8
// Name: Rock Palmer
// StudentID: 1214784662
// Lecture: T Th 1:30-2:45
// Section: CSE 205
// Description: This class takes a single integer <N> as a parameter value and 
//		tries to find if N number of queens can be fit into an N-by-N chess board
//		without any of them being in the same row, column or diagonal. It does
//		so by placing possible placements into a stack of valid solutions and 
//		checking if this solution breaks the row, column, diagonal rule for any
//		of the other solutions. If so, it will try the next column over (provided
//		that that does not put it out of bounds) until it finds the correct 
//		placement. It does this row by row until it finds a solution.
"""
from Stack import Stack
from Answer import Answer
from Pair import Pair

class NQueenSolver:

    # Constructor to initialize the boardSize, which is also the number of  
    # queens to be placed. Also create an answer object.
    def __init__(self, queennum):
        self.answer = Answer(queennum)
        self.boardsize = queennum # This is N in the assignment description.
    # Return an answer -- accessor of the answer
    def returnanswer(self):
        return self.answer
    # The findSolution will return true if a solution is found,  
    # false otherwise.
    def findsolution(self):
        stacksoln = Stack()
        # back-up stack 
        stacksoln2 = Stack()
        success = False

        # Push information onto the stack indicating the first choice    
	# is a queen in row 0 and column 0.  
        stacksoln.push(Pair(0,0))

        # Continue loop until either a solution is found or there are not possible solutions
        while not success and not stacksoln.isempty():

            # Set conflict to false every time so the program can check if this is so
            conflict = False
            print("Trying to place a queen in row " + str(stacksoln.peek().getrow()) + " in column " + str(stacksoln.peek().getcolumn()))

            # Place choice to be checked into backup stack and store value of choice in variable solution
            solution = stacksoln.pop()
            stacksoln2.push(solution)

            # Check whether the most recent choice (on top of the stack) is in the same row, same column,        
	    # or same diagonal as any other choices in the stack.        
	    # If so, there is a conflict; otherwise, there is no conflict.
            while not conflict and not stacksoln.isempty():

                # Check if they are in the same row
                if solution.getrow() == stacksoln.peek().getrow():
                    conflict = True
                # Check if they are in the same column
                elif solution.getcolumn() == stacksoln.peek().getcolumn():
                    conflict = True
                # Check if they are in the same diagonal
                elif solution.getrow() + solution.getcolumn() == stacksoln.peek().getrow() + stacksoln.peek().getcolumn():
                    conflict = True
                elif solution.getrow() - solution.getcolumn() == stacksoln.peek().getrow() - stacksoln.peek().getcolumn():
                    conflict = True
                # Uncover the next solution in the stack to compare and check it
                else:
                    conflict = False
                    stacksoln2.push(stacksoln.pop())
            # Push solutions back onto stacksoln
            else:
                while not stacksoln2.isempty():
                    stacksoln.push(stacksoln2.pop())

            # If the proposed solution breaks the row, column, diagonal rule, increment the column
	    # of the top solution (as long as that does not put it out of bounds)
            if conflict:
                # Pop items off the stack until the stack becomes empty or            
		# the top of the stack is a choice whose column is not N-1. 
                while not stacksoln.isempty() and stacksoln.peek().getcolumn() == self.boardsize - 1:
                    stacksoln.pop()
                else:
                    # If the stack is now not empty after popping items,            
		    # then increase the column number of the top choice by 1.            
		    # That is, pop the top choice, and increase its column, then push it back.
                    if not stacksoln.isempty():
                        newpair = stacksoln.pop()
                        stacksoln.push(Pair(newpair.getrow(), newpair.getcolumn() + 1))
            # If a solution is found and all Queens have been fit on the board, end the loop and
	    # and print out the solution
            elif not conflict and stacksoln.size() == self.boardsize:
                success = True

                # Since a solution is found, copy the stack info into the answer           
		# so that it can print them.  
                self.answer.copysolution(stacksoln)
            # no conflict, and it has not finished finding a solution yet 
            else:
                # The next choice is to place a queen at row number stackSoln.size()            
                # (one more than the current choice's row) and column number 0.            
		# So push (stacksoln.size(), 0) onto the stack  
                stacksoln.push(Pair(stacksoln.size(), 0))
        else:
            return success
