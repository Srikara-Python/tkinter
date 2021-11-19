# My Calculator from tkinter 

from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

mylabel1 = Label(root, text= "Hi")
mylabel1.grid(row=0, column=3, columnspan=1, padx=40, pady=20)


  ### Define our buttons

def button_exit():
    exit()

def button_click(number):
   # e.delete(0, END)
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    check_add = "mylabel_add" in globals()
    check_sub = "mylabel_sub" in globals()
    check_mult = "mylabel_mult" in globals()
    check_div = "mylabel_div" in globals()
    check_rem = "mylabel_rem" in globals()
    check_pow = "mylabel_pow" in globals()
    check_sqr = "mylabel_sqr" in globals()

    if check_add == True:
        mylabel_add.destroy()

    if check_sub == True:
        mylabel_sub.destroy()

    if check_mult == True:
        mylabel_mult.destroy()

    if check_div== True:
        mylabel_div.destroy()

    if check_rem== True:
        mylabel_rem.destroy()

    if check_pow== True:
        mylabel_pow.destroy()

    if check_sqr== True:
        mylabel_sqr.destroy()

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "+"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "-"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "*"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "/"
    f_num = float(first_number)
    e.delete(0, END)

def button_rem():
    first_number = e.get()
    global f_num
    global math
    math = "%"
    f_num = float(first_number)
    e.delete(0, END)

def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "**"
    f_num = float(first_number)
    e.delete(0, END)

def button_sqr():
    first_number = e.get()
    global f_num
    global math
    math = "sqr"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    global second_number

    if math == 'sqr':
        second_number = f_num

    else:
        second_number = float(e.get())
        e.delete(0, END)


    if math == "+":
        e.insert(0, f_num + float(second_number))
        whatfunction_add()


    if math == "-":
        e.insert(0, f_num - float(second_number))
        whatfunction_sub()


    if math == "*":
        e.insert(0, f_num * float(second_number))
        whatfunction_mult()


    if math == "/":
        e.insert(0, f_num / float(second_number))
        whatfunction_div()



    if math == "%":
        e.insert(0, f_num % float(second_number))
        whatfunction_rem()



    if math == "**":
        e.insert(0, f_num ** float(second_number))
        whatfunction_pow()


    if math == "sqr":
        e.insert(0, f_num * f_num)
        whatfunction_sqr()


  ## Make our labels
def whatfunction_add():
    if math == "+":
        global mylabel_add
        mylabel_add = Label(root, text= str(f_num ) + " " + "+" + " " + str(second_number))
        mylabel_add.grid(row=0, column=4, columnspan=1, padx=40, pady=20)


def whatfunction_sub():
    global mylabel_sub
    if math == "-":
        mylabel_sub = Label(root, text= str(f_num ) + " " + "-" + " " + str(second_number))
        mylabel_sub.grid(row=0, column=4, columnspan=1, padx=40, pady=20)


def whatfunction_mult():
    global mylabel_mult
    if math == "*":
        mylabel_mult = Label(root, text= str(f_num ) + " " + "*" + " " + str(second_number))
        mylabel_mult.grid(row=0, column=4, columnspan=1, padx=40, pady=20)

def whatfunction_div():
    global mylabel_div
    if math == "/":
        mylabel_div = Label(root, text= str(f_num ) + " " + "/" + " " + str(second_number))
        mylabel_div.grid(row=0, column=4, columnspan=1, padx=40, pady=20)

def whatfunction_rem():
    global mylabel_rem
    if math == "%":
        mylabel_rem = Label(root, text= str(f_num ) + " " + "%" + " " + str(second_number))
        mylabel_rem.grid(row=0, column=4, columnspan=1, padx=40, pady=20)

def whatfunction_pow():
    global mylabel_pow
    if math == "**":
        mylabel_pow = Label(root, text= str(f_num ) + " " + "**" + " " + str(second_number))
        mylabel_pow.grid(row=0, column=4, columnspan=1, padx=40, pady=20)

def whatfunction_sqr():
    global mylabel_sqr
    if math == "sqr":
        mylabel_sqr = Label(root, text= str(f_num ) + " square")
        mylabel_sqr.grid(row=0, column=4, columnspan=1, padx=40, pady=20)



# Define buttons
Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
Button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
Button_clear = Button(root, text="clear", padx=40, pady=20, command=button_clear)
Button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
Button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
Button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
Button_point = Button(root, text=".", padx=40, pady=20, command=lambda: button_click('.'))
Button_open_paranthesis = Button(root, text="(", padx=40, pady=20, command=lambda: button_click('('))
Button_close_paranthesis = Button(root, text=")", padx=40, pady=20, command=lambda: button_click(')'))
Button_remainder = Button(root, text="%", padx=35, pady=20, command=button_rem)
Button_power = Button(root, text="pow", padx=30, pady=20, command=button_pow)
Button_sqr = Button(root, text="sqr", padx=30, pady=20, command=button_sqr)
Button_exit = Button(root, text="Exit", padx=10, pady=7, command=button_exit)

#Put buttons on screen
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_point.grid(row=4, column=1)
Button_remainder.grid(row=4, column=2)

Button_add.grid(row=1, column=3)
Button_subtract.grid(row=2, column=3)
Button_multiply.grid(row=3, column=3)
Button_divide.grid(row=4, column=3)


Button_power.grid(row=5, column=1, columnspan=1)
Button_sqr.grid(row=5, column=0, columnspan=1)

Button_clear.grid(row=1, column=4, columnspan=1)
Button_equal.grid(row=4, column=4, columnspan=1)
Button_open_paranthesis.grid(row=2, column=4)
Button_close_paranthesis.grid(row=3, column=4)


Button_exit.grid(row=0, column=3)


# Create a main loop
root.mainloop()
