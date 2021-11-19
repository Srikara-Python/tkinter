from tkinter import *

root = Tk()
root.title("Simple Calculator")

frame = LabelFrame(root, text="This is my frame.. ", padx=50, pady=50)
frame.pack(pady=10, padx=10)


b = Button(frame, text="Dont click here!")
b.pack()







root.mainloop()