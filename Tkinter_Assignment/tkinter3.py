from tkinter import *

Win= Tk()
lst = Listbox(Win, height = 3)
lst.pack()
lst.insert(END, 'First Entry')
lst.insert(END, 'Second Entry')
lst.insert(END, 'Third Entry')
lst.insert(END, 'Fourth Entry')
sb= Scrollbar(Win, orient = VERTICAL)
sb.pack(side = LEFT, fill = Y)
sb.configure(command = lst.yview)
lst.configure(yscrollcommand = sb.set)

