from tkinter import *
from tkinter import messagebox
from tkinter import font

top = Tk()
top.geometry("200x100")

# def_font = font.nametofont("TkDefaultFont")
myfont = font.Font(family='Helvetica', size=10, weight='bold')
top.option_add("*Font", myfont)

def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()