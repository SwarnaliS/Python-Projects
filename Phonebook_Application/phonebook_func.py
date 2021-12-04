import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

import phonebook_main
import phonebook_gui

#Centering the window on the user's system
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()   #Getting user's system width and height info.
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y)) #Placing the app centered on the user's screen.

#Defining the exit method
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Do you want to exit the application?"):
        self.master.destroy()#this will close the app.
        os._exit(0)#This will release all the memory.
#Creating the database.
def create_db(self):
    conn= sqlite3.connect('phonebook.db')
    with conn:
        cur=conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_phonebook(\
        ID PRIMARY KEY INT AUOINCREMENT,\
        col_fname TEXT ,\
        col_lname TEXT,\
        col_fullName TEXT,\
        col_phone TEXT,\
        col_email )')
        conn.commit()
    conn.close()
    first_run(self)
#Defining the method with a dummy data when the db runs first time
def first_run(self):
    data = ('John','Doe','John Doe','111-111-1111','john.doe@email.com')
    conn = sqlite3.connection('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count <1:
            cur.execute('INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullName,col_phone,col_email) VALUES(?,?,?,?,?)',data)
            conn.commit()
    conn.close()
def count_records(cur):
    count =''
    cur.execute('SELECT COUNT(*) FROM tbl_phonebook')
    count = cur.fetchone()[0]
    return cur,count
#Select item in listbox
def onSelect(self,event):
    varlist = event.widget
    select= varlist.curselection()[0]
    value = varlist.get(select)
    conn =sqlite3.connection('phonebook.db')
    with conn:
        cur= conn.cursor()
        cur.execute('SELECT col_fname,col_lname,col_fullName,col_phone,col_email from tbl_phonebook WHERE col_fullName = (?)', [value])
        varBody= cursor.fetchall()#This will return a tuple
        #Slicing the data into parts
        for data in varBody:
            self.text_fname.delete(0,End)
            self.text_fname.insert(0,data[0])
            self.text_lname.delete(0,End)
            self.text_lname.insert(0,data[1])
            self.text_phone.delete(0,End)
            self.text_phone.insert(0,data[2])
            self.text_email.delete(0,End)
            self.text_email.insert(0,data[3])
#Adding to the list
def addToList(self):
    var_fname = self.text_fname.get() #Getting data from user
    var_lname = self.text_lname.get()
    var_phone = self.text_phone.get().strip()#getting data from user and normalizing
    var_email = self.text_email.get().strip()
    var_fullNmae = ('{} {}'.format(var_fname,var_lname))
    print('Full Name: {}'.format(var_fullName))
    #normalizing data from user
    var_fname = self.text_fname.strip()
    var_lname = self.text_lname.strip()
    var_fname = self.text_fname.title()
    var_lname = self.text_lname.title()
    if (len(var_fname >0) and len(var_lname >0) and len(var_phone >0) and len(var_email >0)):
        conn = sqlite3.connection('phonebook.db')
        with conn:
            cursor=conn.cursor()
            #Checking if the name exists
            cursor.execute('SELECT COUNT(col_fullName) from tbl_phonebook WHERE col_fullName ="{}"'.format(var_fullName))
            count = cursor.fetchone()[0]
            chkName= count
            if chkName==0: #If the name does not exists
                cursor.execute('INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullName,col_phone,col_email) VALUES (?,?,?,?,?)',(var_fname,var_lname,var_fullNmae,var_phone,var_email))
                self.lstList1.insert(END, var_fullName)
                onClear(self) # Clear all the text boxes
            else:
                messagebox.showerror('Name Error:','"{}" already exixts in the phonebook. Please choose a different name'.format(var_fullName))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing text error:','PLease ensure that there is data in all four fields')
def onDelete(self):
    var_select= self.lstList1.get(self.lstList1.curselect()) #Defining list box's selected value
    conn = sqlite3.connection('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cur.execute('SELECT COUNT(0) FROM tbl_phonebook')
        count = fetchone()[0]
        if count>1:
            confirm = messagebox.askokcancel('Delete Confirmation:',"All information associated with {}\nWill be permanently deleted.\nProcced with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connection('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cur.execute('DELETE FROM tbl_phonebook WHERE col_fullName = {}'.format(var_select))
                onDeleted(self)
                conn.commit()
            else:
                confirm = messagebox.showerror('Last record error:','{} is the last record in the database and can not be deleted at this time. Please add another record first before you delete {}'.format(var_select))
#Clearing the record from database
def onDeleted(self):
    self.text_fname.delete(0, END)
    self.text_lname.delete(0, END)
    self.text_phone.delete(0, END)
    self.text_email.delete(0, END)
    #updating the listbox
    try:
        index= self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass
def onClear(self):
    self.text_fname.delete(0, END)
    self.text_lname.delete(0, END)
    self.text_phone.delete(0, END)
    self.text_email.delete(0, END)
    
def onRefresh(self): #On refresh, refreshing the listbox
    self.lstList1.delete(0,END)
    conn = sqlite3.connection('phonebook.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute('SELECT COUNT(0) FROM tbl_phonebook')
        count = fetchone()[0]
        i=0
        while i<count:
            cursor.execute('SELECT col_fullName FROM tbl_phonebook')
            varlist = fetchall()[i]
            for item in varlist:
                self.lstList1.insert(0,str(item))
                i= i+1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showerror('Selection error:','No name was selected from the listbox.\nCancelling the update request')
        return
    var_phone = self.text_phone.get().strip()#normalizing data for data integrity
    var_email = self.text_email.get().strip()
    if(len(var_phone > 0) and len(var_email > 0 )):
        conn = sqlite3.connection('phonebook.db')
        with conn:
            cursor= conn.cursor()
            cur.execute('SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = {}'.format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute('SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = {}'.format(var_email))
            count = cur.fetchone()[0]
            print(count2)
            if count ==0 or count2==0:
                response = messagebox.askokcancel('Update Request','The following changes {} and {} will be implemented for {},\nProcced with the update request?'.format(var_phone,var_email.var_fullName))
                print(response)
                if response:
                    with conn:
                        cursor= conn.cursor()
                        cursor.execute('UPDATE tbl_phonebook SET col_phone = {}, col_email = {} WHERE col_fullName = {}'.format(var_phone,var_email,var_value))
                        onClear(self)
                    conn.commit()
                else:
                    messagebox.showinfo('Cancel Request', 'No changes have been made to {}'.format(var_value))
            else:
                messagebox.showinfo('NO changes detected')
            onClear(self)
        conn.close()
    else:
        messagebox.showinfo('Missing Information:','Please select a name from the list\nThen edit the phone or email information')
    onClear(self)


            
            
        
        


                
    
    
    
        

        
                
                
    
