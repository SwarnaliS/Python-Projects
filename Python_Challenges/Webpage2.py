import webbrowser
from tkinter import *

import webbrowser

#Creating the webpage
def web_browser():
    f = open ('new.html', 'w')
    txt = source.get()
    message = """<html>
            <body>
               %s
            </body>
            </html>""" % txt
    f.write( message )
    f.close()
    webbrowser.open_new_tab("file:///C:/Users/Swarnali/Desktop/Tech_Academy_Github/Python-Projects/Python_Challenges/new.html")



#crating the tkinter window
Win = Tk()
source= StringVar()# setting the text inside the text widget as a stringvar
#Main frame cration
Win.minsize(250,150)
Win.maxsize (250,150)
Win.title ('Test')
Win.config(bg='Black')

#text entry widget
Win.text= Entry (Win, textvariable = source, bg='gray')
Win.text.grid (row=0, column=0, padx=(50,0),pady=(50,0))

#button widget with a command, onclick it will open the webpage with the text entered
Win.btn = Button (Win, text = 'Click', bg='gray', command = lambda: web_browser() )
Win.btn.grid(row=1, column = 0, padx = (50,0), pady= (10,0))





Win.mainloop()
