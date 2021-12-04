import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import studentTracking_gui
import studentTracking_func

class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        self.master = master
        Frame.__init__(self,master, *args, **kwargs)

        self.master.minsize (400,200) #Defining the maater frame
        self.master.maxsize (400,200)
        self.master.title ('Student Tracker')
        self.master.config (bg='light gray')
        self.master.protocol ("WM_DELETE_WINDOW",lambda: studentTracking_func.ask_quit(self))
        studentTracking_gui.load_gui(self)
        studentTracking_func.create_db(self)
        studentTracking_func.onSubmit(self)
        
        
        




    
        

        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
