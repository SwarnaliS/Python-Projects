#Impoted sqlite to use
import sqlite3
#Created the file
fileList = ['information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
#Creating the database
conn = sqlite3.connect ('dataBase.db')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_file(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    file_name TEXT\
    )')
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute('INSERT INTO tbl_file (file_name) VALUES (?)',(file,))
            print(file)
    conn.commit()
conn.close()
