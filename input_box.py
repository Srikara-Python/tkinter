from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='blue', fg='white', borderwidth=5)
e.pack()
e.insert(0, "Enter You Name: ")

def myClick():
    hello = "hello " + e.get()
    myLabel = Label(root, text=hello )
    myLabel.pack()
    

myButton = Button(root, text="Enter you name ", padx = 50, pady = 50, command=myClick, fg="blue", bg="red") # state = DISABLED
myButton.pack()



# Create a main loop
root.mainloop()