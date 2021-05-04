"""
LinkedList
"""
class Node:
    data = None
    after = None
    def __init__(self):
        pass
class LinkedList:
    first = Node()

    # Constructs an empty linked list.
    def __init__(self):
        self.first = None

    # Adds an element to the list at the correct index
    def add(self, element):
        iterator = self.__iter__()
        if self.size() == 0:
            iterator.add(element)
        else:
            current = iterator.getnext() # ///Equals list1.first right now///
            while current != None and current.val < element:
                iterator.__next__()
                current = iterator.getnext()
            else:
                iterator.add(element)

    # Counts how many times an element appears in the list
    def count(self, element):
        count = 0
        iterator = self.__iter__()
        while iterator.hasnext():
            current = iterator.__next__()
            if current.val == element:
                count = count + 1
        return count

    # Searches the list for the specified element and returns it's index.
    # If the element is not in the list, the method returns -1
    def search(self, element):
        iterator = self.__iter__()
        count = 0
        while iterator.hasnext() and iterator.getnext().val != element:
            iterator.__next__()
            count = count + 1
        else:
            if iterator.getnext().val == element:
                return count
            else:
                return -1

    # Removes the element at the specified index
    def remove(self, index):
        if index + 1 > self.size():
            return None
        else:
            count = 0
            iterator = self.__iter__()
            current = iterator.position
            obj = None
            while iterator.hasnext() and count < index:
                current = iterator.__next__()
                count = count + 1
            else:
                obj = iterator.getnext().val
                iterator.remove()
                return obj
                
    # Returns the iterator object for the list
    def __iter__(self):
        return ListIterator(self)

    # Returns the number of elements in the list
    def size(self):
        iterator = self.__iter__()
        count = 0
        while iterator.hasnext():
            iterator.__next__()
            count = count + 1
        return count

    # Removes the last 'n' number elements from the end of the list
    # determined by the user
    def removelastfew(self, num):
        if num > self.size():
            num = self.size()
        iterator = self.__iter__()
        count = 0
        while count < (self.size() - num):
            current = iterator.__next__()
            count = count + 1
        else:
            while iterator.hasnext():
                iterator.remove()

    def __repr__(self):
        string = "{ "
        iterator = self.__iter__()
        while iterator.hasnext():
            current = iterator.__next__()
            string = string + current.val + " "
        else:
            string = string + "}"
        return string
class ListIterator:
    def __init__(self, alist):
        self.list = alist
        self.position = None

    # Returns the next element in the list and puts the iterator position at that element
    def __next__(self):
        if self.position == None:
            if self.list.first == None:
                raise StopIteration
            else:
                self.position = self.list.first
        elif self.position.after == None:
            raise StopIteration
        else:
            self.position = self.position.after
        return self.position
    def hasnext(self):
        if self.position == None:
            if self.list.first == None:
                return False
            else:
                return True
        elif self.position.after == None:
            return False
        else:
            return True
    def getnext(self):
        if self.position == None:
            return self.list.first
        else:
            return self.position.after
    
    # Inserts an element at the index the iterator is facing
    def add(self, value):
        newnode = Node()
        newnode.val = value
        if self.position == None:
            newnode.after = self.list.first
            self.list.first = newnode
        else:
            newnode.after = self.position.after
            self.position.after = newnode

    # Removes the element at the index the iterator is facing
    def remove(self):
        if self.position == None:
            if self.list.first != None:
                self.list.first = self.list.first.after
        elif self.position.after != None:
            self.position.after = self.position.after.after
        
