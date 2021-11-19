from tkinter import *
from tkinter import messagebox

root = Tk()

def button_click(number):
   e = Entry(top1, width=35, borderwidth=5)
   e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))


def basic_mode():
	global top1
	top1 = Toplevel()

	buttons()
	top1.mainloop()

def advanced_mode():
	global top2
	top2 = Toplevel()
	Button_1 = Button(top2, text="1", padx=40, pady=20)
	Button_1.pack()
	Button_2 = Button(top2, text="2", padx=40, pady=20)
	Button_2.pack()
	top2.mainloop()

def main_buttons():
	basic_button = Button(root, text = "Basic Mode", command = basic_mode)
	advanced_button = Button(root, text = "Advanced Mode", command = advanced_mode)
	basic_button.pack()
	advanced_button.pack()

main_buttons()

def buttons():
	Button_1 = Button(top1, text="1", padx=40, pady=20, command=lambda: button_click(1))
	Button_1.grid(row=2, column=0)
	Button_2 = Button(top1, text="2", padx=40, pady=20, command=lambda: button_click(1))
	Button_2.grid(row=2, column=1)



root.mainloop()