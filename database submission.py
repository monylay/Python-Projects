

import sqlite3

#create the database and table

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()

    #create a table to store the file names
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
    conn.commit()

conn.close()


#File names from assignment

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#add .txt files to the database

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()

    #go through every file in fileList
    for file in fileList:

        #check if the file ends with .txt
        if file.endswith('.txt'):

            #add the file name to database
            cur.execute(
                "INSERT INTO tbl_files(file_name) VALUES (?)",(file,)
            )
    conn.commit()
conn.close()

#print the .txt files from the database

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()

    #get the file name from the database
    cur.execute("SELECT file_name FROM tbl_files")

    varFiles = cur.fetchall()

    #print each file name

    print("Text files:")

    for item in varFiles:
        print(item[0])
conn.close()

