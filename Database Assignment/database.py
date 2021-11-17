#Importing qlite to be able to work with database using Python
import sqlite3

#creating the database
conn = sqlite3.connect('mydb.db')
with conn:
    cur = conn.cursor()
    #Creating thde table
    cur.execute ('CREATE TABLE IF NOT EXISTS tbl_file (\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    file_name TEXT, \
    file_type TEXT \
    )')
    conn.commit()
conn.close()

#Inserting values
conn = sqlite3.connect('mydb.db')
with conn:
    cur = conn.cursor()
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('information','.docx'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('Hello','.txt'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('myImage','.png'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('myMovie','.mpg'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('World','.txt'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('data','.pdf'))
    cur.execute ('INSERT INTO tbl_file(file_name,file_type) VALUES (?,?)',\
    ('myPhoto','.jpg'))

    conn.commit()
conn.close()

#Serching for the file names with .txt extension
conn = sqlite3.connect('mydb.db')
with conn:
    cur = conn.cursor()
    cur.execute ('SELECT file_name,file_type FROM tbl_file WHERE file_type =".txt"')
    varfile = cur.fetchall()
    for i in varfile:
        msg = 'These are the .txt files: {} {}'.format(i[0],i[1])
        print (msg)
        conn.commit()
conn.close()

   
    
    
