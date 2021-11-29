import tkinter.filedialog
from tkinter import *
import shutil
from datetime import datetime, timedelta
import os


def pickSourceDir():
    myDir = tkinter.filedialog.askdirectory()
    source_dir.delete(0,END)
    source_dir.insert(0,myDir)


def pickDestDir():
    myDir = tkinter.filedialog.askdirectory()
    destination_dir.delete(0,END)
    destination_dir.insert(0,myDir)


def moveFiles():
    source = source_dir.get()
    destination = destination_dir.get()
    source_files = os.listdir(source)
    for i in source_files:
        file_path = os.path.join (source,i)
        hours_ago_24 = datetime.datetime.now()-timedelta(hours = 24)
        modification_time =  os.path.getmtime(file_path)
        date_time_of_files = datetime.datetime.fromtimestamp(modification_time)
        if hours_ago_24 > date_time_of_file:
            shutil.move(source+ '/' + i, destination)
            print(i + 'was sucessfully transfered')



#creating the GUI
Win= Tk()
Win.title("Check Files")
Win.minsize (200,150)
Win.minsize (200,150)
#creating buttons and text entries    
Win.btn1 = Button(Win, text="File check", command = lambda: pickSourceDir())#onclick can browse the folder.
Win.btn1.pack(padx=(0,0), pady=(20,0))
Win.btn2 =Button (Win, text= "Copied files", command = lambda : pickDestDir())#onclick can see the copied file list.
Win.btn2.pack(padx=(0,0), pady=(5,0))
Win.btn3 = Button(Win, text="Move files", command = lambda: moveFiles())#onclick can move the files.
Win.btn3.pack(padx=(0,0), pady=(5,0))

Win.text1= Entry(Win, text ="")
Win.text1.pack(padx=(0,0),pady=(5,0))







    
