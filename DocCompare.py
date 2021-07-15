"""
Doc Compare
"""

answer = input("Start the program? (Y/N)\n")
while answer != "N":
    if answer == "Y":
        print("Please enter your first piece of text below.\n")
        text_1 = ""
        line = input("When you are done, press \"ENTER\", type \"DONE\", then press \"ENTER\" again.\n")
        while line != "DONE":
            text_1 = text_1 + line
            line = input("")
        else:
            print("Please enter your second piece of text below.\n")
            text_2 = ""
            line = input("When you are done, press \"ENTER\", type \"DONE\", then press \"ENTER\" again.\n")
            while line != "DONE":
                text_2 = text_2 + line
                line = input("")
            else:
                print("The two pieces of text are", end=" ")
                if text_1 == text_2:
                    print("not", end=" ")
                print("the same.")
        answer = input("Would you like to do this again? (Y/N)\n")
    else:
        print("Unrecognized response. Please try again.")
else:
    print("Goodbye!")
        
