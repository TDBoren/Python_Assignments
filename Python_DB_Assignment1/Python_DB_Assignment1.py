import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data,pdf','myPhoto.jpg')




conn = sqlite3.connect('Files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('Files.db')

with conn:
    for file in fileList:
        if file.endswith(".txt"):
            cur = conn.cursor()
            cur.execute("""INSERT INTO tbl_Files(col_fileList) VALUES(?)""", (file,))
            conn.commit()
conn.close()

conn = sqlite3.connect('Files.db')                        

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_Files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[1])
        print(msg)
conn.close()

                        
