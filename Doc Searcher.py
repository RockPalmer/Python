"""
Doc Searcher
"""
option = "Y"
while option != "N":
    filename = input("Enter the name of the file you are searching\n").strip()
    print("The program will search " + filename)
    string = input("Enter the string you would like to search for\n").strip()
    content = ""
    indexlist = list()
    with open("C:\\Users\\16026\\Python\\Python Projects\\Doc Searcher\\" + filename, "r") as file:
        content = file.readlines()
    for line in content:
        index = 0
        charnum = 0
        for char in line:
            if index + 1 < len(string):
                if char == string[index]:
                    index = index + 1
                else:
                    index = 0
            else:
                index = 0
                indexlist.append("line " + str(content.index(line)) + ", character " + str(charnum - (len(string) - 1)))
            charnum = charnum + 1
    print("Your string was found at the following locations:")
    for element in indexlist:
        print(element)
    option = input("Would you like to search another file or search the same file for another word? (Y/N)\n")
    
