string1 ="First String"
print(string1)
string2 = """This string
is over
multiple lines"""
print(string2)
print(string2[2:5:7])
print(len(string2))
print(string1.strip())
print(string1.lower())
print(string2.upper())
x = "ing" in string2
print(x)
y = "ing" in string2
print(y)
c = string1 + string2
print(c)
txt = "I want to keep these \"quotes\" without having to debug this code."
print(txt)
print (10+5)
b=5
print(b)
m=4
n=6
print(m>n)
print(m<n or m==n)
print (m is n)
print (string1 in string2)
p=0
q=1
print(p^q)
animal=('zebra','alligator','giraffe','goat','ox')
listofAnimals=list(animal)
print(listofAnimals)
listofAnimals.append("honey boadger")
print(listofAnimals)
myString="Can I add to this Tuple?"
newString=list(myString)
print(newString)
newString=myString.split(" ")
print(newString)
list1=["First","Second","Third","Fourth","Fifth"]
print(list1)
for z in list1:
    print(z)
list1.append("Sixth")
print(list1)
copyList=list1.copy()
print(copyList)
list3= list1 + copyList
print(list3)
list4=list3.reverse()
print(list4)
tuple1=("Thousands","Hundreds","Tens","Ones")
for t in tuple1:
    print(tuple1)
c=tuple1.count("Hundreds")
print(c)
set1={"Set1","Set2","Set3","Set4","Set5"}
print(set1)
set1.add("Set6")
print(set1)
set1.remove("Set6")
print(set1)
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
gm = a.difference(b)
print(gm)
cardict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(cardict)
ford = cardict.get("model")
print(ford)
cardict["year"]=2020
print(cardict)
cardict["color"]="blue"
print(cardict)
child1 = {"name" : "David Ryan", "year" : 1994}
child2 = {"name" : "Candice Nicole", "year" : 1998}
child3 = {"name" : "Dawnesia Joanne", "year" : 1999}
mykids = {"child1" : child1, "child2" : child2, "child3" : child3}
print(mykids)
w = ('brand', 'model', 'year', 'color')
v = 0
cardict = dict.fromkeys(w, v)
print(cardict)
color = ['Red','Blue','Green','Orange','Pink','Yellow','Black','White']
print(type(color))
print(10 > 9)
print(10 == 9)
print(10 < 9)




