num1=12
key =True

if num1 == 12:
    if key:
        print ("Num1 is equal to Twelve and they have the key!")
elif num1<12:
    print("Num1 is less than Twelve and they do not have the key!")
else:
    print("Num1 is not equal to Twelve!")

print(bool(15))
x = 200
print(isinstance(x,int))
i=0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1
i=0
while i<10:
    print("{} iteration through the loop".format(i))
    i += 1
name = 'Python'
print(len(name))
for i in enumerate(name):
    print(i)

mySentence = "loves the color"
color_list = ['red','blue','green','pink','teal','black']
def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst
lst = color_function("Sally")
for i in lst:
    print(i)
    
def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("You need to provide your name!")
        elif name == 'Sally':
            print("Sally, you may not use thios software")
        else:
            go = False
            
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

def getSum(num1,num2):
    answer = num1 + num2
    print("the answer is {}.".format(answer))
myAdd = getSum

myList = ('Pink','Black','Green','Teal','Red','Blue') 
for color in myList:
     if color == 'Black':
         print('The chosen color is Green.')
