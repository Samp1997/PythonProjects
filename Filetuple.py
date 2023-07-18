import sqlite3

conn = sqlite3.connect('Files.db')

#creating the table 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT, \
        col_fileType TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('Files.db')
#list of tuple file names 
files_tuple = ('information.docx', 'Hello.txt', 'myimage.png', 'mymovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


for x in files_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fileType) VALUES (?)", (x,))
            print(x)


conn = sqlite3.connect('Files.db')





