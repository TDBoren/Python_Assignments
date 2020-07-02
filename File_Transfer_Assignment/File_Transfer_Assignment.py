import shutil
import os.path, time
import datetime
from datetime import timedelta, date
import tkinter
from tkinter import *
from tkinter import filedialog

class ParentWindow(Frame): 
    def __init__ (self, master):
        Frame.__init__ (self)
        self.sourceFile = ""
        self.targetFile = ""
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(850, 250))
        self.master.title("Check Files")
        self.master.config(bg='lightgray')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
 
        self.selectSource = Button(self.master, text = 'Browse... ', font=("Helvetica", 16), width = 15, height = 1, command = self.select_source)
        self.selectSource.grid(row=0,column=0, padx=(30,0),pady=(10,0))

        self.selectTarget = Button(self.master, text = 'Browse... ', font=("Helvetica", 16), width = 15, height = 1, command = self.select_target)
        self.selectTarget.grid(row=1,column=0, padx=(30,0),pady=(10,0))
        
        self.SourceDirectory = Entry(self.master, text=self.varBrowse1, font=("Helvetica", 16), fg = 'black', width = 50)
        self.SourceDirectory.grid(row=0, column=1, padx=(10,0),pady=(10,0))
        
        self.TargetDirectory = Entry(self.master, text=self.varBrowse2, font=("Helvetica", 16), fg = 'black', width = 50)
        self.TargetDirectory.grid(row=1,column=1, padx=(10,0),pady=(10,0))

        self.btnCheck = Button(self.master, text='Check for files...', font=("Helvetica", 16), width = 15, height = 3, command = self.file_transfer)
        self.btnCheck.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=NE)
        
        self.btnClose = Button(self.master, text='Close Program', font=("Helvetica", 16), width = 15, height =3, command = self.cancel)
        self.btnClose.grid(row=2, column=1, padx=(30,0), pady=(30,0), sticky=NE)

    
    def select_source(self):
        global source
        source = filedialog.askdirectory(title="Select Source")
        self.SourceDirectory.insert(0, source)

    def select_target(self):
        global target
        target = filedialog.askdirectory(title="Select Destination")
        self.TargetDirectory.insert(0, target)

    def file_transfer(self):
        todaysDate = datetime.datetime.now()
        fileList =os.listdir(source)
        for file in fileList:
            print("file: ", file)
            fpath = os.path.join(source, file)
            print("fpath: ", fpath)
            modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(fpath))
            newDate = todaysDate - timedelta(days=1)
            if modifyDate > newDate:
                shutil.move(source + "/" + file, target)
                
                
    def cancel(self):
        self.master.destroy()
        
    
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


