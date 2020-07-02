import glob
import os
import datetime
import shutil

def GetFileList(path, type):
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)

originPath = "C:\Python27\Origin Folder\\"
destinationPath = "C:\Python27\Dest Folder\\"
fileType = ".txt"

# Create list of text filenames in Origin folder
fileList = GetFileList(originPath, fileType)

for file in fileList:
    # Get last modified date and today's date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.todayc
    
    # If modified within last 24 hours, then copy to destination folder
    modifyDateLimit = modifyDate + datetime.timedelta(days=1)

    # If the file was edited less then 24 hours ago then copy it
    if modifyDateLimit > todaysDate:
        shutil.copy2(file, destinationPath + filename)



def file_transfer():
source = 'C:/Users/Troy/Documents/GitHub/Folder_A/' ##(will be changed to user selected directory)
destination = 'C:/Users/Troy/Documents/GitHub/Folder_B/'  ##(will be changed to user selected directory)
## create variable for today's date
files = os.listdir(source)
for i in files:
## create an absolute file path to each element (i) in files and assign it to a variable
## get the modified time for the above variable and assign that to a variable (because it's in a loop it will show you when each of the files was modified - use the print method to see how this is working)
## get the modified date from the above modified time variable
## create variable that adds one day to the modified time
if ## variable in one day is greater than today's date variable
shutil.move(absolute file path variable, destination)
