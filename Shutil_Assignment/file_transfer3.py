from tkinter import *
import shutil
from datetime import datetime, timedelta
import os

#creating the GUI
Win= Tk()
Win.title("Check Files")
Win.minsize (200,150)
Win.minsize (200,150)

#Creating the file list to browse
def list_of_files():
    source = "/Users/Swarnali/Desktop/folder B/"
    destination = "/Users/Swarnali/Desktop/folder A/"
    files = os.listdir(source)
    print (files)

#copying files
def copied_files():
    source = "/Users/Swarnali/Desktop/folder B/"
    destination = "/Users/Swarnali/Desktop/folder A/"
    files = os.listdir(source)
    for i in files:
        shutil.copy (source+i, destination)
        print (i)

#creating buttons and text entries    
Win.btn1 = Button(Win, text="File check", command= lambda: list_of_files())#onclick can browse the folder.
Win.btn1.pack(padx=(0,0), pady=(20,0))
Win.btn2 =Button (Win, text= "Copied files", command = lambda: copied_files())#onclick can see the copied file list.
Win.btn2.pack(padx=(0,0), pady=(5,0))
Win.text1= Entry(Win, text ="")
Win.text1.pack(padx=(0,0),pady=(5,0))
Win.text2= Entry(Win, text ="")
Win.text2.pack(padx=(0,0),pady=(5,0))




    
