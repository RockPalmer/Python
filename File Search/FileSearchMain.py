"""
File Search Main
"""
import os

initial_path = "../../../../../.."
answer = input("Start program? (Y/N)\n")
while answer != "Y" and answer != "N":
    print("Unrecognized response. Please try again.")
    answer = input("Start program? (Y/N)\n")
else:
    while answer == "Y":
        search_option = input("Would you like to search for a file name, type of file, or term in a file? (name/type/term)\n")
        while search_option != "name" and search_option != "type" and search_option != "term":
            print("Unrecognized response. Please try again.")
            search_option = input("Shall I search for a file name or a term in a file? (file name/term in a file)\n")
        else:
            if search_option == "name":
                file_name = input("Please enter the file name below.\n")
                print("Thank you.")
                file_directory = input("Now, please enter the path of the directory you want to search.\n")
                print("Thank you.")
                print("Searching...")
            elif search_option == "type":
                file_extension = input("Please enter the file extension below\n")
                print("Thank you.")
                file_directory = input("Now, please enter the path of the directory you want to search.\n")
                print("Thank you.")
                print("Searching...")
            elif search_option == "term":
                term = ""
                line = input("Please enter the term below, press \"ENTER\", then type DONE, then press \"ENTER\" again.\n")
                while line != "DONE":
                    term = term + line
                    line = input("")
                else:
                    file_directory = input("Now, please enter the path of the directory you want to search.\n")
                    print("Thank you.")
                    print("Searching...")
    else:
        if answer == "N":
            print("Goodbye!")
