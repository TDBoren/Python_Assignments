
from tkinter import *
from tkinter import filedialog

class Application():
    def __init__(self):
        self.root = Tk()
        self.sourcefile = ""
        self.targetfile = ""

        sourceDirectory = Entry(self.root, width=10)
        targetDirectory = Entry(self.root, width=10)
        selectSource = Button(self.root, text="Select Source", command=self.select_source)
        selectTarget = Button(self.root, text="Select Target", command=self.select_target)
        startSync = Button(self.root, text="Start", command=self.synchronize)

        sourceDirectory.grid(row=0, column=0)
        targetDirectory.grid(row=0, column=5)
        selectSource.grid(row=0, column=1)
        selectTarget.grid(row=0, column=10)
        startSync.grid(row=1, column=2)

        self.root.mainloop()

    def select_source(self):
        source = filedialog.askdirectory(title="Select Source")
        self.sourceDirectory.insert(0, source)
        self.sourcefile = source

    def select_target(self):
        target = filedialog.askdirectory(title="Select Target")
        self.targetDirectory.insert(1, target)
        self.targetfile = target

    def synchronize(self):
        dirsync.sync(self.sourcefile, self.targetfile, "sync", verbose = True)
        dirsync.sync(self.sourcefile, self.targetfile, "update", verbose = True)

Application()
