from tkinter import *
root = Tk()
root.title("hello!")

mylabel1 = Label(root, text="Hello ! I am Srikara !")
mylabel1.pack()

def buttons():
	mylabel2 = Label(root, text="Nice!")
	mylabel2.pack()


myButton = Button(root, text="Click Me!", command=buttons)
myButton.pack()




mainloop()