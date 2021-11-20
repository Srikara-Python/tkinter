from tkinter import *
from tkinter import messagebox

root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def entryinbasic():
    pass
   # while True:


def button_click_basic(number):
    check_error = "top1" in globals()
  #  e = Entry(top1, width=35, borderwidth=5)
#    e.grid(row=1, column=0)
    if check_error == True:
        
        print(check_error)
        e = Entry(top1, width=35, borderwidth=5)
        e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    else:
        return
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
   # entryinbasic()

def button_click_advanced(number):
    root = top2
    while True:
        e = Entry(top2, width=35, borderwidth=5)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))




def basic_mode():
    global top1
    top1 = Toplevel()
    
    buttons_basic()
    top1.mainloop()

def advanced_mode():
    global top2
    top2 = Toplevel()
    
    buttons_advanced()
    top2.mainloop()

def main_buttons():
    basic_button = Button(root, text = "Basic Mode", command = basic_mode)
    advanced_button = Button(root, text = "Advanced Mode", command = advanced_mode)
    basic_button.grid(row=0, column=0)
    advanced_button.grid(row=1, column=1)

main_buttons()

def buttons_basic():
    Button_1 = Button(top1, text="1", padx=40, pady=20, command=lambda: button_click_basic(1))
    Button_1.grid(row=2, column=0)
    Button_2 = Button(top1, text="2", padx=40, pady=20, command=lambda: button_click_basic(2))
    Button_2.grid(row=2, column=1)


def buttons_advanced():
    Button_1 = Button(top2, text="1", padx=40, pady=20, command=lambda: button_click_advanced(1))
    Button_1.grid(row=2, column=0)
    Button_2 = Button(top2, text="2", padx=40, pady=20, command=lambda: button_click_advanced(2))
    Button_2.grid(row=2, column=1)


                
root.mainloop()













