from tkinter import *

root = Tk()

# Create a label widget 
mylabel1 = Label(root, text="Hello World") #.grid(row=0, column=0)
mylabel2 = Label(root, text="My Name is Srikara") #.grid(row=1, column=5)


# put it on the screen 
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=5)


# Create a main loop
root.mainloop()
