import time
X = 10
print ("X (10) is not euqal to 15:")
time.sleep (1)
print (X!=15)
print ("X is greater than or equal to 15")
time.sleep (1)
print (X>=15)
if (X<15):
    print ("X is not equal to or greater than 15")
    time.sleep (1)
number=25
if number == 15:
    print ("25 is not equal to 15")
else:
    print ("The number is 25")
    time.sleep (.5)
counter=25
print (counter)
time.sleep(.5)
counter=counter+5
print (counter)
time.sleep(.5)
counter=counter-28
print (counter)
time.sleep(.5)
counter=counter*2
print (counter)
time.sleep (.5)
counter=counter/3
print (counter)
time.sleep (.5)
for counter in range (2,6):
    print (counter)
    time.sleep (.5)
for counter in range (10,4,-1):
    print (counter)
    time.sleep (.5)
while counter <22:
    print (counter+2)
    counter=counter+4
    time.sleep(0.5)
list = ['a','b','c','d','e','f','g','etc.']
print (list)
time.sleep (.5)
dictionary = {'Apple':'Fruit','Bush':'Plant','Carrot':'Vegetable'}
print (dictionary)
time.sleep (1)
print ("Now we shall add 'dog' to the dictionary.")
time.sleep (.5)
dictionary['Dog']='Animal'
print (dictionary)
time.sleep (.5)
del dictionary ['Apple']
print ("Now you can see we deleted apple from the dictionary.")
print (dictionary)
