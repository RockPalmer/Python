"""
Assignment 1
"""
word = input("Enter a number:")
num = ""
for c in word:
    if c != " " :
        num = num + c
print("This program reads an integer from a keyboard,\nand prints it out on the display screen.\nThe number is: " + num)
print("Make sure you get the exact same output as the expected one!\n")
