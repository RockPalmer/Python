"""
Linked List
"""
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def __repr__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        return Iterator(self)
    def __repr__(self):
        out = "[ "
        iterator = self.__iter__()
        while iterator.getnext() != None:
            out = out + str(iterator.__next__()) + " "
        else:
            out = out + "]"
            return out
    
    # Get the size of the list
    def size(self):
        size = 0
        iterator = self.__iter__()
        while iterator.getnext() != None:
            iterator.__next__()
            size = size + 1
        return size
    
    # Add element to the end of the list
    def append(self, data):
        iterator = self.__iter__()
        while iterator.getnext() != None:
            iterator.__next__()
        else:
            iterator.add(data)

    # Removes an element from the end of the list
    def trim(self):
        iterator = self.__iter__()
        try:
            while iterator.getnext().next != None:
                iterator.__next__()
            else:
                iterator.remove()
        except AttributeError:
            raise IndexError("Cannot remove an element from an empty LinkedList.") from None

    # Inserts an element at the specified index of the list
    def insert(self, data, index):
        iterator = self.__iter__()
        try:
            if index < 0:
                raise AttributeError
            else:
                count = 0
                while count < index:
                    iterator.__next__()
                    count = count + 1
                else:
                    iterator.add(data)
        except (AttributeError,StopIteration):
            raise IndexError("Index out of bounds for the given LinkedList.") from None

    # Remove an element at the specified index of the list
    def remove_at(self, index):
        iterator = self.__iter__()
        try:
            if index < 0:
                raise AttributeError
            else:
                count = 0
                while count < index:
                    iterator.__next__()
                    count = count + 1
                else:
                    iterator.remove()
        except (AttributeError,StopIteration):
            raise IndexError("Index out of bounds for the given LinkedList.") from None

    # Remove an element with a specified data value
    def remove(self, data):
        iterator = self.__iter__()
        try:
            current = iterator.getnext()
            while current.data != data:
                iterator.__next__()
                current = iterator.getnext()
            else:
                iterator.remove()
        except (AttributeError,StopIteration):
            raise IndexError("Specified element does not exist in the current LinkedList instance.") from None

# Defines the iterator for the LinkedList object
class Iterator:
    def __init__(self, alist):
        self.list = alist
        self.position = None

    # Return the element after the iterator position
    def __next__(self):
        if self.position == None:
            self.position = self.list.head
        else:
            self.position = self.position.next
            if self.position == None:
                raise StopIteration
        return self.position
    def getnext(self):
        if self.position == None:
            return self.list.head
        else:
            return self.position.next

    # Add element in the list after the iterator position
    def add(self, data):
        newnode = Node()
        newnode.data = data
        if self.position == None:
            newnode.next = self.list.head
            self.list.head = newnode
        else:
            newnode.next = self.position.next
            self.position.next = newnode

    # Remove element in the list after the iterator position
    def remove(self):
        self.position.next = self.position.next.next
