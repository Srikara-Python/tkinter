from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look!  clicked a button !")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx = 50, pady = 50, command=myClick, fg="blue", bg="red") # state = DISABLED
myButton.pack()



# Create a main loop
root.mainloop()