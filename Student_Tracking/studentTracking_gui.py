import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import studentTracking
import studentTracking_func


def load_gui(self):
    self.text_fname = tk.Entry(self.master,text = '',bg='white')
    self.text_fname.grid(row = 1, column =1 ,padx =(0,0) , pady=(10,0),sticky=N+E )
    self.text_lname = tk.Entry(self.master,text = '',bg='white')
    self.text_lname.grid(row =2 , column =1 ,padx =(0,0) , pady=(10,0),sticky = N+E)
    self.text_grade = tk.Entry(self.master,text = '',bg='white')
    self.text_grade.grid(row =3 , column = 1,padx =(0,0) , pady=(10,0),sticky =S+E)

    self.label_fname = tk.Label(self.master, text = 'First Name:',bg='lightgray')
    self.label_fname.grid(row =1 , column = 0,padx =(0,10) , pady=(10,0), sticky = N+E)
    self.label_lname = tk.Label(self.master, text = 'Last Name:',bg='light gray')
    self.label_lname.grid(row = 2, column =0 ,padx =(0,10) , pady=(10,0),sticky = N+E)
    self.label_grade = tk.Label(self.master, text = 'Grade:', bg= 'lightgray')
    self.label_grade.grid(row = 3, column =0 ,padx =(0,10) , pady=(10,0), sticky= S+E) 

    self.btn_add = tk.Button(self.master, text = 'Submit', bg='darkgray', command = lambda: studentTracking_func.onSubmit(self))
    self.btn_add.grid(row = 3, column =2 ,padx =(30,20) , pady=(10,0),sticky= S+E)
    self.btn_Delete = tk.Button(self.master, text = 'Delete', bg='darkgray', command= lambda:studentTracking_func.onDelete(self) )
    self.btn_Delete.grid(row = 3, column =3 ,padx =(0,0) , pady=(10,0), sticky= S+W)

    self.label_title = tk.Label(self.master, text = 'Student Information', bg ='lightgray')
    self.label_title.grid(row =0 , column = 2,padx =(0,0) , pady=(0,0) )

    

    if __name__ == "__main__":#this is a pass so that only the main program runs.
        pass

