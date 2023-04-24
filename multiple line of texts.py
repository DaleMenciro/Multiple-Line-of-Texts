'''
Write a method in python to write multiple line of text contents into a text file mylife.txt.
See sample output:
Enter line: Beautiful is better than ugly.
Are there more lines y/n? y
Enter line: Explicit is better than implicit.
Are there more lines y/n? y
Enter line: Simple is better than complex.
Are there more lines y/n? n 
'''

def write_file():
    #open file for writing
    with open("mylife.txt", "w") as my_file:
        #loop until the user is done entering
        while True:
            #asks user to input the line
            line_input = input("Enter line: ")
            #write the line to the file
            my_file.write(line_input + "\n")
            #loop until the user input valid response y/n
            while True:
                #asks user if they want to input more lines
                response = input("Are there more lines (y/n)? ")
                #if input is valid, loop breaks
                #if not, prompt the user again
            #if user says no, break out the loop


#==== START ====
write_file()