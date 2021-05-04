"""
Assignment 9
"""

# Finds the largest number in a list recursively
def findmaxnum(alist):
    mnum = alist[0]
    if len(alist) > 1:
        newlist = alist[1:]
        if mnum < findmaxnum(newlist):
            mnum = findmaxnum(newlist)
    return mnum

# Finds the largest even number in a list recursively
def findlargesteven(alist):
    largeven = alist[0]
    if len(alist) > 1:
        newlist = alist[1:]
        if largeven % 2 == 0:
            if largeven < findlargesteven(newlist) and findlargesteven(newlist) % 2 == 0:
                largeven = findlargesteven(newlist)
            else:
                largeven = alist[0]         
        else:
            largeven = findlargesteven(newlist)
    return largeven

# Finds the total amount of numbers in alist that are divisible by 3 recursively
def findnumdivby3(alist):
    count = 0
    if alist[0] % 3 == 0:
        count = 1
    if len(alist) > 1:
        newlist = alist[1:]
        count = count + findnumdivby3(newlist)
    return count

# Finds the sum of all numbers in a list that are greater than the last number in the list recursively
def findsumlarglast(alist):
    mysum = 0
    if alist[0] > alist[len(alist) - 1]:
        mysum = mysum + alist[0]
    if len(alist) > 2:
        newlist = alist[1:]
        mysum = mysum + findsumlarglast(newlist)
    return mysum
num = 0
numlist = list()
try:
    num = int(input(""))
    while num != 0:
        numlist.append(num)
        num = int(input(""))
except ValueError:
    print("Value Error")
print("The maximum number is " + str(findmaxnum(numlist)))
print("The largest even integer in the sequence is " + str(findlargesteven(numlist)))
print("The count of numbers divisible by 3 is " + str(findnumdivby3(numlist)))
print("The sum of numbers larger than the last is " + str(findsumlarglast(numlist)))
