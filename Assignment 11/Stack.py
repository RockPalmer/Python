"""
Stack

// Assignment #: 8
// Name: Rock Palmer
// StudentID: 1214784662
// Lecture: T Th 1:30-2:45
// Section: CSE 205
// Description: The Stack class is a reconstruction of the Stack data structure
//      native to java. It organizes data in a "first in, first out" set up.
//      Each element of the stack is called a node and each node contains a pointer
//      to its own data and a pointer to the node underneath it in the stack.
"""

# Defines the node object that the stack is built out of
class Node:
    def __init__(self):
        # The object/value stored in the given node
        self.val = None
        # A reference the the following node under the current node
        # in the stack
        self.under = None
class Stack:
    # Initializes an empty stack
    def __init__(self):
        self.top = None
    # Adds an element to the top of the stack
    def push(self, obj):
        newnode = Node()
        newnode.val = obj
        newnode.under = self.top
        self.top = newnode
    # Removes the top element in the stack
    def pop(self):
        # Raise an exception if the stack is empty
        if self.isempty():
            raise IndexError("Cannot pop an item from an empty stack")
        # If there is only one element in the stack, return the
        # value of the top value of the stack and then set the top
        # element to 'None'
        elif self.size() == 1:
            obj = self.top.val
            self.top = None
        # If there are multiple elements in the stack, remove and return
        # the value of the top element in the stack
        else:
            obj = self.top.val
            self.top = self.top.under
        return obj
    # Return the value of the top element in the stack without removing it
    def peek(self):
        # If the stack is empty return nothing
        if self.isempty():
            return None
        else:
            return self.top.val
    # Checks if the stack is empty
    def isempty(self):
        if self.top == None:
            return True
        else:
            return False
    # Returns the size of the stack
    def size(self):
        size = 0
        if not self.isempty():
            current = self.top
            while current != None:
                current = current.under
                size = size + 1
        return size
