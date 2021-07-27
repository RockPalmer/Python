"""
File Search Main
"""
import os

def findterm(term, file_directory, path_list):
    files = os.listdir(file_directory)
    i = 0
    try:
        while True:
            temp_directory = file_directory + "\\" + files[i]
            i = i + 1
            try:
                file_obj = open(temp_directory, "r")
                content = file_obj.read()
                file_obj.close()
                if content.find(term) != -1:
                    path_list.append(temp_directory)
            except UnicodeDecodeError:
                pass
            except PermissionError:
                path_list = findterm(term, temp_directory, path_list)
    except IndexError:
        return path_list
def findfile(file_name, file_directory, path_list):
    # Initialize list of files in file_directory
    files = os.listdir(file_directory)
    # Check each file in file_directory
    i = 0
    try:
        while True:
            # Add file being checked to end of file_directory
            temp_directory = file_directory + "\\" + files[i]
            # Check if name matches
            if files[i].find(file_name) != -1:
                # Add file path to path_list
                path_list.append(temp_directory)
            else:
                # If names don't match, try to open the file as a directory
                try:
                    path_list = findfile(file_name, temp_directory, path_list)
                except NotADirectoryError:
                    # Go to the next file if files[i] is not a folder
                    pass
            # increment counter
            i = i + 1
    except IndexError:
        # If all of the contents of a folder have been read, return the collected paths
        return path_list
search_option = ""
file_name = ""
file_directory = ""
files = list()
path_list = list()  
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
                while True:
                    file_name = input("Please enter the file name below.\n")
                    print("Thank you.")
                    file_directory = input("Now, please enter the path of the directory you want to search.\n")
                    print("Thank you.")
                    try:
                        files = os.listdir(file_directory)
                        print("Directory found.\n\n/**************************************************************/"
                              + "\n\nSearching...\n\n")
                        path_list = findfile(file_name, file_directory, path_list)
                        if len(path_list) == 0:
                            print("File not found.")
                        else:
                            print("Your file is located at the following directories.")
                        break
                    except NotADirectoryError:
                        print("The path entered leads to a file that is not a directory. Please try again.")
                    except FileNotFoundError as e:
                        print("The path entered does not exist. Please try again.")
                for i in path_list:
                    print(i)
                answer = input("Restart program? (Y/N)\n")
            elif search_option == "type":
                while True:
                    file_extension = input("Please enter the file extension below\n")
                    print("Thank you.")
                    file_directory = input("Now, please enter the path of the directory you want to search.\n")
                    print("Thank you.")
                    try:
                        files = os.listdir(file_directory)
                        print("Directory found.\n\n/**************************************************************/"
                              + "\n\nSearching...\n\n")
                        path_list = findfile(file_extension, file_directory, path_list)
                        if len(path_list) == 0:
                            print("File not found.")
                        else:
                            print("Your file is located at the following directories.")
                        break
                    except NotADirectoryError:
                        print("The path entered leads to a file that is not a directory. Please try again.")
                    except FileNotFoundError:
                        print("The path entered does not exist. Please try again.")
                for i in path_list:
                    print(i)
                answer = input("Restart program? (Y/N)\n")
            elif search_option == "term":
                while True:
                    term = ""
                    line = input("Please enter the term below, press \"ENTER\", then type DONE, then press \"ENTER\" again.\n")
                    while line != "DONE":
                        term = term + line
                        line = input("")
                    else:
                        file_directory = input("Now, please enter the path of the directory you want to search.\n")
                        print("Thank you.")
                    try:
                        files = os.listdir(file_directory)
                        print("Directory found.\n\n/**************************************************************/"
                                  + "\n\nSearching...\n\n")
                        path_list = findterm(term, file_directory, path_list)
                        if len(path_list) == 0:
                            print("File not found.")
                        else:
                            print("The term you entered was found at the following directories.")
                        break
                    except NotADirectoryError:
                            print("The path entered leads to a file that is not a directory. Please try again.")
                    except FileNotFoundError:
                            print("The path entered does not exist. Please try again.")
                for i in path_list:
                    print(i)
                answer = input("Restart program? (Y/N)\n")
    else:
        if answer == "N":
            print("Goodbye!")
    

