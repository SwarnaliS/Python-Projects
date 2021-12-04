from tkinter import *

Win=Tk()

f= Frame (Win)
b1 = Button(f,text='One')
b2 = Button(f, text = 'Two')
b3 = Button (f, text = 'Three')
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)

l = Label(Win,text='This is a label for all buttons')
l.pack()
f.pack()

b1.configure(text = 'Uno')

def btn1():
    print ('Button One is pushed')

b1.configure(command =btn1)
