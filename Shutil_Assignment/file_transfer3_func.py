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
