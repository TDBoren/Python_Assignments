import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data,pdf','myPhoto.jpg')

def getText_Files():
    if "*.txt" in fileList:
        return Text_File_List
        print(Text_File_List)


conn = sqlite3.connect('Files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT \
        )")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('information.docx')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('Hello.txt')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('myImage.png')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('myMovie.mpg')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('World.txt')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('data.pdf')"),
    cur.execute("INSERT INTO tbl_Files(col_fileList) VALUES ('myPhoto.jpg')")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileList FROM tbl_Files WHERE col_fileList = '*.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
    print(msg)
    
conn.close()
    
