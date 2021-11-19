from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Hello!")



# img=PhotoImage(file='test.jpg')
# Label(root,image=img).pack()
my_img = ImageTk.PhotoImage(Image.open("test.png"))
my_label1 = Label(image=my_img)
# my_label1.pack


# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)

# img = ImageTk.PhotoImage(Image.open("test.png"))  # PIL solution
# canv.create_image(20, 20, anchor=NW, image=img)



root.mainloop()