import tkinter.filedialog
from tkinter import *
import shutil
from datetime import datetime, timedelta
import os

import file_transfer3_func


#creating the GUI
Win= Tk()
Win.title("Check Files")
Win.minsize (200,150)


btn1 = Button(Win, text="Browse", command = lambda:file_transfer3_func.pickSourceDir())#onclick can browse the folder.
btn1.pack(padx=(0,0), pady=(10,0))

source_dir= Entry(Win)
source_dir.pack(padx=(0,0),pady=(5,0))


btn2 =Button (Win, text= "Browse", command = lambda:file_transfer3_func.pickDestDir())#onclick can see the copied file list.
btn2.pack(padx=(0,0), pady=(5,0))

destination_dir= Entry(Win)
destination_dir.pack(padx=(0,0),pady=(5,0))


btn3 = Button(Win, text="Check files", command = lambda:file_transfer3_func.moveFiles())#onclick can move the files.
btn3.pack(padx=(0,0), pady=(5,0))


Win.mainloop()


















    
