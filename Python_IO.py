import OS

def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

def writeData():
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()
