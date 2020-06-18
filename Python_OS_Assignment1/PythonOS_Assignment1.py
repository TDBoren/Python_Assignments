
import os
import sys
import time

path1 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path1)
local_time1 = time.ctime(modification_time)

path2 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path2)
local_time2 = time.ctime(modification_time)

path3 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path3)
local_time3 = time.ctime(modification_time)

path4 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path4)
local_time4 = time.ctime(modification_time)

path5 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path5)
local_time5 = time.ctime(modification_time)

path6 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path6)
local_time6 = time.ctime(modification_time)

path7 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path7)
local_time7 = time.ctime(modification_time)

path8 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path8)
local_time8 = time.ctime(modification_time)

path9 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path9)
local_time9 = time.ctime(modification_time)

path10 = ('C:/Users/Troy/Documents/Python_OS_Assignment1/OS_String1.txt')
modification_time = os.path.getmtime(path10)
local_time10 = time.ctime(modification_time)


path1 = ('C:/')
path2 = ('Users/')
path3 = ('Troy/')
path4 = ('Documents/')
path5 = ('Python_OS_Assignment1/')
file1 = ('OS_String1.txt')
file2 = ('OS_String2.txt')
file3 = ('OS_String3.txt')
file4 = ('OS_String4.txt')
file5 = ('OS_String5.txt')
file6 = ('OS_String6.txt')
file7 = ('OS_String7.txt')
file8 = ('OS_String8.txt')
file9 = ('OS_String9.txt')
file10 = ('OS_String10.txt')

print(os.path.join(path1,path2,path3,path4,path5,file1,"\nLast time the file was modified", local_time1))
print(os.path.join(path1,path2,path3,path4,path5,file2,"\nLast time the file was modified", local_time2))
print(os.path.join(path1,path2,path3,path4,path5,file3,"\nLast time the file was modified", local_time3))
print(os.path.join(path1,path2,path3,path4,path5,file4,"\nLast time the file was modified", local_time4))
print(os.path.join(path1,path2,path3,path4,path5,file5,"\nLast time the file was modified", local_time5))
print(os.path.join(path1,path2,path3,path4,path5,file6,"\nLast time the file was modified", local_time6))
print(os.path.join(path1,path2,path3,path4,path5,file7,"\nLast time the file was modified", local_time7))
print(os.path.join(path1,path2,path3,path4,path5,file8,"\nLast time the file was modified", local_time8))
print(os.path.join(path1,path2,path3,path4,path5,file9,"\nLast time the file was modified", local_time9))
print(os.path.join(path1,path2,path3,path4,path5,file10,"\nLast time the file was modified", local_time10))
