import tkinter
from tkinter import *
from tkinter import messagebox

Win = Tk()
Win.title ('Check files')
Win.minsize (400,200)
Win.maxsize (400,200)
Win.btn1 = Button (Win,text = 'Browse..', bg = 'darkgray', width = 10, height = 1)
Win.btn1.grid(row = 1, column = 0,padx =(10,0), pady= (50,0))
Win.btn2 = Button (Win,text = 'Browse..', bg = 'darkgray', width = 10, height = 1)
Win.btn2.grid(row = 2, column = 0,padx =(10,0), pady= (10,0))
Win.btn3 = Button (Win,text = 'Check Files..', bg = 'darkgray', height = 2)
Win.btn3.grid(row = 3, column = 0,padx =(10,0), pady= (10,0))





Win.text1 = Entry (Win, bg='White', text = '')
Win.text1.grid (row = 1, column = 1, columnspan=2, padx= (10,20),pady = (50,0))
Win.text2 = Entry (Win, bg='White', text = '')
Win.text2.grid (row = 2, column = 1, columnspan=2, padx= (10,20),pady = (10,0))

Win.btn4 = Button (Win,text = 'Close Program', bg = 'darkgray', height = 2)
Win.btn4.grid(row = 3, column = 10,padx =(0,20), pady= (0,0), sticky =E)
        
        



