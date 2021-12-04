#Python version  3.9.7
#Author: Swarnali Satpathy
#Purpose: Creating a phonebook application.

#Importing tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox


#importing other useful methods
import phonebook_gui
import phonebook_func

#Creating class which inherits tk class Frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        self.master.config(bg='#FDF2E9')
        self.master.title ('The Tkinter Phonebook')
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        phonebook_func.center_window(self,500,300)
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.main()

    
    




