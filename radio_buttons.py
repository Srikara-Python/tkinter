  
from tkinter import *


root = Tk()
root.title('Learn To Code at Codemy.com')

#r = IntVar()
#r.set("2")

TOPPINGS = [
	("Pepperoni", "a"),
	("Cheese", "b"),
	("Mushroom", "c"),
	("Onion", "d"),
]

pizza = StringVar()
pizza.set("Cheese")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()	

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
mainloop()

root.mainloop()