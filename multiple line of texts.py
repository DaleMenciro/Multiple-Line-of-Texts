import tkinter as tk

def write_file():
    #open file for writing
    with open("mylife.txt", "w") as my_file:
        #loop until the user is done entering
        while True:
            #asks user to input the line
            line_input = input_box.get()
            #write the line to the file
            my_file.write(line_input + "\n")
            #loop until the user input valid response y/n
            while True:
                #asks user if they want to input more lines
                response= response_box.get().lower()
                #if input is valid, loop breaks
                if response == "y" or response == "n":
                    break
                #if not, prompt the user again
                response_box.delete(0, tk.END)
                response_box.insert(tk.END, "Invalid response! Please input 'y' or 'n' only: ")
            #if user says no, break out the loop
            if response == "n":
                break

#create window
window = tk.Tk()
window.title("My Life")

#create input box
input_box = tk.Entry(window, width=50)
input_box.pack()

#create response box
response_box = tk.Entry(window, width=50)
response_box.pack()

#create submit button
submit_button = tk.Button(window, text="Submit", command=write_file)
submit_button.pack()

#==== START ====
window.mainloop()