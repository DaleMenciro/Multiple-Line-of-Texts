import colorama
from termcolor import colored

def write_file():
    #open file for writing
    with open("mylife.txt", "w") as my_file:
        #loop until the user is done entering
        while True:
            #asks user to input the line
            line_input = input("Enter line: ", "blue")
            #write the line to the file
            my_file.write(line_input + "\n")
            #loop until the user input valid response y/n
            while True:
                #asks user if they want to input more lines
                response = input("Are there more lines (y/n)? ", "yellow")
                response = response.lower
                #if input is valid, loop breaks
                if response() == "y" or response() == "n":
                    break
                #if not, prompt the user again
                print("Invalid response! Please input 'y' or 'n' only: ", "red")
            #if user says no, break out the loop
            if response() == "n":
                break

#==== START ====
write_file()