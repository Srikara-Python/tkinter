
from tkinter import *

root = Tk()
root.title('New windows in tkinter ! ')


def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')

	my_label = Label(top).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Window", command=open).pack()

def open2():
	top1 = Toplevel()
	top1.title("My Third window")
	btn2 = Button(top1, text="close window", command=top1.destroy).pack()

third =  Button(root, text="Open Third Window", command=open2).pack()



mainloop()