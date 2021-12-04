import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import studentTracking_gui
import studentTracking


def ask_quit(self):
    if messagebox.askokcancel('Exit Pragram','OK to exit application?'):
        self.master.destroy()
        os._exit(0)


#Creating the database
def create_db(self):
    conn = sqlite3.connect('students.db')
    with conn:
        cur=conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_students(\
        ID PRIMARY KEY INTEGER AUTOINCREMENT,\
        stu_fName TEXT ,\
        stu_lName TEXT ,\
        stu_grade TEXT\
        );')
        conn.commit()
    conn.close()


#Deffining the adding method
def onSubmit(self):
    var_fName= self.text_fname.get().strip().title() #Normalization of input data.
    var_lName= self.text_lname.get().strip().title()
    var_grade = self.text_grade.get().strip().title()
    var_fullName = ('{} {}'.format(var_fName,var_lName))
    if (len(var_fName)>0 and len(var_lName)>0 and len(var_grade)>0):
        conn= sqlite3.connect('students.db')
        with conn:
            cur= conn.cursor()
            cur.execute('INSERT INTO tbl_students (stu_fName,stu_lName,stu_grade) VALUES (?,?,?)',(var_fName,var_lName,var_grade))
            
        conn.commit()
        conn.close()
        messagebox.showinfo('Submitted:', 'Your informations submitted sucessfully')
        onClear(self)
    
    else:
        messagebox.showerror('Error:','Please fill all the required field')


def onClear(self):
    self.text_fname.delete (0,END)
    self.text_lname.delete (0,END)
    self.text_grade.delete (0,END)

        
       

 
    





if __name__ == "__main__":#this is a pass so that only the main program runs.
    pass





